from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "CareerHub/personalisation/portfolio-catalog.json"
PROFILE = ROOT / "CareerHub/personalisation/portfolio.yaml"
INDEX = ROOT / "WriterRoom/portfolio/PRIMARY_AREA_INDEX.md"
CONTRACT = ROOT / "CareerHub/personalisation/PORTFOLIO_CATALOG.md"
EXPANSION = ROOT / "WriterRoom/portfolio/RECONCILIATION_EXPANSION_2026-10-07.md"

ADDITIONS = [
    {
        "id": "2012-tako-maska-lwa",
        "date": "2012",
        "title": "Maska lwa",
        "outlet": "Tako",
        "language": "pl",
        "type": "book translation",
        "evidence": "A",
        "status": "verified",
        "url": "https://tako.biz.pl/p,83,maska-lwa",
        "themes": ["translation", "children's-literature", "picture-book", "Spanish-Polish"],
        "phase": "translation-publishing",
        "primary_area": "books-translation",
        "credit_role": "translator",
        "note": "Polish translation of Margarita del Mazo's La máscara del león; illustrations by Paloma Valdivia; Tako, 2012; ISBN 978-83-62737-08-6."
    },
    {
        "id": "2013-tako-niedzwiedz-lowca-motyli",
        "date": "2013-03-01",
        "title": "Niedźwiedź łowca motyli",
        "outlet": "Tako",
        "language": "pl",
        "type": "book translation",
        "evidence": "A",
        "status": "verified",
        "url": "https://lubimyczytac.pl/ksiazka/172052/niedzwiedz-lowca-motyli",
        "themes": ["translation", "children's-literature", "picture-book", "Spanish-Polish"],
        "phase": "translation-publishing",
        "primary_area": "books-translation",
        "credit_role": "translator",
        "note": "Polish translation of Susanna Isern's Oso Cazamariposas; illustrations by Marjorie Pourchet; Tako, first Polish edition 2013; ISBN 978-83-62737-17-8."
    },
    {
        "id": "pending-krull-whats-in-store-styling",
        "date": None,
        "title": "WHAT’S IN STORE?",
        "outlet": "Krull Magazine",
        "language": "en",
        "type": "fashion editorial styling",
        "evidence": "A",
        "status": "verified",
        "url": "https://krullmag.com/blog/whats-in-store/",
        "themes": ["fashion", "styling", "editorial", "Stockholm", "visual-culture"],
        "phase": "visual-editorial",
        "primary_area": "visual-editorial",
        "credit_role": "styling",
        "note": "Direct Krull editorial credit: styling WERONIKA PÉREZ BORJAS. Publication date remains unresolved."
    },
    {
        "id": "2018-tygodnik-adresat-bog",
        "date": "2018-12-24",
        "title": "Adresat: Bóg",
        "outlet": "Tygodnik Powszechny",
        "language": "pl",
        "type": "social/religion reportage",
        "evidence": "A",
        "status": "verified",
        "url": "https://www.tygodnikpowszechny.pl/adresat-bog-157064",
        "themes": ["religion", "Stockholm", "Sweden", "community", "faith", "social-observation"],
        "phase": "long-form-social-reportage",
        "primary_area": "long-form-reportage",
        "credit_role": "author",
        "note": "Direct Tygodnik Powszechny author page and article byline verify authorship and publication date."
    },
    {
        "id": "2019-tygodnik-pierwsza-pani-prymas",
        "date": "2019-03-25",
        "title": "Pierwsza pani prymas",
        "outlet": "Tygodnik Powszechny",
        "language": "pl",
        "type": "long-form profile/interview",
        "evidence": "A",
        "status": "verified",
        "url": "https://www.tygodnikpowszechny.pl/pierwsza-pani-prymas-158130",
        "themes": ["Sweden", "religion", "gender", "church", "MeToo", "migration", "institutions"],
        "phase": "long-form-social-reportage",
        "primary_area": "long-form-reportage",
        "credit_role": "author",
        "note": "Direct Tygodnik Powszechny author page and article byline verify the Antje Jackelén profile/interview and publication date."
    },
]

