# Validation strategy — the spine of a generalisable imaging study

Validation type is what reviewers judge first. Decide it **before** modelling and describe it
honestly. Discrimination on the training distribution proves almost nothing.

## The validation ladder (weak → strong)

1. **Apparent (resubstitution)** — performance on training data. Not validation; never report alone.
2. **Internal cross-validation / bootstrap** — resampling within one cohort; corrects optimism
   but does **not** test transportability. Use **nested CV** if hyperparameters are tuned.
3. **Internal hold-out (split-sample)** — one random split; weak with small n; patient-level only.
4. **Temporal validation** — train on earlier period, test on later. Tests drift over time.
5. **Geographic / center-held-out validation** — leave whole center(s) out for test. Tests
   site/scanner transportability — the most common imaging failure mode.
6. **Fully external validation** — independent cohort, different institution(s), collected and
   labelled independently. The strongest single step short of prospective.
7. **Prospective validation** — applied to a future cohort under the intended workflow
   (→ radiology-translation). The closest to clinical truth.

## What honestly counts as "external"

- **External** = a cohort the model never saw, ideally from different site(s)/scanner(s)/period,
  with the **entire** pipeline (preprocessing, feature selection, harmonisation, thresholds)
  frozen from training.
- **Not external:** randomly mixing multi-center data then holding out a fold; tuning the
  threshold on the "external" set; re-fitting harmonisation including the external data.
- If the only option is internal, **say "internal validation"** — do not dress it as external.

## Multi-center design choices

| Strategy | What it shows | Watch-outs |
|---|---|---|
| Pooled training, center-held-out test | Transportability to an unseen site | Need ≥3 centers to be convincing; report per-center performance |
| Train one center, test others (fully external) | Strong external claim | Performance drop expected; report it, don't hide it |
| Temporal (same/multi center) | Robustness to drift | Define the cut date a priori |
| Federated learning | Privacy-preserving multi-center training | Heterogeneity, communication, harder reproducibility |
| Leave-one-center-out CV | Uses all centers as external in turn | Report the spread, not just the mean |

## Center / scanner / batch effects

- Radiomic and deep features carry strong scanner/protocol signal that mimics biology.
- **Harmonise** (e.g. ComBat / ComBat_seq) with **biological covariates preserved** and
  **fit on training only**; show the target association **survives** harmonisation.
- Report per-center distributions, scanner/vendor/slice-thickness/sequence differences, and
  center-stratified or center-adjusted results.
- Expect and **report** external performance drop; an honest drop beats a suspicious non-drop.

## Partition hygiene (applies to every level)

- Split at the **patient level** — never let a patient's slices/lesions/sequences/timepoints/
  phases span train and test.
- Fit preprocessing, feature selection, normalisation, imputation, harmonisation, and
  augmentation on **training only**.
- Never use the test set for model selection, threshold choice, or early stopping.

## Reporting sentence

*"Models were developed on centers A–C (patient-level 5-fold nested cross-validation, all
preprocessing and feature selection fit within training folds) and validated externally on
center D (n=…, different vendor and period), with the pipeline frozen; per-center performance
and ComBat-harmonised results are reported."*
