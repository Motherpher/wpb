# CareerHub — one-time maintainer setup

> Weronika should not normally need this page. Her normal interface is [CONTROL_ROOM.md](CONTROL_ROOM.md).

## Recommended production architecture

For regular use, run CareerHub in a **private repository** and keep this public WPB repository as the archival/public-safe layer.

A private CareerHub makes job targets, application case files, workflow history and generated documents private while preserving exactly the same one-click user flow.

The current public implementation is functional, but it should be treated as **public-safe mode**.

See [PRIVACY.md](PRIVACY.md).

## Minimum setup

No external job API keys are required for the basic job board.

Immediately available:
- Platsbanken / Arbetsförmedlingen JobSearch
- Remotive
- Remote OK
- We Work Remotely
- automated shortlist
- HRDM input packet
- editable DOCX generation
- public job URL / pasted-text drill

## Let Weronika use the three-step flow

Automatic issue-based case creation and status updates are restricted to the repository owner, members and collaborators.

**One-time action:** add Weronika as a collaborator to whichever repository hosts CareerHub.

Her normal route is then:

**Find jobs → Choose job → Apply**

She does not need access to API credentials or the implementation files.

In the public WPB repository, chosen-job issues are public. In a private CareerHub repository, the same workflow is suitable for real application case management.

## Enable full AI-assisted HRDM + drafting

Add this repository secret:

`OPENAI_API_KEY`

Optional:

`CAREERHUB_MODEL`

If no model override is supplied, the current code uses its configured default.

Repository path:

**Settings → Secrets and variables → Actions → New repository secret**

Never put API credentials in tracked files.

## Optional extra job sources

### Adzuna
Secrets:
- `ADZUNA_APP_ID`
- `ADZUNA_APP_KEY`

Then enable Adzuna in `config/sources.yaml`.

### Jooble
Secrets:
- `JOOBLE_API_KEY`
- `JOOBLE_API_ENDPOINT`

Then enable Jooble in `config/sources.yaml`.

## Candidate-profile completion

The profile needs one private reconciliation pass with Weronika's current CV/LinkedIn export.

Use:
- [profile/PROFILE_REVIEW.md](profile/PROFILE_REVIEW.md)
- [profile/LINKEDIN_IMPORT.md](profile/LINKEDIN_IMPORT.md)

Do not put private contact details into public GitHub issues.

## Maintainer workflows

- [Job refresh](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-scan.yml)
- [Direct drill](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-drill.yml)

The normal user flow should instead use [CONTROL_ROOM.md](CONTROL_ROOM.md).


## Deadline reminders

CareerHub checks chosen, non-closed jobs daily and can remind at:

- 7 days before deadline
- 3 days before deadline
- 1 day before deadline
- deadline day

### GitHub reminders

No extra setup is required. The workflow comments directly on the CareerHub case issue.

### Email reminders

Add these repository secrets:

- `RESEND_API_KEY`
- `CAREERHUB_NOTIFY_EMAIL`
- `CAREERHUB_NOTIFY_EMAIL_FROM`

The email address stays in GitHub Secrets and is not committed.

### SMS reminders

Add:

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_FROM_NUMBER`
- `CAREERHUB_NOTIFY_PHONE`

The phone number stays in GitHub Secrets and is not committed.

### Reminder workflow

[CareerHub — Deadline Reminders](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-deadline-reminders.yml)

It runs daily and can also be triggered manually.

## Application tracking

A chosen job is stored in `CareerHub/data/applications.json`.

The human-readable monitor is:

[APPLICATIONS.md](APPLICATIONS.md)

Status changes are made with the simple **CareerHub — Update an application** form or the quick status links in the Control Room.

## Historic Job Vault

Every scan merges new results into `CareerHub/data/job_vault.json`; jobs are not deleted when they disappear from the latest shortlist.

Human-readable view:

[JOB_VAULT.md](JOB_VAULT.md)
