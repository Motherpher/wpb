# WPB Profile Architecture v1.0

The WPB repository is the private professional profile environment for **Weronika Pérez Borjas**.

Weronika is the profile. CareerHub and WriterRoom are peer operational rooms inside that profile.

```text
WERONIKA PÉREZ BORJAS
│
├── Profile Core
│   ├── identity
│   ├── verified professional facts
│   ├── claim states / provenance
│   ├── permissions
│   └── source-library intake
│
├── Writer & Journalism Room
│   ├── active writing / reporting
│   ├── pitches / commissions
│   ├── research / source handling
│   ├── manuscripts / revisions
│   ├── editorial review
│   ├── publication records
│   ├── archive / bibliography
│   ├── rights / attribution
│   └── portfolio / public presentation
│
└── CareerHub
    ├── job sourcing
    ├── job analysis / HRDM-R
    ├── application preparation
    ├── deadlines / reminders
    └── recruitment outcomes
```

## 1. Root manifest

[`wpb.profile.yaml`](wpb.profile.yaml) declares the profile, room manifests, visibility domains and the explicit WriterRoom → CareerHub bridge.

## 2. Profile Core

[`profile/profile.yaml`](profile/profile.yaml) is the cross-room factual and permission substrate. It is not a CV, biography, portfolio or operational state store.

Allowed claim states are:

- `verified`
- `confirmed_by_weronika`
- `provisional`
- `interpretive`
- `unresolved`
- `rejected`

AI-generated interpretation does not become evidence merely because it is generated or stored.

Profile permissions and AI-use rules live in [`profile/permissions/profile_policy.yaml`](profile/permissions/profile_policy.yaml).

## 3. Writer & Journalism Room

[`WriterRoom/writerroom.yaml`](WriterRoom/writerroom.yaml) is the room manifest.

WriterRoom owns the professional work itself:

- ideas, pitches and commissions;
- research and reporting;
- drafts and revision history;
- editorial development;
- publication state;
- publication archive and bibliography;
- portfolio selection;
- rights and attribution;
- analysis of the body of work.

Canonical work-state logic lives in [`WriterRoom/work/lifecycle.yaml`](WriterRoom/work/lifecycle.yaml).

WriterRoom security uses four handling classes:

`PUBLIC → INTERNAL → CONFIDENTIAL → PROTECTED_SOURCE`

See [`WriterRoom/security/README.md`](WriterRoom/security/README.md).

## 4. Editorial Desk

WriterRoom contains an editorial layer for form/function review, structural coherence, source/referential control, style/register calibration, fact/claim support and deployment readiness.

`The Writer and the Beast` / Publicist may be used as an optional editorial protocol. It remains advisory; Weronika retains authorship and editorial authority.

See [`WriterRoom/editorial/README.md`](WriterRoom/editorial/README.md).

## 5. Publication, archive and portfolio

Publication records and archive evidence are distinct from portfolio curation.

```text
Published work
   ↓
Archive record
   ↓
Portfolio review
   ↓
Optional Career evidence export
```

The archive answers **what work exists**. The portfolio answers **what should represent Weronika now**.

See:

- [`WriterRoom/publication/README.md`](WriterRoom/publication/README.md)
- [`WriterRoom/portfolio/README.md`](WriterRoom/portfolio/README.md)
- [`WriterRoom/rights/README.md`](WriterRoom/rights/README.md)

## 6. CareerHub

CareerHub remains bounded to finding and securing work.

Its user journey remains:

**Find jobs → Analyse? → Apply → Follow**

The reusable engine lives in `Motherpher/CareerHubZero`. The local [`CareerHub/careerhub.yaml`](CareerHub/careerhub.yaml) is the Weronika-specific profile/state manifest.

`CareerHub/profile/candidate_verified.yaml` remains a compatibility adapter until a tested cutover to direct Profile Core consumption is performed.

## 7. WriterRoom ↔ CareerHub bridge

The rooms do not share operational storage.

CareerHub receives WriterRoom material only through the explicit evidence-export contract:

[`bridges/writer-career-evidence/export.yaml`](bridges/writer-career-evidence/export.yaml)

Permitted examples:

- verified publication records;
- selected work;
- confirmed biography statements;
- verified professional capabilities;
- approved portfolio references.

Prohibited automatic transfer includes unpublished drafts, confidential/protected sources, interview notes, private research notes, unresolved records and private editorial material.

CareerHub may reframe exported evidence for a vacancy but may not silently strengthen or change the underlying factual claim.

## 8. Existing archive estate

The historical archive predates WriterRoom and remains at repository root for compatibility:

```text
data/
bibliography/
content/
analysis/
sources/
harvest/
reports/
visuals/
docs/
DASHBOARD.md
```

Those paths are functionally owned by WriterRoom but are **not physically migrated in v1.0**. Migration is deferred until links, scripts, workflows and site dependencies have been audited.

## 9. Visibility domains

### Public
Approved portfolio, biography, selected work and contact material.

### Private professional
Profile Core, CareerHub, ordinary pitches/drafts/work tracking and archive analysis.

### Restricted journalism
Protected-source identities, confidential communications, embargoed documents and equivalent sensitive material.

Restricted journalism must not flow into CareerHub, general AI workflows or public portfolio surfaces.

## 10. Human authority

System precedence is:

```text
Weronika
   ↓
verified primary evidence
   ↓
Profile Core / Writer archive
   ↓
room-specific operational state
   ↓
AI interpretation
```

Weronika may correct, approve, reject, hide, replace, delete, exclude or mark material `NO-AI`.

## 11. Public surfaces

A future public portfolio is generated from approved WriterRoom + Profile Core material.

CareerHub state is not a public-site source.

## 12. Future rooms

Additional rooms may be introduced later if they represent a genuinely separate professional operating domain. They must have their own authority boundary and explicit data bridges rather than being absorbed into CareerHub or WriterRoom by default.

## 13. Implementation state

The non-destructive v1.0 architecture is implemented. Physical archive relocation, a dedicated source-safe vault, WriterRoom AI automation and the final user-facing UI remain later gates.

See [`PROFILE_IMPLEMENTATION_STATUS.md`](PROFILE_IMPLEMENTATION_STATUS.md).
