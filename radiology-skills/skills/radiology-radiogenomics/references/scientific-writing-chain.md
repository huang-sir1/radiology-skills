# Scientific writing chain for radiomics and mechanism research

Use this module for manuscript planning, section drafting, scientific rewriting, compression,
cross-artifact consistency review, or evidence-bounded response text. It applies to `imaging-only`,
`mechanism-only`, and `imaging-mechanism` studies. Writing is evidence propagation, not a late
language-polishing step.

Scientific facts are constrained by the author's source artifacts, data and verifiable evidence.
No skill owns scientific facts. Within this task, `radiology-radiogenomics` maintains the domain ledger for study
topology, independent unit, matched intersection, modality roles, evidence state, claim branch,
claim ceiling, decisive alternatives and reporting facts. The same skill can complete the scientific
writing chain locally. When another internal module receives a frozen packet, it preserves that
source-bounded state while improving architecture, language or reporting.

## 1. Detect the writing entry point

Do not force an author to restart the whole pipeline. Select the narrowest entry point that can
produce the requested artifact:

| `writing_job` | Material available | Immediate product | Upstream facts that must still be checked |
|---|---|---|---|
| `argument-map` | question, protocol, or result summary | one-sentence argument and claim-to-section/evidence map | scope, estimand, units, decisive evidence, claim ceiling |
| `section-draft` | locked evidence plus one or more named sections | ready-to-paste section(s) | claims assigned to evidence and canonical terminology |
| `scientific-rewrite` | existing prose plus evidence | bounded rewrite and change log | source traceability, claim verb, downstream dependencies |
| `evidence-compression` | overgrown draft | shortest sufficient main-text chain and relocation map | conclusion-changing evidence must remain visible |
| `language-polish-handoff` | scientifically stable prose and allocation | immutable scientific packet for a polishing skill | W8 fidelity and consistency gates |
| `consistency-audit` | near-final manuscript package | discrepancies and exact repairs | text, tables, figures, legends, supplement, availability and abstract |

If only prose is supplied, do not infer that the reported analyses or experiments occurred. Mark
untraceable facts `AUTHOR_INPUT_NEEDED` or `W-RETURN-TO-LEDGER: source required`.

For Results drafting from `user-description` alone, return `W-RETURN-TO-LEDGER` unless traceable result
facts are supplied. A structural scaffold with placeholders is allowed; a fluent Results narrative
that implies completed analyses, numerical findings or validation is not.

### Interaction-mode overlay

Apply this overlay before W0; it changes the artifact and teaching depth, not the scientific threshold:

| Mode | Writing behavior | Required components |
|---|---|---|
| `reviewer` | inspect and diagnose supplied writing; do not default to expanding or ghostwriting the paper | Preset D scientific map plus Preset A typed locations, claim consequence, exact repair and closure criterion; revised wording only for the bounded passage requested |
| `mentor` | teach why the architecture works and help the learner choose | Preset D architecture plus Preset B principle, options/trade-offs, recommendation, next action and success/failure criterion; use scaffolds when result facts are missing |
| `combined` | review first, freeze valid claims/text, then revise only affected nodes | Preset E order followed by the affected part of Preset D; preserve/repair/retire and a change log are mandatory |

For “review then rewrite,” complete the reviewer overlay and freeze finding/claim IDs before changing
text. A fluent rewrite cannot erase a finding or silently adopt an optional experiment.

## 2. Writing chain

### W0 — Lock the writing contract

Record:

- study scope, interaction mode, manuscript stage and requested artifact;
- article type, primary reader and target venue if supplied;
- central question, estimand, comparator, time zero and intended use where applicable;
- independent biological unit, total n, matched n and observation hierarchy;
- active, external-reference, generated/predicted and proposed-validation modalities;
- selected claim branch or branches and their current `PASS / CONDITIONAL / STOP` verdicts;
- available source artifacts and facts that remain author assertions.

Venue prestige changes emphasis and compression, not the evidence threshold. Current journal format
requirements must be checked by the reporting/submission skill rather than guessed here.

### W1 — Freeze the source-bound scientific state

Before drafting fluent prose, complete or inspect the claim ledger. Every material sentence must be
traceable to:

`Claim ID -> evidence pointer -> primary evidence state -> modality subtype -> claim-link status ->
independent unit and n -> effect/uncertainty -> claim branch -> branch verdict -> maximum wording ->
boundary or rival explanation`.

Use `measured / derived / estimated / associated / predicted / perturbed` as positive evidence
states and `direct / inferred / proposed` as the relationship to the exact claim. `missing` is an
absence marker, not a positive state. Do not let a software-derived label, enrichment, saliency map,
cell-state transfer, deconvolution, reconstructed spatial layer, virtual perturbation or language
model narrative become a measured mechanism through prose.

Freeze a terminology and units ledger:

- cohort and subset names;
- patient, lesion, region/habitat, block, section, cell/spot and time-point terms;
- imaging phenotype, model and validation-set names;
- assay, cell-state, program, pathway and perturbation names;
- endpoint definitions, reference categories and effect directions;
- the verbs allowed for each claim.

Technical repetition is preferable to synonym cycling when a different word could imply a different
biological object or evidence state.

Assign one ledger status after this gate:

- `W-LEDGER-READY`: the source, units, evidence three-axis fields, claim branches and ceilings are
  sufficiently locked to begin argument and placement work;
- `W-RETURN-TO-LEDGER`: a missing source, invalid analysis premise or unresolved claim branch blocks
  truthful drafting; return to the scientific ledger before prose generation.

These are writing-workflow states, not claim verdicts or finding severity. Keep them separate from
`PASS / CONDITIONAL / STOP` and `P0 / P1 / P2`.

### W2 — Define the contribution and argument

Write one bounded sentence:

`In [population/system and context], we show [principal advance] using [design and modalities],
supported by [decisive evidence], with [most important boundary].`

Then decompose it into no more claims than the evidence requires:

1. the phenomenon or technical object established;
2. the principal association, localization, prediction, treatment-effect, mechanism or causal claim;
3. the decisive robustness, validation or discrimination evidence;
4. the boundary that prevents a stronger interpretation.

For each subclaim, state what readers knew before, what this study changes, and which result makes
that delta defensible. Novelty is a comparison to relevant prior knowledge, not a synonym for a new
algorithm, assay or multimodal combination.

### W3 — Classify and place evidence

Classify each result before choosing its location:

| Evidence role | Default placement | Placement rule |
|---|---|---|
| Core discovery | main Results and principal figure/table | must be visible without opening the supplement |
| Necessary support | main text, legend, or immediately linked table | keep with the claim whose validity depends on it |
| Qualification or boundary | main Results/Discussion when it changes interpretation | never bury conclusion-changing discordance or failure |
| Robustness or sensitivity | main text if decision-bearing; otherwise supplement with a main-text pointer | report enough result, not only that the check was done |
| Heterogeneity or failure case | main text when it limits transport or intended use | do not select only favorable strata |
| Provenance detail | Methods, flow diagram, supplement, data/code statement | retain enough in the main Methods to reconstruct the chain |
| Alternative inference | Results or Discussion according to whether directly tested | separate tested alternatives from proposed explanations |
| Edge case or exploratory extension | supplement or explicitly exploratory subsection | cannot carry the abstract or title claim |

Build the shortest sufficient evidence chain. More analyses do not compensate for an unidentifiable
estimand, leakage, a mismatched tissue-image pair, donor pseudoreplication, failed target engagement,
or missing independent validation.

### W3b — Stress-test material claims from a reviewer perspective

Before prose drafting, run one claim-linked stress test. This is not a generic checklist and does not
authorize fashionable extra experiments. For each material claim ask only the applicable questions:

1. **Contribution:** what current, fair prior method or biological explanation makes this advance
   non-trivial, and has the manuscript stated the actual delta rather than novelty-by-combination?
2. **Identification:** could cohort selection, unit inflation, leakage, batch, treatment timing,
   tissue-image mismatch or composition produce the result?
3. **Attribution:** for a method claim, which ablation or comparator isolates the advertised
   contribution; for a mechanism claim, which rival explanation produces the same pattern?
4. **Transport:** what has actually been tested across site, scanner, platform, donor, disease
   spectrum or condition, and what remains internal or out-of-distribution?
