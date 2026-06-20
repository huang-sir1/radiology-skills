---
name: radiology-stats
description: "Plan, run, and report imaging biostatistics the way Radiology (RSNA) reviewers expect — diagnostic accuracy with CIs, ROC/AUC comparison (DeLong/bootstrap), reader agreement (Cohen/Fleiss kappa, ICC, Bland-Altman), multi-reader multi-case (MRMC) studies, calibration and decision-curve analysis, multiplicity control for high-dimensional radiomics/omics (Bonferroni vs FDR), survival/prognostic modelling, and sample-size/EPV planning. Use when the user mentions AUC, DeLong, sensitivity/specificity, kappa, ICC, MRMC, calibration, decision curve, p-value, FDR, multiple comparisons, sample size, C-index, or asks how to report a statistic for Radiology. Provides runnable Python/R and a results sentence; never fabricates numbers."
---

# Imaging Biostatistics for _Radiology_

Use this skill to choose the right test, run it correctly, and **report it the way
_Radiology_ wants** — estimates with 95% CIs, exact p-values, named tests, and multiplicity
handled. It covers the statistics that imaging-AI, radiomics, and reader studies live or die
on.

## Core stance

- **Estimate + uncertainty, not just p.** Every primary result gets a 95% CI. Report exact
  p-values (e.g. `P = .03`, not `P < .05`); use `P < .001` only below that floor.
- **The test must match the design.** Paired data → paired test (same patients/cases read by
  both methods); clustered data (multiple lesions per patient) → account for clustering;
  multiple readers → MRMC, not a naive average.
- **Discrimination is not enough for a clinical model.** Report **calibration** and
  **clinical utility (decision-curve)** alongside AUC.
- **Control multiplicity honestly.** Thousands of radiomic/omic features ⇒ FDR or stronger;
  pre-specify primary vs exploratory.
- **No fishing, no fabrication.** Pre-specify the primary analysis; never invent a number,
  a CI, or a p-value. If data are insufficient, say what is needed.
- **Reproducible.** Return runnable code (Python first; R where it is the field standard)
  with the software/version and the exact method for CIs.

## When to use

- Diagnostic accuracy: sensitivity/specificity/PPV/NPV/accuracy/likelihood ratios + CIs.
- Comparing models/readers/tests: **DeLong** or bootstrap for AUCs; McNemar for paired
  sensitivity/specificity.
- Reader studies: **kappa / weighted kappa / Fleiss / ICC / Bland-Altman**; **MRMC** design
  and analysis.
- Prediction models: ROC, **calibration** (slope/intercept, Brier), **decision-curve
  analysis**, threshold selection.
- Radiomics/omics: feature reproducibility (ICC), **multiple-testing** correction,
  cross-validation/nested CV, bootstrap optimism.
- Survival/prognosis: Kaplan-Meier + log-rank, **Cox**, **C-index**, time-dependent ROC,
  competing risks.
- Planning: **sample size** for accuracy / AUC; **EPV** and **Riley** minimum sample size
  for prediction models.

## When to open extra files

| File | Open when |
|---|---|
| [references/diagnostic-accuracy.md](references/diagnostic-accuracy.md) | Sensitivity/specificity/PPV/NPV/LR, the right CI method, paired comparison (McNemar) |
| [references/model-evaluation.md](references/model-evaluation.md) | ROC/AUC, DeLong vs bootstrap, thresholds, calibration, Brier, decision-curve analysis |
| [references/agreement-mrmc.md](references/agreement-mrmc.md) | Cohen/weighted/Fleiss kappa, ICC model choice, Bland-Altman, MRMC (Obuchowski-Rockette / DBM) |
| [references/high-dimensional-omics.md](references/high-dimensional-omics.md) | Multiple testing (Bonferroni/Holm/BH-FDR/q-values), CV/nested CV, leakage, optimism, harmonisation stats |
| [references/survival-prognostic.md](references/survival-prognostic.md) | Kaplan-Meier, Cox PH (+ assumptions), C-index, time-dependent AUC, competing risks |
| [references/sample-size.md](references/sample-size.md) | Sample-size for sensitivity/specificity/AUC; EPV; Riley minimum sample size for prediction models |

## Workflow

1. **Restate the design** — unit of analysis (patient/lesion/slice), paired vs unpaired,
   number of readers, prevalence, primary vs secondary endpoints.
2. **Pick the estimand and test** using the reference files. Name it explicitly.
3. **Choose the CI method** (e.g. Wilson/Clopper-Pearson for proportions; DeLong or
   bootstrap for AUC; bootstrap for derived metrics).
4. **Handle multiplicity** — declare the primary analysis; correct the rest (method + family).
5. **Run it** — provide runnable code; compute estimate + CI (+ exact p where a test applies).
6. **Write the result** — a _Radiology_-style sentence (estimate, CI, p, n) plus a Methods
   sentence (test, software/version, CI method, multiplicity).
7. **Sanity-check** — does the CI width match n? is the test paired if the data are? is
   calibration reported for a clinical model? are subgroups pre-specified?

## Reporting templates (fill from real output — never fabricate)

- Accuracy: *"Sensitivity was 0.87 (95% CI: 0.81, 0.92; 130/149) and specificity 0.79 (95%
  CI: 0.72, 0.85; 158/200)."*
- AUC comparison: *"The model's AUC (0.88; 95% CI: 0.84, 0.92) exceeded the radiologists'
  (0.81; 95% CI: 0.76, 0.86; difference 0.07; P = .004, DeLong)."*
- Agreement: *"Inter-reader agreement was substantial (ICC, 0.82; 95% CI: 0.75, 0.87;
  two-way random-effects, absolute agreement, single rater)."*
- Multiplicity: *"Of 1218 features, 47 differed after Benjamini-Hochberg control at FDR <
  0.05."*

## Output contract

1. **`Design read`** — unit, pairing, readers, prevalence, endpoints.
2. **`Recommended analysis`** — estimand, test, CI method, multiplicity plan.
3. **`Code`** — runnable Python (and/or R), with library versions noted.
4. **`Results sentence`** — _Radiology_-style, with placeholders only where the user must
   supply data.
5. **`Methods sentence`** — for the statistical-analysis paragraph.
6. **`Caveats`** — assumptions, when the test breaks, what the reviewer may ask.

## Integrity & handoffs

- Never invent numbers, CIs, or p-values; compute from supplied data or mark as needed.
- Reporting-guideline alignment of the statistics → `radiology-reporting`.
- Plotting the result (ROC, calibration, DCA, forest, KM) → `radiology-figure`.
- High-dimensional study design (leakage, batch effects in radiogenomics) →
  `radiology-radiogenomics`.
- This skill is statistical guidance, not a substitute for a qualified biostatistician on
  high-stakes or regulatory work.
