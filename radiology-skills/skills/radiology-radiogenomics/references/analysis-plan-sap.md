# Scope-aware statistical analysis plan

Use this module for protocols, preregistration, Methods/SAP drafting and pre-analysis review in
`imaging-only`, `mechanism-only` or `imaging-mechanism` studies. The plan follows the estimand and
independent unit; it does not assume that every study contains both imaging and omics.

## 1. Freeze the primary question

Record one row before choosing a test:

| Field | Required content |
|---|---|
| Population/system | disease, tissue/model, setting, eligibility and treatment context |
| Independent unit | patient/donor, lesion, animal, organoid, culture replicate; include nesting |
| Exposure/index | imaging phenotype, condition, molecular state, region, perturbation or assigned treatment |
| Comparator | reference group, baseline/time, sham/control, alternative treatment, or not applicable |
| Outcome | molecular/phenotypic endpoint and measurement window |
| Estimand | contrast, association parameter, prediction target, treatment interaction or intervention effect |
| Claim branch | `descriptive`, `association`, `localization-or-concordance`, `prognostic-prediction`, `average-treatment-effect`, `effect-modification`, `mechanistic` or `causal` |
| Success criterion | effect direction/magnitude, uncertainty, multiplicity rule and validation condition |

The claim branches are not a single ladder. Good prediction does not imply mechanism; localization
does not imply direction; prognostic association in one treatment arm does not establish treatment
benefit; an intervention effect is causal only for the assigned intervention, system and outcome
supported by the design.

## 2. Scope-specific variable contract

- `imaging-only`: specify acquisition, reconstruction, segmentation, feature/model definition,
  scanner/site, patient–lesion–series–ROI–time mapping and endpoint level.
- `mechanism-only`: specify specimen, assay/measurement, condition or perturbation, batch, donor-level
  hierarchy, time, cell/spot/section nesting and functional endpoint. Do not add imaging fields.
- `imaging-mechanism`: specify both contracts plus the exact patient–lesion–region–specimen–time bridge.
  State which molecular values are measured, derived, estimated or predicted.

## 3. Confirmatory versus discovery work

- **Confirmatory:** prespecified exposure/index, outcome, model, covariates, contrast, direction or
  two-sided rule, alpha/multiplicity handling, effect measure, CI and success criterion.
- **Discovery:** high-dimensional feature, gene, pathway, cell-state, niche or interaction scan with a
  declared test family and false-discovery control. Label selected findings exploratory until tested
  with independent or orthogonal evidence.
- Selection, annotation or thresholding performed after inspecting outcomes cannot be retroactively
  described as prespecified.

## 4. Unit hierarchy and model family

Match inference to the independent unit:

- paired/repeated samples: paired contrasts, mixed models, GEE or other repeated-measure models;
- lesions/regions/sections/cells/spots nested within people or donors: aggregate to a defensible unit
  or model clustering explicitly;
- bulk counts: design-matrix-based count models with library/composition handling and donor covariates;
- single-cell: donor-aware pseudobulk or a validated hierarchical approach for confirmatory inference;
- spatial: patient-aware models with region/section dependence and sensitivity to neighborhood scale;
- perturbation: treatment-assignment/guide model including efficiency, multiplicity, dose/time and
  biological replicate; define whether the effect is intention-to-treat-like or target-engagement-based;
- survival: time origin, censoring, competing risks, proportionality/functional-form checks;
- prediction: patient/donor/site/time split appropriate to intended deployment.

Cells, spots, tiles and technical replicates increase measurement resolution, not biological n.

## 5. Confounders, mediators and nuisance structure

Predefine variables from biology and design, not from univariable p-value screening. Candidates may
include age, sex, stage/grade, treatment, disease subtype, purity/composition, site/scanner/protocol,
assay platform/batch, preservation, processing time, library depth and experimental plate.

For every adjustment, state whether it is a confounder, precision covariate, batch/nuisance variable,
mediator or collider risk. Do not adjust for a downstream mediator when estimating a total effect.
If condition is perfectly or nearly confounded with batch/site, correction cannot recover the missing
counterfactual; return `STOP` or narrow the estimand.

## 6. Preprocessing and leakage boundary

Mark each step as fixed before splitting, learned on training data, or applied unchanged to validation.
Feature selection, scaling, harmonisation, imputation, normalization parameters, dimensionality
reduction, batch transforms, label-derived regions, thresholds and hyperparameter selection must not
use held-out outcomes. Unsupervised does not mean leakage-free when the transformation sees validation
distribution or when clustering and testing reuse the same signal without correction.

## 7. Multiplicity

