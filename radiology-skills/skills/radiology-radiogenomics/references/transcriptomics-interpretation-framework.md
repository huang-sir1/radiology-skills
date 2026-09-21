# Transcriptomics research guidance framework

Use this reference when a standalone mechanism or imaging-mechanism task requires biological
planning, execution guidance, review, interpretation, scientific judgement or writing for
**bulk RNA-seq, scRNA-seq/snRNA-seq, or spatial transcriptomics**. The skill must move from a
scientific question to an auditable analysis and a bounded claim; it must not reduce the work to a
fixed software recipe, a collection of UMAP plots or a post-hoc biological story.

For `study_scope == mechanism-only`, use this framework and the relevant modality playbook without
requesting an imaging study, radiomic feature, imaging habitat, sample-to-image map or
tissue-to-image registration. When and only when `study_scope == imaging-mechanism`, also open
[radiomics-mechanism-bridge.md](radiomics-mechanism-bridge.md); molecular interpretation
must then be linked to the same patient, lesion, region, time and biological scale rather than added
as a parallel narrative.

## Governing chain

```text
scientific question -> data and sample contract -> unit of inference -> assay-aware QC
-> modality-specific inference -> branch-specific validation -> calibrated claim
```

Apply these invariants in every mode:

- Define the contrast, endpoint, tissue region, time point, treatment context, and intended claim
  before selecting a method.
- Treat the independent biological sample or patient as the inferential unit. Cells and spots are
  repeated observations nested within samples, not independent patient replicates.
- Record three independent fields for every result: `primary_evidence_state`,
  `modality_subtype`, and `claim_link_status`. The only primary evidence states are
  **measured**, **derived**, **estimated**, **associated**, **predicted**, and **perturbed**;
  `missing` means that evidence does not exist and is never a positive state. Do not allow an
  imputed, deconvolved, mapped, derived, or simulated value to silently become a measurement.
- Separate discovery, tuning, and validation. Fit data-dependent filtering, signatures, thresholds,
  harmonization, and predictive models without using the held-out cohort.
- When `study_scope == imaging-mechanism` only, preserve tissue-to-image provenance: patient,
  lesion, biopsy/section, region/habitat, collection time, treatment interval, and registration
  uncertainty. Do not add these fields to a mechanism-only request.

## Operating model: five actions, not interpretation alone

Route every request through one or more of these actions. Do not substitute one action for another.

| Action | What the skill must do | Required deliverable |
|---|---|---|
| **Expand** | Turn the user's broad biological idea into testable questions, estimands, contrasts, units, decision branches and a minimal evidence plan | question tree, estimand table, data requirements and analysis branches |
| **Review** | Audit study design, metadata, preprocessing, model assumptions, outputs, figures and prose against assay-specific constraints | severity-ranked findings with evidence location, consequence and repair |
| **Explain** | Translate an output into biological meaning while keeping the three evidence axes separate | finding-to-evidence map, alternatives and uncertainty |
| **Judge** | Decide whether each analysis or claim is supported, conditionally usable, or blocked | `PASS / CONDITIONAL / STOP` decision with explicit criterion |
| **Help** | Produce the next usable artifact: analysis plan, missing-data request, sensitivity analysis, revised paragraph, figure legend, reviewer response or validation experiment | concrete repair or draft, not only criticism |

For a combined request, use the order `expand -> review -> explain -> judge -> help`. If the user
provides only final figures or prose, reconstruct the upstream assumptions but label them as
unverified rather than pretending that the raw-data stages were audited.

## Research modes the skill should route

