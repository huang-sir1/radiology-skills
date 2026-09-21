# Regulatory and deployment readiness for imaging AI

Use this reference when a manuscript or proposal wants to move from retrospective model performance toward clinical implementation, regulatory framing, or real-world validation.

## Maturity map

| Application type | Current maturity pattern | Typical role |
|---|---|---|
| Acute triage/notification | relatively mature among radiology AI products | parallel workflow prioritization, not autonomous diagnosis |
| CAD/assistive detection | mature in selected domains such as breast and emergency imaging | concurrent aid to radiologist |
| Reconstruction / enhancement / quantification | mature and often easier to evaluate | image quality, speed, quantitative measurement |
| Segmentation / radiation oncology contouring | increasingly mature | workflow acceleration with human review |
| Report generation / VLM | active research, expert-evaluation stage | draft/report aid, not independent final report |
| Radiogenomics genotype prediction | high-potential research, less mature regulatory category | hypothesis support, risk stratification, trial enrichment; not replacement for molecular testing |

## Evidence-state boundary

First open `evidence-state-and-translation-lifecycle.md` and maintain seven orthogonal states:
technical/analytical performance, clinical validation, clinical utility/impact, regulatory status,
HTA/economic value, implementation state and production monitoring. A high state on one axis never
promotes another axis.

Use this ladder:

| Evidence | Claim allowed |
|---|---|
| Retrospective internal performance | feasibility / development |
| Retrospective external validation | generalisability under tested conditions |
| Silent/shadow deployment | prospective technical availability, drift and counterfactual performance; **no human-AI interaction or care-impact evidence** |
| Controlled reader-assist study | human-AI performance under the tested reader/case/interface conditions; no live workflow or patient-benefit claim |
| Prospective validation | intended-use performance |
| Clinical impact study or trial | patient/workflow outcome effect |
| Regulatory-cleared locked model | use only within cleared intended use |

Do not describe a model as deployment-ready if it has only retrospective discrimination.

Also enforce:

- external validation does not establish clinical utility;
- regulatory clearance/approval does not establish patient benefit, reimbursement, procurement or
  local activation;
- DCA/net benefit is not an economic evaluation;
- DICOM conformance is not end-to-end interoperability;
- QIBA/phantom precision is not clinical validity; and
- no drift alert is not evidence of stability when labels are delayed, missing or selectively verified.

## Regulatory-facing design questions

Before claiming translation, answer:

- What is the intended use and user?
- Is the output a notification, detection aid, risk score, segmentation, report draft, or molecular-risk clue?
- Is the model locked or adaptive?
- What is the versioning/change-control plan?
- What data represent the intended-use population?
- What subgroup/site/scanner performance and calibration are known?
- What happens when the model abstains, fails, or sees OOD input?
- How will drift, recalibration, and failure feedback be monitored?
- What human oversight is required?

## Silent deployment plan

Silent deployment is useful between retrospective validation and active clinical use:

```text
frozen model
-> runs prospectively without influencing care
-> logs outputs, latency, failures, OOD flags, calibration, subgroup/site performance
-> compares against final clinical outcomes
-> defines thresholds and human-review triggers before active deployment
```

## Reader-assist / workflow endpoints

For clinical utility, include endpoints beyond AUC:

- time to notification or report
- reader sensitivity/specificity/AUC with and without AI
- confidence and workload
- clinically significant error reduction
- downstream management or MDT decision change
- net benefit across plausible thresholds
- automation bias or overreliance assessment

## International readiness

For regulatory-aware proposals, include:

- risk management
- high-quality and representative data
- transparency/user information
- human oversight
- traceability and audit logs
- post-deployment monitoring
- predefined change-control or revalidation rules

Exact FDA/EU guidance titles, dates, and device-list examples must be verified live before submission.

## Jurisdiction and source-status ledger

For every regulatory statement record `jurisdiction | product/version/intended use | source title |
official URL | document status (draft/final/rule/etc.) | issue/effective date | accessed date |
qualified owner | exact permitted wording | unresolved action`. Use `LIVE_VERIFICATION_REQUIRED` when
any field can affect the decision.

Verified snapshot on 2026-08-23:

- IMDRF N41 SaMD Clinical Evaluation: final, 2017;
- IMDRF N88 GMLP: final, 2025;
- FDA AI-enabled device lifecycle/marketing-submission recommendations: **draft, not for
  implementation**, January 2025;
- FDA AI-enabled PCCP guidance: final, August 2025;
- FDA QMSR: official page states effective 2026-02-02.

These are source states, not a finding that they apply to a specific product or jurisdiction. Formal
classification, submission, quality-system, safety and authorization decisions require qualified
local regulatory/quality/clinical owners.

## Primary official sources

- [IMDRF N41 SaMD Clinical Evaluation](https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation)
- [IMDRF N88 GMLP](https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles)
- [FDA AI-enabled device lifecycle draft](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing)
- [FDA PCCP final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence)
- [FDA QMSR](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr)
