# Radiomics–Mechanism Reviewer Audit

Use this template for an integrated audit, not as evidence of multiple independent reviewers.
Every finding must identify the evidence location, consequence, and repair. Do not modify the source
unless the author separately requests revision.

## 1. Review contract

| Field | Entry |
|---|---|
| Project/manuscript identifier | [AUTHOR_INPUT_NEEDED: identifier] |
| Artifact and version reviewed | [AUTHOR_INPUT_NEEDED: filename/version/date] |
| Review mode | [AUTHOR_INPUT_NEEDED: full / focused / methods / mechanism / re-review] |
| Study scope | [AUTHOR_INPUT_NEEDED: imaging-only / mechanism-only / imaging-mechanism] |
| Review target | [AUTHOR_INPUT_NEEDED: protocol, analysis, figure, manuscript, response, or other] |
| Intended venue/audience | [AUTHOR_INPUT_NEEDED: venue/audience or state unknown] |
| Intended headline claim | [AUTHOR_INPUT_NEEDED: exact claim] |
| Intended claim class | [AUTHOR_INPUT_NEEDED: technical-validity / descriptive / association / localization-or-concordance / prognostic-prediction / average-treatment-effect / effect-modification / mechanistic / causal] |
| Primary inferential unit | [AUTHOR_INPUT_NEEDED: patient / lesion / region / block / section / other] |
| Primary matched n | [AUTHOR_INPUT_NEEDED: n and intersection definition] |
| Materials available to the reviewer | [AUTHOR_INPUT_NEEDED: files, tables, figures, data, code, protocols] |
| Materials not available | [AUTHOR_INPUT_NEEDED: missing materials affecting coverage] |

## 2. Executive judgement

| Field | Entry |
|---|---|
| Overall verdict | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] |
| Strongest valid contribution | [AUTHOR_INPUT_NEEDED: contribution preserved by the evidence] |
| Highest-risk defect | [AUTHOR_INPUT_NEEDED: defect and why it changes the claim] |
| Claim ceiling | [AUTHOR_INPUT_NEEDED: strongest defensible wording] |
| Claim-changing stop condition | [AUTHOR_INPUT_NEEDED: condition that forces a weaker claim or halt] |
| Blocking next action | [AUTHOR_INPUT_NEEDED: single action required before the decisive claim can advance] |
| Coverage boundary | [AUTHOR_INPUT_NEEDED: what this review did and did not verify] |

Verdict meanings:

- `PASS`: the audited claim is supported within the stated scope; remaining issues do not change it.
- `CONDITIONAL`: a usable claim remains, but specified analyses, disclosures, or wording changes are required.
- `STOP`: the requested claim is not identifiable or supportable from the present evidence.

## 3. Genuine strengths

List only strengths actually supported by an evidence anchor. There is no required number. Strengths
do not receive `P0/P1/P2`, which is a weakness-severity scale.

| Strength ID | Review lens | Typed evidence anchor | Strength | Why it matters | Preserve in revision |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: stable ID] | [AUTHOR_INPUT_NEEDED: lens] | [AUTHOR_INPUT_NEEDED: text/table/figure/dataset/code locator] | [AUTHOR_INPUT_NEEDED: strength] | [AUTHOR_INPUT_NEEDED: decision relevance] | [AUTHOR_INPUT_NEEDED: element] |

## 4. Evidence-linked findings

Use `P0`, `P1`, or `P2` severity from the shared integrity gates. Do not assign a numerical score
or translate severity mechanically into the scientific verdict. Use a typed anchor; for an absence,
name where the item should appear and which manuscript/data/code surfaces were checked. `Obligation`
is an editorial action class, not a fourth scientific verdict.

| Finding ID | Review lens | Class | Severity | Obligation | Typed evidence anchor | Problem | Governing criterion | Scientific consequence | Target-fit relevance | Claim affected/ceiling | Minimum feasible repair | Optional stronger route | Cost/trade-off | Verification criterion | Confidence/scope limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: stable ID] | [AUTHOR_INPUT_NEEDED: lens] | [AUTHOR_INPUT_NEEDED: defect / clarification-needed] | [AUTHOR_INPUT_NEEDED: P0 / P1 / P2] | [AUTHOR_INPUT_NEEDED: must-fix / should-fix / consider] | [AUTHOR_INPUT_NEEDED: text/table/figure/dataset/code/absence plus locator] | [AUTHOR_INPUT_NEEDED: one atomic problem] | [AUTHOR_INPUT_NEEDED: criterion] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: separate venue relevance or not applicable] | [AUTHOR_INPUT_NEEDED: claim ID and wording ceiling] | [AUTHOR_INPUT_NEEDED: smallest honest repair] | [AUTHOR_INPUT_NEEDED: separate optional route or none] | [AUTHOR_INPUT_NEEDED: data/sample/time/complexity/interpretability/generalizability burden] | [AUTHOR_INPUT_NEEDED: observable closure condition and evidence type] | [AUTHOR_INPUT_NEEDED: confidence/basis/limit] |

