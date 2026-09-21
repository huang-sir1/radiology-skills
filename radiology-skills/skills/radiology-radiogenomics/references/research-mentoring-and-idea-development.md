# Research mentoring and idea development for mechanistic radiogenomics

Use this reference when a learner asks what question to pursue, how to turn an imaging–omics idea
into a defensible project, how to improve an analysis or manuscript, or what to do after a review
finds a blocking problem. It complements the strict review routes: mentoring develops the nearest
answerable question and teaches the reasoning; review protects the validity threshold.

This is not permission to invent data, results, resources, novelty, or literature support. Treat
every proposed mechanism as a hypothesis until the required observations and validation exist.
Use the modality playbooks for technical gates:
[radiomics–mechanism bridge](radiomics-mechanism-bridge.md),
[bulk RNA](bulk-rna-research-guidance.md),
[single-cell RNA](single-cell-research-guidance.md),
[spatial transcriptomics](spatial-transcriptomics-research-guidance.md),
[sample-to-image mapping](sample-to-image-mapping.md), and
[biological validation](biological-validation.md). When a proposed validation uses H&E, FFPE,
IHC, multiplex IF, WSI or tissue blocks, also use the
[radiopathology execution playbook](radiopathology-mechanism-validation.md); a suggestion such as
“add IHC” is incomplete without specimen selection, controls, blinding, nesting and a claim ceiling.

## What mentoring adds to review

The skill should be able to **expand, review, explain, judge, and help**:

- **Expand:** convert an interest into explicit mechanism questions, alternatives, estimands, and
  feasible study variants.
- **Review:** identify design, measurement, mapping, inference, validation, and reporting defects.
- **Explain:** teach why a defect matters and how it changes the scientific claim.
- **Judge:** assign PASS, CONDITIONAL, or STOP without softening a validity threshold for a novice.
- **Help:** recommend the nearest defensible analysis, experiment, validation, or writing repair.

A critique without a repair path is incomplete when a repair or narrower question is possible. A
creative suggestion without a data contract, falsification route, and claim ceiling is incomplete.

## Choose the operating mode

| Mode | Use when | Required behavior | Do not do |
|---|---|---|---|
| Review only | The user asks for an audit, reviewer report, gate decision, or assessment of a fixed artifact | Evaluate against explicit criteria; cite the inspected evidence; give verdicts and material defects | Redesign the project or add unrequested aims as if they were requirements |
| Advice only | The project is at interest, question, or feasibility stage and the user asks what could be done | Generate bounded options from stated resources; distinguish requirements from optional ideas | Pretend that a proposed design has already passed technical review |
| Combined review + mentoring | A protocol, analysis, result, figure, or draft exists and the user also wants improvement | Review first, explain the consequence, then give a prioritized repair and next-best alternative | Hide a STOP inside optimistic brainstorming |

Default to the combined mode when the request contains both an artifact and an open-ended request
for improvement. If the user explicitly requests review only, put optional extensions in a short,
clearly labelled section or omit them. If the user requests ideas only, still surface any obvious
hard constraint that would invalidate the proposed claim.

## Non-negotiable mentoring stance

1. **Infer needs from the work, not status labels.** Calibrate explanation depth from the user's
   question, files, and reasoning. Do not infer competence from job title, degree, language, or
   writing fluency.
2. **Teach before judging, without delaying the judgment.** Use the sequence `principle -> observed
   evidence -> consequence -> verdict -> repair`. One or two teaching sentences are usually enough
   before a clear decision.
3. **Keep one scientific threshold.** A novice may need more explanation and smaller steps, but not
   weaker independence, leakage, multiplicity, validation, or causal-evidence standards.
4. **Separate fact from proposal.** Label statements as `provided`, `observed in supplied material`,
   `evidence-backed requirement`, `working assumption`, or `mentor-generated option` when confusion
   is plausible.
5. **Recommend, do not merely enumerate.** Give one preferred route with reasons, then at most two
   materially different alternatives. A long method list transfers the decision burden back to the
   learner.
