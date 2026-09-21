# Validation strategy — the spine of a generalisable imaging study

Validation type is what reviewers judge first. Decide it **before** modelling and describe it
honestly. Discrimination on the training distribution proves almost nothing.

## Complementary validation dimensions

No universal weak-to-strong ladder applies across all questions. Each design answers a different
contrast; prospective collection is not automatically an impact study, and an external cohort is
not automatically representative. Combine the dimensions required by the intended claim.

1. **Apparent (resubstitution)** — performance on training data. Not validation; never report alone.
2. **Internal cross-validation / bootstrap** — resampling within one cohort; estimates/corrects optimism
   but does **not** test transportability. Use **nested CV** if hyperparameters are tuned.
3. **Internal hold-out (split-sample)** — one random split; weak with small n; patient-level only.
4. **Temporal validation** — train on earlier period, test on later. Tests drift over time.
5. **Geographic / center-held-out validation** — leave whole center(s) out for test. Tests
   site/scanner transportability — the most common imaging failure mode.
6. **External cohort validation** — independent cohort with a named population, setting, time,
   measurement/reference-standard process and frozen analysis. Tests only the represented transport
   contrast; “different institution” alone does not guarantee independence or relevance.
7. **Prospective validation** — applied to a future cohort under the intended workflow
   (→ radiology-translation). Prospective silent evaluation can test temporal/operational transport,
   but only an active impact design observes human interaction, workflow or patient consequences.

## What honestly counts as "external"

- **External** = a cohort the model never saw, ideally from different site(s)/scanner(s)/period,
  with the executable derivation pipeline (preprocessing, feature selection, thresholds, and only
  harmonisation methods that support the encountered batch levels) frozen before evaluation.
- **Not external:** randomly mixing multi-center data then holding out a fold; tuning the
  threshold on the "external" set; re-fitting harmonisation including the external data.
- If the only option is internal, **say "internal validation"** — do not dress it as external.

## Multi-center design choices

| Strategy | What it shows | Watch-outs |
|---|---|---|
| Pooled training, center-held-out test | Transportability to an unseen site | Center count alone does not establish information; report center-level support and per-center performance |
| Train one center, test others (fully external) | Strong external claim | Performance drop expected; report it, don't hide it |
| Temporal (same/multi center) | Robustness to drift | Define the cut date a priori |
| Federated learning | Privacy-preserving multi-center training | Heterogeneity, communication, harder reproducibility |
| Leave-one-center-out CV | Uses all centers as external in turn | Report the spread, not just the mean |

## Center / scanner / batch effects

- Radiomic and deep features carry strong scanner/protocol signal that mimics biology.
- If harmonisation is justified, fit it without outcome/test leakage and state whether validation
  samples belong to **batch levels represented during fitting**. A frozen ComBat transform may be
  usable for represented levels only when the implementation supports it; ordinary/transductive
  ComBat cannot be assumed to transform a wholly unseen external site because that site's batch
  parameters do not exist.
- For a wholly unseen site, make the untouched raw-scale evaluation primary or pre-specify an
  inductive/reference harmoniser validated for unseen batches. Re-estimating parameters using the
  external cohort is adaptation/transductive analysis, not a fully untouched external validation;
  report it separately. (`ComBat_seq` assumes an RNA-seq count model and is not for continuous
  radiomic/deep features.)
- Report per-center distributions, scanner/vendor/slice-thickness/sequence differences, and
  center-stratified or center-adjusted results.
- Expect and **report** external performance drop; an honest drop beats a suspicious non-drop.

## Investigating external performance decay

A drop on external validation is expected; the response is a diagnosis, not a panic. Work
the steps in order:

Treat each pattern as a hypothesis, not a diagnosis. Calibration intercept/slope and discrimination
can change because of case mix/prevalence, selection, measurement/reference-standard differences,
protocol/scanner shift, treatment/workflow changes, model misspecification or development
overfitting. Use the following investigation matrix:

1. **Calibration change:** quantify intercept/slope/curve and inspect outcome prevalence, case mix,
   label/reference-standard and time/workflow differences. An intercept update may be evaluated for
   a target population, but the pattern alone does not identify prevalence shift.
2. **Site/protocol pattern:** report per-center/vendor/sequence support and performance; test
   measurement and protocol hypotheses. Harmonisation is a prespecified sensitivity/adaptation
   method, not proof that protocol shift caused the decay.
3. **Discrimination and calibration deterioration:** evaluate optimism, effective complexity,
   leakage, spectrum, measurement and label shift. If redevelopment is justified, return to the
   development state and seek a new protected evaluation; do not patch on the external set and keep
   calling it independent validation.
4. **If nothing fixes it:** report honestly and downgrade the claim — generalisation failure
   is itself a publishable finding (→ `weak-result-pivot.md`).

Red lines:

- Report the **frozen-model result first**, exactly as applied. Any recalibrated or updated
  result is secondary and labelled as such — never report only the repaired numbers.
- Recalibrating on the external set **consumes its independence**: the updated model no
  longer has external validation on that cohort. Say so, or find a new cohort.

*"Applied frozen, the model's AUC fell from 0.8x (internal) to 0.7x (external) with
calibration intercept −0.x; after intercept-only recalibration, calibration-in-the-large was
0.0x while discrimination was unchanged. Frozen results are primary; the recalibrated model
awaits a further independent cohort."* (Template — fill from real output.)

## Center-level information, not a center-count licence

There is no universal number of centers that licenses external generalization, leave-one-center-out
inference, random effects or meta-analytic pooling. Record the target transport contrast, eligible
and analyzed patients/events by center, within-center class/outcome support, scanner/protocol and
reference-standard heterogeneity, center–outcome confounding, missingness and the number/information
of independent center units. Let the estimand/model and interval precision determine what can be
estimated.

Practical boundaries:

- **ComBat and alternatives need estimable, appropriate batch structure.** Per-center z-scoring or
  scanner covariate adjustment is not a universal small-center repair; either may erase biological
  signal, be unidentified under confounding or fail on an unseen site. Pre-specify the method,
  validate signal/measurement preservation and report raw-scale results/sensitivity.
- **Center confounded with outcome** (one center supplies nearly all positives): batch and
  biology cannot be separated — do **not** ComBat; stratify or adjust and bound the claim.
- With few centers, per-center performance and the LOCO spread beat any pooled "external"
  claim.

## Partition hygiene (applies to every level)

- Split at the **patient level** — never let a patient's slices/lesions/sequences/timepoints/
  phases span train and test.
- Fit preprocessing, feature selection, normalisation, imputation, compatible harmonisation, and
  augmentation on **training only**. This prevents leakage but does not make a transductive
  harmoniser capable of handling an unseen batch.
- Never use the test set for model selection, threshold choice, or early stopping.

## Reporting sentence

*"Models were developed on centers A–C (patient-level nested cross-validation, all
data-dependent preprocessing and feature selection fit within training folds) and evaluated on
previously unseen center D with the derivation pipeline frozen. Because center D was a new batch
level, raw-scale external performance was primary. [If performed: a pre-specified adaptation or
unseen-batch harmonisation analysis was labelled separately, with its external-data use and
remaining assumptions reported.]"*
