# Radiology Skills Advanced Modules Design

Date: 2026-07-25

## Objective

Extend `radiology-skills` from 22 to 27 independently routable modules. The new modules cover five advanced research capabilities:

1. imaging-to-single-cell and spatial cross-modal mapping;
2. five-dimensional multi-omics fusion;
3. federated learning for multi-center imaging research;
4. medical imaging foundation-model adaptation and fine-tuning;
5. LLM-based agents for imaging-research automation.

The fifth module is limited to research automation. It must not provide autonomous clinical diagnosis, treatment recommendations, or individual-patient decision support.

## Architecture

Each capability is implemented as a self-contained directory under `radiology-skills/modules/`, following the repository's existing module pattern:

```text
module-name/
├── SKILL.md
└── references/
    └── focused workflow references
```

The repository-level `README.md` remains the user-facing overview. The root `radiology-skills/SKILL.md` remains the single installed entry point and routes requests to the five new internal modules. Users continue to install one skill folder rather than 27 separate skills.

Detailed subject matter belongs in reference files. Each module's `SKILL.md` stays concise and contains triggers, scope, workflow, output contract, routing boundaries, and red lines.

## New Modules

### 1. `radiology-crossmodal-mapping` — 跨模态映射师

Purpose: design and audit links between radiology phenotypes and single-cell, spatial-omics, or pathology-derived cellular states.

Core coverage:

- patient, lesion, specimen, section, region, and time-point alignment;
- paired versus unpaired data and the permitted strength of inference;
- imaging habitat to cell-state or spatial-neighborhood mapping;
- pseudobulk, deconvolution, label transfer, weakly paired and contrastive mapping;
- spatial registration uncertainty and scale mismatch;
- leakage-safe validation, negative controls, sensitivity analysis, and bounded biological claims.

Boundary: routes general radiogenomics integration to `radiology-radiogenomics`; this module is used when the cross-scale mapping itself is the central methodological problem.

### 2. `radiology-multiomics-fusion` — 五维融合架构师

Purpose: design and audit joint modeling across imaging, clinical, pathology, molecular bulk omics, and single-cell/spatial omics.

Core coverage:

- definition and availability matrix for the five dimensions;
- early, intermediate, late, graph-based, and latent-factor fusion;
- MOFA, SNF, DIABLO, iCluster and deep multimodal representations where justified;
- missing modalities, block-wise preprocessing, batch/site effects and nested feature selection;
- ablation studies, modality contribution, interaction testing and external validation;
- sample-size constraints and protection against high-dimensional overfitting.

Boundary: does not recommend a complex fusion architecture when a simpler late-fusion or single-modality baseline is more defensible.

### 3. `radiology-federated-learning` — 联邦协作工程师

Purpose: turn a multi-center, data-cannot-leave-site constraint into a reproducible federated imaging study.

Core coverage:

- governance, data-controller roles and cross-site feasibility;
- horizontal, vertical, split and personalized federated-learning choices;
- FedAvg-style baselines, heterogeneity-aware aggregation and site weighting;
- secure aggregation, differential privacy and threat modeling;
- non-IID center/scanner distributions, communication burden and failure handling;
- centralized/local baselines, leave-one-center-out tests, fairness and calibration;
- reproducibility, audit logs, versioning and deployment boundaries.

Boundary: distinguishes federated training from ordinary external validation and never treats federated learning as privacy proof by itself.

### 4. `radiology-foundation-models` — 基础模型调优师

Purpose: select, adapt, compare and report medical imaging foundation models for realistic downstream studies.

Core coverage:

- model and pretraining-data suitability for modality, anatomy and task;
- zero-shot evaluation, linear probing, full fine-tuning and parameter-efficient fine-tuning;
- adapters, LoRA, prompt tuning and domain adaptation;
- 2D/3D and vision-language input design;
- frozen test sets, leakage controls and site-aware validation;
- comparison against strong task-specific and conventional transfer-learning baselines;
- compute reporting, reproducibility, calibration, uncertainty and subgroup evaluation.

Boundary: advises against training a foundation model from scratch when data and compute scale are inadequate.

### 5. `radiology-research-agent` — 科研智能体架构师

Purpose: design and audit LLM agents that automate parts of the imaging-research lifecycle.

Core coverage:

- literature, dataset and research-gap discovery;
- protocol, statistical-analysis and reporting-checklist planning;
- retrieval-augmented generation with source provenance;
- single-agent versus multi-agent orchestration and tool selection;
- imaging, manuscript, spreadsheet and code artifact handling;
- task state, memory, checkpoints and resumability;
- human approval gates for evidence, analysis, manuscript and external actions;
- hallucination, prompt-injection, data-exfiltration and privacy controls;
- evaluation of task success, citation accuracy, reproducibility, cost, latency and human time saved.

Hard boundary:

- no autonomous diagnosis, treatment recommendation or patient-specific clinical decision;
- no invented literature, metrics, analyses, approvals or completed actions;
- no automatic submission, messaging, data sharing or other external write without explicit authorization;
- no bypassing ethics, governance, institutional security or human review.

## Root Routing and User Documentation

Update `radiology-skills/SKILL.md` to:

- add trigger terms and a routing row for each new module;
- distinguish cross-modal mapping from general radiogenomics;
- distinguish foundation-model adaptation from general deep learning;
- distinguish federated study design from generic multi-center validation;
- route research-agent requests only when workflow automation is central;
- preserve the single-entry installation model.

Update the repository `README.md` to:

- change all module counts from 22 to 27;
- add five virtual-consultant names and descriptions;
- expand the quick-selection table and module index;
- add the five capabilities to the overview and research-pain-point sections;
- explain that the research-agent module excludes clinical autonomous decision-making;
- add a dated update note.

## Validation Strategy

Create failing structural and routing tests before adding production module files. Tests must verify:

- all five module directories and `SKILL.md` files exist;
- every module has valid YAML frontmatter with the expected name and trigger-rich description;
- the root skill routes to every new module;
- all local Markdown links and referenced files resolve;
- README module counts and indexes consistently state 27;
- the research-agent module contains explicit clinical and external-action boundaries;
- the installed single-entry structure remains intact;
- unrelated `.gitignore`, existing `docs/` content, and `promo-video/` files are excluded from the publication commit.

Run the repository's existing validation scripts when available, plus a deterministic PowerShell structural audit and `git diff --check`.

## Publication

Implementation changes will be staged by explicit paths. The existing unrelated `.gitignore`, `docs/`, and `promo-video/` working-tree changes will not be included. After fresh validation, commit the five modules, root routing, README, tests, and this approved design/implementation documentation, then push to `origin/main` at `huang-sir1/radiology-skills`.

