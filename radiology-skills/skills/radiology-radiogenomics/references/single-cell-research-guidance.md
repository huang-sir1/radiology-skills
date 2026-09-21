# Single-cell research guidance: evidence-to-decision playbook

Use this reference for research planning, analysis audit, interpretation, repair and manuscript
writing for scRNA-seq and snRNA-seq studies. It is deliberately a decision playbook rather than a
software tutorial. Its evidence map is the accompanying
`single-cell-literature-map-2024-2026.tsv`: 34 formally published articles with online publication
dates from 2024-08-21 through 2026-08-21 in journals whose screening-time 2025 JIF was at least 10.

The evidence window is narrow by design. It supports decisions where a recent paper materially
changed the workflow, but it does not turn journal metrics into article-level evidence or imply that
unrepresented older methods are invalid. Two deliberate evidence gaps must remain visible:

- this corpus has no general recent high-impact benchmark that establishes one best ambient-RNA,
  empty-droplet or transcriptome-only doublet method for standard droplet scRNA-seq; SC01 concerns
  retained Fluidigm cell photographs and cannot be generalized to 10x data;
- it has no recent qualifying benchmark that establishes one universally best replicate-aware
  differential-abundance method. The estimand, sampling design and sensitivity analyses must drive
  that choice.

## Non-negotiable inferential language

Keep three independent axes distinct throughout the analysis and manuscript. They are not a ladder.

| Axis | Allowed values | Single-cell interpretation |
|---|---|---|
| Primary evidence state | `measured`, `derived`, `estimated`, `associated`, `predicted`, `perturbed` | counts are measured; normalized/pseudobulk summaries are derived; labels, pseudotime, CNV and communication scores are estimated; sample-level effects are associated; locked held-out model outputs are predicted; observed assigned-intervention results are perturbed |
| Modality subtype | declared operation such as `molecule-count`, `pseudobulk-DE`, `cell-state-label`, `trajectory`, `RNA-CNV`, `GRN-edge`, `ligand-receptor-score`, `virtual-knockout`, `perturbation-response` | identifies the operation without changing its primary state |
| Claim-link status | `direct`, `inferred`, `proposed` | describes how directly the result supports the sentence being evaluated |

`missing` means that evidence does not exist and belongs in a gap register; it is never a primary
evidence state. A measured expression value may still have only an inferred link to cell function,
and a perturbed result is not universal causality across cell types, doses or patients.

### Branch-specific claim requirements

Select every branch invoked by the claim and judge each independently.

| Claim branch | Required support | Common STOP condition |
|---|---|---|
| Descriptive | traceable donor/sample/cell provenance, assay/QC contract, correct denominator and uncertainty | estimated label or imputed expression presented as measurement |
| Association | sample-aware contrast/model, effect/CI, multiplicity, donor consistency and appropriate replication | cells pooled as independent biological replicates |
| Localization | direct spatial/pathology evidence or validated mapping at the claimed scale; when `study_scope == imaging-mechanism`, also lesion/region/time registration to imaging | dissociated cell identity alone claimed to establish tissue or radiology location |
| Prediction | locked target, features and model; donor/patient-level split; named baseline; unseen-domain evaluation; calibration and OOD analysis | random-cell leakage or only in-domain apparent performance |
| Treatment effect or effect modification | treatment comparator, explicit treatment-by-biomarker interaction or identified causal contrast, time zero, allocation/confounding strategy, effect/CI and independent confirmation | one-arm response or prognostic signal relabelled as benefit |
| Mechanistic | competing hypotheses, directional chain, temporal compatibility, target engagement, pathway/mediator and phenotype readouts, perturbation or strong orthogonal triangulation, and alternative-mechanism tests | co-expression, GRN or ligand-receptor score alone called mechanism |
| Causal | explicit causal estimand; randomized perturbation or defended exchangeability/positivity/consistency; temporal order; negative controls/sensitivity; rescue where applicable | observational association, pseudotime or predicted perturbation alone |

A study may PASS prediction and STOP mechanism, or PASS association while localization remains
untested. Report the shortest missing requirement within each selected branch, never a single
“highest grade.”

Cells are repeated observations nested in biological samples. More cells increase measurement
precision; they do not increase the number of independent patients.

## Stage-gated workflow

Every gate ends in `PASS`, `CONDITIONAL` or `STOP`. A later attractive UMAP, network or prediction
cannot rescue a failed upstream gate.