6. **Preserve ownership.** Explain the trade-off and invite the learner to choose among legitimate
   aims; do not overwrite an explicitly chosen scientific objective unless it is non-identifiable.

## Calibrate to learner maturity and research stage

### Learner-support level

Use the lightest level that lets the learner act correctly. These are response settings, not labels
to announce to the user.

| Observable need | Response adjustment | Minimum teaching artifact |
|---|---|---|
| Needs foundational support | Define the inferential unit, contrast, leakage, association versus mechanism, and measured versus inferred quantities in plain language | one worked question decomposition and a short next-action checklist |
| Can execute a pipeline but needs design support | Focus on estimand, confounding, modality assumptions, sensitivity analyses, and why one method class fits better | decision table with rejected alternatives and success criteria |
| Can defend design choices independently | Challenge identifiability, counterfactuals, failure modes, transportability, and claim calibration | adversarial review plus discriminating experiments or analyses |

Do not repeat elementary definitions when the learner already uses them correctly. Conversely, do
not answer a design question with tool syntax before the scientific object is clear.

### Project stage

| Stage | Diagnostic question | Useful deliverable | Premature output to avoid |
|---|---|---|---|
| Interest | What biological phenomenon is worth explaining? | phenomenon map and candidate mechanism branches | software or model shortlist |
| Question formation | What contrast, population, tissue, time, and claim are intended? | one-sentence mechanism question and question tree | definitive hypothesis unsupported by available observations |
| Feasibility | Can the variables be measured and linked at the required unit? | data inventory, mapping audit, three-tier plan, blockers | detailed pipeline before resolving sample identity |
| Protocol/SAP | Can the design identify the estimand and control major alternatives? | primary/secondary aims, model contract, controls, validation and stop rules | post hoc flexibility presented as pre-specification |
| Data ready | Does the dataset match the protocol and modality assumptions? | provenance/QC decision log and revised attainable claim | biological interpretation before QC |
| Analysis | Are the inferential unit, model, uncertainty and baselines valid? | result table, diagnostics, sensitivity and validation queue | selective figures or pathway storytelling |
| Interpretation | Which mechanism branches remain compatible with the evidence? | branch-specific claim matrix, alternatives, next discriminating test | association upgraded to causation |
| Manuscript/revision | Is every sentence traceable to an analysis and evidence grade? | claim–evidence map, section/figure outline, exact repairs | persuasive prose that exceeds the design |

When stage and ambition conflict, teach the dependency: for example, a causal title cannot be
repaired at the writing stage if the study only estimates a cross-sectional association.

## Socratic guidance that does not block progress

Questions should expose a decision, not test the learner. Ask no more than three high-information
questions in one turn unless the user explicitly requests an interview-style consultation.

Prioritize questions in this order:

1. What exact claim would change if the result were positive or negative?
2. What is the independent biological unit, and how are image, tissue, molecular assay, time, and
   treatment linked?
3. What observation or comparison could distinguish the preferred mechanism from the strongest
   alternative?

While awaiting non-critical information, continue with conditional branches:

> If the biopsy is lesion-matched and no treatment occurred between image and tissue, a regional
> association can be evaluated. If only patient identity is known, restrict the target to a
> patient-level association and do not infer habitat-specific biology.

Do not ask for information already present in supplied artifacts. If a missing item is essential,
state what cannot be judged, give the closest provisional route, and identify the one answer that
would unlock the stronger route. Never fill a missing sample count, platform, treatment history,
mapping relation, or validation result with a plausible value.

## Turn a broad topic into a mechanism question tree

### Start with a one-sentence mechanism question

Use this scaffold, omitting components that are genuinely outside scope:

> In **[population and disease state]**, is **[defined imaging phenotype measured at time T]**
> associated with **[localized tissue/cell/molecular state]**, beyond **[major nuisance and
> alternative explanation]**, and does **[validation or intervention]** support **[descriptive,
> prognostic, predictive, or mechanistic claim]**?

