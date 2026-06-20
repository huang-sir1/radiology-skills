# Deep-learning leakage & validity audit

The checklist CLAIM-literate reviewers apply. Pass/fail each with a fix; one failure can sink the
paper.

## Partition hygiene

- [ ] Split at the **patient level**; verified no patient spans train/val/test.
- [ ] Slices/lesions/sequences/phases/timepoints of one patient stay in one set.
- [ ] Test (or external) set untouched until final evaluation.

## Fit-on-training-only

- [ ] Normalisation/standardisation statistics from training only.
- [ ] Augmentation never crosses the split or enters test.
- [ ] Resampling/oversampling for imbalance done inside training folds.
- [ ] Any clinical-feature scaling/imputation fit on training.

## Tuning / selection hygiene

- [ ] Hyperparameters tuned via nested CV / separate validation, not test.
- [ ] Checkpoint / early stopping on validation, **not** test.
- [ ] Operating threshold chosen on training/derivation, not test.

## Input integrity

- [ ] No report-text leakage (label not visible in text input).
- [ ] No post-outcome clinical variables.
- [ ] Mask/ROI availability consistent with the intended inference workflow.
- [ ] Foundation/SSL pretraining data excludes the external test cohort.

## Evaluation honesty

- [ ] Real prevalence reported; balanced-sampling not passed off as clinical.
- [ ] Discrimination **+ calibration + utility** (and segmentation: Dice/HD + failure cases).
- [ ] CIs everywhere; external/temporal validation stated honestly.
- [ ] Fair, well-tuned **baseline** reported (not a strawman).
- [ ] Failure cases / error analysis included.

## Output

```
DL audit:
  Partition:       PASS / FAIL — [detail + fix]
  Fit-on-training: PASS / FAIL — [detail + fix]
  Tuning:          PASS / FAIL — [detail + fix]
  Input integrity: PASS / FAIL — [detail + fix]
  Evaluation:      PASS / FAIL — [detail + fix]
Overall: [Blocker(s) / Should-fix / Clean]
```

Hand statistics to `radiology-stats` and guideline mapping to `radiology-reporting`.
