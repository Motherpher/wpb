# CareerHub privacy

## Recommended operating mode: private repository

CareerHub is personal job-search infrastructure. The cleanest production setup is a **private CareerHub repository**.

Why:

- job targets and application history remain private
- application issues can safely act as case files
- workflow runs and downloadable artifacts are private to repository collaborators
- a fuller CV/profile can be stored without publishing it
- notes about salary, availability, interviews and applications do not become public
- the UX can stay simple instead of repeatedly warning the user about public visibility

The current WPB repository is public. CareerHub therefore operates here in **public-safe mode**.

## What is public in the current repository

If CareerHub remains inside this public repo, assume these are visible:

- the job board
- job links and shortlist
- CareerHub issue requests
- issue comments
- workflow-run metadata
- public-safe profile information
- search preferences and source configuration

Do not use public issues for private notes.

## Safe to commit here

- public job-ad metadata and links
- public professional evidence already verified in the WPB archive
- sanitized capability/profile data
- generic search preferences
- triage metadata
- HRDM schemas, prompts and workflow code

## Do not commit here

- private email addresses
- phone numbers
- home/street address
- birth date or identification numbers
- full/private CV
- full LinkedIn export
- private references
- salary history or private salary requirements
- interview correspondence
- application drafts containing non-public personal information
- passwords, tokens or API keys

## Generated applications

Application packs are generated into an ignored output directory and uploaded as temporary workflow artifacts rather than committed to `main`.

In a **private** CareerHub repository, the same workflow can safely become the normal application case-management system.

In this **public** repository, download the pack promptly and keep final/private versions elsewhere.

## Private local overrides

The code supports:

`CareerHub/private/profile.local.yaml`

The `private/` directory is gitignored.

## GitHub Actions secrets

Credential-based automation uses GitHub Secrets, for example:

- `OPENAI_API_KEY`
- `CAREERHUB_MODEL`
- `ADZUNA_APP_ID`
- `ADZUNA_APP_KEY`
- `JOOBLE_API_KEY`
- `JOOBLE_API_ENDPOINT`

Never write those values into tracked files.

## Recommended architecture

**Public WPB repository**
- archive and portfolio research
- public-safe candidate evidence
- CareerHub code and search architecture
- optional public-safe job discovery board

**Private CareerHub repository**
- real candidate profile/CV
- private job requests
- HRDM case files
- applications
- interview notes
- application status/history
- private API-backed automation

This is the recommended production configuration if Weronika is going to use CareerHub regularly.
