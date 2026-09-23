# CareerHub operating workflow

## 0 — Profile

Public evidence is stored in `profile/candidate.yaml`.

Before relying on the system for final applications, reconcile:
- current role/status
- exact languages
- current location
- education chronology
- software/tools
- availability
- salary expectations
- sectors to exclude
- current CV chronology

LinkedIn is treated as a user-controlled source, not a scrape target.

## 1 — Sourcing

The scan workflow runs the configured queries across enabled providers.

Output:
- raw jobs in memory during the workflow
- deduplicated leads
- commit-safe public metadata in `data/latest_jobs.json`
- ranked view in `CONTROL_ROOM.md`

## 2 — Triage

Triage exists only to reduce a large pool.

Inputs:
- job title/text
- search lane
- verified candidate capability vocabulary
- work arrangement
- geography/remote
- recency
- explicit unknown requirements

Output:
- 0–100 operational triage score
- reasons
- review flags

It is **not** an HRDM score.

## 3 — Drill

A selected ad enters the full HRDM-R v6.3 sequence.

The drill workflow accepts:
- public job URL
- lane
- optional pasted job text

If robots/access controls block retrieval, paste the ad text instead.

## 4 — HRDM-R

The run creates:
- Process-ID
- HRDM input packet
- signal extraction
- concept clusters
- hidden need
- field logic
- FunctionCore
- DoD
- assessment zones
- candidate positioning
- HCC
- application strategy

With no AI key, CareerHub creates the packet/prompt and placeholder documents.

With `OPENAI_API_KEY`, the structured HRDM result is generated automatically. The API request uses `store=False`.

## 5 — Company / role research

The automated HRDM runner may use web search for current public employer/role context.

It may **not** web-search the candidate to invent or expand candidate evidence.

## 6 — Write-up

A second structured drafting pass creates:
- cover-letter draft
- CV profile draft
- CV emphasis bullets
- interview notes
- claims check

For bridge-income roles, the system deliberately uses a shorter, more practical application style.

## 7 — Word documents

The workflow generates:
- `Application_<employer>_<role>.docx`
- `HRDM_<employer>_<role>.docx`

These are uploaded as workflow artifacts for further editing and are not committed to the public repository.

## 8 — Human gate

Before sending:
- verify all factual claims
- resolve language/tool/certification unknowns
- adjust voice
- remove unnecessary overqualification signalling for bridge roles
- check deadline/application method
- save the final version outside the public repository
