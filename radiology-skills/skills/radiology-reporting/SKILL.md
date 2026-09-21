---
name: radiology-reporting
description: "Select/audit reporting guidelines across imaging AI, diagnosis, reviews, guidelines and economics."
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
  CLEAR 2023, METRICS 2024, STARD-AI 2025 for AI accuracy studies, CONSORT/SPIRIT **2025**,
  PROBAST**+AI** 2025 — full list with sources in `references/guideline-versions.md`).
  Name the version you audited against.
- **Provenance matters.** Record the official guideline/checklist source, version/update date,
  access date, and any target-journal overlay. Treat remembered requirements as provisional.
- **Reporting ≠ quality ≠ risk-of-bias.** CLEAR (reporting) → METRICS / RQS (methodological
  quality) → PROBAST+AI / QUADAS-3 v1.2 (risk of bias). Different tools, different jobs; pick
  the right one(s).
- **Don't invent the science.** This skill audits reporting; it never fabricates the missing
  experiment, metric, or dataset. It tells the author what to add.
- **Venue changes the stack, not the rigor.** _Radiology_-family submissions stop at the
  guideline checklist; Nature-portfolio submissions add a **Reporting Summary / Editorial
  Policy Checklist** on top of the same guideline stack (→ `nature-reporting-summary.md`) —
  never treat the Reporting Summary as a replacement for CLAIM/TRIPOD+AI/CLEAR.

## When to use

- "Which checklist does my study need?" / "What will _Radiology_ require at submission?"
- "Audit this manuscript against CLAIM / TRIPOD+AI / STARD / CLEAR / METRICS / RQS."
- "Is my radiomics pipeline reported reproducibly (IBSI)?"
- "Fill in the CLAIM checklist with page numbers."
- "What's my risk-of-bias exposure under PROBAST+AI / QUADAS-3?"
- "Which checklist applies to a guideline/consensus, qualitative/mixed-methods, economic evaluation,
  implementation study or PPI report?"
- Pre-submission self-audit, or triaging a reviewer comment that cites a guideline.

## Routing — pick the guideline(s) before auditing

Most imaging-AI papers need **two or more** of these (a reporting guideline **and** a
quality/risk-of-bias tool).

| Study type | Primary reporting guideline | Add for quality / risk-of-bias |
|---|---|---|
| AI/ML system in medical imaging (any task) | **CLAIM 2024** | TRIPOD+AI if it is a prediction model; DECIDE-AI for early clinical decision-support |
| Diagnostic/prognostic **prediction model** (incl. ML/DL) | **TRIPOD+AI (2024)** (+ TRIPOD-Cluster, TRIPOD+AI for Abstracts) | **PROBAST / PROBAST+AI (2025)** (risk of bias) |
| **Radiomics** (hand-crafted features → model) | **CLEAR (2023)** for reporting | **METRICS (2024)** and/or **RQS / RQS 2.0** for quality; **IBSI** for feature reproducibility |
| **Diagnostic accuracy** (test vs reference standard) | **STARD 2015**; **STARD-AI (2025)** when the index test is AI | **QUADAS-3 v1.2** when primary-study accuracy estimates are appraised in a review |
| **DTA systematic review / meta-analysis** | **PRISMA-DTA (2018)** | **QUADAS-3 v1.2** per selected accuracy estimate; for within-study comparisons of two or more index tests, apply **QUADAS-C alongside QUADAS-3** using the QUADAS-3 E&E adaptation guidance |
| Systematic review / meta-analysis (general) | **PRISMA 2020** | AMSTAR-2; ROBIS |
| Scoping review / evidence map | **PRISMA-ScR (2018)** | critical appraisal only if performed and justified; AMSTAR-2/ROBIS do not replace the reporting checklist |
| Systematic-review or meta-analysis protocol | **PRISMA-P (2015)** | protocol reporting only; registration/freeze and review conduct remain with `radiology-systematic-review` |
| Living systematic review | **PRISMA 2020 + PRISMA-LSR (2024)** | update surveillance, changed-study ledger, transition/retirement and tailored flow |
| Review of outcome measurement instruments | **PRISMA-COSMIN for OMIs (2024)** | only when measurement properties/instruments are the review object; use design-matched COSMIN appraisal |
| Observational (cohort/case-control/cross-sectional) | **STROBE** | (REMARK for tumour-marker prognostic studies) |
| Randomised trial of an imaging/AI intervention | **CONSORT 2025** (+ CONSORT-AI 2020 extension) | protocol: **SPIRIT 2025** (+ SPIRIT-AI 2020) |
| Imaging biomarker / quantitative imaging | QIBA Profile reporting + STARD/TRIPOD as applicable | IBSI; phantom/repeatability (QIBA) |
| Practice guideline / biomedical consensus | **RIGHT 2017** / **ACCORD 2024** | **AGREE II** appraises guideline quality; recommendation methods stay with `radiology-consensus-guideline` |
| Qualitative / mixed methods | **COREQ** for interviews/focus groups or **SRQR** for broader qualitative work; add quantitative design guideline and integration reporting | method credibility/integration stay with `radiology-qualitative-mixed-methods` |
| Health economic evaluation | **CHEERS 2022** (+ current CHEERS-AI when applicable) | economic estimand/model/uncertainty stay with `radiology-health-economics` |
| Implementation study | **StaRI 2017** + design-specific guideline(s) | implementation determinants, strategies/outcomes and success stay with `radiology-translation` |
| Patient/public involvement report | **GRIPP2 2017** | actual involvement/decision impact stay with `radiology-design` |

