# Writer Room ↔ CareerHub Boundary

## Principle

The WPB repository is a **profile container with multiple rooms**. CareerHub is one room. The Writer & Journalism Room is another.

They may exchange selected evidence, but they do not share operational state.

## Ownership

### Writer & Journalism Room owns

- writing/reporting work;
- publication corpus and bibliography;
- source provenance;
- research notes and writer-facing analysis;
- portfolio selection;
- writer/editorial development;
- rights and publication context.

### CareerHub owns

- job sourcing;
- vacancy analysis;
- HRDM-R outputs;
- candidate-positioning for a specific vacancy;
- application drafts;
- application/recruitment status;
- deadlines, reminders and outcomes.

## Permitted bridge

CareerHub may receive only deliberately exported career evidence such as:

- verified publication records;
- selected work;
- confirmed biography statements;
- verified professional capabilities;
- approved portfolio links or descriptions.

The bridge is **evidence export**, not shared storage.

## Prohibited automatic transfer

CareerHub must not automatically ingest:

- unpublished drafts;
- source identities or confidential reporting material;
- interview notes;
- private research notes;
- incomplete/unverified archive leads;
- editorial comments not intended as career evidence;
- personal material unrelated to a specific career-use case.

WriterRoom must not write into CareerHub's job/application state.

## Direction of authority

For published-work facts, the Writer & Journalism Room/archive evidence layer is authoritative.

For job-search state, CareerHub is authoritative.

If CareerHub uses evidence exported from WriterRoom, the original provenance remains attached. CareerHub may reframe evidence for an application but may not silently strengthen or alter the underlying factual claim.

## Future implementation

A machine-readable bridge may later expose a small approved evidence bundle, for example:

```yaml
writer_evidence_export:
  version: "1.0"
  approved_sources:
    - publication_record
    - selected_work
    - confirmed_bio
    - verified_capability
  excludes:
    - drafts
    - confidential_sources
    - private_notes
    - unresolved_records
```

Until such a contract is implemented, the boundary is manual and explicit.
