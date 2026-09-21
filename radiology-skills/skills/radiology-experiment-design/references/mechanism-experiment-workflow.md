# Mechanism experiment workflow

This reference converts a mechanism claim into a falsifiable experiment programme. It is a design
and review framework, not a laboratory SOP. Values that depend on model, reagent, instrument,
facility or regulation remain `LOCAL_VALIDATION_REQUIRED` until supported by an exact source and
approved local practice.

## 1. Start with claim decomposition

Write the intended claim in operational form:

`In population/context P, process or target X contributes to phenotype Y through mediator M, and
the imaging feature or model output Z is associated with the relevant state.`

Then separate five propositions that often get collapsed:

1. **Presence/localization:** X or M exists in the relevant tissue/cell/compartment.
2. **Association:** X/M covaries with Y or Z at the correct independent unit.
3. **Temporal order:** the change in X/M occurs before the measured change in Y.
4. **Intervention response:** changing X/M changes Y under a controlled contrast.
5. **Specificity/mediation:** rescue, orthogonal perturbation or mediator analysis makes major
   alternatives less plausible.

An experiment should state which proposition it addresses. Evidence for one cannot be silently used
as evidence for all five.

## 2. Build a competing-explanation map

For every proposed mechanism, list plausible alternatives under these headings:

- composition: a change in cell/tissue mixture rather than within-cell biology;
- measurement: staining, segmentation, batch, sampling or normalization artifact;
- selection: model, ROI, dose, time or endpoint chosen after seeing the preferred result;
- common cause: disease burden, treatment, hypoxia, necrosis, inflammation or another exposure;
- intervention artifact: delivery, vehicle/vector, toxicity, stress or off-target effect;
- reverse direction or feedback;
- model-context mismatch: the experimental model lacks the human context represented by imaging.

For each alternative, specify one discriminating control or readout and the observation that would
leave it unresolved. Do not claim to have eliminated an alternative without a direct discriminator.

## 3. Fix the experimental unit and hierarchy

Document four levels separately:

| Level | Examples | Role |
|---|---|---|
| independently assigned unit | animal, donor-derived organoid line, independently treated culture | supports the intervention contrast |
| biological replicate | independent donor, passage-derived experiment, independent model | supports biological reproducibility, subject to design |
| technical replicate | repeated well, section, assay run or measurement | estimates measurement variability; not extra biological n |
| subsample/repeated measure | cells, fields, tiles, ROIs, spots, time points | preserves within-unit structure; must not be counted as independent n |

State allocation ratio, blocking factors, batch, nesting, repeated measurements and whether the same
unit contributes to multiple conditions. Analysis must preserve these dependencies.

## 4. Choose the experimental system by the question

Use the least complex system that retains the biology required by the claim:

- **Tissue observation** tests human relevance and localization but usually cannot establish
  directionality.
- **Cell lines** offer tractable perturbation but may lack patient heterogeneity and tissue context.
- **Organoids/ex vivo systems** may preserve donor context but introduce derivation, selection,
  culture and passage effects.
- **Animal models** add systemic and temporal context but require explicit species/model relevance
  and cannot be assumed to reproduce human disease.
- **Mixed triangulation** is strongest when different systems answer distinct propositions rather
  than repeat the same weak association.

Record why the chosen model is sufficient, what relevant feature it lacks, and which claim words
must therefore be avoided.

## 5. Order the evidence chain

Use this order unless the design supplies a documented reason to deviate:

1. authenticate and characterize the model;
2. verify delivery or exposure;
3. establish target engagement at the planned time and compartment;
4. measure the primary phenotype without outcome-dependent assay selection;
5. measure toxicity/viability and technical validity;
6. test specificity with independent guide/construct, orthogonal agent or another modality;
7. perform rescue/reversal where it distinguishes target-specific effect;
8. repeat independently and, where justified, test another model/donor/system;
9. reconnect the experimental effect to the human imaging/molecular observation without claiming
   the experimental model validated clinical performance.

If target engagement fails, downstream phenotype does not support the target mechanism even when it
is statistically unusual. If phenotype fails after engagement, report evidence against the proposed
effect under the tested context rather than repeatedly searching conditions for significance.

## 6. Design dose and time without outcome shopping

Treat dose and exposure time as design factors with four components:

1. **Rationale:** prior validated protocol, pharmacology/exposure evidence, pilot objective or local
   assay range; cite the exact source when available.
2. **Permissible region:** biological plausibility, solubility/delivery, viability, instrument range,
   ethics/welfare and resource constraints. Do not invent numeric bounds.
3. **Selection rule:** predefine which target-engagement, exposure and toxicity criteria select a
   condition. The desired phenotype cannot be the sole selection criterion.
4. **Freeze:** separate exploratory range finding from locked confirmatory evaluation and retain all
   screened conditions and failures.

Time-course design should distinguish exposure/engagement, early molecular response, phenotype and
late stress/toxicity. The order is a biological hypothesis, not merely a plotting preference.

## 7. Assign controls to failure modes

Do not add controls decoratively. Each control must rule in/out a specific explanation:

- untreated/baseline: natural drift and handling;
- vehicle/vector/mock/sham: delivery or procedure effect;
- non-targeting/isotype/secondary-only/knockout tissue: assay and non-specific signal;
- positive control: assay responsiveness, not proof that the study condition worked;
- batch/plate/section controls: technical drift and comparability;
- viability/toxicity/stress: non-specific loss or stress response;
- independent guide/construct or orthogonal agent: specificity;
- rescue/reversal: target-specific attribution, subject to rescue validity;
- model/donor replication: context robustness;
- negative biological endpoint or irrelevant target: general response and claim specificity.

