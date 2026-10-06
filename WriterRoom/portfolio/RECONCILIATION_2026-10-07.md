# Portfolio reconciliation — 2026-10-07

## Purpose

Reconcile the public Writer portfolio against the repository archive and direct publisher evidence, then ensure every currently verified authored work is reachable through exactly one primary portfolio-area sub-site.

## Defect found

The first portfolio implementation connected the four area cards to broad search filters. Those filters used OR semantics across phase, type, theme and free-text conditions. This caused the same work to appear under multiple buttons while other archive records were silently omitted.

A second defect was the archive loader's strict `status == verified` rule. The canonical repository bibliography described 38 reconstructed works, but the site loaded only 31 records from `data/corpus.json` because not every A-grade archive item used that exact status value.

Result before reconciliation: the visible section counts overlapped and did not form a complete partition of the work.

## Sources reviewed

Repository-wide review included the canonical corpus, article metadata, master bibliography, WriterRoom portfolio rules, content model, recurring themes, writer dossier, source registry and harvest protocol.

External reconciliation used direct publisher pages and bylines as the preferred evidence layer. Search results were treated as discovery evidence only; a work was added to the public catalog only where direct publisher evidence supported authorship.

## Newly recovered direct-publisher work

### Into the Sound — The Forumist

- URL: https://theforumist.com/into-the-sound/
- byline: Weronika Pérez Borjas
- year: 2015
- primary area: Culture & interviews
- status: verified for public catalog
- significance: direct publisher byline found during the 2026-10-07 portfolio reconciliation; it was not present in the previous 38-work canonical bibliography.

This raises the currently verified reconstructed public catalog from 38 to 39 authored works. The repository must still describe the body of work as reconstructed rather than proven exhaustive until writer-supplied reconciliation is complete.

## Primary taxonomy

The public portfolio now uses one explicit `primary_area` per work. Themes remain multi-valued and can describe cross-cutting subjects without causing duplicate placement.

| Area | Count | Function |
| --- | ---: | --- |
| Long-form reportage | 8 | Long-form, field and social reporting on institutions, rights, gender, labour and public life |
| Culture & interviews | 23 | Music, art, film, subculture, urban life and conversations with cultural/creative actors |
| Research & criticism | 4 | Academic, analytical and essayistic work on fashion, visual culture, body and representation |
| Transnational reporting | 4 | Reporting where migration, borders, belonging and cross-border systems are the primary frame |
| **Total** | **39** | **Every current verified authored work assigned once** |

## Public-site contract

- `/writer` is the portfolio overview and displays the exact primary-area counts.
- `/writer/long-form-reportage` contains the 8 works assigned to that mode.
- `/writer/culture-interviews` contains the 23 works assigned to that mode.
- `/writer/research-criticism` contains the 4 works assigned to that mode.
- `/writer/transnational-reporting` contains the 4 works assigned to that mode.
- `/writer/all` contains all 39 currently verified reconstructed authored works.
- Featured work remains a curated subset and does not control archive completeness.

## Exclusions

Professional-context records such as communications/press roles, institutional profiles or role references are not automatically treated as authored portfolio work. The repository's harvest protocol requires a specific authored work or direct authorship evidence for inclusion in the authored-work catalog.

## Remaining completeness boundary

This reconciliation fixes the site taxonomy and current verified public catalog. It does not claim that the public web proves Weronika's complete lifetime output. Print-only work, deleted commissions, translations, editing, audio/film, talks and other material still require long-tail harvest and/or Weronika's own reconciliation.