## 5. Review lenses

Mark each lens `APPLICABLE`, `NOT APPLICABLE`, or `NOT ASSESSED` before using it. Delete or omit
non-applicable detail rather than filling it with `missing`. `imaging-only` does not require omics or
a mechanism; `mechanism-only` does not require imaging or sample-to-image mapping;
`imaging-mechanism` requires both sides and the bridge.

The detailed lens tables below are coverage summaries, not an alternate finding channel. Every
`CONDITIONAL`/`STOP` or otherwise decision-bearing defect must cite a Section 4 Finding ID and retain
the full atomic contract there; do not create a new defect only inside a lens table.

| Lens | Coverage status | Reason / materials checked |
|---|---|---|
| Imaging validity | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Cohort, estimand and statistics | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Sample-to-image provenance | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Omics and pathology validity | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Mechanism and causal language | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Clinical validity and relevance | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Contribution, literature and argument | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |
| Writing, reporting and availability | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: reason/materials] |

### A. Imaging validity

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Acquisition, reconstruction, preprocessing | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Segmentation, registration, habitat definition | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Repeatability, stability, scanner/site sensitivity | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Train-only preprocessing and leakage control | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### B. Cohort, estimand, and statistics

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Eligibility and cohort flow | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Matched n versus total n | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Inferential unit and repeated observations | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Covariates, multiplicity, missing data, power | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Prediction versus treatment-benefit estimand | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### C. Sample-to-image provenance

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Patient and lesion identity | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Region/habitat to block/section mapping | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Timing and intervening treatment | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Spatial resolution compatibility | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### D. Omics and pathology validity

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Preanalytics, QC, normalization, batch | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Patient-aware single-cell/spatial inference | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Pathology assay controls and blinding | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Molecular/pathology endpoint definition | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### E. Mechanism and causal language

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Measured versus inferred links | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Competing biological explanations | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Technical/sampling explanation | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Discriminating or perturbational evidence | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### F. Clinical validity and relevance

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Endpoint validity and follow-up | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Baseline comparison, calibration, utility | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Internal versus external validation | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Generalisability and intended use | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### G. Writing, reporting, and availability

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Claim–evidence alignment | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Methods reproducibility and reporting standards | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Figure/table denominators and legends | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Data, code, accession, ethics statements | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

### H. Contribution, literature, and argument

| Check | Evidence summary and Finding ID(s) | Verdict | Repair/boundary |
|---|---|---|---|
| Defensible knowledge delta and significance | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Necessary, contrary and recent literature integrated | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Problem, gap, method, Results and conclusion coherent | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Method benefit versus complexity and failure modes | [AUTHOR_INPUT_NEEDED: evidence/finding] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: repair/boundary] |

## 6. Competing explanation audit

| Headline observation | Biological explanation 1 | Biological explanation 2 | Technical/sampling explanation | Discriminating test | Current conclusion |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: explanation] | [AUTHOR_INPUT_NEEDED: explanation] | [AUTHOR_INPUT_NEEDED: explanation] | [AUTHOR_INPUT_NEEDED: test] | [AUTHOR_INPUT_NEEDED: bounded conclusion] |

## 7. Preserve, repair, or retire

| Element | Disposition | Reason | Required action |
|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: claim, analysis, figure, or section] | [AUTHOR_INPUT_NEEDED: preserve / repair / retire] | [AUTHOR_INPUT_NEEDED: reason] | [AUTHOR_INPUT_NEEDED: action] |

## 8. STOP rescue, if required

| Rescue element | Entry |
|---|---|
| Blocked question or claim | [AUTHOR_INPUT_NEEDED: question/claim] |
| Blocking evidence | [AUTHOR_INPUT_NEEDED: evidence and pointer] |
| Nearest answerable question | [AUTHOR_INPUT_NEEDED: replacement question] |
| Minimum new evidence needed | [AUTHOR_INPUT_NEEDED: evidence] |
| Wording currently allowed | [AUTHOR_INPUT_NEEDED: wording] |

## 9. Author inputs required

| Missing input | Why it changes the decision | Who must provide it |
|---|---|---|
| [AUTHOR_INPUT_NEEDED: input] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: owner] |

## 10. Frozen criteria for any re-review

| Criterion ID | Source finding ID | Frozen criterion | Required evidence type | Observable closure condition | Original severity | Original obligation | Original claim ceiling | Original confidence/scope limit |
|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: stable criterion ID] | [AUTHOR_INPUT_NEEDED: finding ID] | [AUTHOR_INPUT_NEEDED: criterion] | [AUTHOR_INPUT_NEEDED: text/table/figure/dataset/code/experiment] | [AUTHOR_INPUT_NEEDED: closure condition] | [AUTHOR_INPUT_NEEDED: P0/P1/P2] | [AUTHOR_INPUT_NEEDED: must-fix/should-fix/consider] | [AUTHOR_INPUT_NEEDED: ceiling] | [AUTHOR_INPUT_NEEDED: confidence/basis/limit] |