5. **Traceability:** can a reviewer locate the method, result, uncertainty, figure/table and data/code
   artifact needed to verify the response?

Record `likely concern -> governing criterion -> current evidence -> pre-emptive manuscript action ->
claim consequence if unresolved`. A concern already closed by visible evidence needs better placement,
not a redundant analysis. A concern that is inapplicable to the article type or declared claim is marked
`NOT APPLICABLE`, not converted into an experiment. Use the transparent-review lessons reference for
corpus-derived examples, but load the paper-level TSV only for evidence tracing.

After W0–W3, continue directly to W4–W8 when this skill is producing the requested writing artifact
itself. Assign `W-HANDOFF-READY` only when a shared state will actually pass to another internal
module and the claim-to-section allocation, protected placement, terminology and packet are complete.
Build that packet from `../templates/scientific-writing-handoff-packet.template.json`, apply
`scientific-handoff-contract.md`, and run
`../scripts/validate_scientific_handoff.py --require-ready`. If the supplied prose still needs
bounded scientific repair, use `W-REVISE` until those affected allocations are resolved.

When `radiology-writing` receives an existing packet, it must validate and preserve it. When a user
enters `radiology-writing` directly without a packet, that module may build a minimal local
claim–evidence map from supplied artifacts and proceed with defensible sections; it blocks only the
specific untraceable claim, result or mechanism statement. The packet is an interoperability
contract for composition, not permission from a superior skill to begin work.

### W4 — Build the Results and figure spine first

For an empirical original-research manuscript, lock Methods facts before writing but draft the
scientific story from the Results and display items. For a protocol, resource, review or other article
type, use its real evidence/product spine and section jobs; never invent a Results section merely to
fit this sequence.
For each Results subsection use one question and one new claim:

`sample/analysis set -> observed result -> effect and uncertainty -> decisive robustness or
validation -> discordance/alternative -> bounded local interpretation`.

The order may shorten when a component is not applicable, but it must not skip a decision-bearing
negative result. Lead with the finding, not with a test name. Separate patient/donor counts from
lesions, sections, cells, spots, ROIs, tiles, reads or repeated observations.

Every figure or table needs a declared job: establish the cohort, validate the measurement, answer a
primary question, test an alternative, demonstrate transport, or delimit failure. If two displays
make the same inferential point at the same level, combine, relocate or remove one unless the second
is a necessary independent replication.

### W5 — Draft Introduction and Methods around the locked evidence

#### Introduction

Use the sequence:

`important problem -> specific known phenomenon -> what prior work establishes -> exact unresolved
distinction -> study question/hypothesis -> evidence route`.

Draft backward from the Results. The gap must be answerable by the actual cohort and design. Do not
promise causal mechanism, treatment benefit, single-cell resolution, spatial localization or
clinical deployment when the study delivers only association, prediction, transferred annotation or
retrospective performance.

#### Methods

Methods are the reconstruction contract, not a software inventory. At minimum make visible:

1. eligibility, sampling, exclusions, missing modalities and cohort flow;
2. patient/lesion/specimen/region/section/time/treatment mapping and the independent unit;
3. acquisition, tissue handling, assay/platform, preprocessing, QC, annotation and versioned parameters;
4. which layers were measured, derived, estimated, associated, predicted or perturbed;
5. estimand, contrasts, covariates, nesting, missingness, multiplicity and uncertainty procedure;
6. train-only operations, patient-level splits, tuning, baselines, calibration and external validation;
7. sensitivity analyses, negative controls, orthogonal validation and perturbation checks;
8. ethics, registration, data/code/accession and access restrictions.

State a scientifically consequential choice directly; a package citation or “default parameters” is
not a substitute. Use the active modality playbook for assay-specific requirements.

### W6 — Write Discussion and conclusion as bounded synthesis

Use this sequence:

`compressed answer -> cross-result synthesis -> relation to prior evidence -> competing biological
and technical explanations -> clinical/scientific meaning -> generalizability and limitations ->
next discriminating observation or experiment`.

