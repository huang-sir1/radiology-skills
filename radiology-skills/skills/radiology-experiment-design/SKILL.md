---
name: radiology-experiment-design
description: "Design/audit tissue, cell, organoid, animal, perturbation and rescue validation; not physical SOP execution."
---

# Mechanism experiment design and review

Use this skill as an independent entry point for turning an imaging-mechanism hypothesis into a
feasible, falsifiable and auditable experimental programme. It can also review an existing plan or
result package and teach the author how to improve it. It does not claim that an experiment was run
and never substitutes generic advice for a laboratory's validated SOP.

## Core stance

- Start from a decision-bearing claim and at least one competing explanation, not from a preferred
  assay. Ask what observation would distinguish the explanations.
- Preserve an evidence ladder: observational alignment, orthogonal measurement, perturbation,
  target engagement, phenotype, rescue/reversal and replication are different evidential jobs.
- A perturbation-associated change supports a causal interpretation only to the extent justified by
  assignment, specificity, target engagement, toxicity control, temporal order and rescue or
  orthogonal replication. Avoid the phrase "proves the mechanism".
- Dose, exposure time, guide/construct, delivery, assay conditions and experimental model are
  **experimental-design factors**, not ordinary machine-learning hyperparameters. Never optimize
  them against a desired phenotype and then report the selected condition as confirmatory evidence.
- Distinguish biological replicates, technical replicates, fields, sections, wells, cells and repeated
  measurements. Inference follows the independently assigned biological or experimental unit.
- Be constructive. For every defect, give the criterion, minimum feasible repair, stronger option,
  resource consequence, closure evidence and the claim that survives without the repair.
- Label evidence as `PLANNED`, `AUTHOR_REPORTED`, `PARTLY_VERIFIED`, `VERIFIED` or
  `NOT_ASSESSABLE`. Never invent conditions, sample sizes, results, effect sizes or failures.

## Choose the entry mode

| Mode | Use when | Required emphasis |
|---|---|---|
| `plan` | no experiment has been run | hypothesis discrimination, model/assay choice, controls, dose-time logic, unit, feasibility, decision and stop rules |
| `audit` | a protocol, Methods, notebook, images or result files exist | provenance, assignment, controls, independence, deviations, missing evidence, reproducibility and atomic repairs |
| `mentor` | a learner asks what to do next | explain why each design choice matters; give minimum, stronger and resource-limited routes without inventing a local SOP |
| `interpret` | real experimental outputs are supplied | target engagement before phenotype, magnitude/uncertainty, concordance, discordance, failure modes and claim ceiling |
| `writing-handoff` | the design and results are fixed | auditable Title/Abstract/Methods/Results/Figure/Supplement placement, negative evidence, claim ceiling, source-data map and separate data/code/reagent availability jobs |

Also declare `system: tissue | cell-line | organoid | animal | mixed`, `intervention: none |
genetic | pharmacological | environmental | mixed`, and the affected Claim IDs.

## Minimal intake

Record what is supplied and mark the rest `AUTHOR_INPUT_NEEDED`:

1. biological question, proposed mechanism, affected imaging/molecular claim and at least one
   competing explanation;
2. human cohort or discovery evidence motivating the experiment, including whether it is merely
   correlational;
3. experimental system, biological source, authentication/status checks and relevance to the
   intended population;
4. intervention, delivery, candidate dose/exposure levels and timing, with rationale source;
5. primary target-engagement readout, primary phenotype, secondary readouts and measurement time;
6. positive, negative, vehicle/vector, sham, batch and rescue controls that are actually available;
7. independently assigned unit, planned biological replicates, technical structure, randomization,
   blinding, exclusions, attrition and stopping logic;
8. local biosafety/ethics approvals, equipment, tissue, staff, budget, calendar and validated SOP
   constraints;
9. supplied protocols, raw/processed outputs, laboratory records and exact artifact locations.

## Required workflow

1. Open [the mechanism experiment workflow](references/mechanism-experiment-workflow.md).
2. Convert the claim into a causal contrast: `proposed mechanism versus competing explanation ->
   discriminating intervention/measurement -> expected patterns -> failure interpretation`.
3. Select the weakest experimental system that can answer the question, then state its translation
   limit. Do not choose complexity for prestige.
