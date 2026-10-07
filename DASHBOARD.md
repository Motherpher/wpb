# WPB Archive Dashboard

![WPB Archive Dashboard](visuals/dashboard.svg)

## What you can see

The dashboard is the **single visual surface** for the repository. It is generated from the canonical archive data rather than maintained as a separate illustration.

It combines six views in one composition:

- **Archive size and readiness** — 39 verified works, 34 enriched article-metadata records, 12 portfolio candidates, 4 contextual credits, 2 unresolved dates and 39 A-grade authorship records.
- **Editorial structure** — every verified work is represented as one curve flowing into four analytical phases: 2 body/fashion research, 22 cultural journalism, 10 social-observational reporting and 5 long-form social reportage.
- **Metadata coverage** — 87% of works have additional publisher-level metadata enrichment; A-grade evidence covers 100% of the authored/research corpus; 5% still lack a resolved publication date.
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
