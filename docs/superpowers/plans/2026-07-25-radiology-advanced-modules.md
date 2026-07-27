# Radiology Advanced Modules Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the single-entry `radiology-skills` package from 22 to 27 independently routable modules and publish the verified update to `huang-sir1/radiology-skills`.

**Architecture:** Add five focused module directories under `radiology-skills/modules/`, each with a concise `SKILL.md` and detailed reference files. Preserve `radiology-skills/SKILL.md` as the only installed entry point, update repository documentation, and use a deterministic PowerShell audit as the red/green structural test.

**Tech Stack:** Markdown Agent Skills, YAML frontmatter, PowerShell validation, Git.

---

## File Map

**Create**

- `radiology-skills/tests/advanced-modules-structure.ps1` — deterministic structural, routing, link, count, and safety-boundary audit.
- `radiology-skills/modules/radiology-crossmodal-mapping/SKILL.md` — cross-modal mapping triggers and workflow.
- `radiology-skills/modules/radiology-crossmodal-mapping/references/alignment-and-pairing.md` — multi-scale alignment and inference limits.
- `radiology-skills/modules/radiology-crossmodal-mapping/references/mapping-and-validation.md` — mapping methods, controls, and validation.
- `radiology-skills/modules/radiology-multiomics-fusion/SKILL.md` — five-dimensional fusion workflow.
- `radiology-skills/modules/radiology-multiomics-fusion/references/fusion-architecture.md` — early/intermediate/late/graph/latent fusion.
- `radiology-skills/modules/radiology-multiomics-fusion/references/missingness-and-validation.md` — missing blocks, leakage, ablation, validation.
- `radiology-skills/modules/radiology-federated-learning/SKILL.md` — federated research design and audit.
- `radiology-skills/modules/radiology-federated-learning/references/federated-design.md` — federation type, aggregation, heterogeneity.
- `radiology-skills/modules/radiology-federated-learning/references/privacy-governance-evaluation.md` — threat model, governance, baselines, evaluation.
- `radiology-skills/modules/radiology-foundation-models/SKILL.md` — model selection and adaptation workflow.
- `radiology-skills/modules/radiology-foundation-models/references/adaptation-strategies.md` — zero-shot, probe, full and parameter-efficient tuning.
- `radiology-skills/modules/radiology-foundation-models/references/evaluation-and-reporting.md` — leakage-safe comparisons and reporting.
- `radiology-skills/modules/radiology-research-agent/SKILL.md` — imaging-research automation Agent workflow.
- `radiology-skills/modules/radiology-research-agent/references/agent-architecture.md` — orchestration, RAG, tools, state, checkpoints.
- `radiology-skills/modules/radiology-research-agent/references/safety-and-evaluation.md` — hallucination, injection, privacy, evaluation, clinical boundaries.

**Modify**

- `radiology-skills/SKILL.md` — add five trigger routes and scope boundaries.
- `README.md` — change module count to 27 and document the five virtual consultants.

**Exclude from staging**

- `.gitignore`
- `docs/` other than this plan and the approved design document already committed
- `promo-video/`

---

### Task 1: Add the Failing Structural Audit

**Files:**

- Create: `radiology-skills/tests/advanced-modules-structure.ps1`

- [ ] **Step 1: Write the failing test**

Create a PowerShell script that:

```powershell
$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$repoRoot = Split-Path -Parent $skillRoot
$expected = @(
  'radiology-crossmodal-mapping',
  'radiology-multiomics-fusion',
  'radiology-federated-learning',
  'radiology-foundation-models',
  'radiology-research-agent'
)

$rootSkill = Get-Content -Raw -LiteralPath (Join-Path $skillRoot 'SKILL.md')
$readme = Get-Content -Raw -LiteralPath (Join-Path $repoRoot 'README.md')

foreach ($name in $expected) {
  $module = Join-Path $skillRoot "modules/$name"
  $skill = Join-Path $module 'SKILL.md'
  if (-not (Test-Path -LiteralPath $skill)) { throw "Missing module skill: $name" }
  $content = Get-Content -Raw -LiteralPath $skill
  if ($content -notmatch "(?s)^---\s+name:\s+$([regex]::Escape($name))\s+description:") {
    throw "Invalid frontmatter: $name"
  }
  if ($rootSkill -notmatch [regex]::Escape("modules/$name/SKILL.md")) {
    throw "Root route missing: $name"
  }
}

if ($readme -match '\b22\b') { throw 'README still contains module count 22' }
if ($readme -notmatch '\b27\b') { throw 'README does not contain module count 27' }

$agent = Get-Content -Raw -LiteralPath (
  Join-Path $skillRoot 'modules/radiology-research-agent/SKILL.md'
)
foreach ($required in @(
  'clinical diagnosis',
  'treatment recommendation',
  'explicit authorization',
  'prompt injection',
  'citation accuracy'
)) {
  if ($agent -notmatch [regex]::Escape($required)) {
    throw "Research-agent boundary missing: $required"
  }
}

$markdownFiles = Get-ChildItem -LiteralPath $skillRoot -Recurse -Filter '*.md'
foreach ($file in $markdownFiles) {
  $text = Get-Content -Raw -LiteralPath $file.FullName
  $links = [regex]::Matches($text, '\[[^\]]+\]\(([^)#]+\.md)\)')
  foreach ($link in $links) {
    $target = Join-Path $file.DirectoryName $link.Groups[1].Value
    if (-not (Test-Path -LiteralPath $target)) {
      throw "Broken Markdown link in $($file.FullName): $($link.Groups[1].Value)"
    }
  }
}

Write-Output 'Advanced module audit passed: 5 modules, root routes, README count, safety boundaries, and Markdown links.'
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File radiology-skills/tests/advanced-modules-structure.ps1
```

