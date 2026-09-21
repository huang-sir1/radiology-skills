# Bulk RNA research guidance

Use this reference when bulk RNA-seq, targeted RNA-seq, long-read RNA-seq, a bulk-derived
signature, or a bulk deconvolution result is an active target in a standalone mechanism or
radiogenomics study. This is a
decision playbook, not a software tutorial. It converts the 33 screened studies in
[bulk-rna-literature-map-2024-2026.tsv](bulk-rna-literature-map-2024-2026.tsv) into gates, repair
actions, reporting artifacts, and claim
boundaries.

## Evidence binding and scope

- Evidence IDs `BK01`–`BK33` refer only to the companion TSV. The corpus was screened on
  2026-08-21 for formal publication from 2024-08-21 through 2026-08-21 and a screening-date latest
  verifiable JIF of at least 10.
- The evidence is used to change a decision, not to endorse one default pipeline. A method paper
  establishes what can be estimated under its benchmark; it does not prove validity in a new
  tissue, platform, disease, or endpoint.
- The patient or independent biological specimen is the unit of clinical inference. Reads,
  technical replicates, genes, junctions, lesions, and multiple biopsies do not increase the
  number of independent patients.
- Label every output with the shared primary evidence state (**measured**, **derived**, **estimated**,
  **associated**, **predicted**, or **perturbed**), retain the bulk-specific subtype, and record the
  claim link as **direct**, **inferred**, or **proposed**. Deconvolved fractions, inferred splicing-factor activity,
  RNA-predicted protein, and multimodal model scores are not direct observations.
- For `study_scope == mechanism-only`, do not request imaging, radiology habitats or
  sample-to-image fields. Only when `study_scope == imaging-mechanism`, open
  `sample-to-image-mapping.md` and require lesion/region/time linkage; weak mapping then limits the
  imaging–molecular result to a patient-level association even if the RNA analysis is otherwise
  strong.

## Route the request before analysing

| User intent | Primary route | Minimum deliverable | Do not substitute |
|---|---|---|---|
| Feasibility or protocol | gates G0–G4 | estimand, matched-n, feature passport, blockers, power/validation plan | a list of tools |
| Differential expression or splicing | blocks 2–5 | model-ready feature contract, contrast, effect/CI/FDR table, diagnostics | a volcano plot alone |
| Pathway, signature, or network interpretation | block 6 | tested universe or rank, gene-set version, leading genes, stability and composition sensitivity | unqualified pathway labels |
| Composition or “virtual cell” inference | block 7 | target cell types/states, reference audit, truth strategy, sensitivity and uncertainty | one deconvolution bar plot |
| Clinical subtype, prognosis, or treatment response | block 8 | target claim, leakage-safe model, calibration/interaction, external validation | internal AUC or survival split only |
| Imaging–transcriptome integration, only when `study_scope == imaging-mechanism` | block 9 | sample-to-image map, unimodal baselines, incremental value, held-out evaluation | joint embedding as validation |
| Manuscript or reviewer audit | blocks 1–10 | PASS/CONDITIONAL/STOP verdicts, exact repair analyses, writing corrections | generic reporting advice |

## User input contract

Request missing items before making a strong recommendation. A user may explicitly accept a
bounded exploratory analysis, but missing information cannot be silently invented.

### Study and estimand

`Population | disease/state | exposure or treatment | comparator | time zero | sampling time | endpoint | target claim | primary contrast | estimand | confirmatory or discovery`

For treatment work, additionally require `treatment arms | randomization or allocation |
biomarker-by-treatment interaction target | censoring/competing events | intended-use population`.

### Samples and linkage

`Patient ID | specimen ID | tissue/biopsy region | tissue date | treatment before tissue collection |
biological replicate | technical replicate | site | batch | discovery/validation membership`.

Only when `study_scope == imaging-mechanism`, append
`Imaging study and date | mapped lesion/region | treatment between scan and tissue |
sample-to-image linkage quality`.

### Assay and raw-feature generation

`Assay/platform | fresh/FFPE/autopsy | extraction and RIN/DV200 | library strategy | strandedness |
read type/length | depth | reference genome | annotation release | aligner/pseudoaligner/assembler |
feature level | count type | spike-ins/calibrators | software and parameters`.

Feature level must be one of `gene | transcript | exon | junction/event | allele/haplotype | de novo
sequence feature | targeted panel`. “Expression matrix” is not a sufficient feature definition.

### Covariates, missingness, and validation

`Age/sex/stage/grade | purity | composition | site/batch/platform | treatment | pairing/longitudinal
structure | missingness by variable | external cohort | orthogonal truth | frozen signature/model`.

### Required files when auditing completed work

Provide the sample sheet, raw/processed QC summaries, feature annotation, design matrix or model
formula, complete unfiltered result tables, pathway/gene-set versions, deconvolution reference and
truth source, split/fold assignments, model code/configuration, and figure legends.

## Verdict language

- **PASS**: the target estimand is identifiable; feature generation and QC are traceable; the
  inferential unit/model are valid; uncertainty, multiplicity, and validation match the claim.
- **CONDITIONAL**: the analysis can answer a narrower question after a stated repair or sensitivity
  analysis. Name the allowed claim, missing evidence, owner, and completion criterion.
- **STOP**: continuing would yield a non-identifiable or materially misleading result. Stop for
  complete group–batch confounding, no independent biological replication for population claims,
  incompatible or unknowable feature generation, outcome leakage, non-overlapping discovery and
  validation definitions, or a treatment-predictive claim without treatment comparison/interaction.

A STOP does not prohibit descriptive QC or transparent data inventory. It prohibits the claimed
inferential analysis until the blocking condition changes.

## End-to-end stage gates

