# Dashboard metadata schema

The WPB dashboard is a **single integrated derived surface** for repository governance and a future portfolio/admin interface.

## Source-of-truth rule

Canonical research data lives in:

- `data/corpus.json` — authored/research works
- `data/article-metadata.json` — publisher metadata and creative credits
- `data/credits.json` — contextual, translation and unresolved non-authorship credits
- `data/themes.json` — theme registry
- `data/outlets.json` — outlet registry

Derived data and presentation live in:

- `data/dashboard.json`
- `DASHBOARD.md`
- `bibliography/master-bibliography.md`
- `visuals/dashboard.svg`

The integrated SVG is the **only canonical public data visual**.

## Automation

`scripts/build_outputs.py` regenerates every derived dashboard surface from canonical JSON.

`.github/workflows/sync-derived.yml` runs automatically when the canonical corpus, article metadata, credits or the builder changes. If derived outputs change, the workflow commits them back to the repository.

`.github/workflows/validate.yml` then verifies:

- JSON validity
- unique corpus IDs
- article-metadata coverage for every corpus record
- dashboard metadata on each work
- SVG validity
- zero drift between canonical data and generated outputs

Harvest discoveries are **not** promoted automatically into the canonical corpus; they pass through the evidence review gate first.

## Integrated dashboard sections

The SVG contains six coordinated views:

1. KPI strip
2. editorial-phase flow
3. metadata coverage
4. publication timeline
5. Discover → Verify → Structure → Interpret → Publish pipeline
6. portfolio readiness

One central flow curve represents one verified work.

## Work-level dashboard metadata

Each work in `data/corpus.json` retains its `dashboard` object.

### Date precision
- `exact-day`
- `year`
- `unknown`
- `other`

### Source completeness
- `verified`
- `verified-partial-metadata`
- `missing-url`
- `review`

### Portfolio state
A `featured: true` work is a **candidate**, not a writer-approved selection.

Record-level portfolio metadata tracks:

- candidacy/readiness
- rights status
- visual-asset status
- public-copy status

### Taxonomy
Canonical theme IDs and descriptive/free-form tags remain distinguishable. No silent normalization is performed.

## Aggregate status semantics

- **verified** — strong publication metadata recorded
- **verified-partial-metadata** — authorship/work is verified but some publication metadata remains incomplete
- **pending-writer-review** — requires Weronika's editorial confirmation
- **not-assessed** — no rights/asset review has yet been performed
- **unresolved** — evidence is insufficient for a firmer classification

Unknown is preserved as unknown rather than converted into an assumption.
