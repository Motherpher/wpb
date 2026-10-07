# Portfolio catalog contract

`portfolio-catalog.json` is the role-aware public portfolio source consumed by the CareerHub `/writer` surfaces.

It exists because the research corpus and the public portfolio have different responsibilities:

- `data/corpus.json` remains the canonical research archive and evidence record for the reconstructed writing corpus.
- `CareerHub/personalisation/portfolio-catalog.json` is the verified public portfolio projection used by the site. It can contain authored work and other professionally credited work such as translation or styling, but those roles must never be conflated.
- `portfolio.yaml` defines public sections, featured work and exact primary-area membership.

For every public portfolio credit:

1. the record must have a stable ID and evidence sufficient for public attribution;
2. `status` must be `verified`;
3. `primary_area` must match exactly one section slug in `portfolio.yaml`;
4. that ID must occur exactly once across the section `filter.ids` lists;
5. cross-cutting subjects belong in `themes`, not in additional primary-area placements;
6. a non-author contribution must carry an explicit `credit_role` such as `translator` or `styling`; authored records default to `author` for backward compatibility.

CI enforces the one-credit/one-primary-area partition and the declared catalog count.

The public catalog is reconstructed and should not be described as an exhaustive lifetime archive until writer reconciliation and unresolved screen-credit reconciliation are complete.
