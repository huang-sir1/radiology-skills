---
name: radiology-transcriptomics-analysis
description: "Build/run/audit bulk RNA, sc/snRNA and spatial workflows with traceable QC; not mechanism claims."
---

# Transcriptomics analysis execution

Use this skill when the requested object is an executable or auditable bulk RNA, sc/snRNA, or
spatial-transcriptomics workflow. It can be entered directly with raw matrices, processed objects,
code, logs, or only a proposed analysis. It does not require an imaging dataset.

## Core contract

- Separate `PLAN_ONLY`, `CODE_READY`, `RUNNING`, `RUN_COMPLETE`, `RUN_FAILED`, `AUDIT_ONLY`, and
  `REPRODUCED`. Never turn a plan, code draft, screenshot, reported result, or partial log into a
  completed run.
- Preserve the chain `source files -> sample/donor map -> QC decisions -> transformed object ->
  analysis object -> result table/figure -> claim handoff` with exact paths and versions.
- Use the biological sampling unit for inference. Cells, nuclei, spots, genes, tiles, fields,
  technical replicates, bootstrap draws, seeds and clusters are not new patients or donors.
- Build the shortest workflow that answers the locked question. Optional trajectory, cell-cell
  communication, GRN, deconvolution or integration is activated only when its assumptions and
  decision value are explicit.
- Never invent data availability, sample annotations, reference labels, package versions, QC
  thresholds, commands, run success, results, cell identities, spatial domains or mechanisms.
- Review is read-only by default. Build, edit, or execute code only when the user requests it and
  the target inputs, working directory, output root, environment and protected-data boundary are
  known.

## Choose the entry mode

| Mode | Use when | Primary output |
|---|---|---|
| `plan` | question and data state are known but no locked workflow exists | modality plan, decision points, expected artifacts and analysis lock |
| `build` | code/configuration must be created or repaired | versioned code/config plus dry-run and output contract |
| `run-audit` | code should be executed/monitored, or an existing run must be audited | run manifest, log/QC evidence, failures and artifact inventory |
| `reproduce` | an earlier modality-specific run has command, environment and reference outputs | controlled assay/workflow rerun, QC comparison and domain verdict; cross-domain evidence level goes to `radiology-reproducibility` |
| `interpret-handoff` | real outputs exist and need scientific interpretation | result-to-question packet with evidence and claim ceilings; no invented mechanism |
| `mentor` | a learner needs constructive choices before or after analysis | minimum defensible, standard publishable and ambitious routes with rationale, cost, failure signal, fallback and closure evidence |
| `writing-handoff` | verified outputs must be placed into a manuscript without claim drift | Methods/Results/display/Supplement/Discussion/Abstract-title placement map with evidence locators and prohibited upgrades |

Declare exactly one primary modality: `bulk-rna`, `scrna`, `snrna`, or `spatial`. Declare secondary
modalities only when there is a real matched or bridge analysis. If the user asks whether a
parameter or method choice is defensible rather than to configure or run it, route that decision to
`radiology-method-evaluation`.

## Minimal intake

Record what is available and mark the rest `AUTHOR_INPUT_NEEDED`:

1. question, endpoint/contrast, intended use, affected Claim IDs and whether imaging is involved;
2. source type and exact locations: FASTQ, counts, features/barcodes, matrices, object files,
   histology images, coordinates, annotations, code, logs and prior outputs;
3. donor/patient/specimen/region/section/batch/library hierarchy and matched-sample map;
4. platform/chemistry/reference build or assay version when known; strandedness and feature
   definition for bulk; spot/bin/cell resolution for spatial;
5. clinical covariates, group/contrast, repeated measures, confounders and protected test state;
6. environment, package lock, compute limits, output root, seed policy and execution authority;
7. pre-existing QC thresholds, exclusions, reference atlases, labels, checkpoints and deviations.

If donor identity, sample-to-donor mapping, contrast, output root or execution authority is missing,
planning may continue but execution returns `RUN_BLOCKED`.

## Required workflow

1. Open [the modality workflows](references/modality-execution-workflows.md) and
   [the runtime/reproducibility contract](references/runtime-and-reproducibility-contract.md).
2. Freeze an intake manifest and choose the narrowest modality branch.
3. Define the true independent unit, analysis unit, repeated-measure structure and aggregation
   rule before filtering, integration or testing.
4. Create a decision ledger for every irreversible or conclusion-bearing choice: inclusion,
   filtering, normalization, reference/annotation, integration, contrast, spatial scale and
   exclusion.
5. Write the analysis plan and expected-output contract. Preserve a protected-test boundary where
   applicable.
6. In `build`, create code/configuration with explicit inputs, outputs, versions, seeds, assertions,
   checkpoints and failure behavior. Run only safe dry checks until real execution is authorized.
7. In `run-audit`, record the exact command, working directory, environment, start/end state, log,
   exit status, warnings, QC decisions, deviations and artifact checksums where feasible.
8. Stop on mapping ambiguity, corrupt/incompatible objects, sample-count mismatch, output
   overwrite risk, unresolved privacy boundary, or a requested analysis that changes the locked
   estimand without approval.
9. Package real outputs for statistical inference, biological interpretation, method evaluation,
   writing and review without silently upgrading evidence state.

Use [the analysis plan](templates/transcriptomics-analysis-plan.md),
[run manifest](templates/analysis-run-manifest.md), [QC decision log](templates/qc-decision-log.md),
[local runtime profile](templates/local-transcriptomics-runtime-profile.md), and
[local analysis experience registry](templates/local-analysis-experience-registry.md) when
persistent artifacts are useful. Local experience can guide failure diagnosis only inside its
recorded platform/tissue/data-state boundary; it never becomes an unreported default.

