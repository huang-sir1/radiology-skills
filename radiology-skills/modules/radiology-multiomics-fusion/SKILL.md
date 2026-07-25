---
name: radiology-multiomics-fusion
description: "Use when a radiology study must jointly model five data dimensions: imaging, clinical, pathology, bulk molecular omics, and single-cell or spatial omics. Selects early, intermediate, late, graph, or latent-factor fusion; handles block-specific preprocessing, missing modalities, batch and site effects, nested feature selection, ablation, interaction analysis, and external validation. Prevents high-dimensional fusion from outrunning the matched sample size."
---

# Five-Dimensional Multi-Omics Fusion

Use this skill when all five dimensions — **imaging, clinical, pathology, bulk
molecular omics, and single-cell or spatial omics** — are intended for joint prediction
or integration. The analysable cohort is defined by patient-level linkage and modality
availability, not by the largest source cohort. If fewer than five dimensions are used,
label the study a **reduced-dimensional variant** and confirm that this module is still
more appropriate than an existing focused module.

## Core stance

- **Availability before architecture.** Build the patient-by-modality matrix and
  report the matched intersection before choosing a fusion method.
- **Matched n limits complexity.** The complete-case count, modality patterns,
  centers, and validation groups — plus endpoint events for supervised prediction —
  must support every fitted component. De-escalate when they do not.
- **Earn the fusion by branch.** Supervised models must beat clinical-only,
  single-modality, and simple regularized or late-fusion baselines. Unsupervised
  solutions must show stable, assignable, independently replicable structure.
- **Nest the whole pipeline.** Fit normalization, harmonization, embeddings, feature
  selection, imputation, fusion, and tuning using training data only.
- **Respect the experimental unit.** Cells, spots, regions, slides, and tiles are nested
  observations; donors or patients, not their subunits, determine the independent n.
- **Missing blocks are design information.** Distinguish structural, workflow, and
  quality-related absence; do not silently convert them into complete cases.
- **Contribution is comparative, not causal.** For supervised prediction, use
  single-block models, predictive ablation, conditional permutation, and pre-specified
  interactions. For unsupervised discovery, examine block-removal effects on
  cluster/factor alignment, stability, and assignment uncertainty. Neither establishes
  biological mechanism.
- **Validate transportability.** Preserve patient, site, batch, and time boundaries;
  external validation must reproduce the required modalities and processing route.

## When to use

- A study intends to jointly model all five dimensions and must choose a defensible
  fusion architecture.
- The user asks about early, intermediate, late, graph, SNF, MOFA, DIABLO, iCluster,
  or deep multimodal fusion.
- Modality blocks are missing for some patients, or site and assay availability are
  entangled.
- A fusion manuscript needs leakage-safe preprocessing, ablation, contribution
  analysis, interaction testing, or site-aware validation.

## Boundary and reciprocal handoff

- Use **this module** when fusion architecture and joint modeling across the intended
  five dimensions are the central problems.
- Use **`radiology-radiogenomics`** when imaging-to-molecular association, pathway or
  cell-state interpretation, or biological mechanism is the central workflow.
- If fewer than five dimensions are available, state that this is a reduced-dimensional
  variant. Consider `radiology-radiogenomics` for imaging-omics association,
  `radiology-deep-learning` for a primarily multimodal predictive architecture, or
  `radiology-design` when the cohort and question remain unsettled.
- Hand formal sample-size and performance-inference calculations to `radiology-stats`.

## When to open extra files

| File | Open when |
|---|---|
| [references/fusion-architecture.md](references/fusion-architecture.md) | Choosing among early, intermediate, late, SNF, MOFA, DIABLO, iCluster, graph, and deep multimodal approaches |
| [references/missingness-and-validation.md](references/missingness-and-validation.md) | Handling missing blocks, complete-case bias, imputation, modality dropout, nested selection, site-aware validation, or ablation |

## Workflow

1. **Build the patient-by-modality availability matrix.** Put patients in rows and the
   five dimensions in columns; record usable/failed/missing status, acquisition time,
   lesion or specimen linkage, site, assay batch, and exclusion reason. Report total n,
   per-block n, every common availability pattern, and the all-block intersection.
2. **Apply the matched-n feasibility gate.** Check the matched n against proposed
   parameters, selected features, missingness patterns, centers, and intended
   validation; add endpoint-event adequacy for supervised prediction. If stable fitting
   and validation are not credible, reduce blocks or dimensions, use late fusion,
   restrict the aim to exploratory discovery, or collect more matched data.
