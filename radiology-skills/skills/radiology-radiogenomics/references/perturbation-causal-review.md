# Perturbation and causal-evidence review

Use this scope-aware module whenever measured genetic, pharmacologic, environmental or ex vivo
perturbation is an active modality, or when a mechanism-only or imaging–mechanism task targets a
causal claim. It applies in reviewer, mentor, protocol, analysis and validation work. Do not
introduce imaging, radiomics or sample-to-image requirements unless imaging is actually part of the
declared study scope; when imaging is active, layer this module under the cross-scale bridge rather
than replacing it. A perturbation changes the evidence state from observational to interventional,
but it does not make causality automatic.

## First-pass causal question

Write the proposed causal contrast before reviewing figures:

`assigned intervention -> verified target change -> downstream molecular or cellular response -> phenotype`

Record the experimental unit, assignment unit, analysis unit, intervention level, comparator,
dose or intensity, time point, endpoint and estimand. Then list at least one rival explanation:
off-target activity, delivery toxicity, selection, altered composition, batch, temporal mismatch or
regression to the mean.

Do not accept a causal verb when the paper shows only target-expression correlation, inferred
regulatory activity, ligand-receptor scores, pseudotime, deconvolution, virtual knockout or a
model-generated response. Those results can nominate a perturbation; they do not substitute for one.

## Non-negotiable review domains

### 1. Assignment and exchangeability

- State whether assignment was randomized, blocked, paired, matched, sequential or observational.
- Verify that the assignment unit is the unit used for inference. Cells, fields or wells nested in
  one donor are not independent biological replicates.
- Check allocation concealment and blinding where feasible, including endpoint reading and image or
  colony scoring.
- Report attrition, failed cultures, excluded wells, missing time points and post-assignment filtering
  by arm. Exclusion after seeing outcomes requires a prespecified rule or sensitivity analysis.
- For pooled screens, inspect guide assignment, multiplet handling, ambient guide calls and minimum
  cells per guide, donor and batch.
- For paired or repeated-measure designs, preserve donor, clone, organoid, animal, plate and time
  structure in the model.

**STOP:** causal inference is not defensible when treatment assignment is confounded with donor,
plate, batch, site or acquisition time and those factors cannot be separated.

### 2. Perturbation identity and efficiency

- Define the perturbation reagent, sequence or compound, delivery method, lot, concentration,
  exposure duration and washout.
- Measure editing, knockdown, overexpression or inhibition efficiency at the appropriate molecular
  level. Transcript change alone may not verify protein or activity change.
- Report efficiency distributions, not only a mean, when perturbation is heterogeneous.
- Distinguish attempted assignment, detected perturbation and effective perturbation; do not silently
  analyze only responder cells.
- For CRISPR screens, review guide representation, guide concordance, cutting or repression
  efficiency and target-essentiality effects.
- For pharmacology, distinguish nominal dose from intracellular exposure and verify compound
  stability when relevant.

**STOP:** a null phenotype is uninterpretable if target modulation was not demonstrated; a positive
phenotype is weak if effective perturbation status was inferred from the same endpoint being tested.

### 3. Off-target and delivery effects

- Use multiple independent guides, siRNAs, shRNAs or chemically distinct compounds where feasible.
- Show concordant direction across reagents and report reagent-level estimates rather than pooling
  away disagreement.
- Include delivery-only, vehicle and non-targeting controls appropriate to the intervention.
- Check toxicity, stress, innate immune activation, cell-cycle arrest and selection as alternative
  explanations.
- For gene editing, evaluate predicted high-risk off-target loci or use an orthogonal strategy when
  the claim is central.
- For drugs, review selectivity at the tested concentration and known polypharmacology.

**STOP:** one reagent with no orthogonal confirmation cannot uniquely attribute the phenotype to the
named target when plausible off-target or delivery effects remain.

### 4. Dose, intensity and time

- Justify dose range and time points biologically; a single convenient dose-time pair cannot establish
  ordering or specificity.
- Examine whether the response is monotonic, saturating, biphasic or toxic.
- Separate early target-proximal effects from late secondary adaptation and population selection.
- Align molecular, cellular and phenotypic measurements to the expected causal sequence.
- For reversible interventions, include washout or recovery when it distinguishes transient pathway
  modulation from irreversible damage.
- Report all prespecified dose-time comparisons and multiplicity handling.

**STOP:** temporal precedence is not established when the proposed mediator and phenotype are measured
only at one terminal time point.

### 5. Target engagement and pathway position

- Verify direct target engagement with an assay appropriate to the mechanism: occupancy, activity,
  phosphorylation, localization, protein abundance, editing genotype or another proximal readout.
- Distinguish target engagement from downstream pathway response and from the final phenotype.
- Test whether the mediator changes before the phenotype and whether its magnitude tracks the
  intervention.
