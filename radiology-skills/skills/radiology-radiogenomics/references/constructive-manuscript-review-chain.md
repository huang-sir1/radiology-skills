# Constructive manuscript review chain

Use this module for manuscript review in `imaging-only`, `mechanism-only`, or `imaging-mechanism`
scope. It turns a scientific audit into advice an author or learner can act on. It does not simulate
multiple independent reviewers, manufacture balance, assign numerical scores, or edit the source
unless the user separately asks for revision.

The matching scope reviewer playbook and active modality playbooks supply the domain criteria. This
module supplies the review sequence, cross-cutting dimensions, constructive-feedback contract and
repair synthesis. For a later re-review, route to `revision-verification` and freeze the criteria in
the original report.

## 1. Review modes

The scientific threshold is constant; presentation changes with interaction mode.

| Mode | How to review | Minimum output |
|---|---|---|
| reviewer | judge the supplied work against named criteria and evidence | preserved contribution, evidence-anchored findings, verdicts, repairs and claim consequence |
| mentor | expose the same problems through explanation and discriminating questions | judgement backbone plus options, trade-offs, recommendation and next executable action |
| combined | preserve valid work, audit defects, then redesign the blocked path | review first; redesign cannot hide or neutralize a `STOP` |

If a request asks to “review and rewrite,” complete the review first, freeze finding IDs and claim
ceilings, then re-route the accepted revision work to `writing-revision`. Do not silently rewrite a
scientific defect into smoother prose.

## 2. Constructive review sequence

### R0 — Establish the review contract

Record the artifact/version, requested review focus, declared study scope, article type, intended
audience/venue if supplied, central claim, claim branches, independent unit, matched n, materials
available and unavailable, and whether data/code can actually be inspected.

State coverage. A full manuscript review is not a code audit when no code was supplied, and a prose
review cannot verify that an analysis or experiment occurred. Do not infer missing evidence from a
polished description.

### R1 — Reconstruct the author's strongest defensible case

Before criticizing, answer:

1. What exact problem is addressed, for whom or in what biological system?
2. What did the field know before, and what knowledge delta is claimed?
3. What design and data could answer the question?
4. What are the principal claims and their strongest evidence anchors?
5. What is the current claim ceiling if the paper is read charitably but rigorously?

Record every genuine strength that affects trust, contribution or repairability; there is no praise
quota. Do not invent a strength for rhetorical balance. A valid component may be preserved even when
the headline claim stops.

### R2 — Trace claims to evidence before judging style

For every material title, abstract, Results and Discussion claim, identify:

`location -> Claim ID -> evidence pointer -> primary evidence state -> modality subtype ->
claim-link status -> independent unit/n -> effect and uncertainty -> branch -> verdict -> boundary`.

Acceptable evidence anchors include a precise text location, table and cell/row, figure and panel,
dataset or analysis artifact, code/function/commit, or an `absence` anchor naming where the required
item should have appeared and which surfaces were checked. A major claim that cannot be anchored is
a question for the authors until the relevant material is inspected; it is not licence to invent a
defect.

Audit title and abstract claims first because they set the reader's interpretation, but never let
surface language displace a design, leakage, unit, spatial mapping or causal-identification defect.

### R3 — Evaluate cross-cutting dimensions

Use all applicable dimensions and mark non-assessable ones explicitly. Do not aggregate them into a
score; a decision-bearing failure is not cancelled by strengths elsewhere.