| Gate | Question and required evidence | PASS | CONDITIONAL | STOP | Required output |
|---|---|---|---|---|---|
| G0 question | What population, contrast, time point, cell state and decision does the study target? | estimand and biological unit are explicit | exploratory question is bounded | no definable contrast or endpoint | question/estimand card |
| G1 provenance | Can every cell be linked to donor, sample, tissue/biopsy region, assay, processing batch and condition? | complete stable identifiers and data layers | non-critical metadata gap is declared | donor/sample identity or claimed tissue-region linkage is irrecoverable | sample-cell passport |
| G2 assay/QC | Are empty droplets, ambient RNA, low-quality libraries, doublets and sample outliers assessed without outcome-tuned thresholds? | per-sample diagnostics and exclusion ledger pass | residual risk is quantified and sensitivity-tested | group-specific catastrophic QC or unresolved mixed-cell signal drives the claim | QC ledger |
| G3 representation | Is normalization, feature selection, integration or mapping fitted for the stated task? | task-specific layers and held-out checks | result depends on a defensible representation | biology is completely confounded with batch or corrected values are treated as observations | data-layer passport |
| G4 identity | Are class, subtype, state, disease relevance and malignancy distinguished with uncertainty? | convergent evidence and an `unknown` option | label is provisional and downstream results are stable | circular labels, propagated patient labels or RNA-CNV alone define truth | cell-state dictionary |
| G5 sample inference | Is abundance/expression tested at the independent sample level? | replicated sample-aware model, effect and uncertainty | low power but estimand remains identifiable | pooled-cell test substitutes for biological replication | composition/DE tables |
| G6 dynamics | Does trajectory, velocity or lineage evidence match the claimed temporal statement? | compatible measurement plus sensitivity/orthogonal support | ordering is hypothesis-generating | snapshot pseudotime is called observed time or lineage | dynamic evidence card |
| G7 mechanism | Do GRN/CCC results distinguish expression compatibility, regulation and causality? | validated directional perturbation or orthogonal evidence | mechanistic hypothesis is bounded | ligand-receptor or correlation score is claimed as causal signaling | hypothesis-validation matrix |
| G8 perturbation | Are guide assignment, efficiency, dose, controls and heterogeneous responses modeled? | observed effects are estimable and reproducible | partial/variable perturbation is modeled | guide confounding, failed controls or no usable biological replication | perturbation effect table |
| G9 prediction/FM | Is evaluation genuinely out of domain and compared with simple baselines? | locked model wins on the prespecified held-out task with uncertainty | setting-specific benefit only | random-cell leakage or systematic variation explains performance | generalization report |
| G10 release | Do Methods, Results, legends and Discussion report the same three evidence axes and branch verdicts? | counts, versions, effects, uncertainty and limitations align | wording repair suffices | untraceable values, hidden exclusions or causal language contradict evidence | release checklist |

When `STOP` fires, retain any valid descriptive output, lower the claim, state what is not
identifiable, and request the shortest repair. Do not continue mechanically to downstream analyses.

## Input contract

Before interpretation, require or reconstruct the following. Mark each item `provided`, `derived`,
`missing-but-noncritical` or `blocking`.

| Contract group | Required fields | Blocking examples |
|---|---|---|
| Research target | target population, exposure/intervention, comparator, endpoint, time, cell class/state, estimand, intended claim | “find differences” with no comparison or biological unit |
| Biological hierarchy | patient/donor ID, sample ID, lesion/biopsy/region, visit, paired/repeated status, condition, clinical endpoint | cells cannot be assigned to independent samples |
| Assay | scRNA versus snRNA, chemistry/version, UMI status, feature reference, genome/annotation version, sequencing depth, multiplexing | assay or feature definition is unknown |
| Processing | site, collection-to-processing interval, tissue handling, dissociation/nuclei method, lane, library batch, operator | condition is perfectly aligned with batch |
| Data objects | raw molecule/count matrix, cell/sample metadata, QC metrics, ambient-adjusted counts if used, normalized data, selected features, scaled data, integrated embedding, imputed/predicted data | only a corrected embedding is available for a requested DE claim |
| Perturbation | guide/perturbation identity, multiplicity, target sequence, controls, efficiency, dose, duration, replicate, cell line/donor | perturbation identity or controls cannot be recovered |
| Validation | held-out donors/datasets, orthogonal DNA/protein/spatial/lineage assay, negative controls, preregistered primary endpoint | confirmatory claim with no independent evidence |
| Imaging linkage, only when `study_scope == imaging-mechanism` | patient, lesion, tissue region, acquisition/biopsy times, co-registration or sampling relationship | cell data are assigned to a different lesion or unverifiable region |

### Data-layer access matrix

| Object | Allowed primary uses | Do not use as |
|---|---|---|
| raw counts | ambient/doublet diagnostics, pseudobulk aggregation, count-aware models | directly comparable values across unequal libraries without a model |
| ambient-adjusted counts | sensitivity analysis and supported downstream tasks | proof that contamination was eliminated |
| normalized expression | visualization, marker exploration, some task-specific scoring | independent patient-level replication |
| selected features | representation/integration fitted within the analysis scope | a universal gene universe or outcome-leaking screen |
| scaled values | PCA/visualization where appropriate | molecule counts or DE effect sizes |
| integrated latent space | visualization, neighborhood construction, mapping when validated | measured expression or default DE input |
| imputed/generated expression | denoising or prediction analysis with measured-data validation | observed expression, biological replicate or independent corroboration |

