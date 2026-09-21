# Terminology and claim ledgers

Use two persistent ledgers from first contact through final revision. They prevent terminology drift and keep
every headline tied to its actual evidence rather than to the desired story.

## Terminology ledger

Record recurring features, models, cohorts, modalities, assays, cell states, pathways, endpoints, metrics,
units, abbreviations, and anatomical regions.

| Canonical term | First-use definition | Variants or collisions found | Decision/source |
|---|---|---|---|
| one stable name | expansion and operational definition | spellings, synonyms, same name for different objects | retained form and rationale |

- Use one name for one object; scientific consistency outranks lexical variety.
- Define abbreviations once and keep units, signs, reference categories, thresholds, and feature directions fixed.
- Never rename an author's method or biological state merely to improve style.
- Ask only when the collision is scientifically consequential; otherwise adopt the traceable source form and note it.
- If a canonical term changes, update every dependent artifact and the ledger, not only the current paragraph.

## Claim-evidence ledger

Create one row per headline claim, not one row per analysis output:

`claim_id | canonical claim | population | inferential unit | spatial/time/treatment scope | imaging object |
biological object | evidence state | source location | independence | alternatives | verdict | maximum wording |
missing link | upgrade test`

Use the reusable [claim-evidence-mechanism ledger](../../templates/claim-evidence-mechanism-ledger.md)
when the task needs a persistent artifact rather than an inline summary.

Use controlled evidence states:

- `measured` — directly observed by a declared assay at a traceable unit.
- `derived` — calculated from measured inputs, such as a radiomic feature or embedding.
- `estimated` — annotation, deconvolution, activity, trajectory, mapping, imputation, or generated layer.
- `associated` — a relationship estimated with design, uncertainty, confounding, and multiplicity considered.
- `predicted` — a locked rule evaluated on unseen units; name calibration, comparator, and target context.
- `perturbed` — an intervention with assignment, target-engagement, controls, and outcome measurement.

Also label provenance as `user-provided`, `inspected`, `working assumption`, `mentor-generated option`, or
`missing`. A confident user assertion is not the same as an inspected artifact.

### Three-column evidence crosswalk

Do not flatten modality detail into the primary state. Record three separate columns:

1. **Primary evidence state** — one of `measured`, `derived`, `estimated`, `associated`, `predicted`, `perturbed`.
2. **Modality-specific subtype** — for example radiomic feature/embedding; segmented/assigned/deconvolved/
   mapped/imputed/interpolated spatial layer; pseudobulk/trajectory/communication score; pathologist annotation,
   IHC signal, digital-pathology segmentation, or neighbourhood estimate.
3. **Claim-link status** — `direct`, `inferred`, or `proposed`, describing how that evidence supports the claim.

Crosswalk rules:

- segmentation, assignment, deconvolution, trajectory, activity, communication, mapping, imputation and
  interpolation are normally `estimated` with the specific operation retained as subtype;
- a radiomic feature or deterministic quantity calculated from declared measurements is `derived`;
- the legacy label “experimental support” maps to `perturbed` only when an intervention, target engagement, controls and
  response were actually measured; otherwise retain the underlying measured/associated state and an inferred link;
- a proposed future assay is `missing` evidence with a proposed acquisition plan, not a seventh positive state;
- domain playbooks may require finer subtype labels, but those labels never replace the primary state or inflate
  the claim-link status.

## Claim discipline

- The weakest necessary link sets the claim ceiling. Fine-scale biological wording cannot outrun coarse mapping.
- Two correlated or estimated layers may share training data, references, tissue composition, or batch and are
  not automatically independent corroboration.
- `Associated with` requires a valid unit, effect/uncertainty, confounding assessment, and multiplicity handling.
- `Predicts outcome under regimen X` requires unseen-unit validation but does not mean treatment benefit.
- `Average treatment effect` requires a valid treatment contrast and design-specific identification assumptions;
  it does not by itself establish heterogeneity of benefit.
- `Modifies treatment benefit` requires a comparator, biomarker-by-treatment interaction, and validation.
- `Mechanism`, `drives`, `mediates`, or `causes` requires scale-compatible evidence that changes the proposed
  factor and phenotype and excludes serious alternatives, preferably with orthogonal confirmation or rescue.

Keep claim IDs and canonical wording stable across text, figures, tables, responses, and mentoring plans. Every
revision must state which rows changed and whether any dependent claim ceiling moved.
