# CareerHub Control Room

> **Status:** installed · ready for first scan  
> **Candidate profile:** public-evidence draft; LinkedIn reconciliation pending  
> **Workflow:** Source → Triage → HRDM-R → Research → Draft → DOCX

## Quick actions

### 1. Refresh job leads
[Open **CareerHub — Scan & Rank Jobs**](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-scan.yml) and choose **Run workflow**.

Use a search lane:
- `core`
- `adjacent`
- `bridge`
- `all`

The workflow updates this control room and `data/latest_jobs.json`.

### 2. Drill one job
[Open **CareerHub — Drill & Application Pack**](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-drill.yml) and choose **Run workflow**.

Paste a job-ad URL. The workflow:
1. ingests the ad,
2. creates a full HRDM-R packet,
3. optionally performs web/company research when an AI API key is configured,
4. creates candidate positioning and application strategy,
5. produces editable Word documents,
6. uploads the pack as a workflow artifact.

### 3. Broaden the profile
Review [profile/candidate.yaml](profile/candidate.yaml) and [profile/LINKEDIN_IMPORT.md](profile/LINKEDIN_IMPORT.md).

### 4. Enable full automation
Read [SETUP.md](SETUP.md) for optional AI/API credentials and operating setup.

## Search lanes

| Lane | Objective | Examples |
|---|---|---|
| Core | Direct use of strongest professional evidence | writer, journalist, editor, communications, press, research, NGO/culture |
| Adjacent | Transferable capability | content, coordinator, research support, editorial production, community/media |
| Bridge | Extra income / lower barrier / flexible | admin, customer support, reception, event/venue, service, temporary, remote support |

## Job board

No scan has been run yet.

After the first scan this section is regenerated automatically with the strongest current leads, source, location, work arrangement, lane, triage score, reasons and application deadline where available.

## Drill queue

No jobs drilled yet.

Application drafts are intentionally **not committed** to the public repository. They are generated as downloadable artifacts.

## Source health

| Source | Mode | Current setup |
|---|---|---|
| Platsbanken / JobSearch | Public API | Ready |
| Remotive | Public API | Ready |
| Remote OK | Public JSON | Ready |
| We Work Remotely | Public RSS | Ready |
| Adzuna | API key | Optional |
| Jooble | Regional API key | Optional |
| Indeed | Partner/manual | URL drill / browser search |
| Monster | Manual | URL drill / browser search |
| Ideella Jobb | Manual | URL drill / browser search |
| Jobbland | Manual | URL drill / browser search |
| LinkedIn Jobs | Manual | URL drill / browser search |

## Human review gates

CareerHub can automate research and drafting, but these remain deliberate decisions:

- Is the role actually worth applying to?
- Is a gap acceptable or material?
- Is the current candidate profile complete?
- Are all application claims evidenced?
- Should a bridge-income role use a simplified application rather than full career positioning?
- Is the final letter in Weronika's own voice?

The generated document is a **draft for further fine-tuning**, never an auto-send.
