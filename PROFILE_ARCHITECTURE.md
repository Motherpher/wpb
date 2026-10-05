# WPB Profile Architecture

The WPB repository is not CareerHub itself. It is a **profile container** for Weronika Pérez Borjas with distinct operational rooms.

```text
WPB PROFILE
│
├── WriterRoom/
│   ├── writing & journalism work
│   ├── archive / bibliography
│   ├── research & source evidence
│   ├── editorial development
│   └── portfolio / public presentation
│
└── CareerHub/
    ├── job sourcing
    ├── job analysis / HRDM-R
    ├── application preparation
    ├── deadlines / reminders
    └── recruitment outcomes
```

## Separation rule

The two rooms are peers under the WPB profile.

CareerHub may consume explicitly approved evidence exported from WriterRoom, but CareerHub does not own the writer corpus, drafts, reporting material or portfolio state.

WriterRoom does not own vacancy, application or recruitment state.

## Existing repository estate

The historical archive folders currently remain at repository root for compatibility with existing automation and links. They belong functionally to WriterRoom:

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

They can be physically migrated under `WriterRoom/` later only after link, workflow and script dependencies are audited.

## Central CareerHub relationship

The reusable CareerHub engine lives in:

`Motherpher/CareerHubZero`

The `CareerHub/` directory in this profile is Weronika-specific context/state and user-facing operation. It must remain bounded to career use.

## Future rooms

Additional rooms may be added to the WPB profile later without being absorbed into CareerHub, provided each room has a defined authority boundary and explicit data bridge where needed.