## Evidence-derived execution cards

Each card tells the skill what to expand, review, explain, judge and repair. The cited IDs resolve to
the literature map.

### 1. Research question, estimand and cohort-scale target

- **Expand:** name the biological sample, cell population, contrast, target population and output:
  sample-level state distribution, cell-type-specific mean/variability, rare disease-relevant cell
  probability, or patient stratification. Only when `study_scope == imaging-mechanism`, add mapped
  lesion/region and imaging time.
- **Review:** reconstruct donor and sample counts by group; pairing, repeated visits, recruitment
  site and treatment; whether patient labels were copied to cells; whether latent patient groups
  were defined and tested in the same cohort.
- **Interpret:** SC09 supports sample-level latent heterogeneity without prespecified states; SC18
  and SC19 show that a patient label can localize to only a subset of cells. These are estimated
  subpopulations or sample strata, not diagnoses or cell-level ground truth.
- **Judge:** `PASS` when the estimand and independent unit match and validation is separated;
  `CONDITIONAL` for discovery-only latent strata with stability checks; `STOP` if cells replace
  patients as n, or the outcome defines both the cell label and its validation.
- **Repair/help:** make a donor-by-condition table; refit discovery on training donors; test cluster,
  abundance and outcome stability in held-out donors; downgrade to descriptive atlas if sample n
  cannot support inference.
- **Hard constraints:** no population or clinical claim from one donor per group; no patient label
  propagated as a cell truth. When `study_scope == imaging-mechanism`, no lesion-specific imaging
  claim without lesion linkage.
- **Writing:** Methods—state estimand, hierarchy, splits and covariates. Results—give donor counts,
  effect/uncertainty and donor consistency. Legend—show independent n and what each point means.
  Discussion—limit transfer to sampled populations/sites and call latent groups exploratory until
  externally reproduced.
- **Evidence:** SC09, SC18, SC19.

### 2. Data layers, preprocessing and feature selection

- **Expand:** identify whether the target is gene abundance, lncRNA detection, transcriptional
  kinetics, integration, reference query or DE; create a separate object and fit scope for every
  transformation.
- **Review:** assay/kit, alignment or quantification route, annotation build, raw-count retention,
  filtering, normalization, number/source of features, batch-aware feature selection and whether
  any step saw validation labels.
- **Interpret:** SC02 shows platform and read-utilization trade-offs; SC03R shows that aligner,
  reference and filtering materially change low-expression lncRNA recovery; SC04R models
  nascent/mature count dynamics; SC05 shows that feature choice and feature count alter integration,
  query mapping and unseen-population detection.
- **Judge:** `PASS` when the data layer is matched to the estimand and preprocessing is fitted within
  the correct samples; `CONDITIONAL` when conclusions survive plausible feature/annotation choices;
  `STOP` for DE on an embedding/corrected latent variable, missing raw counts for a count claim, or
  feature selection informed by held-out outcomes.
- **Repair/help:** regenerate a layer passport; repeat key results across defensible feature counts,
  annotation versions or quantifiers; rerun DE from counts with donor-aware design; preserve the
  integrated object only for its validated purpose.
- **Hard constraints:** no universal “best kit” from the single-donor SC02 comparison; no universal
  preprocessing winner from lncRNA-specific SC03R; no kinetic interpretation without compatible
  nascent/mature information and model checks.
- **Writing:** Methods—name chemistry, genome/annotation, quantifier, filtering, normalization,
  feature rule and fit scope. Results—report sensitivity, not only the chosen pipeline. Legend—name
  the plotted layer. Discussion—state platform, annotation and feature-selection dependence.
- **Evidence:** SC02, SC03R, SC04R, SC05.

### 3. QC, ambient RNA and doublets

- **Expand:** define which failures threaten the estimand: empty droplets, ambient transcripts,
  low complexity, high mitochondrial/ribosomal signal, sample-specific outliers, homotypic or
  heterotypic doublets and dissociation/nucleus artifacts.
- **Review:** per-sample distributions before/after filtering; threshold provenance; expected versus
  removed doublet rates; marker co-expression; ambient-sensitive markers; losses by donor/group;
  whether thresholds were tuned to improve the desired result.
- **Interpret:** a doublet score or ambient-adjusted value is a model output. SC01 demonstrates that
  retained Fluidigm cell photographs can directly improve doublet identification, but it does not validate a
  transcriptome-only method or generalize to standard droplet datasets. SC02 supports
  platform-specific QC and read-utilization reporting.
- **Judge:** `PASS` when QC is per-sample, exclusions are traceable and identities/results are stable;
  `CONDITIONAL` when contamination risk remains but sensitivity analysis bounds it; `STOP` when
  disease markers are indistinguishable from ambient RNA, hybrid clusters drive the claim, or one
  group loses cells/samples catastrophically.