| Mode | User intent | Minimum useful output |
|---|---|---|
| Intake and feasibility | "Can these data answer my question?" | data passport, matched sample count, missing metadata, blocking limitations |
| Analysis design | "How should I analyse this study?" | estimand, contrast, unit of inference, baseline ladder, validation and multiplicity plan |
| Result interpretation | "What do these outputs mean biologically?" | three-axis finding map, alternative explanations, applicable claim branch and unmet requirement |
| Cross-modal integration | "How do bulk, single-cell and spatial evidence agree?" | triangulation table with concordance, discordance, scale mismatch and uncertainty; include imaging only when `study_scope == imaging-mechanism` |
| Virtual experiment | "Can I simulate a cell, knockout or spatial map?" | task class, measured versus generated inputs, simple baseline, OOD test and experimental boundary |
| Manuscript or reviewer audit | "Are these claims defensible?" | blockers, overclaims, missing controls, reproducibility gaps and exact repair actions |

## Stage-gated guidance workflow

Use gates to prevent an attractive downstream result from hiding an invalid upstream design. Each
gate ends in `PASS`, `CONDITIONAL` or `STOP`.

| Gate | Core question | PASS requires | CONDITIONAL means | STOP examples | Output |
|---|---|---|---|---|---|
| G0 request routing | What decision or deliverable is needed? | modality, study stage and requested action are known | reasonable assumptions are explicitly listed | mutually incompatible goals remain unresolved | task contract |
| G1 scientific estimand | What population-level quantity or relationship is being estimated? | contrast, endpoint, unit, time and claim target are explicit | exploratory objective with bounded language | no definable comparison or endpoint | question tree and estimand |
| G2 data fitness | Can the available data identify that estimand? | independent samples, provenance, metadata and assay layer are adequate | missing non-critical metadata or limited generalizability | pseudoreplication, complete batch-biology confounding, wrong data layer or irrecoverable mapping | data/sample passport and gap list |
| G3 analysis contract | Does the proposed analysis match the data and question? | model, covariates, filtering, baseline, multiplicity and validation are prespecified | defensible sensitivity analysis can address a weakness | outcome leakage, test-set tuning, circular marker/signature reuse or incompatible null hypothesis | analysis plan and baseline ladder |
| G4 execution audit | Were inputs and outputs generated as claimed? | versions, parameters, sample retention and QC are traceable | partial reproducibility with recoverable omissions | unverifiable processing, silent sample loss or result/data mismatch | QC and reproducibility ledger |
| G5 result interrogation | Is the signal robust and what else could create it? | effect, uncertainty, donor consistency and key sensitivities agree | result is method-, threshold- or subgroup-dependent | direction reversal, single-donor dominance or failed negative control | finding-to-evidence table |
| G6 triangulation | Do the active modalities support the same biological statement at compatible scales? | concordance with provenance and scale compatibility | useful but indirect or spatially mismatched support | generated or deconvolved layer is presented as independent measurement | concordance/discordance matrix |
| G7 validation and claim | Which claim branch is being tested, and are its own requirements met? | every mandatory requirement in that branch is traceable | a bounded preliminary claim with named unmet requirements | the requested branch lacks a defining design element, such as held-out data for prediction or intervention/identification for causality | branch decision and next requirement |
| G8 writing and release | Does the manuscript faithfully report the evidence chain? | Methods, Results, legends, Discussion and availability are aligned | wording can be repaired without new analysis | fabricated/untraceable values or text that contradicts the analysis | revised text and release checklist |

For a composite or headline claim, use the **most restrictive verdict** across every required gate
and active modality route. A PASS in one modality cannot override a required spatial-mapping STOP; agreement
between several indirect estimates cannot promote the headline above their weakest
claim-determining link. Report valid subsidiary findings separately when the headline is blocked.

### Universal stop rules

Do not continue to a stronger inferential claim when any of the following remains unresolved:

- cells, spots, tiles or technical replicates are used as independent patient replicates;
- biological condition is completely confounded with batch, site, platform or processing date;
- normalization, feature selection, signature construction, harmonization or threshold selection used
  held-out outcomes or was fitted before the train/test split;
- an integrated embedding, imputed matrix, deconvolved fraction, mapped cell, virtual slice or
  predicted perturbation is reported as a direct measurement;
- the molecular sample cannot be linked to the claimed patient, specimen, tissue region or time
  point; when `study_scope == imaging-mechanism`, this also includes the claimed lesion and imaging
  acquisition;
