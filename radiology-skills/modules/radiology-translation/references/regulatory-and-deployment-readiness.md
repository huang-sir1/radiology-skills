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

## Claim boundary

Use this ladder:

| Evidence | Claim allowed |
|---|---|
| Retrospective internal performance | feasibility / development |
| Retrospective external validation | generalisability under tested conditions |
| Reader-assist or silent deployment | workflow or human-AI interaction evidence |
| Prospective validation | intended-use performance |
| Clinical impact study or trial | patient/workflow outcome effect |
| Regulatory-cleared locked model | use only within cleared intended use |

Do not describe a model as deployment-ready if it has only retrospective discrimination.

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
