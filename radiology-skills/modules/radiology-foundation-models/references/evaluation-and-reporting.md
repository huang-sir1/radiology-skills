# Foundation-Model Evaluation and Reporting

Use this reference to make foundation-model comparisons independent, fair, reproducible, and
clinically bounded. A locked downstream test is not automatically independent: pretraining exposure
can precede the study and still contaminate evaluation.

## Contents

- [Pretraining overlap and leakage audit](#1-pretraining-overlap-and-leakage-audit)
- [Frozen split and evaluation protocol](#2-frozen-split-and-evaluation-protocol)
- [Fair baseline and budget design](#3-fair-baseline-and-budget-design)
- [Task performance and statistical comparison](#4-task-performance-and-statistical-comparison)
- [Calibration](#5-calibration)
- [Uncertainty and abstention](#6-uncertainty-and-abstention)
- [Subgroup, site, and shift evaluation](#7-subgroup-site-and-shift-evaluation)
- [External validation and model exposure](#8-external-validation-and-model-exposure)
- [Compute, energy, and carbon reporting](#9-compute-energy-and-carbon-reporting)
- [Reproducibility, checkpoint, and license disclosure](#10-reproducibility-checkpoint-and-license-disclosure)
- [Minimum reporting table](#11-minimum-reporting-table)
- [Claim limits](#claim-limits)

## 1. Pretraining overlap and leakage audit

Create a provenance-and-overlap table for every candidate checkpoint and evaluation cohort:

| Field | Required record |
|---|---|
| Checkpoint | Model name, version, source, release date, hash, parent checkpoint, modifications |
| Pretraining data | Named datasets, institutions, collection dates, modalities, anatomy, reports/text, public/private status |
| Deduplication | Patient/study/image/report/near-duplicate methods, identifiers or hashes used, known residual risk |
| Evaluation cohort | Institution, dataset, collection dates, patient/study counts, public/private status |
| Overlap result | Excluded, detected and removed, model-exposed, or unknown |
| Independence claim | Independent, non-independent/model-exposed, or indeterminate, with rationale |

Check for overlap at multiple levels:

- dataset release or named benchmark;
- institution and acquisition date;
- patient and examination identifiers;
- DICOM identifiers and image hashes;
- resized, cropped, compressed, or otherwise near-duplicate images;
- report text, captions, labels, and derived image-text pairs;
- repeated scans, bilateral organs, lesions, patches, slices, and video frames from one patient.

Use checkpoint-specific evidence. A generic statement that “public data were removed” does not
establish that a particular evaluation cohort was excluded. If the pretraining corpus is not
disclosed, state that overlap cannot be ruled out and qualify the evaluation accordingly.

Downstream leakage checks must also cover:

- patient/site/time contamination across train, validation, and test;
- preprocessing, harmonization, pooling, feature selection, prompts, thresholds, or calibration
  fitted using held-out data;
- report text that contains the target diagnosis or outcome;
- labels or metadata unavailable at prediction time;
- repeated testing that influenced model, prompt, or checkpoint selection;
- target-domain adaptation performed on the dataset later described as untouched external
  validation.

## 2. Frozen split and evaluation protocol

Define and version:

1. patient-level development partitions and inner tuning folds;
2. outer internal validation or a sealed internal test;
3. temporal, geographic, or institutional external cohorts;
4. all exclusion, deduplication, and repeated-measure grouping rules;
5. primary outcome, metric, confidence interval, comparison method, and subgroup plan;
6. the point at which preprocessing, prompts, architecture, adaptation, calibration, and thresholds
   are frozen.

Preserve site, family, examination, lesion, specimen, slice, patch, and temporal dependencies. Do
not use the external cohort to select the adaptation route, learning rate, prompt, threshold, or
calibration method. If selection occurs, relabel it target-development data and seek another
untouched cohort.

## 3. Fair baseline and budget design

### Baseline ladder

Use comparators that answer distinct questions:

- **clinical or operational baseline:** current score, reader, workflow, or standard method when
  relevant;
- **task-specific baseline:** a strong architecture designed and trained for the endpoint;
- **conventional transfer baseline:** a non-foundation pretrained encoder with a comparable head;
- **frozen representation baseline:** a linear or shallow probe;
- **adaptation ablations:** partial tuning, parameter-efficient tuning, and full tuning as needed to
  identify the source of gain.

For segmentation, include an established task-specific pipeline where appropriate. For
classification or prognosis, include a regularized conventional model and clinically relevant
variables when they are available at prediction time. For image-text tasks, compare against
task-specific text or image-only alternatives and report modality ablations.

### Fairness of comparison

Hold constant:

- eligible patients, exclusions, outcome definitions, split assignments, and random split seeds;
- input modalities, resolutions, temporal windows, and prediction-time information;
- reference standards and annotation versions;
- preprocessing and augmentation opportunities, unless the model requires a documented input
  contract;
- tuning objective, stopping policy, number of seeds, metric computation, and test access.

Use a prespecified tuning policy. Depending on the question, this can be:

- an equal number of trials and seeds;
- a matched accelerator-hour or energy budget;
- a standardized expert-derived configuration plus a sensitivity analysis.

No policy makes every model equally easy to optimize. Report the policy, actual trials, failures,
runtime, and total compute so readers can interpret both performance and optimization effort. Do
not compare a heavily tuned foundation model against an untuned default baseline.

## 4. Task performance and statistical comparison

Use metrics appropriate to the output and intended use:

- classification: discrimination, sensitivity, specificity, predictive values at prespecified
  thresholds, and class-wise results;
- regression/prognosis: prediction error, calibration, time-dependent metrics, and clinically
  relevant horizons;
- segmentation/detection: overlap plus boundary or lesion-level metrics, false positives, and
  case-level failure;
- retrieval: recall/precision at prespecified ranks and clinically meaningful query strata;
- generation: task-grounded factuality, omission/commission errors, expert evaluation, and
  workflow-relevant outcomes rather than lexical similarity alone.

Report confidence intervals and paired comparisons because models are evaluated on the same cases.
Account for clustering by patient, site, reader, or repeated examination. Pre-specify one primary
metric and treat broad metric searches as exploratory. Report per-seed results or between-run
variation rather than only the best checkpoint.

## 5. Calibration

For probabilistic outputs, report calibration on the frozen evaluation data using:

- calibration plots with uncertainty;
- calibration intercept and slope when appropriate;
- Brier score or another proper scoring rule;
- threshold-specific observed risk and decision consequences.

Fit temperature scaling, isotonic regression, Platt scaling, or other recalibration on development
or dedicated calibration data only. Apply the frozen mapping to each test domain. Report both
before and after recalibration, the calibration sample source, and whether recalibration is
site-specific. Good discrimination does not imply good calibration, and pooled calibration can
hide site or subgroup miscalibration.

## 6. Uncertainty and abstention

Name the uncertainty target: predictive probability, epistemic variability, aleatoric ambiguity,
segmentation confidence, out-of-distribution score, or selective prediction. State the estimation
method and its computational cost.

Evaluate whether uncertainty is useful:

- error detection or risk-coverage/selective-risk curves;
- calibration of confidence;
- performance on low-quality inputs, rare findings, and shifted sites or scanners;
- failure under plausible corruptions;
- subgroup and prevalence sensitivity;
- comparison with simple confidence baselines.

Do not claim safety from entropy, ensemble variance, or a heatmap alone. If the model abstains,
define the threshold without test access, coverage, error among accepted cases, error among
rejected cases, and the downstream human workflow.

## 7. Subgroup, site, and shift evaluation

Pre-specify clinically and technically plausible groups: age, sex or gender as recorded,
race/ethnicity where valid and ethically appropriate, disease severity, rare classes, acquisition
site, scanner vendor, field strength, protocol, image quality, referral pathway, and time period.

For every group, report:

- denominator, outcome count or prevalence, and missingness;
- performance and calibration with uncertainty;
- absolute differences and interaction or heterogeneity analyses when justified;
- whether thresholds or recalibration differ;
- small-sample limitations and multiplicity.

Do not infer fairness from nonsignificant subgroup differences. Small groups often have wide
uncertainty. Avoid biological interpretations of administrative or socially constructed
categories, and do not invent unavailable subgroup data.

## 8. External validation and model exposure

A defensible external cohort differs meaningfully in institution, geography, time, workflow, or
population; was not used for pretraining, downstream fitting, prompt selection, adaptation,
calibration, thresholding, or model choice; and receives the frozen pipeline.

Report:

- inclusion flow, prevalence, missingness, case mix, scanner/protocol differences, and label route;
- any input incompatibility or cases the model cannot process;
- performance, calibration, uncertainty, subgroup/site results, and failure cases;
- whether local recalibration or adaptation was performed.

If local adaptation is necessary, separate the cohort into target-development and untouched
target-test partitions or use a design that preserves unbiased evaluation. A participating
pretraining institution, a benchmark known to be in pretraining, or a target cohort used for
test-time optimization is model-exposed, not independent external validation.

## 9. Compute, energy, and carbon reporting

For every principal model and baseline, report:

- total and trainable parameters;
- hardware type and count, memory, precision, and distributed strategy;
- number of trials, seeds, epochs or steps, early-stopping rule, and failed/repeated runs;
- wall-clock training time, accelerator-hours, peak memory, and inference latency/throughput;
- energy consumed when measured, measurement tool and boundary;
- carbon estimate when available, including energy source or region, carbon-intensity source,
  assumptions, and whether embodied hardware emissions are excluded.

Distinguish pretraining cost, which may be unknown or reported by the model developer, from the
downstream adaptation and evaluation cost measured by the study. Do not fabricate energy or carbon
precision. If unavailable, report hardware and runtime transparently and state the limitation.

## 10. Reproducibility, checkpoint, and license disclosure

Release or archive, subject to governance and license:

- model name, exact version, source URL or repository record, parent checkpoint, and cryptographic
  hash;
- downstream head, adapter, LoRA delta, prompt, or merged-checkpoint hash;
- code commit, environment lockfile, library and driver versions, hardware, seeds, and deterministic
  settings;
- data manifests or stable dataset identifiers, split manifests, exclusions, and preprocessing
  configuration;
- hyperparameter search space, trial results, selected configuration, logs, and evaluation script;
- model card updated with intended use, evaluated populations, limitations, failures, and overlap
  status.

State the licenses for code, base weights, derivative weights or deltas, datasets, and outputs.
Check restrictions on modification, redistribution, commercial or clinical use, attribution,
derivatives, hosted access, and revocation. “Open weights” does not necessarily mean open source or
permission for clinical deployment. If weights cannot be shared, describe an access route or
reproducibility limitation without violating the license.

## 11. Minimum reporting table

| Domain | Report |
|---|---|
| Provenance | Model card, checkpoint/version/hash, pretraining objective and data sources, release date |
| Overlap | Deduplication method, overlap class for every cohort, exclusions, residual uncertainty |
| Data | Cohort flow, sites/dates, patient and study counts, prevalence/events, input and label definitions |
| Adaptation | Frozen/trainable components, strategy, prompts, optimizer, schedule, stopping, seeds |
| Comparisons | Baseline rationale, identical splits/inputs, tuning-budget policy, actual trials and compute |
| Evaluation | Primary metric and CI, paired comparisons, calibration, uncertainty, subgroups, sites, external cohort |
| Resources | Parameters, hardware, memory, runtime, accelerator-hours, inference cost, energy/carbon boundary |
| Reproducibility | Code/environment/data manifests, hashes, configs, logs, split files |
| Legal/release | Code, weights, data and output licenses; access and redistribution restrictions |
| Claims | Supported population/task/domain, model-exposure caveats, failures, prohibited extrapolations |

## Claim limits

Use narrow language:

- “The adapted checkpoint improved the prespecified metric over the stated baselines on these
  frozen cohorts” is supportable when the comparison is fair.
- “The representation transferred to an unseen institution” requires a genuinely unexposed,
  untouched institution and a frozen pipeline.
- “The model is general,” “clinically useful,” “fair,” “safe,” or “deployment ready” requires
  evidence beyond a retrospective average metric.
- Unknown pretraining overlap, undisclosed checkpoints, incompatible licensing, unstable seeds,
  poor calibration, or absent external validation must appear in the conclusion, not only in a
  supplement.