| Gate | Decision | PASS evidence | CONDITIONAL route | STOP trigger | Required artifact |
|---|---|---|---|---|---|
| G0 Question | Is the target claim and estimand explicit? | population, contrast, time, endpoint and claim class fixed | exploratory association with narrowed wording | causal/predictive claim cannot be represented by the design | estimand card |
| G1 Cohort | Is matched biological n valid? | patient/specimen crosswalk, replicate roles and exclusions fixed | aggregate repeated specimens or fit a justified hierarchical model | cells/reads/lesions counted as independent patients; no biological replication | cohort and mapping table |
| G2 Feature | Does the matrix represent the intended molecule? | reference, annotation, strandedness, pipeline and feature level recorded | reprocess or restrict to compatible features | provenance missing or gene/transcript/junction units mixed | feature-generation passport |
| G3 QC | Are pre-analytic and technical artifacts bounded? | pre-specified sample/feature QC plus batch and tissue-quality diagnostics | sensitivity analysis or narrower cohort | artifact perfectly confounded with the primary contrast | QC decision log |
| G4 Inference | Can the design estimate the contrast with adequate information? | model formula, pairing, covariates, independent n, effect/CI/FDR and power rationale | exploratory effect estimation with uncertainty and no absence claim | underpowered null marketed as equivalence; unidentifiable design | analysis contract |
| G5 Molecular layer | Is gene, isoform, splicing, pathway, or network inference task-matched? | compatible counts/null, coverage, gene-set/network provenance | orthogonal confirmation or alternate representation | a gene-level matrix is used to claim unmeasured isoform/allele effects | layer-specific result table |
| G6 Composition | Is mixture addressed without converting estimates into observations? | purity/reference/shift audit, benchmark-relevant method, uncertainty and truth/sensitivity | consensus across plausible references/methods | missing target state/reference with no validation while making cell-specific claims | composition audit |
| G7 Clinical | Is subtype/signature evidence matched to prognostic or predictive intent? | locked definition, patient-level split, calibration, external validation; interaction for treatment prediction | discovery-only candidate with explicit future validation | outcome-guided preprocessing; treatment prediction without comparator | clinical evidence table |
| G8 Multimodal, only when `study_scope == imaging-mechanism` | Does RNA add value beyond imaging/clinical baselines? | matched modalities, train-only fusion, unimodal baselines, incremental and external evaluation | association-only triangulation | sample/lesion/time mismatch or leakage across modalities | multimodal comparison table |
| G9 Validation | Does validation test the same frozen object? | same estimand/features/model, independent patients, direction/effect/CI and failure accounting | cross-platform/orthogonal corroboration with bounded claim | reused patients, refitted “validation” model, or endpoint drift | validation manifest |
| G10 Reporting | Can a reviewer reproduce the claim and see its boundary? | Methods/Results/legend/Discussion aligned with complete supplements | explicit unresolved limitation | invented metadata, selective result reporting, or measured/inferred conflation | manuscript evidence map |

Do not use a PASS in one claim branch to conceal a CONDITIONAL gate required by another branch.
Resolve or carry each condition forward in every downstream table and sentence.

## Decision block 1 — research question, estimand, and inferential unit

**Evidence anchor:** `BK06`, `BK12`, `BK19`, `BK20`, `BK21`, `BK32`.

### Expand

- Write the estimand as a contrast in a defined population and time: sample-level mean expression,
  within-patient change, subtype membership, outcome risk, treatment-effect modification, or
  incremental multimodal prediction.
- Separate descriptive molecular characterization, etiologic association, prognosis, diagnosis,
  and treatment prediction. `BK32` changes the decision by requiring an explicit biomarker-by-
  treatment interaction before using “treatment sensitivity” and by distinguishing prespecified
  from exploratory interactions; `BK20` shows how a randomized
  treatment context plus external cohort supports, but does not universalize, a response signature.
- Determine independent biological n before selecting models. `BK12` shows why increasing a fold-
  change cutoff does not repair low replication or poor power.
- For unsupervised subtypes, define the object to be clustered and the stability/replication target.
  `BK21` requires cross-method and cross-cohort consensus rather than a single preferred clustering.

### Review

Check whether the contrast is encoded in the design matrix; whether paired/longitudinal samples,
multiple lesions, or repeated biopsies are nested correctly; whether the endpoint or treatment
occurred before/after RNA sampling. When `study_scope == imaging-mechanism`, additionally check
whether selection into the matched imaging–RNA cohort changes the target population.

### Interpret and decide

- **PASS:** model coefficient maps one-to-one to the declared estimand; patient/specimen roles and
  analysis population are explicit; the claim class matches the design.
- **CONDITIONAL:** exploratory cross-sectional association is feasible, but prognosis, temporal
  change, treatment response, or regional biology must be removed from the claim.
- **STOP:** primary condition equals batch/site with no overlap; no independent biological
  replication; outcome or future treatment information was used to create features; “predictive”
  is claimed from one treatment arm.

### Repair or add analysis

Rebuild the sample crosswalk; aggregate technical replicates before inference; use a paired or
mixed model when the estimand requires it; pre-specify one primary contrast and test family;
recast an unpowered null as an imprecise estimate with CI; for treatment prediction add the formal
interaction or downgrade to prognostic association.

### Writing four-part contract

- **Methods:** state population, independent n, biological unit, estimand, exact coefficient/
  contrast, covariates, multiplicity family, and validation success rule.
- **Results:** lead with effect size and CI, then FDR/p value; report patients and specimens
  separately and include failures/exclusions.
- **Figure legend:** identify biological n, pairing/nesting, center line/error interval, exact test,
  sidedness, adjustment family, and whether the panel is discovery or validation.
- **Discussion:** name every invoked claim branch—such as descriptive, association, prediction,
  treatment effect, mechanism or causality—and the shortest unmet requirement for each; do not
  imply that they are sequential grades.

## Decision block 2 — sample, assay, and raw feature generation

**Evidence anchor:** `BK01`, `BK02`, `BK07`, `BK09`, `BK13`.

### Expand

- Build a feature-generation passport from FASTQ/BAM or assay output to the tested matrix.
  `BK07` makes the reference genome/representation a reported analysis choice; `BK02` requires
  reference-based and reference-free assembly QC when transcript reconstruction is central.
- Route annotation-free sequence discovery separately from ordinary quantification. `BK01` can
  find unannotated splicing/circular RNA from raw reads but is not an end-to-end gene-count route.
