# TRIPOD+AI (2024) + PROBAST / PROBAST+AI (2025)

Use when an individual-level **prediction model** (diagnostic or prognostic) is developed
and/or validated — including ML/DL. **TRIPOD+AI** = reporting; **PROBAST+AI** = risk of
bias. They are complementary: good TRIPOD+AI reporting still permits high PROBAST risk of
bias, and vice versa.

## TRIPOD+AI (2024) — what changed vs TRIPOD 2015
- One harmonised guidance for **regression OR machine learning** models (27-item checklist).
- New emphasis on **fairness** (performance across subgroups/protected attributes),
  **open science** (data/code/model/protocol availability), patient/public involvement,
  and ML-specific reporting.
- **TRIPOD+AI for Abstracts** — Table 3 of the same statement, not a standalone checklist;
  audit the abstract too.

## TRIPOD+AI item clusters (audit all)
- **Title/Abstract** — model purpose (diagnosis/prognosis), development vs validation,
  outcome, predictors, data source, performance with uncertainty.
- **Introduction** — rationale, objectives, intended use and users.
- **Methods — source of data** — study design, setting, dates, eligibility.
- **Methods — participants & outcome** — outcome definition, blinded assessment, time
  horizon (prognostic).
- **Methods — predictors** — definition, timing, blinding to outcome; for imaging/radiomics,
  acquisition + extraction (cross-ref CLEAR/IBSI).
- **Methods — sample size** — rationale; events-per-variable / Riley minimum sample size.
- **Methods — missing data** — handling (imputation method, not silent case deletion).
- **Methods — analysis** — model type, predictor handling, selection procedure,
  hyperparameter tuning, internal validation (CV/bootstrap), performance measures
  (discrimination **and** calibration), and how the final model is specified.
- **Methods — fairness** — planned subgroup/fairness evaluation.
- **Results** — participants/flow, model specification (so others can use it),
  performance (discrimination, calibration, clinical utility), validation results.
- **Discussion** — limitations, generalisability, intended use.
- **Open science** — funding, conflicts, protocol, data/code/model availability.

## PROBAST (risk of bias) — four domains × signalling questions
1. **Participants** — appropriate sources and inclusions? (selection bias)
2. **Predictors** — defined/assessed without knowledge of outcome; available at intended
   moment of use?
3. **Outcome** — defined/determined appropriately, without knowledge of predictors?
4. **Analysis** — enough events; continuous predictors handled sensibly; no inappropriate
   dichotomisation; missing data handled; **overfitting/optimism** addressed (internal
   validation, shrinkage); relevant performance (calibration!) reported; model not selected
   solely by univariable significance.

**PROBAST+AI** (Moons et al., *BMJ* 2025;388:e082505) is the current version, superseding
PROBAST 2019. The "+AI" deliberately parallels TRIPOD+AI — one tool for regression **and**
AI/ML, no false dichotomy. What changed:
- Two parts: model **development** (quality assessment; 16 signalling questions) and model
  **evaluation** (risk of bias; 18 signalling questions).
- Evaluation distinguishes **apparent performance / internal validation / external
  validation** — judge each on its own terms.
- **Fairness and algorithmic bias** are embedded across all four domains (not a bolt-on),
  alongside AI-era concerns: data leakage, tuning leakage, computational reproducibility.

## Highest-yield prediction-model failures
1. **Calibration not reported** — discrimination (AUC) only. Reviewers will ask. (radiology-stats)
2. **Optimism** — performance reported on the same data used to build/tune the model.
3. **EPV too low** / no sample-size justification → overfitting.
4. Continuous predictors dichotomised, losing information.
5. Model not fully specified → not usable/reproducible by others.
6. No fairness/subgroup analysis (now expected under TRIPOD+AI).

## Output
`Item/Domain | Requirement or signalling question | Status / RoB judgement | Location | Fix | Owner | Closure evidence`
For PROBAST, give a per-domain judgement (Low / High / Unclear) and an overall RoB.
