![WPB Archive Dashboard](visuals/dashboard.svg)

### What this shows

The dashboard above belongs to the **Writer & Journalism Room**. It is generated from the publication archive and combines corpus size, editorial phases, metadata completeness, publication chronology, research workflow and portfolio readiness. One curve in the central field represents one verified work.

> **Weronika:** start with [START_HERE.md](START_HERE.md). The WPB profile now has two separate rooms: your [Writer & Journalism Room](WriterRoom/CONTROL_ROOM.md) and [CareerHub](CareerHub/CONTROL_ROOM.md).

> **Profile architecture:** [PROFILE_ARCHITECTURE.md](PROFILE_ARCHITECTURE.md) · **Writer dashboard:** [DASHBOARD.md](DASHBOARD.md) · **Discovery system:** [harvest/README.md](harvest/README.md)

# WPB — Weronika Pérez Borjas

Private profile workspace for writer and reporter **Weronika Pérez Borjas**.

The profile contains two separate operational rooms:

1. **[Writer & Journalism Room](WriterRoom/README.md)** — the body of work: writing, reporting, research, publication archive, editorial development and portfolio.
2. **[CareerHub](CareerHub/README.md)** — the career-search layer: job sourcing, vacancy analysis, application preparation and recruitment follow-up.

These are peer rooms. CareerHub does not own the writer archive or editorial work, and the Writer & Journalism Room does not own job-search/application state.

## Writer & Journalism Room

The writer room currently grows from the reconstructed archive and corpus of Pérez Borjas's published work. It serves two connected purposes:

1. **Archive and research** — reconstruct, verify and analyse published work across journalism, cultural writing, academic publishing and translation.
2. **Writer workspace and portfolio base** — provide a structured base for current/future writing work, editorial development and a public-facing portfolio or writer site without rebuilding the underlying bibliography and metadata.

The current archive is substantial but not claimed to be exhaustive. Older publication archives are incomplete, some author pages have lost historical entries, and some material may survive only in print or migrated web archives.

Open the [Writer & Journalism Room Control Room](WriterRoom/CONTROL_ROOM.md).

## CareerHub

CareerHub is deliberately separate from the writer room. It handles the practical employment/application process:

**Find jobs → Analyse? → Apply → Follow the case**

Open the [CareerHub Control Room](CareerHub/CONTROL_ROOM.md).

CareerHub may use explicitly selected and verified evidence from the writer room for applications, but it must not automatically ingest unpublished drafts, reporting notes, confidential sources or unresolved archive material. See [WriterRoom/ROOM_BOUNDARY.md](WriterRoom/ROOM_BOUNDARY.md).

## Writer-room research dashboard

- [Integrated archive dashboard](DASHBOARD.md) — the writer-room data-visual surface, generated from canonical metadata
- [Visual system](visuals/README.md) — design and automation notes for the integrated SVG
- [Metadata harvester](harvest/README.md) — repeatable public-web discovery workflow

The dashboard is regenerated automatically when canonical corpus, article-metadata or credit data changes.

## Repository map

### Profile-level rooms

- `WriterRoom/` — writer/journalist navigation, workroom boundary and future active-work layer
- `CareerHub/` — job sourcing, triage, HRDM-R matching, application drafting and recruitment workflow

### Writer & Journalism Room estate

The archive predates the `WriterRoom/` directory and remains at root for compatibility. These paths are functionally owned by the writer room:

- `data/` — machine-readable corpus, outlets and theme taxonomy
- `content/` — portfolio-ready profile, chronology, thematic essays and featured-work copy
- `analysis/` — research analysis of the writing, methods and development
- `bibliography/` — reconstructed publication bibliography
- `sources/` — evidence model, source registry and unresolved records
- `harvest/` — discovery and metadata-harvesting system
- `docs/` — archive rules, editorial policy and future site architecture
- `reports/` — durable research reports and export notes
- `visuals/` — archive/portfolio visual system

Physical migration of those paths under `WriterRoom/` should happen only after dependent links, scripts and workflows have been audited.

## Working interpretation

Across the corpus, a consistent line can be traced from early work on **fashion, anatomy and bodily representation** toward cultural journalism and later long-form social reportage on **migration, gender, labour, healthcare, reproductive rights, borders and institutions**.

A recurring analytical question is:

> What happens when lived human experience does not fit the categories through which institutions, cultures or societies attempt to organise it?

This is a repository-level interpretation of the corpus, not a statement attributed to Pérez Borjas herself.

## Core research principles

- Primary publication evidence takes precedence.
- Authorship is kept separate from employment, translation, press-office and incidental credits.
- Facts, interpretation and unresolved claims are labelled separately.
- Original titles, dates, outlets and languages are retained where possible.
- Broken or migrated links are documented rather than silently replaced.
- No personal characteristic is inferred beyond what reliable published sources establish.
- Copyright remains with the original author and publishers. This repository should link to original publications rather than reproduce copyrighted articles in full.

## Evidence grades

- **A — Verified authorship:** direct byline, author page, journal record or equivalent primary publication evidence.
- **B — Verified contextual/professional record:** employment, press-office, academic affiliation, translation or other professional evidence that does not establish authorship of a specific text.
- **C — Unresolved/provisional association:** plausible connection requiring further verification.

## Editorial phases used in the archive

1. **Body & fashion research** — anatomy, fashion, bodily difference, visual representation.
2. **Cultural journalism** — music, art, cities, diaspora, subculture, spirituality.
3. **Social-observational reporting** — migration, motherhood, race, bodies, LGBT politics, national identity.
4. **Long-form social reportage** — migration systems, gender recognition, healthcare, labour, reproductive rights, borders and state institutions.

These phases overlap. They are analytical tools, not fixed career labels.

## Future writer/portfolio architecture

The Writer & Journalism Room deliberately separates **content from presentation**. A later website can consume `data/corpus.json` and Markdown under `content/` while the archival and research layers remain intact.

Potential site sections:

- Home / writer profile
- Selected work
- Full archive
- Themes
- About
- Research & academic work
- Languages / geographies
- Contact / representation
- Source and archive note

See `docs/site-roadmap.md` for the proposed implementation path.

## Copyright & independence

The archive component began as an independent archival and research reconstruction and should not be presented as an official bibliography or definitive biography unless Weronika explicitly adopts it as such.

Copyright in original articles, photographs, books, translations and other published works remains with their respective rights holders. Repository-authored metadata and analysis are provided for research, documentation and portfolio-development purposes.

---

**Repository:** https://github.com/Motherpher/wpb  
**Maintainer:** Motherpher / Hybrismannen
