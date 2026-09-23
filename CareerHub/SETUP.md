# CareerHub — one-time maintainer setup

> Weronika should not normally need this page. Her normal interface is [CONTROL_ROOM.md](CONTROL_ROOM.md).

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

Because the repository is public and the workflow can use private API credentials, automatic issue-based analysis is restricted to the repository owner, members and collaborators.

**One-time action:** add Weronika as a repository collaborator.

After that she can use the **Analyze** links without accessing any secret.

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