- **Repair/help:** inspect raw droplets and negative/low-RNA profiles when available; compare results
  before/after ambient adjustment and doublet removal; remove suspect identities from primary
  inference; obtain orthogonal microscopy or protein evidence for a key mixed phenotype.
- **Hard constraints:** do not invent one best general method from this corpus; SC01 requires retained
  cell photographs; thresholds must not be chosen by the downstream p value; removal of cells does not create
  new biological replicates.
- **Writing:** Methods—report metrics, per-sample thresholds, tools/versions and cells/samples removed.
  Results—show attrition by group and sensitivity. Legend—state filtered versus unfiltered counts
  and denominators. Discussion—name residual ambient/doublet and dissociation risk.
- **Evidence:** SC01, SC02. **Corpus gap:** general droplet ambient/doublet benchmarking.

### 4. Integration, reference mapping and unseen populations

- **Expand:** select one purpose—visualization, label transfer, query mapping, atlas construction or
  multi-omic integration—and a preservation target; do not use “remove batch” as the estimand.
- **Review:** feature-selection scope, reference/query compatibility, batch and biology balance,
  mapping uncertainty, unknown/rejection behavior, leave-one-donor/batch/dataset-out tests, and
  whether integration erased condition-specific or rare-cell signals.
- **Interpret:** SC05 makes feature selection part of the model; SC06 shows that integration can erase
  biological signal and that recovery depends on a pool-of-controls design; SC07R supports reusable
  pretrained probabilistic models with reference-bias checks; SC08R shows integration performance is
  task and multi-omic configuration dependent.
- **Judge:** `PASS` when batch mixing and biological preservation both pass held-out tests;
  `CONDITIONAL` when mapping is useful only within reference support; `STOP` if biology is perfectly
  confounded with batch, unknown cells are forcibly absorbed, or an integrated value is presented as
  measured expression.
- **Repair/help:** return to unintegrated counts for inference; compare feature sets/methods; add
  reference-free marker review and an unknown class; use leave-dataset-out mapping; redesign or add
  controls when biology/batch are non-identifiable.
- **Hard constraints:** integration cannot identify a fully confounded effect; reference coverage and
  preprocessing compatibility are required; query labels must carry uncertainty.
- **Writing:** Methods—state purpose, reference, features, fit data, hyperparameters and held-out test.
  Results—report preservation and mapping uncertainty alongside mixing. Legend—distinguish raw and
  integrated spaces. Discussion—bound claims to reference/domain coverage.
- **Evidence:** SC05, SC06, SC07R, SC08R.

### 5. Annotation, weak labels, malignancy and RNA-derived CNV

- **Expand:** separate cell class, subtype, activation/program state, disease relevance and malignant
  identity; specify which can remain unknown and what orthogonal truth is available.
- **Review:** marker direction and specificity, reference/ontology version, consensus and confidence,
  batch/donor distribution, doublet risk, manual overrides, LLM prompt/model version, negative
  references and DNA/protein/pathology validation.
- **Interpret:** popV (SC10) supports consensus ontology-aware labels with uncertainty; CASSIA
  (SC11R) can expose reasoning and quality checks but its text is not evidence; TCAT/starCAT (SC12)
  favors continuous T-cell programs over forced subtypes; HiDDEN and MMIL (SC18, SC19) treat patient
  labels as weak cell labels; the caller benchmark (SC14) makes RNA-CNV a reference- and data-size-
  dependent estimate. mcRigor (SC13R) tests metacell homogeneity, not cell truth.
- **Judge:** `PASS` for convergent marker/reference evidence with confidence and unknowns;
  `CONDITIONAL` for provisional rare/malignant states stable to methods; `STOP` when LLM output,
  patient diagnosis, RNA-CNV or one marker alone defines ground truth.
- **Repair/help:** build a cell-state evidence matrix; relabel low-confidence cells unknown; run
  reference/marker/consensus sensitivity; validate malignancy with matched DNA or pathology where
  possible; test metacell homogeneity before aggregation.
- **Hard constraints:** RNA-CNV is not DNA CNV; a disease-bearing sample contains non-disease cells;
  ontology mismatch and novel states must be allowed; reasoning narratives cannot replace citations
  and marker evidence.
- **Writing:** Methods—report references, ontology, marker rules, confidence, overrides and CNV inputs.
  Results—give unresolved fractions and concordance. Legend—show label source/confidence and whether
  CNV is RNA-derived. Discussion—use “putative/probable” for unvalidated malignant or disease-relevant
  cells.
- **Evidence:** SC10, SC11R, SC12, SC13R, SC14, SC18, SC19.

### 6. Sample-aware differential abundance and expression

- **Expand:** define abundance as a marginal proportion, conditional proportion or compositional
  contrast; define expression target as mean, variability, correlation or program within a cell
  population; predefine primary cell states and multiplicity family.
