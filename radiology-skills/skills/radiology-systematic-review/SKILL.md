---
name: radiology-systematic-review
description: "Design/audit systematic or scoping reviews from protocol through synthesis, certainty and living updates."
---

# Systematic review and evidence synthesis

Use this skill to turn a review question into an auditable evidence-synthesis project, or to test
whether an existing review can support its conclusion. It is an independent scientific entry point
and a cross-cutting mentor/reviewer module. It does not require a manuscript to exist first.

## Core stance

- **Protocol first.** Freeze the question, eligibility, outcomes, synthesis route, independent unit,
  subgroup/sensitivity families and deviation policy before result-aware decisions. If work began
  first, record the protocol as `RETROSPECTIVE` rather than implying prospective registration.
- **Design before pooling.** A forest plot is not the objective. Judge clinical, methodological and
  statistical compatibility before quantitative synthesis; use a structured synthesis without
  meta-analysis when pooling would erase the question.
- **One evidence row is not always one independent study.** Detect overlapping cohorts, multiple
  publications, arms, readers, lesions, images, blocks, sections, cells and spots. Preserve the
  patient/donor/study hierarchy and never inflate precision through pseudoreplication.
- **Risk of bias and applicability are not journal prestige scores.** Match the assessment tool to
  the included design and evaluate domains with evidence anchors. Do not average a fatal domain
  into a reassuring total score.
- **Constructive review.** For every problem, state the criterion, consequence, minimum repair,
  stronger option and cost, closure evidence, and claim that survives if it remains unresolved.
- **No invention.** Never fabricate a searched database, search date, registration, duplicate
  screening, included study, extracted value, risk-of-bias judgment, effect size, heterogeneity,
  certainty rating or review result.

## Choose the entry mode

| Mode | Use when | Required emphasis |
|---|---|---|
| `protocol` | the review is being designed | question framework, eligibility, outcomes, search brief, duplicate processes, pooling gate and prospective decision rules |
| `audit` | a protocol, search log, screening file, extraction sheet, analysis or draft exists | artifact-bound verification, deviations, overlap, missing fields, bias/applicability, reproducibility and atomic repairs |
| `mentor` | a learner needs choices explained while building the review | options, tradeoffs, examples, next decision, minimum viable route and stronger route without silently doing unverified work |
| `synthesis-handoff` | extraction is sufficiently mature for synthesis or meta-analysis | compatible effect rows, hierarchy, covariance/dependence, model candidates, heterogeneity and sensitivity specification for `radiology-stats` |
| `writing-handoff` | synthesis findings are fixed and need a manuscript package | PRISMA flow inputs, Methods/Results/display jobs, certainty, limitations and claim ceiling for reporting/writing modules |

Also declare `review_route` from the routing table below and the evidence state of supplied
artifacts: `PLANNED`, `AUTHOR_REPORTED`, `PARTLY_VERIFIED`, `VERIFIED`, or `NOT_ASSESSABLE`.

## Required route selection

Open [the evidence-synthesis router](references/evidence-synthesis-routing.md) and select one
primary route. Hybrid reviews may activate more than one route, but keep separate eligibility,
extraction and synthesis branches when their estimands differ.

| Route | Typical question |
|---|---|
| `scoping` | What concepts, methods, evidence types and gaps exist? |
| `systematic-narrative` | What does comparable evidence show when quantitative pooling is unsuitable? |
| `diagnostic-accuracy-meta` | How accurately does an index test identify the target condition against a reference standard? |
| `prevalence-incidence-meta` | What proportion or rate has a defined state or event in a specified population, setting and period? |
| `observational-association-meta` | What is the bounded association between an exposure/feature and an outcome after preserving design, contrast and adjustment? |
| `reliability-agreement-method-comparison-meta` | How reproducible, concordant or quantitatively interchangeable are readers, measurements, segmentations, devices or methods? |
| `prediction-radiomics-ai-meta` | How well is an imaging/radiomics/AI model developed, validated, calibrated or clinically evaluated? |
| `prognostic-meta` | What is the association between a factor/model and a time-bound outcome? |
| `intervention-meta` | What is the effect of an imaging, AI-guided or biological intervention? |
| `omics-mechanism-synthesis` | What bulk/scRNA/spatial/pathology/perturbation evidence supports a bounded biological explanation? |

## Minimal intake

Record available materials and mark missing decision-bearing fields `AUTHOR_INPUT_NEEDED`:

1. review objective, intended audience/use, scope and preliminary claim;
2. route and question framework: PICO, PIRD, PECO/PICOS, CHARMS-like prediction domains, or a
   concept-context-population framework for scoping reviews;
3. protocol version/date, registration platform/identifier/status and amendments;
4. databases/platforms, coverage dates, complete strategies, last-search date and grey-literature
   policy—reported as a search brief until verified by `radiology-search`; search-strategy peer-review
   receipt/status and lifecycle state `STATIC`, `LIVING` or `RETIRED`;
5. eligibility, outcomes/estimands, time horizons, effect measure, report/study unit and language/
   publication-status restrictions;