- Treat targeted RNA as a different measurement universe. `BK09` supports clinical fusion/splice/
  expression detection in FFPE but does not make a targeted panel equivalent to whole-transcriptome
  profiling.
- State whether the analysis is relative abundance or calibrated absolute transcript quantity.
  `BK13` shows that absolute claims require calibrators introduced during sample processing.

### Review

Verify FASTQ pairing, read length and strandedness; genome build and annotation release; aligner,
pseudoaligner or assembly mode; multi-mapping/duplicate/junction handling; gene ID version and
collapse rules; feature type and units; targeted-panel content; and whether samples were processed
together with any spike-in or SI-traceable calibrator.

### Interpret and decide

- **PASS:** every tested row maps to a versioned biological feature and one compatible unit;
  feature generation is reproducible and task-matched.
- **CONDITIONAL:** gene-level analysis remains possible after restricting to a common annotation
  or reprocessing; reference-sensitive loci are labelled and sensitivity-tested.
- **STOP:** counts from incompatible genome/annotation/strandedness routes are merged without
  recovery; transcript/exon/junction rows are treated as genes; absolute abundance is inferred
  from historical relative counts without calibrators.

### Repair or add analysis

Reprocess from the earliest common raw level; produce annotation mapping and attrition tables;
rerun key signals under a second reference where biologically material; inspect junctions or
assemblies visually/orthogonally; analyze targeted panels within their measured universe; replace
absolute wording with relative abundance when no calibrator exists.

### Writing four-part contract

- **Methods:** report material, extraction, library, read properties, reference/annotation, command
  or workflow versions, feature definition, counting rules and calibrators.
- **Results:** report reads/samples/features entering and leaving each step, mapping/assignment/
  assembly metrics, panel or reference coverage, and failed specimens.
- **Figure legend:** name the plotted unit and transformation; state whether zero means not detected,
  not targeted, filtered, or structurally absent.
- **Discussion:** bound reference/annotation sensitivity, panel ascertainment, and relative-versus-
  absolute measurement; do not claim an unmeasured transcriptome-wide absence.

## Decision block 3 — pre-analytic variables and QC

**Evidence anchor:** `BK03`, `BK08`, `BK09`, `BK13`.

### Expand

- Treat collection-to-preservation time, temperature, ischemia/post-mortem interval, extraction,
  RIN/DV200, input quantity, FFPE age, library/run, and tissue composition as candidate causes of
  signal, not cosmetic metadata.
- `BK08` demonstrates that even short and long post-mortem handling can induce structured brain
  transcriptional programs. A processing score can flag risk but cannot reconstruct the original
  transcriptome.
- `BK09` requires reporting real-world assay failure and diagnostic yield rather than silently
  excluding poor FFPE samples. `BK03` warns that platform/protocol performance from cell lines
  must not be copied to low-input or FFPE tissue.
- Use calibrators such as those in `BK13` to quantify technical bias only when they accompanied the
  biological material through processing.

### Review

Plot QC by primary group, site, batch and outcome; inspect library complexity, mapping/assignment,
gene-body/coverage or insert metrics, degradation signatures, sample correlation/PCA, sex and
tissue identity checks, contamination, outliers, replicate concordance, missingness and exclusion
timing. Confirm QC rules were not chosen after seeing the endpoint.

### Interpret and decide

- **PASS:** QC thresholds were pre-specified or blinded to outcome; retained groups overlap in
  technical covariates; exclusions and assay failures are fully accounted for.
- **CONDITIONAL:** residual quality differences can be covariate-adjusted and tested by restriction/
  sensitivity; claims are limited to the retained quality range.
- **STOP:** quality, processing time, site, or platform is perfectly aligned with the primary group;
  mislabeled/contaminated samples cannot be resolved; selective QC depends on outcome or model fit.

### Repair or add analysis

Recover metadata; blind and freeze QC thresholds; repeat analyses with/without flagged samples;
restrict to comparable quality or site; model quality covariates without adjusting away the target
biology; add negative-control processing signatures; report the lost target population and
selection bias rather than hiding failures.

### Writing four-part contract

- **Methods:** define every sample-level and feature-level QC criterion, when it was applied, who/
  what was blinded, and treatment of technical replicates and failures.
- **Results:** give initial, failed, excluded and analysed counts with reasons by group/site; show
  QC distributions rather than only thresholds.
- **Figure legend:** state whether panels are pre- or post-QC, the n at each level, outlier rule,
  batch/site encoding, and transformation.
- **Discussion:** name residual pre-analytic confounding and the population excluded by QC; never
  say batch correction “removed all technical variation.”

## Decision block 4 — normalization, differential expression, power, and multiplicity

**Evidence anchor:** `BK06`, `BK08`, `BK12`, `BK13`.

### Expand

- For count inference, keep raw count-like inputs and an explicit design. `BK06` supports quasi-
  likelihood, small/fractional count handling, complex contrasts, fold-change thresholds and
  exon/transcript usage, but does not license TPM as count input.
- Define filtering, library-size/composition normalization, dispersion/mean–variance modeling,
  covariates, contrast, test family, effect-size threshold and FDR before inspecting desired genes.
- Use independent biological n, expected variability and plausible effect to discuss power.
  `BK12` shows that a stricter fold-change filter cannot rescue a weak experiment.
- Distinguish relative compositional change from absolute molecules. `BK13` changes this decision
  when suitable calibrators exist.

### Review

Inspect count provenance; low-count filtering; library composition and zero patterns; normalization
factors; mean–variance and dispersion diagnostics; design rank and confounding; residuals/influence
and sample-level outliers; number and definition of tests; FDR method; effect/CI; donor consistency;
and whether all preprocessing was fit without validation/outcome leakage.

### Interpret and decide

- **PASS:** count-compatible model and estimable design; effect/CI/FDR reported; results are stable
  to plausible filtering, normalization and influential-sample checks.
- **CONDITIONAL:** exploratory estimates can be reported with wide uncertainty, restricted cohort,
  robust sensitivity or independent replication requirement.
- **STOP:** TPM/FPKM fed into a count likelihood without justification; singular design; group is
  inseparable from batch; no biological replication for a population contrast; uncorrected
  high-dimensional scan presented as confirmatory.