Do not repeat the Results at the same level. The Discussion must explain what the combined evidence
changes and why the most serious alternatives remain plausible or were weakened. Distinguish a
limitation that narrows scope from a defect that invalidates the headline claim; a limitation
paragraph cannot rescue a `STOP` claim.

The conclusion states the knowledge delta and the claim ceiling. It must not introduce a new endpoint,
population, mechanism, validation set or causal verb.

### W7 — Write title and abstract after the body stabilizes

The title names the true design, population/system and principal contribution without using a
stronger claim branch than the paper supports. Avoid “non-invasive biopsy,” “predicts treatment
response,” “reveals mechanism,” or “drives” unless the corresponding branch requirements pass.

Write the abstract last:

`precise gap -> answer-enabling design and independent n -> primary effect with uncertainty ->
decisive validation/robustness and relevant negative result -> bounded conclusion`.

Every number and claim in the abstract must have a matching body location. Do not use the abstract to
hide cohort attrition, internal-only validation, spatial mismatch, generated evidence status or a
failed mechanism link that changes interpretation.

### W8 — Run scientific and cross-artifact gates before polishing

| Gate | Acceptance criterion | Repair when not met |
|---|---|---|
| Scientific truth | every material claim has a source pointer and valid analysis premise | obtain source/reanalysis, remove, or mark author input |
| Claim-verb | wording does not exceed branch verdict or evidence state | weaken verb or add the missing discriminating evidence |
| Unit and denominator | n and hierarchy agree across all artifacts | reconcile flow, labels, tables, legends and prose |
| Section job | every paragraph advances the section's scientific job | delete, merge, relocate or rewrite |
| Evidence placement | decisive support, discordance and boundaries remain visible | restore to main text or add a precise pointer |
| Modality visibility | measured, external, generated and proposed layers remain distinguishable | relabel text, panels, tables and legends |
| Cross-artifact consistency | title, abstract, text, figures, tables, supplement and availability agree | use stable claim IDs and correct every dependent location |
| Reproducibility | another investigator can reconstruct sampling, processing and inference | add missing provenance, parameters and artifacts |
| Integrity | citations, ethics, accessions, analyses and experiments are not invented | verify, disclose uncertainty or remove |

Only after these gates pass should a language-polishing skill optimize concision, rhythm, grammar and
venue-appropriate register. Do not import arbitrary punctuation quotas or generic style preferences
when they conflict with precise scientific reporting.

After all applicable W8 gates meet their acceptance criteria, assign `W-POLISH-READY`. A manuscript
may be `W-HANDOFF-READY` for structural drafting but not yet `W-POLISH-READY` for final language work.

### W9 — Complete internal module and release composition

The scientific writing chain ends with explicit, non-overlapping handoffs:

- **Literature/citations:** verify both that each citation exists and that it supports the attached
  sentence; use the literature/citation skill for live retrieval and metadata.
- **Statistics:** preserve the independent-unit and estimand packet when checking numerical reporting,
  model assumptions, effects, intervals, multiplicity and legends.
- **Figures/tables:** transmit claim IDs, denominators, evidence states, display jobs and source-data
  pointers; visual polish cannot remove failure cases or uncertainty.
- **Reporting/ethics/data:** check the appropriate reporting guideline, approvals, registration,
  accessions, code/data availability and controlled-access language.
- **Journal/submission:** after the scientific manuscript stabilizes, send the explicit upload root,
  target journal, exact article type and stage to `radiology-submission`. That separate route refreshes
  the current guide, closes the inventory in both directions, verifies actual file types and renders
  all human-facing files. Initial submission, revision and production packages are distinct jobs;
  published exemplars can guide house style but cannot create a hard file requirement.

Each receiving module returns changed locations, preserved scientific facts, unresolved fields and a
Claim-ID drift ledger under `scientific-handoff-contract.md`. The immutable packet contains claim
IDs, branch/verdict/ceiling, all three
evidence axes, independent unit/n, effects/uncertainty and protected evidence placement. Writer-editable
elements are paragraph order, transitions, syntax and compression that does not alter protected
placement. A module request to change an immutable field returns to this chain; it is never silently
accepted. Reopen W1 when a receiving artifact conflicts with the locked ledger.

## 3. Scope-aware writing contracts