| Dimension | Core questions | Common decision-bearing failure | Constructive direction |
|---|---|---|---|
| Scope and question | Is the population/system, comparator, estimand, time and intended use explicit and answerable? | vague or shifting question; design cannot identify the target | restate the nearest answerable question and exact estimand |
| Contribution and relevance | What defensible knowledge delta matters to the field, clinic or method user? | novelty asserted from tool combination alone; “so what” remains unclear | name the delta supported now; separate reframing from new evidence |
| Literature and theory | Are the necessary prior findings, alternatives and conceptual frame critically integrated? | selective precedent, missing competing model or unsupported priority claim | add or correct only literature that changes the argument |
| Cohort and provenance | Are eligibility, flow, attrition, timing, matching and data origin traceable? | usable matched intersection hidden; selection/treatment timing unresolved | add flow/mapping artifacts, sensitivity analysis or narrow scope |
| Units and replication | Are biological and technical units, nesting, pairing and repeated measures respected? | cell/spot/ROI count substitutes for donor/patient replication | reanalyse at the biological unit or lower the claim |
| Modality validity | Do acquisition/assay QC, annotation, preprocessing and versioned parameters support the measurements? | unstable phenotype, failed assay QC, circular annotation or generated layer presented as measured | repair the modality pipeline, disclose failure, or retire the affected evidence |
| Parameter, metric and method validity | Are decision-bearing settings traceable, leakage-safe, justified and frozen; do metrics and methods match the question, data, unit and assumptions; are comparisons and sensitivities fair? | outcome/test-informed selection, package default as rationale, arbitrary cutoff/resolution, unmatched benchmark, or conclusion that flips across plausible settings | route the focused audit to `radiology-method-evaluation`; build separate parameter/metric/method ledgers, run the minimum decision-bearing comparison or narrow the claim |
| Statistical validity | Are estimand, uncertainty, multiplicity, missingness, model assumptions and leakage controlled? | leakage, pseudoreplication, unidentifiable contrast or selective testing | rebuild analysis, add sensitivity/negative controls, or reduce the claim |
| Validation and comparators | Are simple/clinical baselines, internal versus external validation and failure cases appropriate? | internal resampling sold as external evidence; no relevant baseline | add a fair comparator/locked validation or state discovery-only status |
| Cross-scale linkage | Are identity, region, scale, time and treatment compatible across modalities? | parallel datasets or unmatched tissue presented as a patient/region mechanism | repair mapping, label patient-level association, or remove the bridge claim |
| Mechanism and causality | Are direction, temporal order, target engagement, alternatives, specificity and rescue adequate? | enrichment, proximity, prediction or perturbation assignment alone called mechanism/causality | test a discriminating link, show engagement/control/rescue, or use bounded wording |
| External validity, utility and implementation | Does generalization match the sampling frame, site/platform spectrum and intended use; are affected groups, workflow burden, fairness and material unintended consequences addressed where applicable? | one retrospective cohort claimed as deployment or universal biology; implementation benefit asserted without workflow or subgroup evidence | define boundary conditions, stakeholders and evidence needed for transport, utility or implementation |
| Argument coherence | Do problem, gap, method, findings and implications form a traceable chain? | sections promise different questions; conclusion is not earned by Results | rebuild the argument map and remove unsupported branches |
| Evidence placement and visuals | Are decisive results, negative evidence, denominators and inferred status visible in text/figures/legends? | conclusion-changing caveat buried; panel cannot be interpreted independently | relocate evidence and repair labels/legend rather than add narrative padding |
| Reporting and reproducibility | Can readers reconstruct methods, data/code provenance, ethics and availability? | missing parameters, accession, code state, approval or full result set | complete the reproducibility package or state the access boundary |
| Writing precision | Are terms, numbers, verbs and paragraph jobs consistent without confusing polish with science? | causal/mechanistic inflation, denominator drift, untraceable number | correct the scientific statement first, then polish |
| Integrity and transparency | Are exclusions, deviations, negative findings, overlap, conflicts and limitations disclosed? | fabricated/unverifiable claims, hidden overlap or selective result reporting | verify and disclose; stop release when integrity cannot be established |

### R4 — Apply scope and modality lenses

The dimensions above are shared; these lenses specify what “valid” means in the declared scope.

| Lens | Review emphasis | Do not demand or infer |
|---|---|---|
| imaging-only | acquisition, segmentation/annotation, feature stability, train-only processing, patient split, calibration, comparators and transport | absent omics or a molecular mechanism unless claimed |
| bulk RNA | specimen/donor unit, preanalytics, library/feature construction, composition, normalization, contrasts, multiplicity and reference versions | cell-specific source or function from bulk association alone |
| single-cell/snRNA | donor replication, cell/nucleus QC, annotation uncertainty, composition, pseudobulk/hierarchical inference, trajectory and reference transfer | thousands of cells as independent replication or trajectory as time/causality |
| spatial | tissue/section provenance, segmentation, coordinates, registration error, spatial null, patient replication and resolution | cell identity, communication or locality below measurement precision |
| multi-omics | usable matched-sample intersection, blockwise QC, missing-modality handling, integration sensitivity, unimodal and paired ablations, latent-factor meaning and incremental value | a shared embedding, factor or fused-model gain as proof that every modality contributes or that the latent axis is a measured mechanism |
| pathology | block/section provenance, assay controls, blinding, annotation, spatial sampling and nested statistics | molecular mechanism from morphology or co-localization alone |
| perturbation | assignment, efficiency, target engagement, dose/time, off-targets, controls, replication and rescue | causal success from assigned guides or condition contrast alone |
| imaging-mechanism | both modality pipelines plus patient/lesion/region/time mapping, evidence-state separation, discordance and discriminating validation | co-occurring imaging and molecular results as a connected mechanism |

