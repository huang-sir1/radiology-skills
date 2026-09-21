# Underpowered fallback — when the sample is not enough

Sample-size and EPV calculation lives in `radiology-stats/sample-size.md`; design locks live in
`radiology-design`. This file takes over when the calculation says **no**: events too few, EPV
below the pre-specified floor, or a matched cohort too small to support the planned claim.
Choose a downgrade branch, re-lock what changes, and downgrade the claims to match. Never run
confirmatory wording on an exploratory sample.

## Branches (in order of preference)

### 1. Shrink the feature load
- Restrict to a small, clinically-prior feature set; pre-filter within training folds only.
- Use dimension reduction or stability-filtered subsets
  (`radiology-annotation/reproducibility-qc.md`) instead of the full feature space.
- Effect: fewer parameters for the same events; the estimand is unchanged.

### 2. Change the estimator
- Penalised regression (ridge / lasso / elastic net); Firth-type correction when separation
  threatens with rare events.
- Drop deep learning and other high-capacity models — they are the first casualty of low EPV.
- Effect: same endpoint and cohort; validation design holds, claims shrink in strength.

### 3. Change the endpoint
- Composite, surrogate, or continuous endpoint carrying more information per patient.
- This **is** an estimand change: re-lock the protocol (stage-2 gate,
  `stage-gates-and-handoffs.md`), re-check the reporting stack and guideline routing
  (`radiology-reporting`), and record the deviation.

### 4. Change the design
- Add a public external-validation cohort
  (`radiology-data/ai-radiogenomics-public-resources.md`) — check patient overlap and role
  separation first.
- Reframe as a pilot / feasibility study, or extend accrual (more centers, longer window).
- Label the analysis **exploratory** everywhere — abstract, claims, passport.

### 5. Stop or redirect
- If no branch survives honest review, record a negative feasibility finding and redirect
  (grant reshaping: `radiology-grant`; new design: `radiology-design`). A stopped project with
  a clean record beats an underpowered paper.

## What to rewrite per branch

| Branch | `project_state.json` fields | `claim_register.csv` action | Mark stale |
|---|---|---|---|
| 1 Shrink features | `primary_model` (feature-space note) | soften strength wording | feature selection, model, figures |
| 2 Change estimator | `primary_model` | scope unchanged; strength softened | model, values, figures |
| 3 Change endpoint | `primary_endpoint_estimand`, `event_count`, `reporting_stack` | re-scope affected claims; new-endpoint claims stay `pending` until analysed | nearly everything downstream |
| 4 Change design | `cohorts`, `validation_design`, `event_count` | add the exploratory boundary; external claims `pending` until validated | analysis plan, figures, availability statement |
| 5 Stop/redirect | `current_stage`, `unresolved_items` | submission claims → `unsupported` or withdrawn | whole submission package |

- Every branch is a `decision_log.csv` entry with rationale and affected artifacts
  (`project-passport-and-registries.md`); its staleness rule applies in full.
- Re-run the stage-2 gate ("estimand and validation locked before modelling") after any branch
  that touches endpoint, cohort, or validation.

## Honesty checks

- Claims match the realised evidence, not the planned one: an exploratory sample carries
  exploratory wording in title, abstract, and discussion.
- Do not rescue power by relaxing leakage rules — train-only transforms, patient-level splits,
  and locked test sets are not negotiable.
- Simulation can teach the pipeline but cannot substitute for evidence
  (`simulation-and-teaching-data.md`).
- Record the EPV / events actually achieved in the passport; reviewers and
  `radiology-prereview` will ask.