- **Review:** independent donor counts, paired/repeated design, cell yield and precision by sample,
  compositional denominator, covariates, random effects, pseudobulk aggregation, rare-state support,
  donor influence, zero handling and multiple testing.
- **Interpret:** Memento (SC15) estimates mean, variability and gene correlation; TRADE (SC16R)
  separates perturbation-atlas effect distributions from estimation error; FLASH-MM (SC17) models
  sample correlation and individual variation; MrVI (SC09) captures sample-level heterogeneity.
  Method significance does not turn cells into independent n.
- **Judge:** `PASS` for a replicated sample-aware model with effect, interval/FDR and donor
  consistency; `CONDITIONAL` when a rare state is estimable but underpowered; `STOP` for pooled-cell
  tests, one sample per condition, or abundance claims based only on unequal recovered cell counts.
- **Repair/help:** aggregate counts per donor/state for pseudobulk; fit a justified mixed model when
  within-sample structure is essential; perform leave-one-donor-out and alternative-denominator
  sensitivity; collapse or descriptively report unsupported rare states.
- **Hard constraints:** biological n is samples; pseudobulk requires raw counts and adequate sample
  replication; no universal DA method is endorsed by this corpus; TRADE's atlas estimand is not a
  default clinical-cohort DE test.
- **Writing:** Methods—state aggregation/unit, design formula, offsets/covariates, contrasts and FDR.
  Results—give effect sizes, intervals and donor consistency. Legend—each point/box must reveal its
  biological n. Discussion—separate composition, state-frequency and within-state expression.
- **Evidence:** SC09, SC15, SC16R, SC17. **Corpus gap:** universal replicate-aware DA benchmark.

### 7. Trajectory, kinetics, velocity and lineage

- **Expand:** choose among observed longitudinal change, snapshot pseudotime, RNA kinetics/velocity,
  paired multi-omic ordering and barcode lineage; define root, endpoint, branch and transient-event
  estimand.
- **Review:** sampling times, root/graph assumptions, cell-cycle/stress confounding, genes/features,
  kinetics model, spliced/unspliced or nascent/mature information, paired ATAC availability, lineage
  barcode/tree quality, donor replication and sensitivity to preprocessing/subsampling.
- **Interpret:** Monod (SC04R) fits stochastic transcriptional dynamics; scTransient (SC20R) detects
  wave-like events along an upstream supervised pseudotime; scLANE (SC21) provides interpretable
  trajectory tests including multi-subject models; ArchVelo (SC22) needs paired ATAC/RNA; Carta
  (SC23R) uses lineage trees and can admit convergent differentiation/unobserved progenitors.
- **Judge:** `PASS` for measurement-compatible dynamics stable to roots/methods and supported by
  time/lineage evidence; `CONDITIONAL` for a reproducible snapshot ordering; `STOP` when pseudotime is
  called chronological time, velocity arrows prove fate, or lineage is inferred without lineage data.
- **Repair/help:** vary roots, neighborhoods and features; analyze donors separately and jointly;
  validate ordered markers at measured time points; collect paired multiome or lineage tracing for a
  directional claim; downgrade to state continuum when direction is unsupported.
- **Hard constraints:** upstream ordering errors propagate into transient/trajectory tests; ArchVelo
  is not scRNA-only; Carta requires lineage trees; TFs inferred from accessibility/velocity remain
  hypotheses.
- **Writing:** Methods—state dynamic evidence class, root, model, features, donor handling and
  sensitivities. Results—report branch/stability and uncertainty. Legend—label pseudotime units as
  dimensionless/inferred. Discussion—separate ordering, kinetics, fate and lineage.
- **Evidence:** SC04R, SC20R, SC21, SC22, SC23R.

### 8. Gene-regulatory networks and cell-cell communication

- **Expand:** define whether the claim concerns co-expression, regulator-target influence,
  perturbation-supported regulation, ligand-receptor compatibility, pathway crosstalk or physical
  signaling between spatially adjacent cells.
- **Review:** network priors and versions, expression thresholds, cell counts and donors, target
  direction, edge uncertainty, permutation/reference null, spatial compatibility, perturbation
  evidence and replication across samples/datasets.
- **Interpret:** SigXTalk (SC24) links receptors, TFs and targets through hypergraphs; FastCCC (SC25)
  replaces permutations with analytical/reference-based scoring; D-SPIN (SC26) builds interpretable
  regulatory models across perturbations; PSGRN (SC27) uses perturbational/observational data and
  synthetic gold standards. All remain model-dependent.
- **Judge:** `PASS` for a directional edge supported by independent perturbation and compatible
  downstream response; `CONDITIONAL` for replicated network/CCC hypotheses; `STOP` if expression
  compatibility is called physical contact or causality, or cell-level p values replace donor-level
  replication.
- **Repair/help:** require edge agreement across donors/methods; report effect and uncertainty rather
  than p value alone; test ligand/receptor/target perturbations; add protein/spatial evidence; prune
  unstable or prior-only edges.
