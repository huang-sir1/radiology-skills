# Missingness and Validation

Treat modality availability as part of the sampling mechanism and clinical workflow.
The first analysis object is a patient-by-modality matrix, not an imputed feature table.

## Define block-wise missingness

For each patient and each of the five dimensions, distinguish:

- **observed and usable** — passed block-specific QC and can enter the analysis;
- **not acquired** — the test or specimen was never obtained;
- **acquired but failed** — technical, quality, registration, or linkage failure;
- **structurally unavailable** — the modality is impossible or inappropriate by design;
- **temporally mismatched** — acquired outside the pre-specified clinical window;
- **excluded after QC** — present in source data but unusable under locked criteria.

Also separate a **missing block** from missing entries within an observed block. Their
causes, handling, and inferential meaning are different. Report counts by availability
pattern, endpoint, site, time, disease severity, and key demographics.

## Bias from complete cases

Complete-case analysis is unbiased only under restrictive assumptions. In multi-omics,
completion often depends on referral, biopsy or surgery, tissue adequacy, center
resources, disease stage, and outcome-related workflow. Therefore:

1. compare included complete cases with excluded or partially observed patients;
2. model or tabulate block availability against site, endpoint, and baseline variables;
3. state the target population changed by requiring all blocks;
4. repeat key analyses in broader availability patterns when the estimand permits;
5. do not describe the largest single-block cohort as the fusion sample.

If site almost determines assay availability or outcome, the data may not identify a
transportable modality effect. Restrict the claim or redesign the study.

## Handling options and boundaries

| Strategy | Defensible use | Boundary or risk |
|---|---|---|
| **Complete-case analysis** | A transparent primary or sensitivity analysis when the intersection is adequate and selection is assessed | Discards information and may induce selection bias; cannot be the silent default |
| **Within-block imputation** | Sporadic missing values in an otherwise observed block, using parameters fitted on training data | Does not justify fabricating an entirely absent assay; uncertainty and missingness mechanism still matter |
| **Multiple imputation** | Supported clinical or low-dimensional variables with a defensible imputation model | High-dimensional omics and whole-block absence usually exceed credible imputation; imputation must occur within resampling |
| **Pattern-specific models** | Common, clinically meaningful modality combinations | Small patterns yield unstable models; evaluation must match each intended use pattern |
| **Late fusion over available blocks** | Stable block-specific predictors and an explicitly defined aggregation rule | Fusion weights and calibration must be trained for the same patterns; unavailable blocks may be informative |
| **Missingness indicators** | Workflow availability is observable at deployment and its use is clinically acceptable | Indicators can encode site, access, or severity shortcuts and fail after transport |
| **Modality dropout** | Training a deep model to tolerate realistic absent-block patterns | It is augmentation, not imputation or proof of robustness; dropout frequencies must reflect plausible deployment and be evaluated by pattern |
| **Cross-modal generation** | A separately validated research task with clear uncertainty | Synthetic omics are predictions, not measured biology, and must not be used as ground truth or mechanistic confirmation |

Never use outcome information, external-test distributions, or full-cohort neighbors to
impute or reconstruct predictor inputs in a prediction or deployment pipeline.

### Prediction versus inferential multiple imputation

- **Prediction/deployment:** fit imputation using development predictors only, within
  resampling, then freeze it for validation and deployment. Do not use the outcome to
  impute model inputs, and do not recompute imputations from the external cohort's joint
  distribution.
- **Inferential multiple imputation:** outcome-assisted imputation can be valid when the
  goal is estimating an association or effect rather than producing deployable predictor
  inputs. State the estimand and the missingness assumption (for example, missing at
  random conditional on variables in the imputation model), use a congenial imputation
  model, fit the analysis in each imputed dataset, and pool estimates and standard errors
  with Rubin's rules. Propagate imputation uncertainty and add sensitivity analysis for
  plausible missing-not-at-random departures.

Neither branch justifies reconstructing an entire high-dimensional assay without
empirical support. Keep prediction validation and inferential MI workflows separate.

## Nested preprocessing and selection

Use an untouched outer evaluation layer and an inner model-development layer.

Inside each outer-training set, and repeated inside inner resampling as applicable:

1. perform block-specific QC and filtering;
2. estimate scaling, normalization, harmonization, and batch adjustment;
3. impute supported within-block values;
4. learn embeddings, similarity networks, latent factors, or graphs;
5. select features, components, and blocks; select interactions only in the supervised
   branch;
6. tune shared hyperparameters and fusion weights, plus predictive thresholds and
   calibration only in the supervised branch;
7. refit the locked pipeline on outer-training data and transform the outer test once.

Keep patients, lesions, repeated scans, families, sites, and assay batches grouped as
required. Global ComBat, normalization, feature screening, factor learning, or feature
selection before splitting is leakage even when outcome labels were not explicitly used.

