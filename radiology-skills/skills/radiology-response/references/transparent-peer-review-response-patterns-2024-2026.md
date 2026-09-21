# Transparent peer-review response patterns, 2024–2026

Use this reference to calibrate response strategy against the screened public exchanges paired with
recent high-impact biomedical papers. It is a response-writing evidence source, not proof that every
reviewer request is correct or that publication validates every claim.

## Evidence unit and limitations

The accepted unit is:

`published paper + official reviewer report + official author response + page-aligned concern/action`.

Paper-level counts use one DOI as the denominator, not the number of comments. This is a deliberate,
criterion-sampled corpus of published papers with full public reviewer reports and author responses.
That design is fit for its intended purpose: observing how real concerns were framed, what authors
actually did, how revisions were documented and what closure evidence accompanied publication. Use
it directly for qualitative response strategy and do not attach a generic “selection bias” warning
to ordinary case-guided advice.

Activate a denominator boundary only for population-rate or causal questions. The corpus does not
contain all submissions or a rejected-manuscript comparison set, so it cannot estimate how often all
reviewers make a request, explain general causes of rejection, calculate acceptance probability, or
identify which private editorial discussion caused acceptance. Public review files may omit
confidential editor/reviewer communication. Check corrections, editor's notes and retractions
separately; transparent review is not a clean-paper certificate.

Keep three evidence types distinct in every output: a **formal journal requirement** from current
official guidance, a **recurrent empirical pattern** across several exchanges, and a **case-derived
example** from one concern–action–closure record. All three can guide a response, but only the first
may be presented as the journal's rule.

The synchronized [response evidence map](transparent-peer-review-response-map-2024-2026.tsv)
contains 100 unique 2024-08-22–2026-08-22 records: Nature 12, Nature Methods 22,
Nature Genetics 15, Nature Biomedical Engineering 11, Nature Medicine 2 and Nature Communications 38.
Its primary strata are imaging AI 30, spatial 34, digital pathology 9, multi-omics 8, perturbation 4,
imaging–mechanism 6, single-cell 7, radiomics 1 and bulk RNA 1. The last two strata support examples,
not modality-level frequency claims. The synchronized corpus has no historical-impact exception;
every record meets the frozen Nature/major-specialist/current-JIF>=10 venue rule.

The map preserves source-level `concern_codes` for provenance and also carries ontology v1.0.0 plus
deduplicated `canonical_concern_families`. Use canonical families for cross-paper routing or
frequency; use raw codes only to recover the exact source-level issue. Neither level is an
acceptance-probability model.

For analysis, the corpus assigns one decisive request class per paper: 67 manuscript-grounded
defects, 24 clarification-needed items, 5 reviewer preferences, 4 optional strengthening requests and
0 scope-contested/infeasible requests. These are local evidence-map classifications, not publisher
labels or the distribution of all comments in the review files.

The one-time 2026-08-22 post-publication screen found 97 records without a targeted official notice
signal, 2 with linked author corrections and 1 (TPR059) with an Editor's Note describing an ongoing
reliability investigation. Do not use TPR059 as a model of scientific correctness. Use it, if needed,
only to study response structure while displaying the notice; absence of a detected notice is not a
clean-paper finding.

## What strong author responses actually do

Across the inspected exchanges, a credible response is a small evidence package:

1. identify the exact scientific criterion behind the comment;
2. state whether the authors agree, partly agree, contest or cannot complete the request;
3. describe the actual analysis, experiment, reporting correction or claim reduction;
4. report the resulting estimate, direction, benchmark, negative finding or functional readout;
5. identify the exact revised text, figure, table, method or supplement location;
6. disclose what remains unresolved and keep the claim within that boundary.

Use a **result-before-location** test: after an author claims an analysis or experiment was performed,
the next substantive unit must report what happened before the paragraph relies on a page, line or
figure locator. A locator proves where to inspect a change; it does not prove that the scientific
criterion was met.

This is stronger than courtesy-first boilerplate. Appreciation may open the paragraph, but it cannot
replace the action, result and location.

## Request-class calibration

| Request class | Appropriate response |
|---|---|
| Manuscript-grounded defect | accept or partially accept; repair/reanalyse/validate or narrow the affected claim; show closure evidence |
| Clarification needed | expose the existing design/result or add reconstructable reporting; answer the precise ambiguity |
| Optional strengthening | state whether adopted; if declined, explain cost/scope and why the current claim remains valid |
| Reviewer preference | test the named assumptions or add a proportionate sensitivity analysis; do not replace a valid method merely from preference |
| Scope-contested or infeasible | give evidence-based pushback, the nearest feasible analysis or wording boundary, and the residual limitation |

The language of the comment does not determine the class. A reviewer may phrase optional future work
strongly; an apparently minor wording request may expose a decision-bearing claim defect.

## Recurrent concern-to-response patterns

| Concern family | Response evidence expected |
|---|---|
| Fair benchmark or comparator | comparator eligibility, matched data/splits/tuning, actual comparative result and affected claim |
| Ablation or attribution | component removed/changed, metric with uncertainty, conclusion limited to supported components |
| Unit, replication and sample size | biological unit and hierarchy, corrected model or bounded inference; more cells/tiles do not answer donor/patient replication |
| External validation and distribution shift | frozen object, independent site/platform/cohort, metric/failure result, or explicit discovery-only wording |
| Ground truth, QC and preprocessing | acquisition/assay/annotation reference, thresholds/versions, sensitivity and downstream result |
| Statistics and robustness | estimand, appropriate test/model, multiplicity/uncertainty, sensitivity result and changed interpretation |
| Mechanism and alternatives | discriminating evidence, target engagement/control/rescue when required, or claim reduction from causal/mechanistic language |
| Spatial resolution and mapping | physical resolution, segmentation/registration error, spatial null and patient/region boundary |
| Reproducibility and availability | actual repository/accession/code/model artifact, version and restriction; never a promised-but-unmade deposit |
| Novelty and relevance | precise knowledge delta against applicable prior work; no novelty-by-tool-combination or impact rhetoric without evidence |