- **Hard constraints:** analytical p values are not biological effects; reference panels and curated
  networks carry bias; synthetic gold standards are incomplete truth; no causal CCC without an
  intervention that changes the receiver response.
- **Writing:** Methods—version databases, null, aggregation, donor handling and validation. Results—
  separate candidate edges from validated mechanisms. Legend—encode direction, effect, support and
  sample n. Discussion—name prior/reference and causal limitations.
- **Evidence:** SC24, SC25, SC26, SC27.

### 9. Observed Perturb-seq effects

- **Expand:** define target, perturbation modality, dose/duration, efficiency, direct versus downstream
  response, population-average versus heterogeneous effect, and whether the estimand is a gene,
  program, pathway or state-composition change.
- **Review:** guide assignment/multiplicity, non-targeting and positive controls, perturbation
  efficiency, cell line/donor/replicate, guide-level concordance, cell-cycle/stress, batch, dose and
  partial responders.
- **Interpret:** TRADE (SC16R) estimates transcriptome-wide perturbation impact; D-SPIN and PSGRN
  (SC26, SC27) derive regulatory hypotheses; the perturbation-response score (SC28) exposes buffered
  versus sensitive cells; GPerturb (SC29) models discrete/continuous effects with uncertainty;
  SC31R reconstructs pathway signatures across more than 1,500 perturbations while addressing
  efficiency.
- **Judge:** `PASS` when controls, efficiency, replicate consistency and effect uncertainty support the
  observed response; `CONDITIONAL` for partial/heterogeneous effects explicitly modeled; `STOP` when
  guide identity/controls fail, target knockdown is absent, or pooled cells substitute for
  experimental replication.
- **Repair/help:** model efficiency/dose; compare guides per target; separate responders/nonresponders;
  analyze control variation; validate top genes/programs in an independent perturbation or protein/
  functional assay.
- **Hard constraints:** CRISPRi/knockdown is not a complete knockout; observed transcript response is
  not a phenotypic mechanism; cell-line pathway conservation does not establish patient transfer.
- **Writing:** Methods—report guide design, assignment, controls, multiplicity, efficiency, dose,
  duration and replicate model. Results—give target engagement, effect/uncertainty and heterogeneity.
  Legend—show controls and biological replicate n. Discussion—bound mechanism to tested system.
- **Evidence:** SC16R, SC26, SC27, SC28, SC29, SC31R.

### 10. Perturbation-response prediction and virtual knockout

- **Expand:** label the target domain: unseen cells, unseen donor/dataset, unseen dose/condition,
  unseen perturbation, or combinations. Distinguish data completion, state mapping, response
  prediction and causal counterfactual; “virtual knockout” alone is not an estimand.
- **Review:** split level, control construction, systematic variation, perturbation-selection bias,
  simple baselines, mean versus gene-level metrics, calibration, uncertainty, target engagement,
  external/OOD data and prospective validation.
- **Interpret:** the 27-method/29-dataset benchmark (SC30) shows scenario-dependent generalization;
  Systema (SC32) shows that perturbed-control systematic variation can inflate metrics; scDrugMap
  (SC33R) finds different foundation-model winners across pooled, cross-dataset, fine-tuned and
  zero-shot drug-response settings.
- **Judge:** `PASS` only when a locked model exceeds simple baselines on the prespecified held-out
  domain and predicts perturbation-specific signal with uncertainty; `CONDITIONAL` for narrow
  interpolation; `STOP` for random-cell splits, evaluation on training perturbations, or performance
  explained by controls/systematic variation.
- **Repair/help:** rebuild donor/perturbation/dataset-level splits; add control mean, linear and nearest-
  neighbor baselines; report gene-, pathway- and distribution-level metrics; apply Systema-style
  variation control; prospectively test prioritized predictions.
- **Hard constraints:** predictions are hypotheses, not experimental facts; no “causal
  counterfactual” from observational training alone; imputed cells are not replicates; zero-shot
  claims require truly unseen perturbations and contexts.
- **Writing:** Methods—define target domain, splits, baselines, metrics and calibration. Results—report
  absolute and baseline-relative performance by scenario. Legend—mark measured versus predicted
  values. Discussion—state OOD failures and required experiments.
- **Evidence:** SC30, SC32, SC33R.

### 11. Foundation models and reusable pretrained models

- **Expand:** specify the downstream decision—embedding, annotation, imputation, deconvolution or
  perturbation prediction—and the exact transfer setting; model size is not the scientific target.
- **Review:** pretraining corpus overlap, donor/species/tissue/platform coverage, objective, model and
  checkpoint version, preprocessing/tokenization compatibility, frozen versus fine-tuned status,
  compute budget, simple specialist baselines and calibration.
