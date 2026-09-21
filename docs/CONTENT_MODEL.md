# Content model

The repository is deliberately framework-neutral.

## Canonical work record
Each entry in `data/corpus.json` can include:

- `id` — stable internal identifier
- `date` — ISO date, year, or null
- `title`
- `outlet`
- `language`
- `type`
- `evidence` — A/B/C
- `status`
- `url`
- `themes[]`
- `phase`
- `featured`
- `note`

## Site derivation
A future site should generate article cards and archive pages from the JSON data rather than manually duplicating bibliography in frontend code.

## Proposed routes
- `/` — profile + selected work
- `/work` — featured work
- `/archive` — all works, filterable
- `/themes/[theme]`
- `/about`
- `/research`
- `/archive-note`

## Asset model
When authorised portfolio imagery is added later, store references in a future `data/assets.json` rather than hard-wiring file paths in article records.
