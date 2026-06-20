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
- **Guideline:** STARD 2015 (+ CLAIM if AI); QUADAS-2 if part of a review.

## 2. Prediction / prognosis model
- **Question:** does an imaging-derived score predict an outcome (recurrence, survival, response)?
- **MVP:** patient-level split, model with discrimination **and calibration**, decision-curve
  analysis, internal validation (bootstrap/CV), EPV respected.
- **Stronger:** external/temporal validation, comparison vs established clinical model, net
  benefit across thresholds, subgroup stability.
- **Guideline:** TRIPOD+AI (2024) + PROBAST(-AI).

## 3. Treatment-response / longitudinal
- **Question:** does imaging (baseline or delta) predict response or progression?
- **MVP:** defined response criteria (e.g. RECIST / disease-specific), baseline+follow-up
  imaging registered, outcome ascertained uniformly.
- **Stronger:** delta-radiomics with reproducibility shown, multi-center, time-to-event modelling.
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
- **Guideline:** CLAIM + reader-study stats (MRMC → radiology-stats). (→ radiology-translation)

## Blueprint output skeleton

```
Clinical question:
Target population / setting:
Primary endpoint (estimand):
Comparator / baseline:
Design type: [1–7 above]
MVP version:        [what's publishable now]
Stronger version:   [what raises the tier] + extra cost
Unit of analysis:   patient / lesion / slice  (default: patient)
Validation:         [→ validation-strategy.md]
Reporting guideline:[→ radiology-reporting]
Binding constraint: [the one number everything hinges on]
```