- a treatment-benefit or effect-modification claim lacks a treatment comparator and explicit
  biomarker-by-treatment interaction; an outcome/response prediction under one observed regimen
  lacks held-out validation and must not be relabelled as differential treatment benefit;
- key sample counts, exclusions, data versions or statistical tests cannot be reconstructed.

When a stop rule fires, preserve any valid result outside the blocked branch, narrow the claim,
state what is not identifiable, and propose the shortest feasible repair. Do not manufacture a complete workflow
from absent metadata.

## Standard execution card for every concrete topic

The modality playbooks expand each literature-derived topic with the same eight fields:

1. `Question to expand` — the biological question and its competing estimands.
2. `Inputs and preconditions` — data objects, metadata and independent units required.
3. `Review checks` — design, QC, model, benchmark and reproducibility checks.
4. `Decision rule` — explicit `PASS / CONDITIONAL / STOP` criteria.
5. `Interpretation boundary` — what may and may not be inferred.
6. `Repair/help` — the next analysis, control, metadata request or experiment.
7. `Writing contract` — minimum Methods, Results, legend and Discussion content.
8. `Evidence map` — eligible papers whose concrete content changed the rule, including limitations.

## Direction 1: question, design and data passport

The skill should first reconstruct the experiment rather than infer it from filenames.

Capture:

`Question | Assay/platform | Raw or processed input | Biological sample/patient | Cells/spots per sample | Tissue/region | Time/treatment | Batch/site | Clinical endpoint | Validation cohort`

When `study_scope == imaging-mechanism` only, append
`Imaging study | Lesion/region linkage | Scan-to-tissue interval | Registration uncertainty`.

The first gate asks whether the available data can support the intended level of inference. A
cross-sectional atlas cannot establish treatment response; one section cannot represent a whole
tumour; and many cells from one patient do not create a large clinical cohort.

## Direction 2: bulk RNA-seq research route

Guide the researcher through eight linked questions:

1. **What molecular feature does the matrix represent?** Record genome and annotation versions,
   strandedness, short- versus long-read assay, alignment or pseudoalignment route, and whether the
   feature is a gene, transcript, exon, splice junction or de novo assembly. Route gene-level DE,
   isoform/usage, alternative-splicing and assembly questions separately.
2. **Is the sample-level contrast valid?** Check biological replication, covariates, pairing,
   longitudinal structure, tissue purity, RNA quality, platform and batch.
3. **What is changing?** Use leakage-safe filtering/normalization and an explicit model to estimate
   differential expression with effect sizes, uncertainty and multiplicity control.
4. **Which biological programs change?** For over-representation analysis, define the tested-gene
   universe; for preranked enrichment, record the ranking statistic and direction. Version the gene
   sets, address redundancy, report leading genes, and do not compare single-sample scores across
   cohorts without checking scale and preprocessing. Fit any score-based predictor inside training
   folds. A co-expression module is neither a regulatory network nor a causal mechanism and may be
   driven by cell composition.
5. **Is composition driving the signal?** Evaluate tumour purity and cell-type mixture; when using
   deconvolution, audit reference choice, reference-to-bulk shift, transcriptome-size effects, rare
   cell performance and uncertainty.
6. **Do transcript usage or splicing change without gene-level DE?** Require compatible counts,
   coverage and task-specific null hypotheses; validate important isoforms or junctions separately.
7. **Does the signal matter clinically?** Separate prognostic association from treatment-predictive
   interaction; require locked signatures and independent validation for prediction.
8. **Can another modality localize the signal?** Use single-cell to identify the cellular source and
   spatial data or orthogonal assays to determine where the program occurs.

Core outputs are a feature-generation passport, sample-level contrast and transcript-usage tables,
pathway/program map, composition sensitivity analysis, clinical association or interaction table,
and bounded biological narrative.

## Direction 3: single-cell and single-nucleus research route

The skill should guide ten decisions:

1. Data-layer contract: record UMI versus non-UMI assay, raw counts, normalized expression,
   selected features, scaled values and integrated embeddings as distinct objects with distinct
   purposes. Do not run differential expression on an integrated embedding or silently replace raw
   counts with batch-corrected expression.
2. Assay-aware QC: empty droplets, ambient RNA, doublets, depth, detected genes, mitochondrial
   signal and sample-specific outliers.
3. Integration purpose: visualization, reference mapping, label transfer or cross-study atlas
   construction. Batch mixing alone is not proof of good integration. For DE, return to counts and
   model donor/batch; when biology and batch are completely confounded, state that the effect is not
   identifiable rather than claiming that harmonization recovered it.
4. Annotation level: cell class, subtype and state; record marker evidence, reference agreement,
   uncertainty, doublets and unresolved populations.
5. Weak-label and malignancy logic: a patient-level disease label is a weak cell-level label, not a
   property of every cell from that patient. Disease-relevant or malignant cells require negative
   references, dedicated evidence and independent validation. RNA-derived CNV is not DNA truth.
6. Patient-level composition: test differential abundance across biological samples rather than
   comparing pooled cells.
7. Patient-level expression: use pseudobulk or a justified sample-aware model; report effect sizes,
   donor consistency and within-cell-type heterogeneity.
8. Dynamic inference: distinguish observed time series, pseudotime, RNA velocity and lineage tracing;
   trajectories require sensitivity analysis and preferably orthogonal validation.
9. Regulatory and communication hypotheses: distinguish co-expression, inferred regulation,
   ligand-receptor compatibility and experimentally demonstrated signaling.
10. Perturbation analysis: separate observed Perturb-seq effects from predicted responses and test
   cross-cell-type, cross-condition and out-of-distribution generalization.

Core outputs are a data-layer passport, cell-state dictionary, sample-by-cell-state composition
table, patient-level differential program table, weak-label/CNV warning where applicable,
uncertainty register, and validation-ready mechanistic hypotheses.

## Direction 4: spatial transcriptomics research route

Spatial analysis requires a technology and tissue model before it requires an algorithm.

Guide the researcher through:

1. **Platform/resolution and reproducibility contract:** sequencing- versus in situ
   microscopy-based,
   spot/bin/cell/subcellular
   resolution, whole-transcriptome versus targeted panel, fresh-frozen versus FFPE, and effective
   rather than advertised resolution. Record protocol/software versions, site, panel, sensitivity,
   specificity, dynamic range, signal-to-noise and cross-site or replicate concordance.
2. **Tissue and spatial QC:** coverage, tissue folds, necrosis, edge effects, local outliers,
   transcript spillover, segmentation errors, panel sensitivity/specificity and section damage.
3. **Segmentation uncertainty propagation:** before cell-level DE, neighborhood or communication
   analysis, compare an alternative segmentation or segmentation-free route where feasible and run
   a segmentation perturbation/correction sensitivity analysis. Carry stability into the applicable
   claim branch; a single segmentation output is not ground truth.
4. **Coordinate and registration chain:** for every spatial study, trace transcript coordinates ->
   cell/spot -> assay-native microscopy or histology -> tissue region. Only when
   `study_scope == imaging-mechanism`, extend the chain to a radiology imaging habitat and quantify
   or at least bound that additional registration.
5. **Spatial estimand and representation:** declare whether the task is an overall spatially
   variable gene, cell-type-specific spatially variable gene, domain marker, continuous gradient or
   subcellular localization problem. Record spot versus cell resolution, dependence on deconvolution,
   the spatial null and multiplicity control before selecting the method.
6. **Composition and mapping:** distinguish observed single-cell-resolution labels from spot
   deconvolution or scRNA-to-space mapping; report reference dependence and rare-cell uncertainty.
7. **Neighborhood and communication:** test enrichment against an appropriate spatial null;
   ligand-receptor or information-flow results remain hypotheses without functional evidence.
