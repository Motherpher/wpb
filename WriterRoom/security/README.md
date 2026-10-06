# WriterRoom Security & Source Protection

WriterRoom uses four handling classes:

## PUBLIC
Material already public or explicitly approved for public portfolio/archive use.

## INTERNAL
Private professional material such as ordinary drafts, planning notes and internal editorial work.

## CONFIDENTIAL
Material with heightened sensitivity: unpublished commissioned work, embargoed information, private interview material or restricted documents.

## PROTECTED_SOURCE
Source identities, protected communications, confidential source documents and equivalent high-risk journalism material.

## Hard rules

- `PROTECTED_SOURCE` material must not enter general AI workflows.
- `PROTECTED_SOURCE` material must not be exported to CareerHub.
- Restricted material must not be exposed through public portfolio generation.
- Credentials and secrets are never stored in WriterRoom content files.
- GitHub is not assumed to be an adequate long-term vault for protected source material merely because the repository is private.
- Until a dedicated encrypted/source-safe storage layer is established, protected material should be referenced by metadata only where necessary, not stored here.

## AI handling

`NO-AI` is a valid human restriction marker. Human restrictions override automation and model convenience.
