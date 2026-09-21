# Experiment provenance and model card

## Experiment record

Preserve for every reported run or locked ensemble:

- run ID, purpose, date, code version/commit, configuration file, random seeds;
- cohort/split manifest at patient level, center/time role, and duplicate/overlap audit;
- preprocessing, augmentation, sampling, loss, optimizer, schedule, stopping, and checkpoint rule;
- hyperparameter search space, budget, selection metric, and inner/outer validation scope;
- pretrained weights/model version, adaptation method, licensing/access, and frozen/trainable layers;
- hardware, accelerator count/type, major library/runtime versions, training time when available;
- output predictions with patient IDs/hashes, cohort, outcome, and checkpoint ID;
- planned versus executed deviations and reason.

## Test-set access log

Record each evaluation against the test/external set: date, code/model version, reason, metrics
returned, and whether any later decision used those metrics. Repeated test-set-driven model changes
turn the test set into validation and must be disclosed or corrected with a new independent set.

## Model card minimum

| Domain | Record |
|---|---|
| Intended use | population, modality, workflow point, output, user, excluded uses |
| Data | development/validation sources, centers, dates, prevalence/spectrum, missing modalities |
| Performance | discrimination/task metric, calibration, utility, uncertainty, subgroup/fairness |
| Robustness | scanner/site/protocol shift, OOD, artifacts, missing inputs, failure cases |
| Explainability | method, stability/quantitative check, bounded interpretation |
| Limitations | known failure modes and evidence gaps |
| Governance | oversight, privacy, version/change control, monitoring if deployed |

## Negative and failure results

Preserve failed configurations, unstable models, subgroups with degraded performance, shortcut
signals, calibration failures, and robustness tests that did not pass. Do not show only favorable
examples. Decide whether each belongs in the manuscript, supplement, limitation, or internal log.

## Handoff

Register the final run/model artifact IDs with `radiology-pipeline`. Figures and tables must point to
the same prediction files and checkpoint IDs; manuscript Methods must describe the same configuration.
