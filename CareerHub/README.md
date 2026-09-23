# CareerHub — Weronika Pérez Borjas

CareerHub is a job-search control room inside the WPB repository.

Its purpose is to turn the existing verified writer/professional archive into a repeatable workflow:

**Profile → Source → Triage → HRDM-R → Company/role research → Candidate positioning → Application draft → Word document**

The hub supports both career-track work and pragmatic extra-income searches without mixing the two.

## Start here

1. Open [CONTROL_ROOM.md](CONTROL_ROOM.md).
2. Run **CareerHub — Scan & Rank Jobs** from GitHub Actions to refresh leads.
3. Pick a job and run **CareerHub — Drill & Application Pack** with the job URL.
4. Download the generated HRDM/application artifact.
5. Fine-tune the generated DOCX before sending.

## Three search lanes

### A — Core career
Writer, reporter, editor, communications, press/media, research, cultural/NGO and related roles that make direct use of the strongest verified evidence in the archive.

### B — Adjacent capability
Content, communications coordination, project coordination, research support, editorial production, translation/localisation, community/media work and other roles where the evidence transfers strongly even if the title is different.

### C — Bridge / extra income
Part-time, temporary, service, administration, customer support, event/cultural venue work, remote support and similar roles where the objective may simply be reliable additional income.

CareerHub never assumes that a lower-seniority role is a poor choice. It records **search intent** separately from career-level fit.

## HRDM

CareerHub implements the user's HRDM Reverse Mode v6.3 as the full analytical path:

**Ad/Text Intake → Signal Extraction → Key Words & Concepts → Hidden Need Reconstruction → Field Logic Reconstruction → FunctionCore Estimation → DoD Diagnostic → Likely Assessment Zones → Candidate Positioning Map → HCC Reverse Commentary**

The quick scan uses a separate **triage score** only to decide which jobs deserve the full HRDM run. Triage is not HRDM.

See [hrdm/HRDM_R_v6.3.md](hrdm/HRDM_R_v6.3.md).

## Source architecture

Enabled without credentials:
- Arbetsförmedlingen / JobSearch
- Remotive
- Remote OK
- We Work Remotely RSS

Optional with API credentials:
- Adzuna
- Jooble

Manual / URL-drill providers:
- Indeed
- Monster
- Ideella Jobb
- Jobbland
- LinkedIn Jobs
- any public job-ad URL that can be fetched without authentication

CareerHub deliberately does **not** bypass logins, paywalls, robots restrictions or job-board access controls.

See [config/sources.yaml](config/sources.yaml).

## Optional AI automation

The sourcing and deterministic triage work without an AI API.

For full automated HRDM-R analysis, company/role research and application drafting, add an `OPENAI_API_KEY` GitHub Actions secret and optionally `CAREERHUB_MODEL`.

The implementation uses the OpenAI Responses API and structured JSON output. When the key is absent, the drill workflow still produces a complete HRDM input packet for review/use in ChatGPT.

## Privacy

This repository is public-facing. Do not commit:
- phone numbers
- home address
- private email
- full LinkedIn exports
- unpublished CVs
- private references
- API keys
- application letters containing non-public personal information

Use the private/local override mechanism or GitHub Secrets for anything sensitive.

Read [PRIVACY.md](PRIVACY.md).

## Repository structure

```text
CareerHub/
├── README.md
├── CONTROL_ROOM.md
├── PRIVACY.md
├── config/
│   ├── search_profiles.yaml
│   └── sources.yaml
├── profile/
│   ├── candidate.yaml
│   └── LINKEDIN_IMPORT.md
├── hrdm/
│   ├── HRDM_R_v6.3.md
│   └── hrdm_result.schema.json
├── src/careerhub/
│   ├── models.py
│   ├── sources.py
│   ├── matching.py
│   ├── hrdm.py
│   ├── application.py
│   ├── dashboard.py
│   └── cli.py
├── scripts/
│   └── careerhub.py
├── data/
│   ├── latest_jobs.json
│   └── README.md
└── requirements.txt
```

## Design rule

The WPB archive remains the evidence base. CareerHub can consume it, but it must not silently rewrite the archive or invent candidate evidence.

Candidate positioning can only use:
1. verified/public evidence in the CareerHub profile,
2. repository evidence explicitly referenced by the profile,
3. private evidence supplied for that run.
