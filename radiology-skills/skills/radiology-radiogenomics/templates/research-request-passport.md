# Research Request Passport

Use this passport at intake or when a project changes direction. Replace every
`[AUTHOR_INPUT_NEEDED: ...]` field with supplied information. Do not infer missing cohort counts,
matching, timing, treatment exposure, approvals, accessions, results, or validation status. If a
field does not apply, write `not applicable` and the reason.

## 1. Request identity

| Field | Entry |
|---|---|
| Project or manuscript identifier | [AUTHOR_INPUT_NEEDED: project identifier] |
| Task token | [AUTHOR_INPUT_NEEDED: idea-feasibility / protocol-design / pipeline-qc / analysis-interpretation / biological-validation / statistics-sap / manuscript-review / writing-revision / revision-verification / submission-rebuttal / evidence-trace] |
| Writing job, if applicable | [AUTHOR_INPUT_NEEDED: not-applicable / argument-map / section-draft / scientific-rewrite / evidence-compression / language-polish-handoff / consistency-audit] |
| Manuscript section, if applicable | [AUTHOR_INPUT_NEEDED: not-applicable / title / abstract / introduction / methods / results / figure-legend / discussion / conclusion / supplement / full-manuscript] |
| Submission phase, if applicable | [AUTHOR_INPUT_NEEDED: not-applicable / initial / post-decision] |
| Interaction mode | [AUTHOR_INPUT_NEEDED: reviewer / mentor / combined] |
| Study scope | [AUTHOR_INPUT_NEEDED: imaging-only / mechanism-only / imaging-mechanism] |
| Current project stage | [AUTHOR_INPUT_NEEDED: idea / feasibility / protocol / data / analysis / results / manuscript / revision / submission] |
| Active modalities | [AUTHOR_INPUT_NEEDED: measured or actual analysis/design targets] |
| External reference modalities | [AUTHOR_INPUT_NEEDED: atlas/reference-only modalities or none] |
| Generated or predicted modalities | [AUTHOR_INPUT_NEEDED: imputed/mapped/deconvolved/generated/predicted layers or none] |
| Proposed validation modalities | [AUTHOR_INPUT_NEEDED: future assays not yet active or none] |
| Immediate decision to support | [AUTHOR_INPUT_NEEDED: decision that this request must resolve] |
| Requested deliverable | [AUTHOR_INPUT_NEEDED: exact output artifact] |
| Input evidence | [AUTHOR_INPUT_NEEDED: user-description / manuscript-prose-or-figure / summary-results / processed-data / raw-data-plus-code] |
| Intended audience | [AUTHOR_INPUT_NEEDED: learner / investigator / reviewer] |
| Intended venue, if relevant | [AUTHOR_INPUT_NEEDED: journal, committee, or state unknown] |
| Output language and carrier | [AUTHOR_INPUT_NEEDED: language and Markdown / Word-ready text / LaTeX / other] |
| Learner experience, if relevant | [AUTHOR_INPUT_NEEDED: training level and areas needing explanation] |

## 2. Scientific frame

| Field | Entry |
|---|---|
| Disease and clinical setting | [AUTHOR_INPUT_NEEDED: disease, stage, care setting] |
| Population | [AUTHOR_INPUT_NEEDED: eligibility, exclusions, recruitment source] |
| Imaging phenotype | [AUTHOR_INPUT_NEEDED: modality, sequence, ROI, radiomic/deep/habitat phenotype] |
| Mechanistic layer | [AUTHOR_INPUT_NEEDED: pathology, DNA, bulk RNA, single-cell, spatial, perturbation, other] |
| Clinical endpoint | [AUTHOR_INPUT_NEEDED: endpoint definition and assessment time] |
| Primary estimand or question | [AUTHOR_INPUT_NEEDED: precise comparison or association and target population] |
| Intended claim class | [AUTHOR_INPUT_NEEDED: technical-validity / descriptive / association / localization-or-concordance / prognostic-prediction / average-treatment-effect / effect-modification / mechanistic / causal] |
| Primary hypothesis | [AUTHOR_INPUT_NEEDED: prespecified hypothesis or state that the work is exploratory] |
| Main competing explanation | [AUTHOR_INPUT_NEEDED: plausible alternative biological or technical explanation] |

## 3. Data topology and matched counts

Record actual available counts, not planned counts. `Matched n` means that the required modalities
refer to the same inferential entity at a compatible lesion, region, and time point.

| Data layer | Source or accession | Total available n | QC-usable n | Matched n for this question | Inferential unit | Repeated-unit hierarchy | Site/platform/batch |
|---|---|---:|---:|---:|---|---|---|
| Imaging | [AUTHOR_INPUT_NEEDED: source] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: patient / lesion / region] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: site, scanner, protocol] |
| Pathology | [AUTHOR_INPUT_NEEDED: source] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: patient / lesion / block / section / field] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: laboratory, staining, scanning batch] |
| Bulk or targeted RNA | [AUTHOR_INPUT_NEEDED: source] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: patient / lesion / sample] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: center, assay, library batch] |
| scRNA/snRNA | [AUTHOR_INPUT_NEEDED: source] | [AUTHOR_INPUT_NEEDED: patients and cells] | [AUTHOR_INPUT_NEEDED: patients and cells] | [AUTHOR_INPUT_NEEDED: patient-level matched n] | [AUTHOR_INPUT_NEEDED: patient, with cells nested within patient] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: platform and batch] |
| Spatial omics | [AUTHOR_INPUT_NEEDED: source] | [AUTHOR_INPUT_NEEDED: patients, sections, spots/cells] | [AUTHOR_INPUT_NEEDED: patients, sections, spots/cells] | [AUTHOR_INPUT_NEEDED: patient/lesion/region matched n] | [AUTHOR_INPUT_NEEDED: patient / lesion / section, with spots or cells nested] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: platform and batch] |
| Other molecular or functional assay | [AUTHOR_INPUT_NEEDED: layer and source] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: site/platform/batch] |
| External validation | [AUTHOR_INPUT_NEEDED: source] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: matched n] | [AUTHOR_INPUT_NEEDED: unit] | [AUTHOR_INPUT_NEEDED: hierarchy] | [AUTHOR_INPUT_NEEDED: independence from discovery data] |