- **Interpret:** scvi-hub (SC07R) enables model-driven reuse but makes reference provenance part of the
  analysis; SC30 and SC33R show that foundation models do not dominate every perturbation setting;
  SC34's 400-model/6,400-experiment study found early performance plateaus and no clear universal
  scaling law over the tested designs.
- **Judge:** `PASS` for a versioned model that adds task-relevant held-out value without data overlap;
  `CONDITIONAL` for in-domain representation reuse; `STOP` when corpus leakage is unresolved,
  preprocessing is incompatible, or “foundation”/parameter count substitutes for evaluation.
- **Repair/help:** audit pretraining overlap; compare frozen/fine-tuned and simple baselines; stratify
  by tissue/platform/rare state; measure calibration and abstention; choose the smallest model that
  meets the scientific requirement.
- **Hard constraints:** larger is not automatically better; pretrained imputation is not measurement;
  resource/model availability does not establish clinical or biological validity.
- **Writing:** Methods—name checkpoint, corpus, overlap audit, preprocessing, tuning and compute.
  Results—report baseline-relative performance and strata. Legend—mark model outputs and uncertainty.
  Discussion—limit transfer to evaluated domains and architectures.
- **Evidence:** SC07R, SC30, SC33R, SC34.

### 12. Cohort-scale discovery, rare states and patient-level validation

- **Expand:** determine whether the goal is atlas description, sample stratification, rare disease-
  relevant cell discovery or prognostic association; prespecify discovery and validation cohorts.
  Only when `study_scope == imaging-mechanism`, add imaging-phenotype association as a target.
- **Review:** recruitment/site/batch balance, donor/sample weights, repeated visits, cell yield,
  missingness, rare-state prevalence, site/donor influence, clinical covariates and train/test
  isolation. Only when `study_scope == imaging-mechanism`, also audit sample-to-image provenance.
- **Interpret:** MrVI (SC09) models sample-level heterogeneity; FLASH-MM (SC17) scales sample-aware
  expression tests; HiDDEN/MMIL (SC18, SC19) identify probabilistic disease-relevant subsets from
  weak case-control labels. None converts a large cell count into a large patient cohort.
- **Judge:** `PASS` for patient-level effects replicated across donors/sites and a held-out cohort;
  `CONDITIONAL` for stable discovery with explicit validation deficit; `STOP` for single-site/batch
  confounding, patient leakage or rare states represented by too few independent samples.
- **Repair/help:** leave one donor/site out; downsample cells per donor; test alternate state
  resolutions; confirm rare states in raw markers and an orthogonal assay; freeze the signature
  before external validation; downgrade clinical claims when validation is unavailable.
- **Hard constraints:** patient/donor is the clinical unit; latent strata need external meaning and
  replication; prognosis does not imply treatment prediction. When
  `study_scope == imaging-mechanism`, radiogenomic association requires matched lesion/time
  provenance.
- **Writing:** Methods—report cohort flow, hierarchy, sites, split and model. Results—give sample-level
  effects, intervals and validation performance. Legend—show donors, not only cells. Discussion—state
  recruitment, tissue and platform limits; when `study_scope == imaging-mechanism`, also state
  imaging-sampling limits.
- **Evidence:** SC09, SC17, SC18, SC19.

## Standard outputs

Return the smallest auditable package that answers the user's request. Use these artifacts and keep
their identifiers consistent across text, tables and figures.

1. **Question/estimand card:** population, exposure/intervention, comparator, outcome, time, cell
   population, biological unit, estimand, intended claim.
2. **Sample-cell passport:** donor/sample/tissue or biopsy region/visit/condition/batch plus raw and
   retained cell counts; list exclusions and reasons. Only when
   `study_scope == imaging-mechanism`, append mapped lesion, imaging acquisition and linkage fields.
3. **Data-layer ledger:** object name, assay layer, transformation, fit samples, features, permitted
   downstream uses, prohibited uses.
4. **QC ledger:** per-sample metrics, thresholds, ambient/doublet evidence, attrition, group balance,
   unresolved risk and sensitivity result.
5. **Cell-state dictionary:** class/subtype/state, positive and negative evidence, reference,
   confidence, unknown fraction, doublet/CNV/weak-label warnings.
6. **Sample-by-state composition table:** counts, proportions/denominators, model, contrast, effect,
   interval, multiplicity and donor sensitivity.
7. **Expression/program table:** raw-count source, aggregation/model, effect, interval, FDR, donor
   consistency and annotation version.
8. **Dynamic evidence card:** measurement class, root/time/lineage inputs, branch, uncertainty,
   sensitivities and allowed claim.
9. **Mechanism matrix:** proposed regulator/sender/receiver/target, three-axis evidence record,
   donor support, perturbation/orthogonal validation, competing hypotheses and branch verdict.
10. **Perturbation/generalization report:** observed versus predicted, target engagement, split domain,
    baselines, metrics, calibration, OOD result and prospective validation need.