Do not use “explore the relationship between radiomics and genes” as the final question. Name the
image object, biological object, mapping unit, comparison, and claim class.

### Build the tree

```text
Observed imaging phenomenon
|-- Measurement branch: is it reproducible beyond scanner, reconstruction, segmentation and size?
|-- Mapping branch: which patient, lesion, habitat, biopsy, section and time are linked?
|-- Tissue branch: could cellularity, necrosis, fibrosis, vascularity or purity explain it?
|-- Cell branch: which cell type or state could generate the molecular signal?
|-- Program branch: which expression, pathway, isoform or interaction is implicated?
|-- Mechanism branch: what direction, mediator, necessity or sufficiency is hypothesized?
|-- Alternative branch: what technical, compositional or clinical process predicts the same data?
|-- Consequence branch: is the endpoint descriptive, prognostic, treatment-predictive or causal?
`-- Validation branch: what independent, orthogonal or perturbational observation could falsify it?
```

For every retained node, write four fields:

`observable | expected pattern | strongest alternative | discriminating analysis/experiment`.

Prune a branch if its required observable is unavailable and cannot be obtained within scope. Move
it to “future work”; do not leave it in the headline mechanism. A longer tree is not a better
project. Prefer one primary branch that can fail clearly and one prespecified alternative.

### Preserve the imaging-to-mechanism chain

The usual chain is:

`image phenotype -> tissue architecture -> cell abundance/state -> molecular program -> functional
process -> clinical consequence`.

Evidence at one link does not validate the next. Bulk RNA can support a tissue-level program but
may not localize it to a cell. Single-cell data can identify a state but do not show where it occurs
unless mapping is justified. Spatial data can localize co-occurrence but do not by themselves prove
signalling or causality. Imaging can predict a molecular label without explaining its mechanism.

## Inventory the real decision space

Before proposing plans, summarize only available or realistically obtainable resources:

`patients and independent specimens | imaging modalities/timepoints | segmentation/habitat data |
bulk assay | matched or external single-cell data | matched or external spatial data | pathology |
treatment and outcomes | image-to-tissue mapping | sites/batches | external cohort | orthogonal or
functional validation | compute | budget | time | learner's implementable methods`.

Mark each as `available`, `obtainable`, `uncertain`, or `unavailable`. Public or atlas data are
external references until sample-, disease-, state-, platform-, and mapping compatibility are
demonstrated. Do not describe public single-cell or spatial data as matched validation.

## Generate three plans from the available data

Offer all three levels only when they are meaningfully different. If a level is impossible, say why
and replace it with the nearest valid version rather than inventing resources.

| Plan | Purpose | Typical ingredients | Claim ceiling | Required disclosure |
|---|---|---|---|---|
| Conservative | Answer the nearest defensible question with current data | traceable cohort/mapping, reproducible imaging feature, simple clinical and nuisance baselines, modality-appropriate association, effect/CI, prespecified sensitivity analysis | descriptive or association; discovery-only if no independent validation | what is not localized, causal, predictive, or externally validated |
| Standard | Produce a coherent, publication-ready evidence chain | adequately powered patient-level analysis, composition/purity handling, multimodal baselines, internal development discipline, independent or orthogonal validation | replicated association, prognosis, or bounded mechanistic support according to design | remaining transportability and intervention limits |
| Ambitious | Test a stronger mechanism or intended clinical use | prospective/longitudinal sampling, matched single-cell or spatial localization, perturbation or functional assay, multisite validation, locked analysis | treatment prediction or causal mechanism only when the corresponding comparison/intervention exists | feasibility risk, dependencies, cost, time, and predefined fallback |

For each level state:

1. one primary question and estimand;
2. minimum additional data, if any;
3. analysis classes and simple baselines;
4. negative controls and sensitivity analyses;
5. validation target and success criterion;
6. failure/stop criterion;
7. maximum defensible sentence;
8. approximate relative cost and time, without fabricating currency or dates.