6. screening, conflict resolution, exclusion reasons, PRISMA counts and any automation/priority
   screening contract: tool, model, prompt and version; pilot/calibration evidence; frozen threshold;
   low-priority exclusion audit and recall safeguard; human override; and final human responsibility;
7. extraction form, reviewer structure, linked reports/overlapping cohorts and usable effect rows;
8. risk-of-bias/applicability tool/version, judgments and evidence anchors;
9. synthesis outputs/code, independent unit, dependence structure, model, heterogeneity,
   subgroup/sensitivity and certainty evidence.

## Required workflow

1. **Classify and frame.** Choose the route and define the estimand/question before choosing a
   synthesis method. Do not force every review into PICO; use PIRD for diagnostic accuracy and
   prediction-specific domains when model development/validation is central.
2. **Freeze or reconstruct the protocol.** Use
   [the protocol template](templates/systematic-review-protocol.md). Record prospective,
   retrospective, amended or unregistered status and distinguish dated decisions from later
   deviations.
3. **Create the search handoff.** Specify concepts, synonyms, controlled vocabulary needs,
   eligible designs, databases/platforms, dates and update trigger. `radiology-search` owns actual
   database execution, exact query logs, deduplication and corpus acquisition; `radiology-citation`
   owns identifier/reference verification. Record whether the complete source-specific strategy was
   independently peer reviewed, by whom/which role, against which stated criterion, the strategy
   version reviewed, comments and resolution locators, unresolved issues and whether material
   amendments require re-review. `NOT_REVIEWED` is an honest state, not a reason to invent a receipt.
   Also declare `STATIC`, `LIVING` or `RETIRED`, with update trigger/cadence or retirement reason;
   a living label does not prove the search is current.
4. **Verify selection integrity.** Reconcile retrieved, deduplicated, screened, full-text and
   included counts; document independent screening, conflict resolution and exclusion reasons.
   For AI-assisted or priority screening, freeze the exact tool/model/prompt/version and threshold
   before production use; record pilot/calibration corpus and results; preserve every score,
   recommendation, exclusion and human override; audit a prespecified sample of low-priority
   exclusions against a recall safeguard; and name the human who retains final inclusion/exclusion
   responsibility. If the low-priority audit breaches the frozen safeguard, `STOP` exclusions,
   expand human screening and recalibrate without deleting the failed pilot. Preserve a study-family
   identifier linking multiple reports from one cohort.
5. **Extract for the question and design.** Use
   [the extraction matrix](templates/data-extraction-and-synthesis-matrix.md). Separate study/report
   metadata, population, index/exposure/intervention, comparator/reference standard, outcomes,
   hierarchy, effect estimates and adjustment from reviewer interpretations.
6. **Assess risk of bias and applicability.** Open
   [the methods and quality-gates reference](references/review-methods-and-quality-gates.md), choose
   a design-matched tool, and use
   [the risk matrix](templates/risk-of-bias-applicability-matrix.md). Preserve domain judgments and
   supporting anchors; do not invent a numeric quality score.
7. **Run the pooling-feasibility gate before meta-analysis.** Test compatibility of population,
   design, target condition/endpoint, time horizon, index/model/intervention/exposure, comparator/
   reference standard, effect definition, threshold, unit and dependence. Return `POOL`,
   `STRATIFY`, `NARRATIVE`, or `STOP_FOR_REPAIR` with reasons.
8. **Specify synthesis.** For compatible rows, define effect-size transformation, within-study
   uncertainty/dependence, random/fixed or hierarchical model candidate, heterogeneity, small-study
   assessment, prespecified subgroup/meta-regression and sensitivity analyses. Hand computation and
   statistical model implementation to `radiology-stats`; never claim an analysis ran from a plan.
9. **Handle non-pooling honestly.** Group evidence by question-bearing dimensions, tabulate effect
   direction/magnitude/precision and risk of bias, explain heterogeneity, and state why quantitative
   synthesis was not justified. Do not vote-count only by statistical significance.
10. **Judge certainty and claim ceiling.** Apply GRADE or another verified, question-appropriate
    certainty framework when relevant, or an explicit confidence rationale when it is not. Do not
    label an informal impression as GRADE. Separate association, prediction,
    diagnostic performance, intervention effect, reproducibility and mechanism. Cross-sectional or
    inferred omics concordance does not establish causality.
11. **Package reporting and writing handoffs.** Send current checklist/version audit and PRISMA/
    PRISMA-DTA placement to `radiology-reporting`; send only fixed, traceable evidence and bounded
    claims to `radiology-writing`.
12. **Operate a living route when declared.** For `LIVING`, freeze update triggers/cadence, search
    version, new-record triage, study-family reconciliation, analysis/checklist changes, public
    version links and retirement criteria. After publication, register corrections, retractions and
    evidence that can invalidate eligibility, risk-of-bias, synthesis or certainty through the
    pipeline post-publication lifecycle. `LIVING` is an operating commitment, not a freshness badge.

## Scientific red lines

- Do not change eligibility, outcomes, thresholds, time horizons, subgroup families or pooling
  decisions because one option yields a favourable conclusion; record justified amendments.
