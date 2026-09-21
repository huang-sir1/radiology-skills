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

*"Models were trained using patient-grouped split/resampling design and partition sizes
[AUTHOR_INPUT_NEEDED], with loss, optimiser, learning-rate schedule, batch size and stopping rule
[AUTHOR_INPUT_NEEDED]. Augmentation and imbalance methods and their data scope, or their absence,
were [AUTHOR_INPUT_NEEDED]; checkpoint criterion and selection partition were
[AUTHOR_INPUT_NEEDED]. Hyperparameters used fixed settings or a tuning procedure
[AUTHOR_INPUT_NEEDED]. Seed settings and number of runs were [AUTHOR_INPUT_NEEDED]."*

- Only if tuning was performed: *"The search space, search method and tuning partition were
  [AUTHOR_INPUT_NEEDED]."*
- Only if artifacts are shared: *"Code/weights and version [AUTHOR_INPUT_NEEDED] are available
  at verified location [AUTHOR_INPUT_NEEDED], under permission, licence and access conditions
  [AUTHOR_INPUT_NEEDED]."*

Populate only from executed configurations, split manifests and logs. Remove unperformed optional
branches; do not infer nested validation, augmentation, tuning, fixed seeds or completed sharing
from recommended practice. Unknown settings remain unverified. A sharing statement requires an
existing accessible artifact/location and permission for that release; intended sharing is not
completed sharing.