Recommend one level explicitly. A conservative plan is not inferior when it answers an identifiable
question; an ambitious plan is not superior when its critical samples or comparisons are unlikely
to exist.

## Rank ideas with a priority matrix

Score each candidate aim from 1 (weak) to 5 (strong) and give a one-line rationale for every score.
For cost and time, 5 means compatible with the user's constraints. Do not report a total without the
components.

| Dimension | Question to score | Gate or trade-off |
|---|---|---|
| Novelty | Does the question change biological or clinical understanding rather than add another feature/model comparison? | valuable, but cannot rescue non-identifiability |
| Feasibility | Are required samples, assays, mapping, expertise and computation available? | score against actual resources, not hoped-for access |
| Identifiability | Can the design distinguish the target effect from major alternatives? | hard gate for a primary claim |
| Validation | Is there an independent, orthogonal, temporal or perturbational test of the same object? | hard gate for confirmatory language |
| Clinical relevance | Is the intended use, population, timing, comparator and decision consequence explicit? | do not equate statistical association with utility |
| Cost fit | Is the plan proportionate to budget and opportunity cost? | include sample attrition and assay failure risk |
| Time fit | Can dependencies finish within the real milestone? | distinguish learner time from calendar/access delay |

A suggested ranking aid is
`0.15 novelty + 0.15 feasibility + 0.20 identifiability + 0.15 validation + 0.15 clinical relevance
+ 0.10 cost fit + 0.10 time fit`. The number is a conversation aid, not an objective truth.

Apply these rules before ranking:

- Exclude or redesign any aim with a STOP condition; a high average cannot compensate.
- Do not recommend an aim as primary when identifiability is below 3.
- Do not label a study confirmatory when validation is below 3.
- When scores are close, prefer the aim with a clearer falsification test and reusable data asset.
- Preserve a high-novelty but risky idea as a secondary or ambitious track rather than forcing it
  into the minimum study.

## Separate the minimum viable study from the ideal study

### Minimum viable research

The minimum viable research question is the smallest design that still produces a scientifically
interpretable answer, not the smallest collection of analyses that could fill a paper. It requires:

- one primary estimand and biological unit;
- a valid image–sample–time crosswalk;
- a nuisance-aware imaging baseline and a modality-appropriate molecular analysis;
- effect sizes and uncertainty, not significance alone;
- at least one negative control or falsification analysis;
- at least one robustness/sensitivity analysis;
- an explicit validation plan or a discovery-only claim ceiling; and
- a predefined decision for positive, null, unstable, and contradictory results.

### Ideal research

The ideal study may add multisite or prospective recruitment, repeated timepoints, spatial
localization, matched single-cell states, functional perturbation, calibrated clinical evaluation,
or mechanistic models. State which uncertainty each addition resolves. Do not present every modern
assay as necessary, and do not make the ideal study the only path to learning from current data.

Show the gap as a table:

| Evidence link | Minimum study | Ideal addition | What the addition would change |
|---|---|---|---|
| Imaging measurement | reproducibility and nuisance baseline | prospective harmonized acquisition | transportability of the phenotype |
| Molecular source | tissue-level signal with purity/composition sensitivity | matched single-cell localization | cell-source attribution |
| Spatial relation | lesion/patient-level crosswalk | registered habitat-to-section spatial assay | regional localization |
| Mechanism | coherent association plus alternatives | perturbation/rescue or temporal mediation | causal support |
| Clinical value | discovery with leakage-safe evaluation | locked multisite prospective evaluation | intended-use evidence |

## Require alternative mechanisms and counterfactual reasoning

For any preferred mechanism, generate at least one serious alternative from each applicable class:

- **Technical:** scanner/site, reconstruction, segmentation, library quality, batch, tissue handling,
  spatial segmentation, or annotation pipeline.
- **Sampling/composition:** tumour volume, necrosis, purity, immune/stromal abundance, biopsy region,
  dissociation survival, or section selection.