### Repair or add analysis

Return to raw counts or use an appropriate continuous-expression model; simplify the estimand/
design; aggregate technical replicates; re-estimate normalization within the analysis population;
add influence and leave-one-sample-out checks; report a complete result table; obtain more
biological samples or downgrade absence/equivalence claims.

### Writing four-part contract

- **Methods:** state filter, normalization, model family, formula, contrasts, robust/outlier policy,
  effect threshold, sidedness, FDR family, software/version and sensitivity analyses.
- **Results:** report effect, CI, raw p and adjusted p with tested-feature denominator; include
  direction consistency and sensitivity, not only DEG counts.
- **Figure legend:** define log-fold change base/reference, adjusted p, thresholds, displayed versus
  tested features, n and any shrinkage/transformation.
- **Discussion:** a non-significant result is inconclusive unless the CI excludes a meaningful
  effect; distinguish relative abundance from absolute transcript quantity.

## Decision block 5 — isoforms, splicing, long reads, and allele-specific inference

**Evidence anchor:** `BK03`, `BK04`, `BK05`, `BK10`, `BK11`, `BK31`.

### Expand

- Route the biological question to transcript discovery/quantification, differential transcript
  usage, local splice event, targeted event measurement, allele-specific expression/splicing, or
  inferred splicing-factor activity. These outputs are not interchangeable.
- `BK03` and `BK05` benchmark long-read isoform discovery across protocols and resolutions;
  `BK04` adds SNP calling, phasing and allele-specific splicing. `BK10` shows that targeted LSV-seq
  gains sensitivity for preselected low-coverage events. `BK11` supports cross-platform event
  detection, including unannotated events. `BK31` estimates regulator activity from exon-inclusion
  signatures rather than regulator expression.

### Review

Check molecule/read accuracy, depth and full-length support; transcript annotation and collapsing;
junction/event coverage and minimum counts; biological replication; event-specific null and
multiplicity; haplotype phasing and mapping bias; platform/reference comparability; and whether the
claimed regulator activity is directly measured or inferred from a perturbation-derived network.

### Interpret and decide

- **PASS:** task-specific counts, coverage, null and biological replication are adequate; key novel
  events/alleles have visual or orthogonal support.
- **CONDITIONAL:** candidate ranking is allowed when coverage or transfer is limited, with targeted
  validation required and no transcriptome-wide absence claim.
- **STOP:** gene-level counts are used to claim isoform switching; targeted-panel non-detection is
  called global absence; unphased/biased reads support a cis-regulatory claim; pseudobulk cells are
  treated as independent patients.

### Repair or add analysis

Requantify at transcript/exon/junction level; require minimum informative reads and donor
consistency; use short-read junction evidence or targeted RT-PCR/LSV-seq; audit reference-mapping
bias and phasing; validate predicted protein consequence; label `BK31` output “inferred splicing-
factor activity.”

### Writing four-part contract

- **Methods:** specify platform/chemistry, basecalling or read processing, transcript construction,
  event definition, coverage filter, phasing, model/null, FDR and validation assay.
- **Results:** report event-level effect and uncertainty, supporting reads/donors, annotated versus
  novel status, gene-level concordance/discordance and validation result.
- **Figure legend:** draw exon/junction coordinates and strand; state read/support denominator,
  PSI/usage definition, haplotype assignment and whether traces are measured or inferred.
- **Discussion:** do not translate an RNA event into protein/function or cis mechanism without
  protein, perturbation, allele or other orthogonal evidence.

## Decision block 6 — pathways, signatures, co-expression, and regulatory interpretation

**Evidence anchor:** `BK21`, `BK24`, `BK25`, `BK28`, `BK29`, `BK30`, `BK31`, `BK33`.

### Expand

- Route analyses explicitly: ORA tests overlap among a selected list; preranked GSEA tests
  coordinated directional shifts across a ranked universe; per-sample scoring creates a derived
  phenotype; co-expression builds association modules; regulator/activity tools infer latent
  activity; RNA-to-protein models predict an unmeasured layer.
- Record the tested-gene universe for ORA and the signed ranking statistic for GSEA. Version every
  collection and collapse redundant pathways without hiding discordant leading genes.
- `BK29` and `BK30` show the scale and utility of learned/co-expression gene relationships, while
  also motivating a hard boundary: embedding proximity or co-expression is not a directed
  regulatory edge. `BK31` shows why inferred activity may differ from regulator expression.
- Use `BK25` PerturbAtlas and `BK28` ASTRA to test whether a proposed program recurs under genetic
  perturbation or generic stress, but return to original studies and conditions before a causal
  statement. Use `BK24` PRECOG for outcome replication, not for automatic model validation.
- `BK33` permits protein-candidate prioritization from RNA but requires the label “RNA-predicted”
  until measured proteomics or another protein assay confirms it.

### Review

Check universe/rank and ties; gene identifiers and collection/version; gene-set size and overlap;
direction and leading genes; score scale and preprocessing; whether scoring/thresholding occurred
inside training folds; module preservation and donor stability; composition/purity sensitivity;
network direction/evidence source; external-dataset overlap; and direct versus predicted protein.

### Interpret and decide

- **PASS:** pathway direction is supported by a declared test, FDR, leading genes and stability;
  network/module language remains associative; any derived score is locked before validation.
- **CONDITIONAL:** a pathway/module is hypothesis-generating when gene-set redundancy, composition
  or cohort transfer is unresolved; require alternate collection, deconvolution/purity adjustment
  or module-preservation analysis.
- **STOP:** ORA has no defensible background; GSEA rank was selected after inspecting results;
  score construction used outcome/validation data; one hub/embedding neighbor is called a regulator;
  RNA-predicted protein is presented as measured protein.

### Repair or add analysis

Recreate the appropriate universe/rank; map versioned identifiers and disclose dropped genes;
cluster redundant terms and show leading-edge genes; rebuild scores within training only and test
scale transfer; test modules after purity/composition adjustment and in an independent cohort;
compare perturbation/stress references; validate predicted protein or downgrade the claim.