SOURCE_HUBS = [
    {"label": "VICE Polska contributor", "url": "https://www.vice.com/pl/contributor/weronika-perez-borjas/", "status": "reviewed-existing-writing-credits"},
    {"label": "Krull Magazine tag", "url": "https://krullmag.com/blog/tag/weronika-perez-borjas/", "status": "reviewed-new-styling-credit-found"},
    {"label": "The Forumist tag", "url": "https://theforumist.com/tag/weronika-perez-borjas/", "status": "reviewed-tag-incomplete-direct-bylines-retained"},
    {"label": "Tygodnik Powszechny author", "url": "https://www.tygodnikpowszechny.pl/autor/weronika-perez-borjas-18702", "status": "reviewed-two-new-authored-works-found"},
    {"label": "Lubimyczytac translator", "url": "https://lubimyczytac.pl/tlumacz/23615/weronika-perez-borjas", "status": "reviewed-translation-domain"},
    {"label": "Tako — Maska lwa", "url": "https://tako.biz.pl/p,83,maska-lwa", "status": "reviewed-translation-credit"},
    {"label": "IMDb", "url": "https://www.imdb.com/name/nm12788912/", "status": "pending-concrete-screen-credit-extraction"},
    {"label": "Filmweb filmography", "url": "https://www.filmweb.pl/person/Weronika+Perez+Borjas-725403/filmography", "status": "pending-concrete-screen-credit-extraction"},
]

AREA_ORDER = [
    ("long-form-reportage", "Long-form reportage"),
    ("culture-interviews", "Culture & interviews"),
    ("research-criticism", "Research & criticism"),
    ("transnational-reporting", "Transnational reporting"),
    ("books-translation", "Books & translation"),
    ("visual-editorial", "Visual & editorial"),
]


def sort_key(work: dict) -> tuple:
    date = work.get("date")
    return (date is None, date or "9999-99-99", work.get("id", ""))


def update_catalog() -> dict:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    works_by_id = {work["id"]: work for work in catalog.get("works", [])}
    for record in ADDITIONS:
        works_by_id[record["id"]] = record
    works = sorted(works_by_id.values(), key=sort_key)
    catalog["works"] = works
    catalog["work_count"] = len(works)
    catalog["classification_rule"] = (
        "Each public portfolio credit has exactly one primary portfolio area. "
        "Cross-cutting themes remain descriptive and do not duplicate a credit across area pages; "
        "non-author roles are explicit in credit_role."
    )
    roles = {"author": 0, "translator": 0, "styling": 0}
    for work in works:
        role = work.get("credit_role", "author")
        roles[role] = roles.get(role, 0) + 1
    catalog["credit_counts"] = {
        "authored_works": roles.get("author", 0),
        "translations": roles.get("translator", 0),
        "visual_editorial": roles.get("styling", 0),
        "total_portfolio_credits": len(works),
    }
    catalog["source_hubs"] = SOURCE_HUBS
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return catalog


def update_profile() -> None:
    text = PROFILE.read_text(encoding="utf-8")
    text = text.replace(
        'eyebrow: "Writer · reporter · researcher"',
        'eyebrow: "Writer · reporter · translator · researcher"',
    )
    text = text.replace(
        'headline: "Writing across borders, systems and lived experience."',
        'headline: "Writing, translation and visual editorial work across borders, systems and lived experience."',
    )
    text = text.replace(
        'intro: "Weronika Pérez Borjas is a writer and reporter whose published work moves across cultural criticism, interviews, social observation and long-form reportage. A recurring strength is cross-cultural translation: reporting that begins with people encountering institutions, borders, labour systems, law and public life."',
        'intro: "Weronika Pérez Borjas is a writer, reporter and translator whose portfolio moves across long-form reportage, cultural criticism, interviews, books and visual editorial work. A recurring strength is cross-cultural translation in both senses: translating texts between languages and reporting across institutions, borders, cultural systems and lived experience."',
    )
    anchor = '        - "2018-duzy-format-russians"\n        - "2019-duzy-format-nonbinary"'
    replacement = (
        '        - "2018-duzy-format-russians"\n'
        '        - "2018-tygodnik-adresat-bog"\n'
        '        - "2019-tygodnik-pierwsza-pani-prymas"\n'
        '        - "2019-duzy-format-nonbinary"'
    )
    if '2018-tygodnik-adresat-bog' not in text:
        if anchor not in text:
            raise SystemExit("Could not locate Long-form insertion anchor")
        text = text.replace(anchor, replacement)

    if 'slug: "books-translation"' not in text:
        section_block = '''  - label: "Books & translation"
    slug: "books-translation"
    description: "Published literary translation, with the translator role kept distinct from authored journalism."
    filter:
      ids:
        - "2012-tako-maska-lwa"
        - "2013-tako-niedzwiedz-lowca-motyli"

  - label: "Visual & editorial"
    slug: "visual-editorial"
    description: "Credited visual, styling and editorial work outside the authored-text archive."
    filter:
      ids:
        - "pending-krull-whats-in-store-styling"

'''
        text = text.replace("featured:\n", section_block + "featured:\n")

    text = text.replace("  count: 39\n", "  count: 44\n")
    text = text.replace(
        '  label: "verified works in the reconstructed public portfolio catalog"',
        '  label: "verified credits in the reconstructed public portfolio catalog"',
    )
    text = text.replace(
        '  note: "All currently verified reconstructed authored works are indexed under exactly one primary portfolio area. Featured work remains a curated selection. The archive remains reconstructed rather than claimed exhaustive until writer reconciliation is complete."',
        '  note: "The public catalog now contains 44 verified portfolio credits: 41 authored works, 2 book translations and 1 visual-editorial styling credit. Each credit appears in exactly one primary area and non-author roles are explicitly distinguished. The archive remains reconstructed rather than claimed exhaustive until screen credits and writer-supplied reconciliation are complete."',
    )
    PROFILE.write_text(text, encoding="utf-8")