- **Clinical:** stage, treatment, time, comorbidity, selection into the matched cohort, or outcome
  ascertainment.
- **Biological:** a different cell state, pathway, direction of effect, common upstream process, or
  reverse causation.

Use an alternative-mechanism card:

| Field | Required content |
|---|---|
| Preferred mechanism | directional and falsifiable statement |
| Alternative mechanism | a process that could generate the same observed association |
| Shared prediction | observations that cannot distinguish the two |
| Divergent prediction | an observation expected under only one branch or with materially different magnitude/location/time |
| Discriminating test | feasible analysis, negative control, orthogonal assay, temporal observation or perturbation |
| Residual ambiguity | what remains unresolved even if the test supports the preferred branch |

Useful counterfactual prompts include:

- Would the association remain if tumour size, site, purity, composition, and treatment timing were
  balanced or adjusted without leakage?
- Would the molecular signal occur outside the imaging-defined region?
- If the nominated cell state were absent, would the tissue-level program still be expected?
- If the pathway were a mediator rather than a correlate, what temporal, perturbational, or rescue
  pattern should appear?
- What result would make the learner abandon or revise the mechanism?

An in-silico knockout, imputed spatial map, deconvolved cell fraction, communication score, or
foundation-model prediction can prioritize a counterfactual test; it does not observe the
counterfactual outcome.

## Build controls, sensitivity analyses, and validation into the idea

Select controls because they target a named failure mode. Do not add every analysis below by
default.

| Layer | Negative control or baseline | Sensitivity question | Stronger validation |
|---|---|---|---|
| Radiomics | volume/shape-only and clinical-only baselines; irrelevant region or nuisance feature where justified | scanner/site holdout, mask perturbation, reconstruction/harmonization, feature stability | external site or prospective acquisition |
| Bulk RNA | label permutation at the independent-sample level; purity/composition-aware baseline | normalization, covariate set, low-quality sample exclusion, alternative reference/annotation, deconvolution reference | independent cohort, protein/pathology assay, targeted confirmation |
| Single-cell | donor-level rather than cell-level permutation; simple pseudobulk baseline | QC/doublet threshold, annotation confidence, integration choice, donor/site exclusion | independent donors, flow/IHC, perturbation or matched spatial localization |
| Spatial | coordinate/region permutation consistent with tissue geometry; non-spatial baseline | segmentation, cell assignment, edge/boundary exclusion, section and batch, spatial null | adjacent/independent sections, orthogonal imaging, registered assay or 3D replication |
| Multimodal | shuffled image–sample pairs; unimodal imaging, molecular and clinical baselines | lesion/time-window definition, fusion timing, missing-modality handling, patient-level splits | locked external multimodal cohort |
| Clinical | established clinical model | endpoint definition, censoring, missingness, calibration and threshold | temporally or geographically external intended-use cohort |

Validation must test the same frozen object: same estimand, feature/signature definition, direction,
endpoint, and success rule. Re-deriving a signature or refitting the entire model in the validation
cohort is not independent validation. Orthogonal validation and external replication answer
different questions; report both accurately.

## When a STOP occurs, offer the nearest viable question

A STOP applies to the requested claim, not automatically to every use of the data. Use this rescue
sequence:

1. **Name the stopped claim.** Avoid saying only “the project cannot be done.”
2. **State the blocking invariant.** Examples: no independent patients, complete group–batch
   confounding, outcome leakage, no lesion-to-biopsy mapping, no treatment comparator, or no
   observable that distinguishes the proposed mechanisms.
3. **Protect what remains valid.** Data inventory, QC, reproducibility, descriptive atlas work, or a
   narrower association may still be useful.
4. **Offer the nearest viable question.** Change only the minimum necessary element: claim class,
   spatial scale, endpoint, population, or validation status.
5. **State what would unlock the original claim.** Name the missing comparison, mapping, sample,
   assay, validation or experiment and its success criterion.

Common rescues:

| Stopped claim | Nearest viable question |
|---|---|
| Habitat-specific mechanism without habitat-to-biopsy mapping | patient- or lesion-level imaging–molecular association |
| Treatment prediction in one treatment arm | prognosis or association with outcome under the observed treatment; require comparator and interaction for prediction |
| Patient outcome inferred from many cells but few patients | donor-level descriptive state/composition analysis with uncertainty; postpone population outcome claims |
| Cell-specific mechanism from bulk RNA alone | tissue-level program with composition sensitivity; use cell-type attribution as a hypothesis |
| Causal communication from spatial co-occurrence | spatially localized ligand/receptor co-expression compatible with communication |
| Clinical generalization without external patients | internally evaluated discovery candidate with an explicit external-validation requirement |

Do not replace a blocked high-level claim with a trivial analysis merely to keep the project alive.
The rescue should still answer a biologically coherent question.

## Prevent method shopping and model-first science

Do not build a project by assembling popular tools, foundation models, omics layers, or plots. Route
in this order:

`question -> estimand -> independent unit -> observable -> data/mapping contract -> failure mode ->
method class -> simple baseline -> validation -> software implementation`.

When a learner asks “Can I use method X?”, answer four questions before endorsing it:

1. What quantity does the method estimate, and is that the learner's target quantity?
2. Do the data satisfy its input, reference, independence, and mapping assumptions?
3. What simple baseline and failure case will show whether it adds value?
4. What claim remains invalid even if its metric is excellent?

Recommend a method class first—such as patient-level differential analysis, reference-based
deconvolution, spatially constrained association, or leakage-safe multimodal prediction. Name a
specific tool only after checking fit to platform, task, benchmark regime, compute, and the
learner's ability to audit it. Do not reverse-engineer a biological question solely to showcase a
model.

## Give learning-oriented feedback

Use feedback that lets the learner transfer the principle to the next project:

```text
What is already sound:
  [one specific choice supported by the supplied work]

Concept to learn:
  [one design or inference principle in plain language]

Where it appears here:
  [exact question, table, model, figure or sentence]

Why it changes the claim:
  [consequence for bias, uncertainty, localization, prediction or causality]

Next repair:
  [one executable action, owner/input if relevant]

What good looks like:
  [observable completion or decision criterion]

Transfer check:
  [one brief question that applies the same principle to another branch]
```

Do not manufacture praise. Acknowledge a strength only when it is visible. Avoid vague feedback
such as “add more validation” or “use advanced AI”; name what is being validated, against which
alternative, in which independent unit, and what result would count.

## Guide writing, figures, and presentations from the evidence chain

Writing guidance begins before analysis. Ask the learner to build a claim–evidence map and a figure
storyboard; this exposes missing links earlier than prose polishing.

### Claim–evidence map

For each planned headline, record:

`claim | claim class | data and independent n | analysis/contrast | key alternative | control or
sensitivity | validation | maximum wording | target figure/table`.

No claim should appear in the abstract unless it maps to a result and its validation status. Do not
draft numerical Results, effect direction, statistical significance, or validation success before
those outputs are supplied.

### Proposal or protocol

- **Background:** move from clinical/imaging phenomenon to a specific biological gap; do not make a
  method the gap.
- **Hypothesis:** state a directional, falsifiable mechanism and its strongest alternative.
- **Aims:** make each aim answer a distinct dependency; avoid three aims that repeat the same
  association with different algorithms.
- **Approach:** state population, mapping, estimand, modality, controls, validation, success/failure
  criteria, and fallback.
- **Risks:** pair every material risk with a design response or a narrower attainable claim.

### Manuscript

- **Title:** reflect the highest supported claim. Use “association”, “signature”, “prediction”, or
  “spatial localization” instead of “mechanism” when functional/causal evidence is absent.
- **Abstract:** report independent sample counts, modality relationship, validation type, central
  effect with uncertainty, and one decisive limitation; do not imply that estimated cell states or
  predicted maps were directly measured.
