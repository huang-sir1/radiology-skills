# Modelling-route decision — radiomics vs deep features vs end-to-end DL vs foundation

Pick the modelling route **before** touching the data, from five inputs: patient n, event
count, annotation cost, compute, and timeline. You do **not** need to run the whole baseline
ladder — choose **one defensible primary route**; other routes appear only as pre-registered
comparators if the claim needs them (baseline logic → `radiology-deep-learning/architecture-choice.md`).

## Inputs

| Input | Why it gates the route |
|---|---|
| Patient n / event count (EPV) | Caps model capacity — the single strongest gate (→ `radiology-stats/sample-size.md`) |
| Annotation cost | Radiomics needs masks; end-to-end DL can work image-level but then needs more n |
| Compute | End-to-end 3D and foundation adaptation need a real GPU budget; radiomics and deep-feature routes run on a workstation |
| Timeline | End-to-end training + tuning takes weeks to months; a radiomics pipeline takes days to weeks |
| External-validation path | A weaker validation path forces a simpler route — transportability beats capacity |

## Decision tree

```text
Clinical question and endpoint fixed first (→ endpoints-and-estimands.md)
│
├─ n small (≲ 500 patients, or events ≲ 100), masks available or cheap, modest compute
│    → Route A: hand-crafted IBSI radiomics
│      [default start for most single-disease cohorts]
│
├─ n small-to-medium, want image-learned signal without full DL training
│    → Route B: pretrained deep features + classical ML
│      [radiomics discipline applied to embeddings]
│
├─ n medium-to-large (≳ 1000s of patients or many events), multi-center/scanner diversity,
│    GPU budget, image-level task (diagnosis / detection / segmentation)
│    → Route C: end-to-end transfer learning
│      [never from scratch at small n]
│
└─ large unlabelled pool, a strong pretrained encoder exists, and a fair task baseline is planned
     → Route D: foundation-model adaptation (linear probe / adapter / LoRA)
```

The n thresholds are orientation, not cut-offs — confirm the binding constraint with
`radiology-stats` before locking.

## Per-route card

| Route | Default starting point | Upgrade when | Downgrade / exit when |
|---|---|---|---|
| **A. Hand-crafted radiomics** | IBSI pipeline → ICC filter → de-correlate → LASSO → penalised regression; nested CV (→ `radiology-radiomics/selection-modelling.md`) | External validation secured; deep-feature comparison pre-registered | Events too few even for an EPV-legal model → feasibility claim (→ `weak-result-pivot.md`) |
| **B. Deep features + classical ML** | Pretrained encoder (state source, layer, pooling) → the same selection/modelling discipline as Route A; harmonise embeddings | Strong stable result + need for spatial context → Route C | Embeddings unstable across scanners and harmonisation fails → Route A |
| **C. End-to-end transfer learning** | ImageNet/medical-pretrained 2D/2.5D CNN, freeze-then-fine-tune, patient-level nested CV, fair baseline (→ `radiology-deep-learning/training-protocol.md`) | Multi-center external validation in hand; reader study planned | Compute/timeline slips, or internal CV shows overfit → Route B |
| **D. Foundation adaptation** | Linear probe first, then adapter/LoRA; pretraining-leakage audit; strong task baseline (→ `radiology-deep-learning/foundation-models-trustworthy-ai.md`) | Label-efficient win over a tuned Route C baseline + external test | Does not beat a tuned simple baseline → drop the foundation claim |

## Hard rules

- **One primary route.** The others are comparators only if the claim needs them; running all
  four and publishing the winner is route-shopping — the same optimism mechanism as model
  shopping (→ `radiology-radiomics/selection-modelling.md`).
- **Capacity follows evidence, not fashion.** A foundation model does not rescue a small
  single-center cohort (anti-pattern → `feasibility-triage.md`).
- **The validation plan gates the route, not vice versa.** No external path + a heavy route =
  a claim the data cannot carry (→ `validation-strategy.md`).
- Record the chosen route and its rationale in the protocol lock; changing route mid-study is
  a deviation and goes to the deviation log.

## Output pattern

```text
Inputs: n=[…], events=[…], masks=[…], compute=[…], timeline=[…]
Chosen primary route: [A/B/C/D] — one-line rationale
Default starting point: [per the card]
Comparator(s), if any: [pre-registered]
Upgrade trigger: [what evidence would justify moving up]
Deviation rule: [route change goes to the deviation log]
```
