# CareerHub privacy and public-repository rules

The WPB repository is designed as a public research/archive repository. CareerHub therefore runs in **public-safe mode** by default.

## Safe to commit

- public job-ad metadata and links
- public professional evidence already verified in the WPB archive
- sanitized capability/profile data
- search queries and preferences
- triage scores and non-sensitive job notes
- HRDM schemas, prompts and workflow code

## Do not commit

- private email addresses
- phone numbers
- street/home address
- birth date or identification numbers
- unpublished CVs
- full LinkedIn exports
- private references
- salary history not already public
- private correspondence
- application drafts containing private personal data
- API keys or tokens

## Private local overrides

The code supports a local file:

`CareerHub/private/profile.local.yaml`

The `private/` directory is gitignored.

## GitHub Actions secrets

Credential-based providers use GitHub Secrets, for example:

- `OPENAI_API_KEY`
- `CAREERHUB_MODEL` (optional)
- `ADZUNA_APP_ID`
- `ADZUNA_APP_KEY`
- `JOOBLE_API_KEY`
- `JOOBLE_API_ENDPOINT`

Never write these values into YAML files in the repository.

## Generated applications

Application packs and DOCX files are generated into an ignored/output directory and uploaded as temporary workflow artifacts. They are not committed to `main`.

For applications that include private contact details or highly personal evidence, a private repository/fork is the safer operating environment.
