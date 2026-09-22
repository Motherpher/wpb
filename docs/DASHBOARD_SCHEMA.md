# Dashboard metadata schema

The WPB dashboard layer supports repository governance now and a future portfolio/admin interface later.

## Source-of-truth rule

- `data/corpus.json` remains the canonical source for authored/research works.
- `data/credits.json` remains canonical for contextual, translation and unresolved non-authorship credits.
- `data/themes.json` remains the canonical theme registry.
- `data/outlets.json` remains the canonical outlet registry.
- `data/dashboard.json` is a **derived aggregate**, not a replacement source of truth.

## Work-level dashboard metadata

Each work in `data/corpus.json` now contains a `dashboard` object.

### Date
`date_precision`:
- `exact-day`
- `year`
- `unknown`
- `other`

### Source
`source_completeness`:
- `verified`
- `verified-partial-metadata`
- `missing-url`
- `review`

### Portfolio
The `portfolio` object contains:
- `candidate`
- `readiness`
- `rights_status`
- `visual_asset_status`
- `public_copy_status`

Important: a current `featured: true` record is a **portfolio candidate**, not a writer-approved final selection.

### Metadata completeness
The `metadata` object counts required fields and lists any missing required fields.

Publication date completeness is tracked separately, because exact dating and work verification are different questions.

### Taxonomy
The `taxonomy` object separates:
- canonical theme tags
- descriptive/free-form theme tags
- normalization status

No silent theme mapping is performed.

### Flags
Action/status flags can include:
- `missing-date`
- `partial-publication-metadata`
- `portfolio-candidate`

## Contextual-credit dashboard metadata

Each record in `data/credits.json` includes:
- authored-corpus inclusion logic
- verification status
- portfolio relevance
- rights status

This keeps press-office roles, translation credits and unresolved film associations from being counted as authored journalism.

## Theme dashboard metadata

Each canonical theme in `data/themes.json` includes:
- exact tag use count
- matching work IDs
- taxonomy status
- a reminder that descriptive tags are not automatically mapped

## Outlet dashboard metadata

Each outlet in `data/outlets.json` includes:
- corpus work count
- featured candidate count
- represented languages
- represented career phases
- unresolved date count
- metadata status

## Aggregate dashboard

`data/dashboard.json` contains:
- project status
- corpus totals
- evidence, language, phase, outlet and year distributions
- date/source completeness
- raw theme frequency
- portfolio readiness
- contextual-credit counts
- data-quality flags
- open workstreams and next decisions

`DASHBOARD.md` is the human-readable view.

## Status semantics

- **verified** — strong publication metadata recorded
- **verified-partial-metadata** — work/title/URL verified but one or more publication details remain incomplete
- **candidate-needs-editorial-and-rights-review** — potential portfolio work, not yet approved for public use
- **not-assessed** — no review has yet been performed
- **mixed-taxonomy** — the work uses one or more descriptive tags outside the canonical theme IDs
- **unresolved** — evidence is insufficient for a firmer classification

## Rule for unknowns

Use `not-assessed`, `unknown` or `unresolved` rather than inference. This is especially important for rights, assets, exact dates, current biography and portfolio approval.