4. Build the [assay and control matrix](references/assay-control-matrix.md). Separate target
   engagement, phenotype, toxicity/viability, specificity and technical validity readouts.
5. Declare the independent unit, allocation, blocking, randomization, blinding, replicate hierarchy,
   analysis population, exclusions, missingness/attrition and batch structure before outcomes.
6. Order evidence in time: characterize model -> establish exposure/delivery -> demonstrate target
   engagement -> measure phenotype -> test specificity/rescue -> replicate or translate.
7. Define dose and time as a scientific design problem. State rationale, permissible range and
   decision rule; never propose a universal concentration, duration or reagent recipe without a
   verified local/source protocol.
8. Create minimum, stronger and resource-limited routes. Each route must state the question it can
   answer, extra cost/time/tissue and resulting claim ceiling.
9. Apply the quality gates below. A fatal gate cannot be averaged away by attractive downstream
   results.
10. Use [the experiment plan](templates/mechanism-experiment-plan.md), local
    [assay capability profile](templates/local-assay-capability-profile.md), case-level
    [mechanism-validation experience registry](templates/local-mechanism-validation-experience-registry.md)
    and [failure/decision log](templates/failure-decision-log.md) when durable artifacts are useful.
    A local case may inspire a check, but never becomes a universal rule without external evidence.

## Quality gates

| Gate | Pass question | If unresolved |
|---|---|---|
| `E0 Claim` | Is there a falsifiable claim, competing explanation and discriminating observation? | stop assay shopping; rewrite the question |
| `E1 Model` | Does the system contain the target/process and represent the intended biology? | limit to feasibility or choose another model |
| `E2 Unit` | Is the independently assigned unit explicit and protected from pseudo-replication? | redesign allocation and inference |
| `E3 Intervention` | Are identity, delivery/exposure, timing, specificity and assignment auditable? | no causal interpretation |
| `E4 Engagement` | Is target engagement measured independently of the headline phenotype? | phenotype cannot be attributed to the target |
| `E5 Controls` | Do controls distinguish baseline, delivery/vehicle, off-target, batch, assay failure, toxicity and rescue? | state the unresolved alternative explanation |
| `E6 Analysis` | Are endpoint, analysis population, exclusions, multiplicity and uncertainty prespecified at the correct unit? | exploratory only; hand off inference design |
| `E7 Reproducibility` | Are independent repeats, batch transfer, deviations, raw evidence and failure logs available? | do not claim robust replication |
| `E8 Translation` | Does cross-model or human evidence support the intended scope, with discordance explained rather than hidden? | constrain translation and clinical language |

Return `PASS`, `CONDITIONAL` or `STOP` per gate and per claim. `STOP` is appropriate for absent
target identity, unusable experimental unit, missing intervention contrast, outcome-selected
conditions, or an ethics/biosafety barrier.

## Assay and system routing

| Route | Primary design job | Minimum discriminators |
|---|---|---|
| IHC / multiplex IF | localize and quantify cell/marker relationships in tissue | validated marker/assay controls, ROI sampling, scoring/blinding, section/block/patient hierarchy, batch control |
| tissue molecular assay | test abundance, activation or pathway state in matched tissue | tissue provenance, purity/composition, pre-analytics, reference/normalization, batch and patient-level unit |
| cell line | establish tractable perturbation-response logic | identity/contamination status, context relevance, multiple independent models where feasible, vehicle/vector and toxicity controls |
| organoid / ex vivo | preserve patient or tissue context while enabling intervention | donor-level unit, derivation/selection bias, passage/culture state, matched control and cross-donor replication |
| animal model | test system-level temporal or microenvironmental consequences | allocation unit, randomization/blinding, sex/age/model relevance, attrition, welfare endpoints and translation limit |
| genetic perturbation | test target-specific necessity or sufficiency | independent guides/constructs, non-targeting control, editing/knockdown and protein/function engagement, off-target strategy and rescue |
| pharmacological perturbation | test target/pathway modulation under exposure | vehicle, exposure and selectivity rationale, target engagement, toxicity, orthogonal agent or genetic triangulation |
| rescue / reversal | distinguish target-specific effect from perturbation artifact | rescue construct/agent validity, expression/exposure comparability, timing, baseline effect and blinded analysis |

