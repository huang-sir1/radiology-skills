# Study blueprints — design templates with minimum-viable vs stronger versions

Pick the template that matches the clinical question. For each, the **minimum-viable (MVP)**
version is what is publishable now; the **stronger** version is what reaches a higher tier.
Every blueprint must end with a validation plan (validation-strategy.md) and a reporting
guideline (→ radiology-reporting).

## 1. Diagnostic accuracy (test vs reference standard)
- **Question:** does the imaging/AI test correctly classify disease vs a reference standard?
- **MVP:** prospective or consecutive retrospective cohort, credible reference standard,
  sensitivity/specificity/AUC with CIs, real prevalence reported.
- **Stronger:** multi-reader comparison (radiologist vs AI vs radiologist+AI), external cohort,
  reader study (→ radiology-translation).
- **Guideline:** STARD 2015 (STARD-AI + CLAIM if the index test is AI); QUADAS-3 v1.2 when
  primary-study accuracy estimates are appraised in a review, with QUADAS-C alongside QUADAS-3
  for eligible within-study comparative-accuracy assessments.

## 2. Prediction / prognosis model
- **Question:** does an imaging-derived score predict an outcome (recurrence, survival, or response)
  in a defined care/treatment context? A single-treatment cohort supports prognosis under that
  context, not differential treatment benefit.
- **MVP:** patient-level split, model with discrimination **and calibration**, decision-curve
  analysis, internal validation (bootstrap/CV), EPV respected.
- **Stronger:** external/temporal validation, comparison vs established clinical model, net
  benefit across thresholds, subgroup stability.
- **Guideline:** TRIPOD+AI (2024) + PROBAST+AI (2025).

## 3. Treatment-response / longitudinal
- **Question:** first identify which estimand is intended:
  - **Treatment-contextual prognosis:** does imaging predict response/progression among patients
    receiving a specified treatment? A single arm may answer this bounded prediction question.
  - **Average treatment effect (ATE):** what is the average contrast between defined treatment
    strategies in a target population?
  - **Effect modification / predictive biomarker:** does treatment benefit differ by an imaging
    marker, requiring a treatment-by-marker contrast rather than separate within-arm significance?
- **MVP for treatment-contextual prognosis:** defined response criteria (e.g. RECIST or a
  disease-specific standard), explicit time zero, baseline+follow-up imaging, uniform outcome
  ascertainment, and treatment exposure described. Bound the claim to the observed treatment
  context.
- **MVP for ATE or effect modification:** a credible treatment comparator (randomised when
  feasible; otherwise a defensible causal design), aligned eligibility/time zero/follow-up,
  positivity/overlap, pre-treatment confounders, treatment switching/censoring handling, and a
  pre-specified treatment contrast. For effect modification, test and report the interaction or
  another explicitly defined heterogeneous-treatment-effect estimand; two within-arm P values do
  not establish a difference.
- **Stronger:** external/temporal validation of prognostic performance; for causal treatment claims,
  independent confirmation of the treatment contrast, sensitivity to unmeasured confounding and
  treatment switching, and decision-relevant absolute effects. Delta-radiomics additionally needs
  acquisition/registration reproducibility and a landmark that avoids immortal-time leakage.
- **Guideline:** TRIPOD+AI / STARD as applicable; report longitudinal acquisition consistency.

## 4. Segmentation / detection
- **Question:** can the model delineate/detect the target reproducibly?
- **MVP:** high-quality reference masks, Dice/HD/sensitivity with CIs, held-out test, failure
  cases shown.
- **Stronger:** multi-center/scanner test, inter-observer reference, downstream-task impact
  (does better segmentation improve the clinical endpoint?).
- **Guideline:** CLAIM; report annotation protocol (→ radiology-annotation).

## 5. Radiomics signature
- **Question:** do hand-crafted features predict the endpoint?
- **MVP:** IBSI-compliant features, segmentation reproducibility (ICC), feature selection
  **inside** training only, model + calibration, internal validation.
- **Stronger:** external validation, biological correlate (→ radiology-radiogenomics),
  comparison vs deep features or clinical model.
- **Guideline:** CLEAR (reporting) + METRICS/RQS (quality) + IBSI. (→ radiology-radiomics)

## 6. Radiogenomics / imaging-multi-omics
- **Question:** what biology underlies an imaging phenotype?
- **MVP:** matched imaging∩omics cohort (state the intersection n), FDR-controlled association,
  bounded interpretation.
- **Stronger:** independent validation cohort, multi-omics integration, single-cell/spatial
  linkage via habitats. (→ radiology-radiogenomics)
- **Guideline:** CLEAR/IBSI for imaging side; document omics accessions.

## 7. Reader / clinical-utility study
- **Question:** does AI change radiologist performance or workflow?
- **MVP:** MRMC design, washout, with/without AI, reader experience reported.
- **Stronger:** prospective, real-workflow, time and confidence outcomes, harm analysis.
- **Guideline:** CLAIM + reader-study stats (MRMC → radiology-stats); for the prospective/
  early-clinical-evaluation version add DECIDE-AI (early clinical evaluation, Nat Med 2022) /
  CONSORT-AI (if a randomised trial) — route via radiology-reporting. (→ radiology-translation)

## Blueprint output skeleton

```
Clinical question:
Target population / setting:
Primary endpoint (estimand):
Treatment estimand class: [not applicable / treatment-contextual prognosis / ATE / effect modification]
Comparator / baseline:
Design type: [1–7 above]
MVP version:        [what's publishable now]
Stronger version:   [what raises the tier] + extra cost
Unit of analysis:   patient / lesion / slice  (default: patient)
Validation:         [→ validation-strategy.md]
Reporting guideline:[→ radiology-reporting]
Binding constraint: [the one number everything hinges on]
```