8. **Image-to-expression and super-resolution:** label H&E-predicted expression, virtual cells,
   interpolated slices and super-resolved maps as generated outputs and validate on measured data.
9. **Across-section and 3D inference:** audit alignment accuracy, missing tissue, section spacing and
   whether virtual slices are being mistaken for sampled anatomy.
10. **Time, perturbation and lineage:** distinguish measured time points from spatial velocity,
   experimentally indexed CRISPR/perturbation effects from computed counterfactuals, and barcode
   lineage from state similarity. Require the relevant kinetic assumptions, guide/barcode controls
   and held-out or orthogonal validation.
11. **Spatial clones and phylogeography:** label RNA-derived CNA and clone/phylogeny estimates as
   inferred and validate important structures with DNA or another orthogonal assay.

Core outputs are a platform/QC passport, segmentation-sensitivity result, explicit spatial estimand,
domain-and-gradient map, niche/neighborhood table, registration uncertainty statement,
three-axis evidence-layer map, and spatial claim boundary.

## Direction 5: cross-modal triangulation

The modalities answer different questions and provide complementary evidence; they do not form a
single ladder and one modality cannot upgrade the evidence state of another:

| Evidence layer | Main contribution | Typical overclaim to block |
|---|---|---|
| Bulk RNA | sample-level population signal and clinical association | assigning a pathway to a cell type without evidence |
| scRNA/snRNA | cellular source, state and within-tissue heterogeneity | treating cells as independent patient replicates |
| Spatial transcriptomics | location, neighborhood, gradient and tissue architecture | treating deconvolution or mapped cells as directly observed |
| Pathology or assay-native microscopy | tissue morphology and local architecture | treating an adjacent section or predicted expression map as direct co-localization |
| Radiology imaging, only when `study_scope == imaging-mechanism` | whole-lesion phenotype and clinical-scale heterogeneity | claiming micron-scale co-localization from coarse registration |
| Orthogonal/functional assay | corroboration or intervention | calling correlation a mechanism before perturbation |

For each conclusion, return: `claim | bulk support | single-cell support | spatial support |
pathology/orthogonal support | discordance | alternative explanation | validation needed`.
When `study_scope == imaging-mechanism`, append `radiology support | mapping scale and uncertainty`.

## Direction 6: virtual experiments and foundation models

Route each request into one of five distinct task classes:

- data generation or completion;
- state representation or reference mapping;
- perturbation-response prediction;
- spatial mapping or super-resolution;
- causal or counterfactual inference.

Require control/mean and simple statistical or linear baselines, held-out biological contexts,
calibration or error analysis where meaningful, and explicit out-of-distribution tests. For
perturbation prediction, report perturbation-specific effects, unseen perturbations, unseen cellular
contexts, gene-level biological signatures and model uncertainty. Common correlation or RMSE scores
can be inflated by systematic treated-versus-control variation; do not use one aggregate score to
declare a virtual knockout accurate. A larger pretrained model is not automatically a better
biological model. Predicted knockout responses, virtual cells and virtual spatial slices remain
hypotheses until tested against measured perturbations or held-out tissue.

## Direction 7: optional radiology linkage

Run this direction only when `study_scope == imaging-mechanism`; skip it completely for
`study_scope == mechanism-only`. The imaging-mechanism extension should ask whether molecular and
radiology signals refer to the same patient, lesion, region and time. Prefer a staged linkage:

1. establish the sample-level molecular program;
2. localize its cell source with single-cell evidence;
3. localize its tissue niche with spatial/pathology evidence;
4. relate that niche to a registered imaging habitat;
5. validate the imaging-molecular association in an independent matched cohort.

Weak mapping lowers the claim from local co-localization to patient-level association. Open
`sample-to-image-mapping.md` for the detailed mapping contract.

## Direction 8: three-axis evidence record and branch-specific claim requirements

The axes below are labels, not ranks. Never infer a one-way progression from `measured` to
`causal`, and never use one axis as a substitute for another.

### Axis 1 — primary evidence state

