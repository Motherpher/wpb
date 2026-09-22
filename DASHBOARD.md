# WPB Dashboard

> Machine-readable source: [`data/dashboard.json`](data/dashboard.json) · Article metadata: [`data/article-metadata.json`](data/article-metadata.json) · Harvest system: [`harvest/`](harvest/)

This dashboard summarizes the current state of the WPB archive and future portfolio content system.

![WPB corpus timeline](visuals/corpus-timeline.svg)

## Snapshot

| Metric | Current state |
|---|---:|
| Canonical authored/research works | **38** |
| A-grade records | **38** |
| Portfolio candidates | **12** |
| Exact-day dates | **16** |
| Year-only dates | **20** |
| Missing dates | **2** |
| Strongly verified publication records | **31** |
| Partial publication metadata | **7** |
| Article metadata records | **38** |
| Manually enriched publisher records | **33** |
| Contextual/non-authorship credits | **4** |

## Visual overview

- [Corpus timeline](visuals/corpus-timeline.svg)
- [Career arc](visuals/career-arc.svg)
- [Archive → portfolio research pipeline](visuals/archive-to-portfolio.svg)
- [Metadata coverage](visuals/metadata-coverage.svg)

## Corpus by phase

- **body-fashion-research:** 2
- **cultural-journalism:** 21
- **social-observational-reporting:** 10
- **long-form-social-reportage:** 5

## Corpus by language

- **pl:** 12
- **en:** 26

## Date completeness

- Missing exact year/date: **Henry Rude – Max of Wax** — Krull Magazine (`krull-henry-rude`)
- Missing exact year/date: **Joanna Lemnelius – Mixed Grill, Motherhood and Business** — Krull Magazine (`krull-joanna-lemnelius`)

## Article-level metadata

`data/article-metadata.json` now provides a separate enrichment layer for bylines, publication timestamps, creative credits, DOI/academic fields, event context and discovery evidence. It does not duplicate full article text.

## Harvest capability

The repository now includes a repeatable public-web metadata harvester. It can combine the canonical corpus, author/tag pages, robots-aware allowlisted crawling, Internet Archive CDX, Crossref, OpenAlex and optional Brave Search discovery.

Generated harvest results are **review inputs**, not automatic corpus truth.

## Portfolio readiness

- Final writer-approved selection: **pending**
- Final writer-approved biography: **pending**
- Rights review: **not yet performed**
- Visual asset review: **not yet performed**
- Frontend implementation: **not started**
- Site architecture: **framework-neutral**

## Data-quality cautions

- Theme tags still mix canonical taxonomy IDs and descriptive free-form tags.
- 2 records still lack a resolved publication date.
- 7 records remain partial at publication-metadata level.
- Rights and reusable visual assets remain deliberately unassessed until explicit review.
- The corpus is reconstructed and substantial, but not claimed to be exhaustive.

See [`docs/DASHBOARD_SCHEMA.md`](docs/DASHBOARD_SCHEMA.md) and [`harvest/README.md`](harvest/README.md).
