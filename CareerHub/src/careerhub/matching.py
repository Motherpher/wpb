from __future__ import annotations

import re
from datetime import datetime, timezone

import yaml
from dateutil import parser as dtparser
from rapidfuzz.fuzz import token_set_ratio

from .models import Job


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
    return {w for w in re.findall(r"[\wåäöé]+", text.lower()) if len(w) > 3}


def triage(job: Job, lane_name: str, lane_cfg: dict, profile: dict, defaults: dict) -> Job:
    queries = lane_cfg.get("queries", [])
    blob = job.search_blob

    title_fit = max([token_set_ratio(job.title, q) / 100 for q in queries] or [0])
    cterms = candidate_terms(profile)
    ctoken = set()
    for t in cterms:
        ctoken |= _tokens(t)
    jtoken = _tokens(blob)
    overlap = len(ctoken & jtoken) / max(1, min(16, len(ctoken)))

    positive = ["remote", "distans", "hybrid", "part time", "deltid", "temporary", "tidsbegränsad", "freelance"]
    arrangement = 1.0 if any(x in blob for x in positive) else 0.7

    geo = 0.65
    targets = [x.lower() for x in profile.get("career_preferences", {}).get("target_geographies", [])]
    if "remote" in blob or "distans" in blob:
        geo = 1.0
    elif any(t in blob for t in targets if t not in {"sweden", "remote europe", "remote worldwide where legally eligible"}):
        geo = 1.0
    elif "sweden" in blob or "sverige" in blob:
        geo = 0.9

    recency = 0.6
    if job.published:
        try:
            d = dtparser.parse(str(job.published))
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone.utc)
            age = max(0, (datetime.now(timezone.utc) - d).days)
            recency = max(0.2, 1 - min(age, 60) / 75)
        except Exception:
            pass

    flags = []
    uncertainty_patterns = [
        ("language", ["native swedish", "modersmål svenska", "flytande svenska", "fluent swedish"]),
        ("licence", ["driver's licence", "körkort", "legitimation", "licensed"]),
        ("security", ["security clearance", "säkerhetsprövning", "säkerhetsklass"]),
    ]
    for flag, pats in uncertainty_patterns:
        if any(p in blob for p in pats):
            flags.append(f"{flag}-requirement-needs-verification")

    lane_weight = float(lane_cfg.get("weight", 1.0))
    raw = 45*title_fit + 30*min(1, overlap*2.2) + 10*arrangement + 10*geo + 5*recency
    if flags:
        raw -= min(12, 4*len(flags))
    job.triage_score = round(max(0, min(100, raw*lane_weight)), 1)
    job.lane = lane_name
    job.review_flags = flags
    job.triage_reasons = [
        f"title/query fit {round(title_fit*100)}%",
        f"candidate-evidence lexical overlap {round(min(1, overlap*2.2)*100)}%",
        f"arrangement fit {round(arrangement*100)}%",
        f"geography/remote fit {round(geo*100)}%",
        f"recency signal {round(recency*100)}%",
    ]
    return job


def rank_jobs(jobs: list[Job], lane_name: str, lane_cfg: dict, profile: dict, defaults: dict) -> list[Job]:
    ranked = [triage(j, lane_name, lane_cfg, profile, defaults) for j in jobs]
    return sorted(ranked, key=lambda j: (-j.triage_score, j.deadline or "9999", j.title.lower()))
