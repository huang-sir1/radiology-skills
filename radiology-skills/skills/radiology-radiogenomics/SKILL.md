---
name: radiology-radiogenomics
description: "Interpret mechanisms and imaging-mechanism bridges with competing explanations and causal ceilings."
---

# Imaging–Mechanism Research Router

Own the scientific meaning of standalone biological evidence and the validity of an explicit
imaging-to-mechanism bridge. Return the narrowest evidence-bounded interpretation, rival explanation,
claim ceiling or validation decision that answers the current mechanism question.

## Ownership gate before loading the manifest

First decide whether the current requested decision is actually a mechanism decision. If not, hand
off immediately without loading the radiogenomics manifest or playbooks:

| Clear isolated intent | Unique owner |
|---|---|
| pure radiomics configuration, extraction, modelling or leakage audit | `radiology-radiomics` |
| imaging deep-learning build/train/audit | `radiology-deep-learning` |
| real bulk/sc/snRNA/spatial workflow planning, code, execution or run audit | `radiology-transcriptomics-analysis` |
| functional wet-lab validation design | `radiology-experiment-design` |
| parameter provenance, metric fit, ablation or method comparison | `radiology-method-evaluation` |
| routine inference, uncertainty, multiplicity or sample-size calculation | `radiology-stats` |
| generic manuscript drafting/restructuring or language polish | `radiology-writing` or `radiology-polishing` |
| whole-manuscript imaging prereview | `radiology-prereview` |
| reviewer response, rebuttal or revision-letter closure | `radiology-response` |
| reporting checklist, journal choice or final upload package | `radiology-reporting`, `radiology-journal` or `radiology-submission` |
| unclear learner request or multi-stage academic coaching | `radiology-pipeline` |

A manuscript, reviewer letter or proposed assay does not make this skill the owner. Stay only when
the requested judgement concerns a biological mechanism, a causal boundary, competing biological
explanations, or the physical/evidentiary bridge between a named imaging object and biology.

## Owned scopes

- `mechanism-only` — interpret or audit measured/derived/estimated evidence from bulk RNA,
  single-cell, spatial, pathology, multi-omics or perturbation studies without inventing imaging.
- `imaging-mechanism` — connect a named imaging phenotype to a named biological object through an
  explicit patient–lesion–region–sample–time map and scale-compatible evidence.

Pure `imaging-only` work is not an owned scope. The manifest retains compatibility adapters only for
an explicit, already-bound scientific handoff; do not select this skill as its primary owner.

## Routing protocol

1. **Run the ownership gate.** If the request belongs to a unique specialist above, hand it off with
   the available scope, unit, evidence state, Claim IDs and exact source locators.
2. **Load the minimal router.** For an owned mechanism decision, read [manifest.yaml](manifest.yaml)
   and its single `always_load` file. Do not preload the other shared-core files.
3. **Resolve axes without optimistic defaults.** Determine interaction mode, tutor style, scope,
   immediate task, stage, modality roles, claim target, input evidence and audience. Keep an
   unresolved axis `unknown` or `provisional`; never silently convert an ambiguous learner prompt
   into `combined | mechanism-only | analysis-interpretation`. Ask at most two targeted questions
   only when the ambiguity changes the estimand, independent unit, evidence boundary or requested
   artifact. Otherwise state a bounded provisional branch and proceed.
4. **Load rules additively.** Apply only rules matching the resolved axes. Passport, integrity gates,
   claim ledger, mentor workflow and output presets are conditional core, not universal context.
   Load one full playbook only for a modality that is measured or is the actual design/audit target.
   An external atlas, generated layer, proposed future assay or casual mention does not trigger its
   full playbook.
5. **Work from validity to meaning.** Use
   `question/estimand -> provenance and matched n -> independent unit -> measurement/QC -> leakage,
   batch and multiplicity -> spatial/time/treatment mapping -> rival explanations -> validation ->
   claim ceiling` unless the user requests a narrower artifact.
6. **Return the smallest complete mechanism artifact.** Do not append generic manuscript, response,
   submission or project-management work. When prose or review is downstream, freeze the mechanism
   decision and hand it to the unique receiving owner.

If a durable request passport is useful and the user requests an artifact, use
[templates/research-request-passport.md](templates/research-request-passport.md). Advisory work keeps
the route and missing facts in the response; it does not create or update files.

## Tutor interaction

For direct invocation by a learner, use the conditionally loaded
`static/core/reader-and-mentor-workflow.md`:

- `direct-expert` gives the mechanism judgement, rationale, assumptions and next action.
- `guided-learning` records a baseline attempt, diagnoses at most two material misconceptions,
  teaches the smallest needed principle, elicits teach-back/retry, then uses one transfer case and
  records mastery evidence.

Preserve these learner fields across every handoff:

`interaction_style | learning_objective | target_decision | demonstrated_level | baseline_attempt |
misconception_ids | evidence_of_understanding | mastery_status | current_tutor_state |
next_transfer_task | support_preference | unresolved_learner_questions`.

Use `unknown` or `provisional` instead of inferring ability from degree, confidence or language.
Tutoring is read-only by default and does not authorize simulated data/results or filesystem edits.

## Scientific invariants

- The limiting sample size is the usable matched intersection for the intended claim, not the
  largest upstream cohort or number of cells, spots, ROIs, tiles or repeated measurements.
- Patient, lesion, region/habitat, specimen, block/section, cell/spot and time point are not
  interchangeable. Keep nesting and the biological independent unit explicit.
- Keep `measured`, `derived`, `estimated`, `associated`, `predicted` and `perturbed` separate. A
  feature name, saliency map, embedding, enrichment score or generated layer has no intrinsic
  mechanistic meaning.
- An imaging-to-mechanism claim requires the radiomics–mechanism bridge, at least two serious
  biological explanations, one technical/sampling/confounding explanation and discriminating
  evidence. Concordance between correlated or estimated layers is not independent validation.
- Outcome prediction under one observed regimen is prognostic or treatment-contextual prediction.
  An average treatment effect requires a valid treatment contrast and its identification assumptions;
  differential benefit/effect modification additionally requires a prespecified
  biomarker-by-treatment interaction and appropriate validation.
- Review findings use `P0 / P1 / P2`; individual claims use `PASS / CONDITIONAL / STOP`. Do not mix
  severity with scientific support.
- A `STOP` returns
  `blocked claim -> reason -> nearest answerable question -> minimum new evidence -> wording allowed
  now -> smallest next action`; it is not the end of mentoring.
- Reviewer requests are inputs to adjudicate, not automatic obligations. Do not let reviewer prose
  reverse a scientific verdict without new evidence or a corrected premise.
- Never invent cohort counts, accessions, approvals, analyses, p values, effects, citations,
  mechanisms, validations, manuscript locations or completed changes.

## Progressive-loading constraints

- `imaging-mechanism` loads the bridge and mapping contract. `mechanism-only` does not load them.
- Load the full bulk, single-cell, spatial, pathology, multi-omics or perturbation playbook only for
  an active measured/design/audit target. Use the compact linkage guide for an external atlas.
- Generated, mapped, deconvolved or predicted data remain labelled as generated even when they are
  the active audit target.
- A proposed validation assay remains proposed until the user chooses an executable design; do not
  load its full handbook merely because it sounds desirable.
- Search literature-map TSVs by PMID/topic/rule. Do not load whole tables into context.
- A mechanism claim embedded in a manuscript may load the scope-specific claim-review adapter, but
  generic whole-manuscript review remains with `radiology-prereview`; scientific prose remains with
  `radiology-writing`; reviewer correspondence remains with `radiology-response`.
- For composite work, freeze the current mechanism decision before loading or handing off a later
  writing, review or response stage.

## Handoff contract

For cross-skill writing/review/revision work, freeze the immutable scientific packet under
[references/scientific-handoff-contract.md](references/scientific-handoff-contract.md) before prose
or reviewer synthesis. The handoff states:

`producer | current mechanism decision | scope and modality roles | independent unit/hierarchy |
matched intersection | Claim IDs and maximum wording | evidence states and exact locators |
alternatives/falsifiers | unresolved assumptions | requested receiving artifact | learner fields when
applicable | acceptance/closure condition`.

Receiving modules may improve presentation or complete their own artifact, but they may not silently
upgrade an immutable evidence state or claim ceiling. Return changed scientific fields to this owner
for re-adjudication.

The radiology suite remains independently publishable, and the full workflow must remain usable
without external academic-writing or Nature-branded skill products.

## Boundary

Predictions are not experimental facts, orthogonal concordance is not causality, and a same-cohort
validation subset is not independent external validation. Computational assistance does not transfer
scientific ownership: production bioinformatics, clinical decisions, physical experiments and local
ethics/legal review remain with qualified collaborators and responsible investigators.
