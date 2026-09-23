# Repository map

## Dashboard
- `visuals/dashboard.svg` — **single canonical integrated data visual**
- `DASHBOARD.md` — human-readable explanation of the dashboard
- `data/dashboard.json` — aggregate machine-readable dashboard metadata
- `scripts/build_outputs.py` — generator for all derived dashboard outputs
- `.github/workflows/sync-derived.yml` — automatic regeneration/commit workflow
- `.github/workflows/validate.yml` — integrity and derived-output drift checks
- `docs/DASHBOARD_SCHEMA.md` — dashboard field definitions and semantics

## Canonical data
- `data/corpus.json` — publication corpus
- `data/article-metadata.json` — article-level publisher metadata and creative credits
- `data/themes.json` — thematic taxonomy
- `data/outlets.json` — outlet registry
- `data/credits.json` — contextual, translation and unresolved non-authorship credits
- `data/discovery-scope.json` — exhaustive-discovery coverage model

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
- `docs/HARVEST_PROTOCOL.md` — exhaustive discovery protocol
- `CONTRIBUTING.md`

## Harvesting
- `harvest/harvest_wpb.py` — public-web metadata harvester
- `harvest/seeds.json` — identity variants, author pages and allowlisted domains
- `.github/workflows/harvest.yml` — manual GitHub Actions harvest
- `harvest/output/` — review-only run artifacts

## Visuals
- `visuals/dashboard.svg` — the only current public data visual
- `visuals/README.md` — design and automation notes

Earlier standalone charts remain available through Git history but are intentionally retired from the current branch.

## CareerHub
- `CareerHub/CONTROL_ROOM.md` — Weronika's job-search control room
- `CareerHub/profile/candidate.yaml` — sanitized public-evidence candidate profile
- `CareerHub/config/search_profiles.yaml` — core / adjacent / bridge search lanes
- `CareerHub/config/sources.yaml` — provider registry
- `CareerHub/hrdm/HRDM_R_v6.3.md` — canonical HRDM Reverse workflow
- `CareerHub/scripts/careerhub.py` — CLI entrypoint
- `CareerHub/src/careerhub/` — source, triage, HRDM, application and dashboard engine
- `.github/workflows/careerhub-scan.yml` — manual + weekday sourcing/ranking refresh
- `.github/workflows/careerhub-drill.yml` — one-job HRDM/research/application/DOCX pack
- `.github/workflows/careerhub-validate.yml` — offline integrity and DOCX smoke tests
- `CareerHub/docs/SOURCE_MATRIX.md` — provider/API strategy
- `CareerHub/docs/WORKFLOW.md` — end-to-end operating model

## Future site
- `site/` remains framework-neutral until scope, visual identity and rights are settled.

## Reports
- `reports/` is reserved for rendered research outputs.
