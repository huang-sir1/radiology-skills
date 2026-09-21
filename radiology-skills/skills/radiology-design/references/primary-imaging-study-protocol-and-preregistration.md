# Primary imaging-study protocol and preregistration

Use this reference to turn an imaging research idea into a frozen, auditable protocol before outcome-
aware modelling or protected-test access. It covers diagnostic, prediction, detection, segmentation,
longitudinal, reconstruction, reader and clinical-impact studies. It does not replace ethics approval,
a trial registry's current requirements, a full statistical analysis plan (SAP), or a modality-specific
acquisition protocol.

## 1. Keep four artifacts distinct

| Artifact | Purpose | Minimum timing |
|---|---|---|
| Scientific protocol | why, who/what, design, measurements, outcomes, analysis intent and governance | before enrollment/data selection or before retrospective cohort construction becomes outcome-aware |
| SAP | executable estimands, populations, models, uncertainty, multiplicity, missingness, validation and sensitivity | before confirmatory outcome inspection/protected-test access |
| Preregistration/registry record | public/time-stamped subset of the protocol on an appropriate platform | prospectively whenever applicable; record actual status honestly |
| Amendment/deviation log | what changed, when, why, whether result-aware and what it invalidates | contemporaneously; never overwrite the frozen version |

Registration is not ethics approval, peer review, protocol quality or proof of prospective conduct. A
retrospective registration remains useful transparency but must be labelled retrospective.

## 2. Declare applicability and evidence state

Record:

```text
Study family:
Jurisdiction/institution:
Human-participant/interventional status:
Applicable registry/policy and live verification date:
Registration platform / record ID / public link:
Registration status: PROSPECTIVE / RETROSPECTIVE / UNREGISTERED / NOT_APPLICABLE / NOT_VERIFIED
Protocol version/date/digest:
SAP version/date/digest:
Outcome/test-access state at each freeze:
Ethics/consent/data-use state and evidence locator:
```

Use `NOT_VERIFIED` until a real record or official receipt is inspected. Do not invent an ID, approval
or prospective status. Trial-registration obligations depend on design, jurisdiction, sponsor and
journal; verify them live with the responsible governance owner.

## 3. Minimum protocol contract

### A. Question and claim

- clinical/scientific decision, target population and pathway position;
- task-specific question and estimand, primary independent unit and hierarchy;
- primary hypothesis/contrast and smallest effect or precision worth detecting;
- comparator, intended use, action/threshold and preliminary claim ceiling;
- confirmatory versus exploratory components.

Open the matching task contract under `references/tasks/` and attach its task card. A project may have
multiple tasks, but each needs its own estimand, denominator, reference process and success criterion.

### B. Design and sampling

- prospective/retrospective, observational/interventional, single/multicenter, cohort/cross-sectional/
  case-control, reader/cluster/time-series or other exact design;
- setting, recruitment/export source, calendar period and consecutive/random/convenience sampling;
- inclusion/exclusion and index-exam/time-zero rules that can be applied without outcome/model knowledge;
- sampling frame, expected prevalence/event information, spectrum, verification and referral pathway;
- participant/patient/exam/lesion/report linkage and overlap/duplicate-public-dataset audit;
- target, development, validation and analysis populations with flow reconciliation.

### C. Imaging and technical input

- modality, body region, views/sequences/phases and series-selection algorithm;
- acquisition/reconstruction parameters, dose/count/contrast timing and protocol/site/scanner ranges;
- image-quality acceptance, missing/corrupt-series policy and technical deviation log;
- DICOM/derived-format provenance, de-identification and frame-of-reference/geometry checks;
- preprocessing fixed versus learned, registration/resampling/interpolation and software/version.

Route detailed technical conformance to the acquisition/physics owner. Do not use a generic protocol
cutoff when modality, vendor or quantitative-biomarker requirements differ.

### D. Reference standard, labels and readers

- target construct/ontology, label unit, uncertainty/non-evaluable states and reference-standard source;
- timing, blinding, information available, reader number/expertise, training/calibration, independent
  reads, consensus/adjudication and provenance;
- report-derived/weak/model-assisted labels and clean-reference evaluation plan;
- longitudinal lesion/exam linking, criteria/version and inter-/intra-reader assessment where relevant.

### E. Intervention/index test/model and comparator

- complete executable version, inputs available at use, output and abstention/failure states;
- architecture/algorithm only after the clinical/task contract; simple and real-world comparators;
- training/tuning plan, data-dependent preprocessing, candidate parameter complexity and stopping rule;
- model/prompt/retrieval/checkpoint/configuration provenance and allowed updating.

### F. Partition and access governance

- patient-level grouping plus family, repeat, lesion, series, timepoint and site dependencies;
- derivation, internal resampling, temporal/geographic/external and prospective roles;
- split-generation code/seed, immutable manifest and overlap checks;
- which roles can see labels, outcome summaries and protected-test predictions;
- test-access events, permitted diagnostics and consequence of access;
- rule that threshold/model selection and compatible harmonisation are fitted within development only.

