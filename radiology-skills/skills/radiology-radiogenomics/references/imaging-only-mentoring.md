# Imaging-only research mentoring

Use this module in `mentor` or `combined` mode when the study remains imaging-only. Help the learner
turn radiography, CT, MRI, PET, ultrasound, radiomics, deep imaging or habitat data into a defensible
technical or clinical question. Do not require tissue, omics, pathology or a molecular mechanism
unless the user explicitly changes the scope.

## 1. Start with the imaging question

Write one sentence:

`In [population and clinical setting], does [locked imaging phenotype/model] [characterize,
associate with, diagnose or predict] [defined endpoint] at [patient/lesion/time unit], compared with
[clinical/simple imaging baseline], as evaluated by [validation design]?`

Clarify:

- intended use and decision point;
- population, eligibility, disease spectrum and time zero;
- imaging modality, sequence/tracer, ROI and phenotype/model;
- patient versus lesion/scan/ROI hierarchy;
- endpoint, comparator and current claim branch;
- development, temporal, geographic, multisite or external validation resources.

An imaging-only question may be scientifically valuable without a molecular story. Do not describe a
radiomic feature, saliency map, embedding or habitat as a “non-invasive biopsy” or mechanism.

## 2. Teach validity before complexity

Use this order:

1. cohort flow, exclusions, missingness and independent unit;
2. acquisition/reconstruction and preprocessing provenance;
3. annotation/segmentation protocol, blinding and reproducibility;
4. feature or model stability and train-only data-dependent operations;
5. patient-level separation, leakage prevention and tuning design;
6. estimand, uncertainty, multiplicity, calibration and missing-data handling;
7. simple imaging and clinical comparators;
8. internal versus independent validation, failure cases and transportability;
9. intended-use, workflow and reporting boundary.

If an upstream gate fails, preserve the nearest valid technical or descriptive question rather than
adding model complexity.

## 3. Generate three materially different routes

| Route | Typical design | Claim ceiling | Main trade-off |
|---|---|---|---|
| Conservative | reproducibility/QC study, prespecified association, or simple locked model with honest internal validation | technical validity, description or bounded association | feasible now but narrower contribution |
| Standard | patient-level nested development, strong clinical/simple baseline, calibration, temporal/geographic validation and sensitivity analyses | bounded diagnostic/prognostic prediction in the tested setting | more data curation and validation burden |
| Ambitious | prospective or external multisite locked evaluation, reader comparison, workflow impact, subgroup/fairness and drift assessment | transport, utility or implementation only for evidence actually collected | highest coordination, sample and operational burden |

Recommend one using identifiability, matched usable n, event count, site/scanner spectrum, annotation
burden, validation independence, time and cost. An ambitious route is optional, not a hidden defect in
a valid narrower study.

## 4. Competing explanations and falsifiers

For an imaging association or performance result, test at least:

- disease severity, lesion volume, site/scanner/protocol and acquisition artifacts;
- segmentation/annotation instability and preprocessing sensitivity;
- prevalence/spectrum shift, missingness, treatment timing and follow-up;
- leakage, shortcut features, confounded labels or repeated-patient contamination;
- whether a simple clinical or imaging baseline explains the apparent gain.

Name the result pattern that would support the intended explanation and the pattern that would force
weaker wording or a redesigned study.

## 5. Learner-facing decision contract

For each major recommendation return:

`principle -> supplied/inspected evidence -> consequence -> current verdict -> conservative/standard/
ambitious options -> trade-offs -> recommendation -> next executable action -> success/failure criterion`.

When the preferred plan fails, return:

`blocked claim -> reason -> nearest answerable imaging question -> minimum repair or evidence ->
wording allowed now -> smallest next action`.

Ask only questions that change the estimand, independent unit, validation design or requested artifact.
Do not transfer the decision back through a list of algorithms.

## 6. Writing and review boundary

For writing, preserve true cohort counts, acquisition/annotation facts, train-only pipeline, validation
level, comparator, uncertainty, calibration and transport boundary. For manuscript review, pair this
mentor module with `imaging-reviewer-playbook.md` and the constructive review chain. A future molecular
study may appear as an optional hypothesis only; it does not become a requirement or present result.
