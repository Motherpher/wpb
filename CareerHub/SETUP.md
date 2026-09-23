# CareerHub setup

CareerHub works at two levels.

## Level 1 — no private API keys

Immediately available:
- Platsbanken / Arbetsförmedlingen JobSearch
- Remotive
- Remote OK
- We Work Remotely
- deterministic triage ranking
- control-room generation
- full HRDM input packet
- DOCX generation with a structured fallback draft
- manual URL/text drill for any selected job

No setup is required beyond running the workflows.

## Level 2 — full HRDM + research + application drafting

To automate the full HRDM-R interpretation, current employer/role research and evidence-bounded application drafting, add a repository secret:

`OPENAI_API_KEY`

Optional model override:

`CAREERHUB_MODEL`

If no model value is provided, CareerHub currently defaults to `gpt-5.4`.

The AI calls use the Responses API with `store=False`.

## Optional additional job APIs

### Adzuna

Add:
- `ADZUNA_APP_ID`
- `ADZUNA_APP_KEY`

Then set `adzuna.enabled: true` in `config/sources.yaml`.

### Jooble

Add:
- `JOOBLE_API_KEY`
- `JOOBLE_API_ENDPOINT`

Then set `jooble.enabled: true`.

Jooble keys are region/domain-specific. Do not use a US endpoint for Swedish sourcing.

## Where to add GitHub Secrets

Repository → **Settings → Secrets and variables → Actions → New repository secret**

Do not place credentials in tracked YAML files.

## LinkedIn profile completion

The current CareerHub candidate profile is built from verified WPB archive evidence and the LinkedIn profile URL supplied for Weronika.

For current-role, language, software/tool and detailed chronology data, use:

[profile/LINKEDIN_IMPORT.md](profile/LINKEDIN_IMPORT.md)

The preferred method is to reconcile a writer-provided LinkedIn export/CV with the public archive rather than scrape LinkedIn.

## Running a scan

Open:

https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-scan.yml

Choose:
- `all` for the complete control room
- `core` for strongest professional fit
- `adjacent` for transferable roles
- `bridge` for extra-income/flexible roles

The workflow is also scheduled on weekdays.

## Drilling a role

Open:

https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-drill.yml

Provide:
- job URL
- lane
- optional pasted job text

Pasted text is useful when a job board blocks automated retrieval.

## Output

A drill run creates:
- HRDM input packet
- HRDM prompt
- HRDM structured result
- application package JSON
- editable application DOCX
- editable HRDM brief DOCX

These are uploaded as workflow artifacts rather than committed to the public repository.

## Final review

CareerHub never auto-submits an application.

Before sending:
1. verify factual claims,
2. confirm language/tool/certification requirements,
3. tune voice,
4. decide how much seniority to signal,
5. check deadline/application instructions,
6. edit the Word document.