### Writing four-part contract

- **Methods:** name database/release, universe or ranking statistic, score algorithm and
  normalization, redundancy rule, network construction/stability test, FDR family and train-only
  steps.
- **Results:** give NES/overlap or score effect with CI/FDR, leading genes, cohort/module stability,
  composition sensitivity and discordant pathways; distinguish measured and predicted layers.
- **Figure legend:** define color/score direction and scale, tested versus displayed terms, FDR,
  similarity/redundancy rule, edge meaning and whether a network is directed or undirected.
- **Discussion:** use “enriched,” “associated module,” “inferred activity,” or “RNA-predicted
  protein”; reserve “activated,” “regulated,” and protein-level claims for appropriate evidence.

## Decision block 7 — tumour purity, composition, and deconvolution

**Evidence anchor:** `BK14`, `BK15`, `BK16`, `BK17`, `BK18`, `BK22`, `BK23`, `BK26`.

### Expand

- Define the target before choosing a tool: broad cell fraction, RNA fraction, absolute cell
  fraction, cell-type-specific expression, or within-type state. `BK23` provides the decision
  taxonomy; it is a guide, not independent validation.
- Audit total transcriptome-size and gene-length effects (`BK14`), reference-to-bulk batch shift
  (`BK15`), controlled-mixture performance and difficult functional states (`BK16`), pseudobulk-to-
  real distribution shift and reference choice (`BK17`), incomplete references and cross-platform
  robustness (`BK18`), and tumour-state/purity dependence (`BK22`).
- `BK26` can provide cross-cancer immune context, but platform scores and fractions remain estimates
  influenced by tumour purity and cancer-type composition.
- Choose a truth strategy before interpreting: FACS, IHC/RNA-ISH, known laboratory mixtures,
  matched single-cell/nucleus measurements, or at minimum cross-reference/method sensitivity.

### Review

Record target quantity; cell ontology and resolution; reference donors/tissue/disease/platform;
unknown/missing states; transcriptome-size correction; marker specificity; signature overlap;
bulk/reference normalization and batch handling; rare-cell limit; purity; negative controls;
ground truth; uncertainty; and whether a result is an estimate of cells, RNA contribution, or
cell-type-specific expression.

### Interpret and decide

- **PASS:** reference covers the target biology; method has a benchmark relevant to the tissue/
  platform; known mixtures or orthogonal measurements show acceptable performance; conclusions
  include uncertainty and composition-versus-expression alternatives.
- **CONDITIONAL:** use a consensus/sensitivity range across plausible references or methods and
  limit claims to broad cell classes when fine states lack truth.
- **STOP:** target state is absent from the reference and no independent evidence exists; same
  single-cell data create pseudobulk and reference and are called external validation; fractions
  are converted to absolute cells without calibration; inferred cell-specific DE is described as
  direct single-cell measurement.

### Repair or add analysis

Match or rebuild the reference; harmonize gene space without erasing disease biology; correct/test
transcriptome-size effects; include an unknown/other component where justified; collapse
unresolvable subtypes; compare at least two plausible references/method families; validate selected
fractions by IHC/FACS/RNA-ISH or matched single-cell data; rerun downstream associations with purity
and composition terms.

### Writing four-part contract

- **Methods:** define estimand, algorithm/version, reference provenance and donors, gene selection,
  normalization/batch/transcriptome-size handling, unknown states, truth source and uncertainty/
  sensitivity plan.
- **Results:** say “estimated”; report reference/method variability, rare-state performance, purity
  sensitivity, negative controls and agreement with orthogonal truth—not only correlations.
- **Figure legend:** identify estimate type, reference, normalization, whether bars are constrained
  to sum to one, error/replicate information, and ordering/clustering rules.
- **Discussion:** deconvolution localizes a plausible cellular source but does not directly observe
  cells, state transitions, signaling, or cell-specific causality.

## Decision block 8 — clinical subtype, diagnostic utility, prognosis, and treatment prediction

**Evidence anchor:** `BK09`, `BK20`, `BK21`, `BK24`, `BK27`, `BK32`.

### Expand

- Classify the intended result before modeling: analytical/diagnostic utility, unsupervised subtype,
  prognostic association, response association, or treatment-predictive interaction.
- `BK09` changes clinical assay review by requiring failure rate, revised diagnosis and treatment
  consequence, not only analytical detection. `BK21` requires subtype consensus across methods,
  cohorts, time points and treatment settings.
- `BK24` PRECOG and `BK27` CTR-DB can supply independent outcome/therapy contexts only after
  patient/publication overlap, endpoint, platform and treatment definitions are audited.
- `BK20` demonstrates nested resampling, external cohort testing and panel translation. `BK32`
  contrasts a prespecified Decipher analysis with a non-prespecified PTEN–docetaxel interaction,
  showing that treatment-interaction evidence must retain its prespecification status.

### Review

Check intended use and time zero; inclusion/exclusion and spectrum; endpoint/adjudication;
treatment availability and assignment; censoring; signature derivation and lock; sample/event
counts; patient-level split; nested tuning; calibration; comparator models; decision threshold;
external cohort overlap and transport; subgroup/interactions; and assay failure/missingness.

### Interpret and decide

- **PASS:** frozen signature/subtype applied to unseen independent patients; performance includes
  CI and calibration; clinical baselines are compared; treatment prediction includes a valid
  interaction and arm-specific effects.
- **CONDITIONAL:** internally validated discovery signature or cross-cohort association may be
  reported as a candidate, not a clinical test; subtype utility remains exploratory until stable
  assignment and outcome/treatment relevance replicate.
- **STOP:** feature selection or thresholding used validation outcomes; the same/overlapping public
  patients appear in discovery and validation; a median split creates the endpoint; treatment
  sensitivity is claimed from responders in one arm or from a prognostic Cox association.

### Repair or add analysis

Deduplicate cohorts by accession/publication/sample identifiers; freeze preprocessing, genes,
coefficients and threshold; use nested CV only for development; test an untouched external cohort;
report calibration and clinical-only comparator; add interaction and arm-specific absolute effects;
translate to a feasible assay and account for test failure; otherwise downgrade to exploratory.