### Limiting denominator

| Count | Value and derivation |
|---|---|
| Patient-level matched n | [AUTHOR_INPUT_NEEDED: n and intersection rule] |
| Lesion-level matched n | [AUTHOR_INPUT_NEEDED: n and mapping rule] |
| Region/block/section-level matched n | [AUTHOR_INPUT_NEEDED: n and mapping rule] |
| Complete-case n for the primary analysis | [AUTHOR_INPUT_NEEDED: n and missingness exclusions] |
| Independent validation n | [AUTHOR_INPUT_NEEDED: n or state that none exists] |
| Primary power-limiting count | [AUTHOR_INPUT_NEEDED: count that constrains inference and why] |

## 4. Spatial, temporal, and treatment alignment

| Linkage | Spatial relationship | Acquisition/sampling time | Treatment exposure between measurements | Compatibility verdict |
|---|---|---|---|---|
| Imaging ↔ pathology | [AUTHOR_INPUT_NEEDED: patient, lesion, region, habitat, block, section mapping] | [AUTHOR_INPUT_NEEDED: dates or intervals] | [AUTHOR_INPUT_NEEDED: exposure] | [AUTHOR_INPUT_NEEDED: aligned / partially aligned / not aligned / unknown] |
| Imaging ↔ transcriptomics | [AUTHOR_INPUT_NEEDED: mapping] | [AUTHOR_INPUT_NEEDED: dates or intervals] | [AUTHOR_INPUT_NEEDED: exposure] | [AUTHOR_INPUT_NEEDED: aligned / partially aligned / not aligned / unknown] |
| Transcriptomics ↔ pathology/functional assay | [AUTHOR_INPUT_NEEDED: mapping] | [AUTHOR_INPUT_NEEDED: dates or intervals] | [AUTHOR_INPUT_NEEDED: exposure] | [AUTHOR_INPUT_NEEDED: aligned / partially aligned / not aligned / unknown] |

## 5. Evidence inventory

Use only these evidence states: `measured`, `derived`, `estimated`, `associated`, `predicted`,
`perturbed`, or `missing`. Put a proposed future assay in `missing` and describe the proposal in the
available-observation or uncertainty field.

| Evidence layer | Available observation | Status | Source pointer | Main uncertainty |
|---|---|---|---|---|
| Imaging phenotype | [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: file, figure, table, or dataset] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Tissue structure | [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Cell source or state | [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Molecular programme | [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Functional or perturbational evidence | [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Clinical endpoint evidence | [AUTHOR_INPUT_NEEDED: observation] | [AUTHOR_INPUT_NEEDED: status] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: uncertainty] |

## 6. Design constraints and authority boundaries

| Constraint | Current state | Consequence for the question | Repair or boundary |
|---|---|---|---|
| Matching or provenance | [AUTHOR_INPUT_NEEDED: state] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Sample size and effective n | [AUTHOR_INPUT_NEEDED: state] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Scanner/site and omics batch | [AUTHOR_INPUT_NEEDED: state] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Multiplicity and model complexity | [AUTHOR_INPUT_NEEDED: state] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Validation | [AUTHOR_INPUT_NEEDED: state] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: repair/boundary] |
| Ethics, consent, controlled access | [AUTHOR_INPUT_NEEDED: state] | [AUTHOR_INPUT_NEEDED: consequence] | [AUTHOR_INPUT_NEEDED: institutional action or boundary] |

## 7. Intake decision

| Field | Entry |
|---|---|
| Entry route | [AUTHOR_INPUT_NEEDED: scoping / design audit / analysis audit / interpretation / manuscript review / revision] |
| Files or playbooks to load | [AUTHOR_INPUT_NEEDED: only the resources needed for this request] |
| Current verdict | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] |
| Claim ceiling | [AUTHOR_INPUT_NEEDED: strongest wording currently defensible] |
| Claim-changing stop condition | [AUTHOR_INPUT_NEEDED: condition that would force a weaker claim or halt analysis] |
| Minimum author inputs still required | [AUTHOR_INPUT_NEEDED: missing items that materially affect the decision] |
| Agreed output profile | [AUTHOR_INPUT_NEEDED: Reviewer / Mentor / Combined and selected artifacts] |

## 8. STOP rescue, if required

| Rescue element | Entry |
|---|---|
| Blocked question | [AUTHOR_INPUT_NEEDED: original question] |
| Blocking reason | [AUTHOR_INPUT_NEEDED: exact evidence or design failure] |
| Nearest answerable question | [AUTHOR_INPUT_NEEDED: bounded replacement question] |
| Minimum new evidence needed to restore the original question | [AUTHOR_INPUT_NEEDED: evidence] |
| Wording currently allowed | [AUTHOR_INPUT_NEEDED: evidence-bounded wording] |
