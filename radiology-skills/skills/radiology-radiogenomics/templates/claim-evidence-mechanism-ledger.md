# Claim–Evidence–Mechanism Ledger

Create one row per atomic claim. Split compound claims before judging them. Preserve the exact
inferential unit, spatial mapping, timing, treatment context, and matched denominator. A real
citation is not sufficient unless it supports the stated claim in the stated context.

## 1. Ledger scope

| Field | Entry |
|---|---|
| Project or manuscript identifier | [AUTHOR_INPUT_NEEDED: identifier] |
| Artifact and version audited | [AUTHOR_INPUT_NEEDED: filename/version/date] |
| Evidence cut-off | [AUTHOR_INPUT_NEEDED: date or version boundary] |
| Intended audience or venue | [AUTHOR_INPUT_NEEDED: audience/venue] |
| Study scope | [AUTHOR_INPUT_NEEDED: imaging-only / mechanism-only / imaging-mechanism] |
| Active modalities | [AUTHOR_INPUT_NEEDED: modalities that produced evidence in this study] |
| Primary inferential unit | [AUTHOR_INPUT_NEEDED: patient / lesion / region / block / section / other] |
| Primary matched n | [AUTHOR_INPUT_NEEDED: n and intersection definition] |
| Reviewer or author responsible for adjudication | [AUTHOR_INPUT_NEEDED: role or name] |

## 2. Claim registry

| Claim ID | Exact claim | Location | Claim class | Importance | Unit | Spatial scope | Time/treatment context |
|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: stable ID] | [AUTHOR_INPUT_NEEDED: one atomic claim] | [AUTHOR_INPUT_NEEDED: section, paragraph, figure, table, or line] | [AUTHOR_INPUT_NEEDED: technical-validity / descriptive / association / localization-or-concordance / prognostic-prediction / average-treatment-effect / effect-modification / mechanistic / causal] | [AUTHOR_INPUT_NEEDED: headline / major / supporting] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: scope] | [AUTHOR_INPUT_NEEDED: context] |

Add rows without changing existing claim IDs.

## 3. Claim-level evidence ledger

Allowed positive primary evidence states are `measured`, `derived`, `estimated`, `associated`,
`predicted`, or `perturbed`. Use `missing` only as an explicit absence marker for evidence that does
not exist; it is not a seventh primary state and must pair with a `proposed` acquisition/link plan.
Record the relationship from an evidence item to the claim separately as `direct`, `inferred`, or `proposed`;
an inferred relationship is not an evidence-production state.

Issue severity and gate verdict answer different questions and must remain separate: `P0 / P1 / P2`
classifies the impact of a problem, whereas `PASS / CONDITIONAL / STOP` judges whether the claim
can pass the current evidence gate. Neither field may be replaced by a support score or another
verdict scale.

| Claim ID | Direct evidence and effect direction | Source pointer and locator | Primary evidence state | Modality subtype | Claim-link status | Analysed n / eligible n | Matched n | Main inferred link | Competing explanation | Technical/confounding explanation | Issue severity (P0/P1/P2) | Gate verdict (PASS/CONDITIONAL/STOP) | Claim ceiling | Allowed wording | Next discriminating evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: claim ID] | [AUTHOR_INPUT_NEEDED: result, comparison, uncertainty, direction] | [AUTHOR_INPUT_NEEDED: data/table/figure/citation plus locator] | [AUTHOR_INPUT_NEEDED: measured / derived / estimated / associated / predicted / perturbed; use missing only as an absence marker] | [AUTHOR_INPUT_NEEDED: operation or assay-specific subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: numerator and denominator] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: inference] | [AUTHOR_INPUT_NEEDED: biological alternative] | [AUTHOR_INPUT_NEEDED: relevant batch, sampling, purity, volume, segmentation, scanner, annotation, model, or other alternative] | [AUTHOR_INPUT_NEEDED: P0 / P1 / P2] | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] | [AUTHOR_INPUT_NEEDED: strongest defensible claim] | [AUTHOR_INPUT_NEEDED: manuscript-ready wording] | [AUTHOR_INPUT_NEEDED: observation or experiment that separates explanations] |

## 4. Cross-scale mechanism chain

Complete one scope-appropriate block for every headline or major mechanism claim. Use the
`mechanism-only` block when imaging is not active evidence; do not add placeholder imaging
phenotypes, acquisition physics, scanner variables, or image-to-tissue mappings. Use the
`imaging-mechanism` block only when the claim actually connects imaging to biology. In either
block, record primary evidence state, modality subtype, and claim-link status independently.

### Mechanism-only claim [AUTHOR_INPUT_NEEDED: claim ID]

Use when `Study scope = mechanism-only`. Add or delete biological rows to match the study while
preserving the actual evidence chain; do not retain a non-applicable row merely to complete the
table. An absent imaging layer is not a missing-data item.