### Writing four-part contract

- **Methods:** state intended use, time zero, endpoint, development/validation populations, full
  locked signature, internal/external validation, metrics/calibration, comparator, interaction and
  missing/failure handling.
- **Results:** report flow, events and failures; effect/AUC or other metric with CI; calibration;
  validation degradation; subgroup interaction rather than within-group significance; and net/
  incremental value when relevant.
- **Figure legend:** distinguish development, internal validation and external validation; state n/
  events, censoring/time horizon, locked cutoff, CI method and model version.
- **Discussion:** “prognostic” means outcome association independent of treatment; “predictive” is
  reserved for differential treatment effect. Do not claim clinical utility from discrimination
  alone.

## Decision block 9 — optional multimodal and radiotranscriptomic integration

Use this block only when `study_scope == imaging-mechanism`. Skip it for mechanism-only bulk RNA
research; its absence is not missing evidence for a molecular, cellular or perturbational claim.

**Evidence anchor:** `BK13`, `BK18`, `BK19`, `BK33`.

### Expand

- Start from a patient–lesion–region–time crosswalk. RNA and imaging from the same patient are not
  necessarily from the same lesion or biological state.
- Predefine whether the goal is association, shared latent biology, response prediction, or
  localization. `BK19` shows that clinical, pathology, PET and bulk transcriptomic information can
  add predictive value, but requires explicit unimodal and routine-clinical baselines.
- Build a baseline ladder: clinical only; imaging only; RNA only; clinical+imaging;
  clinical+RNA; full multimodal model. Evaluate the incremental gain and uncertainty of each step.
- `BK18` supports tissue-level multi-omics deconvolution but its reconstructed cellular layers are
  estimated. `BK33` RNA-predicted protein and `BK13` calibrated absolute RNA are distinct views,
  not interchangeable substitutes for measured proteomics.

### Review

Audit patient/lesion/region/time matching; treatment interval; modality missingness and selection;
sample aggregation; per-block scaling; dimension imbalance; feature extraction and harmonization;
fold assignment shared across modalities; train-only imputation/normalization/fusion; clinical and
unimodal baselines; calibration; external transport; and whether latent-factor labels were chosen
after viewing outcomes.

### Interpret and decide

- **PASS:** all modalities map to the same inferential unit and allowed biological scale; fusion is
  trained without held-out information; full model adds reproducible value over strong baselines;
  shared factors are supported by loadings and external/orthogonal evidence.
- **CONDITIONAL:** patient-level association is possible despite uncertain tissue localization;
  claims must avoid regional co-localization and model gains require independent validation.
- **STOP:** samples or time points are mismatched for the intended regional/causal claim; slices,
  ROIs or biopsies leak across patient folds; full-cohort normalization/factor learning precedes
  validation; only the fused model is reported.

### Repair or add analysis

Rebuild the mapping table; aggregate at patient/lesion level; exclude or sensitivity-test treatment
mismatch; fit every data-dependent step inside training; compare the baseline ladder; quantify
incremental discrimination, calibration and clinical value; perform missing-modality and site/
batch sensitivity; downgrade to cross-modal triangulation when true integration is unsupported.

### Writing four-part contract

- **Methods:** define mapping level/time window, modality preprocessing and scale, split hierarchy,
  fusion stage, missing-view strategy, baseline ladder, tuning, calibration and external validation.
- **Results:** report intersection n and modality attrition; unimodal versus multimodal performance
  with CI; incremental value; site/batch and mapping sensitivity; factor loadings/leading genes.
- **Figure legend:** label measured versus estimated/predicted layers, training versus validation,
  patient-level n, registration/mapping level, model version and uncertainty.
- **Discussion:** use “patient-level radiotranscriptomic association” when tissue location is
  uncertain; multimodal prediction does not establish that an imaging phenotype directly measures
  a pathway or cellular state.

## Decision block 10 — validation, reproducibility, and evidence escalation

**Evidence anchor:** `BK02`, `BK03`, `BK12`, `BK13`, `BK16`, `BK17`, `BK19`, `BK20`, `BK21`,
`BK23`, `BK24`, `BK25`, `BK26`, `BK27`, `BK28`, `BK32`, `BK33`.

### Expand

- Define the validation object before seeing validation outcomes: feature definition, contrast,
  score/model, preprocessing, reference, cutoff, endpoint, time horizon and success criterion.
- Match validation to the claim. Benchmarks need relevant truth and stress scenarios; associations
  need independent biological samples and direction/effect replication; prediction needs a locked
  model, calibration and useful comparator; mechanism needs perturbation or orthogonal support.
- Treat public resources (`BK24`–`BK28`) as candidate sources only after accession, sample overlap,
  platform, condition, endpoint and metadata quality are verified.
- Preserve negative and failure evidence: assay failures (`BK09`), state/reference weaknesses
  (`BK16`–`BK18`), sample-size uncertainty (`BK12`), cross-platform degradation (`BK03`, `BK20`),
  and RNA–protein gap (`BK33`).

### Review

Inspect discovery/validation patient overlap; whether any filter, harmonization, gene set, module,
reference, threshold or model was refit; endpoint and feature equivalence; population/platform
shift; missingness; all attempted validations; software/container/reference versions; random
seeds; code and accession availability; correction notices; and complete result tables.

### Interpret and decide

- **PASS:** independent patients, frozen object and same estimand; validation reports direction,
  magnitude, CI/calibration and failures; code/data provenance permits re-execution.
- **CONDITIONAL:** cross-platform or orthogonal corroboration supports a bounded association but
  not the original clinical performance; internal resampling supports development only.
- **STOP:** patient/sample overlap; validation labels used for preprocessing or selection; model or
  cutoff is optimized in validation and called frozen; endpoint changes; only successful cohorts
  are disclosed; accession/model cannot be identified.

### Repair or add analysis

Create a validation manifest and overlap audit; restore the original frozen pipeline; if refitting
is unavoidable, relabel the cohort as development and obtain a new validation set; harmonize by a
pre-specified mapping without outcome information; release code/configuration and complete tables;
reproduce key claims with alternate reference/method and orthogonal assay.