- Do not treat reports from the same cohort, multiple thresholds, time points, outcomes, readers,
  lesions, sections, cells or spots as statistically independent without modelling or selecting the
  dependence.
- Do not pool adjusted and unadjusted estimates, development and external-validation performance,
  per-lesion and per-patient accuracy, incompatible time horizons, or incompatible effect measures
  merely because they share a label.
- For prevalence or incidence, preserve numerator, denominator or person-time, sampling frame,
  outcome definition and period. A pooled transformed proportion is not population incidence unless
  the contributing studies actually estimate incidence on compatible time scales.
- For observational association, preserve the exposure contrast, effect scale, confounder set,
  adjustment class and temporal order. Correlation or cross-sectional association is not causality,
  prognosis, diagnostic accuracy or treatment effect.
- Correlation is not agreement. Do not pool unspecified ICC variants, weighted and unweighted kappa,
  Dice and overlap variants, repeatability coefficients, limits of agreement or reader/model effects
  as interchangeable. Preserve the measurement object, rater/reader/device hierarchy, repetitions,
  metric definition/model/form and direction before any synthesis.
- For diagnostic accuracy, do not pool sensitivity and specificity independently while ignoring
  their threshold relationship when a joint model is required.
- For prediction/radiomics/AI evidence, separate discrimination, calibration and clinical utility;
  a pooled AUC alone does not establish transportability or patient benefit.
- For bulk/scRNA/spatial/pathology evidence, the donor/patient is normally the inferential unit for
  patient-level claims. More genes, cells, spots or tiles do not create more biological subjects.
- Mechanistic convergence across modalities strengthens plausibility only to the degree that
  samples, spatial/temporal scales, perturbations and validation are aligned. Association remains
  association without intervention, target engagement, rescue or equivalent causal evidence.
- Funnel plots and asymmetry tests are not automatic proof of publication bias and may be
  uninformative with few or highly heterogeneous studies.
- AI or priority rank is decision support, not an autonomous exclusion authority. Do not silently
  change a threshold after seeing included studies, discard low-priority records without the frozen
  audit/recall safeguard, or represent model output as independent duplicate human screening.

## Output contract

Return the shortest complete package needed for the selected mode:

1. `Review identity` — mode, route, objective, framework, scope, protocol/registration state,
   lifecycle `STATIC/LIVING/RETIRED`, search-currency state, artifacts and evidence boundary.
2. `Question and eligibility lock` — population/context, index/exposure/intervention, comparator/
   reference standard, outcomes/estimands, horizons, designs, report unit and amendments.
3. `Search and selection handoff` — executable brief for `radiology-search`, versioned
   search-strategy peer-review receipt, dedup/study-family policy, screeners/conflicts, exclusion
   taxonomy, PRISMA reconciliation and lifecycle update/retirement trigger; when automated, include
   the frozen tool/model/prompt/version and threshold, pilot/calibration receipt, low-priority audit
   sample and recall safeguard, human overrides and named final human responsibility.
4. `Extraction readiness` — required fields, linked reports, missingness, hierarchy, compatible
   effect rows and unresolved data queries.
5. `Risk-of-bias and applicability matrix` — design-matched domains, anchors, judgments,
   consequence and sensitivity role.
6. `Pooling-feasibility decision` — `POOL / STRATIFY / NARRATIVE / STOP_FOR_REPAIR`, decisive
   incompatibilities and eligible synthesis groups.
7. `Synthesis specification or results` — clearly labelled planned/reported/verified effect
   measures, model, dependence, heterogeneity, subgroup, sensitivity and small-study assessments.
8. `Certainty and claim ceiling` — certainty/confidence rationale, what is supported, what is not,
   residual heterogeneity and applicability limits.
9. `Strengths and atomic findings` — evidence anchor, severity, criterion, minimum repair,
   stronger option/cost and closure evidence.
10. `Reporting and writing placement` — PRISMA flow inputs, Methods, Results, tables/figures,
    Supplement, Discussion and Abstract/title constraints.
11. `Next action` — the single next decision-bearing step and all `AUTHOR_INPUT_NEEDED` fields.

## Handoffs and non-ownership

- Database retrieval, exact search execution, deduplication, corpus acquisition and search updates
  → `radiology-search`.
- DOI/PMID/reference metadata and claim-support verification → `radiology-citation`.
- Effect calculation, hierarchical/meta-analytic model fitting, uncertainty, heterogeneity and
  multiplicity → `radiology-stats` after this skill supplies compatible rows and hierarchy.
- Current PRISMA/PRISMA-DTA or other reporting-checklist version and item-by-item audit →
  `radiology-reporting`.
- Manuscript construction from fixed evidence → `radiology-writing`; language polish →
  `radiology-polishing`.
- Full-manuscript adversarial review → `radiology-prereview`; final upload-file audit →
  `radiology-submission`.
- Published-version monitoring, correction linkage, downstream derivative staleness and retirement
  coordination → `radiology-pipeline`; the review owner retains eligibility/synthesis/update decisions.

Do not silently convert a request to find papers into a full review, and do not certify a review as
completed when only a protocol, author report or incomplete corpus is available.