| State | Meaning |
|---|---|
| `measured` | direct assay observations under a stated platform and QC contract |
| `derived` | deterministic or rule-based transformation or summary of measured inputs |
| `estimated` | latent quantity inferred with a model, reference, mapping or deconvolution |
| `associated` | estimated relationship between variables at the valid inferential unit |
| `predicted` | output of a locked model for an unseen observation or declared target domain |
| `perturbed` | observed result under an experimentally assigned or implemented perturbation |

`missing` means that the evidence is absent. It belongs in a gap register, not in
`primary_evidence_state`.

### Axes 2 and 3

- `modality_subtype` records what operation produced the result, such as `gene-count`,
  `pseudobulk-DE`, `cell-state-label`, `deconvolution`, `spatial-domain`, `ligand-receptor-score`,
  `histology-predicted-expression`, or `perturbation-response`.
- `claim_link_status` is exactly `direct`, `inferred`, or `proposed` relative to the sentence being
  evaluated. A measured input may still have only an inferred link to a mechanism.

### Claim-requirement matrix

Select every branch invoked by the claim and judge each independently. A study may PASS prediction
while STOPping mechanism, or PASS localization while remaining non-causal.

| Claim branch | Defining requirements | Common STOP condition |
|---|---|---|
| Descriptive | traceable assay/sample provenance, valid QC, correct denominator and uncertainty | generated or inferred output presented as measurement |
| Association | prespecified contrast, valid biological unit, effect size/CI, multiplicity control, confounder/sensitivity plan and independent replication appropriate to the claim | pseudoreplication, unidentifiable design or selective reporting |
| Localization | direct spatial measurement or validated mapping, coordinate/region provenance, resolution and registration error compatible with the claimed scale, independent or orthogonal support | locality claimed below assay/mapping precision or from unmatched tissue |
| Prediction | locked target, features, preprocessing and model; patient/sample-level separation; named baseline; unseen evaluation; calibration and transport/OOD assessment | leakage, only internal apparent performance, or no calibration/comparator |
| Treatment effect or effect modification | treatment comparator, explicit treatment-by-biomarker interaction or identified causal contrast, time zero, allocation/confounding strategy, effect/CI and independent confirmation | one-arm response or prognostic association relabelled as treatment benefit |
| Mechanistic | explicit competing hypotheses, directional chain, temporal compatibility, target engagement, pathway/mediator and phenotype readouts, perturbation or strong orthogonal triangulation, and alternative-mechanism tests | enrichment, co-expression, proximity or prediction alone called mechanism |
| Causal | explicit intervention/exposure and causal estimand; randomized assignment or defended exchangeability/positivity/consistency assumptions; temporal order; negative-control/sensitivity analysis; intervention and rescue where the causal target is molecular | correlation alone, unresolved confounding, failed target engagement or post-treatment leakage |

The final answer must name the selected branch or branches, give `PASS / CONDITIONAL / STOP` for each,
and state the shortest missing requirement within each blocked or conditional branch. Do not report a
single “highest grade.”

## Direction 9: scientific writing and reporting contract

Writing is the final audit of the analysis, not a separate polishing step. Match the strength and
grammar of every sentence to its primary evidence state, claim-link status and selected claim branch.

### Title and abstract

- State the design and modality accurately; do not imply prospective validation, treatment
  prediction, single-cell resolution, spatial measurement or mechanism when these were not present.
- Put the independent biological sample count and validation setting near headline performance or
  biological claims when omission would change interpretation.
- Use `associated with`, `estimated`, `predicted` or `supported by` according to the recorded state
  and claim link. Reserve
  `drives`, `mediates`, `determines` and `confers sensitivity` for intervention-supported claims.

### Methods

Methods must allow reconstruction of the full evidence chain:

1. cohort flow and independent biological units, including exclusions and missing modalities;
2. tissue, lesion, section, time and treatment provenance;
3. platform, chemistry/panel, genome, annotation, software and parameter versions;
4. the exact matrix or layer used for each analysis and whether it was measured, normalized,
   corrected, imputed, mapped, deconvolved or simulated;
