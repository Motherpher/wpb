# Repository map

## Dashboard
- `DASHBOARD.md` — human-readable status dashboard
- `data/dashboard.json` — aggregate machine-readable dashboard metadata
- `docs/DASHBOARD_SCHEMA.md` — dashboard field definitions and semantics

## Canonical data
- `data/corpus.json` — publication corpus
- `data/article-metadata.json` — article-level publisher metadata and creative credits
- `data/themes.json` — thematic taxonomy
- `data/outlets.json` — outlet registry
- `data/credits.json` — contextual, translation and unresolved non-authorship credits

## Human-readable archive
- `bibliography/master-bibliography.md`
- `sources/source-registry.md`
- `sources/unresolved-records.md`

## Portfolio content
- `content/profile.md`
- `content/bio-versions.md`
- `content/featured-work.md`
- `content/career-timeline.md`
- `content/themes.md`
- `content/method-and-style.md`

## Analysis
- `analysis/writer-dossier.md`
- `analysis/corpus-notes.md`

## Governance
- `docs/EVIDENCE_MODEL.md`
- `docs/EDITORIAL_POLICY.md`
- `docs/CONTENT_MODEL.md`
- `docs/site-roadmap.md`
- `CONTRIBUTING.md`

## Harvesting
- `harvest/harvest_wpb.py` — public-web metadata harvester
- `harvest/seeds.json` — identity variants, author pages and allowlisted domains
- `.github/workflows/harvest.yml` — manual GitHub Actions harvest
- `harvest/output/` — review-only run artifacts

## Visuals
- `visuals/corpus-timeline.svg`
- `visuals/career-arc.svg`
- `visuals/archive-to-portfolio.svg`
- `visuals/metadata-coverage.svg`
- editable Mermaid sources in `visuals/*.mmd`

## Future site
- `site/` remains framework-neutral until scope, visual identity and rights are settled.

## Reports
- `reports/` is reserved for rendered research outputs.
