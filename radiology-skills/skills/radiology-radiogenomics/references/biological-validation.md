# Biological interpretation and validation by claim branch

Use this module for localization, concordance, mechanistic and causal claims in any scope. It does not
assume that imaging is present. Select validation because it tests a named uncertainty or competing
hypothesis, not because another assay would make the study look more sophisticated.

## 1. First classify the evidence

For each atomic claim, record independently:

- **Primary evidence state:** `measured`, `derived`, `estimated`, `associated`, `predicted` or `perturbed`.
- **Modality subtype:** assay/model and its spatial, temporal and biological resolution.
- **Claim-link status:** `direct`, `inferred` or `proposed` for the exact link under review.

Then state `study_scope`, independent unit, matched/usable n, condition/time and active versus external,
generated or proposed modalities. An assay can be measured while its cell-state label is estimated;
the fields must not be collapsed.

## 2. Competing-hypothesis requirement

Before choosing validation, write at least:

- `H1`: the favored biological explanation;
- `H2`: a serious alternative biological explanation;
- `H3`: a technical, batch, sampling, composition, registration or selection explanation.

For each hypothesis, name one observation that would support it and one that would weaken it. A new
assay is useful only if its expected outcomes differ across H1/H2/H3.

## 3. Requirements by claim branch

| Claim branch | Minimum support | Still not established |
|---|---|---|
| association | valid unit-level effect, multiplicity/confounder control and uncertainty | localization, direction or mechanism |
| localization-or-concordance | matched/registered objects, scale-aware null, uncertainty and patient/specimen replication | signaling, temporal order or causality |
| mechanistic | coherent chain plus evidence that discriminates the favored mechanism from serious alternatives | causal direction when all links remain observational |
| causal | identifiable intervention/contrast, assignment assumptions, target engagement, controls, temporal order and replicated phenotype | transport beyond the tested system, dose and context |

Prediction is a separate branch. A model that predicts a molecular label or perturbation response does
not validate its mechanism without independent evidence for the proposed link.

## 4. Scope-aware validation routes

### `imaging-only`

Imaging can support technical validity, reproducible phenotype, localization within the image and
prediction in a named domain. Imaging-only data ordinarily cannot identify a tissue, cellular or
molecular mechanism. If mechanism is desired, mark the biological assay as `proposed_validation`, state
the expected discriminating result and keep the current wording at imaging association/prediction.

### `mechanism-only`

Begin at the actual tissue, cell, molecular or perturbational object. Possible orthogonal checks include:

- bulk program with protein, targeted assay, composition-aware analysis or independent cohort;
- single-cell state with donor-level replication, protein/spatial localization or perturbation;
- spatial niche with alternative segmentation/radius/null, pathology/protein assay or perturbation;
- pathology phenotype with blinded scoring, orthogonal marker/panel, independent material or functional
  experiment;
- perturbation with assignment, efficiency, off-target, dose/time, target engagement, controls,
  biological replication and rescue/orthogonal perturbation.

Do not request scan, ROI, scanner or sample-to-image fields.

### `imaging-mechanism`

Open `radiomics-mechanism-bridge.md` and `sample-to-image-mapping.md`. Validate the weakest named link in:

`imaging acquisition/physics -> reproducible phenotype -> matched tissue architecture -> cell source/state -> molecular program -> functional evidence -> clinical meaning`.

Require patient–lesion–region/habitat–specimen–block–section–assay–time compatibility. If H&E, IHC,
multiplex IF or WSI is active, use `radiopathology-mechanism-validation.md` for preanalytics, blinded
reading, algorithm QC and patient-aware nested inference.

## 5. What common validations can and cannot do

| Validation | Can support | Cannot by itself establish |
|---|---|---|
| independent cohort | reproducibility/transport of frozen effect or model | mechanism or absence of hidden bias |
| protein/IHC/mIF | presence, abundance or localization of a named target/cell phenotype | signaling direction or target-specific causality |
| spatial assay | regional localization, neighborhood compatibility and sampling-aware concordance | communication or direction from proximity alone |
| external atlas | annotation/context and hypothesis nomination | target-cohort measurement or matched validation |
| longitudinal sampling | temporal ordering and dynamic consistency | causal effect without an identifiable contrast |
| perturbation | intervention effect in the tested system | target specificity without engagement/off-target controls; broad transport |
| rescue/orthogonal perturbation | target specificity and direction | repair of poor assignment or inadequate replication |
| generated/virtual layer | prioritization and counterfactual prediction | observed biology or experimental fact |

## 6. Perturbation/causal audit minimum

For any measured perturbation or causal claim, record:

`unit and assignment | intervention/guide/drug | multiplicity | efficiency/adherence | dose | duration/time | target engagement | off-target/toxicity | negative/positive/vehicle controls | biological replicates | primary phenotype | missing outcomes | rescue/orthogonal test`.

If these details are being reviewed rather than merely proposed, also load
`perturbation-causal-review.md`. A statistically significant condition contrast is not causal when
condition is confounded with batch, assignment is unknown or there is no independent biological
replication.

## 7. Verdict and rescue

| Verdict | Meaning |
|---|---|
| `PASS` | the exact claim meets its branch-specific design, evidence and uncertainty requirements |
| `CONDITIONAL` | a named sensitivity, scope restriction, wording downgrade or targeted validation is needed |
| `STOP` | the evidence type, identity, comparison, independence or intervention design cannot support the requested claim |

For `STOP`, return:

`blocked claim -> failed link/assumption -> strongest claim supported now -> smallest discriminating evidence -> permitted wording`.

Do not recommend a large multi-omic package when one targeted control, reanalysis or orthogonal assay
would answer the uncertainty.

## 8. Writing contract

### Methods

State the unit hierarchy, assay/perturbation provenance, mapping/registration when applicable,
preanalytics/QC, blinding, controls, model, uncertainty and validation independence.

### Results

Separate observation from interpretation:

1. measured/derived/estimated/predicted/perturbed result with effect and uncertainty;
2. claim-link status and competing explanations;
3. validation result and which hypothesis it changes;
4. residual uncertainty and claim verdict.

### Discussion

Use:

`bounded main finding -> H1/H2/H3 comparison -> what validation discriminated -> what remains unresolved -> next decisive test`.

Avoid “drives,” “causes,” “mechanism,” “surrogate,” “noninvasive biopsy,” “cell–cell communication”
or “treatment benefit” unless the corresponding branch requirements are satisfied. Prefer “associated
with,” “localized with,” “was concordant with,” “predicted,” or “supports the hypothesis that” as
appropriate.
