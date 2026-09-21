# Endpoints, estimands, and the clinical question

A study is the **question** it answers and the **decision** it informs. Fix these before any
modelling; they determine the design, the metric, and the reporting guideline.

## Build the question top-down

1. **Clinical question** — the decision a clinician faces (Is this malignant? Will it recur?
   Will this patient respond? Where is the lesion?).
2. **Target population / setting** — who, where in the pathway, what prevalence. Screening,
   diagnosis, staging, treatment selection, surveillance, or MDT support each imply different
   data and metrics.
3. **Primary endpoint / estimand** — the precise quantity estimated:
   - Diagnosis → sensitivity/specificity/AUC at a defined operating point.
   - Prognosis → time-to-event (HR, C-index, time-dependent AUC) or risk at a horizon.
   - Response under one specified treatment → treatment-contextual prognosis: risk of
     response/progression in that care context, not individual treatment benefit.
   - Treatment effect → a contrast between defined treatment strategies (e.g. ATE at a horizon).
   - Treatment selection / predictive biomarker → effect modification or an individualised
     treatment-effect estimand, with a treatment comparator and marker-by-treatment contrast.
   - Segmentation → Dice/HD vs reference.
4. **Comparator / baseline** — vs radiologist, vs established clinical model/score, vs prior
   imaging biomarker, or vs standard of care. A model with no comparator answers little.
5. **Clinical-use scenario** — what the output *does*: triage, rule-in/rule-out, risk
   stratification, treatment selection, or workflow assist. This fixes the threshold and the
   cost of false positives/negatives.

## Primary vs secondary

- Declare **one** primary endpoint and primary analysis. Everything else is secondary or
  exploratory and must be labelled so (multiplicity → radiology-stats).
- The primary endpoint should match the clinical-use scenario, not the metric that looks best.

## Map endpoint → metric → what else is mandatory

| Endpoint | Primary metric | Also required |
|---|---|---|
| Diagnostic test | Sens/Spec/AUC + CIs | Real prevalence, PPV/NPV at prevalence, operating point |
| Prediction/prognosis | C-index / time-dep AUC | **Calibration** + decision-curve; never discrimination alone |
| Treatment-contextual response prediction | Response/PFS by criteria | Specified treatment context, uniform ascertainment, explicit time zero, baseline+follow-up imaging |
| Average treatment effect | Risk/survival/mean contrast under defined strategies | Credible comparator, causal assumptions, aligned time zero, confounding/overlap/switching plan |
| Effect modification / predictive biomarker | Treatment-by-marker contrast or defined heterogeneous-effect estimand | Treatment variation/comparator, interaction scale, overlap, multiplicity and confirmation plan |
| Segmentation | Dice / HD95 | Reference-mask protocol, failure cases |
| Reader study | MRMC AUC / Δ | Washout, reader experience, with/without AI |

## Clinical-use scenario → threshold logic

- A **rule-out** tool prioritises sensitivity (minimise missed disease); a **rule-in** tool
  prioritises specificity. State which, and choose the threshold on the **training/derivation**
  data, never the test set.
- Tie the threshold to the **consequence**: what action follows a positive/negative, and what a
  false positive/negative costs the patient. (→ radiology-translation for net benefit.)

## Common framing errors to fix

- "We built a model with high AUC" stated as a clinical conclusion — AUC is not clinical utility.
- Endpoint chosen after seeing which one was significant.
- No comparator, so "better" is undefined.
- Screening claims from an enriched diagnostic cohort (spectrum/prevalence mismatch).
- Operating point and prevalence omitted, making sensitivity/specificity uninterpretable.
- Calling a marker “predictive of treatment benefit” from one treatment arm; that design estimates
  prognosis under the observed treatment, not a treatment contrast.
- Claiming effect modification because one within-arm association is significant and the other is
  not; test the between-treatment contrast on a pre-specified scale.

## Output snippet

```
Clinical question:
Population / pathway position / prevalence:
Primary endpoint (estimand):
Treatment estimand class: [not applicable / treatment-contextual prognosis / ATE / effect modification]
Comparator / baseline:
Clinical-use scenario → threshold logic:
Secondary / exploratory endpoints (labelled):
```
