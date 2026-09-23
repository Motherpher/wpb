from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import Job


def save_public_jobs(path: Path, jobs: list[Job]):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(jobs),
        "jobs": [j.public_dict() for j in jobs],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_control_room(path: Path, jobs: list[Job], lane: str):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# CareerHub Control Room",
        "",
        f"> **Last scan:** {now}  ",
        f"> **Lane:** {lane}  ",
        f"> **Leads shown:** {len(jobs)}",
        "",
        "## Quick actions",
        "",
        "1. **Refresh:** Actions → CareerHub — Scan & Rank Jobs.",
        "2. **Drill:** copy a job URL and run CareerHub — Drill & Application Pack.",
        "3. **Download:** use the drill workflow artifact for HRDM and DOCX drafts.",
        "",
        "## Current ranked leads",
        "",
        "| Score | Lane | Role | Employer | Location | Source | Flags |",
        "|---:|---|---|---|---|---|---|",
    ]
    for j in jobs[:60]:
        title = j.title.replace("|", "\\|")
        company = j.company.replace("|", "\\|")
        location = j.location.replace("|", "\\|")
        url = j.url or "#"
        flags = ", ".join(j.review_flags) if j.review_flags else "—"
        lines.append(f"| **{j.triage_score:.1f}** | {j.lane} | [{title}]({url}) | {company} | {location} | {j.source} | {flags} |")

    lines += [
        "",
        "## How to read the score",
        "",
        "The number above is a **triage score**, not HRDM. It ranks a large lead pool using title/query fit, public candidate-evidence overlap, work arrangement, geography/remote fit and recency. Requirements that are currently unverified in the candidate profile are flagged for human review.",
        "",
        "A selected job then goes through the full HRDM-R v6.3 sequence.",
        "",
        "## Manual sources to check",
        "",
        "- [Ideella Jobb](https://ideellajobb.se/)",
        "- [Indeed Sweden](https://se.indeed.com/jobs)",
        "- [Monster](https://www.monster.com/jobs)",
        "- [Jobbland](https://jobbland.se/)",
        "- [LinkedIn Jobs](https://www.linkedin.com/jobs/)",
        "",
        "Paste any selected public job URL into the Drill workflow. If automated retrieval is blocked, paste the job text into the optional workflow field.",
        "",
        "## Privacy",
        "",
        "Application drafts are not committed. See [PRIVACY.md](PRIVACY.md).",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
