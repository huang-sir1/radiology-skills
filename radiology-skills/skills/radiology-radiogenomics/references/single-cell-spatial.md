# Single-cell and spatial reference linkage

Use this compact module when a single-cell or spatial atlas is an external reference rather than the
active assay being designed or audited. It supports standalone mechanism studies and imaging–mechanism
studies. An atlas can provide annotation, signatures or contextual comparison; it is not patient-
matched evidence unless the biological units and specimens truly match.

## 1. Evidence-role contract

Record separately:

- active measured layer, such as bulk RNA, pathology or imaging;
- external atlas source, population, tissue, condition, assay and annotation provenance;
- transferred object: marker signature, label, cell fraction, state score, mapping or prior;
- primary evidence state of the transferred result, usually `estimated` or `predicted`;
- modality subtype, such as `deconvolution/BayesPrism`, `label-transfer/scVI`,
  `spatial-mapping/anchor-based` or another explicit assay/operation label;
- claim-link status (`direct`, `inferred` or `proposed`) relative to the atomic claim;
- uncertainty, rejection/unassigned behavior and sensitivity to the reference.

Use an explicit three-column record in outputs:

| Primary evidence state | Modality subtype | Claim-link status |
|---|---|---|
| [measured / derived / estimated / associated / predicted / perturbed] | [assay plus transfer/deconvolution/mapping operation] | [direct / inferred / proposed] |

Do not describe reference transfer, deconvolution, label mapping or imputation as direct measurement in
the target cohort.

## 2. Bulk-to-cell deconvolution

Reference-based methods such as CIBERSORTx, BayesPrism, MuSiC, Bisque, SCDC, EPIC or quanTIseq can
estimate cell fractions or expression components from bulk data.

Audit:

- reference tissue, disease, treatment, platform and cell-state compatibility;
- donor representation, annotation method and marker/signature construction;
- missing or collinear cell types, malignant-state diversity and cross-platform transformation;
- identifiability, uncertainty and sensitivity to alternative references/signatures;
- target-cohort inference at the patient/donor level rather than treating genes or inferred cells as n;
- orthogonal validation for load-bearing cell fractions or states.

For `mechanism-only`, relate estimates to the actual condition, phenotype or molecular program. For
`imaging-mechanism`, only then associate the estimated fraction/state with a region- and time-compatible
imaging phenotype.

## 3. Label or state transfer to active single-cell/spatial data

- Preserve target data as the measured layer and transferred labels/scores as estimated or predicted.
- Report reference/target preprocessing, feature overlap, mapping method, confidence/rejection rule and
  the fraction left unassigned.
- Inspect novel target states instead of forcing every cell/spot into a reference class.
- Validate important labels with target-data markers, morphology/protein/spatial context and donor-
  level consistency.

Transferred labels cannot establish lineage, communication, regulation or perturbation response.

## 4. External spatial context

An external spatial atlas can test whether a nominated cell state or program is anatomically plausible
in a comparable tissue. Check platform resolution, segmentation, disease/site, treatment, region and
sampling compatibility. Treat cross-cohort localization as contextual concordance, not co-localization
within the target specimen.

In a standalone mechanism study, stop at the specimen–section–region chain. In an
`imaging-mechanism` study, radiology registration is a separate bridge:

`patient -> lesion -> scan/ROI or habitat -> gross pathology -> block -> section -> spatial cell/spot`

Quantify or bound the mm-to-micron mapping and sampling uncertainty. A single section does not
represent the whole lesion.

## 5. Minimal comparisons and failure tests

- compare at least two compatible references or a reference-free/coarse-label baseline when feasible;
- repeat conclusions under alternative marker sets, label granularity and uncertain-cell rejection;
- hold out donors/datasets when claiming transfer generalization;
- use negative-control cell types/programs and permutation/reference nulls where appropriate;
- check whether batch, tissue composition or broad stress/proliferation explains the transferred signal.

Return `STOP` for an incompatible tissue/context presented as target truth, unrecoverable sample identity,
reference leakage into evaluation, or a direct-measurement/mechanism claim based only on transferred
labels. Rescue with a coarser label, bounded contextual claim or target-cohort orthogonal assay.

## 6. Writing contract

Methods must name the atlas/accession, population, tissue, condition, assay, annotation, mapping or
deconvolution method, parameters, rejection rule and uncertainty assessment. Results must call the
output estimated/predicted and report robustness. Discussion must separate target-cohort observation
from external-reference plausibility and name the validation still required.

Sentence skeleton:

“Using [atlas] as an external [tissue/condition] reference, [method] estimated [cell state/fraction]
in [target data]. The association/localization was robust to [reference/sensitivity] but remains an
inferred target-cohort link pending [orthogonal or matched spatial validation].”