def write_index(catalog: dict) -> None:
    by_area = {slug: [] for slug, _ in AREA_ORDER}
    for work in catalog["works"]:
        by_area.setdefault(work["primary_area"], []).append(work)
    lines = [
        "# Primary-area portfolio index",
        "",
        "This index mirrors `CareerHub/personalisation/portfolio-catalog.json` and exists for human audit. Each verified public portfolio credit has one primary area. Cross-cutting themes can still be multiple, and non-author roles are explicitly labelled.",
        "",
    ]
    for slug, label in AREA_ORDER:
        items = sorted(by_area.get(slug, []), key=sort_key)
        lines.append(f"## {label} — {len(items)}")
        lines.append("")
        for idx, work in enumerate(items, 1):
            date = work.get("date")
            year = date[:4] if date else "date unresolved"
            role = work.get("credit_role", "author")
            role_note = "" if role == "author" else f" — **{role} credit**"
            lines.append(f"{idx}. {work['title']} — {work['outlet']} ({year}){role_note}")
        lines.append("")
    counts = catalog["credit_counts"]
    lines.extend([
        f"**Total: {counts['total_portfolio_credits']} verified portfolio credits.**",
        "",
        f"Role breakdown: **{counts['authored_works']} authored works · {counts['translations']} translations · {counts['visual_editorial']} visual-editorial styling credit.**",
        "",
        "IMDb and Filmweb remain source hubs for a separate screen-credit reconciliation. No screen credit is counted until a concrete title and role can be verified.",
        "",
    ])
    INDEX.write_text("\n".join(lines), encoding="utf-8")


def write_contract() -> None:
    CONTRACT.write_text("""# Portfolio catalog contract

`portfolio-catalog.json` is the role-aware public portfolio source consumed by the CareerHub `/writer` surfaces.

It exists because the research corpus and the public portfolio have different responsibilities:

- `data/corpus.json` remains the canonical research archive and evidence record for the reconstructed writing corpus.
- `CareerHub/personalisation/portfolio-catalog.json` is the verified public portfolio projection used by the site. It can contain authored work and other professionally credited work such as translation or styling, but those roles must never be conflated.
- `portfolio.yaml` defines public sections, featured work and exact primary-area membership.

For every public portfolio credit:

1. the record must have a stable ID and evidence sufficient for public attribution;
2. `status` must be `verified`;
3. `primary_area` must match exactly one section slug in `portfolio.yaml`;
4. that ID must occur exactly once across the section `filter.ids` lists;
5. cross-cutting subjects belong in `themes`, not in additional primary-area placements;
6. a non-author contribution must carry an explicit `credit_role` such as `translator` or `styling`; authored records default to `author` for backward compatibility.

CI enforces the one-credit/one-primary-area partition and the declared catalog count.

The public catalog is reconstructed and should not be described as an exhaustive lifetime archive until writer reconciliation and unresolved screen-credit reconciliation are complete.
""", encoding="utf-8")


