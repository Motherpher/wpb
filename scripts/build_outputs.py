#!/usr/bin/env python3
"""Regenerate human-readable derived outputs from canonical WPB JSON data.

This script intentionally does not modify canonical research decisions. It reads
data/corpus.json, data/credits.json and data/article-metadata.json, then rebuilds
aggregate dashboard/bibliography outputs after reviewed corpus changes.
"""

from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

def main():
    corpus=load("data/corpus.json")
    credits=load("data/credits.json")
    meta=load("data/article-metadata.json")
    works=corpus["works"]

    by=lambda key: Counter((w.get(key) or "unknown") for w in works)
    years=Counter(str(w["date"])[:4] if w.get("date") else "unknown" for w in works)
    source=Counter((w.get("dashboard") or {}).get("source_completeness","unknown") for w in works)
    precision=Counter((w.get("dashboard") or {}).get("date_precision","unknown") for w in works)

    dash=load("data/dashboard.json")
    dash["generated"]=corpus.get("updated")
    dash["corpus"].update({
        "total_works":len(works),
        "featured_candidates":sum(bool(w.get("featured")) for w in works),
        "evidence":dict(by("evidence")),
        "languages":dict(by("language")),
        "phases":dict(by("phase")),
        "outlets":dict(by("outlet")),
        "years":dict(years),
        "date_precision":dict(precision),
        "source_completeness":dict(source),
        "unresolved_dates":sum(not w.get("date") for w in works),
        "article_metadata_records":len(meta["records"]),
    })
    (ROOT/"data/dashboard.json").write_text(json.dumps(dash,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    lines=[
        "# Master bibliography","",
        "Generated from `data/corpus.json`. The JSON file is canonical; this file is the human-readable view.","",
        "| Date | Title | Outlet | Type | Lang. | Evidence | Link |",
        "|---|---|---|---|---|---|---|",
    ]
    for w in works:
        title=w["title"].replace("|","\\|")
        lines.append(f'| {w.get("date") or "date pending"} | {title} | {w["outlet"]} | {w["type"]} | {w["language"]} | {w["evidence"]} | [source]({w["url"]}) |')
    lines += ["","## Notes",f'- Current canonical count: **{len(works)}** works.',
              "- Missing dates remain unresolved rather than estimated.",
              "- Detailed publisher metadata lives in `data/article-metadata.json`.",
              "- This bibliography is reconstructed and not claimed to be exhaustive."]
    (ROOT/"bibliography/master-bibliography.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

    print(json.dumps({"works":len(works),"credits":len(credits["records"]),"metadata_records":len(meta["records"])},indent=2))

if __name__=="__main__":
    main()
