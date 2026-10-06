# Portfolio catalog contract

`portfolio-catalog.json` is the public Writer portfolio source consumed by the CareerHub `/writer` surfaces.

It exists because the research corpus and the public portfolio have different responsibilities:

- `data/corpus.json` remains the canonical research archive and evidence record.
- `CareerHub/personalisation/portfolio-catalog.json` is the verified public authored-work projection used by the portfolio site.
- `portfolio.yaml` defines public sections, featured work and exact primary-area membership.

For every public work:

1. the record must have a stable ID and direct evidence sufficient for public attribution;
2. `status` must be `verified`;
3. `primary_area` must match exactly one section slug in `portfolio.yaml`;
4. that ID must occur exactly once across the section `filter.ids` lists;
5. cross-cutting subjects belong in `themes`, not in additional primary-area placements.

CI enforces the one-work/one-primary-area partition and the declared catalog count.

The public catalog is reconstructed and should not be described as an exhaustive lifetime archive until writer reconciliation is complete.
