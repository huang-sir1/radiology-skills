# radiology-stats

**Imaging biostatistics, done the way _Radiology_ reviewers expect.** Choose the right test,
run it correctly, and report estimates with 95% CIs, exact p-values, named tests, and proper
multiplicity control.

## What it does
- Diagnostic accuracy (sens/spec/PPV/NPV/LR) with correct CIs.
- AUC comparison (**DeLong**, bootstrap), paired McNemar.
- Reader agreement (**Cohen/weighted/Fleiss kappa, ICC, Bland-Altman**) and **MRMC** reader
  studies.
- Prediction-model evaluation: **calibration** (slope/intercept, Brier), **decision-curve
  analysis**, threshold selection.
- High-dimensional radiomics/omics: **multiple-testing** (Bonferroni/Holm/BH-FDR), nested
  CV, bootstrap optimism, leakage-aware statistics.
- Survival/prognosis: Kaplan-Meier, Cox, C-index, time-dependent ROC, competing risks.
- **Sample-size / EPV / Riley** planning.

## Reference files
```
references/
├── diagnostic-accuracy.md     sens/spec/PPV/NPV/LR, CI methods, McNemar
├── model-evaluation.md        ROC/AUC, DeLong vs bootstrap, calibration, Brier, DCA, thresholds
├── agreement-mrmc.md          kappa, ICC model choice, Bland-Altman, MRMC (OR/DBM)
├── high-dimensional-omics.md  multiplicity (FDR), CV/nested CV, optimism, harmonisation stats
├── survival-prognostic.md     KM, Cox + assumptions, C-index, time-dependent AUC, competing risks
└── sample-size.md             accuracy/AUC sample size, EPV, Riley minimum sample size
```

## Typical Python stack
`numpy scipy pandas scikit-learn statsmodels lifelines` (+ R: `pROC`, `irr`, `rms`,
`dcurves`, `RJafroc` for MRMC).

## Example prompts
- "Compare these two ROC curves on the same 300 cases (paired) and write the sentence."
- "Which ICC model do I report for 3 readers scoring continuous size?"
- "I have 1200 radiomic features and 90 patients — how do I handle multiplicity and overfitting?"
- "Design an MRMC reader study, 6 readers, AI-vs-no-AI."
- "Sample size to show sensitivity ≥ 0.90 at prevalence 0.15."

## Integrity
Never fabricates numbers, CIs, or p-values. Pre-specifies primary vs exploratory analyses.
Hands plotting to `radiology-figure` and guideline alignment to `radiology-reporting`. Not a
substitute for a biostatistician on regulatory-grade work.
