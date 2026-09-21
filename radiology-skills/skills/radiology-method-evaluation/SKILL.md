---
name: radiology-method-evaluation
description: "Audit parameter provenance, metric fit, fair comparisons and robustness; not execution or paper review."
---

# Parameter and methodology evaluation

Use this skill to decide whether a parameter choice, evaluation metric, or analytical method is
scientifically defensible and whether the available evaluation is sufficient for the stated claim.
It is an independent entry point and a cross-cutting reviewer/mentor module, not a sub-skill of
statistics, radiogenomics, writing, or prereview.

## Core stance

- Treat **parameters/settings**, **evaluation metrics/readouts**, and **methodology** as three
  separate objects. Do not hide one behind another.
- Use exact evidence anchors. Report whether evidence is `PLANNED`, `AUTHOR_REPORTED`,
  `PARTLY_VERIFIED`, `VERIFIED`, or `NOT_ASSESSABLE`.
- Return `PASS`, `CONDITIONAL`, or `STOP` per decision-bearing object and claim. Do not average a
  fatal defect into a composite quality score.
- Be constructive: identify the criterion, minimum feasible repair, stronger option and its cost,
  closure evidence, and the claim that survives if the repair cannot be completed.
- Review is read-only by default. Do not alter code, data, configurations, or manuscript files
  unless the user explicitly asks for implementation or editing.
- Never invent a parameter range, run, result, effect, uncertainty interval, software version,
  benchmark, ablation, or validation.

## Choose the entry mode

| Mode | Use when | Required output emphasis |
|---|---|---|
| `plan` | the evaluation has not been run | decision-bearing parameters, defensible alternatives/ranges, fair comparison design, controls, freeze point and analysis handoff |
| `audit` | Methods, configurations, code, logs or result artifacts exist | provenance, selection timing, leakage, metric fit, method assumptions, fairness, evidence gaps and atomic repairs |
| `interpret` | real evaluation results are supplied | direction/magnitude, uncertainty, stability/failure boundary, heterogeneity, claim consequence and residual limit |
| `writing-package` | the science is fixed and must be placed in a paper | exact Methods/Results/Figure/Supplement/Discussion jobs without implying unrun analyses |

Also declare `focus: parameters | evaluation-metrics | methodology | combined` and the active
scope/modalities. A request may enter with an incomplete manuscript or a single configuration file;
do not require a prior pipeline task.

## Minimal intake

Record what is available and mark the rest `AUTHOR_INPUT_NEEDED`:

1. study question, estimand or intended use and affected Claim IDs;
2. scope and modalities; cohort/specimen hierarchy and true independent unit;
3. frozen method/model/pipeline version and data/split/test-access state;
4. parameter values, defaults, candidate ranges/levels, units and rationale sources;
5. when and on which data each setting, threshold, model or metric was selected;
6. comparators, controls, ablations, evaluation metrics, tuning/compute budget and hardware;
7. supplied results, uncertainty, run/seed structure, failures and exact artifact locations.

## Required workflow

1. Open [the canonical assessment reference](references/parameter-and-methodology-evaluation.md).
2. Reconstruct the chain:
   `question/estimand -> unit -> measurement -> preprocessing -> representation -> selection ->
   method/model -> metric -> validation -> claim`.
3. Build separate methodology-fit, parameter, metric/readout, and sensitivity/robustness tables.
4. Activate only evaluations that can change a decision or claim. Do not demand every possible
   grid, ablation, or alternative method.
5. For each finding, bind the exact evidence anchor, criterion, affected claim, minimum repair,
   optional stronger route/cost, closure evidence, and manuscript placement.
6. If actual comparison outputs need statistical inference, hand off the paired predictions or
   estimates, independent unit, resampling hierarchy and multiplicity family to `radiology-stats`.
7. Use [the reusable assessment matrix](templates/parameter-methodology-evaluation-matrix.md) when a
   durable artifact is useful.
8. When the team wants to reuse institution- or platform-specific experience, open
   [the local experience registry](templates/local-parameter-and-method-experience-registry.md).
   Transfer only rows whose platform, specimen, data state, endpoint, unit and intended claim are
   compatible; preserve failed and null experience as well as successful settings.

## Scientific red lines

- Tuning selects a configuration; sensitivity analysis evaluates a locked conclusion. Do not
  present the tuning trace as independent robustness evidence.
- The protected test set cannot select parameters, methods, thresholds, features, stopping rules,
  favourable seeds, figures or claims.
- Fair method comparison holds cases, splits, preprocessing, endpoint, metric and—where relevant—
  tuning budget, pretraining information, implementation and hardware conditions comparable.
- Folds, seeds, patches, slices, lesions, cells, spots, tiles and model runs are not new patients or
  donors. Preserve the actual sampling and resampling hierarchy.
- If changing a setting changes the estimand, inclusion population, spatial scale, cell identity,
  biological object or decision threshold, treat it as a distinct analysis question—not a routine
  sensitivity check.
- Perturbation dose, time, guide design/number, assignment and target-engagement criteria are
  experimental-design factors. Do not optimize them against the desired phenotype as if they were
  ordinary machine-learning hyperparameters.
