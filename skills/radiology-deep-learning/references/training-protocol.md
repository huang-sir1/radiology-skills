# Training protocol — reproducible and leakage-free

Record enough that another lab could re-run it. Every data-dependent choice respects the patient
boundary.

## Pretraining strategy

| Strategy | When | Report |
|---|---|---|
| **From scratch** | Large datasets only | Why scratch was viable |
| **Transfer learning** | Default for small/medium imaging cohorts | Source weights, frozen vs fine-tuned layers |
| **Self-supervised pretraining** | Large unlabelled pool | Pretext task, pretraining data (must exclude the external test) |

## Data splitting (patient-level, always)

- Split by **patient**; verify no patient spans train/val/test.
- Small n → **nested cross-validation** (outer = performance, inner = tuning).
- Keep a truly held-out test (or external cohort) untouched until the end.

## Augmentation

- Spatial (flips/rotations/elastic), intensity (noise/bias-field for MRI), crops — clinically
  plausible only.
- Fit any augmentation statistics on training; **never** augment across the split or into test.

## Class imbalance

- Options: class-weighted loss, focal loss, balanced sampling, threshold adjustment.
- Do **not** oversample before splitting (leak); resample inside training folds.
- Report **real prevalence**; don't present a balanced-sampled metric as the clinical setting.

## Optimisation & selection

- Loss (CE/focal/Dice/Cox-PL), optimiser (AdamW/SGD), LR + schedule, batch size, epochs.
- **Checkpoint/early-stop on the validation set, never the test set.**
- Fix and report random **seeds**; report run-to-run variability if feasible.

## Hyperparameter search

- Grid/random/Bayesian — but **inside** nested CV or on a separate validation set.
- Report the search space and the selected values.

## Reproducibility bundle (share — CLAIM open science)

- Architecture + input size, augmentation, loss/optimizer/LR/batch/epochs, seeds, checkpoint
  rule, framework + versions, hardware. Code/weights where possible (→ radiology-data).

## Reporting sentence

*"Models were trained with patient-level 5-fold nested cross-validation; augmentation
(flips, rotations, intensity jitter) was applied within training folds only. Class imbalance was
addressed with focal loss; checkpoints were selected on the inner validation fold. Hyperparameters
(LR, weight decay) were tuned in the inner loop; seeds were fixed (code and weights provided)."*
