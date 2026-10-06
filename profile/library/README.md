# WPB Source Library

The source library is the intake layer for material supplied by Weronika or added for professional verification.

## Intended material

Examples include CVs, LinkedIn exports, certificates, publication lists, biography drafts, PDFs, scans, images, portfolio documents and other professional records.

## Intake rule

Uploading a document does **not** change Profile Core automatically.

The intended flow is:

**Upload → Source Library → Extract candidate claims → Review → Approve/Reject → Profile Core**

## Source states

- `active`
- `inactive`
- `replaced`
- `review_required`
- `restricted`

## Safety

Credentials and secrets never belong here.

Protected journalistic source material does not belong in the general profile library. It must follow WriterRoom restricted-source handling.