def write_expansion(catalog: dict) -> None:
    counts = catalog["credit_counts"]
    EXPANSION.write_text(f"""# Portfolio reconciliation expansion — 2026-10-07

## Scope

This pass expands the public portfolio beyond an authored-article-only model while preserving role integrity. The preceding 39-work reconciliation remains the historical record of the first complete writing partition; this addendum records newly verified writing, translation and visual-editorial credits.

## New verified authored work

### Tygodnik Powszechny

The publisher author page exposes two works absent from the preceding catalog:

1. **Adresat: Bóg** — 24 December 2018 — https://www.tygodnikpowszechny.pl/adresat-bog-157064
2. **Pierwsza pani prymas** — 25 March 2019 — https://www.tygodnikpowszechny.pl/pierwsza-pani-prymas-158130

Both are direct publisher bylines and are assigned to **Long-form reportage**.

## New verified translation credits

1. **Maska lwa** — Margarita del Mazo; illustrations Paloma Valdivia; Polish translation by Weronika Pérez Borjas; Tako, 2012; ISBN 978-83-62737-08-6. Publisher/source hub: https://tako.biz.pl/p,83,maska-lwa
2. **Niedźwiedź łowca motyli** — Susanna Isern; illustrations Marjorie Pourchet; Polish translation by Weronika Pérez Borjas; Tako, first Polish edition 2013; ISBN 978-83-62737-17-8. Bibliographic work page: https://lubimyczytac.pl/ksiazka/172052/niedzwiedz-lowca-motyli

These are public portfolio credits under **Books & translation**, not authored journalism.

## New verified visual-editorial credit

**WHAT’S IN STORE?** — Krull Magazine — https://krullmag.com/blog/whats-in-store/

The publisher page directly credits **styling WERONIKA PÉREZ BORJAS**. It is therefore included under **Visual & editorial** with `credit_role: styling`; it is not counted as an authored text. The publication date remains unresolved.

## Source-hub reconciliation

Reviewed source hubs supplied for this pass:

- IMDb — https://www.imdb.com/name/nm12788912/
- Filmweb filmography — https://www.filmweb.pl/person/Weronika+Perez+Borjas-725403/filmography
- Krull Magazine tag — https://krullmag.com/blog/tag/weronika-perez-borjas/
- The Forumist tag — https://theforumist.com/tag/weronika-perez-borjas/
- Tygodnik Powszechny author page — https://www.tygodnikpowszechny.pl/autor/weronika-perez-borjas-18702
- Lubimyczytac translator page — https://lubimyczytac.pl/tlumacz/23615/weronika-perez-borjas
- VICE Polska contributor page — https://www.vice.com/pl/contributor/weronika-perez-borjas/
- Tako / Maska lwa — https://tako.biz.pl/p,83,maska-lwa

The Krull, Forumist and VICE hubs strengthen or consolidate already catalogued credits. The Forumist tag is not treated as exhaustive because direct byline pages verify additional Forumist work not exposed on the current tag page.

IMDb and Filmweb identify a screen-work domain that still requires concrete title-and-role extraction. No film/screen item is counted merely because a name page exists. This avoids contaminating the public portfolio with an unverified role.

## Current public portfolio partition

| Area | Count |
| --- | ---: |
| Long-form reportage | 10 |
| Culture & interviews | 23 |
| Research & criticism | 4 |
| Transnational reporting | 4 |
| Books & translation | 2 |
| Visual & editorial | 1 |
| **Total** | **{counts['total_portfolio_credits']}** |

Role breakdown: **{counts['authored_works']} authored works · {counts['translations']} translations · {counts['visual_editorial']} visual-editorial styling credit.**

The portfolio remains reconstructed rather than claimed exhaustive. The next evidence frontier is the screen-credit domain plus any print-only, deleted, unindexed or writer-supplied work.
""", encoding="utf-8")


def main() -> None:
    catalog = update_catalog()
    update_profile()
    write_index(catalog)
    write_contract()
    write_expansion(catalog)
    print("PORTFOLIO ROLE-AWARE RECONCILIATION", catalog["credit_counts"])


if __name__ == "__main__":
    main()
