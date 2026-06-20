# CLAIM 2024 Update — auditing a medical-imaging AI paper

**CLAIM** = Checklist for Artificial Intelligence in Medical Imaging. The **2024 Update**
(Mongan, Kahn, Moy et al.; *Radiology: Artificial Intelligence*, 2024) is the de-facto
standard for any imaging-AI study and is what _Radiology_ / Radiology: AI reviewers use.
It is organised around the IMRaD manuscript flow. Audit **every** item; below are the
clusters and the questions that catch the most problems.

> Always reconcile against the published checklist for exact item wording and numbering.
> This file is an auditing aid, not a substitute for the source checklist.

## Title / Abstract
- States that AI/ML is used, the task, and the imaging modality.
- Structured abstract reports study design, data, model, and key performance with
  uncertainty (CI).

## Introduction
- Scientific/clinical background and the specific gap.
- Study objectives and hypotheses stated a priori.

## Methods — study design
- Prospective vs. retrospective; registration if applicable.
- Ethical approval / IRB and consent (or waiver).
- Intended use / clinical role of the AI (triage, replacement, assist).

## Methods — data
- **Data sources** and eligibility (inclusion/exclusion) at patient level.
- **Acquisition**: modality, scanner vendor/model, key protocol parameters, field strength,
  contrast, reconstruction.
- **De-identification** method.
- **Data splits**: how train / validation / test were defined and the **unit** of splitting
  (patient, not slice/lesion). State that the test set was untouched during development.
- **Sample size** rationale; flowchart of patient selection.
- **Missing data** handling.

## Methods — ground truth / reference standard
- How labels were established; reference standard and its rationale.
- Number, qualifications, and blinding of annotators; adjudication of disagreement;
  inter-/intra-rater reproducibility.

## Methods — model
- Model type/architecture; software + version; key hyperparameters.
- **Pre-processing** (resampling, normalisation, registration) — fit on training only.
- Feature selection / engineering (for radiomics, cross-ref CLEAR + IBSI).
- Training procedure, loss, optimiser, augmentation, stopping rule.
- Hardware; reproducibility (seed, code availability).

## Methods — evaluation
- **Metrics** appropriate to the task and prevalence (classification: AUC + sensitivity/
  specificity at a *pre-specified* threshold, PPV/NPV with prevalence; segmentation: DSC,
  HD95/surface metrics; detection: FROC/sensitivity per lesion at given FP rate).
- **Uncertainty**: confidence intervals; method for CIs.
- Statistical comparison method (e.g. DeLong for AUCs) — see radiology-stats.
- **Calibration** and **clinical utility** (decision-curve) for prediction models.
- Robustness / subgroup / failure-mode analysis.

## Results
- Patient flow and characteristics (per split).
- Model performance with CIs on the **internal test** and, ideally, **external** data.
- Comparison to readers / standard of care where claimed.
- Errors and failure cases discussed.

## Discussion
- Practical/clinical significance bounded by the evidence.
- Limitations (generalisability, spectrum, prevalence, label noise).
- Intended clinical integration and next validation steps.

## Open science
- **Code, model, and data availability** statements — specific routes, not "on request"
  alone (cross-ref radiology-data).

## CLAIM audit output (per item)
`Item | Requirement | PRESENT/PARTIAL/MISSING/NA | Location | Fix`

## Highest-yield CLAIM failures (check first)
1. Split unit is slice/lesion, not patient → **leakage** → Blocker.
2. No external/independent validation, or "validation" set used for tuning.
3. Operating threshold chosen on the test set (should be pre-specified or chosen on
   validation).
4. Metrics ignore prevalence (1:1 sampling reported as if clinical).
5. Reference standard quality / reader blinding not described.
6. No CIs; no calibration for a prediction model.
7. Vague availability statements.