### Donor and patient grouping

Cells, spots, regions, slides, and tiles from the same donor or patient are correlated
subunits, not independent samples. Use donor/patient-level splitting and report the
independent donor/patient n. Prefer pseudobulk or prespecified patient-level summaries
when they answer the question; otherwise use hierarchical or mixed-effects models that
represent the nesting. Fit subunit filtering, embeddings, feature selection, and
aggregation rules using training donors only. Random cell-, spot-, slide-, or tile-level
folds leak donor identity and inflate precision.

### Harmonization for unseen data

For predictive validation and deployment, freeze harmonization parameters, reference
distributions, feature definitions, and software settings from development data. The
transform must accept an unseen patient and, where claimed, an unseen site without
refitting on validation patients. If a method requires the full target cohort to
re-estimate batch or site distributions, label it **transductive harmonization** and
report it separately; it is not evidence of an inductive, deployable pipeline. Never use
external outcomes to choose or tune either transform.

## Site-aware validation

- Use patient-level nested resampling for development; stratify without breaking
  patient or site grouping.
- When multiple centers exist, add leave-one-site-out, geographic, or site-held-out
  evaluation. A pooled random split is not external validation.
- Prefer temporal validation when assay platforms or workflow change over time.
- Lock feature definitions, preprocessing, missingness handling, fusion, and thresholds
  before fully external evaluation.
- Verify that the frozen harmonization and preprocessing transform runs on each unseen
  patient/site without access to the remaining validation cohort; otherwise label the
  evaluation transductive.
- Report each site's modality availability, batch/platform, exclusions, and case mix.
  For supervised prediction, add endpoint prevalence, performance, and calibration by
  site and common availability pattern. For unsupervised discovery, report cluster or
  factor distribution, assignment uncertainty, and stability by site and pattern.
- If the external cohort lacks a required modality, evaluate a pre-specified compatible
  model; do not call it validation of the full five-dimensional model.

For supervised prediction, report endpoint-appropriate performance with confidence
intervals, calibration, and clinical-utility measures when justified. For unsupervised
discovery, report resampling stability, assignment uncertainty, locked factor projection
or cluster assignment, block-removal alignment, and independent replication. Quantify
between-site heterogeneity rather than averaging it away; use outcomes only as secondary
associations in discovery.

## Ablation and contribution reporting

Use the same splits and evaluation patients for all comparisons.

### Supervised prediction

Report predictive contribution using:

| Analysis | Question answered |
|---|---|
| Clinical-only and each single block | How much can each input achieve alone? |
| Strongest block plus clinical variables | Does fusion improve a realistic comparator? |
| Simple early or late fusion | Does the complex architecture beat a low-complexity fusion? |
| Leave-one-block-out full model | Which blocks carry non-redundant predictive information? |
| Block permutation or conditional permutation | How sensitive is the locked model to a block after accounting for correlation? |
| Full model by missingness pattern and site | Does performance survive the intended deployment conditions? |
| Pre-specified interaction removal | Does a claimed interaction add reproducible value beyond main effects? |

Show effect estimates or metric differences with uncertainty, not ranks alone. Refit the
model when the estimand requires leave-one-block-out comparison; merely zeroing a block
can create an out-of-distribution input. Do not translate ablation importance into
causality or biological mechanism.

### Unsupervised discovery

Do not require predictive single-block baselines, calibration, event counts, conditional
permutation, or interaction tests unless a separate supervised analysis makes them
relevant. Instead report:

- cluster/factor alignment between the full solution and each leave-one-block-out
  solution, with label matching or factor matching defined in advance;
- resampling and perturbation stability for the full and block-removed solutions;
- assignment uncertainty for new patients under the prespecified assignment or
  factor-projection rule;
- sensitivity of cluster sizes, factor loadings, and site/batch enrichment to each
  block's removal;
- independent replication using the locked preprocessing, tuning, and assignment rule;
- outcomes only as secondary associations, never as criteria for choosing the solution.

## Minimum sensitivity package

- complete-case versus broader-pattern analysis, where scientifically coherent;
- alternative reasonable within-block preprocessing or imputation;
- site- or batch-held-out evaluation;
- supervised: single-block, simple-fusion, predictive leave-one-block-out, conditional
  permutation, and pre-specified interaction comparisons;
- unsupervised: block-removal cluster/factor alignment, stability, assignment
  uncertainty, and independent replication;
- missing-modality stress tests using observed deployment patterns;
- analysis excluding sites or batches that nearly determine outcome or availability;
- explicit accounting of patients lost at each linkage and QC step.

If any sensitivity result changes the conclusion materially, report that instability
and narrow the claim rather than selecting the favorable analysis.
