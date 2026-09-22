# WPB metadata harvester

This directory contains a reproducible public-web discovery and metadata-harvesting workflow for the WPB archive.

## Purpose

The harvester is designed to find **as much public evidence as possible** about Weronika Pérez Borjas and her published/professional corpus while preserving the repository's evidence and copyright rules.

It can collect:

- canonical URLs and redirects
- page titles and descriptions
- bylines / author metadata
- publication and modification dates
- language and section
- JSON-LD / schema.org article metadata
- OpenGraph and Twitter-card metadata
- DOI and academic metadata
- keywords/tags
- image URLs and image metadata references
- visible credit lines
- word counts and content fingerprints for deduplication
- internal links from known author/archive pages
- Internet Archive CDX captures
- Crossref and OpenAlex records
- optional Brave Search discovery results
- robots.txt decisions, HTTP status and retrieval errors

It **does not store full article bodies** and does not bypass logins, paywalls, anti-bot systems or access controls.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r harvest/requirements.txt
```

## Normal run

```bash
python harvest/harvest_wpb.py --wayback --crossref --openalex
```

This uses:
1. every URL already present in `data/corpus.json`,
2. curated author/tag pages in `harvest/seeds.json`,
3. one-hop links found on positive author/archive pages.

## Deep domain discovery

```bash
python harvest/harvest_wpb.py --deep --max-pages 750 --wayback --crossref --openalex
```

Deep mode follows same-domain HTML links only on the allowlist, honours robots.txt, rate-limits requests, and stops at `--max-pages`.

## Search-engine discovery

If you have a Brave Search API key:

```bash
export BRAVE_SEARCH_API_KEY="..."
python harvest/harvest_wpb.py --brave-search --wayback --crossref --openalex
```

The key is read only from the environment and must never be committed.

## Output

Generated files go to `harvest/output/`:

- `all_fetched_metadata.jsonl` — metadata for every fetched page
- `positive_matches.jsonl` — pages with strong WPB identity evidence
- `candidate_urls.csv` — review queue
- `wayback_captures.jsonl` — archived URL/capture evidence
- `scholarly_records.jsonl` — Crossref/OpenAlex results
- `search_results.jsonl` — optional search-engine discoveries
- `errors.jsonl` — fetch/parse errors
- `discovery_report.json` — run statistics

Outputs are intentionally not auto-committed. Review evidence before promoting anything into the canonical corpus.

## Evidence promotion

Discovery is not authorship.

A result can be promoted to `data/corpus.json` only after it satisfies the repository evidence model in `docs/EVIDENCE_MODEL.md`.

Professional credits, styling, translation, press-office work and other verified non-authorship roles belong in `data/credits.json`.

## Copyright and access rules

The harvester:
- stores metadata, not complete article text;
- never attempts paywall or authentication circumvention;
- obeys robots.txt by default;
- uses a configurable delay between requests;
- records blocked/skipped URLs rather than forcing access;
- identifies itself with a descriptive user agent;
- should be used only for public, lawful research and archive maintenance.

The goal is **exhaustive discovery and provenance**, not copying publishers' content.