Use the active playbook for detailed checks. An external atlas, generated molecular layer or proposed
future assay keeps its declared role and does not acquire patient-matched status through review prose.

### R5 — Convert observations into constructive findings

Every decision-bearing weakness uses this contract:

`Finding ID -> class -> review dimension -> severity -> obligation -> evidence anchor -> observed problem ->
governing criterion -> why it matters -> claim consequence if unchanged -> minimum feasible remedy ->
optional stronger route -> cost/trade-off -> closure evidence -> confidence/scope limit`.

Fields mean:

- **Class:** `defect` or `clarification-needed`. A point that cannot yet be established from inspected
  material belongs in Questions for Authors, not in the findings table. Optional ideas are not defects.
- **Severity:** `P0`, `P1`, or `P2` from the shared integrity gates, determined by scientific impact,
  not tone or reviewer preference.
- **Obligation:** `must-fix`, `should-fix`, or `consider`; this describes editorial action, not a
  fourth scientific verdict, and is not derived mechanically from severity.
- **Minimum feasible remedy:** the smallest change that makes the current claim defensible. It may be
  a correction, fuller reporting, reanalysis, sensitivity test, new validation, new experiment,
  claim reduction or claim retirement.
- **Optional stronger route:** a separately labelled opportunity to increase depth or impact; it is
  never smuggled into “required” merely because it is interesting.
- **Cost/trade-off:** data, sample, time, assay, analytic complexity, interpretability or
  generalizability burden introduced by the proposed remedy.
- **Closure evidence:** an observable manuscript/data/code/experiment condition by which a re-review
  can verify completion.

For a strength, record the exact evidence anchor and why it is decision-relevant. Do not attach a
weakness severity to a strength.

Triage every reviewer-like request before prescribing a repair:

| Request class | Meaning | Review handling |
|---|---|---|
| manuscript-grounded defect | inspected evidence fails a named criterion | create an atomic finding with severity, claim consequence and closure evidence |
| clarification needed | the answer may exist but cannot be verified from supplied material | ask a decision-changing question or require exact reporting; do not assume failure |
| optional strengthening | the current claim is defensible and the idea would add depth or impact | keep outside required findings; state benefit, cost and why it is optional |
| reviewer preference | an alternative method or presentation is preferred but the chosen approach can answer the question | evaluate the actual method on its assumptions; do not impose preference as a defect |
| scope-contested or infeasible request | the requested modality/experiment is unnecessary for the declared claim or cannot be completed honestly | give an evidence-based boundary, feasible sensitivity or claim reduction; never fabricate compliance |

The wording of a reviewer comment does not determine its class. Terms such as “must,” “should” or
“future work” are evidence about the requester's emphasis, not proof of scientific necessity.

### R6 — Choose a proportionate repair class

| Repair class | Use when | What must be returned |
|---|---|---|
| Clarify | evidence exists but question, term, unit or boundary is ambiguous | exact text/legend/location to change |
| Complete reporting | method/result exists but cannot be reconstructed | missing fields and where they belong |
| Correct or reanalyse | current implementation or inference is invalid but data can answer the question | analysis change, affected claims and success criterion |
| Sensitivity/negative control | a plausible alternative could change interpretation | discriminating analysis and result pattern that supports each explanation |
| Validate | transport, assay identity or claim branch needs independent/orthogonal support | frozen object, validation set/assay, metric/readout and pass/fail criterion |
| New experiment | a mechanistic/causal link cannot be identified from existing data | minimum intervention, controls, timing, engagement and phenotype readout |
| Narrow or retire claim | evidence cannot support the requested branch within the project | nearest defensible wording and downstream locations to update |
| Optional extension | current paper is valid and the idea is genuinely additive | benefit, burden, risk and why it is optional |

Do not prescribe a fashionable assay when claim reduction is the only feasible repair. Do not call a
new experiment “minor revision.” If no feasible repair exists within one revision cycle, state that
directly while still showing the nearest scientifically valid project or claim.

### R6a — Build a response-and-closure path

When actual reviewer comments are supplied, split each compound comment into stable commitments and
record an explicit author decision: `accept`, `partially accept`, `contest`, or `cannot address`.
For each commitment, the response block must contain:

`comment -> decision/rationale -> action and method -> result or evidence -> exact revised location ->
residual limitation/claim boundary -> observable closure state`.

“We performed the analysis,” “the manuscript was revised,” or a response-letter promise without the
result and revised location is not closure. Evidence-based disagreement is allowed: show why the
criterion is already met or inapplicable, add a discriminating sensitivity analysis when proportionate,
and state what text or boundary changed. A parent comment closes only when every required commitment
closes; one completed subpart cannot hide an unaddressed sibling.

### R7 — Synthesize judgement without score arithmetic

Return separate judgements for:

- scientific validity of each material claim (`PASS / CONDITIONAL / STOP`);
- contribution and audience/venue fit, when a venue was supplied;
- submission readiness;
- repairability within the declared resources and one revision cycle.

Do not average dimensions. Explain the overall conclusion by naming unresolved decision-bearing
criteria, the claims they affect and whether they are repairable. Venue mismatch is not proof that a
study is scientifically invalid; fluent writing is not proof that it is ready for submission.

Lead with the single most important issue, then group dependent findings to avoid a long copyediting
list obscuring the scientific problem. Minor language and formatting items remain a separate channel.

Before release, calibrate the review:

- evaluate whether the chosen design answers the stated question, not whether it is the reviewer's
  favorite method;
- apply baseline, ablation, mechanistic, clinical-utility or reporting expectations only when they
  fit the article type and declared claim;
- separate manuscript evidence from institutional prestige, author identity and language fluency;
- verify that every `P0/P1` finding has an adequate anchor and that uncertainty is visible;
- ask whether the report would still help the authors improve if the venue recommendation were negative.

## 3. Section-by-section review angles

| Section/artifact | Questions that produce useful comments |
|---|---|
| Title | Does it name the true design and claim branch without causal, mechanistic, predictive or spatial inflation? |
| Abstract | Can every number/claim be traced; are n, validation setting, effect/uncertainty and decisive boundary visible? |
| Introduction | Is the gap exact, literature-grounded and answerable by the actual design? |
| Methods | Can sampling, mapping, preprocessing, QC, analysis, validation and evidence roles be reconstructed? |
| Results | Does each subsection answer one question with effect, uncertainty, robustness and relevant discordance? |
| Figures/tables | Are units, denominators, patient/donor replication, state, scale, test and missing data interpretable? |
| Legends | Can the display be understood without guessing observed versus inferred/generated layers? |
| Discussion | Does synthesis address alternatives, relation to prior work, external validity, utility and claim boundaries? |
| Conclusion | Is the knowledge delta memorable but no stronger than the evidence? |
| Supplement/data/code | Are decision-bearing details and full results accessible, versioned and consistent with the main paper? |

## 4. Guided, learner-facing review

When the author seeks advice, do not unload the entire report at once. Start with the highest-impact
decision and ask questions that reveal the reasoning:

1. Which exact sentence do you want the study to earn?
2. What is the independent unit and usable matched intersection for that sentence?
3. Which evidence is directly observed, and which is estimated, predicted or proposed?
4. What serious alternative would produce the same pattern?
5. What result would distinguish the explanations or force weaker wording?
6. Which repair is feasible now, and what new limitation would it introduce?

Then offer up to three genuinely different routes:

- **Minimum repair:** defensible with the current data and narrowest claim.
- **Standard repair:** best balance of credibility, feasibility and contribution.
- **Mechanism-advancing/ambitious repair:** new spatial, longitudinal, orthogonal, perturbational or
  external evidence with explicit cost and failure criteria.

Recommend one. A question-based teaching style must not soften severity or transfer the scientific
decision back to the learner without guidance.

## 5. Output contract

Return the smallest complete review package in this order:

1. route, review contract and coverage boundary;
2. reconstructed contribution and genuine strengths;
3. overall judgement and current claim ceiling;
4. decision-bearing findings using the full constructive contract;
5. scope/modality and section-level comments needed to interpret those findings;
6. preserve/repair/retire map;
7. minimum repair roadmap, optional stronger routes and trade-offs;
8. author questions that could change the decision;
9. exact replacement wording only after the governing scientific issue is resolved;
10. frozen closure criteria for a later `revision-verification` task.

Use [the constructive review and repair matrix](../templates/constructive-review-and-repair-matrix.md)
for a reusable report. Use the deeper [reviewer audit](../templates/reviewer-audit.md) when the task
requires a full domain-by-domain evidence audit; keep finding IDs identical rather than duplicating
the same defect as separate opinions.