### Writing four-part contract

- **Methods:** name all cohorts/accessions, split rationale, overlap checks, frozen artifacts,
  success criteria, external transformation, software/reference versions, code/data availability
  and corrections consulted.
- **Results:** report every attempted validation, attrition/failure, effect/performance with CI,
  direction, calibration, heterogeneity and sensitivity—not “validated” based only on p<0.05.
- **Figure legend:** identify cohort and role, n/events, frozen versus refit elements, exact
  statistic/CI, platform differences and whether evidence is orthogonal or independent.
- **Discussion:** distinguish internal reproducibility, external replication, cross-platform
  transport and experimental validation; state what failed and how that limits scope.

## Standard output contract

Return only the components needed for the user’s mode, but preserve the order of dependency:

1. **Decision summary:** one-line target claim, applicable claim branch or branches, branch-specific
   `PASS | CONDITIONAL | STOP`, and overall study verdict.
2. **Estimand card:** population, biological unit, contrast/exposure, time, endpoint, effect
   measure, covariates, test family, and intended interpretation.
3. **Sample/cohort table:** patient, specimen, tissue/region, time/treatment, assay, site/batch,
   replicate role, discovery/validation role and exclusions. Only when
   `study_scope == imaging-mechanism`, append imaging study, mapped lesion/region, scan-to-tissue
   interval and linkage uncertainty.
4. **Feature-generation passport:** material → library → reads → reference/annotation →
   alignment/assembly → feature/count unit → filtering/normalization.
5. **QC decision log:** criterion, rationale, blinded/pre-specified status, affected samples/
   features, group imbalance, verdict, sensitivity and final action.
6. **Primary result table:** feature/contrast, effect, CI, raw p, adjusted p, denominator/test
   family, donor consistency, sensitivity, primary evidence state, modality subtype and claim-link
   status.
7. **Interpretation table:** finding, pathway/cell/clinical meaning, alternative explanation,
   composition/reference sensitivity, evidence ID, allowed claim, required validation.
8. **Validation manifest:** cohort/accession, overlap status, frozen artifacts, endpoint/features,
   result with uncertainty, failure/shift, verdict.
9. **Repair plan:** blocker, exact analysis/data needed, owner/input, completion criterion, and
   claim permitted if unresolved.
10. **Manuscript map:** exact Methods, Results, figure-legend, Discussion and supplement items.

## Three-axis evidence record and branch-specific claim requirements

The axes are independent labels, not a ladder.

| Axis | Allowed values | Bulk-RNA use |
|---|---|---|
| Primary evidence state | `measured`, `derived`, `estimated`, `associated`, `predicted`, `perturbed` | assay counts are measured; normalized/pseudobulk summaries are derived; deconvolution or activity is estimated; a sample-level effect is associated; a locked unseen-sample output is predicted; an observed assigned intervention result is perturbed |
| Modality subtype | declared operation such as `gene-count`, `transcript-usage`, `pathway-enrichment`, `coexpression-module`, `deconvolution`, `clinical-model`, `perturbation-response` | identifies how the result was produced without changing its primary state |
| Claim-link status | `direct`, `inferred`, `proposed` | records how directly that result supports the sentence under review |

`missing` means no evidence is available and belongs in the gap register. It must never be entered as
a primary evidence state.

| Claim branch | Required support | Bulk-RNA STOP example |
|---|---|---|
| Descriptive | traceable feature generation, assay/QC contract, correct biological denominator and uncertainty | inferred fraction or predicted protein called measured |
| Association | prespecified sample-level contrast, estimable model, effect/CI, multiplicity, confounder/composition sensitivity and appropriate replication | reads or biopsies treated as independent patients; complete group–batch confounding |
| Localization | tissue/region provenance plus direct spatial or orthogonal localization at the claimed scale; if `study_scope == imaging-mechanism`, also valid sample-to-image registration | bulk composition alone assigned to a cell or local habitat |
| Prediction | locked signature/model and preprocessing, patient-level split, named baseline, unseen validation, calibration and transport/OOD analysis | internal AUC or outcome-guided feature construction |
| Treatment effect or effect modification | treatment comparator, explicit biomarker-by-treatment interaction or identified causal contrast, time zero, allocation/confounding strategy, effect/CI and independent confirmation | one-arm response or prognosis relabelled as treatment benefit |
| Mechanistic | explicit competing hypotheses, directional molecular chain, temporal compatibility, target engagement, mediator/pathway and phenotype readouts, perturbation or strong orthogonal triangulation, and alternative-mechanism tests | pathway enrichment or co-expression alone called mechanism |
| Causal | explicit causal estimand; randomized intervention or defended exchangeability/positivity/consistency assumptions; temporal order; negative-control/sensitivity analysis; intervention and rescue where applicable | observational correlation alone or unresolved post-treatment bias |

Report a verdict for every invoked branch. A result may PASS prediction and STOP mechanism, or PASS
association while localization remains untested; there is no single “highest grade” and no automatic
next rung.

## Reviewer checklist

