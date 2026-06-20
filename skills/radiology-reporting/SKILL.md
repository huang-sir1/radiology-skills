---
name: radiology-reporting
description: "Route an imaging-research manuscript or protocol to the correct reporting/quality guideline and audit it item-by-item for Radiology (RSNA) submission. Use when the user mentions CLAIM, TRIPOD+AI, STARD, PRISMA-DTA, QUADAS-2, CLEAR, METRICS, RQS, IBSI, PROBAST, CONSORT-AI, a \"reporting checklist\", \"what's required for submission\", radiomics quality, or wants to know what a reviewer will check. Produces a filled checklist with PRESENT / PARTIAL / MISSING per item, manuscript location, and concrete fixes. Do not fabricate compliance — flag missing items honestly."
---

# Radiology Reporting-Guideline Compliance

Use this skill to make an imaging study **reviewer-proof on reporting**. _Radiology_ and the
RSNA family require the relevant EQUATOR checklist at submission, and imaging-AI / radiomics
papers are now judged against a specific, version-sensitive stack of guidelines. This skill
(1) identifies the study type, (2) selects the correct guideline(s), (3) audits the manuscript
item-by-item, and (4) returns a submission-ready checklist plus a prioritised fix list.

## Core stance

- **The checklist is the contract.** A reviewer maps your paper to a guideline; do the same
  first, in their seat.
- **Report honestly.** Mark each item `PRESENT`, `PARTIAL`, or `MISSING`. Never label
  something compliant to be agreeable. A `MISSING` flag you surface is cheaper than a
  reviewer finding it.
- **Cite the location.** Every `PRESENT` claim must point to a section / page / figure /
  supplement. If you cannot point to it, it is `PARTIAL` at best.
- **Versions matter.** Use the current version (CLAIM **2024 Update**, TRIPOD**+AI** 2024,
  CLEAR 2023, METRICS 2024). Name the version you audited against.
- **Reporting ≠ quality ≠ risk-of-bias.** CLEAR (reporting) → METRICS / RQS (methodological
  quality) → PROBAST(-AI) / QUADAS-2 (risk of bias). Different tools, different jobs; pick
  the right one(s).
- **Don't invent the science.** This skill audits reporting; it never fabricates the missing
  experiment, metric, or dataset. It tells the author what to add.

## When to use

- "Which checklist does my study need?" / "What will _Radiology_ require at submission?"
- "Audit this manuscript against CLAIM / TRIPOD+AI / STARD / CLEAR / METRICS / RQS."
- "Is my radiomics pipeline reported reproducibly (IBSI)?"
- "Fill in the CLAIM checklist with page numbers."
- "What's my risk-of-bias exposure under PROBAST-AI / QUADAS-2?"
- Pre-submission self-audit, or triaging a reviewer comment that cites a guideline.

## Routing — pick the guideline(s) before auditing

Most imaging-AI papers need **two or more** of these (a reporting guideline **and** a
quality/risk-of-bias tool).

| Study type | Primary reporting guideline | Add for quality / risk-of-bias |
|---|---|---|
| AI/ML system in medical imaging (any task) | **CLAIM 2024** | TRIPOD+AI if it is a prediction model; DECIDE-AI for early clinical decision-support |
| Diagnostic/prognostic **prediction model** (incl. ML/DL) | **TRIPOD+AI (2024)** (+ TRIPOD-Cluster, TRIPOD for Abstracts) | **PROBAST / PROBAST-AI** (risk of bias) |
| **Radiomics** (hand-crafted features → model) | **CLEAR (2023)** for reporting | **METRICS (2024)** and/or **RQS / RQS 2.0** for quality; **IBSI** for feature reproducibility |
| **Diagnostic accuracy** (test vs reference standard) | **STARD 2015** | QUADAS-2 if part of a review; STARD-AI when finalised |
| **DTA systematic review / meta-analysis** | **PRISMA-DTA (2018)** | **QUADAS-2** (+ QUADAS-C for comparative) per included study |
| Systematic review / meta-analysis (general) | **PRISMA 2020** | AMSTAR-2; ROBIS |
| Observational (cohort/case-control/cross-sectional) | **STROBE** | (REMARK for tumour-marker prognostic studies) |
| Randomised trial of an imaging/AI intervention | **CONSORT 2010 (+ CONSORT-AI)** | protocol: **SPIRIT (+ SPIRIT-AI)** |
| Imaging biomarker / quantitative imaging | QIBA Profile reporting + STARD/TRIPOD as applicable | IBSI; phantom/repeatability (QIBA) |

> Open [`references/guideline-router.md`](references/guideline-router.md) for the full
> decision tree, including hybrid studies (e.g. a radiomics **prediction model** validated
> for **diagnostic accuracy** → CLEAR + TRIPOD+AI + STARD + IBSI).

## When to open extra files

