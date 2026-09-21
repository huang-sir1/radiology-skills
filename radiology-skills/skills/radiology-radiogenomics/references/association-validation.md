# Association, enrichment, prediction, and validation

Use this module across all study scopes. Start from `claim_target`; association, localization,
prediction, treatment effect, mechanism and causality are different claim branches, not successive
rungs of one ladder.

## 1. Define the atomic claim

Write the claim as:

`independent unit | index/exposure | outcome | condition/time | effect or performance measure | validation domain`

Then record three independent evidence fields:

1. **Primary evidence state:** `measured`, `derived`, `estimated`, `associated`, `predicted` or `perturbed`.
2. **Modality subtype:** the actual assay/model source and resolution.
3. **Claim-link status:** `direct`, `inferred` or `proposed` relative to this atomic claim.

An estimated cell fraction can be measured as an output file yet remain an `estimated` biological
quantity. A replicated association remains an association. A predicted response is not a perturbation.

## 2. Descriptive and association analyses

- Choose the effect measure and model for the variable types, unit hierarchy and sampling design.
- Report effect size and CI, not p value alone.
- Define and correct the full multiplicity family for feature, gene, pathway, cell-state, niche,
  region or interaction scans.
- Model patient/donor clustering; cells, spots, tiles, sections, aliquots and repeated lesions are
  not automatically independent replicates.
- Predefine confounders and nuisance variables. Test whether site, scanner, assay batch, tissue
  composition, purity, library depth, segmentation, region selection or disease subtype explains the
  apparent signal.
- Replication requires a frozen direction/contrast and comparable effect estimate in an independent
  cohort/system; a second p value in a reused or overlapping cohort is not independent validation.

For `imaging-mechanism`, associate the imaging phenotype only with the molecular/pathology sample that
is compatible at patient, lesion, region and time. For `mechanism-only`, use specimen/assay provenance
and do not request imaging fields.

## 3. Gene-set and program interpretation

- State the gene-set collection and version, universe/background, ranking metric, method, direction,
  enrichment/effect measure and adjusted significance.
- Separate over-representation, ranked enrichment and per-sample scores; they answer different questions.
- Check whether the result is driven by a few genes, cell-composition shifts, gene-set overlap, broad
  stress/proliferation programs or batch.
- Pathway scores and regulons are `derived` or `estimated`; enrichment is not pathway activation and
  does not establish direction.
- Use held-out or orthogonal evidence for a named program, not a post-hoc collection of only favorable
  gene sets.

## 4. Localization and concordance

Claims about co-localization, spatial compatibility or cross-modal concordance require:

- an explicit coordinate/registration or region-matching rule;
- the resolution and uncertainty of each layer;
- a null model preserving relevant density/geometry or sampling structure;
- sensitivity to segmentation, region definition, radius/kernel and section choice;
- patient/specimen-level replication rather than spot/cell pseudo-replication.

Co-location does not prove interaction, signaling direction, temporal sequence or causality. In
`imaging-mechanism`, add the sample-to-image bridge. In standalone spatial/pathology work, stop at the
specimen–section–region chain.

## 5. Prediction

When the output is an individual-unit score or label:

- define intended use, prediction time, target, deployment domain and simple baselines;
- prevent leakage by learning selection, normalization, harmonization, imputation, thresholds and
  hyperparameters inside training data;
- split at patient/donor/site/time or the named unseen perturbation/context level;
- report discrimination/error, calibration, CI and utility where relevant;
- freeze the model and test the claimed external domain;
- compare complex models with simple clinical, linear, mean/control and nearest-neighbor baselines as
  appropriate.

Prediction performance does not validate the model's saliency, pathway story or causal mechanism.

## 6. Treatment effect and causal contrasts

- Prognostic association is not differential treatment benefit.
- Effect modification requires an appropriate comparator and prespecified exposure/biomarker-by-
  treatment interaction with absolute effects and uncertainty.
- Observational causal claims require a defensible causal contrast and explicit exchangeability,
  positivity, consistency and measurement assumptions.
- Experimental perturbation claims require assignment, efficiency/adherence, off-target assessment,
  dose/time, target engagement, controls, independent biological replication and a phenotype matched
  to the claim. Rescue/orthogonal perturbation strengthens target specificity.
- Bound causal wording to the tested system, intervention, dose, time and outcome.

## 7. Validation purpose matrix

| Validation type | Can support | Cannot repair |
|---|---|---|
| independent cohort/system | reproducibility and transport of a frozen association/model | leakage or a changed estimand |
| orthogonal assay | concordance of a named biological object | direction or causality by itself |
| spatial/pathology evidence | localization or tissue/cell-source plausibility | whole-organ generalization from one region |
| perturbation/rescue | intervention effect and target-specific direction in the tested model | poor assignment, no replication or broad transport |
| internal resampling | optimism/uncertainty under the same data-generating process | external validity |
| external atlas | annotation/context or hypothesis nomination | patient-matched validation unless the samples truly overlap by design |

## 8. Claim verdict

| Verdict | Use when |
|---|---|
| `PASS` | the specified claim branch meets its unit, design, analysis, uncertainty and validation requirements |
| `CONDITIONAL` | the result is usable only after a named sensitivity, scope reduction or wording downgrade |
| `STOP` | identity, independence, leakage, confounding, comparison or evidence type makes the requested claim unsupported |

For a `STOP`, give the nearest valid claim and the smallest discriminating analysis or experiment.

## 9. Writing contract

### Methods

State the independent unit, hierarchy, model, covariates, test family, correction, missing-data method,
preprocessing boundary, validation independence, software/version and all scope-specific mapping.

### Results

Report denominator, effect/performance with CI, multiplicity result, validation status and sensitivity
direction. Keep measured/derived/estimated/predicted/perturbed quantities linguistically distinct.

### Discussion

Use this order:

`main bounded finding -> strongest competing explanation -> validation and failure tests -> scope/transport limits -> next discriminating evidence`.

Avoid “drives,” “causes,” “mechanism,” “surrogate,” “noninvasive biopsy” or “treatment benefit” unless
the corresponding branch requirements are met. Prefer “associated with,” “localized with,” “was
concordant with,” “predicted in the stated domain,” or “supports the hypothesis that” when appropriate.