| Review question | PASS evidence | Frequent defect | Exact repair |
|---|---|---|---|
| Is the estimand named? | one coefficient/contrast maps to the claim | “identify biomarkers” without target | write estimand card and primary contrast |
| Is independent n correct? | patients/specimens separated from technical replicates | reads/biopsies/cells inflate n | aggregate or model nesting |
| When `study_scope == imaging-mechanism`, is tissue linked to imaging? | lesion/region/time/treatment crosswalk | same patient assumed same biology | rebuild map; downgrade to patient level |
| Is feature provenance complete? | versioned reference, annotation, feature and unit | “normalized expression” only | feature passport or reprocess |
| Is targeted versus whole transcriptome clear? | measured panel universe stated | non-targeted gene called absent | constrain universe and wording |
| Is QC independent of outcome? | frozen/blinded rules and full flow | desired result drives exclusions | rerun frozen QC and sensitivity |
| Are pre-analytics balanced? | group/site plots and overlap | PMI/RIN/FFPE equals phenotype | restrict/adjust or STOP |
| Is normalization model-compatible? | count method uses counts; scale stated | TPM used as raw count | reanalyze with compatible model |
| Is design estimable? | full-rank matrix and coefficient definition | batch equals group | new overlapping data or STOP |
| Are power claims calibrated? | rationale plus effect CI | nonsignificance called no biology | report imprecision; add samples |
| Is multiplicity defined? | number/family of tests and FDR | selected nominal p values | release complete table; adjust family |
| Is splicing/isoform evidence compatible? | junction/transcript counts and coverage | gene DE implies isoform switch | task-specific quantification/validation |
| Is pathway analysis reproducible? | universe/rank, release, leading genes | term name alone | rerun with documented inputs |
| Is network language bounded? | co-expression/module stated | hub called master regulator | perturbation/regulatory evidence or soften |
| Is composition audited? | reference, target quantity, shift and truth | estimate called observed cells | relabel, sensitivity, orthogonal truth |
| Is clinical claim typed correctly? | subtype/prognostic/predictive separated | one-arm response called predictive | interaction or downgrade |
| Is fusion leakage-safe? | patient split; all fitting train-only | full-cohort harmonization/factor learning | refit inside training |
| When `study_scope == imaging-mechanism`, are unimodal baselines shown? | clinical, imaging, RNA and combined models | only best fused model | add baseline ladder/incremental tests |
| Is validation independent and frozen? | overlap audit and manifest | refitted validation | relabel development; find new cohort |
| Are all failures visible? | exclusions, assay failures, negative validations | success-only narrative | complete flow and result supplement |
| Are the three evidence axes distinct? | every table/legend records state, subtype and claim link | predicted protein/fraction called measured | correct labels and branch verdict |
| Can the analysis be rerun? | data/accession, code, config, versions | tool name without parameters | archive workflow and artifacts |

## Wording boundaries

| Unsupported wording | Allowed replacement | Evidence needed for stronger wording |
|---|---|---|
| “Gene X was absent” | “Gene X was not detected above the assay/filter threshold” | validated limit of detection in the measured universe |
| “Pathway X was activated” | “genes in pathway X were directionally enriched” | functional readout or intervention |
| When `study_scope == imaging-mechanism`: “MRI measured immune infiltration” | “MRI features were associated with estimated immune fraction” | validated imaging biomarker against direct cellular measurements |
| “Cell type X increased” from deconvolution | “the estimated contribution/fraction of cell type X increased” | matched direct cell counts with adequate precision |
| “Cell-specific expression changed” from bulk inference | “cell-type-specific expression was computationally inferred to differ” | direct sample-aware single-cell or sorted-cell measurement |
| “Hub gene regulates the module” | “hub gene was highly connected in the co-expression module” | directed perturbation/regulatory evidence |
| “Splicing factor X was active” | “activity of splicing factor X was inferred from exon-inclusion signatures” | direct biochemical/perturbation evidence |
| “Protein X increased” from `BK33`-type output | “RNA-based model predicted higher protein X” | measured proteomics/IHC/western assay |
| “Signature predicts treatment benefit” from prognosis | “signature was associated with outcome” | prespecified biomarker-by-treatment interaction plus validation |
| “Validated” after internal CV | “internally evaluated by nested resampling” | frozen independent external cohort |
| “Mechanism” from multimodal correlation | “cross-modal association consistent with the proposed biology” | perturbation and appropriate temporal/spatial evidence |
| “Batch effect was removed” | “results were adjusted for the recorded batch variable and sensitivity-tested” | impossible to prove complete removal; retain bounded wording |

## Hard constraints and global stopping rules

Stop or explicitly narrow the task when any of the following applies:

1. The primary biological contrast is completely confounded with site, processing, library, or
   another technical factor.
2. The tested matrix cannot be traced to one compatible reference, annotation, biological feature
   and numeric unit.
3. There is no independent biological replication for a population-level inferential claim.
4. Outcome/treatment/validation information influenced QC, filtering, normalization, feature or
   gene-set selection, harmonization, latent-factor learning, thresholding, or hyperparameters.
5. Discovery and validation share patients/samples, or the supposedly frozen object was refit.
6. Treatment benefit is claimed without a comparator and biomarker-by-treatment interaction.
7. A deconvolved, imputed, mapped, activity, protein, or virtual-cell output is reported as measured.
8. A gene-level matrix is used to infer unmeasured isoform, splice, allele, protein, cellular or
   spatial claims without task-specific evidence.
9. When `study_scope == imaging-mechanism`, sample-to-image mapping cannot support the asserted
   lesion/region/time scale.
10. Essential counts, accessions, endpoints, model artifacts or software/reference versions would
    have to be guessed. Report `Author input needed` instead.

## Evidence-to-block index

| Block | Evidence IDs |
|---|---|
| Question/estimand | `BK06 BK12 BK19 BK20 BK21 BK32` |
| Feature generation | `BK01 BK02 BK07 BK09 BK13` |
| Pre-analytic/QC | `BK03 BK08 BK09 BK13` |
| DE/normalization/power | `BK06 BK08 BK12 BK13` |
| Isoform/splicing/long-read | `BK03 BK04 BK05 BK10 BK11 BK31` |
| Pathway/signature/network | `BK21 BK24 BK25 BK28 BK29 BK30 BK31 BK33` |
| Composition/deconvolution | `BK14 BK15 BK16 BK17 BK18 BK22 BK23 BK26` |
| Clinical evidence | `BK09 BK20 BK21 BK24 BK27 BK32` |
| Optional multimodal/radiotranscriptomics (`study_scope == imaging-mechanism`) | `BK13 BK18 BK19 BK33` |
| Validation/reproducibility | `BK02 BK03 BK12 BK13 BK16 BK17 BK19 BK20 BK21 BK23 BK24 BK25 BK26 BK27 BK28 BK32 BK33` |

Use the [companion TSV](bulk-rna-literature-map-2024-2026.tsv) for the concrete study content,
decision changed, constraints, writing
requirement, DOI/PMID, and screening-date JIF audit. Do not add a paper to this playbook merely
because it mentions bulk RNA-seq; it must change a decision or boundary.
