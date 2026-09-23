from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from .models import Job


REPO = "Hybrismannen/wpb"


def save_public_jobs(path: Path, jobs: list[Job]):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(jobs),
        "jobs": [j.public_dict() for j in jobs],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def priority_label(score: float) -> str:
    if score >= 72:
        return "Strong lead"
    if score >= 56:
        return "Worth a look"
    return "Explore"


def why_short(job: Job) -> str:
    reasons = []
    blob = job.search_blob
    if job.work_mode:
        reasons.append(job.work_mode)
    elif "remote" in blob or "distans" in blob:
        reasons.append("remote")
    if any(x in blob for x in ["part time", "part-time", "deltid"]):
        reasons.append("part-time")
    if job.matched_query:
        reasons.append(f"matches {job.matched_query}")
    if not reasons and job.triage_reasons:
        reasons.append(job.triage_reasons[0].replace("title/query fit ", "role match "))
    return " · ".join(reasons[:2]) or "matched search profile"


def analyze_link(job: Job) -> str:
    title = f"[CareerHub Drill] {job.company or 'Employer'} — {job.title}"
    body = (
        "### Job URL\n"
        f"{job.url}\n\n"
        "### Lane\n"
        f"{job.lane}\n\n"
        "### Job text (optional)\n"
        "_Leave blank unless the site blocks automated retrieval._\n\n"
        "### Note to self (optional)\n"
        f"Found by CareerHub via {job.source}. Priority: {priority_label(job.triage_score)}."
    )
    return (
        f"https://github.com/{REPO}/issues/new"
        f"?title={quote(title)}&body={quote(body)}"
    )


def lane_title(lane: str) -> tuple[str, str]:
    return {
        "core": ("Career-track roles", "Closest to writing, reporting, research, editorial and communications strengths."),
        "adjacent": ("Adjacent roles", "Transferable work in content, coordination, research support and communications."),
        "bridge": ("Extra-income / flexible roles", "Practical part-time, temporary and lower-barrier work."),
    }.get(lane, (lane.title(), ""))


def render_lane(lines: list[str], lane: str, jobs: list[Job]):
    title, explanation = lane_title(lane)
    lines += [
        f"## {title}",
        "",
        explanation,
        "",
    ]
    if not jobs:
        lines += ["No current leads in this lane.", ""]
        return

    lines += [
        "| Priority | Role | Employer | Location | Why it surfaced | Action |",
        "|---|---|---|---|---|---|",
    ]
    for job in jobs[:18]:
        role = job.title.replace("|", "\\|")
        company = (job.company or "—").replace("|", "\\|")
        location = (job.location or job.work_mode or "—").replace("|", "\\|")
        why = why_short(job).replace("|", "\\|")
        source_link = f"[{role}]({job.url})" if job.url else role
        lines.append(
            f"| **{priority_label(job.triage_score)}** | {source_link} | {company} | "
            f"{location} | {why} | **[Analyze →]({analyze_link(job)})** |"
        )
    lines.append("")


def render_control_room(path: Path, jobs: list[Job], lane: str):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    by_lane = {
        "core": [j for j in jobs if j.lane == "core"],
        "adjacent": [j for j in jobs if j.lane == "adjacent"],
        "bridge": [j for j in jobs if j.lane == "bridge"],
    }

    lines = [
        "# CareerHub",
        "",
        "## Find a job. Click Analyze. Edit the Word draft.",
        "",
        f"**Last refreshed:** {now} · **{len(jobs)} current leads**  ",
        "Jobs refresh automatically on weekdays. You normally do **not** need to run anything yourself.",
        "",
        "### I already found a job somewhere else",
        "",
        "**[Analyze any job →](https://github.com/Hybrismannen/wpb/issues/new?template=careerhub-analyze-job.yml)**  ",
        "Paste the job link, choose what kind of job it is, and submit. CareerHub will create the HRDM/application pack.",
        "",
        "---",
        "",
    ]

    for lane_name in ["core", "adjacent", "bridge"]:
        if lane == "all" or lane == lane_name:
            render_lane(lines, lane_name, by_lane[lane_name])

    lines += [
        "---",
        "",
        "## What happens when I click Analyze?",
        "",
        "1. A pre-filled CareerHub request opens. Press **Submit new issue**.",
        "2. CareerHub reads the public job ad and runs the full HRDM-R analysis.",
        "3. It researches the employer/role when full automation is enabled.",
        "4. It creates an application strategy and editable Word draft.",
        "5. A comment appears on the request with a link to the finished download.",
        "",
        "You do not need to open GitHub Actions or understand the HRDM files.",
        "",
        "## My profile",
        "",
        "CareerHub currently uses the verified WPB archive plus the public-safe candidate profile.  ",
        "**[Review what CareerHub knows →](profile/PROFILE_REVIEW.md)**",
        "",
        "<details>",
        "<summary><strong>Advanced controls & system status</strong></summary>",
        "",
        "- [Refresh jobs now](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-scan.yml)",
        "- [Open the old direct drill workflow](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-drill.yml)",
        "- [Setup / optional APIs](SETUP.md)",
        "- [Source matrix](docs/SOURCE_MATRIX.md)",
        "- [How HRDM works](hrdm/HRDM_R_v6.3.md)",
        "- [Privacy rules](PRIVACY.md)",
        "",
        "The numeric triage score is retained in the data layer but intentionally hidden from the main board. "
        "It is only a sourcing heuristic; the real analysis happens after a job is selected.",
        "",
        "</details>",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