## Modality routes

| Modality | Minimum execution chain | Decision-bearing extensions |
|---|---|---|
| bulk RNA | optional FASTQ front end -> gene/transcript counts + raw-read QC -> metadata identity/QC -> filtering -> normalization/exploration -> design/contrast -> gene-level model -> multiplicity -> pathway/score -> export | batch/composition adjustment, paired/repeated design, deconvolution, signature validation, survival/clinical association |
| sc/snRNA | optional chemistry-aware FASTQ front end -> raw + filtered feature-barcode matrices -> calling/ambient/RBC/QC -> doublets -> normalization/HVG -> dimension reduction -> integration decision -> neighbors/clustering -> annotation -> donor-aware DE/abundance -> export | subclustering, trajectory, state scoring, communication, GRN, reference mapping, perturbation response |
| spatial | optional platform-aware FASTQ/image front end -> matrix + barcode/coordinate/image bundle -> geometry/registration/segmentation QC -> filtering/normalization -> cell-type mapping/deconvolution decision -> domains -> spatial statistic/neighborhood -> patient aggregation -> export | multi-section alignment, ligand-receptor context, boundary gradients, image-feature bridge, spatial trajectory |

## Scientific red lines

- Do not treat cell/spot-level P values as patient-level evidence. For case-control or clinical
  claims, use donor/patient-aware models, pseudobulk or another justified hierarchical strategy.
- Integration is not automatic quality improvement. It can erase real biological or clinical
  differences; preserve unintegrated evidence and test whether the intended contrast remains.
- Cluster labels are hypotheses supported by declared markers/references and discordance checks,
  not ground truth supplied by an algorithm.
- Post hoc QC tuned until the desired biology appears is outcome leakage. Record timing and inspect
  conclusion stability under defensible alternatives.
- Gene-set enrichment depends on the tested universe, ranking/statistic, database version and
  multiplicity family. A pathway label is not direct pathway activity or causal mechanism.
- Deconvolution, imputation, virtual cells/spots, spatial completion and inferred interactions are
  estimates. They are not measured cells, molecules, physical contact, perturbation or validation.
- Trajectory ordering is an inferred geometry; it does not establish real time, lineage or causal
  direction without external evidence.
- A spatial neighborhood result must state coordinate system, radius/kernel/k, edge handling,
  null model, section/patient aggregation and sensitivity to scale.
- Cross-modal agreement in the same cohort is orthogonal concordance, not independent replication.
- Never overwrite raw inputs or the only copy of a processed object. Write to an explicit output
  root and preserve provenance.

## Output contract

Return only the sections needed for the current mode, but preserve this order:

1. `Execution scope` — mode, modality, question/contrast, hierarchy, independent unit, evidence
   state, protected-test state and supplied artifacts.
2. `Input and identity audit` — source paths, dimensions/checksums when available, donor/sample
   mapping, missing/duplicate identities and blockers.
3. `Workflow and decision ledger` — each step's input, output, rationale, alternatives,
   assumption, decision owner, freeze state and failure condition.
4. `Run record` — exact command/environment/seed, start/end/exit status, log path, deviations and
   monitored output paths; omit only in `plan`.
5. `QC and exclusion ledger` — metric, level, rule, timing, affected units, retained/excluded counts,
   reason, sensitivity need and author approval.
6. `Artifact inventory` — object/table/figure/report path, schema/dimensions, checksum or other
   integrity evidence, producer and verification state.
7. `Findings and failure boundary` — real observed results only, alternative explanations,
   unresolved confounding and what failed or was not run.
8. `Handoffs` — exact packet for inference, method judgement, mechanism interpretation, wet-lab
   validation, writing or prereview.
9. `State and next action` — one of the declared execution states, blockers, surviving claim
   ceiling and the single next decision-bearing action.

In `mentor`, every major recommendation also reports: why it matters, minimum repair, stronger
alternative, resource/time burden, expected failure signal, fallback, closure evidence and the claim
that survives if it cannot be repaired. In `writing-handoff`, do not draft around missing evidence:
map frozen workflow/version/unit/QC to Methods; verified prespecified or labeled exploratory outputs
to Results; source-data locators to figures/tables; full exclusions/sensitivities/environment/
deviations to Supplement; alternatives and limits to Discussion; and enforce the weakest-link claim
ceiling in Abstract/title.

## Handoffs and non-ownership

- Biological interpretation, alternative mechanism hypotheses, cross-scale imaging bridge and
  claim ceiling -> `radiology-radiogenomics`, using only verified result artifacts.
- Parameter provenance, method fit, integration/normalization alternatives, sensitivity and fair
  comparison -> `radiology-method-evaluation`.
- Donor-aware effect estimation, confidence intervals, multiplicity, hierarchical modelling or
  survival inference -> `radiology-stats` after this skill freezes units and contrasts.
- Functional/perturbational wet-lab validation design -> `radiology-experiment-design`.
- Data governance, de-identification and sharing -> `radiology-data` and `radiology-ethics`.
- Frozen replay packaging, prespecified tolerance, operator independence and cumulative evidence
  level -> `radiology-reproducibility`; this skill retains assay/workflow-specific rerun and QC.
- Fixed-evidence manuscript construction -> `radiology-writing`; whole-manuscript review ->
  `radiology-prereview`; upload-file audit -> `radiology-submission`.

This skill may explain what an output means operationally, but a computational association,
estimated cell state, inferred spatial relation or computational perturbation is **not causal proof**.
