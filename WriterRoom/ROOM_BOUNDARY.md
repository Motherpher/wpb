# Writer Room ↔ CareerHub Boundary

## Principle

The WPB repository is a **profile container with multiple peer rooms**. CareerHub is one room. The Writer & Journalism Room is another.

They may exchange selected evidence, but they do not share operational state.

## Ownership

### Writer & Journalism Room owns

- writing/reporting work;
- pitches and commissions;
- publication corpus and bibliography;
- source provenance;
- research notes and writer-facing analysis;
- editorial state;
- publication state;
- portfolio selection;
- rights and publication context.

### CareerHub owns

- job sourcing;
- vacancy analysis;
- HRDM-R outputs;
- candidate positioning for a specific vacancy;
- application drafts;
- application/recruitment status;
- deadlines, reminders and outcomes.

### Profile Core owns

- cross-room verified professional facts;
- claim state/provenance;
- profile-level permissions and use scope.

## Implemented bridge

The machine-readable bridge is:

[`../bridges/writer-career-evidence/export.yaml`](../bridges/writer-career-evidence/export.yaml)

CareerHub may receive only deliberately approved career evidence such as:

- verified publication records;
- selected work;
- confirmed biography statements;
- verified professional capabilities;
- approved portfolio links or descriptions.

The bridge is **evidence export**, not shared storage.

## Prohibited automatic transfer

CareerHub must not automatically ingest:

- unpublished drafts;
- source identities or confidential/protected reporting material;
- interview notes;
- private research notes;
- incomplete/unverified archive leads;
- editorial comments not intended as career evidence;
- personal material unrelated to a specific career-use case.

WriterRoom must not write into CareerHub's job/application state.

## Direction of authority

For published-work facts, WriterRoom/archive evidence is authoritative.

For cross-room verified profile facts, Profile Core is authoritative.

For job-search state, CareerHub is authoritative.

If CareerHub uses evidence exported from WriterRoom, original provenance and evidence status remain attached. CareerHub may reframe evidence for an application but may not silently strengthen or alter the factual claim.

## Security

`PROTECTED_SOURCE` material is categorically outside the CareerHub bridge and general AI workflows.

## Automation rule

The bridge defaults to deny. Automatic shared storage and automatic export are disabled. Human approval is required for any item crossing from WriterRoom to CareerHub.