## Legitimate response strategies

- **Analysis/experiment added:** give method, result and location; show whether the claim survived,
  weakened or failed.
- **Evidence/reporting added:** expose an existing but previously hidden result or reconstruction detail;
  do not imply new data were collected.
- **Text/claim revised:** quote the bounded revised wording and update every dependent title, abstract,
  Results, Discussion, legend and conclusion location.
- **Evidence-based pushback:** identify the inapplicable premise or factual misreading, cite manuscript
  evidence, and add a clarification/sensitivity when it prevents the next reader from repeating the
  misunderstanding.
- **Declined with explicit boundary:** state infeasibility, what was done instead, the limitation and
  the claim no longer made.

The coded closure states are 32 experiment-or-analysis added, 31 analysis-or-evidence added,
24 text-or-claim revised, 2 author-response documented, 2 partially addressed, 4 reviewer confirmed,
1 evidence-based pushback
and 4 declined with an explicit boundary. These states describe the selected decisive issue, not the
entire revision and not a recommendation to default to new experiments.

When one dominant response architecture is assigned for analysis, the map yields 49 accept-and-repair,
24 clarify/rewrite, 22 partially accept and 5 evidence-based contest/infeasibility routes. The rule is
forced onto mixed responses to support teaching; it is not a publisher label and does not estimate
which strategy causes acceptance.

### Four response architectures

| Author decision | Required paragraph architecture | Closure test | Public-record anchors |
|---|---|---|---|
| Accept and repair | acknowledge the criterion -> name method/operation -> report result, including negative result -> state changed claim -> exact location | the repaired artifact can be found and the result answers every required child commitment | TPR095 published RNA baselines; TPR097 known-ground-truth simulation; TPR098 omitted comparator; TPR099 null calibration |
| Clarify or expose existing evidence | identify the ambiguity -> distinguish existing from new evidence -> add reconstructable detail/result -> quote or locate revision | an independent reader can reconstruct the design or find the previously hidden evidence | use records classified `clarification-needed`; do not imply data collection |
| Partially accept | agree with the valid premise -> define the unsupported extension -> perform the feasible discriminating step -> report result -> retain residual limitation and lower claim where necessary | completed and uncompleted parts are separately visible; headline text respects the residual boundary | records with `partially-addressed`, including acquisition/deployment boundaries in imaging AI |
| Contest or cannot perform | state position without defensiveness -> give governing scientific/feasibility reason -> supply nearest interpretable control or triangulation -> revise claim -> disclose remaining uncertainty | editor can see why the exact request is not decisive or feasible and what claim was surrendered | TPR014 protected training data plus public external evaluation; TPR044 frozen-feature boundary |

Do not use “reviewer confirmed” as the only closure evidence. Preserve the underlying action, result
and page locator even when a later-round reviewer explicitly states that a concern is resolved.

## Modality-aware response emphasis

| Scope | A final response must make explicit |
|---|---|
| Imaging AI / radiomics / pathology | patient-level split and independence; label/reference standard; exact comparator and tuning; calibration/uncertainty; external cohort or the absence of one; scanner/site/workflow boundary |
| Bulk RNA | biological sample unit; model, batch/composition and multiplicity handling; pathway versus functional evidence; what an external cell atlas did and did not measure |
| Single-cell | donor-level inference; annotation evidence; integration sensitivity; rare-state support; trajectory/communication inference ceiling |
| Spatial | physical resolution; segmentation/registration and null model; patient/section hierarchy; orthogonal imaging/staining; single-case or cross-patient boundary |
| Multi-omics | matched sample intersection; blockwise QC; unimodal and paired ablations; latent-factor meaning; incremental value of each modality |
| Perturbation | assignment, efficiency, dose-time, target engagement, off-target/vehicle controls, rescue feasibility and the causal wording that survives |
| Imaging–mechanism | patient–lesion–block–section–cell mapping; measured versus generated biology; mapping error; unimodal/fusion ablation; competing mechanisms and functional evidence |

If a reviewer requests a modality the study does not contain, do not fabricate an “expected” result.
First determine whether the current claim logically requires that modality. If it does, add the study
or lower the claim; if it does not, give criterion-based pushback and, where useful, an optional future
route clearly separated from closure.

## Failure patterns

- “We agree and have revised accordingly” with no operation or location.
- “We performed an additional analysis” with no result.
- Calling internal resampling external validation.
- Adding a limitation paragraph while keeping the same unsupported headline claim.
- Answering a donor-level concern with a larger number of cells, spots, slices or tiles.
- Treating an optional experiment or reviewer-preferred method as scientifically mandatory without a
  manuscript-grounded criterion.
- Promising an accession, code deposit, experiment or analysis that is not present in the package.
- Closing a compound comment after answering only one child commitment.

## How this skill uses the corpus

Use corpus lessons to anticipate applicable concerns, select a response structure and define closure
evidence. Do not copy stock author wording, imitate praise, or infer missing results. When a paper-level
provenance audit is requested, search the synchronized response map by TPR ID, DOI, stratum, request
class, canonical concern family or closure state. The canonical 39-field source remains in the
`radiology-radiogenomics` skill; preserve its DOI, official review URL, SHA-256, page locators,
fine-grained `concern_codes` and `concern_ontology_version`. Use canonical families for cross-paper
frequency or routing; use raw codes for source-level traceability.
