from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_ID = "2015-forumist-seance-with-goat"
URL = "https://theforumist.com/seance-with-goat/"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def insert_after_id(items: list[dict], new_item: dict, anchor_id: str | None = None) -> None:
    if any(item.get("id") == new_item["id"] for item in items):
        return
    if anchor_id:
        for index, item in enumerate(items):
            if item.get("id") == anchor_id:
                items.insert(index + 1, new_item)
                return
    items.append(new_item)


def update_corpus() -> None:
    path = ROOT / "data/corpus.json"
    data = load_json(path)
    new_work = {
        "id": NEW_ID,
        "date": "2015",
        "title": "Séance with Goat",
        "outlet": "The Forumist",
        "language": "en",
        "type": "music interview/profile",
        "evidence": "A",
        "status": "verified",
        "url": URL,
        "themes": ["music", "spirituality", "identity", "Sweden"],
        "phase": "cultural-journalism",
        "featured": False,
        "note": "Direct publisher page credits words to Weronika Pérez Borjas; interview/profile with Goat in Way Out West 2015 context, focused on anonymity, place, spirituality and music.",
        "dashboard": {
            "date_precision": "year",
            "source_completeness": "verified",
            "evidence_grade": "A",
            "portfolio": {
                "candidate": True,
                "readiness": "candidate-needs-editorial-and-rights-review",
                "rights_status": "not-assessed",
                "visual_asset_status": "not-assessed",
                "public_copy_status": "working-copy",
            },
            "metadata": {
                "required_fields_present": 12,
                "required_fields_total": 12,
                "missing_required_fields": [],
            },
            "taxonomy": {
                "canonical_theme_tags": ["identity"],
                "descriptive_theme_tags": ["music", "spirituality", "Sweden"],
                "normalization_status": "mixed-taxonomy",
            },
            "flags": ["portfolio-candidate"],
        },
    }
    insert_after_id(data["works"], new_work, "2015-forumist-talking-to-los-muertos")
    data["updated"] = "2026-10-07"
    write_json(path, data)


def update_article_metadata() -> None:
    path = ROOT / "data/article-metadata.json"
    data = load_json(path)
    if NEW_ID not in data["records"]:
        data["records"][NEW_ID] = {
            "canonical_url": URL,
            "metadata_status": "manually-enriched-from-publisher",
            "retrieved_on": "2026-10-07",
            "publication": {"date": "2015", "date_precision": "year"},
            "byline": {"name": "Weronika Pérez Borjas", "verified": True},
            "credits": [{"role": "photography", "names": ["Clara Uddman"]}],
            "platform": {"subject": "Goat", "context": "Way Out West 2015 / music interview"},
            "academic": {},
            "discovery_evidence": [URL],
        }
    data["updated"] = "2026-10-07"
    write_json(path, data)


def update_portfolio_catalog() -> None:
    path = ROOT / "CareerHub/personalisation/portfolio-catalog.json"
    data = load_json(path)
    new_work = {
        "id": NEW_ID,
        "date": "2015",
        "title": "Séance with Goat",
        "outlet": "The Forumist",
        "language": "en",
        "type": "music interview/profile",
        "evidence": "A",
        "status": "verified",
        "url": URL,
        "themes": ["music", "spirituality", "identity", "Sweden"],
        "phase": "cultural-journalism",
        "primary_area": "culture-interviews",
        "note": "Direct publisher page credits words to Weronika Pérez Borjas; recovered during source reconciliation from the Way Out West 2015 context.",
    }
    insert_after_id(data["works"], new_work, "2015-forumist-into-the-sound")
    data["work_count"] = len(data["works"])
    data["updated"] = "2026-10-07"
    if data["work_count"] != 45:
        raise SystemExit(f"Expected 45 public credits after reconciliation, got {data['work_count']}")
    write_json(path, data)