- An ablation supports the component's conditional contribution in the evaluated pipeline and
  data; it does not prove universal necessity, biological mechanism or causality.
- Stability is not correctness. Simulation, generated molecular layers and synthetic
  perturbations are not external or biological validation.
- A package default, popular paper or high-impact venue is not by itself a scientific rationale.

## Domain routing

Use this skill as the evaluation owner; open the relevant internal domain reference only for the
meaning, plausible alternatives and operational constraints of the active parameter or method.

| Domain | Domain execution/source owner | Typical decision-bearing evaluation |
|---|---|---|
| image formation/quantitation | `radiology-acquisition-qc` | series/phase/sequence acceptance, DICOM quantitative transforms, acquisition/reconstruction, contrast/tracer timing, dose, artifacts, phantom/test-retest, site qualification and protocol drift |
| radiomics/imaging analysis | `radiology-radiomics`, `radiology-annotation` | resampling/interpolation, binning, segmentation perturbation, stability cutoff, harmonisation, feature selection and threshold freeze after the measurement passport |
| deep imaging | `radiology-deep-learning` | input scale/patch, architecture/pretraining, augmentation, loss/optimizer/schedule, search budget, seeds, checkpointing, ablation, OOD and efficiency |
| bulk RNA | execution: `radiology-transcriptomics-analysis`; meaning: `radiology-radiogenomics` bulk playbook | filtering, normalization, design/contrast, batch/composition, model family, FDR/effect thresholds, gene-set universe |
| sc/snRNA | execution: `radiology-transcriptomics-analysis`; meaning: `radiology-radiogenomics` single-cell playbook | QC, ambient/doublet handling, normalization/HVG, integration, PCs/kNN/resolution, annotation, pseudobulk unit, trajectory root |
| spatial | execution: `radiology-transcriptomics-analysis`; meaning: `radiology-radiogenomics` spatial playbook | segmentation, coordinate error, deconvolution, smoothing, domain resolution/seed, radius/kernel/k, spatial null and patient aggregation |
| pathology | `radiology-radiogenomics` pathology playbook | stain/scoring, magnification/tile, colour normalization, segmentation, phenotype cutoff, ROI sampling and patient aggregation |
| multi-omics | `radiology-radiogenomics` integration playbooks | matched intersection, missing-modality policy, scaling, factor/latent dimension, modality weights, alignment objective, unimodal ablation |
| perturbation | design/audit source: `radiology-experiment-design`; mechanism meaning: `radiology-radiogenomics` perturbation playbook | assignment, efficiency, off-target, dose-time, target engagement, toxicity, control/rescue and multiplicity |
| imaging-mechanism | `radiology-radiogenomics` bridge playbook | all active modality settings plus patient-lesion-region-block-section-cell/time mapping, bridge sensitivity and discordance |

## Output contract

Return the shortest complete set needed for the request, in this order:

1. `Evaluation scope and claim` — mode, focus, scope, active modalities, independent unit,
   materials and evidence boundary.
2. `Methodology-fit matrix` — question/estimand, data layer/unit, assumptions, comparator/control,
   validation and verdict.
3. `Parameter ledger` — role, value/range/unit, rationale, selection data/timing, search budget,
   freeze state, sensitivity, provenance and claim consequence.
4. `Evaluation-metric/readout matrix` — task fit, aggregation, threshold/prevalence dependence,
   uncertainty, tuning-objective overlap and blind spot.
5. `Benchmark/ablation/control matrix` and `Sensitivity/robustness results or plan` — matched
   conditions, execution state, failure boundary and negative results.
6. `Strengths and atomic findings` — evidence anchor, criterion, severity, minimum repair, stronger
   option/cost and closure evidence.
7. `Statistical handoff` — only the comparisons requiring estimation, intervals, tests or
   multiplicity control.
8. `Writing placement` — Methods, Results, Figure/Table, Supplement/config/code, Discussion and
   Abstract/title constraints.
9. `Claim verdict and next action` — `PASS / CONDITIONAL / STOP`, surviving claim ceiling, the
   single next decision-bearing action and `AUTHOR_INPUT_NEEDED` fields.

## Handoffs and non-ownership

- Configure or run a radiomics/DL pipeline → its imaging execution skill; configure, run, audit or
  reproduce bulk/sc/snRNA/spatial workflows → `radiology-transcriptomics-analysis`.
- Design functional IHC/mIF, tissue, cell, organoid, animal, perturbation, target-engagement or
  rescue evidence → `radiology-experiment-design`; this skill may later audit its method choices.
- Estimate paired differences, CIs, cluster bootstrap, run variability or multiplicity →
  `radiology-stats` after this skill defines the comparison and hierarchy.
- Audit all dimensions of a full manuscript → `radiology-prereview`; it consumes these findings
  without replacing the criterion or closure evidence.
- Draft prose from fixed evidence → `radiology-writing`; sentence-level polish →
  `radiology-polishing`.
- Turn reviewer comments into a response/verification ledger → `radiology-response`.
- Audit journal upload files and format rules → `radiology-submission`.

Do not silently broaden a focused parameter/method question into a full manuscript review or an
unrequested execution project.