Use `references/assay-control-matrix.md` for modality-specific checks.

## 8. Prespecify analysis and decision rules

Before observing the headline outcome, define:

- primary contrast and estimand;
- primary target-engagement and phenotype endpoints;
- independently assigned unit and analysis population;
- transformation/normalization and aggregation from fields/cells/wells to unit;
- batch, blocking, repeated-measure and paired structures;
- exclusions and quality failures defined independently of the desired outcome;
- multiplicity family for doses, times, endpoints, models and subgroups;
- uncertainty reporting and handling of non-detects/missingness;
- success, inconclusive, stop and redesign outcomes.

Hand computations and model selection to `radiology-stats`. Do not infer sample size from a fixed
universal replicate count; it depends on estimand, variability, hierarchy, effect worth detecting,
error control, attrition and feasibility.

## 9. Create three decision routes

### Minimum decision-bearing route

The smallest design that can distinguish the main mechanism from the most dangerous alternative.
It requires a valid unit, intervention contrast, target engagement, primary phenotype, core
delivery/vehicle and toxicity controls, locked analysis and honest claim limit.

### Stronger causal-triangulation route

Add only elements that close a named alternative: independent perturbation, rescue, orthogonal
readout, multiple models/donors, temporal ordering, cross-system confirmation or blinded replication.
State the additional resource and which claim upgrade it supports.

### Resource-limited route

When tissue, time, cost, equipment or expertise is binding, preserve design validity before breadth.
Reduce secondary endpoints, conditions or mechanistic depth; do not remove the valid comparator,
target-engagement evidence or independent unit and then retain a causal claim.

## 10. Feasibility and local capability

Use `templates/local-assay-capability-profile.md`. Classify every dependency:

- `AVAILABLE_AND_VALIDATED`
- `AVAILABLE_NEEDS_PILOT`
- `EXTERNAL_COLLABORATION_REQUIRED`
- `NOT_AVAILABLE`
- `UNKNOWN_AUTHOR_INPUT_NEEDED`

Capture tissue availability, model access, reagent lead time, instrument, trained operator, data
capture, analysis support, approvals, budget band and calendar. Do not write a detailed local SOP in
the profile; link the controlled SOP identifier, version and owner.

Route governance as three independent applicability decisions: `human-subjects` (IRB/ethics
equivalent), `animal-welfare` (IACUC/animal ethics equivalent) and `biosafety-biosecurity`
(IBC/biosafety equivalent, including designated dual-use review where applicable). A gene-modified
animal or human-derived potentially infectious material may require multiple branches. Use the
`radiology-ethics` governance matrix; do not start covered work while any applicable current local
approval, owner, facility/training dependency or approved scope is unresolved. Do not use this
workflow to assign containment or generate a hazardous SOP.

## 11. Failure is a scientific output

Use `templates/failure-decision-log.md` for failed engagement, toxicity, inconsistent batches,
discordant assays, attrition and null phenotype. A defensible response records:

`failure signal -> evidence -> plausible causes -> discriminator -> predeclared decision -> action ->
claim consequence`.

Do not quietly discard failed conditions, donors or experiments. Distinguish assay failure,
intervention failure, model-context limitation and evidence against the hypothesis.

## 12. Interpretation and claim ceiling

Use the strongest row satisfied, not the most ambitious intended design:

| Evidence achieved | Defensible language |
|---|---|
| tissue/imaging association only | "associated with", "consistent with", "motivates" |
| orthogonal measurement with correct unit | "supported across measurements"; direction remains uncertain |
| controlled perturbation + engagement + phenotype | "modulating X altered Y in this model/context" |
| specificity/rescue or orthogonal perturbation | "supports a target-linked contribution in the tested context" |
| replicated cross-model/temporal/human triangulation | stronger mechanistic support, still bounded by models and translation |

Avoid "proves", "drives human disease", "clinical mechanism" or treatment claims unless the full
relevant evidence chain and intended-use evidence independently support them.

## 13. Writing handoff

The writing package must preserve provenance and negative evidence:

- **Title/Abstract:** state only the strongest evidence level actually satisfied; neither location may
  upgrade association or a context-specific perturbation into a proven human causal mechanism.
- **Methods:** model provenance/authentication, allocation, intervention and rationale, target
  engagement, controls, unit/replicate hierarchy, randomization/blinding, endpoints, exclusions,
  analysis, approvals and deviations.
- **Results:** denominators, target engagement before phenotype, effect and uncertainty at the correct
  unit, all prespecified contrasts, failures/attrition, rescue/orthogonal results and discordance.
- **Figures/legends:** representative image selection rule, scale, biological n versus fields/wells,
  exact tests/intervals, batch/repeat structure and unedited/source-data locations.
- **Supplement/source data:** complete conditions, validation evidence, raw-to-summary mapping,
  reagent/model identifiers, protocol references, deviations and failure log.
- **Discussion/limitations:** model relevance, unresolved alternatives, null/discordant results,
  translation boundary and experiments not yet run.
- **Data Availability:** identify raw/processed experimental data, repository/accession or controlled
  access and the participant/animal/biosafety governance that constrains sharing.
- **Code Availability:** identify analysis code, versioned environment and stable locator, or state the
  evidence-supported restriction without a vague promise.
- **Reagent/Model Availability:** provide identifiers, source and truthful access/transfer conditions;
  do not promise a reagent, construct, cell line, organoid or animal model that is not available.
- **Source Data:** map each figure/table to unit-level values and original assay/image records at their
  verified locator; representative panels do not replace source data.

Writing cannot turn `PLANNED` or `AUTHOR_REPORTED` work into verified evidence.
