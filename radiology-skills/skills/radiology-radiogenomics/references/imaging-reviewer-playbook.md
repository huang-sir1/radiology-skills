# Imaging-only reviewer and revision playbook

Use this for manuscript review, rebuttal and frozen-yardstick revision verification when the study is
imaging-only. Review radiography, CT, MRI, PET, ultrasound, radiomics, deep imaging or imaging-derived
endpoints on their own terms. Do not demand omics, tissue sampling or a molecular mechanism merely
because those modalities could be interesting future work.

## Reviewer domains

| Domain | Questions that must be resolved | Minimum repair when weak |
|---|---|---|
| Clinical question | Population, index test/input, comparator, outcome and intended use explicit? | Rewrite objective and estimand |
| Cohort | Flow, exclusions, missingness, timing and eligibility reproducible? | Patient flow and cohort table |
| Acquisition | Scanner, site, protocol, reconstruction and preprocessing reported? | Protocol table and site sensitivity |
| Annotation | Segmentation/labels blinded, reproducible and clinically defensible? | Reader protocol and reproducibility |
| Feature/model pipeline | All data-dependent steps fitted inside training folds? | Rebuild nested patient-level pipeline |
| Validation | Internal resampling distinguished from independent external validation? | Downgrade claim or test frozen model externally |
| Statistics | Estimand, multiplicity, uncertainty, calibration and missingness handled? | Prespecified analysis and full estimates |
| Comparators | Clinical and simple imaging baselines included? | Add baseline comparison |
| Generalisability | Site, scanner, disease spectrum and temporal drift examined? | Stratified/sensitivity analyses |
| Reproducibility | Parameters, versions, model artifact, features and code available as allowed? | Complete technical supplement |

## Claim boundaries

- Association does not establish diagnostic performance, prognostic value, treatment benefit or
  clinical utility.
- Cross-validation is not external validation, and slice-level or region-level splitting is not
  patient-level validation.
- An imaging correlate can be described as a phenotype marker; do not call it a molecular mechanism,
  non-invasive biopsy or causal driver without corresponding evidence.
- A single retrospective cohort cannot establish deployment readiness. Calibration, transportability,
  workflow impact and prospective evaluation remain separate claims.

## Reviewer output

Use the atomic contract in `constructive-manuscript-review-chain.md`:
`Finding ID | class | review dimension/lens | P0/P1/P2 | obligation | typed evidence anchor |
observed problem | governing criterion | why it matters | claim consequence | minimum feasible remedy |
optional stronger route | cost/trade-off | closure evidence | confidence/scope limit`. Lead with design
validity and leakage before novelty or polish. Preserve valid
parts, name the smallest repair, and separate mandatory correction from optional future work.

## Revision verification

Freeze the original finding IDs and yardstick. For each point, verify the response letter, revised
manuscript, figure/table/supplement and analysis output against one another. Use VERIFIED, PARTIAL,
NOT ADDRESSED, MADE WORSE or NOT VERIFIABLE. Do not accept “analysis added” without method, result and location.
Do not create a new molecular-data requirement during verification unless the authors introduced a
new molecular claim.

## Rebuttal wording

When a requested assay is absent and not necessary for the imaging claim, respond with a scientific
boundary: explain the declared scope, add the limitation or future hypothesis, and avoid pretending
that imaging predicts unmeasured biology. When a valid technical concern is raised, state the exact
analysis or text changed, result obtained, location and residual limitation.
