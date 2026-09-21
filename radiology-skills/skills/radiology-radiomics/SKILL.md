---
name: radiology-radiomics
description: "Design/audit radiomics preprocessing, IBSI extraction, stability, leakage-safe selection and validation."
---

# Hand-crafted Radiomics Study Design

Use this skill to build (or audit) a **hand-crafted radiomics** study that is reproducible and
leakage-free, from preprocessing through validation. Radiomics papers are desk-rejected for the
same recurring reasons: non-standardised features, segmentation not characterised, and data
leakage in selection/normalisation. This skill encodes the IBSI/CLEAR pipeline and the
partition hygiene reviewers enforce.

## Core stance

- **IBSI defines; evidence verifies.** Use **IBSI** to define and report image processing and
  feature calculations (resampling, discretisation, filters, aggregation, software+version).
  Conformance improves semantic and implementation comparability, but does not by itself establish
  empirical repeatability across segmentations, scans, software builds, scanners or protocols.
  Pair it with implementation checks and task-matched phantom/test-retest/sensitivity evidence.
- **Discretisation is a decision, not a default.** Fixed **bin width** vs fixed **bin count**
  changes every texture feature; state which, the value, and why; keep it consistent.
- **Segmentation error propagates.** Use reproducible masks and **filter unstable features**
  (ICC) before modelling (→ radiology-annotation).
- **Selection lives inside training only.** Feature selection, normalisation, imputation, and
  harmonisation are fit on **training folds**, never on the whole cohort — the classic leak.
- **Match effective complexity to information.** Thousands of features versus few independent
  patients/events is unstable, but no universal EPV threshold grants adequacy. Let
  `radiology-stats` define a project-specific information/precision brief from the estimand,
  event/non-event support, effective degrees of freedom, shrinkage, calibration and resampling
  stability.
- **Report calibration + utility, not just AUC**, for a clinical signature (→ radiology-stats).
- **Integrity.** Never invent feature counts, ICCs, or performance; mark what must be computed.

## When to use

- "Design / review my radiomics pipeline (PyRadiomics, IBSI)." / "影像组学流程设计或审查。"
- "Bin width or bin count? what resampling/normalisation/filters?"
- "How do I select features without leakage?" / "LASSO/mRMR feature selection 怎么做才不泄漏？"
- "Build a radiomics signature/score and validate it."
- "Audit this radiomics Methods for leakage and IBSI compliance."

## When to open extra files

| File | Open when |
|---|---|
| [references/preprocessing-ibsi.md](references/preprocessing-ibsi.md) | Resampling, intensity normalisation, gray-level discretisation/bin width, filters, IBSI reporting |
| [references/feature-extraction.md](references/feature-extraction.md) | Feature families, PyRadiomics settings, aggregation, software/version, parameter file, delta/longitudinal radiomics, test–retest/phantom repeatability |
| [references/selection-modelling.md](references/selection-modelling.md) | Leakage-safe selection (variance/ICC/correlation/LASSO/mRMR), modelling, signature/score, EPV |
| [references/leakage-audit.md](references/leakage-audit.md) | The radiomics-specific leakage checklist reviewers weaponise |
| [references/reproducibility-artifacts.md](references/reproducibility-artifacts.md) | Producing a final analysis package, feature dictionary, run/split manifest, signature equation, or auditable feature-count trail |

## Workflow

1. **Confirm the design** (reuse `radiology-design`) — endpoint, independent unit/hierarchy,
   cohorts, validation type and project-specific information/precision constraints.
2. **Segmentation & stability** — masks and reproducibility from `radiology-annotation`, which owns
   the ICC stability metric and threshold provenance; this skill freezes and applies that filter
   inside training.
3. **Preprocessing** (preprocessing-ibsi.md) — resample, normalise, discretise (state bin
   width/count), filters; record everything for IBSI.
4. **Extraction** (feature-extraction.md) — feature families, PyRadiomics (or equivalent) +
   version, parameter file; produce a documented, versioned feature matrix.
5. **Selection & modelling** (selection-modelling.md) — selection **inside** CV/training only;
   model complexity matched to the statistical brief; build the signature/score; pre-specify the
   primary analysis.
6. **Validate** — internal (nested CV/bootstrap) + external/temporal/geographic; report
   discrimination, calibration, DCA (→ radiology-stats).
7. **Freeze reproducibility artifacts** (`reproducibility-artifacts.md`) — split/run manifest,
   parameter file, feature dictionary/count trail, fitted pipeline, coefficients/signature equation,
   environment, and deviations.
8. **Audit leakage** (leakage-audit.md) and **write Methods** to CLEAR/IBSI.

## Output contract

1. **`Pipeline spec`** — preprocessing → extraction → selection → model → validation, each step
   with its parameters and the leakage control marked.
2. **`Parameters`** — resampling, normalisation, discretisation (bin width/count), filters,
   feature families, software+version (a PyRadiomics parameter file where applicable).
3. **`Selection/modelling plan`** — method, where it sits relative to the split, effective
   complexity and the project-specific information/precision check.
4. **`Validation plan`** — internal + external; metrics incl. calibration/DCA.
5. **`Leakage audit`** — pass/fail per item with the fix.
6. **`Reproducibility bundle`** — run/split manifest, parameter file, feature dictionary and
   count trail, fitted preprocessing/selection/model objects, coefficient/signature mapping,
   environment, and deviations actually available.
7. **`Table handoff`** — feature-stage counts, selected-feature dictionary, coefficients/weights,
   and model-performance value keys for `radiology-table`.
8. **`Methods paragraph`** — CLEAR/IBSI-aligned prose (+ 待确认 for Chinese authors).

## Quality bar

A good radiomics spec lets another lab identify and execute the same feature definition and then
test whether the implementation and measurements agree within declared tolerances. It quantifies
segmentation/acquisition sensitivity, keeps selection inside the split, and reports performance
with calibration and CIs, never AUC alone.

## Handoffs

- Series/phase/sequence qualification, acquisition/reconstruction, quantitative transforms,
  artifacts, dose, phantom/test-retest and protocol drift → `radiology-acquisition-qc`; consume its
  frozen measurement passport before radiomics preprocessing.
- Mask SOP & feature-stability → `radiology-annotation`.
- IBSI/CLEAR/METRICS/RQS audit → `radiology-reporting`.
- Selection/CV statistics, calibration, DCA, multiplicity, sample size → `radiology-stats`.
- Parameter provenance, bin-width/spacing/interpolation/segmentation sensitivity, fair method
  comparison, ablation and claim-level robustness → `radiology-method-evaluation`; this skill still
  owns radiomics configuration and execution.
- Deep features / deep-learning comparison → `radiology-deep-learning`.
- Biological interpretation of the signature → `radiology-radiogenomics`.
- Figures (feature heatmap, ROC, calibration, nomogram) → `radiology-figure`.
- Tables (feature audit, coefficient/signature, performance, subgroup/sensitivity) →
  `radiology-table`.
- Reframing this pipeline as a funding proposal → `radiology-grant`.
- Full-project state, simulation labels, and cross-artifact consistency → `radiology-pipeline`.
