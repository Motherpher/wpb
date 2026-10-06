# WPB Profile Core

This directory is the shared factual and permission layer for the Weronika Pérez Borjas profile.

It is **not** a CV, portfolio, biography or CareerHub state store.

## Authority

The profile core stores only claims that can be assigned an explicit state and provenance. Room-specific operational data remains in the room that owns it.

Allowed claim states:

- `verified`
- `confirmed_by_weronika`
- `provisional`
- `interpretive`
- `unresolved`
- `rejected`

Absent evidence remains unknown.

## Files

- [`profile.yaml`](profile.yaml) — canonical cross-room profile facts and verification queue.
- [`permissions/profile_policy.yaml`](permissions/profile_policy.yaml) — visibility, AI-use and room-access policy.
- `library/` — intake rules for documents supplied by Weronika.
- `evidence/` — evidence/provenance documentation.

## Room relationship

WriterRoom and CareerHub may read only profile material that is approved for their purpose. They do not gain ownership of the Profile Core.

CareerHub's existing `CareerHub/profile/candidate_verified.yaml` remains a compatibility adapter until CareerHubZero/profile integration is explicitly cut over. New cross-room truth belongs here rather than being invented inside CareerHub.

## Human authority

Weronika can correct, approve, reject, hide, replace, delete or restrict profile material. Repository analysis and AI-generated interpretation never outrank her corrections or primary evidence.
