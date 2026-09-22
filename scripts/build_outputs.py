#!/usr/bin/env python3
"""Build all derived WPB archive outputs from canonical repository data.

Canonical inputs:
- data/corpus.json
- data/credits.json
- data/article-metadata.json

Derived outputs:
- data/dashboard.json
- bibliography/master-bibliography.md
- DASHBOARD.md
- visuals/dashboard.svg

Do not put research decisions in this script. Verification/evidence decisions belong
in the canonical data and are reviewed before this builder runs.
"""

from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P = {
    "bg": "#F7F3EA",
    "paper": "#FFFDF8",
    "ink": "#1B1B1B",
    "muted": "#6C675F",
    "rule": "#D9D1C4",
    "yellow": "#E5B843",
    "rose": "#D75A68",
    "roseSoft": "#EAB0B6",
    "teal": "#2D93A5",
    "tealSoft": "#8ECBD0",
    "mint": "#78BBA9",
    "navy": "#14364A",
    "pale": "#EEE8DE",
}

PHASES = [
    ("body-fashion-research", "Body & fashion research", "BODY · VISUAL CULTURE · REPRESENTATION", 390, P["yellow"]),
    ("cultural-journalism", "Cultural journalism", "MUSIC · ART · PLACE · DIASPORA", 485, P["rose"]),
    ("social-observational-reporting", "Social-observational reporting", "MIGRATION · RACE · GENDER · EVERYDAY LIFE", 605, P["teal"]),
    ("long-form-social-reportage", "Long-form social reportage", "INSTITUTIONS · RIGHTS · BORDERS · LABOUR", 710, P["mint"]),
]

def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def write(path: str, content: str):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def count_by(items, fn):
    c = Counter()
    for item in items:
        c[fn(item) or "unknown"] += 1
    return dict(c)

def pct(n: int, total: int) -> int:
    return round(100 * n / total) if total else 0

def esc(value) -> str:
    return html.escape(str(value), quote=True)

def build_dashboard_json(corpus, credits, meta):
    works = corpus["works"]
    total = len(works)
    enriched = sum(str(r.get("metadata_status", "")).startswith("manually-enriched") for r in meta["records"].values())
    years = count_by(works, lambda w: str(w["date"])[:4] if w.get("date") else "unknown")
    phases = count_by(works, lambda w: w.get("phase"))
    languages = count_by(works, lambda w: w.get("language"))
    outlets = count_by(works, lambda w: w.get("outlet"))
    evidence = count_by(works, lambda w: w.get("evidence"))
    date_precision = count_by(works, lambda w: (w.get("dashboard") or {}).get("date_precision"))
    source_completeness = count_by(works, lambda w: (w.get("dashboard") or {}).get("source_completeness"))
    missing = [w for w in works if not w.get("date")]
    partial = [w for w in works if (w.get("dashboard") or {}).get("source_completeness") == "verified-partial-metadata"]

    dashboard = load("data/dashboard.json")
    dashboard["schema_version"] = "1.3"
    dashboard["generated"] = corpus.get("updated")
    dashboard.setdefault("source_of_truth", {}).update({
        "corpus": "data/corpus.json",
        "article_metadata": "data/article-metadata.json",
        "credits": "data/credits.json",
        "dashboard_visual": "visuals/dashboard.svg",
        "builder": "scripts/build_outputs.py",
    })
    dashboard.setdefault("project", {}).update({
        "status": "active-reconstruction",
        "repository_mode": ["research-archive", "portfolio-content-backend"],
        "site_status": "framework-neutral-not-built",
        "official_status": "independent-working-archive",
        "corpus_completeness_claim": "reconstructed-not-exhaustive",
        "dashboard_status": "single-integrated-automated",
    })
    dashboard["visual"] = {
        "canonical": "visuals/dashboard.svg",
        "generated_by": "scripts/build_outputs.py",
        "automation": ".github/workflows/sync-derived.yml",
        "mode": "single-integrated-dashboard",
        "separate_public_visuals": False,
    }
    dashboard.pop("visuals", None)
    dashboard["corpus"] = {
        "total_works": total,
        "featured_candidates": sum(bool(w.get("featured")) for w in works),
        "evidence": evidence,
        "languages": languages,
        "phases": phases,
        "outlets": outlets,
        "date_precision": date_precision,
        "source_completeness": source_completeness,
        "years": years,
        "unresolved_dates": len(missing),
        "article_metadata_records": len(meta["records"]),
        "manually_enriched_article_metadata_records": enriched,
    }
    dashboard["portfolio"] = {
        "candidate_count": sum(bool(w.get("featured")) for w in works),
        "candidate_ids": [w["id"] for w in works if w.get("featured")],
        "rights_review_complete": 0,
        "visual_assets_review_complete": 0,
        "final_public_bio_status": "pending-writer-review",
        "final_featured_selection_status": "pending-writer-review",
        "implementation_status": "not-started",
    }
    dashboard["contextual_credits"] = {
        "total": len(credits["records"]),
        "by_evidence": count_by(credits["records"], lambda r: r.get("evidence")),
        "unresolved": sum(r.get("evidence") == "C" for r in credits["records"]),
    }
    dashboard["data_quality"] = {
        "missing_date_records": [{"id": w["id"], "title": w["title"], "outlet": w["outlet"]} for w in missing],
        "partial_publication_metadata_records": [{"id": w["id"], "title": w["title"]} for w in partial],
        "article_metadata_records": len(meta["records"]),
        "article_metadata_manually_enriched": enriched,
        "rights_status": "not-assessed-at-record-level",
        "asset_status": "not-assessed-at-record-level",
        "taxonomy_note": "Theme arrays include canonical IDs and descriptive free-form tags; no silent normalization.",
    }
    return dashboard

