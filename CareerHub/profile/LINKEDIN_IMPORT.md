# LinkedIn profile import

LinkedIn profile supplied for Weronika:

https://www.linkedin.com/in/weronika-p%C3%A9rez-borjas-0aa68274/

Automated retrieval is intentionally **not** implemented. LinkedIn blocks normal automated access and CareerHub should not attempt to bypass that restriction.

## Recommended import paths

### Option A — profile PDF
From LinkedIn, save/export the profile as PDF and review it locally. Extract only the professional details Weronika wants CareerHub to use.

### Option B — copy/paste profile text
Create locally:

`CareerHub/private/linkedin.txt`

Paste the relevant About, Experience, Education, Skills and Languages sections there.

### Option C — sanitized manual update
Edit `profile/candidate.yaml` with verified non-sensitive details.

## Reconciliation rule

LinkedIn does not automatically override the WPB archive.

When the two disagree:
1. preserve both records,
2. identify the conflict,
3. prefer current writer-confirmed information for current job hunting,
4. preserve archival publication evidence for historical claims.

## Important

Do not commit a full LinkedIn export if it contains personal contact information, private employment details or data not intended for a public repository.
