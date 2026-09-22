# WPB visual system

## Canonical dashboard

![WPB Archive Dashboard](dashboard.svg)

The repository now uses **one integrated data visual**: `visuals/dashboard.svg`.

It combines corpus scale, editorial phases, metadata coverage, publication chronology, the research-to-publication pipeline and portfolio readiness in a single editorial dashboard. Separate public charts have been retired to avoid competing versions of the same data.

## Design direction

The dashboard uses an editorial information-design language: generous off-white space, serif-led typography, restrained mustard/rose/teal accents, thin rules, and a flowing line structure where **one curve represents one verified work**.

The visual is intentionally research-facing rather than a final portfolio identity. A later site can adapt the same visual grammar without changing the underlying data model.

## Automation

Do **not** hand-edit `dashboard.svg` for data changes.

Its canonical generator is:

`scripts/build_outputs.py`

The automatic synchronization workflow is:

`.github/workflows/sync-derived.yml`

Canonical inputs are the repository JSON data. Git history preserves earlier separate visual experiments.
