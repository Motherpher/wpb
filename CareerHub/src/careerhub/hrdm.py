from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from hashlib import sha1
from pathlib import Path

from .models import Job


def process_id(job: Job) -> str:
    seed = job.url or f"{job.company}|{job.title}"
    return f"HRDM-R-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{sha1(seed.encode()).hexdigest()[:8].upper()}"


def public_candidate_evidence(profile: dict) -> dict:
    return {
        "identity": {"name": profile["identity"]["name"]},
        "positioning": profile.get("positioning", {}),
        "verified_capabilities": profile.get("verified_capabilities", []),
        "education_public_evidence": profile.get("education_public_evidence", []),
        "language_evidence": profile.get("language_evidence", {}),
        "career_preferences": profile.get("career_preferences", {}),
        "verification_needed": profile.get("verification_needed", []),
    }


def build_packet(job: Job, profile: dict, lane: str) -> dict:
    return {
        "process_id": process_id(job),
        "mode": "HRDM-R-v6.3",
        "lane": lane,
        "job": job.full_dict(),
        "candidate_evidence": public_candidate_evidence(profile),
        "constraints": [
            "Run the complete canonical HRDM-R sequence in order.",
            "Do not invent candidate evidence.",
            "Separate job-ad facts from inference.",
            "Candidate Positioning may use only evidence supplied in this packet.",
            "Treat unknown language proficiency, current location and current employment as unknown.",
            "DoD diagnoses role deviation, not candidate quality.",
            "HCC must address overload, ambiguity, fairness, dignity and structural honesty.",
        ],
    }


def packet_prompt(packet: dict) -> str:
    return f"""You are running HRDM-R v6.3 for CareerHub.

Canonical sequence:
1 Ad/Text Intake
2 Signal Extraction
3 Key Words & Concepts
4 Hidden Need Reconstruction
5 Field Logic Reconstruction
6 FunctionCore Estimation
7 DoD Diagnostic
8 Likely Assessment Zones
9 Candidate Positioning Map
10 HCC Reverse Commentary

Use web research only for current public employer/role context. Do not use web search to invent or supplement candidate history.

Candidate evidence is bounded to the supplied packet. If evidence is absent, mark it unknown or gap.

Return the JSON schema supplied by the caller.

PACKET:
{json.dumps(packet, ensure_ascii=False, indent=2)}
"""


def run_ai_hrdm(packet: dict, schema_path: Path) -> dict | None:
    if not os.getenv("OPENAI_API_KEY"):
        return None
    try:
        from openai import OpenAI
    except Exception:
        return None

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    model = os.getenv("CAREERHUB_MODEL") or "gpt-5.4"
    client = OpenAI()
    response = client.responses.create(
        model=model,
        store=False,
        tools=[{"type": "web_search", "search_context_size": "medium"}],
        input=packet_prompt(packet),
        text={
            "format": {
                "type": "json_schema",
                "name": "careerhub_hrdm",
                "strict": True,
                "schema": schema,
            }
        },
    )
    return json.loads(response.output_text)


def fallback_hrdm(packet: dict) -> dict:
    job = packet["job"]
    return {
        "process_id": packet["process_id"],
        "job": job,
        "ai_status": "not_run",
        "note": "OPENAI_API_KEY not configured. Use the generated HRDM prompt packet in ChatGPT or rerun after configuring the secret.",
        "signals": [],
        "concept_clusters": [],
        "hidden_need": {"statement": "", "confidence": "low", "rationale": []},
        "field_logic": {},
        "function_core": {"chain": "", "summary": ""},
        "dod": {
            "alpha": job.get("title", ""),
            "zenith": "",
            "dimensions": {"burden": 0, "scope_environment": 0, "function": 0, "signal_identity": 0},
            "average": 0,
            "classification": "Low",
        },
        "assessment_zones": [],
        "candidate_positioning": {
            "strong_matches": [],
            "transferable_matches": [],
            "gaps_unknowns": ["Automated HRDM analysis not run."],
            "prohibited_claims": [],
            "proof_points": [],
            "cv_emphasis": [],
        },
        "hcc": {"risks": [], "commentary": "Not analysed."},
        "application_strategy": {
            "positioning": "",
            "opening": "",
            "evidence_to_use": [],
            "evidence_to_avoid": [],
            "tone": "",
            "interview_themes": [],
        },
    }
