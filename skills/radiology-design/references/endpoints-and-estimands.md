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
   - Response → response/progression by defined criteria.
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
| Treatment response | Response/PFS by criteria | Uniform outcome ascertainment, baseline+follow-up imaging |
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

## Output snippet

```
Clinical question:
Population / pathway position / prevalence:
Primary endpoint (estimand):
Comparator / baseline:
Clinical-use scenario → threshold logic:
Secondary / exploratory endpoints (labelled):
```