Expected: FAIL with `Missing module skill: radiology-crossmodal-mapping`.

- [ ] **Step 3: Commit the red test**

```powershell
git add -- radiology-skills/tests/advanced-modules-structure.ps1
git commit -m "Test advanced radiology module structure"
```

---

### Task 2: Implement Cross-Modal Mapping

**Files:**

- Create: `radiology-skills/modules/radiology-crossmodal-mapping/SKILL.md`
- Create: `radiology-skills/modules/radiology-crossmodal-mapping/references/alignment-and-pairing.md`
- Create: `radiology-skills/modules/radiology-crossmodal-mapping/references/mapping-and-validation.md`

- [ ] **Step 1: Write the module skill**

Use this exact frontmatter and keep the body focused on intake, routing, workflow, output contract, and red lines:

```yaml
---
name: radiology-crossmodal-mapping
description: "Use when an imaging study must map radiology phenotypes or habitats to single-cell, spatial-omics, or pathology-derived cell states across patients, lesions, specimens, regions, or time points. Designs paired, weakly paired, or unpaired cross-modal mapping; audits alignment, deconvolution, label transfer, contrastive learning, validation, scale mismatch, and biological-claim limits. Never treats unpaired public omics as direct patient-level mechanism proof."
---
```

The workflow must require a mapping-unit table, pairing classification, scale-alignment strategy, leakage-safe validation, negative controls, sensitivity analyses, and bounded claims. Link both reference files.

- [ ] **Step 2: Write detailed references**

`alignment-and-pairing.md` must define:

- patient → lesion → specimen → section → region → cell hierarchy;
- paired, partially paired, weakly paired, and unpaired evidence tiers;
- spatial and temporal mismatch;
- inference language allowed at each evidence tier.

`mapping-and-validation.md` must cover:

- pseudobulk, deconvolution, label transfer, canonical correlation, contrastive mapping, graph alignment, and habitat linkage;
- train/test separation at patient and center level;
- permutation, negative-region, null-feature, and sensitivity controls;
- external validation and orthogonal biological validation.

- [ ] **Step 3: Run the audit**

Run the structural audit. Expected: FAIL at the next missing module, proving this module satisfies its checks without falsely making the complete suite green.

- [ ] **Step 4: Commit**

```powershell
git add -- radiology-skills/modules/radiology-crossmodal-mapping
git commit -m "Add imaging cross-modal mapping skill"
```

---

### Task 3: Implement Five-Dimensional Multi-Omics Fusion

**Files:**

- Create: `radiology-skills/modules/radiology-multiomics-fusion/SKILL.md`
- Create: `radiology-skills/modules/radiology-multiomics-fusion/references/fusion-architecture.md`
- Create: `radiology-skills/modules/radiology-multiomics-fusion/references/missingness-and-validation.md`

- [ ] **Step 1: Write the module skill**

Use:

```yaml
---
name: radiology-multiomics-fusion
description: "Use when a radiology study must jointly model five data dimensions: imaging, clinical, pathology, bulk molecular omics, and single-cell or spatial omics. Selects early, intermediate, late, graph, or latent-factor fusion; handles block-specific preprocessing, missing modalities, batch and site effects, nested feature selection, ablation, interaction analysis, and external validation. Prevents high-dimensional fusion from outrunning the matched sample size."
---
```

The workflow must start with a patient-by-modality availability matrix and matched-n feasibility gate. It must require a simple baseline, a justified fusion architecture, nested preprocessing, missingness strategy, ablation, contribution analysis, and validation.

