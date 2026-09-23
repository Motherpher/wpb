from __future__ import annotations

import re
from datetime import datetime, timezone

import yaml
from dateutil import parser as dtparser
from rapidfuzz.fuzz import token_set_ratio

from .models import Job


LANE_TITLE_TERMS = {
    "core": [
        "journalist", "reporter", "writer", "skribent", "editor", "redaktör",
        "editorial", "communications", "communication", "kommunikatör", "press",
        "public affairs", "pr ", "researcher", "research assistant", "content writer",
        "content producer", "copywriter", "translator", "localisation", "localization",
        "media", "communications manager", "communications officer"
    ],
    "adjacent": [
        "communications", "communication", "content", "copywriter", "editorial",
        "coordinator", "koordinator", "project coordinator", "projektkoordinator",
        "research coordinator", "research assistant", "community manager",
        "media monitoring", "communications assistant", "translator", "localisation",
        "localization", "producer", "program coordinator", "programme coordinator"
    ],
    "bridge": [
        "administrative", "administratör", "admin", "customer support", "kundtjänst",
        "receptionist", "event", "museivärd", "museum", "servicevärd", "service",
        "butik", "retail", "booking", "data entry", "content moderation",
        "virtual assistant", "transcription", "assistant", "support"
    ],
}

MISMATCH_TITLE_TERMS = [
    "software engineer", "backend engineer", "frontend engineer", "full stack",
    "developer", "devops", "data engineer", "machine learning engineer",
    "account executive", "sales executive", "sales manager", "sales director",
    "general counsel", "legal counsel", "attorney", "lawyer",
    "clinical", "dentist", "physician", "nurse", "medical doctor",
    "security analyst", "security engineer", "cybersecurity",
    "finance director", "financial controller", "accountant",
    "product director", "product manager", "engineering manager",
]

REMOTE_US_PATTERNS = [
    "remote - united states", "remote - us", "remote us", "remote, us",
    "united states only", "us only", "u.s. only", "must be based in the us",
    "must be located in the united states", "location: remote, us",
    "location: remote - us", "remote (u.s.)", "remote (us)",
]

REMOTE_EU_PATTERNS = [
    "europe", "european union", "eu only", "emea", "cet", "cest",
    "remote europe", "within europe", "based in europe"
]

TITLE_LANGUAGE_TERMS = [
    "danish", "german", "french", "finnish", "norwegian", "dutch",
    "italian", "spanish", "portuguese", "arabic", "czech", "hungarian"
]


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def candidate_terms(profile: dict) -> list[str]:
    terms = []
    pos = profile.get("positioning", {})
    terms += pos.get("primary_public_roles", [])
    terms += pos.get("evidence_domains", [])
    for cap in profile.get("verified_capabilities", []):
        terms.append(cap.get("label", ""))
    return [t.lower() for t in terms if t]


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[\wåäöé]+", (text or "").lower()) if len(w) > 3}


def _title_family_fit(title: str, lane_name: str) -> tuple[float, list[str]]:
    title_l = (title or "").lower()
    terms = LANE_TITLE_TERMS.get(lane_name, [])
    hits = [term for term in terms if term.strip() and term.strip() in title_l]
    if not hits:
        return 0.0, []
    longest = max(len(term.split()) for term in hits)
    score = 0.72 if longest == 1 else 0.92
    if len(hits) >= 2:
        score = min(1.0, score + 0.08)
    return score, hits


def _domain_mismatch(title: str, lane_name: str, positive_hits: list[str]) -> bool:
    title_l = (title or "").lower()
    if not any(term in title_l for term in MISMATCH_TITLE_TERMS):
        return False
    # Explicit lane-relevant title language overrides generic negative words.
    strong_positive = any(len(term.split()) >= 1 and term.strip() in title_l for term in positive_hits)
    return not strong_positive


def _geo_fit(job: Job, profile: dict) -> tuple[float, list[str]]:
    flags = []
    location = (job.location or "").lower()
    blob = job.search_blob[:5000]
    text = f"{location} {blob}"

    if "stockholm" in location:
        return 1.0, flags
    if any(x in location for x in ["sweden", "sverige", "stockholms län"]):
        return 0.92, flags
    # Platsbanken locations are Swedish even when country is omitted.
    if job.source == "platsbanken" and location:
        return 0.82, flags

    remote_signal = job.work_mode.lower() == "remote" if job.work_mode else False
    remote_signal = remote_signal or "remote" in location or "remote" in text or "distans" in text

    if remote_signal:
        if any(p in text for p in REMOTE_US_PATTERNS) or location in {"united states", "usa", "us"}:
            flags.append("remote-us-only-or-us-focused")
            return 0.12, flags
        if any(p in text for p in REMOTE_EU_PATTERNS):
            return 0.95, flags
        flags.append("remote-eligibility-needs-verification")
        return 0.68, flags

    targets = [x.lower() for x in profile.get("career_preferences", {}).get("target_geographies", [])]
    if any(t and t in location for t in targets if t not in {"sweden", "remote europe", "remote worldwide where legally eligible"}):
        return 1.0, flags

    if location:
        flags.append("location-needs-review")
        return 0.45, flags

    flags.append("location-unknown")
    return 0.55, flags


