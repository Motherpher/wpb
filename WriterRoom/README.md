# Weronika Portfolio

This is Weronika Pérez Borjas's **professional writing and journalism workspace** inside the WPB profile.

It is deliberately separate from **CareerHub**.

- **Weronika Portfolio** = the work itself: writing, reporting, research, editorial development, publication archive and portfolio.
- **CareerHub** = finding roles, analysing job opportunities, preparing applications and following recruitment cases.

Neither room owns the other.

## Manifest

[`writerroom.yaml`](writerroom.yaml) is the machine-readable room manifest.

## What belongs here

Weronika Portfolio is the home for:

- current and future writing/reporting projects;
- ideas, pitches and commissions;
- research and source work;
- drafts and revision history;
- editorial review and development;
- published journalism and writing;
- reconstructed bibliography and source evidence;
- publication records and provenance;
- portfolio selection and presentation;
- writer biography/profile development;
- translation/editorial work connected to the writing practice;
- rights and attribution;
- analysis of the body of work.

## Operational desks

The workspace is organised conceptually around these functions:

1. **Work Desk** — current stories, drafts, commissions and status.
2. **Pitch Desk** — pitch development, sending, follow-up and commissioning.
3. **Reporting Desk** — story question, actors, institutions, interviews, claims and open questions.
4. **Research & Source Desk** — research evidence plus security-aware source handling.
5. **Writing Desk** — manuscripts and version lineage.
6. **Editorial Desk** — structure, source/referential control, style and deployment review.
7. **Publication Desk** — final publication records and provenance.
8. **Archive** — reconstructed body of published work.
9. **Portfolio** — selected public-facing representation.

Supporting specifications:

- [Work lifecycle](work/lifecycle.yaml)
- [Editorial Desk](editorial/README.md)
- [Publication Desk](publication/README.md)
- [Portfolio](portfolio/README.md)
- [Rights & attribution](rights/README.md)
- [Security & source protection](security/README.md)
- [Work-item templates](templates/)

## What does not belong here

The following stays in [CareerHub](../CareerHub/README.md):

- vacancy sourcing;
- job ranking;
- HRDM-R job-ad analysis;
- application drafting;
- recruitment deadlines;
- interview/application tracking;
- offers, denials and job-search state.

## Current archive estate

The existing WPB archive predates this workspace and remains in its stable repository paths for compatibility. These paths are functionally owned by Weronika Portfolio:

- [`../data/`](../data/) — canonical corpus and structured metadata
- [`../bibliography/`](../bibliography/) — reconstructed publication bibliography
- [`../content/`](../content/) — profile, featured work and portfolio-ready copy
- [`../analysis/`](../analysis/) — analysis of the work and writer dossier
- [`../sources/`](../sources/) — evidence, source registry and unresolved records
- [`../harvest/`](../harvest/) — discovery/metadata-harvesting system
- [`../reports/`](../reports/) — durable research and archive reports
- [`../visuals/`](../visuals/) — archive/portfolio visual system
- [`../docs/`](../docs/) — archive/editorial/site documentation

The archive has **not** been physically moved in v1.0 so existing links and automation remain intact.

## Working lifecycle

Canonical states are defined in [`work/lifecycle.yaml`](work/lifecycle.yaml):

**Idea → Pitch → Commissioned → Research → Reporting → Draft → Edit → Source/Fact Check → Submitted → Published → Archived → Portfolio Review**

Not every piece must pass through every stage.

## Security classifications

Weronika Portfolio recognises:

**PUBLIC → INTERNAL → CONFIDENTIAL → PROTECTED_SOURCE**

Protected-source material must not enter CareerHub, public surfaces or general AI workflows. GitHub is not treated as a sufficient protected-source vault merely because the repository is private.

See [security/README.md](security/README.md).

## Editorial review

`The Writer and the Beast` / Publicist may be used as an optional editorial-review protocol inside the Editorial Desk. It is advisory. Weronika retains authorship and editorial authority.

## Controlled bridge to CareerHub

CareerHub may use only **explicitly approved, provenance-preserving career evidence** from this workspace.

The bridge is defined in:

[`../bridges/writer-career-evidence/export.yaml`](../bridges/writer-career-evidence/export.yaml)

CareerHub must not automatically ingest drafts, private reporting notes, unpublished sources, unresolved archive material or editorial comments.

See [ROOM_BOUNDARY.md](ROOM_BOUNDARY.md).

## Start

Open [CONTROL_ROOM.md](CONTROL_ROOM.md) for the Weronika Portfolio navigation surface.