- [ ] **Step 2: Write references**

`fusion-architecture.md` must compare early, intermediate, late, SNF, MOFA, DIABLO, iCluster, graph, and deep multimodal approaches by data requirement and failure mode.

`missingness-and-validation.md` must define block-wise missingness, complete-case bias, modality dropout, imputation boundaries, nested feature selection, site-aware validation, and ablation reporting.

- [ ] **Step 3: Run the audit**

Expected: FAIL at `radiology-federated-learning`.

- [ ] **Step 4: Commit**

```powershell
git add -- radiology-skills/modules/radiology-multiomics-fusion
git commit -m "Add five-dimensional multiomics fusion skill"
```

---

### Task 4: Implement Federated Learning

**Files:**

- Create: `radiology-skills/modules/radiology-federated-learning/SKILL.md`
- Create: `radiology-skills/modules/radiology-federated-learning/references/federated-design.md`
- Create: `radiology-skills/modules/radiology-federated-learning/references/privacy-governance-evaluation.md`

- [ ] **Step 1: Write the module skill**

Use:

```yaml
---
name: radiology-federated-learning
description: "Use when multiple imaging centers cannot pool raw data and need a federated-learning research design. Chooses horizontal, vertical, split, or personalized federation; plans aggregation, non-IID handling, site weighting, secure aggregation, differential privacy, threat modeling, governance, communication, reproducibility, fairness, calibration, and centralized/local/external baselines. Never presents federated learning alone as proof of privacy or external validity."
---
```

The workflow must separate governance feasibility, federation topology, baseline definition, training protocol, threat model, heterogeneity analysis, evaluation, and reproducibility.

- [ ] **Step 2: Write references**

`federated-design.md` must cover federation type, FedAvg baseline, personalized and heterogeneity-aware alternatives, scanner/site non-IID data, communication rounds, failures, and site holdout.

`privacy-governance-evaluation.md` must cover membership/gradient leakage threats, secure aggregation, differential privacy trade-offs, controller roles, audit trails, fairness, calibration, centralized/local comparisons, and the distinction between federation and external validation.

- [ ] **Step 3: Run the audit**

Expected: FAIL at `radiology-foundation-models`.

- [ ] **Step 4: Commit**

```powershell
git add -- radiology-skills/modules/radiology-federated-learning
git commit -m "Add federated imaging research skill"
```

---

### Task 5: Implement Foundation-Model Adaptation

**Files:**

- Create: `radiology-skills/modules/radiology-foundation-models/SKILL.md`
- Create: `radiology-skills/modules/radiology-foundation-models/references/adaptation-strategies.md`
- Create: `radiology-skills/modules/radiology-foundation-models/references/evaluation-and-reporting.md`

- [ ] **Step 1: Write the module skill**

Use:

```yaml
---
name: radiology-foundation-models
description: "Use when an imaging study must select, adapt, fine-tune, or audit a pretrained medical imaging or vision-language foundation model. Covers zero-shot evaluation, linear probing, full fine-tuning, adapters, LoRA and other parameter-efficient tuning, prompt learning, domain adaptation, 2D/3D and image-text inputs, frozen tests, strong baselines, compute reporting, calibration, uncertainty, subgroups, and external validation. Warns against training a foundation model from scratch without adequate scale."
---
```

The workflow must require model-card and pretraining-overlap checks, task/modality match, adaptation ladder, frozen validation design, strong baselines, compute/reproducibility reporting, and clinical-claim limits.

- [ ] **Step 2: Write references**

`adaptation-strategies.md` must define when to use zero-shot, linear probe, partial/full tuning, adapters, LoRA, prompt learning, and domain adaptation.

`evaluation-and-reporting.md` must define overlap/leakage checks, task-specific baselines, identical splits and tuning budgets, calibration, uncertainty, subgroups, external validation, compute/carbon reporting, and checkpoint/licensing disclosure.

- [ ] **Step 3: Run the audit**

Expected: FAIL at `radiology-research-agent`.

- [ ] **Step 4: Commit**

```powershell
git add -- radiology-skills/modules/radiology-foundation-models
git commit -m "Add imaging foundation model adaptation skill"
```

---

### Task 6: Implement Imaging-Research Automation Agent

**Files:**

- Create: `radiology-skills/modules/radiology-research-agent/SKILL.md`
- Create: `radiology-skills/modules/radiology-research-agent/references/agent-architecture.md`
- Create: `radiology-skills/modules/radiology-research-agent/references/safety-and-evaluation.md`

- [ ] **Step 1: Write the module skill**

Use:

```yaml
---
name: radiology-research-agent
description: "Use when designing or auditing an LLM Agent that automates medical-imaging research tasks such as literature and dataset discovery, protocol planning, evidence-grounded RAG, analysis orchestration, reporting checks, manuscript workflows, and reproducible artifact handling. Covers tools, multi-agent roles, memory, state, checkpoints, human approval, prompt injection, data exfiltration, citation accuracy, task-success evaluation, cost, and latency. Excludes autonomous clinical diagnosis, treatment recommendation, and patient-specific decision-making."
---
```

The body must contain an explicit authorization gate for external writes and require evidence provenance, state/checkpoint design, human approval gates, failure recovery, security review, and measurable evaluation.

- [ ] **Step 2: Write references**

`agent-architecture.md` must cover:

- single versus multi-agent selection;
- planner, retriever, analyst, verifier, writer, and supervisor roles;
- RAG with source identifiers and claim-to-source mapping;
- tool allowlists, typed inputs/outputs, state machine, durable checkpoints, idempotency, and resumability;
- artifact manifest for papers, data, code, figures, and decisions.

`safety-and-evaluation.md` must cover:

- hallucination and citation verification;
- prompt injection and untrusted-document isolation;
- privacy, least privilege, secrets, data exfiltration and audit logs;
- mandatory human approval for submission, messaging, sharing, deletion, or external writes;
- task success, citation precision, numerical consistency, reproducibility, human correction rate, cost, latency, and time-saved evaluation;
- prohibition on autonomous clinical diagnosis or treatment recommendation.

- [ ] **Step 3: Run the audit**

Expected: FAIL with `Root route missing: radiology-crossmodal-mapping` because all modules now exist but root routing has not yet been updated.

- [ ] **Step 4: Commit**

```powershell
git add -- radiology-skills/modules/radiology-research-agent
git commit -m "Add imaging research automation agent skill"
```

---

### Task 7: Update Root Routing and README

**Files:**

- Modify: `radiology-skills/SKILL.md`
- Modify: `README.md`

- [ ] **Step 1: Add root routes**

Add five rows to `## Internal modules` with the exact module paths. Expand metadata triggers to include:

```text
cross-modal mapping, imaging-to-single-cell, five-dimensional multi-omics,
federated learning, foundation-model fine-tuning, LoRA, research agents,
RAG, multi-agent orchestration
```

Add routing boundaries:

- use cross-modal mapping when alignment itself is the central problem;
- use multi-omics fusion when joint prediction/integration is central;
- use federated learning when raw data cannot be pooled;
- use foundation models when model adaptation/benchmarking is central;
- use research agent only for research workflow automation.

- [ ] **Step 2: Update README**

Replace all user-facing module counts of 22 with 27. Add the five names:

```text
跨模态映射师
五维融合架构师
联邦协作工程师
基础模型调优师
科研智能体架构师
```

Add rows to the skill index and quick-selection table, describe the new capabilities in the overview and pain-point table, and add a 2026-07 update note. State explicitly that the research-agent module does not perform autonomous diagnosis or treatment decisions.

- [ ] **Step 3: Run the audit to verify green**

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File radiology-skills/tests/advanced-modules-structure.ps1
```

Expected:

```text
Advanced module audit passed: 5 modules, root routes, README count, safety boundaries, and Markdown links.
```

- [ ] **Step 4: Commit**

```powershell
git add -- README.md radiology-skills/SKILL.md
git commit -m "Route and document 27 radiology modules"
```

---

### Task 8: Final Verification and Publication

**Files:**

- Verify all changed files.
- Do not stage `.gitignore`, unrelated `docs/`, or `promo-video/`.

- [ ] **Step 1: Run all fresh checks**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File radiology-skills/tests/advanced-modules-structure.ps1
git diff --check HEAD~6..HEAD
git status -sb
git log -8 --oneline --decorate
```

Expected:

- audit passes;
- `git diff --check` has no output;
- only pre-existing unrelated `.gitignore`, `docs/`, and `promo-video/` changes remain uncommitted;
- commits exist for the structural test, five modules, and root documentation.

- [ ] **Step 2: Verify remote position**

```powershell
git fetch origin main
git rev-list --left-right --count origin/main...main
```

Expected: `0` behind and a positive number ahead. If behind is nonzero, stop and reconcile before pushing.

- [ ] **Step 3: Push**

```powershell
git push origin main
```

Expected: remote `main` advances successfully.

- [ ] **Step 4: Verify the remote commit**

```powershell
git ls-remote origin refs/heads/main
git rev-parse HEAD
```

Expected: both commands return the same full SHA.