5. QC thresholds and whether they were fixed, data-adaptive or sample-specific;
6. estimand, model, covariates, random effects, pairing, offsets and unit of inference;
7. filtering universe, effect measure, confidence interval and multiplicity procedure;
8. train/validation separation, baseline comparators, tuning, calibration and missing-data handling;
9. sensitivity, negative-control and orthogonal-validation analyses;
10. data/code/accession availability and controlled-access boundaries.

Do not hide a scientifically consequential choice behind `default parameters` or cite software in
place of describing the analysis contract.

### Results

Use the sequence `sample accounting -> QC -> primary estimate -> uncertainty -> robustness ->
validation -> bounded interpretation`.

- Report patient/sample counts separately from cells, spots, sections, reads or assay-native image
  tiles.
- Lead with effect size and uncertainty; a P value or enrichment score alone is incomplete.
- State the comparison, reference category, direction, tested universe and adjusted versus nominal
  significance.
- Report negative, discordant and sensitivity results when they determine robustness or a branch
  verdict.
- Keep annotation, deconvolution, trajectory, communication, imputation and prediction verbs explicit;
  do not silently convert them into observation verbs.

### Figures, legends and tables

Every legend must define the biological `n`, technical observation count, unit represented by each
point, data layer, normalization/scale, summary statistic, error bar, statistical test, sidedness,
covariates where material and multiple-testing correction. Label inferred or generated maps in the
panel and legend. For spatial figures, give scale, coordinate/registration reference, segmentation or
spot definition and whether cells/genes were measured, mapped, deconvolved or predicted.

### Discussion and conclusion

- Separate replicated findings from exploratory hypotheses.
- Name the strongest plausible alternatives: composition, batch, sampling region, treatment timing,
  reference bias, segmentation, registration, technical sensitivity or model extrapolation.
- State the population, tissue, platform and context to which the result may generalize.
- Identify the missing requirement for each invoked claim branch; do not use a long limitation list
  to excuse an unsupported headline claim.

### Writing review output

When reviewing prose, return a table with:

`location | original claim | primary evidence state | modality subtype | claim-link status | claim branch | branch verdict | evidence gap | revised wording | new analysis needed`

Correct the scientific claim before polishing style. If numbers, tests or cohorts cannot be traced,
mark the claim `STOP (claim)—source required` rather than inventing a replacement.

## Direction 10: output contract

Return only the components needed for the user's mode, selected from:

1. `Task action`: expand, review, explain, judge, help, or a declared combination.
2. `Scientific question and estimand`.
3. `Data and sample passport`.
4. `Unit-of-inference and design audit`.
5. `Assay-aware QC findings`.
6. `Modality-specific analysis and baseline ladder`.
7. `Finding-to-evidence table` with all three evidence axes.
8. `PASS / CONDITIONAL / STOP decisions` with reasons and consequence.
9. `Cross-modal triangulation and discordance`.
10. `Claim-branch verdicts and alternative explanations`.
11. `Validation and next-experiment plan`.
12. `Writing or reviewer-repair artifact` when requested.
13. `Reproducibility artifacts` and `Author input needed`.

Do not return every component by default. Select the smallest set that completes the requested action,
but never omit a stop condition or claim-changing limitation.

## Evidence-derived rules already strong enough for the framework

Recent high-impact studies support several non-optional design rules:

- Feature selection changes integration, reference querying, label transfer and unseen-population
  detection ([PMID 40082610](https://pubmed.ncbi.nlm.nih.gov/40082610/)).
- Cohort-scale single-cell studies need sample-level models, not only cell averages
  ([PMID 41083897](https://pubmed.ncbi.nlm.nih.gov/41083897/)).
- Deep perturbation models must be compared with simple baselines and evaluated in unseen cellular
  contexts ([PMID 40759747](https://pubmed.ncbi.nlm.nih.gov/40759747/);
  [PMID 41381899](https://pubmed.ncbi.nlm.nih.gov/41381899/)).
- Larger single-cell pretraining corpora do not guarantee monotonic gains or clear scaling laws
  ([PMID 42265208](https://pubmed.ncbi.nlm.nih.gov/42265208/)).
- Spatial QC cannot be copied directly from dissociated single-cell workflows; local and regional
  artifacts require spatially aware checks ([PMID 40481362](https://pubmed.ncbi.nlm.nih.gov/40481362/)).
- Targeted spatial platforms require explicit panel, segmentation, specificity and transcript-
  contamination audits ([PMID 40082609](https://pubmed.ncbi.nlm.nih.gov/40082609/);
  [PMID 42062553](https://pubmed.ncbi.nlm.nih.gov/42062553/)).
- Histology-to-transcriptome models are useful bridges, but their expression outputs are predictions
  and require measured spatial validation ([PMID 40442373](https://pubmed.ncbi.nlm.nih.gov/40442373/)).
- Bulk deconvolution depends on transcriptome size, reference shift, batch, cell-type similarity and
  orthogonal benchmarking ([PMID 39893178](https://pubmed.ncbi.nlm.nih.gov/39893178/);
  [PMID 39191725](https://pubmed.ncbi.nlm.nih.gov/39191725/);
  [PMID 40889155](https://pubmed.ncbi.nlm.nih.gov/40889155/);
  [PMID 41772096](https://pubmed.ncbi.nlm.nih.gov/41772096/)).
- Raising a fold-change cutoff does not repair an underpowered bulk RNA-seq experiment
  ([PMID 41261110](https://pubmed.ncbi.nlm.nih.gov/41261110/)).
- Clinical transcriptomic subtypes or treatment biomarkers need multi-cohort consensus, independent
  validation and, for treatment prediction, an explicit biomarker-by-treatment interaction
  ([PMID 41028542](https://pubmed.ncbi.nlm.nih.gov/41028542/);
  [PMID 40865526](https://pubmed.ncbi.nlm.nih.gov/40865526/)).

## Evidence gate for the 100-paper corpus

The modality playbooks and evidence maps are valid only while the corpus passes all gates:

- formal publication date from **2024-08-21 through 2026-08-21**;
- priority to Nature Portfolio and Cell Press, with other field-leading journals allowed only when
  the **latest officially verifiable journal JIF at the screening date is at least 10**; historical
  thresholds are not used unless the user explicitly requests them;
- abstract/full-text content changes a scientific decision, interpretation boundary, benchmark,
  validation requirement or reporting artifact in this skill;
- original method, benchmark, resource, consensus, multi-cohort or clinically anchored study is
  preferred; reviews map the field but do not substitute for primary evidence;
- DOI/PMID and article type are verified; corrections, duplicates, preprints and descriptive papers
  without transferable guidance are excluded;
- each row records `concrete content | decision changed | constraint | skill action | writing
  requirement`, so papers are not included merely because they mention transcriptomics.

The corpus should contain exactly 100 unique eligible articles only if 100 pass these gates. A
shortfall must be reported as an evidence gap rather than repaired by lowering journal, date or
content standards.

## Progressive-disclosure routes

Open only the modality and evidence resources required for the current task:

- [bulk-rna-research-guidance.md](bulk-rna-research-guidance.md) for bulk design, execution,
  review, interpretation, judgement and writing;
- [single-cell-research-guidance.md](single-cell-research-guidance.md) for scRNA/snRNA;
- [spatial-transcriptomics-research-guidance.md](spatial-transcriptomics-research-guidance.md) for
  spatial transcriptomics;
- [transcriptomics-literature-evidence-map-2024-2026.md](transcriptomics-literature-evidence-map-2024-2026.md)
  only when row-level evidence provenance or corpus audit is needed;
- keep cross-modal triangulation, virtual experiments, claim grading and shared writing rules in
  this framework so they apply consistently across all three modalities.
