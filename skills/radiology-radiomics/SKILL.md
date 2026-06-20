---
name: radiology-radiomics
description: "Design and audit a hand-crafted radiomics study end-to-end to Radiology (RSNA) / CLEAR / IBSI standard — image preprocessing (resampling, intensity normalisation, gray-level discretisation/bin width, filters), IBSI-compliant feature extraction (PyRadiomics or equivalent), reproducibility/stability filtering, leakage-safe feature selection, modelling, and internal/external validation. Use when the user plans or reviews a radiomics pipeline, mentions PyRadiomics, IBSI, feature extraction, bin width, gray-level discretisation, LASSO feature selection, radiomics signature/score, or \"影像组学/放射组学\". Produces a reproducible pipeline spec, runnable parameter settings, a leakage audit, and Methods text. Never fabricates feature counts or performance."
---

# Hand-crafted Radiomics Study Design

Use this skill to build (or audit) a **hand-crafted radiomics** study that is reproducible and
leakage-free, from preprocessing through validation. Radiomics papers are desk-rejected for the
same recurring reasons: non-standardised features, segmentation not characterised, and data
leakage in selection/normalisation. This skill encodes the IBSI/CLEAR pipeline and the
partition hygiene reviewers enforce.

## Core stance

- **IBSI or it isn't reproducible.** Report image processing and feature definitions to **IBSI**
  standard (resampling, discretisation, filters, aggregation, software+version) — otherwise
  "feature X predicts Y" is irreproducible. (→ radiology-reporting/IBSI.)
- **Discretisation is a decision, not a default.** Fixed **bin width** vs fixed **bin count**
  changes every texture feature; state which, the value, and why; keep it consistent.
- **Segmentation error propagates.** Use reproducible masks and **filter unstable features**
  (ICC) before modelling (→ radiology-annotation).
- **Selection lives inside training only.** Feature selection, normalisation, imputation, and
  harmonisation are fit on **training folds**, never on the whole cohort — the classic leak.
- **Match complexity to events.** Thousands of features vs tens of patients overfits; respect
  EPV and validate honestly (→ radiology-stats).
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
| [references/feature-extraction.md](references/feature-extraction.md) | Feature families, PyRadiomics settings, aggregation, software/version, parameter file |
| [references/selection-modelling.md](references/selection-modelling.md) | Leakage-safe selection (variance/ICC/correlation/LASSO/mRMR), modelling, signature/score, EPV |
| [references/leakage-audit.md](references/leakage-audit.md) | The radiomics-specific leakage checklist reviewers weaponise |

## Workflow

1. **Confirm the design** (reuse `radiology-design`) — endpoint, unit (patient-level), cohorts,
   validation type, EPV.
2. **Segmentation & stability** — masks and reproducibility from `radiology-annotation`; set the
   ICC stability filter (applied in training).
3. **Preprocessing** (preprocessing-ibsi.md) — resample, normalise, discretise (state bin
   width/count), filters; record everything for IBSI.
4. **Extraction** (feature-extraction.md) — feature families, PyRadiomics (or equivalent) +
   version, parameter file; produce a documented, versioned feature matrix.
5. **Selection & modelling** (selection-modelling.md) — selection **inside** CV/training only;
   model choice matched to EPV; build the signature/score; pre-specify the primary analysis.
6. **Validate** — internal (nested CV/bootstrap) + external/temporal/geographic; report
   discrimination, calibration, DCA (→ radiology-stats).
7. **Audit leakage** (leakage-audit.md) and **write Methods** to CLEAR/IBSI.

## Output contract

1. **`Pipeline spec`** — preprocessing → extraction → selection → model → validation, each step
   with its parameters and the leakage control marked.
2. **`Parameters`** — resampling, normalisation, discretisation (bin width/count), filters,
   feature families, software+version (a PyRadiomics parameter file where applicable).
3. **`Selection/modelling plan`** — method, where it sits relative to the split, EPV check.
4. **`Validation plan`** — internal + external; metrics incl. calibration/DCA.
5. **`Leakage audit`** — pass/fail per item with the fix.
6. **`Methods paragraph`** — CLEAR/IBSI-aligned prose (+ 待确认 for Chinese authors).

## Quality bar

A good radiomics spec is one another lab could re-run from the parameters alone and get the same
features — with segmentation error quantified, selection inside the split, and performance
reported with calibration and CIs, never AUC alone.

## Handoffs

- Mask SOP & feature-stability → `radiology-annotation`.
- IBSI/CLEAR/METRICS/RQS audit → `radiology-reporting`.
- Selection/CV statistics, calibration, DCA, multiplicity, sample size → `radiology-stats`.
- Deep features / deep-learning comparison → `radiology-deep-learning`.
- Biological interpretation of the signature → `radiology-radiogenomics`.
- Figures (feature heatmap, ROC, calibration, nomogram) → `radiology-figure`.