### G. Outcomes, analysis and sample size

- one primary endpoint/estimand, time horizon, scale, operating point/margin and success criterion;
- secondary/exploratory families, subgroup/fairness analyses and multiplicity policy;
- effect/performance measures, uncertainty unit, clustering/repeated measures and calibration;
- missing/non-evaluable/exclusion strategy and sensitivity/negative-control/falsification analyses;
- input-driven sample-size/precision/power rationale with nuisance-source and feasibility scenarios;
- link to the frozen SAP and `BIOSTATISTICIAN_REQUIRED` gates.

### H. Ethics, safety and open science

- ethics/consent/waiver, secondary use, data agreements and privacy/security;
- participant/reader risks, incidental findings, clinical override/fallback and adverse-event reporting;
- code/environment/config/seeds, data/model card, licenses, access restrictions and preservation plan;
- funding, conflicts, sponsor role, patient/public involvement where applicable;
- dissemination, negative-result/deviation policy and reporting-guideline stack.

## 4. Preregistration fields

A registration should make undisclosed outcome switching difficult. At minimum preserve:

```text
question/PICOTS or task card
design, setting and recruitment/sampling dates
eligibility and primary independent unit
planned sample/information size and rationale
imaging/index/model/comparator versions
reference standard and label process
primary outcome/estimand/horizon/threshold or margin
analysis population and primary model/test
partition/external-test and test-access policy
missingness, multiplicity, subgroup and sensitivity policies
study status and whether data/outcomes/test results have been accessed
ethics/registration identifiers actually verified
protocol/SAP/code locators and version/date
```

If the platform cannot hold the full plan, archive a versioned protocol/SAP and register its immutable
locator/digest. An editable private document with no dated receipt is not preregistration evidence.

## 5. Freeze and amendment workflow

1. Draft protocol from verified inputs; unresolved facts remain `AUTHOR_INPUT_NEEDED`.
2. Obtain clinical, acquisition/physics, annotation, statistics and governance review appropriate to
   the task.
3. Freeze version, date, digest, approver roles and actual outcome/test-access state.
4. Register where applicable and preserve the receipt/public record.
5. Execute against immutable cohort/split/config manifests.
6. Log every change with old/new text, reason, timing, result awareness and affected estimand/output.
7. Distinguish amendment (planned design changed) from deviation (conduct differed) and exploratory
   analysis (new question after evidence access).
8. Report the frozen primary result before any repaired, adapted or updated result.

Never backdate a freeze or silently replace the registered outcome/model. A scientifically necessary
result-aware change is allowed when disclosed; it changes confirmatory status.

## 6. Study-family additions

| Family | Required addition |
|---|---|
| Diagnostic accuracy/triage | sampling spectrum, verification/blinding, indeterminate results, threshold/action and STARD route |
| Prediction/prognosis | index time, predictor availability, event/censoring, calibration, model complexity and TRIPOD+AI/PROBAST+AI route |
| Detection/segmentation | candidate/contour matching, multiple lesions/classes, reader reference and clustered metrics |
| Longitudinal/response | time zero, visit windows, intercurrent events, lesion linkage, registration and missing observation process |
| Reconstruction/enhancement | paired/raw reference, dose/time, physical/task metrics, margin and hallucination/failure tests |
| Reader/clinical impact | reader/site/period allocation, order/washout, contamination, workflow clocks, safety and CONSORT/SPIRIT/DECIDE-AI route as applicable |
| VLM/report generation | model/prompt/retrieval snapshot, contamination/privacy audit, human error taxonomy and change control |

## 7. Stop gates

Return `STOP_FOR_REPAIR` when the primary estimand, time zero, independent unit, reference standard,
sampling frame or protected-test boundary is undefined; participant overlap cannot be excluded; or a
claimed prospective registration cannot be verified. Return `BIOSTATISTICIAN_REQUIRED` when the
primary model, sample-size inputs, dependence, causal identification or complex longitudinal/MRMC
analysis remains unresolved.

## Primary and official sources

- SPIRIT–CONSORT Group. [Published SPIRIT 2025 and CONSORT 2025 statements](https://www.consort-spirit.org/published-statements).
- WHO. [Trial Registration Data Set](https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set).
- ClinicalTrials.gov. [Protocol Registration Data Element Definitions](https://clinicaltrials.gov/policy/protocol-definitions).
- Center for Open Science. [OSF Registries](https://osf.io/registries/).
- Bossuyt PM, et al. [STARD 2015](https://doi.org/10.1136/bmj.h5527).
- Collins GS, et al. [TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378).
- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).

These sources serve different study families. Apply only the relevant stack and verify current versions
through `radiology-reporting`; do not present a reporting checklist as a design-quality guarantee.
