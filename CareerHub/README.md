# CareerHub

> **Room boundary:** CareerHub is the **job-search and application room** inside the WPB profile. Weronika's writing, journalism, archive, editorial development and portfolio live separately in the [Writer & Journalism Room](../WriterRoom/README.md).

CareerHub may use explicitly approved, verified career evidence exported from WriterRoom, but it does not own or automatically ingest the writer-room corpus or working material. See [WriterRoom/ROOM_BOUNDARY.md](../WriterRoom/ROOM_BOUNDARY.md).

![CareerHub journey](visuals/careerhub-journey.svg)

## One journey. Three steps.

### 1. Find jobs
CareerHub searches enabled sources, ranks the strongest leads and keeps every discovered job in a historic vault.

### 2. Choose job
When a job looks interesting, answer one question: **Do you want to analyse this job?** If yes, press **YES — Analyse this job**. CareerHub then creates the case, runs HRDM-R, researches the role/employer and prepares the application pack.

### 3. Apply
Edit the Word draft, submit the application and follow the case through **Applied → Contacted → Portfolio/Test → Interview/Meeting 1–5 → Offer / Denied**.

**[Open CareerHub →](CONTROL_ROOM.md)**

## What happens in the background

The user should not need to think about:

**sources → matching → historic vault → HRDM-R → employer research → candidate positioning → DOCX → deadline reminders → application tracking**

Those are implementation layers inside the three-step journey.

## Find jobs

A manual sourcing refresh usually takes about **30–90 seconds** before the new shortlist appears in the Control Room.

CareerHub preserves jobs in two layers:

- [Current control room](CONTROL_ROOM.md) — the strongest current leads.
- [Historic Job Vault](JOB_VAULT.md) — jobs previously or currently sourced, even after they disappear from the latest shortlist.

## Choose and rank

Chosen jobs use a simple 1–5 priority:

- **5 — Must apply**
- **4 — High**
- **3 — Medium**
- **2 — Low**
- **1 — Maybe**

A job found outside CareerHub can be added through **Analyse a job I found elsewhere** without waiting for the sourcing workflow.

## Apply and monitor

[Applications & Follow-up](APPLICATIONS.md) is the process monitor.

A chosen job can move through:

**Chosen → Preparing → Ready to apply → Applied → Contacted → Portfolio/Test → Interview/Meeting 1–5 → Offer / Denied / Withdrawn**

The original GitHub issue acts as the application case file.

## Deadlines and reminders

Deadlines are shown directly beside jobs and application cases.

Chosen jobs can receive automated reminders at **7, 3, 1 and 0 days** before deadline.

- GitHub case reminder: built in.
- Email: optional via private repository secrets.
- SMS: optional via private repository secrets.

See [SETUP.md](SETUP.md#deadline-reminders).

## Evidence boundary

CareerHub's candidate-positioning and application claims must remain evidence-bounded.

WriterRoom can supply selected verified evidence such as publication records, approved biography statements, selected work and documented professional capabilities. CareerHub must not silently upgrade archive interpretation into candidate fact, and it must not automatically use unpublished drafts, confidential reporting material, private notes or unresolved archive leads.

## Visual system

CareerHub uses a deliberately lighter editorial interface inspired by the visual references for this project:

- off-white working surface
- cobalt journey line
- pale-blue information layer
- coral urgency/deadlines
- warm yellow for the Apply stage
- large, restrained typography and generous whitespace

The visual is generated from live CareerHub state, so the numbers change automatically.

## Privacy

This WPB repository is private. Secrets such as API keys and notification credentials remain in repository/environment secret infrastructure and must never be committed to source control.

Candidate evidence, application history and recruitment state belong to CareerHub; writer-room drafts and reporting material remain outside CareerHub unless explicitly exported for a specific career use.

See [PRIVACY.md](PRIVACY.md).

---

<details>
<summary><strong>Technical architecture</strong></summary>

CareerHub contains:
- multi-source job sourcing
- deterministic triage
- persistent job vault
- job priority/ranking
- HRDM-R v6.3
- employer/role research
- evidence-bounded application drafting
- DOCX generation
- application lifecycle tracking
- daily deadline reminder workflow
- optional email/SMS notification channels
- automated SVG dashboard rendering
- validation and regression tests

Maintainer documentation:
- [Workflow](docs/WORKFLOW.md)
- [Source matrix](docs/SOURCE_MATRIX.md)
- [UX review](docs/UX_REVIEW.md)

The reusable central engine is developed separately in `Motherpher/CareerHubZero`; this directory is the WPB-profiled CareerHub surface/state.

</details>
