# WPB Profile Evidence

This directory defines the evidence discipline for cross-room profile claims.

## Evidence states

Every substantive profile claim must use one of:

- `verified`
- `confirmed_by_weronika`
- `provisional`
- `interpretive`
- `unresolved`
- `rejected`

## Rule

A claim may be used outside the Profile Core only when its state and `approved_for` scope permit it.

AI-generated interpretation, archive analysis, conversational memory and search preferences are not evidence by themselves.

## Minimum provenance

Each reusable claim should carry:

- stable claim ID;
- claim text/value;
- state;
- source ID(s);
- last verification or confirmation date where available;
- permitted use scope.

## Archive relationship

WriterRoom may supply verified publication and professional evidence into Profile Core. The original publication/source provenance remains authoritative.

CareerHub may consume approved evidence but may not strengthen or silently rewrite the underlying factual claim.