- When claiming a pathway, include a prespecified proximal readout and avoid relying only on broad
  enrichment scores.
- For cell-state or composition outcomes, distinguish within-cell-state changes from selective loss or
  expansion of cell populations.

**STOP:** perturbing a nominal target without showing engagement supports an intervention effect, not
a target-specific mechanism.

### 6. Controls and comparators

At minimum, map each threat to a control:

| Threat | Required or preferred control | What it resolves |
|---|---|---|
| Natural drift | Concurrent untreated control | Time and handling effects |
| Solvent or carrier | Vehicle control | Delivery chemistry |
| Editing or transfection | Non-targeting or mock control | Procedure and innate-stress effects |
| Reagent-specific action | Independent reagent or orthogonal perturbation | Off-target concern |
| Baseline imbalance | Randomization, blocking or paired baseline | Exchangeability |
| Batch and plate | Balanced allocation and batch-aware model | Technical confounding |
| General toxicity | Viability, stress and proliferation readouts | Nonspecific damage |
| Endpoint subjectivity | Blinded scoring and reproducibility | Observer bias |

Positive controls demonstrate assay responsiveness but do not replace a matched negative control.
Historical controls are usually insufficient when culture, plate, reagent lot or acquisition can drift.

### 7. Rescue, reversal and epistasis

- Prefer a rescue that restores target function without being affected by the original perturbation,
  such as guide-resistant expression or downstream product replacement.
- Quantify whether rescue restores the proximal readout and phenotype, and report partial or failed
  rescue rather than converting it to a binary success.
- Include rescue-only controls to reveal overexpression or vehicle effects.
- Bidirectional perturbation strengthens specificity when biologically coherent but is not mandatory
  for every mechanism.
- Epistasis or mediator blocking can order components of a pathway; interaction claims require the
  corresponding factorial comparison, not separate significance tests.
- A rescue performed at a non-comparable dose or time does not close the causal chain.

**STOP:** rescue cannot repair absent assignment validity, absent target engagement or unresolved
reagent toxicity. It addresses specificity only within an otherwise interpretable experiment.

## Statistical and replication constraints

- Define biological replicates by independent donors, animals, clones, organoids or experimental
  preparations; label wells, cells, fields and reads as technical or nested observations.
- Use donor-aware, batch-aware or mixed models when observations are nested or repeated.
- Report effect sizes and uncertainty for the causal contrast, not p values alone.
- Prespecify primary perturbation, endpoint, time point and contrast; correct multiplicity across the
  actual family of screened targets, doses, times and endpoints.
- Show replicate-level distributions and direction consistency. A large number of cells cannot rescue
  one biological replicate.
- Replicate the central effect in an independent experiment, donor set, model system or orthogonal
  perturbation when the claim ceiling is causal.

## Single-cell and spatial perturbation add-ons

- Separate perturbation assignment uncertainty from expression measurement uncertainty.
- Report guide capture, cells per guide, donor coverage, multiplets, ambient signals and compositional
  changes.
- Use pseudobulk or hierarchical models at the donor or experimental-unit level for population claims.
- Do not treat cell-level differential expression as independent causal replication.
- In spatial assays, ensure intervention and control samples are balanced across slide, region and
  processing batch; account for neighborhood dependence.
- If only a model predicts post-perturbation states, label evidence as predicted and validate against
  held-out measured interventions, simple baselines and out-of-distribution conditions.

## Reviewer output

Return the audit in this order:

1. **Causal contrast and experimental unit.** Restate what was assigned and what was compared.
2. **Validated links.** Identify which links are directly measured: assignment, efficiency, target
   engagement, mediator, phenotype and rescue.
3. **P0/P1/P2 findings.** Keep severity separate from PASS/CONDITIONAL/STOP verdict.
4. **Competing explanations.** Name the strongest rival and the evidence that would distinguish it.
5. **Minimum repair.** Specify the smallest control, reanalysis or wording change needed.
6. **Claim ceiling.** Choose intervention effect, target-associated response, target-specific causal
   effect or ordered mechanism.
7. **Writing boundary.** Provide safe wording for Results and Discussion.

## Writing constraints

Use **intervention effect** when assignment is valid but target engagement or specificity is incomplete.
Use **target-associated perturbation response** when target modulation is shown but off-target concerns
remain. Use **target-specific causal effect** only when assignment, engagement, independent reagents or
orthogonal perturbation, appropriate controls and biological replication are adequate. Use an **ordered
mechanism** only when temporal or epistatic evidence supports the stated sequence.

Do not write “gene X drives phenotype Y” from differential expression after one reagent. Prefer:
“Perturbation of X altered Y under the tested dose and time; target engagement and orthogonal
confirmation support a target-specific effect.” State failed rescue, heterogeneous efficiency,
toxicity, missing time-order evidence and model-system limits in the same evidence chain rather than
hiding them in a generic limitations paragraph.
