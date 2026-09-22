# WPB exhaustive discovery protocol

The word **exhaustive** is treated here as a research objective, not as a claim that the public web can prove completeness.

A defensible “full archive” requires multiple discovery layers, independent corroboration and an explicit residual-unknown queue.

## 1. Direct publication layer

Start with publisher evidence:

- article pages
- journal records
- outlet author pages
- tag/category archives
- publication search pages
- canonical/JSON-LD/OpenGraph metadata

A direct byline is the preferred basis for A-grade authored-work records.

## 2. Publisher-archive layer

Reconcile each outlet in both directions:

**known work → publisher** and **publisher index → corpus**.

This catches the common failure mode where an old article survives but disappears from the author's current archive page, or an author page exists but omits migrated legacy content.

## 3. Search layer

Run all identity variants:

- Weronika Pérez Borjas
- Weronika Perez Borjas
- hyphenated variants
- exact “Words by …” / byline phrases
- outlet-restricted searches
- title + name searches
- role terms: writer, journalist, reporter, translator, styling, press, editor

Search results are discovery evidence, not automatic authorship evidence.

## 4. Historical-web layer

For every verified or candidate URL:

- query Wayback CDX
- retain capture timestamps and digests
- use snapshots to recover legacy metadata where the live page has degraded
- document redirects and migrated slugs

Do not use archives to bypass material that was access-controlled at publication time.

## 5. Scholarly layer

Query:

- publisher DOI metadata
- Crossref
- OpenAlex
- university/institutional repositories
- secondary academic indexes as leads

Record DOI, journal, volume, issue, pages, keywords, affiliation and publication dates where supported.

## 6. Library / translation layer

Search public catalogues and ISBN records for:

- translations
- edited books
- chapters
- print publications
- alternate editions
- audiobook/accessible editions

Keep translation credits distinct from original authorship.

## 7. Professional-context layer

Search institutional press rooms, festival archives and organisations for:

- press/communications roles
- talks and panels
- teaching
- festival work
- editorial roles
- film/audio credits

These are normally B-grade contextual records unless a specific authored work is independently established.

## 8. Credit-graph layer

Creative credits are useful both as metadata and reverse-discovery paths.

For each article, capture where available:

- photographer
- illustrator
- stylist
- hair/make-up
- editor
- producer
- press-material source
- collaborating organisation

A collaborator's portfolio may preserve a disappeared article URL or date.

## 9. Visual-asset layer

Discover public image references, but do not assume reuse rights.

Record:

- lead-image URL
- credited creator
- publisher/source
- potential portfolio relevance
- rights status

No public image becomes a portfolio asset until the rights position is reviewed.

## 10. Writer-supplied reconciliation

Public-web research cannot prove a complete career archive.

The final completeness test is a reconciliation with Weronika herself:

- missing clips
- print-only material
- commissioned or deleted work
- translations
- editing
- talks/panels
- audio/film
- teaching
- work she does or does not want represented

This layer can turn a reconstructed archive into an authoritative personal archive.

## Automated implementation

`harvest/harvest_wpb.py` currently supports:

- canonical corpus seeds
- curated author/tag pages
- identity variants
- allowlisted crawling
- robots.txt
- rate limiting
- HTML/meta/JSON-LD extraction
- credit-line detection
- image references
- visible-text word count + SHA-256 fingerprint
- Wayback CDX
- Crossref
- OpenAlex
- optional Brave Search API
- review outputs rather than automatic canonical writes

See `harvest/README.md`.

## What the harvester deliberately does not do

- bypass paywalls
- log into accounts
- evade anti-bot controls
- store full copyrighted article text
- infer authorship from a name mention
- treat search-engine snippets as final evidence
- infer sensitive personal characteristics

## Completion state

The current public corpus is substantial, but the project should continue to describe itself as **reconstructed, not proven exhaustive** until the automated long-tail harvest and writer reconciliation are both complete.
