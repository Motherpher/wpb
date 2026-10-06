# WPB Profile Implementation Status

**Architecture:** WPB Profile v1.0  
**State:** implemented as a non-destructive profile/room architecture  
**Physical archive migration:** deferred

## Implemented

- root profile manifest: `wpb.profile.yaml`
- shared Profile Core: `profile/profile.yaml`
- profile evidence rules and source-library intake
- profile permission / AI-use / visibility policy
- WriterRoom manifest
- WriterRoom lifecycle model
- editorial desk specification
- publication desk specification
- portfolio layer specification
- rights/attribution rules
- journalism security/source-protection policy
- work, pitch and source templates
- explicit WriterRoom → CareerHub evidence-export contract
- CareerHub remains a peer room with its existing `careerhub.yaml`

## Deliberately not migrated

The historical writer/archive estate remains at repository root:

- `data/`
- `bibliography/`
- `content/`
- `analysis/`
- `sources/`
- `harvest/`
- `reports/`
- `visuals/`
- `docs/`
- `DASHBOARD.md`

This is intentional. Existing automation, links and public/archive logic continue to work while those paths are functionally owned by WriterRoom.

## Compatibility

`CareerHub/profile/candidate_verified.yaml` remains the CareerHub compatibility adapter. Cross-room truth is now defined in `profile/profile.yaml`; CareerHub migration to direct Profile Core consumption should occur only when CareerHubZero/profile integration is explicitly cut over and tested.

## Security boundary

Protected-source material is not to be stored in ordinary WriterRoom files by default and is excluded from general AI workflows and CareerHub export. A dedicated encrypted/source-safe storage layer remains a future infrastructure decision.

## Next implementation gates

1. validate current workflows after architecture insertion;
2. add user-facing UI only after the active CareerHub/site processes stabilise;
3. create WriterRoom active-work state only when real work items are entered;
4. introduce a dedicated `WPB-Writer` API project before live WriterRoom AI automation;
5. decide source-safe storage before any protected journalism material is onboarded;
6. consider physical archive migration only after full dependency/path audit.
