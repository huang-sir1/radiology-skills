# Radiomics reporting & quality — CLEAR + METRICS + RQS

Three distinct tools for radiomics. Use the right one for the right job:

- **CLEAR (2023)** — *reporting* completeness. CheckList for EvaluAtion of Radiomics
  research, **58 items**, endorsed by ESR and EuSoMII (Kocak et al.). The radiomics analogue
  of STARD/CLAIM: did you *write down* everything?
- **METRICS (2024)** — *methodological quality*. METhodological RadiomICs Score, **30 weighted
  items across 9 categories**, EuSoMII, Delphi-derived; produces a percentage and a quality
  band (very low → excellent). Plus **METRICS-E3** (explanation & elaboration, 2025).
- **RQS / RQS 2.0** — *quality score*. Original Radiomics Quality Score (Lambin et al. 2017,
  **16 components, max 36 points**). **RQS 2.0** (2025) reframes around "radiomics readiness
  levels" and clinical translation. Widely cited; some items now superseded by METRICS, so
  many groups report **CLEAR + METRICS** as the modern pair and cite RQS for comparability.

> Modern recommendation for a _Radiology_-grade radiomics paper: **CLEAR** (report) +
> **METRICS** (quality) + **IBSI** (feature reproducibility). Add RQS if reviewers/field
> expect it.

## CLEAR — the 58-item flow (clusters)
- **Title/Abstract** — radiomics identified; design and key result.
- **Introduction** — rationale, objectives, hypothesis.
- **Methods — study design** — prospective/retrospective; eligibility; ethics.
- **Methods — imaging data & acquisition** — modality, scanner, protocol; multi-centre/vendor
  reporting; phantom/QA if used.
- **Methods — segmentation** — manual/auto/semi; software; number of segmenters;
  **inter-/intra-observer reproducibility (ICC)**; handling of non-reproducible features.
- **Methods — preprocessing** — resampling/interpolation, intensity normalisation/
  discretisation (bin width vs. bin count — state which), ROI processing — **IBSI-aligned**.
- **Methods — feature extraction** — software + **version**, feature classes, **IBSI
  compliance**, settings.
- **Methods — harmonisation** — scanner/protocol effects; **ComBat** or equivalent; whether
  fit on training only.
- **Methods — feature selection & modelling** — selection method, model, tuning,
  **validation scheme**, class imbalance handling.
- **Methods — statistics** — performance metrics, calibration, comparison tests, multiplicity.
- **Results** — flow, performance with CIs, validation performance, feature stability.
- **Open science** — data, code, **radiomic feature values**, model availability.

## METRICS — 9 categories (weighted)
Covers: study design; imaging data & protocol; segmentation & reproducibility; preprocessing
& feature extraction (IBSI); feature processing & selection; modelling & validation;
performance evaluation (discrimination, calibration, clinical utility); reproducibility/open
science; and overall transparency. Items are weighted; total is reported as a **percentage**
with a quality band. Use METRICS to *strengthen Methods*, not just to score.

## RQS — 16 components (max 36)
Notable point-bearing items: image protocol quality; **test–retest / phantom** repeatability;
**multiple segmentations**; feature reduction / overfitting control; **multivariable analysis
with non-radiomic features**; **biological correlates** (radiogenomics earns points here);
cut-off analyses; discrimination + **calibration**; **prospective** design; **validation**
(none → internal → external; external + multi-centre scores highest); comparison to gold
standard; potential clinical utility (decision-curve); cost-effectiveness; **open
science/data**.

## Highest-yield radiomics failures
1. **Feature non-reproducibility** — no segmentation ICC; bin-width/normalisation unstated;
   not IBSI-compliant → features not reproducible → Blocker.
2. **Harmonisation leakage** — ComBat fit on the full dataset (incl. test).
3. **Selection bias** — feature selection done outside cross-validation (on all data).
4. **No external validation** — single-centre, single-scanner only.
5. **n ≪ features** without dimensionality control → overfitting.
6. **No calibration / clinical-utility** for a clinical model.
7. **Feature values / code not shared** — blocks reproduction.

## Output
`Tool | Item/Category | Status or score | Location | Fix`. Report CLEAR as
PRESENT/PARTIAL/MISSING per item; METRICS as category scores + total %; RQS as
points/36 if requested.
