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
    note = pick(data, "note to self", "notes")

    if not url:
        raise SystemExit("No Job URL found in the CareerHub issue.")

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "job_url.txt").write_text(url + "\n", encoding="utf-8")
    (outdir / "lane.txt").write_text(lane + "\n", encoding="utf-8")
    (outdir / "job_text.txt").write_text(text, encoding="utf-8")
    (outdir / "note.txt").write_text(note, encoding="utf-8")
    (outdir / "request.json").write_text(json.dumps({
        "issue_number": issue.get("number"),
        "issue_title": issue.get("title"),
        "requester": (issue.get("user") or {}).get("login"),
        "job_url": url,
        "lane": lane,
        "job_text_supplied": bool(text),
        "note": note,
    }, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