| Scope | What the narrative must establish | Prohibited shortcut | Required boundary language |
|---|---|---|---|
| imaging-only | clinically or technically meaningful imaging phenotype/model, leakage-free pipeline, comparator, uncertainty and validation | treating an imaging correlate as an unmeasured molecular mechanism or “biopsy” | name retrospective design, validation level, site/scanner spectrum and intended-use limit |
| mechanism-only | valid biological system, donor/patient replication, assay state, alternatives and evidence appropriate to the mechanistic/causal branch | requiring an imaging link or turning enrichment, pseudotime, communication score or virtual perturbation into mechanism | name measured versus inferred layers, system/context and untested causal links |
| imaging-mechanism | matched intersection, imaging physical meaning, tissue/cell/molecular bridge, scale/time compatibility, discordance and discriminating validation | parallel imaging and omics results presented as a connected mechanism | distinguish patient-level association, regional concordance, mechanistic support and causal evidence |

Additional modality constraints come from the active bulk RNA, single-cell, spatial, multi-omics,
pathology, radiomics, fusion or perturbation playbook. For multi-omics writing, make the usable
matched intersection, blockwise QC, missing-modality handling, unimodal/paired ablation, integration
sensitivity, latent-factor evidence state and incremental-value consequence visible. A proposed
future assay belongs in future work, not in the past-tense Methods or Results.

## 4. Claim-branch language control

Claims are parallel branches, not a mandatory ladder. A prediction claim may pass while mechanism
stops; a localization claim may pass without causality.

| Branch | Usually safe verbs when requirements pass | Wording that needs additional evidence |
|---|---|---|
| Technical validity | reproducible, stable under, calibrated, externally evaluated | clinically useful, generalizable to all sites |
| Descriptive | observed, detected, differed, characterized | explains, mediates, drives |
| Association | associated with, correlated with, linked at patient level | localizes, predicts benefit, causes |
| Localization/concordance | co-localized, regionally concordant, mapped at declared resolution | cell-specific cause, direct interaction |
| Prognostic prediction | predicted outcome in the declared setting, added prognostic information | predicts treatment benefit, changes care |
| Treatment effect | modified the treatment association/effect under the identified design | confers sensitivity without comparator and interaction evidence |
| Mechanistic | supports a mechanism in the tested system; target engagement altered the mediator and phenotype | universal mechanism or clinical causation |
| Causal | caused/mediated only for the identified intervention, system and estimand | transport beyond tested context without evidence |

## 5. Paragraph and revision discipline

Give each paragraph one job: context, gap, design, result, robustness, comparison, mechanism,
alternative, implication or limitation. Ask:

- If removed, does the argument lose evidence or necessary context?
- Can the reader identify the paragraph's claim, evidence and boundary?
- Is it repeating a figure, statistic or conclusion already stated at the same level?
- Does a new sentence require deletion, replacement or relocation elsewhere?

For a targeted revision, freeze accepted claims and terminology, identify affected claim IDs, trace
their dependencies, patch only affected text and displays, then rerun the cross-artifact gates. A
new analysis or stronger claim reopens the relevant Methods, Results, legend, abstract and Discussion
locations. A response-letter promise alone is not a manuscript change.

## 6. Output contract

Return the smallest complete writing artifact requested, plus:

1. route, writing entry point and evidence boundary;
2. writing-workflow status (`W-LEDGER-READY`, `W-REVISE`, `W-HANDOFF-READY`,
   `W-POLISH-READY`, or `W-RETURN-TO-LEDGER`) and the locked one-sentence argument or affected claim IDs;
3. ready-to-paste text or a section/evidence architecture;
4. material terminology, unit and claim-verb decisions;
5. content moved to or from figures, legends, Methods or supplement;
6. `AUTHOR_INPUT_NEEDED`, `W-RETURN-TO-LEDGER: source required`, or new-analysis requirements;
7. scientific gates run and any residual claim ceiling;
8. next internal module: style, statistics, reporting, figures/tables, citations or submission.

Use [the claim-to-section writing map](../templates/claim-to-section-writing-map.md)
when a reusable pre-draft or revision artifact will help. Do not fill every section when the user asks
for one paragraph, one figure narrative or one bounded rewrite.
