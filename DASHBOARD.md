# WPB Dashboard

> Machine-readable source: [`data/dashboard.json`](data/dashboard.json)

This dashboard summarizes the current state of the WPB archive and future portfolio content system. It is derived from the repository's canonical metadata; unknowns remain unknown rather than being guessed.

## Snapshot

| Metric | Current state |
|---|---:|
| Canonical works | **36** |
| A-grade authored/research records | **36** |
| Portfolio candidates | **12** |
| Exact-day dates | **15** |
| Year-only dates | **14** |
| Missing dates | **7** |
| Fully verified publication metadata | **29** |
| Partial publication metadata | **7** |
| Languages represented | **2** |
| Outlet labels represented | **10** |
| Contextual/non-authorship credits | **3** |

## Portfolio readiness

- **Selected candidates:** 12
- **Final writer-approved selection:** pending
- **Final writer-approved biography:** pending
- **Rights review:** not yet performed
- **Visual asset review:** not yet performed
- **Frontend implementation:** not started
- **Site architecture:** framework-neutral by design

No work is treated as publication-ready for the portfolio merely because it is marked `featured`. That flag currently means **candidate**.

## Corpus by phase

- **body-fashion-research:** 2
- **cultural-journalism:** 20
- **social-observational-reporting:** 9
- **long-form-social-reportage:** 5

## Corpus by language

- **pl:** 11
- **en:** 25

## Date completeness

- Missing date: **Fatoumata Diawara** — Krull Magazine (`krull-fatoumata-diawara`)
- Missing date: **Henry Rude – Max of Wax** — Krull Magazine (`krull-henry-rude`)
- Missing date: **Joanna Lemnelius – Mixed Grill, Motherhood and Business** — Krull Magazine (`krull-joanna-lemnelius`)
- Missing date: **All That Jazz** — Krull Magazine (`krull-all-that-jazz`)
- Missing date: **The 27th Edition of Stockholm Film Festival** — Krull Magazine (`krull-stockholm-film-festival`)
- Missing date: **Saving Music in Mali – an Interview with Lutz Gregor** — Krull Magazine (`krull-mali-blues`)
- Missing date: **Tempo Documentary Festival Tips** — Krull Magazine (`krull-tempo`)

## Data-quality flags

- The corpus currently mixes **canonical theme IDs** with **descriptive free-form tags**.
- 36 of 36 records contain at least one descriptive tag outside the eight-ID canonical theme file.
- 7 records have partial publication metadata rather than the repository's strongest verified status.
- Rights and image/asset status are deliberately **not assessed** until there is an explicit review.
- The archive remains reconstructed rather than exhaustive.

## Theme frequency

Raw tags are shown as recorded; this is **not** yet a normalized taxonomy.

- **music:** 14
- **identity:** 9
- **migration:** 7
- **body:** 6
- **Stockholm:** 6
- **Sweden:** 6
- **fashion:** 5
- **diaspora:** 4
- **institutions:** 4
- **place:** 4
- **race:** 4
- **art:** 3
- **Poland:** 3
- **representation:** 3
- **Africa:** 2
- **community:** 2
- **creative-process:** 2
- **Cuba:** 2
- **documentary:** 2
- **family:** 2

## Open workstreams

1. **Issue #1 — Corpus completion:** dates, direct URLs, archived pages, unindexed/print work, educational chronology.
2. **Issue #2 — Portfolio Phase 1:** positioning, biography, final selected work, rights, imagery, languages, visual direction.

## Dashboard metadata on each work

Every record in `data/corpus.json` now contains a `dashboard` object with:

- date precision
- source completeness
- evidence grade
- portfolio candidacy/readiness
- rights status
- visual-asset status
- public-copy status
- required metadata completeness
- canonical vs descriptive theme tags
- dashboard flags

This makes the corpus usable directly by a future admin dashboard or public portfolio without inventing a second metadata system.

## Status semantics

- **verified** — strong publication metadata currently recorded
- **verified-partial-metadata** — work/title/URL verified, but one or more publication details remain incomplete
- **candidate-needs-editorial-and-rights-review** — potentially portfolio-worthy, not yet approved for public portfolio use
- **not-assessed** — no review has been performed; it does not mean unavailable or prohibited
- **mixed-taxonomy** — theme field contains both canonical and descriptive tags

See [`docs/DASHBOARD_SCHEMA.md`](docs/DASHBOARD_SCHEMA.md) for the machine-readable model.