def _recency(job: Job) -> float:
    if not job.published:
        return 0.55
    try:
        d = dtparser.parse(str(job.published))
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        age = max(0, (datetime.now(timezone.utc) - d).days)
        return max(0.15, 1 - min(age, 60) / 70)
    except Exception:
        return 0.55


def triage(job: Job, lane_name: str, lane_cfg: dict, profile: dict, defaults: dict) -> Job:
    queries = lane_cfg.get("queries", [])
    blob = job.search_blob
    title = job.title or ""

    fuzzy_query_fit = max([token_set_ratio(title, q) / 100 for q in queries] or [0])
    family_fit, positive_hits = _title_family_fit(title, lane_name)
    title_fit = max(fuzzy_query_fit, family_fit)

    cterms = candidate_terms(profile)
    ctoken = set()
    for term in cterms:
        ctoken |= _tokens(term)
    jtoken = _tokens(blob)
    overlap = len(ctoken & jtoken) / max(1, min(18, len(ctoken)))
    evidence_fit = min(1.0, overlap * 1.7)

    positive_arrangement = [
        "remote", "distans", "hybrid", "part time", "part-time", "deltid",
        "temporary", "tidsbegränsad", "freelance", "vikariat"
    ]
    arrangement = 1.0 if any(x in blob for x in positive_arrangement) else 0.72

    geo, geo_flags = _geo_fit(job, profile)
    recency = _recency(job)

    flags = list(geo_flags)

    title_l = title.lower()
    if any(lang in title_l for lang in TITLE_LANGUAGE_TERMS):
        flags.append("language-title-requirement-unconfirmed")

    uncertainty_patterns = [
        ("language", ["native swedish", "modersmål svenska", "flytande svenska", "fluent swedish"]),
        ("licence", ["driver's licence", "körkort", "legitimation", "licensed"]),
        ("security", ["security clearance", "säkerhetsprövning", "säkerhetsklass"]),
    ]
    for flag, patterns in uncertainty_patterns:
        if any(p in blob for p in patterns):
            flags.append(f"{flag}-requirement-needs-verification")

    mismatch = _domain_mismatch(title, lane_name, positive_hits)
    if mismatch:
        flags.append("occupational-family-mismatch")

    # Title/role identity carries most of the score. Evidence overlap is supportive,
    # not allowed to turn a software/sales/legal role into a journalism match.
    raw = (
        55 * title_fit +
        15 * evidence_fit +
        10 * arrangement +
        15 * geo +
        5 * recency
    )

    if title_fit < 0.34:
        raw -= 24
        flags.append("weak-title-fit")
    if mismatch:
        raw -= 38
    if "remote-us-only-or-us-focused" in flags:
        raw -= 28
    if any(f.endswith("requirement-needs-verification") for f in flags):
        raw -= 4
    if "language-title-requirement-unconfirmed" in flags:
        raw -= 25

    job.triage_score = round(max(0, min(100, raw)), 1)
    job.lane = lane_name
    job.review_flags = list(dict.fromkeys(flags))
    job.triage_reasons = [
        f"title/role fit {round(title_fit*100)}%",
        f"candidate-evidence support {round(evidence_fit*100)}%",
        f"arrangement fit {round(arrangement*100)}%",
        f"geography/remote fit {round(geo*100)}%",
        f"recency signal {round(recency*100)}%",
    ]
    return job


def _keep(job: Job, lane_name: str) -> bool:
    if "occupational-family-mismatch" in job.review_flags:
        return False
    if "remote-us-only-or-us-focused" in job.review_flags:
        return False
    if "language-title-requirement-unconfirmed" in job.review_flags:
        return False
    minimum = {"core": 55, "adjacent": 52, "bridge": 48}.get(lane_name, 52)
    return job.triage_score >= minimum


def rank_jobs(jobs: list[Job], lane_name: str, lane_cfg: dict, profile: dict, defaults: dict) -> list[Job]:
    ranked = [triage(j, lane_name, lane_cfg, profile, defaults) for j in jobs]
    ranked = [j for j in ranked if _keep(j, lane_name)]
    return sorted(ranked, key=lambda j: (-j.triage_score, j.deadline or "9999", (j.title or "").lower()))
