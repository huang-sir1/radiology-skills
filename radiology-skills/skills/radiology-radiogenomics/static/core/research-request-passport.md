# Research request passport

Build this passport before selecting a technical route. Mark each field `known`, `missing`, `inferred`, or
`not applicable`; never infer provenance from filenames, conventional practice, or a persuasive figure.

## Route declaration

State one compact, user-correctable line:

`mode | tutor style | scope | task | writing job/section when applicable | project stage | active and
role-grouped modalities | claim type | audience | artifact permission | simulation authorization |
deliverable`

Use these values where applicable:

| Axis | Values |
|---|---|
| Mode | unknown, reviewer, mentor, combined |
| Tutor style | provisional, direct-expert, guided-learning, or not-applicable |
| Scope | unknown, imaging-only compatibility handoff, mechanism-only, imaging-mechanism |
| Task | unknown, idea-feasibility, protocol-design, pipeline-qc, analysis-interpretation, biological-validation, statistics-sap, manuscript-review, writing-revision, revision-verification, submission-rebuttal, evidence-trace |
| Writing job | not-applicable, argument-map, section-draft, scientific-rewrite, evidence-compression, language-polish-handoff, consistency-audit |
| Manuscript section | not-applicable, title, abstract, introduction, methods, results, figure-legend, discussion, conclusion, supplement, full-manuscript |
| Submission phase | not-applicable, initial, post-decision |
| Stage | unknown, idea, feasibility, protocol, data, analysis, results, manuscript, revision, submission |
| Active modalities | measured or actual analysis/design targets: radiomics, bulk-rna, single-cell, spatial, pathology, deep-fusion, multi-omics, other-omics, perturbation |
| External references | atlases or public references used only for annotation, nomination or context |
| Generated/predicted layers | imputed, mapped, deconvolved, generated or predicted modalities; may also be active when audited |
| Proposed validations | future assays not yet active unless the user requests an executable design for them |
| Claim | unknown/provisional, technical-validity, descriptive, association, localization-or-concordance, prognostic-prediction, average-treatment-effect, effect-modification, mechanistic, causal |
| Input evidence | unknown, user-description, manuscript-prose-or-figure, summary-results, processed-data, raw-data-plus-code |
| Audience | unknown, learner, investigator, reviewer; record a specific journal/editorial venue separately |
| Artifact permission | read-only by default; authorized-write only when the user requests a persistent artifact |
| Simulation authorization | not-authorized by default; explicitly-authorized only for the named current-task scope |

Multiple biological layers and writing sections may be active. Do not let a downstream label such as
`niche`, `virtual knockout`, or `treatment response` bypass upstream assay, mapping, or inference checks.

## Scientific passport

Capture the minimum facts that can change the route:

| Domain | Required facts |
|---|---|
| Question | population, biological phenomenon, contrast/exposure, endpoint, time, intended use and claim |
| Cohort | patients, lesions, samples, repeated measures, sites, exclusions, matched counts and validation role |
| Imaging | modality/sequence/tracer, timing, ROI, phenotype definition, acquisition, segmentation and stability |
| Tissue/omics | specimen, lesion/region, block/section, assay layer, raw versus processed access, QC and batch |
| Mapping | patient-lesion-region-time chain, treatment interval, registration or sampling uncertainty |
| Analysis | estimand, covariates, multiplicity, split, train-only operations, baselines and missingness |
| Evidence | inspected files/tables/figures/code, supplied assertions, unavailable artifacts and external validation |
| Delivery | requested decision, teaching depth, writing section, format, journal or resource constraints |
| Learner | interaction style, objective, baseline attempt, misconception IDs, mastery evidence/state and next transfer task |

Report matched counts at every relevant intersection, not only total cohort counts. Distinguish data that
exist from data the user could realistically acquire.

Keep this passport in the response for advisory work. Do not create or update a passport file merely
because the user asked for tutoring, review or planning.

## Alignment gate

Proceed without interrogation when the question, evidence, and boundary are clear. Ask at most two or
three targeted questions only when an ambiguity would change the estimand, route, validity verdict, or
major deliverable. If the user elects to proceed without the missing fact, provide a bounded scaffold or
conditional route and record the assumption; do not manufacture a complete study.