| Link | Observation or proposition | Primary evidence state | Modality subtype | Claim-link status | Inferential unit | Matched n | Evidence pointer | Missing link or uncertainty |
|---|---|---|---|---|---|---:|---|---|
| Biological or clinical anchor | [AUTHOR_INPUT_NEEDED: disease state, exposure, treatment, phenotype, or endpoint] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: cohort, clinical assay, bulk RNA, sc/snRNA, spatial, pathology, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Tissue architecture/process | [AUTHOR_INPUT_NEEDED: process] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: H&E, IHC, mIF, WSI-derived, spatial morphology, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Cell source/state | [AUTHOR_INPUT_NEEDED: source/state] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: scRNA-seq, snRNA-seq, deconvolution, cytometry, lineage assay, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Molecular programme | [AUTHOR_INPUT_NEEDED: programme] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: bulk RNA, gene set score, regulon, proteomics, metabolomics, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Spatial or neighbourhood organization | [AUTHOR_INPUT_NEEDED: organization] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: spot-based, imaging-based, spatial domain, neighbourhood, ligand-receptor, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Functional/perturbational link | [AUTHOR_INPUT_NEEDED: functional or intervention evidence] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: genetic perturbation, drug perturbation, organoid, animal model, longitudinal response, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Clinical consequence | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: diagnosis, response, survival, toxicity, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |

### Imaging–mechanism claim [AUTHOR_INPUT_NEEDED: claim ID]

Use only when `Study scope = imaging-mechanism`.

| Link | Observation or proposition | Primary evidence state | Modality subtype | Claim-link status | Inferential unit | Matched n | Evidence pointer | Missing link or uncertainty |
|---|---|---|---|---|---|---:|---|---|
| Imaging phenotype | [AUTHOR_INPUT_NEEDED: phenotype] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: handcrafted feature, embedding, saliency, habitat, longitudinal delta, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Physical or acquisition basis | [AUTHOR_INPUT_NEEDED: basis] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: sequence, tracer, phase, reconstruction, physical model, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Tissue architecture/process | [AUTHOR_INPUT_NEEDED: process] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: H&E, IHC, mIF, WSI-derived, spatial morphology, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Cell source/state | [AUTHOR_INPUT_NEEDED: source/state] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: scRNA-seq, snRNA-seq, deconvolution, cytometry, lineage assay, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Molecular programme | [AUTHOR_INPUT_NEEDED: programme] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: bulk RNA, gene set score, regulon, proteomics, metabolomics, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Functional/perturbational link | [AUTHOR_INPUT_NEEDED: evidence] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: genetic perturbation, drug perturbation, organoid, animal model, longitudinal response, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Clinical consequence | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: diagnosis, response, survival, toxicity, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |

## 5. Contradiction and negative-evidence register

| Claim ID | Contradictory or null evidence | Source pointer | Does it change the claim? | Required action |
|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: claim ID] | [AUTHOR_INPUT_NEEDED: evidence] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: yes / no / uncertain and why] | [AUTHOR_INPUT_NEEDED: revise, analyse, disclose, or retain] |

## 6. Claim disposition summary

This is an editing action register, not an additional evidence verdict. The only evidence-gate
verdict remains `PASS / CONDITIONAL / STOP`.

| Claim ID | Retain / weaken / remove / investigate | Final claim ceiling | Final wording | Unresolved author decision |
|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: claim ID] | [AUTHOR_INPUT_NEEDED: disposition] | [AUTHOR_INPUT_NEEDED: ceiling] | [AUTHOR_INPUT_NEEDED: wording] | [AUTHOR_INPUT_NEEDED: decision or state none] |

## 7. Global integrity gate

| Check | Result |
|---|---|
| Every headline claim is registered | [AUTHOR_INPUT_NEEDED: yes / no with missing claims] |
| Every numerical statement has a source pointer | [AUTHOR_INPUT_NEEDED: yes / no with gaps] |
| Citation existence has been checked separately from claim support | [AUTHOR_INPUT_NEEDED: yes / no / not checked] |
| Measured and inferred links are visibly separated | [AUTHOR_INPUT_NEEDED: yes / no with gaps] |
| Alternative explanations are addressed | [AUTHOR_INPUT_NEEDED: yes / no with gaps] |
| Matched denominators and unknown states remain visible | [AUTHOR_INPUT_NEEDED: yes / no with gaps] |
| Global gate verdict | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] |
| Claim-changing stop condition | [AUTHOR_INPUT_NEEDED: condition] |

## 8. STOP rescue, if required

`[AUTHOR_INPUT_NEEDED: blocked claim]` → `[AUTHOR_INPUT_NEEDED: blocking reason]` →
`[AUTHOR_INPUT_NEEDED: nearest defensible claim]` →
`[AUTHOR_INPUT_NEEDED: minimum new evidence]` →
`[AUTHOR_INPUT_NEEDED: wording currently allowed]`