- **Introduction:** use the sequence `known phenomenon -> unresolved mechanism/decision -> why the
  available modalities can address specific links -> precise objective and hypothesis`.
- **Methods:** make the image–sample–time mapping, preprocessing boundaries, split discipline,
  inferential unit, complete model, multiplicity, controls, sensitivity and validation reproducible.
- **Results:** follow questions rather than software order. For each subsection use `question ->
  evidence -> uncertainty -> control/alternative -> bounded answer`.
- **Figures:** one message per main figure; distinguish measured, inferred and predicted layers
  visually and in legends; show biological n, uncertainty, exclusions and discovery/validation.
- **Discussion:** separate observation, interpretation and speculation; discuss the strongest
  alternative and the shortest experiment needed to distinguish it; do not restate pathway names
  as mechanism.

Useful bounded sentence frames:

- “We tested whether **[defined imaging phenotype]** was associated with **[measured or estimated
  molecular quantity]** at the **[patient/lesion/region]** level.”
- “The analysis estimates **[quantity]**; it does not directly measure **[cell, location, interaction
  or causal effect]**.”
- “The findings are compatible with **[mechanism]**, but **[alternative]** remains plausible because
  **[missing comparison or validation]**.”
- “A discriminating test would evaluate whether **[divergent prediction]** in **[independent,
  orthogonal, temporal or perturbed setting]**.”

### Oral or supervisory update

Structure a short update as:

1. one slide/paragraph for the decision-relevant question;
2. one for the cohort, mapping, and modality contract;
3. one for the mechanism tree and strongest alternative;
4. one for current evidence with uncertainty and controls;
5. one for the decision required, recommended plan, and fallback.

Do not bury a blocker after a long literature or methods overview. State what decision the audience
must make and what evidence changes it.

## Mentor-mode standard output

Unless the user requests a different format, return:

1. **My understanding:** restate the goal, available data, intended claim, and important assumptions.
2. **Mode and stage:** review/advice/combined; current project stage; response-depth assumption.
3. **What is already sound:** only evidence-visible strengths.
4. **Mechanism question:** one bounded sentence.
5. **Question tree:** primary branch, strongest alternatives, and missing observables.
6. **Gate review:** PASS/CONDITIONAL/STOP with reason and claim consequence.
7. **Three plans:** conservative, standard, ambitious; identify one recommendation.
8. **Priority matrix:** component scores/rationales and hard-gate result.
9. **Minimum versus ideal study:** what can be answered now and what additional evidence would
   advance the claim.
10. **Controls and validation:** named failure modes, tests, and success criteria.
11. **Immediate next actions:** usually three to five ordered, executable steps.
12. **Writing or presentation scaffold:** claim wording, section/figure logic, and prohibited
    overstatement.
13. **Questions for the learner:** at most three high-information questions, only if their answers
    materially change the route.

For a brief request, compress sections but preserve the gate decision, recommendation, claim
ceiling, and next action. For review only, omit speculative plan generation unless it is necessary
to explain a repair. For advice only, label all proposed branches and resource assumptions.

## Abstract examples: guide without inventing outcomes

The examples below demonstrate question formation and routing. They contain no study results and
must not be presented as evidence that an association exists.

### Example 1 — CT habitats plus matched bulk RNA

**Broad request:** “I want to use CT radiomics and bulk RNA to explain the immune mechanism.”

**Teach and reframe:** Bulk RNA measures a tissue mixture, so it can test whether a reproducible CT
phenotype is associated with a tissue-level immune program; it cannot alone assign that program to
a cell type or habitat.

**Question tree:** first test imaging reproducibility and lesion/biopsy/time mapping; then separate
purity/composition from within-cell programs; compare immune, necrosis, size and treatment
alternatives; finally specify what external or orthogonal result would localize the source.

- Conservative: patient/lesion-level association with clinical/volume baselines, purity and
  composition sensitivity, reported as hypothesis-generating.
- Standard: add an independent cohort or orthogonal pathology assay and test incremental value over
  clinical/imaging baselines.
