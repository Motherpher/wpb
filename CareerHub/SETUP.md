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

## Let Weronika use the one-click Analyze flow

Automatic issue-based analysis is restricted to the repository owner, members and collaborators.

**One-time action:** add Weronika as a collaborator to whichever repository hosts CareerHub.

She can then use **Analyze** without seeing or handling API credentials.

For the public WPB repository, remind her that the issue itself is public. In a private CareerHub repository, the same interaction becomes the recommended production workflow.

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