> Open [`references/guideline-router.md`](references/guideline-router.md) for the full
> decision tree, including hybrid studies (e.g. a radiomics **prediction model** validated
> for **diagnostic accuracy** → CLEAR + TRIPOD+AI + STARD + IBSI) and Nature-portfolio venues
> (add the Reporting Summary on top of whichever stack applies).

## When to open extra files

| File | Open when |
|---|---|
| [references/guideline-router.md](references/guideline-router.md) | Choosing guideline(s); hybrid/edge-case study types; how guidelines stack; Nature-portfolio add-on; FUTURE-AI; TRIPOD-LLM |
| [references/claim-2024.md](references/claim-2024.md) | Auditing a medical-imaging AI paper against the CLAIM 2024 Update |
| [references/tripod-ai-probast.md](references/tripod-ai-probast.md) | Prediction-model reporting (TRIPOD+AI) and PROBAST / PROBAST+AI risk-of-bias |
| [references/clear-metrics-rqs.md](references/clear-metrics-rqs.md) | Radiomics reporting (CLEAR) and quality scoring (METRICS, RQS / RQS 2.0) |
| [references/ibsi-features.md](references/ibsi-features.md) | Making radiomic features reproducible/standardised (IBSI image processing + feature nomenclature) |
| [references/stard-prisma-quadas.md](references/stard-prisma-quadas.md) | Diagnostic-accuracy reporting (STARD), DTA reviews (PRISMA-DTA), and current risk-of-bias/applicability assessment (QUADAS-3 v1.2; QUADAS-C alongside it for comparative accuracy) |
| [references/prisma-general-scoping.md](references/prisma-general-scoping.md) | General reviews (PRISMA 2020), protocols (PRISMA-P), scoping reviews/evidence maps (PRISMA-ScR), search reporting (PRISMA-S), living reviews (PRISMA-LSR), and measurement-instrument reviews (PRISMA-COSMIN for OMIs) |
| [references/radiology-submission-map.md](references/radiology-submission-map.md) | Mapping checklist items to where they belong in a _Radiology_ manuscript + submission logistics |
| [references/nature-reporting-summary.md](references/nature-reporting-summary.md) | Target is a Nature-portfolio journal — completing the Reporting Summary / Editorial Policy Checklist alongside the primary guideline stack |
| [references/guideline-consensus-qualitative-economic-implementation.md](references/guideline-consensus-qualitative-economic-implementation.md) | Guideline/consensus, qualitative/mixed-methods, health-economics, implementation or PPI reporting; distinguishes reporting from method/appraisal/success |

## Workflow

1. **Classify the study.** Determine task (classification / detection / segmentation /
   prediction / diagnostic accuracy / discovery), data provenance, whether a model is
   developed and/or validated, whether the endpoint is accuracy, prognosis, biology, implementation
   or economics, and whether the output is a guideline/consensus or qualitative/mixed-method report.
2. **Select and verify guideline(s)** from the routing table. State the official source,
   version/update date, and access date. If the study is
   hybrid, select the stack and say why each applies.
3. **Load the relevant reference file(s)** and audit **every item**. For each item record:
   `Item ID | Requirement (short) | Status (PRESENT/PARTIAL/MISSING/NA) | Location | Fix | Owner | Closure evidence`.
4. **Prioritise fixes.** Group into `Blocker` (will trigger major revision / desk reject),
   `Should-fix` (reviewer will likely ask), `Polish`. Tie each blocker to the specific
   reviewer risk.
5. **Cross-check integrity hot-spots** (see below) — the items reviewers weaponise most.
6. **If the target is a Nature-portfolio venue**, also complete the Reporting Summary /
   Editorial Policy Checklist (`nature-reporting-summary.md`) — additive, not a substitute.
7. **Return** the filled checklist + a one-screen executive summary + the prioritised fix
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
  describe the clinical spectrum (STARD spectrum bias; QUADAS-3 Participants domain).
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
2. **`Guideline provenance`** — official source/checklist, version/update date, access date,
   target-journal overlay, and any item marked `VERIFY_FROM_CURRENT_SOURCE`.
3. **`Checklist`** — a table with `Item | Status | Location | Fix | Owner | Closure evidence` for
   every item of each selected guideline. Use `NA` only with a one-line justification. An owner is
   accountable for supplying the named closure evidence; assignment alone never closes an item.
4. **`Compliance summary`** — counts (`PRESENT / PARTIAL / MISSING / NA`) per guideline and
   an overall readiness read (e.g. "CLAIM 31/44 present; 4 blockers").
5. **`Prioritised fixes`** — `Blocker / Should-fix / Polish`, each tied to the reviewer risk
   and the manuscript location to edit.
6. **`Author input needed`** — questions only the authors can answer (e.g. "Was the test set
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
- Data/code availability wording, DICOM de-identification, Extended Data/Source Data → `radiology-data`.
- Radiogenomics-specific design/leakage → `radiology-radiogenomics`.
- Figure that proves an item (ROC, calibration, flow diagram) → `radiology-figure`.
- Table that proves an item (cohort, regression, performance, feature audit) → `radiology-table`.
- Explainability/uncertainty items for a DL model → `radiology-deep-learning/interpretability-uncertainty.md`.
- Checklist complete; want a full adversarial pre-submission read → `radiology-prereview`.
- Guideline/consensus recommendation development → `radiology-consensus-guideline`; qualitative/
  mixed-method execution → `radiology-qualitative-mixed-methods`; economic model/HTA plan →
  `radiology-health-economics`; implementation evaluation → `radiology-translation`.
- Final upload package/checklist location audit → `radiology-submission` / `radiology-pipeline`.