def update_portfolio_yaml() -> None:
    path = ROOT / "CareerHub/personalisation/portfolio.yaml"
    text = path.read_text(encoding="utf-8")
    if f'- "{NEW_ID}"' not in text:
        anchor = '        - "2015-forumist-into-the-sound"\n'
        if anchor not in text:
            raise SystemExit("Could not find portfolio.yaml culture insertion anchor")
        text = text.replace(anchor, anchor + f'        - "{NEW_ID}"\n', 1)
    text = text.replace("  count: 44\n", "  count: 45\n", 1)
    text = text.replace(
        "The public catalog now contains 44 verified portfolio credits: 41 authored works, 2 book translations and 1 visual-editorial styling credit.",
        "The public catalog now contains 45 verified portfolio credits: 42 authored works, 2 book translations and 1 visual-editorial styling credit.",
    )
    path.write_text(text, encoding="utf-8")


def update_primary_area_index() -> None:
    path = ROOT / "WriterRoom/portfolio/PRIMARY_AREA_INDEX.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = "## Culture & interviews — 23"
    if heading in lines:
        lines[lines.index(heading)] = "## Culture & interviews — 24"
    start = lines.index("## Culture & interviews — 24")
    end = lines.index("## Research & criticism — 4")
    block = lines[start + 1 : end]
    if not any("Séance with Goat" in line for line in block):
        insert_at = next(i + 1 for i, line in enumerate(block) if "Into the Sound" in line)
        block.insert(insert_at, "0. Séance with Goat — The Forumist (2015)")
    counter = 0
    for i, line in enumerate(block):
        if re.match(r"^\d+\. ", line):
            counter += 1
            block[i] = re.sub(r"^\d+\.", f"{counter}.", line)
    if counter != 24:
        raise SystemExit(f"Expected 24 culture items, got {counter}")
    lines[start + 1 : end] = block
    text = "\n".join(lines) + "\n"
    text = text.replace("**Total: 44 verified portfolio credits.**", "**Total: 45 verified portfolio credits.**")
    text = text.replace(
        "Role breakdown: **41 authored works · 2 translations · 1 visual-editorial styling credit.**",
        "Role breakdown: **42 authored works · 2 translations · 1 visual-editorial styling credit.**",
    )
    path.write_text(text, encoding="utf-8")


def update_source_reconciliation() -> None:
    path = ROOT / "docs/SOURCE_RECONCILIATION_2026-10-07.md"
    text = path.read_text(encoding="utf-8")
    old_state = (
        "The public portfolio remains **44 verified credits**: **41 authored works, 2 book translations and 1 visual/editorial styling credit**. "
        "The source batch materially strengthens provenance and career history but does not yet prove an additional 45th public credit."
    )
    new_state = (
        "The public portfolio now contains **45 verified credits**: **42 authored works, 2 book translations and 1 visual/editorial styling credit**. "
        "This source batch establishes one additional authored work while the remaining supplied links either strengthen existing credits, provide career context or remain unresolved."
    )
    if old_state in text:
        text = text.replace(old_state, new_state, 1)
    elif new_state not in text:
        raise SystemExit("Could not find source-reconciliation public-state paragraph")
    heading = "### Directly verified public credits / canonical-source upgrades\n\n"
    bullet = (
        "- **Séance with Goat** — The Forumist. The direct publisher page identifies the work and explicitly credits `Words by Weronika Pérez Borjas`; photography is credited to Clara Uddman and the page thanks WOW2015. This is a distinct authored work absent from the preceding 44-credit catalog, so it is added under **Culture & interviews** as the 45th public credit. Source: https://theforumist.com/seance-with-goat/\n"
    )
    if "**Séance with Goat**" not in text:
        if heading not in text:
            raise SystemExit("Could not find direct-verification heading in source reconciliation")
        text = text.replace(heading, heading + bullet, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_corpus()
    update_article_metadata()
    update_portfolio_catalog()
    update_portfolio_yaml()
    update_primary_area_index()
    update_source_reconciliation()
    print("Reconciled Séance with Goat into canonical archive and public portfolio.")


if __name__ == "__main__":
    main()