## Scientific red lines

- Human imaging-omics association motivates experiments but is not biological validation by itself.
- Staining intensity, pathway score, ligand-receptor prediction or colocalization alone does not
  establish activity, directionality or causality.
- A single guide, inhibitor, cell line, donor, batch, section, animal or experiment cannot establish
  general mechanism. Repeated fields/wells/cells do not repair absent biological replication.
- Target engagement must precede attribution of phenotype. Toxicity, stress response, delivery
  artifact and batch must remain explicit competing explanations.
- Rescue is informative only when it addresses the same target/process and does not introduce a new
  uncontrolled exposure. A post hoc rescue chosen because it worked is exploratory.
- Do not convert exploratory dose/time screening into confirmatory evidence without a freeze and an
  independent evaluation.
- Do not prescribe a reagent concentration, animal dose, guide sequence, incubation time, sample
  size or stopping boundary as universally correct. Use source-backed and locally validated values.
- Do not provide clinical treatment advice. Human-subject, animal, genetic manipulation, hazardous
  material and biosafety decisions require the appropriate local review and trained personnel.

## Output contract

Return the shortest complete package needed, in this order:

1. `Scope and evidence boundary` — mode, system/intervention, Claim IDs, supplied evidence and
   what remains planned or unverifiable.
2. `Mechanism contrast` — proposed mechanism, competing explanations, causal graph in words,
   discriminating observations and current association/causal ceiling.
3. `Minimum / stronger / resource-limited routes` — question answered, controls, extra
   tissue/time/cost and resulting claim ceiling.
4. `Experiment matrix` — model, intervention, comparator, allocation unit, dose/time rationale,
   target-engagement readout, phenotype, toxicity/specificity readout and expected/falsifying pattern.
5. `Control and replicate matrix` — positive/negative/vehicle/vector/sham/batch/rescue controls,
   biological versus technical hierarchy, randomization and blinding.
6. `Feasibility and governance` — local capability status, tissue/reagent/equipment/staff, pilot
   dependencies, budget/calendar band, plus separate `human-subjects`, `animal-welfare` and
   `biosafety-biosecurity` applicability, local owners, approval evidence and stop conditions.
7. `Analysis handoff` — estimand/contrast, independent unit, repeated/batch hierarchy, primary
   endpoint, exclusions, multiplicity family and outputs needed by `radiology-stats`.
8. `Gate verdicts and atomic findings` — evidence anchor, criterion, severity, minimum repair,
   stronger option/cost, closure evidence and surviving claim.
9. `Writing placement` — Title/Abstract cannot exceed the verified claim ceiling; assign exact
   Methods, Results, figure/legend, Supplement and Limitations jobs plus separate Data Availability,
   Code Availability, Reagent/Model Availability and Source Data locations.
10. `Next decision` — the single decision-bearing next action plus `AUTHOR_INPUT_NEEDED` fields.

## Handoffs and non-ownership

- Human imaging-to-molecular hypothesis, cross-scale mapping and mechanism claim integration ->
  `radiology-radiogenomics`.
- Experimental-factor rationale, alternative methods, sensitivity, assay performance and robustness
  audit -> `radiology-method-evaluation`; it must not relabel dose/time as ML tuning.
- Sample-size calculation, mixed/hierarchical modelling, effect/interval estimation, multiplicity
  and inference -> `radiology-stats` after this skill fixes the unit and contrasts.
- Human participants/tissue -> IRB/ethics-equivalent; live animals -> IACUC/animal-ethics-equivalent;
  genetic manipulation, potentially infectious material and dual-use concerns -> IBC/biosafety-
  biosecurity-equivalent. Hand all three independent branches to `radiology-ethics` using its
  [research ethics governance matrix](../radiology-ethics/templates/research-ethics-governance-matrix.md).
  Approval in one branch does not authorize another;
  missing, expired, conflicting or out-of-scope local authority is a STOP condition, not a writing
  caveat.
- Draft manuscript text only after evidence states and claim ceiling are fixed ->
  `radiology-writing`.

Physical execution, reagent preparation, laboratory-specific safety procedures and instrument SOPs
remain with trained local staff. Review is read-only unless the user explicitly requests edits to
supplied planning or manuscript artifacts.