def build_svg(corpus, credits, meta) -> str:
    works = corpus["works"]
    total = len(works)
    phases = Counter(w.get("phase") for w in works)
    langs = Counter(w.get("language") for w in works)
    years = Counter(str(w["date"])[:4] if w.get("date") else "unknown" for w in works)
    enriched = sum(str(r.get("metadata_status", "")).startswith("manually-enriched") for r in meta["records"].values())
    featured = sum(bool(w.get("featured")) for w in works)
    unresolved = sum(not w.get("date") for w in works)
    agrade = sum(w.get("evidence") == "A" for w in works)
    strong = sum((w.get("dashboard") or {}).get("source_completeness") == "verified" for w in works)
    partial = sum((w.get("dashboard") or {}).get("source_completeness") == "verified-partial-metadata" for w in works)

    flow_parts = []
    phase_labels = []
    for phase_id, label, sub, y, color in PHASES:
        group = [w for w in works if w.get("phase") == phase_id]
        n = len(group)
        spread = min(90, max(10, n * 4.1))
        flow_parts.append(
            f'<path d="M 90 555 C 285 545, 470 {y}, 765 {y}" fill="none" '
            f'stroke="{color}" stroke-width="{max(8, n*1.35):.2f}" opacity="0.08"/>'
        )
        for i, work in enumerate(group):
            offset = 0 if n == 1 else ((i / (n - 1)) - 0.5) * spread
            bend = ((i % 5) - 2) * 7
            opacity = 0.22 + (i % 4) * 0.055
            flow_parts.append(
                f'<path d="M 90 555 C 255 {555+bend}, 455 {y+offset*0.58:.1f}, 765 {y+offset:.1f}" '
                f'fill="none" stroke="{color}" stroke-width="2.1" opacity="{opacity:.2f}">'
                f'<title>{esc(work["title"])} — {esc(work["outlet"])}</title></path>'
            )
        phase_labels.append(
            f'<circle cx="790" cy="{y}" r="8" fill="{color}"/>'
            f'<text x="820" y="{y+7}" class="phaseCount">{n}</text>'
            f'<text x="862" y="{y+3}" class="phaseTitle">{esc(label)}</text>'
            f'<text x="862" y="{y+27}" class="micro">{esc(sub)}</text>'
        )

    ordered_years = [str(y) for y in range(2013, 2021)]
    max_year = max([years.get(y, 0) for y in ordered_years] or [1])
    bars = []
    for i, year in enumerate(ordered_years):
        n = years.get(year, 0)
        height = 112 * n / max_year if max_year else 0
        x = 70 + i * 48
        yy = 965 - height
        opacity = 0.95 if n == max_year else 0.70
        bars.append(
            f'<rect x="{x}" y="{yy:.1f}" width="25" height="{height:.1f}" rx="3" fill="{P["tealSoft"]}" opacity="{opacity}"/>'
            f'<text x="{x+12.5}" y="992" text-anchor="middle" class="axis">{year}</text>'
            f'<text x="{x+12.5}" y="{yy-7:.1f}" text-anchor="middle" class="axis">{n}</text>'
        )

    rays = []
    import math
    for i, angle in enumerate([-70,-52,-34,-16,2,20,38,56,74]):
        x1, y1 = 1178, 73
        rad = math.radians(angle)
        x2, y2 = x1 + 190*math.cos(rad), y1 + 190*math.sin(rad)
        cx = (x1+x2)/2 + (10 if i % 2 else -8)
        cy = (y1+y2)/2
        width = 18 - (i % 3)*3
        opacity = 0.88 - i*0.035
        rays.append(
            f'<path d="M {x1} {y1} Q {cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f}" '
            f'stroke="{P["yellow"]}" stroke-width="{width}" stroke-linecap="round" fill="none" opacity="{opacity:.2f}"/>'
        )

    kpis = [
        (str(total), "works", "TOTAL CORPUS", P["yellow"], "▤"),
        (str(enriched), "metadata enriched", f"{pct(enriched,total)}% COVERAGE", P["tealSoft"], "▧"),
        (str(featured), "portfolio candidates", "EDITORIAL SHORTLIST", P["roseSoft"], "☆"),
        (str(len(credits["records"])), "contextual credits", "SEPARATE FROM BYLINES", P["mint"], "○"),
        (str(unresolved), "unresolved dates", "NEEDS RESEARCH", P["roseSoft"], "!"),
        (str(agrade), "A-grade records", "VERIFIED AUTHORSHIP", P["tealSoft"], "A"),
    ]
    kpi_svg = []
    for i, (value, label, note, color, icon) in enumerate(kpis):
        x = 55 + i*250
        if i:
            kpi_svg.append(f'<line x1="{x-17}" y1="247" x2="{x-17}" y2="325" stroke="{P["rule"]}"/>')
        kpi_svg.append(
            f'<circle cx="{x+28}" cy="286" r="27" fill="{color}" opacity="0.42"/>'
            f'<text x="{x+28}" y="294" text-anchor="middle" class="kpiIcon">{esc(icon)}</text>'
            f'<text x="{x+67}" y="282" class="kpi">{esc(value)}</text>'
            f'<text x="{x+67}" y="304" class="kpiLabel">{esc(label)}</text>'
            f'<text x="{x+67}" y="323" class="micro">{esc(note)}</text>'
        )

    meta_svg = [f'<line x1="1218" y1="390" x2="1218" y2="735" stroke="{P["navy"]}" stroke-width="1.3"/>']
    blocks = [
        (438, pct(enriched,total), "metadata enriched", f"{enriched} of {total} works", P["teal"], False),
        (548, pct(agrade,total), "A-grade evidence", f"{agrade} of {total} works", P["teal"], False),
        (662, pct(unresolved,total), "unresolved dates", f"{unresolved} of {total} works", P["rose"], True),
    ]
    for y, percentage, label, detail, color, rose in blocks:
        amp = max(15, 135*percentage/100)
        meta_svg.append(
            f'<path d="M 1218 {y-44} C {1218+amp*.25:.1f} {y-34}, {1218+amp:.1f} {y-24}, {1218+amp*.72:.1f} {y} '
            f'C {1218+amp:.1f} {y+22}, {1218+amp*.28:.1f} {y+34}, 1218 {y+44} Z" '
            f'fill="{color}" opacity="{"0.55" if rose else "0.48"}" stroke="{color}" stroke-width="1.3"/>'
            f'<line x1="1125" y1="{y+54}" x2="1510" y2="{y+54}" stroke="{color}" stroke-dasharray="2 5" opacity="0.55"/>'
            f'<text x="1390" y="{y-5}" class="{"pctRose" if rose else "pctTeal"}">{percentage}%</text>'
            f'<text x="1390" y="{y+21}" class="{"metaRose" if rose else "metaTeal"}">{esc(label)}</text>'
            f'<text x="1390" y="{y+43}" class="micro">{esc(detail)}</text>'
        )

    pipeline = [("Discover","⌕",P["yellow"]),("Verify","▧",P["tealSoft"]),("Structure","≡",P["mint"]),("Interpret","◇",P["roseSoft"]),("Publish","↑",P["yellow"])]
    pipe_svg = []
    for i, (label, icon, color) in enumerate(pipeline):
        x = 585 + i*90
        pipe_svg.append(
            f'<circle cx="{x}" cy="908" r="30" fill="{color}" opacity="0.5"/>'
            f'<text x="{x}" y="916" text-anchor="middle" class="pipeIcon">{esc(icon)}</text>'
            f'<text x="{x}" y="958" text-anchor="middle" class="pipeLabel">{esc(label)}</text>'
        )
        if i < len(pipeline)-1:
            pipe_svg.append(f'<text x="{x+45}" y="915" text-anchor="middle" class="arrow">→</text>')

    readiness = [("Writer review","pending"),("Rights review","pending"),("Visual asset review","pending"),("Site implementation","not started")]
    ready_svg = []
    for i, (label, status) in enumerate(readiness):
        y = 860 + i*43
        fill = P["roseSoft"] if status == "not started" else P["yellow"]
        ready_svg.append(
            f'<circle cx="1152" cy="{y}" r="13" fill="{P["yellow"]}" opacity="0.42"/>'
            f'<text x="1177" y="{y+5}" class="ready">{esc(label)}</text>'
            f'<rect x="1384" y="{y-15}" width="118" height="28" rx="14" fill="{fill}" opacity="0.34"/>'
            f'<text x="1443" y="{y+5}" text-anchor="middle" class="ready">{esc(status)}</text>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1080" viewBox="0 0 1600 1080" role="img" aria-labelledby="title desc">
<title id="title">WPB Archive Dashboard</title>
<desc id="desc">Integrated dashboard of the Weronika Pérez Borjas research archive: corpus size, editorial phases, metadata coverage, publication timeline, research pipeline and portfolio readiness.</desc>
<style>
.title{{font:700 55px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.h2{{font:700 27px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.body{{font:16px Georgia,'Times New Roman',serif;fill:{P["muted"]}}}
.small{{font:14px Arial,sans-serif;fill:{P["muted"]}}}
.micro{{font:11px Arial,sans-serif;fill:{P["muted"]};letter-spacing:1.1px}}
.kpi{{font:700 32px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.kpiLabel{{font:15px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.kpiIcon{{font:700 20px Arial,sans-serif;fill:{P["navy"]}}}
.phaseCount{{font:700 28px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.phaseTitle{{font:18px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.axis{{font:11px Arial,sans-serif;fill:{P["muted"]}}}
.pctTeal{{font:700 34px Georgia,'Times New Roman',serif;fill:{P["teal"]}}}
.pctRose{{font:700 34px Georgia,'Times New Roman',serif;fill:{P["rose"]}}}
.metaTeal{{font:18px Georgia,'Times New Roman',serif;fill:{P["teal"]}}}
.metaRose{{font:18px Georgia,'Times New Roman',serif;fill:{P["rose"]}}}
.pipeIcon{{font:700 23px Arial,sans-serif;fill:{P["navy"]}}}
.pipeLabel{{font:14px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.arrow{{font:24px Arial,sans-serif;fill:{P["muted"]}}}
.ready{{font:14px Georgia,'Times New Roman',serif;fill:{P["ink"]}}}
.italic{{font:italic 19px Georgia,'Times New Roman',serif;fill:{P["muted"]}}}
</style>
<rect width="1600" height="1080" fill="{P["bg"]}"/>
<text x="45" y="35" class="micro">SINGLE SOURCE OF TRUTH · CORPUS.JSON · ARTICLE-METADATA.JSON · CREDITS.JSON</text>
<text x="45" y="103" class="title">WPB Archive Dashboard</text>
<text x="47" y="143" class="body">One coordinated view of the reconstructed archive: what has been found, how the work develops,</text>
<text x="47" y="168" class="body">how complete the metadata is, and what remains before the archive can become a public portfolio.</text>
<text x="47" y="195" class="small">All quantitative visuals are regenerated from canonical repository data.</text>
{''.join(rays)}
<path d="M 1120 0 A 73 73 0 0 0 1266 0" fill="{P["yellow"]}" opacity="0.9"/>
<text x="1355" y="55" class="micro">RESEARCH</text><text x="1355" y="78" class="micro">EVIDENCE</text><text x="1355" y="101" class="micro">STORIES</text>
<line x1="1355" y1="120" x2="1390" y2="120" stroke="{P["yellow"]}" stroke-width="2"/><text x="1355" y="145" class="micro">WPB ARCHIVE</text>

<line x1="40" y1="225" x2="1560" y2="225" stroke="{P["rule"]}"/>
{''.join(kpi_svg)}
<line x1="40" y1="342" x2="1560" y2="342" stroke="{P["rule"]}"/>

<text x="45" y="384" class="h2">Archive structure by editorial phase</text>
<text x="47" y="409" class="small">Each curve is one verified work. The four bundles are analytical phases, not self-declared career labels.</text>
<circle cx="90" cy="555" r="5" fill="{P["navy"]}"/>
<text x="48" y="583" class="small">WPB archive</text><text x="48" y="602" class="small">{total} works</text>
{''.join(flow_parts)}
{''.join(phase_labels)}
<text x="48" y="690" class="italic">Body → identity →</text><text x="48" y="716" class="italic">classification → systems</text>

<line x1="1085" y1="360" x2="1085" y2="760" stroke="{P["rule"]}"/>
<text x="1125" y="390" class="h2">Metadata coverage</text>
<text x="1127" y="416" class="small">Coverage, evidence strength and explicit remaining gaps.</text>
{''.join(meta_svg)}
<text x="1127" y="748" class="micro">{strong} STRONGLY VERIFIED PUBLICATION RECORDS · {partial} PARTIAL METADATA RECORDS</text>

<line x1="40" y1="785" x2="1560" y2="785" stroke="{P["rule"]}"/>
<line x1="490" y1="805" x2="490" y2="1025" stroke="{P["rule"]}"/>
<line x1="1090" y1="805" x2="1090" y2="1025" stroke="{P["rule"]}"/>

<text x="45" y="825" class="h2">Publication timeline</text>
<text x="47" y="850" class="small">Verified works by known publication year.</text>
<line x1="62" y1="965" x2="455" y2="965" stroke="{P["rule"]}"/>
{''.join(bars)}
<text x="48" y="1020" class="micro">LANGUAGES · EN {langs.get("en",0)} · PL {langs.get("pl",0)} · {years.get("unknown",0)} RECORDS STILL UNDATED</text>

<text x="540" y="825" class="h2">Research-to-publication pipeline</text>
<text x="542" y="850" class="small">The automated path from public-source discovery to a future portfolio.</text>
{''.join(pipe_svg)}
<line x1="555" y1="990" x2="1005" y2="990" stroke="{P["muted"]}"/>
<text x="780" y="1015" text-anchor="middle" class="italic">Discover → verify → structure → interpret → publish</text>

<text x="1135" y="825" class="h2">Portfolio readiness</text>
<text x="1137" y="850" class="small">Editorial decisions remain human decisions.</text>
{''.join(ready_svg)}

<line x1="40" y1="1044" x2="1560" y2="1044" stroke="{P["rule"]}"/>
<text x="45" y="1067" class="micro">INTEGRATED ARCHIVE DASHBOARD · RESEARCH ARCHIVE + METADATA SYSTEM + FUTURE PORTFOLIO BACKEND</text>
<text x="1450" y="1067" class="micro">UPDATED {esc(corpus.get("updated"))}</text>
</svg>'''

def build_dashboard_md(corpus, credits, meta, dashboard) -> str:
    works = corpus["works"]
    total = len(works)
    phases = Counter(w.get("phase") for w in works)
    enriched = sum(str(r.get("metadata_status", "")).startswith("manually-enriched") for r in meta["records"].values())
    featured = sum(bool(w.get("featured")) for w in works)
    unresolved = sum(not w.get("date") for w in works)
    agrade = sum(w.get("evidence") == "A" for w in works)
    return f"""# WPB Archive Dashboard

![WPB Archive Dashboard](visuals/dashboard.svg)

## What you can see

The dashboard is the **single visual surface** for the repository. It is generated from the canonical archive data rather than maintained as a separate illustration.

It combines six views in one composition:

- **Archive size and readiness** — {total} verified works, {enriched} enriched article-metadata records, {featured} portfolio candidates, {len(credits["records"])} contextual credits, {unresolved} unresolved dates and {agrade} A-grade authorship records.
- **Editorial structure** — every verified work is represented as one curve flowing into four analytical phases: {phases.get("body-fashion-research",0)} body/fashion research, {phases.get("cultural-journalism",0)} cultural journalism, {phases.get("social-observational-reporting",0)} social-observational reporting and {phases.get("long-form-social-reportage",0)} long-form social reportage.
- **Metadata coverage** — {pct(enriched,total)}% of works have additional publisher-level metadata enrichment; A-grade evidence covers {pct(agrade,total)}% of the authored/research corpus; {pct(unresolved,total)}% still lack a resolved publication date.
- **Publication timeline** — the actual known-year distribution from 2013–2020, with undated records disclosed separately.
- **Research pipeline** — Discover → Verify → Structure → Interpret → Publish.
- **Portfolio readiness** — writer review, rights review, visual-asset review and site implementation remain explicit human decisions.

### Source of truth

The dashboard is derived from:

- `data/corpus.json`
- `data/article-metadata.json`
- `data/credits.json`
- `data/dashboard.json`

The visual itself is `visuals/dashboard.svg`.

### Automation

`scripts/build_outputs.py` rebuilds the aggregate dashboard metadata, human-readable bibliography, this page and the integrated SVG.

`.github/workflows/sync-derived.yml` automatically runs that builder when canonical data changes and commits changed derived outputs. `.github/workflows/validate.yml` checks JSON integrity, corpus/metadata alignment, SVG validity and whether derived outputs are synchronized.

The public dashboard therefore has **one visual, one data lineage and one update path**.

## Important interpretation note

The four editorial phases are repository analysis, not labels attributed to Weronika Pérez Borjas. A portfolio candidate is not the same thing as a writer-approved selection. Unknown rights or asset status means **not yet assessed**, not unavailable.

For the deeper archive, continue to [START_HERE.md](START_HERE.md), [the master bibliography](bibliography/master-bibliography.md), or [the writer dossier](analysis/writer-dossier.md).
"""

def build_bibliography(corpus) -> str:
    lines = [
        "# Master bibliography",
        "",
        "Generated from `data/corpus.json`. The JSON file is canonical; this file is the human-readable view.",
        "",
        "| Date | Title | Outlet | Type | Lang. | Evidence | Link |",
        "|---|---|---|---|---|---|---|",
    ]
    for w in corpus["works"]:
        title = w["title"].replace("|", "\\|")
        lines.append(f'| {w.get("date") or "date pending"} | {title} | {w["outlet"]} | {w["type"]} | {w["language"]} | {w["evidence"]} | [source]({w["url"]}) |')
    lines.extend([
        "",
        "## Notes",
        f'- Current canonical count: **{len(corpus["works"])}** works.',
        "- Missing dates remain unresolved rather than estimated.",
        "- Detailed publisher metadata lives in `data/article-metadata.json`.",
        "- This bibliography is reconstructed and not claimed to be exhaustive.",
    ])
    return "\n".join(lines) + "\n"

def main():
    corpus = load("data/corpus.json")
    credits = load("data/credits.json")
    meta = load("data/article-metadata.json")
    dashboard = build_dashboard_json(corpus, credits, meta)

    write("data/dashboard.json", json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n")
    write("bibliography/master-bibliography.md", build_bibliography(corpus))
    write("DASHBOARD.md", build_dashboard_md(corpus, credits, meta, dashboard))
    write("visuals/dashboard.svg", build_svg(corpus, credits, meta))

    print(json.dumps({
        "works": len(corpus["works"]),
        "credits": len(credits["records"]),
        "metadata_records": len(meta["records"]),
        "dashboard": "visuals/dashboard.svg",
    }, indent=2))

if __name__ == "__main__":
    main()