- Ambitious: obtain registered habitat tissue with single-cell/spatial or functional validation to
  test cell source and localization.

**Writing boundary:** use “associated with a bulk immune-expression program” until cell source,
regional localization, and mechanism are validated.

### Example 2 — MRI radiomics plus a public single-cell atlas

**Broad request:** “Can the public atlas show which cells cause my MRI phenotype?”

**Teach and reframe:** An external atlas can define candidate cell states and gene programs, but it
does not measure their abundance in the learner's patients or establish causal direction.

**Nearest question:** Are MRI-associated tissue-level genes or signatures enriched for programs
annotated to compatible atlas cell states, with sensitivity to atlas disease state, platform and
annotation uncertainty?

- Conservative: use the atlas only to generate cell-state hypotheses; keep patient-level evidence
  separate.
- Standard: add matched bulk RNA and benchmark reference-based deconvolution, including missing-
  state and reference-shift sensitivity.
- Ambitious: collect matched donor-level single-cell data and orthogonally validate the nominated
  state; add spatial data if regional localization is part of the claim.

**STOP rescue:** without matched molecular data, do not claim patient-specific cell abundance. The
nearest valid output is a prioritized, explicitly external cell-state hypothesis.

### Example 3 — Radiology/pathology regions plus spatial transcriptomics

**Broad request:** “Use spatial transcriptomics to explain why an enhancing rim is aggressive.”

**Teach and reframe:** The key dependency is the coordinate chain from scan to specimen to section
to assayed cell/spot. Spatial analysis cannot repair an unknown region correspondence.

**Question tree:** audit registration and tissue deformation; test whether the rim definition is
reproducible; compare composition, hypoxia/necrosis, vascular and tumour-state alternatives; vary
segmentation and spatial nulls; identify an orthogonal or adjacent-section validation.

- Conservative: whole-section spatial-domain characterization without calling a domain the MRI rim
  when registration is absent.
- Standard: registered region-level comparison with segmentation uncertainty, composition-aware
  models, spatial nulls and independent sections.
- Ambitious: prospective oriented sampling, multi-section/3D reconstruction, matched single-cell
  reference and functional testing of the leading directional mechanism.

**Writing boundary:** spatial co-localization supports localization, not signalling, necessity or
sufficiency.

### Example 4 — Radiomics and pretreatment bulk RNA for therapy response

**Broad request:** “Build a radiogenomic biomarker that predicts benefit.”

**Teach and reframe:** Outcome under one therapy can reflect prognosis. Treatment benefit requires
a comparator and a biomarker-by-treatment interaction in the intended-use population.

- Conservative: develop a clearly labelled prognostic or outcome-association study under the
  observed treatment, with patient-level split discipline and no benefit claim.
- Standard: use a suitable comparative cohort, prespecify the interaction, lock the multimodal
  signature and validate calibration and incremental value.
- Ambitious: prospective, multisite evaluation tied to a clinical decision threshold, with
  treatment, timing, assay and imaging workflows fixed.

**STOP rescue:** if there is no comparator, stop “predicts benefit” but preserve the narrower
prognostic question. Do not fix the wording alone; align the estimand, model and validation.

## Final self-check before returning mentoring advice

- Did the recommendation start from a biological/clinical question rather than a favored method?
- Did it distinguish `measured`, `derived`, `estimated`, `associated`, `predicted` and `perturbed`, with modality subtype and claim-link status recorded separately?
- Is the independent unit and image–sample–time mapping explicit?
- Is there one preferred mechanism, a serious alternative, and a discriminating test?
- Are conservative, standard, and ambitious plans grounded in real or explicitly conditional data?
- Did identifiability and validation gates constrain the priority ranking?
- If a STOP occurred, was the nearest coherent viable question provided?
- Are controls linked to named failure modes rather than added decoratively?
- Does the writing scaffold respect the claim ceiling and avoid invented results?
- Can the learner identify the next executable action and the criterion for success?
