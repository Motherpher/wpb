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
        key = lines[0].strip().lower()
        value = "\n".join(lines[1:]).strip()
        value = re.sub(r"^_No response_$", "", value, flags=re.I)
        out[key] = value.strip()
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
    data = sections(issue.get("body") or "")

    case_raw = pick(data, "careerhub case issue", "case issue", "case")
    m = re.search(r"(\d+)", case_raw)
    if not m:
        raise SystemExit("No CareerHub case issue number found.")
    case_issue = int(m.group(1))

    status = pick(data, "new status", "status").lower().replace(" ", "_")
    priority_raw = pick(data, "new priority", "priority")
    priority = ""
    if priority_raw:
        m2 = re.search(r"\b([1-5])\b", priority_raw)
        if m2:
            priority = m2.group(1)

    payload = {
        "update_issue_number": issue.get("number"),
        "case_issue_number": case_issue,
        "status": status,
        "priority": priority,
        "date": pick(data, "date"),
        "next_action": pick(data, "next action (optional)", "next action"),
        "next_action_date": pick(data, "next action date"),
    }

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "update.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    for key, value in payload.items():
        (outdir / f"{key}.txt").write_text(str(value or ""), encoding="utf-8")


if __name__ == "__main__":
    main()
