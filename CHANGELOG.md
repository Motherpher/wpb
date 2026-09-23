# Changelog

## 2026-09-23 — CareerHub job-hunting control room
- added a separate CareerHub inside the WPB repository
- created a sanitized public-evidence candidate profile with LinkedIn reconciliation path
- implemented three job-search lanes: core career, adjacent capability and bridge/extra-income
- added Platsbanken/JobSearch, Remotive, Remote OK and We Work Remotely sourcing adapters
- staged credentialed Adzuna and Jooble adapters
- added manual/URL-drill workflow for Indeed, Monster, Ideella Jobb, Jobbland and LinkedIn Jobs
- implemented deterministic triage ranking separate from HRDM
- implemented canonical HRDM-R v6.3 packets, structured output schema and optional OpenAI Responses API runner
- added company/role web-research capability for HRDM when an API key is configured
- added evidence-bounded application drafting and editable DOCX generation
- added manual + weekday scan workflow, one-job drill workflow and validation/smoke-test workflow
- added public-repository privacy rules so application drafts and private profile data are not committed


## 2026-09-22 — Single integrated automated dashboard
- replaced multiple public data charts with one canonical `visuals/dashboard.svg`
- moved the integrated dashboard to the very top of the repository README and Weronika's start page
- made each central flow curve represent one verified corpus work
- integrated archive KPIs, editorial phases, metadata coverage, actual publication timeline, research pipeline and portfolio readiness
- added `scripts/build_outputs.py` generation for dashboard JSON, bibliography, dashboard page and SVG
- added automatic derived-output synchronization and drift validation workflows
- retained research/rights decisions as human-reviewed canonical inputs rather than automating evidence promotion


## 2026-09-22 — Corpus enrichment, visuals and harvesting
- expanded canonical corpus from 36 to 38 verified authored/research works
- added the previously missing VICE masculinity article and Forumist `A World Beyond`
- recovered the direct VICE URL for the Miss Crash article
- resolved several Krull publication years from event context while preserving unresolved exact dates
- reclassified Krull `WHAT’S IN STORE?` as a verified styling credit rather than authored journalism
- added `data/article-metadata.json` for publisher metadata, DOI fields, timestamps and creative credits
- added four SVG research infographics plus editable Mermaid sources
- installed a robots-aware public metadata harvester with Wayback, Crossref, OpenAlex and optional search discovery
- added a manual GitHub Actions workflow for harvest runs
- refreshed dashboard and bibliography


## 2026-09-22 — Dashboard metadata layer
- added per-work dashboard metadata across the canonical corpus
- added dashboard metadata to contextual/non-authorship credits
- added usage/status metadata to theme and outlet registries
- added machine-readable `data/dashboard.json`
- added human-readable `DASHBOARD.md`
- documented dashboard schema and status semantics
- surfaced the dashboard in README and repository navigation

## 2026-09-21 — Repository foundation
- initialized the WPB research/archive repository
- created machine-readable corpus, theme and outlet registries
- separated contextual/non-authorship credits from authored work
- added evidence, editorial and rights rules
- added source registry and unresolved research queue
- added writer profile, chronology, themes, method analysis and featured-work selection
- added reusable portfolio biography drafts
- added writer dossier and corpus limitations
- reserved a framework-neutral future site layer
- generated human-readable master bibliography
