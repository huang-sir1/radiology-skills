# Feature selection, modelling & the signature/score

The single rule: **every data-dependent step is fit inside training only.** Selection on the
whole cohort is the most common radiomics leak.

## Selection pipeline (all inside CV / training folds)

1. **Reproducibility filter** — drop low-ICC features (from radiology-annotation), threshold
   pre-specified.
2. **Unsupervised pruning** — near-zero variance; collapse highly correlated features
   (e.g. |r| > 0.9 keep one).
3. **Supervised selection** — univariate screen (with multiplicity awareness), or embedded
   methods: **LASSO**, elastic net, **mRMR**, Boruta/RF importance.
4. **Dimensionality** — use the project-specific statistical brief for effective complexity,
   shrinkage, event/non-event information, precision, calibration and stability; do not use a
   universal feature:event ratio as an adequacy certificate (→ radiology-stats).

> Wrong: rank features by association on the full dataset, then cross-validate the chosen set.
> Right: re-run selection inside each training fold; report selection stability.

## Modelling

- Match the model and its effective degrees of freedom to the independent-unit information and
  intended estimand. Penalised regression, tree ensembles and SVMs are candidates—not a sample-size
  lookup table—and each needs a fair tuning/stability plan.
- Tune hyperparameters with **nested CV** (inner loop) — never on the test set.
- Pre-specify the **primary** model; others are exploratory.

## Comparison discipline (no model shopping)

- Define the **primary analysis** before protected-result access from the estimand, measurement
  properties, information/precision brief and scientific purpose. No selector/model combination is
  a universal default.
- Pre-register only scientifically justified alternatives. There is no universal permitted number;
  the comparison burden, multiplicity, compute and reporting plan must remain explicit, and all
  prespecified confirmatory alternatives are reported.
- **Do not select a selector × classifier combination and report its same-data validation score
  as a protected performance estimate.** With S
  selectors × M classifiers evaluated on the same validation data, the winning margin is
  partly luck, so the picked combination's validation estimate is optimistically biased —
  and the bias grows with the grid size. If many combinations must be compared, the grid is
  tuning: nest it (inner loop) or hold a final untouched test set.
- Report **selection stability** (per-feature selection frequency across folds/bootstraps) —
  an unstable winner is a red flag, not a result.

*"The primary selector/model pipeline was prespecified from the estimand, measurement-stability
evidence and statistical information brief. Any candidate grid was treated as inner-loop tuning;
the final protected evaluation was not used to select a combination. All prespecified confirmatory
alternatives and their uncertainty are reported."*

## Information and effective-complexity brief

Do not derive an allowed feature count from `events / 10` or another fixed EPV threshold. Before
locking the model, obtain a project-specific brief that records:

- estimand, outcome type, event/non-event counts and independent units by split/site;
- candidate degrees of freedom including nonlinearities/interactions and any selection/tuning;
- separation, shrinkage/penalisation, calibration precision and expected interval width;
- resampling/selection stability and optimism-correction plan;
- missingness, clustering, competing risks or censoring where applicable; and
- the simplification/downgrade rule if precision or stability is inadequate.

Selection inside resampling prevents a particular leakage path; it does not create information or
prove stability. If the prespecified model is not estimable or remains unstable, simplify, obtain
more independent information, change the estimand/design, or downgrade the claim transparently.

## Building a radiomics signature / score

- Combine selected features into a single score (e.g. LASSO linear predictor → "Rad-score").
- Optionally a **nomogram** combining Rad-score with clinical variables — report both the
  combined and component models.
- Report the formula/coefficients (supplement) for reproducibility.

## Validation & reporting (hand computation to radiology-stats)

- Internal: nested CV or bootstrap optimism correction.
- External/temporal/geographic: pipeline frozen.
- Match metrics to the task and estimand. For clinical probability models, report discrimination
  (outcome-appropriate AUC/C-index + CI), calibration (slope/intercept/curve), and overall prediction
  error (e.g. Brier). Use **decision-curve analysis only when** the intended action, comparator
  strategies, threshold range and error consequences are defined; otherwise omit it. Net benefit
  is decision-analytic evidence and does not establish observed clinical utility.
- Report selection stability and per-center performance where relevant.

## Reporting sentence

*"The development partition/resampling design was [AUTHOR_INPUT_NEEDED]. Preprocessing/pruning
steps, criteria and fitting partitions were [AUTHOR_INPUT_NEEDED]; the selection method or no
selection was [AUTHOR_INPUT_NEEDED], and the model was [AUTHOR_INPUT_NEEDED]. Evaluation used
design [AUTHOR_INPUT_NEEDED], with task-appropriate metrics and uncertainty methods
[AUTHOR_INPUT_NEEDED]."*

- Only if a signature was derived: *"The verified signature formula and coefficient location
  are [AUTHOR_INPUT_NEEDED]."*
- Only if the decision contract was defined and decision-curve analysis was performed:
  *"Decision-curve analysis evaluated net benefit under action and threshold assumptions
  [AUTHOR_INPUT_NEEDED], using methods [AUTHOR_INPUT_NEEDED]."*

Replace each placeholder only from the performed pipeline and outputs; omit inapplicable clauses.
The template supplies no default ICC/correlation threshold, selector, combined model, resampling
design or external validation claim. Describe fold-wise fitting only if that resampling procedure
was actually used; a recommended pipeline is not an executed one.