| File | Open when |
|---|---|
| [references/guideline-router.md](references/guideline-router.md) | Choosing guideline(s); hybrid/edge-case study types; how guidelines stack |
| [references/claim-2024.md](references/claim-2024.md) | Auditing a medical-imaging AI paper against the CLAIM 2024 Update |
| [references/tripod-ai-probast.md](references/tripod-ai-probast.md) | Prediction-model reporting (TRIPOD+AI) and PROBAST(-AI) risk-of-bias |
| [references/clear-metrics-rqs.md](references/clear-metrics-rqs.md) | Radiomics reporting (CLEAR) and quality scoring (METRICS, RQS / RQS 2.0) |
| [references/ibsi-features.md](references/ibsi-features.md) | Making radiomic features reproducible/standardised (IBSI image processing + feature nomenclature) |
| [references/stard-prisma-quadas.md](references/stard-prisma-quadas.md) | Diagnostic-accuracy reporting (STARD), DTA reviews (PRISMA-DTA), risk of bias (QUADAS-2) |
| [references/radiology-submission-map.md](references/radiology-submission-map.md) | Mapping checklist items to where they belong in a _Radiology_ manuscript + submission logistics |

## Workflow

1. **Classify the study.** Determine task (classification / detection / segmentation /
   prediction / diagnostic accuracy / discovery), data provenance, whether a model is
   developed and/or validated, and whether the endpoint is accuracy, prognosis, or biology.
2. **Select guideline(s)** from the routing table. State which version. If the study is
   hybrid, select the stack and say why each applies.
3. **Load the relevant reference file(s)** and audit **every item**. For each item record:
   `Item ID | Requirement (short) | Status (PRESENT/PARTIAL/MISSING/NA) | Location | Fix`.
4. **Prioritise fixes.** Group into `Blocker` (will trigger major revision / desk reject),
   `Should-fix` (reviewer will likely ask), `Polish`. Tie each blocker to the specific
   reviewer risk.
5. **Cross-check integrity hot-spots** (see below) — the items reviewers weaponise most.
6. **Return** the filled checklist + a one-screen executive summary + the prioritised fix
   list. Offer to draft the missing text/Methods sentences (hand off to `radiology-writing`).

## Integrity hot-spots (audit these even if not asked)

These are the recurring reasons imaging-AI/radiomics papers get rejected:

- **Data leakage / partition hygiene.** Train/validation/test split made **at the
  patient level** (not slice/lesion); no test-set tuning; preprocessing, feature
  selection, harmonisation, and normalisation fit on **training data only**; augmentation
  never crosses the split. (CLAIM, TRIPOD+AI, METRICS, CLEAR all probe this.)
- **External / independent validation.** Internal CV alone is weak. State the validation
  type (internal resampling, temporal, geographic, fully external) and cohort source.
- **Reference standard & ground truth.** Who labelled, how many readers, expertise,
  blinding, adjudication, and the reference standard's own accuracy. (STARD, CLAIM.)
- **Class/prevalence & spectrum.** Report disease prevalence; flag artificial 1:1 sampling;
  describe the clinical spectrum (STARD spectrum bias; QUADAS-2 patient selection).
- **Radiomics reproducibility.** Software + version, image preprocessing (resampling,
  discretisation/bin width, intensity normalisation), segmentation method and
  inter-observer reproducibility (ICC), feature definitions **IBSI-compliant**, and
  scanner/protocol harmonisation (e.g. ComBat). (CLEAR, METRICS, IBSI.)
- **Sample size / EPV.** Events-per-variable, or a stated sample-size rationale (Riley et al.
  for prediction models). High-dimensional features vs. n is the classic overfitting trap.
- **Metrics match the task & prevalence.** AUC alone is insufficient; report calibration and
  clinical-utility (decision-curve) for prediction models; report CIs everywhere.
  (Hand off computation to `radiology-stats`.)
- **Code / model / data availability.** Statement present and specific. (Hand off to
  `radiology-data`.)

## Output contract

Return, in this order:

1. **`Study classification`** — task, design, endpoint, and the selected guideline stack
   (with versions).
2. **`Checklist`** — a table with `Item | Status | Location | Fix` for every item of each
   selected guideline. Use `NA` only with a one-line justification.
3. **`Compliance summary`** — counts (`PRESENT / PARTIAL / MISSING / NA`) per guideline and
   an overall readiness read (e.g. "CLAIM 31/42 present; 4 blockers").
4. **`Prioritised fixes`** — `Blocker / Should-fix / Polish`, each tied to the reviewer risk
   and the manuscript location to edit.
5. **`Author input needed`** — questions only the authors can answer (e.g. "Was the test set
   sampled at patient level?").

If the user pastes only part of a manuscript, audit what is present and mark the rest
`Cannot assess — section not provided` rather than guessing.

## Quality bar

A good audit reads like a rigorous methods reviewer who is **on the author's side**: it
finds the holes before submission, points to the exact item and location, and hands back
the precise sentence the Methods needs — without ever inventing compliance the paper
doesn't have.

## Handoffs

- Missing statistics → `radiology-stats` (compute/report AUC CIs, DeLong, ICC, calibration, DCA).
- Missing Methods/Results prose → `radiology-writing`.
- Data/code availability wording, DICOM de-identification → `radiology-data`.
- Radiogenomics-specific design/leakage → `radiology-radiogenomics`.
- Figure that proves an item (ROC, calibration, flow diagram) → `radiology-figure`.
