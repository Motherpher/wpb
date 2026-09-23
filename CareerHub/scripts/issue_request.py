#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def sections(body: str) -> dict[str, str]:
    parts = re.split(r"^###\s+", body or "", flags=re.MULTILINE)
    out = {}
    for part in parts[1:]:
        lines = part.splitlines()
        if not lines:
            continue
        heading = lines[0].strip().lower()
        value = "\n".join(lines[1:]).strip()
        value = re.sub(r"^_No response_$", "", value, flags=re.I)
        value = re.sub(r"^_Leave blank.*_$", "", value, flags=re.I)
        out[heading] = value.strip()
    return out


def pick(data: dict[str, str], *names: str) -> str:
    for name in names:
        for key, value in data.items():
            if name in key:
                return value.strip()
    return ""


def parse_priority(raw: str) -> int:
    m = re.search(r"\b([1-5])\b", raw or "")
    return int(m.group(1)) if m else 3


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--event", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    issue = event.get("issue") or {}
    body = issue.get("body") or ""
    data = sections(body)

    url = pick(data, "job url", "job link", "annons")
    lane_raw = pick(data, "lane", "job type", "search lane").lower()
    if lane_raw.startswith("adjacent"):
        lane = "adjacent"
    elif lane_raw.startswith("bridge") or "extra" in lane_raw:
        lane = "bridge"
    else:
        lane = "core"

    text = pick(data, "job text")
    role = pick(data, "role", "job title")
    employer = pick(data, "employer", "company")
    deadline = pick(data, "deadline")
    priority = parse_priority(pick(data, "priority", "rank"))
    note = pick(data, "note to self", "notes")

    if not url:
        raise SystemExit("No Job URL found in the CareerHub issue.")

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    values = {
        "job_url.txt": url,
        "lane.txt": lane,
        "job_text.txt": text,
        "role.txt": role,
        "employer.txt": employer,
        "deadline.txt": deadline,
        "priority.txt": str(priority),
        "note.txt": note,
    }
    for name, value in values.items():
        (outdir / name).write_text(value, encoding="utf-8")

    (outdir / "request.json").write_text(json.dumps({
        "issue_number": issue.get("number"),
        "issue_title": issue.get("title"),
        "requester": (issue.get("user") or {}).get("login"),
        "job_url": url,
        "lane": lane,
        "role": role,
        "employer": employer,
        "deadline": deadline,
        "priority": priority,
        "job_text_supplied": bool(text),
        "note": note,
    }, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