11. **Claim ledger:** each headline statement mapped to primary evidence state, modality subtype,
    claim-link status, selected claim branch, alternatives, branch verdict and exact
    Methods/Results/figure locations.

## Manuscript writing contract

### Methods must permit reconstruction

Report cohort hierarchy and independent n; tissue/region/time linkage; assay and genome/annotation;
raw and transformed layers; QC and attrition; feature selection; integration/reference and fit scope;
annotation evidence/uncertainty; sample-aware design formula, covariates, contrasts and multiplicity;
trajectory/GRN/CCC assumptions; perturbation controls/efficiency; prediction split, baselines and
metrics; software/model/checkpoint versions and code/data availability.

Only when `study_scope == imaging-mechanism`, add lesion-to-imaging linkage, acquisition timing and
registration uncertainty.

### Results must report evidence, not workflow completion

For every headline result give biological n, effect size, interval or uncertainty, multiplicity
status, donor/sample consistency, key sensitivity and validation status. Report unknown/unresolved
cells and negative results. “A method identified” is not a biological result.

### Figure legends must prevent denominator ambiguity

State whether points are cells, samples or patients; exact n by group; assay/data layer; filtering;
summary statistic and error representation; statistical test/model and correction; meaning of color,
edge, arrow, pseudotime and prediction; whether labels/CNV/communication/values are measured,
inferred or predicted.

### Discussion must calibrate transfer and mechanism

Separate association from causality, snapshot order from time/lineage, RNA-CNV from DNA truth,
ligand-receptor compatibility from signaling, observed perturbation from predicted response, and
in-domain performance from OOD generalization. Name the shortest unmet requirement for each claim
branch actually invoked; do not describe claim branches as levels.

## Reviewer checklist

Mark each item `PASS`, `CONDITIONAL`, `STOP` or `NOT APPLICABLE` and cite an evidence location.

- Is the estimand explicit, and is patient/sample—not cell—the independent unit?
- Can every analyzed cell be traced to donor, sample, condition, batch and lesion/region where claimed?
- Are raw counts, normalized data, selected features, integrated embeddings and predictions distinct?
- Are QC thresholds per sample, outcome-independent and accompanied by attrition/sensitivity?
- Are ambient RNA and doublet risks addressed without overgeneralizing SC01?
- Is integration evaluated for biological preservation, not only batch mixing?
- Are mapping/annotation confidence, unknowns, ontology/reference versions and manual overrides shown?
- Are disease relevance, activation state and malignancy separated; is RNA-CNV orthogonally bounded?
- Are abundance and DE replicate-aware, with biological n, effect, uncertainty and multiplicity?
- Are rare-state results supported by enough independent samples and donor-level sensitivity?
- Are pseudotime, velocity and lineage described with the correct primary state, modality subtype
  and claim-link status?
- Are GRN/CCC edges hypotheses unless perturbation or orthogonal evidence supports direction?
- Do Perturb-seq results report guide controls, target engagement, efficiency, dose and heterogeneity?
- Do prediction/FM analyses prevent donor/perturbation/dataset leakage and beat simple baselines?
- Are systematic variation, gene-level metrics, calibration and OOD failures reported?
- Do all legends reveal denominators, data layer, uncertainty and all three evidence axes?
- Are Methods, Results, legends and Discussion consistent about all three evidence axes and every
  selected claim-branch verdict?

## Wording boundary and repair examples

| Avoid | Use instead | What would justify stronger wording |
|---|---|---|
| “integration removed batch effects” | “the selected representation improved prespecified batch-mixing metrics while preserving the tested biological signals” | held-out preservation tests and non-confounded design |
| “cells were definitively annotated” | “cells were assigned labels with marker/reference agreement and reported confidence; unresolved cells remained unknown” | orthogonal and reproducible identity evidence |
| “CNV confirmed malignant cells” | “RNA-expression-derived CNV supported a putative malignant assignment” | matched DNA/pathology validation |
| “cell type X increased” from pooled cells | “the sample-level proportion of state X was associated with condition Y” | replicated sample-aware compositional inference |
| “pseudotime showed progression” | “cells formed an inferred expression-state ordering consistent with the proposed progression” | measured time or lineage validation |
| “ligand-receptor analysis proved signaling” | “expression compatibility nominated a sender-receiver hypothesis” | spatial/protein evidence plus functional intervention |
| “CRISPR knockout caused program Z” after partial CRISPRi | “target perturbation was associated with program Z at the observed efficiency and dose” | verified target loss, controls and replicated functional rescue |
| “the virtual knockout predicts biology” | “the model predicted a response in the stated held-out domain” | prospective perturbation validation and causal design |
| “the foundation model generalized” | “the locked model exceeded named baselines in the prespecified unseen dataset/cell/perturbation setting” | independent multi-domain replication with calibration |

If an analysis cannot meet a stronger boundary, repair the sentence and the claim ledger immediately;
do not wait until Discussion to reveal the limitation.