Define the family of claims being protected:

- one primary contrast may use a prespecified alpha;
- feature×gene, gene, pathway, cell-state, region or ligand–receptor families need FDR/FWER control
  appropriate to their hierarchy;
- post-hoc subgroup, time, radius and model choices enlarge the family;
- report the total number tested, correction method, threshold and complete or accessible result table.

Do not use nominal p values from a selected subset as confirmatory evidence.

## 8. Requirements by claim branch

| Claim branch | Minimum analysis contract | What it does not establish |
|---|---|---|
| descriptive | defined denominator, measurement/QC and uncertainty | association, direction or generalization |
| association | valid unit-level model, confounder plan, multiplicity and sensitivity analyses | mechanism or treatment benefit |
| localization-or-concordance | registration/co-localization definition, null, scale/segmentation sensitivity and patient-level replication | signaling, direction or causality |
| prognostic-prediction | intended-use target, leakage-safe development, simple baselines, calibration, CI and external/transport validation | biological mechanism or differential treatment effect |
| average-treatment-effect | valid treatment contrast, time zero, treatment assignment or exchangeability/positivity/consistency assumptions, effect and uncertainty | individual benefit, effect heterogeneity or mechanism |
| effect-modification | valid comparator plus the average-effect contract, prespecified biomarker-by-treatment interaction, absolute effects by biomarker level and validation | mechanism without mediation/perturbation evidence |
| mechanistic | competing hypotheses, scale-compatible observations and evidence that discriminates among them | causal direction if all links remain observational |
| causal | identifiable intervention/contrast, assignment assumptions, controls, target engagement, temporal order and appropriate effect model | transport beyond the tested system, dose and context |

## 9. Prediction-specific requirements

- State intended users, moment of use, available predictors and clinical/experimental action.
- Split at the patient/donor/site/time level that represents deployment; never split shared slices,
  regions, aliquots, cells or spots across folds.
- Fit all data-dependent steps within training folds and use nested tuning where needed.
- Compare with simple and clinically/biologically meaningful baselines.
- Report discrimination/error, calibration, uncertainty and utility where appropriate.
- Evaluate the named unseen domain. Random-cell splits do not establish donor, condition, cell-type,
  perturbation or dataset generalization.

## 10. Treatment and perturbation effects

- Distinguish treatment-contextual prognosis, average treatment effect and effect modification.
  Prognosis under one regimen identifies neither treatment effect. An average-effect estimand needs
  an appropriate treatment contrast and design-specific identification assumptions but not a
  biomarker interaction; it does not by itself establish heterogeneity of benefit. Differential
  benefit/effect modification additionally needs a prespecified
  biomarker-by-treatment interaction and absolute effects by biomarker level; significance in one
  arm and non-significance in another is not an interaction test.
- For randomized perturbations, document assignment, contamination, adherence/efficiency, multiplicity,
  off-targets, dose, duration, target engagement, controls and missing outcomes.
- For non-randomized exposures, state exchangeability, positivity and measurement assumptions; use a
  design and estimand appropriate to the available confounders.
- Rescue or orthogonal perturbation can strengthen target specificity but does not erase poor assignment,
  one-replicate designs or unmeasured toxicity.

## 11. Validation and sensitivity plan

Predefine which result each check can validate:

1. independent participant/system replication with frozen definitions;
2. temporal, geographic, platform or experimental-system transport test;
3. orthogonal assay or spatial/pathology concordance for a named biological link;
4. perturbation/rescue for a directional mechanism in the tested model;
5. internal resampling for uncertainty/optimism only.

Relevant sensitivities include batch/site-only models, alternative normalization/segmentation,
outlier and missing-data analyses, purity/composition adjustment, negative-control genes/features,
label permutation, alternative spatial radius, donor-level leave-one-out, dose/time separation and
exclusion of post-treatment or temporally incompatible samples.

## 12. SAP output

Return:

1. `Primary question and claim branch`
2. `Population, independent unit and hierarchy`
3. `Analysis populations and cohort flow`
4. `Variables, provenance and role of each covariate`
5. `Preprocessing and leakage boundary`
6. `Primary estimand, model, effect measure, CI and success criterion`
7. `Discovery families and multiplicity`
8. `Prediction/treatment/perturbation addendum when applicable`
9. `Validation, sensitivity and negative controls`
10. `Missing-data, software/version and reproducibility plan`
11. `Allowed claim wording if the primary criterion passes`

Use `AUTHOR_INPUT_NEEDED` for missing design facts. Do not invent sample size, power, covariates,
effect sizes, software, thresholds or validation data.
