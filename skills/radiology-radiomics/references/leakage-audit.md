# Radiomics leakage audit

The checklist reviewers (and METRICS/RQS) use. Each item is pass/fail with a fix. One failure can
sink the paper.

## Partition hygiene

- [ ] Split made at the **patient level** (not slice/lesion).
- [ ] No patient's lesions/slices/sequences/phases/timepoints span train and test.
- [ ] Test set untouched until final evaluation (no peeking).

## Fit-on-training-only

- [ ] **Feature selection** done inside CV/training folds, not on the full cohort.
- [ ] **Normalisation / standardisation** fit on training, applied to test.
- [ ] **Missing-value imputation** fit on training.
- [ ] **Harmonisation (ComBat)** fit on training (biology preserved), applied to test.
- [ ] **Augmentation** never crosses the split.

## Tuning hygiene

- [ ] Hyperparameters tuned by **nested CV** / a separate validation set, not on test.
- [ ] **Threshold / operating point** chosen on training/derivation, not on test.
- [ ] No early stopping / model selection on the test set.

## Reproducibility / stability

- [ ] Non-reproducible (low-ICC) features removed before modelling.
- [ ] Discretisation (bin width/count) fixed and reported (IBSI).
- [ ] Software + version + parameter file recorded and shareable.

## Evaluation honesty

- [ ] Real prevalence reported (no silent 1:1 resampling claimed as the clinical setting).
- [ ] Discrimination **and** calibration **and** decision-curve for clinical models.
- [ ] CIs everywhere; external/temporal validation stated honestly.
- [ ] Selection stability / per-center results where relevant.

## Output

```
Leakage audit:
  Partition:        PASS / FAIL — [detail + fix]
  Fit-on-training:  PASS / FAIL — [detail + fix]
  Tuning:           PASS / FAIL — [detail + fix]
  Reproducibility:  PASS / FAIL — [detail + fix]
  Evaluation:       PASS / FAIL — [detail + fix]
Overall: [Blocker(s) / Should-fix / Clean]
```

Hand the statistical fixes to `radiology-stats` and the reporting-guideline mapping to
`radiology-reporting`.