3. **Choose the supervised or unsupervised branch.** For prediction, pre-specify the
   endpoint, estimand, clinical use, clinical-only model, strongest single-block model,
   and a simple regularized or late-fusion comparator. For SNF/MOFA/iCluster discovery,
   do not force an endpoint, calibration target, or predictive comparator: lock the
   discovery objective and tuning, assess resampling stability, define a prespecified
   cluster assignment rule, seek independent replication, and use outcomes only as
   secondary associations rather than to select clusters or factors.
4. **Partition before preprocessing.** Split by patient and preserve site, time, family,
   lesion, donor, and assay-batch dependencies. Keep cells, spots, regions, slides, and
   tiles from one donor or patient in the same fold; use patient/donor summaries,
   pseudobulk, or hierarchical/mixed-effects models when subunit-level data are retained.
   Define outer evaluation and inner tuning folds; keep external data untouched until
   the final locked evaluation.
5. **Specify block-wise preprocessing.** For each block, document QC, filtering,
   normalization, dimension reduction, batch/site handling, and feature stability.
   Estimate every data-dependent transform within the relevant training fold. For
   prospective prediction, require a frozen harmonization transform that can process an
   unseen patient or site without refitting on its distribution; label cohort-refitted
   harmonization as transductive and do not present it as deployable validation.
6. **Justify the fusion architecture.** Choose the simplest approach supported by the
   objective, matched n, block dimensions, missingness, need for interactions,
   interpretability, and deployment availability. Record why the rejected alternatives
   are less defensible.
7. **Define missingness handling.** Separate absent blocks from within-block missing
   values, assess missingness by endpoint and site, and bound imputation to supported
   quantities. Predictive/deployment pipelines must not use outcomes to impute inputs.
   Inferential multiple imputation may include outcomes under stated assumptions, with
   estimates and uncertainty pooled across imputations. Test pattern-specific or
   missing-modality performance. For deep models, modality dropout is a robustness
   device, not proof that an absent assay was reconstructed.
8. **Fit and tune without leakage.** Place feature selection, representation learning,
   batch correction, imputation, hyperparameter search, and fusion weights inside nested
   training. Freeze the complete pipeline before outer-fold or external evaluation.
9. **Run branch-specific contribution analyses.** For supervised prediction, report
   every single-block model, the simple fusion baseline, the full model, and predictive
   leave-one-block-out ablation; use conditional block permutation for correlated blocks
   and test only pre-specified interactions. For unsupervised discovery, remove one
   block at a time and quantify cluster/factor alignment, resampling stability,
   assignment uncertainty, and replication rather than predictive performance.
10. **Validate by site and availability pattern.** Use nested internal validation and,
    where data permit, temporal, geographic, leave-one-site-out, or fully external
    validation. For prediction, report discrimination or prediction error, calibration,
    uncertainty, subgroup/site results, and realistic missing-block performance. For
    unsupervised discovery, report resampling stability, locked cluster assignment or
    factor projection, and independent replication; keep outcome associations secondary.
11. **Bound the conclusion.** In the supervised branch, claim added predictive value
    only when the locked fusion beats pre-specified baselines in appropriate validation.
    In the unsupervised branch, claim reproducible structure only when stability,
    prespecified assignment, and independent replication support it; keep outcomes
    secondary. Do not infer biological mechanism, clinical utility, or deployability
    from either branch alone.

## Output contract

Return the sections needed for the task:

1. **`Availability and feasibility`** — the five-block matrix summary, matched n,
   missingness patterns, and gate decision; include event counts only for a supervised
   endpoint when relevant.
2. **`Analysis branch`** — supervised endpoint, event adequacy, and baseline ladder; or
   unsupervised discovery objective, stability plan, assignment rule, and replication.
3. **`Fusion rationale`** — objective, selected architecture, data requirements,
   rejected alternatives, and failure controls.
4. **`Nested pipeline`** — split boundaries and block-specific preprocessing,
   selection, imputation, integration, and tuning.
5. **`Missingness plan`** — causes, bias assessment, supported handling, modality
   dropout or pattern-specific evaluation, and sensitivity analyses.
6. **`Contribution analysis`** — supervised single-block baselines, predictive
   leave-one-block-out ablation, conditional permutation, and pre-specified
   interactions; or unsupervised block-removal effects on cluster/factor alignment,
   stability, assignment uncertainty, and replication.
7. **`Validation and claims`** — for supervised prediction, internal and
   site-aware/external performance, calibration, uncertainty, and predictive ablation;
   for unsupervised discovery, stability, assignment uncertainty, block sensitivity,
   and independent replication, with outcomes secondary.
8. **`Author input needed`** — unresolved patient counts, linkage, batches, missingness
   causes, sites, external cohorts, deployment-time modalities, and event counts only
   when a supervised endpoint makes them relevant.

This skill supports study design and audit; it does not provide patient-specific
diagnosis, treatment advice, or permission to fabricate missing assays or results.
