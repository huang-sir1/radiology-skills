# Radiomics–mechanism bridge: review and advisory workflow

Use this reference when the task asks what a radiomic feature, deep imaging embedding, imaging
habitat, delta-radiomic change, or radiology model may mean biologically. It connects imaging to
bulk RNA, single-cell RNA, spatial transcriptomics, pathology, functional experiments, and
clinical evidence. It is not a dictionary that assigns a pathway to a feature.

The skill has two equal duties:

- **Review:** determine whether an existing design, result, figure, manuscript, or mechanistic
  claim is defensible.
- **Advise:** help a learner turn an imaging observation into several testable biological
  hypotheses, understand the trade-offs between assays, and choose an executable next step.

Use the same evidence rules in both modes. Advice may be imaginative, but it must remain explicit
hypothesis generation until the relevant bridge has been measured and validated.

## The central rule: an imaging phenotype has no automatic biological meaning

A radiomic feature, deep embedding, attention map, cluster, or habitat is a **derived numerical
representation of an image**. It does not acquire biological semantics because its name sounds
biological, because a heat map overlaps a lesion, or because an enrichment analysis returns a
recognisable pathway.

Do not silently convert common associations into facts:

- texture is not automatically intratumour heterogeneity;
- enhancement is not automatically angiogenesis;
- low ADC is not automatically high cellularity;
- peritumoural signal is not automatically invasion;
- high FDG uptake is not automatically tumour-cell glycolysis;
- a radiomic habitat is not automatically a histological compartment;
- a deep embedding or attention region is not automatically interpretable tissue biology;
- longitudinal feature change is not automatically treatment response.

Each is a starting observation that may have several biological, physical, acquisition-related,
and analytical explanations. Generate those alternatives before selecting a molecular assay or
writing a mechanism.

## Two directions must not be confused

The **investigative evidence path** often starts from the image:

```text
image acquisition -> derived phenotype -> candidate tissue structure
-> candidate cell composition/state -> molecular program
-> functional or perturbational support -> clinical relevance
```

The **biological data-generating direction** usually runs the other way:

```text
molecular and cellular processes -> tissue composition/architecture/physiology
-> interaction with the imaging contrast and acquisition system
-> voxel signal -> derived feature, embedding, or habitat
```

Therefore, do not write that an imaging feature “drives” a pathway. Imaging and molecular readouts
are commonly two consequences of latent tissue biology, and both may also be affected by treatment,
sampling, acquisition, and patient factors. A defensible mechanism must explain both the physical
image contrast and the biological process that could generate it.

For every link, label the evidence as **measured**, **derived**, **estimated**, **associated**,
**predicted**, or **perturbed**. Agreement between two estimated layers is not equivalent to two
independent measurements.

## Review mode and advice mode

| Mode | Starting material | Required reasoning | Required output |
|---|---|---|---|
| Review | protocol, data, analysis, figures, manuscript, reviewer response | reconstruct the claimed bridge; locate broken links, confounding, circularity, scale mismatch, and overclaim | severity-ranked findings, `PASS / CONDITIONAL / STOP`, claim ceiling, exact repairs and writing changes |
| Advice | research idea, preliminary association, available datasets, or a learner's question | define the image phenotype; generate competing mechanisms; match the uncertainty to the right assay; compare feasible designs | mechanism-bridge canvas, ranked hypothesis portfolio, minimum/standard/enhanced plan, and the next executable action |
| Combined | an incomplete study that also needs revision | audit what exists first, then design only the missing bridge | preserved valid findings, blocked claims, repair plan, and revised narrative |

### Teach rather than merely grade

For every important criticism or recommendation, include four elements:

1. **Principle:** explain in plain language why the issue matters.
2. **Consequence:** state which conclusion becomes biased, ambiguous, or unsupported.
3. **Choice and trade-off:** compare at least two reasonable routes when they exist.
4. **Next action:** give the smallest useful analysis, metadata request, or experiment the learner
   can perform now.

Do not say only “bulk is insufficient,” “add spatial,” or “validate experimentally.” For example:

> Bulk RNA can test whether the imaging phenotype covaries with a patient-level immune program,
> but it cannot determine whether the signal comes from tumour cells or infiltrating immune cells.
> If the immediate aim is cellular source, use patient-aware scRNA pseudobulk or targeted
> multiplex IHC; if the aim is location relative to an imaging habitat, use registered spatial
> transcriptomics or region-matched pathology. With current bulk data, retain a tumour-level
> association claim and run a cell-composition sensitivity analysis first.

## Input contract

Do not infer missing provenance from filenames, figure labels, or conventional practice. Build an
input contract and mark fields as `known`, `missing`, or `not applicable`.

| Domain | Required fields | Why it changes the bridge |
|---|---|---|
| Intended decision | biological question, clinical endpoint, intended claim, discovery versus validation | determines whether association, prediction, localization, or causality is required |
| Cohort | patients, lesions, repeated scans, tissue samples, sites, inclusion/exclusion, matched counts at every intersection | establishes the independent unit and effective sample size |
| Imaging | modality, sequence/tracer, acquisition timing, reconstruction, scanner/vendor/field strength, contrast phase, preprocessing, registration | defines the physical source and technical variation of the signal |
| Phenotype | exact feature/embedding/habitat, ROI, units/direction, extraction software/version, feature selection, model layer/pooling, clustering parameters | prevents semantic interpretation of an undefined or unstable number |
| Segmentation | anatomical target, included/excluded compartments, manual/automatic method, reader variability, perturbation/stability results | determines what tissue contributes to the phenotype |
| Molecular/pathology | assay, raw/processed layer, tissue source, block/section, cellular resolution, preprocessing, batch, QC, annotations | defines what biology is measured versus inferred |
| Mapping | patient, lesion, biopsy/block/section, habitat/region, coordinates, registration chain, uncertainty | determines whether a regional mechanism is identifiable |
| Time and treatment | scan date, biopsy/surgery date, interval, treatment/steroids/intervention between them, longitudinal schedule | distinguishes contemporaneous biology from treatment or temporal drift |
| Analysis | estimand, covariates, split strategy, feature selection, multiplicity, missingness, baselines, external validation | detects leakage, pseudoreplication, and false discovery |
| Writing | target section, current wording, figure/table source, requested claim strength | allows exact revision without inventing evidence |

If the task supplies only a figure or paragraph, reconstruct this contract as far as possible and
label every unverified assumption. Missing information may lower the claim, but it does not justify
inventing a workflow that was never performed.

## Mechanism Bridge Canvas

Complete one canvas for each headline image–biology claim. Do not combine unrelated image
phenotypes or endpoints into one story.

Use the reusable [mechanism bridge canvas](../templates/mechanism-bridge-canvas.md) when the user
needs a fillable design, mentoring or review artifact.

| Canvas field | Required content |
|---|---|
| 1. Decision and claim target | What decision will this evidence support, and is the target descriptive, associative, predictive, or causal? |
| 2. Image phenotype | Exact feature, embedding, habitat, or temporal change; ROI; direction; reproducibility; measured/derived status |
| 3. Physical contrast bridge | What image physics or tracer process could generate the signal: attenuation, relaxation, diffusion, perfusion, permeability, metabolism, or morphology? |
| 4. Tissue-scale bridge | Candidate architecture: viable tumour, necrosis, fibrosis, oedema, vessels, stroma, immune aggregates, invasive front, or mixed compartments |
| 5. Cell bridge | Candidate cell types, proportions, states, interactions, and whether they are measured, deconvolved, mapped, or predicted |
| 6. Molecular bridge | Candidate gene programs, isoforms, pathways, regulatory states, or proteins; data layer and inferential unit |
| 7. Functional bridge | Phenotype or intervention expected if the mechanism is real; perturbation, rescue, organoid, animal, or orthogonal assay |
| 8. Clinical bridge | Outcome, treatment interaction, decision context, validation population, and utility threshold |
| 9. Competing explanations | At least two biological hypotheses plus one technical/sampling explanation |
| 10. Mapping and timing | patient/lesion/region/section link, scale mismatch, date gap, intervening treatment, registration uncertainty |
| 11. Falsifier | Observation that would weaken or reject each leading hypothesis |
| 12. Validation rung | minimum, standard, or enhanced; what claim it permits now |
| 13. Next action | smallest analysis/experiment that best distinguishes the leading explanations |

### Hypothesis portfolio rule

For each image phenotype, generate at minimum:

- `H1`: the most plausible biological explanation;
- `H2`: a biologically distinct explanation that predicts a different observation;
- `H3`: an acquisition, preprocessing, segmentation, volume, site, or sampling explanation;
- one **discriminating test** for H1 versus H2/H3;
- one **negative control** or falsifier.

Rank hypotheses using `biological plausibility | compatibility with image physics | spatial and
temporal match | testability with available data | confounding risk | clinical relevance`. Novelty
alone must not outrank identifiability. If several hypotheses remain compatible with the data,
report them rather than selecting the most attractive story.

## Stage-gated bridge

Use `PASS`, `CONDITIONAL`, or `STOP` at each gate. `CONDITIONAL` allows analysis only with bounded
language and the named sensitivity or validation. `STOP` blocks the headline claim, not every valid
subsidiary result. The overall verdict inherits the most restrictive claim-determining gate.

| Gate | Question and why | PASS | CONDITIONAL | STOP | Help after the verdict |
|---|---|---|---|---|---|
| MB0 — task and estimand | What exactly is being explained or predicted? | phenotype, population, endpoint, unit, time, and claim are explicit | exploratory target can be bounded | no coherent phenotype, contrast, or endpoint | rewrite the question and define the estimand |
| MB1 — image phenotype validity | Is the imaging variable technically reproducible and biologically addressable? | acquisition, ROI, extraction, stability, and train-only derivation are traceable | limited stability or protocol heterogeneity is sensitivity-tested | outcome leakage, unreconstructable feature, dominant scanner/site signal, or failed segmentation stability | create feature passport; repeat segmentation/protocol/site/volume analyses |
| MB2 — sample, scale, and time | Does tissue plausibly correspond to the claimed image region and biological state? | matched patient/lesion/region and acceptable interval/registration | patient-level match supports only tumour-level claims | wrong lesion/patient, unknown intervening treatment central to the endpoint, or irrecoverable mapping | create mapping table; lower to patient-level; request coordinates or matched tissue |
| MB3 — competing mechanisms | Is there a testable portfolio rather than one post-hoc story? | at least two biological and one technical hypothesis with distinct predictions | plausible hypotheses exist but available data cannot distinguish them | a single pathway is chosen only because it was significant in the same discovery data | build and rank the canvas; define falsifiers and negative controls |
| MB4 — assay and analysis fitness | Does the chosen molecular/pathology assay answer the unresolved link at the correct unit? | modality, data layer, model, covariates, multiplicity, and patient-level inference match the question | indirect assay can support a weaker claim | cell/spot pseudoreplication, complete batch–biology confounding, circular signature selection, or wrong data layer | route to bulk/scRNA/spatial/pathology playbook and propose the smallest repair |
| MB5 — cross-modal triangulation | Do independent modalities support the same statement at compatible scales? | concordant measured evidence with explicit provenance and uncertainty | indirect, deconvolved, predicted, or section-limited support is labelled | two generated layers are presented as independent validation, or scale mismatch is hidden | make concordance/discordance table and test alternatives |
| MB6 — functional or temporal support | Does the evidence show function or only coexistence? | intervention/perturbation, temporal ordering, dose response, or rescue supports the stated link | orthogonal association or longitudinal observation supports plausibility only | causal mechanism is claimed from cross-sectional association or mediation alone | specify perturbation, rescue, longitudinal sampling, or orthogonal assay |
| MB7 — clinical relevance | Is the bridge valid in the target clinical population and workflow? | locked result generalises externally; treatment-benefit/effect-modification prediction uses a comparator and interaction; utility is evaluated when claimed | outcome/response prediction under one observed regimen is labelled as such and internally validated | differential treatment benefit, “non-invasive biopsy,” treatment selection, replacement, or utility claim lacks its required comparator/external/prospective evidence | define external cohort, calibration, treatment comparator when benefit is intended, and clinical endpoint |
| MB8 — writing fidelity | Does every sentence preserve measurement and evidence status? | title, Methods, Results, legends, and Discussion agree with the gate record | overstatement is repairable without new analysis | text contradicts data provenance or reports predicted/generated values as measured | provide exact replacement text and claim-grade annotations |

### Immediate STOP rules for mechanistic headlines

Stop or downgrade the mechanistic headline when any of these remains unresolved:

- the molecular sample is not traceably linked to the imaged patient or lesion;
- the image feature is selected using the same molecular endpoint and then “validated” against it
  without a held-out analysis;
- cells, spots, tiles, lesions, or serial scans are treated as independent patients;
- tumour volume, scanner/site, treatment, or acquisition phase is completely confounded with the
  molecular state;
- a pathway enrichment, deconvolved fraction, mapped spatial state, saliency map, or generated
  expression layer is presented as direct mechanistic measurement;
- one biopsy or tissue section is used to make a whole-lesion spatial mechanism claim without a
  sampling argument;
- a deep model predicts a molecular label but no analysis establishes what information it used;
- causal terms are used without functional or perturbational evidence appropriate to the claim.

## Generate mechanisms by imaging phenotype family

The following are hypothesis menus, not semantic labels. Select candidates that are compatible
with the actual modality, sequence, ROI, disease, and treatment context.

| Imaging phenotype family | Competing biological hypotheses | Technical or sampling alternatives | Discriminating evidence or next experiment |
|---|---|---|---|
| Size, shape, irregularity, margin | proliferative burden; infiltrative growth; stromal/ECM remodelling; pressure constrained by anatomy | segmentation convention; partial-volume effect; detection delay; oedema included in ROI | volume-adjusted and unadjusted models; invasive-front pathology; ECM markers; spatial sampling of core versus margin |
| Intensity, attenuation, T1/T2 signal | water/fat/blood/mineral content; viable versus necrotic tissue; fibrosis or proteinaceous material | scanner calibration; phase/sequence choice; bias field; reconstruction; windowing | phantom/protocol stability; compartment-specific pathology; quantitative mapping rather than relative signal alone |
| Texture, entropy, coarseness, wavelets | mixture of viable, necrotic, stromal, vascular, and immune compartments; spatially varying cell states; clonal architecture | feature dependence on volume, voxel size, discretisation, noise, resampling, and segmentation | stability across resampling/binning and volume matching; multi-region pathology or spatial omics; compare spatial heterogeneity rather than bulk mean alone |
| Enhancement, perfusion, permeability | blood volume/flow; vessel density and maturity; endothelial activation; permeability; inflammation | contrast timing/dose; cardiac/renal function; motion; necrosis; acquisition phase | quantitative DCE/perfusion parameters; CD31/endomucin plus vessel morphology; permeability markers; regional spatial validation |
| Diffusion/ADC | cellular packing; extracellular space; ECM/fibrosis; oedema; necrosis; viscosity | distortion, susceptibility, b-values, motion, partial volume | nuclei density and ECM quantification; diffusion-model sensitivity; viable-tissue mask; region-matched histology |
| PET uptake or metabolic imaging | tumour-cell glycolysis or receptor expression; immune-cell metabolism; viable burden; hypoxia-linked metabolism | uptake time, blood glucose, injected dose, reconstruction, partial volume, perfusion/delivery | dynamic or kinetic imaging; tumour- versus immune-cell expression by scRNA/IHC; tracer-specific blocking or orthogonal metabolic assay |
| Peritumoural signal or oedema | invasive cells; immune/stromal reaction; vascular/BBB leakage; lymphatic or venous obstruction | steroid exposure; treatment effect; anatomic boundary; ROI dilation choice | distance-to-margin analysis; matched core/interface/periphery sampling; immune/ECM/endothelial pathology; steroid sensitivity analysis |
| Multiparametric habitat | tissue compartments with different perfusion, diffusion, metabolism, hypoxia, necrosis, or immune exclusion | registration error; normalisation choice; cluster number/seed/algorithm; small or unstable habitat | consensus/stability across clustering choices; pre-specified habitat definition; region-targeted biopsy or registered spatial/pathology |
| Deep feature, foundation embedding, attention map | latent morphology, physiology, tissue context, or multi-scale composition that may combine several known phenotypes | site/scanner shortcut; image annotations; cropping/background; pretraining leakage; preprocessing; model calibration | site-prediction probe; ablation and counterfactual tests; external cross-site validation; pathology/spatial correlation; attribution alone is not validation |
| Longitudinal or delta-radiomics | cell death; reduced proliferation; vascular remodelling; immune infiltration; fibrosis; resistance evolution | scanner/protocol drift; changing ROI; interval length; inflammation/pseudoprogression; supportive treatment | paired protocol-matched analysis; segmentation perturbation; untreated/control trajectory; paired tissue or liquid biomarker; response-specific time course |

### How to choose among hypotheses

- If the uncertainty is **which patient-level program differs**, bulk RNA is usually the efficient
  first molecular layer.
- If it is **which cell type or state generates the signal**, use scRNA/snRNA or targeted pathology.
- If it is **where the state lies relative to a margin, habitat, vessel, or niche**, use spatial
  transcriptomics or registered multiplex pathology.
- If it is **whether the program causes the tissue/image phenotype**, use perturbation, rescue, or
  a longitudinal model capable of producing the relevant imaging readout.
- If it is **whether the marker helps a clinical decision**, use a locked independent or prospective
  validation design; more molecular interpretation does not substitute for clinical validation.

## What each evidence layer can and cannot solve

| Layer | What it can resolve | What it cannot establish by itself | Critical constraint | Best use in the bridge |
|---|---|---|---|---|
| Imaging/radiomics | whole-lesion morphology, physiology, topology, longitudinal change, regional habitats | cell identity, pathway activity, microscopic co-localisation, molecular causality | scanner/protocol, segmentation, volume, registration, model shortcuts | define the reproducible macroscopic phenotype to explain |
| Bulk RNA | patient-level expression, pathway, isoform/splicing, subtype, prognosis or treatment interaction with suitable design | cell source, native spatial position, cell-intrinsic versus composition effect | tissue purity, reference choice, preanalytics, sample-level replication | identify cohort-scale programs and clinically anchored associations |
| scRNA/snRNA | cell types, states, within-tissue heterogeneity, patient-aware cell-type programs, observed perturbation effects | native position after dissociation; whole-lesion representativeness; DNA truth from RNA-CNV | donor replication, dissociation/nucleus bias, annotation, integration, pseudobulk | identify candidate cellular sources and state-specific programs |
| Spatial transcriptomics | domains, gradients, neighbourhoods, cell/spot localisation, relation to histology | automatic whole-tumour generalisation; direct measurement when deconvolution/mapping is used; causality | platform resolution, segmentation, reference dependence, section sampling, registration | test whether candidate cells/programs occupy the predicted imaging region |
| Pathology/IHC/multiplex IF | tissue architecture, cell morphology, targeted proteins, cell density, vessel/ECM/immune context | unbiased transcriptome-wide discovery; complete pathway activity; whole-lesion coverage from one slide | antibody specificity, scoring, section selection, spatial mapping | provide an interpretable physical and cellular bridge close to the imaging phenotype |
| Functional/perturbation model | effect of manipulating a candidate program; dose, time, rescue, and causal direction | direct clinical generalisability or faithful imaging phenotype unless the model reproduces acquisition and tissue scale | model relevance, off-target effects, endpoint fidelity, replication | raise a plausible bridge toward mechanistic evidence |

Do not ask one modality to answer another modality's question. Use the detailed, literature-derived
routes when needed:

- [bulk-rna-research-guidance.md](bulk-rna-research-guidance.md) for feature generation,
  preanalytics, differential expression, pathways, splicing, deconvolution, and clinical signatures;
- [single-cell-research-guidance.md](single-cell-research-guidance.md) for data layers, QC,
  integration, annotation, pseudobulk, trajectories, GRN/communication, and perturbation;
- [spatial-transcriptomics-research-guidance.md](spatial-transcriptomics-research-guidance.md) for
  platform/resolution, segmentation, spatial estimands, mapping, neighbourhoods, H&E prediction,
  longitudinal/perturbational space, and spatial clones.

## Constraint ledger: audit before biological storytelling

| Constraint | Why it matters | Required review | Decision and repair |
|---|---|---|---|
| Patient/lesion/sample mapping | a patient match is not necessarily a lesion or region match | verify patient, lesion, tissue source, block/section, and mapping level | unknown region permits patient-level association only; wrong lesion is `STOP` for lesion mechanism |
| Spatial scale | millimetre voxels average many microscopic compartments | compare voxel/ROI/habitat scale with biopsy/section/cell scale | aggregate or sample at compatible scales; do not claim micron co-localisation from coarse registration |
| Tissue sampling | a biopsy or section may miss the imaging phenotype | record sampled region and representativeness; inspect viable/necrotic/interface content | use multi-region or targeted sampling; otherwise bound to the sampled tissue |
| Time interval | biology can change between scan and tissue | report dates, interval distribution, and time-window sensitivity | predefine window; adjust/stratify when defensible; downgrade if contemporaneity is weak |
| Intervening treatment | treatment can alter both imaging and molecular state | list therapy, radiation, steroids, biopsy, and supportive treatment between events | analyse pre/post states separately; do not treat a mediator as a routine nuisance covariate without defining the estimand |
| Scanner/site/protocol | image features may encode acquisition rather than biology | site prediction, protocol balance, cross-site stability, and acquisition-adjusted analysis | harmonise within training only and preserve biology; complete confounding cannot be repaired computationally |
| Molecular batch/site | sequencing and imaging batches can align and mimic cross-modal biology | joint batch table, batch-only models, PCA/embedding diagnostics | model separately or sensitivity-test; stop if batch and biology are inseparable |
| Tumour volume | size affects texture, shape, partial volume, necrosis, and outcome | correlation with volume; adjusted and unadjusted estimands; volume-matched sensitivity | report both when volume may be real biology; residualising can remove meaningful signal, so explain the target |
| Segmentation | boundaries determine which compartments generate features | inter/intra-reader stability, automatic-model errors, ROI variants, perturbation | retain stable features; compare whole/viable/core/margin ROIs; propagate instability into claim grade |
| Registration | habitat-to-tissue linkage can fail at several transformations | sequence-to-sequence, image-to-gross tissue, histology-to-section alignment and uncertainty | report each transform; use region-level rather than point-level language when uncertainty is large |
| Multiple lesions/scans/samples | repeated observations inflate apparent n and can mix biological levels | identify hierarchy and patient-level split; use multilevel models/aggregation | never split lesions, slices, cells, or scans from one patient across train/test |
| Missing modalities | complete-case fusion can select a non-representative subgroup | compare included/excluded patients and missingness by site/outcome | use a justified missingness strategy; report matched n at every analysis, not only total cohort n |

Harmonisation, covariate adjustment, and residualisation are not automatic repairs. They may remove
real biological variation or create optimistic validation if fitted before the split. State the
estimand, fit data-dependent operations within training data, and show whether the conclusion is
stable under plausible alternative specifications.

## Validation ladder

Choose the rung from the intended claim, not from the prestige of the desired journal. A rigorous
discovery study can stop at the minimum rung if it uses appropriately bounded language.

### Minimum: credible hypothesis-generating bridge

Required:

- reproducible and fully specified image phenotype;
- independent patient-level inference and leakage-safe analysis;
- traceable patient/lesion/tissue mapping and timing;
- scanner/site, segmentation, volume, treatment, batch, and multiplicity checks;
- one molecular or pathology association at an appropriate scale, with measured versus inferred
  status explicit;
- competing explanations and at least one feasible falsifier;
- discovery/association wording.

Supports: a radiogenomic association and a testable mechanistic hypothesis. It does not support
causality, a non-invasive biopsy claim, or clinical replacement.

### Standard: triangulated biological explanation

Add:

- independent, temporal, or cross-site replication of the locked image–biology result;
- orthogonal evidence that resolves the critical missing link, such as patient-aware scRNA,
  spatial transcriptomics, registered pathology, protein assay, or region-matched sampling;
- concordance/discordance analysis across modalities rather than only significant overlap;
- sensitivity to cell composition, tissue compartment, platform, and analytic choices;
- a prespecified negative control and a result that distinguishes at least two leading hypotheses.

Supports: a replicated association with cellular, spatial, or pathological evidence **consistent
with** a proposed biological explanation. It still may not establish mechanism.

### Enhanced: mechanistic and clinically transportable bridge

Add as required by the claim:

- perturbation of the candidate program with dose/time response and, where feasible, rescue;
- an experimental model that reproduces the relevant tissue property and imaging phenotype;
- longitudinal evidence showing the predicted ordering of molecular, tissue, and imaging changes;
- spatially targeted and independently replicated sampling;
- external multicentre/prospective validation, calibration, subgroup/site analysis, and a clinical
  comparator if utility or treatment selection is claimed.

Supports: stronger mechanistic or clinical language only for the links directly demonstrated.
Perturbing a pathway in cells does not by itself prove that a clinical radiomic feature is a valid
surrogate; the image phenotype must also change in a relevant model and generalise to patients.

## Alternative explanations and discriminating tests

Do not merely list limitations. Convert the most consequential alternatives into tests.

| Apparent finding | Competing explanation | Discriminating analysis or experiment | Interpretation after test |
|---|---|---|---|
| Texture associates with a hypoxia score | volume/necrosis or scanner noise drives both | viable-tissue mask; volume-matched and scanner-stratified analysis; spatial hypoxia markers in high- versus low-texture regions | only regionally concordant, technically stable evidence supports a hypoxia-consistent interpretation |
| Enhancement associates with angiogenic genes | contrast timing/permeability/inflammation rather than vessel formation | quantitative perfusion/permeability; vessel density/maturity IHC; inflammatory-cell assessment | separate vascular density, flow, permeability, and inflammation rather than naming all “angiogenesis” |
| Bulk immune program associates with an image habitat | changing immune fraction, not tumour-cell program | deconvolution sensitivity; cell-type pseudobulk; multiplex IHC or spatial localisation | composition explains a tumour-level association unless a cell-intrinsic effect remains |
| Deep embedding predicts molecular subtype | model uses site, scanner, annotations, or background | patient/site-stratified external validation; site probe; crop/background ablation; pretraining-overlap audit | predictive performance without shortcut exclusion does not create biological meaning |
| Habitat-specific pathway is enriched | cluster definition and tissue sampling were chosen post hoc | cluster stability across seeds/k/algorithms; frozen habitat definition; targeted independent samples | unstable habitats remain descriptive computational partitions |
| Imaging feature statistically mediates molecular state and outcome | unmeasured confounding or reverse temporal order | longitudinal sampling, negative controls, causal graph, sensitivity to mediator assumptions, intervention | cross-sectional mediation remains model-dependent association, not mechanism |
| Delta feature changes after therapy | acquisition/segmentation drift or inflammatory pseudoprogression | paired protocol QC, segmentation perturbation, untreated/control trajectory, paired biomarkers | label as response-consistent only if technical drift and plausible alternatives are addressed |
| Peritumoural feature predicts recurrence | feature captures size, anatomy, treatment field, or oedema | size/anatomy/treatment-adjusted model; distance-resolved pathology; external site validation | retain prognostic association unless invasive biology is spatially demonstrated |

Prefer experiments that make the hypotheses predict **different outcomes**. Repeating the same
correlation with another algorithm is robustness testing, not a discriminating mechanistic test.

## Route by available data

Start with the strongest defensible output from what exists, then offer the smallest addition that
would change the claim grade.

| Available data | What the skill can do now | Claim ceiling | High-yield next addition |
|---|---|---|---|
| Imaging only | validate feature/embedding/habitat; describe physical contrast; generate and rank mechanisms; test scanner/volume/segmentation alternatives | reproducible imaging phenotype and biological hypotheses only | targeted pathology or an existing matched bulk cohort selected to distinguish the leading hypotheses |
| Imaging + bulk RNA | test patient-level programs, isoforms, composition estimates, prognosis or treatment interaction; link cohort-scale signals | imaging–transcriptomic association; cellular source and location unresolved | deconvolution sensitivity plus scRNA/pathology for source or spatial data for location |
| Imaging + scRNA/snRNA | identify candidate cell types/states and patient-aware programs; test composition versus state | cellularly informed association; spatial relation unresolved unless sampling coordinates exist | region-matched pathology/spatial data and larger donor-level replication |
| Imaging + spatial transcriptomics | test whether programs, cells, gradients, or niches localise to imaging regions through a documented registration chain | spatially supported association within sampled sections | independent sections/patients, orthogonal protein/pathology, and segmentation/registration sensitivity |
| Imaging + pathology | connect image phenotype to tissue structure, cellular density, vessels, necrosis, ECM, or targeted proteins; route the execution through the radiopathology playbook | tissue/cellular concordance for the assayed markers; not transcriptome-wide mechanism | bulk/scRNA/spatial chosen according to program, source, or location uncertainty |
| Imaging + longitudinal sampling | test temporal concordance and within-patient change; distinguish baseline phenotype from response trajectory | temporal association; causality still vulnerable to treatment and time-varying confounding | paired molecular/pathology samples, appropriate control trajectory, and pre-specified time windows |
| Imaging + perturbation/function | test whether manipulating a program changes cells/tissue and, in a relevant model, the image phenotype | mechanistic support for demonstrated links | rescue, independent perturbation, clinically faithful imaging, and external/prospective validation |

When a learner lacks the ideal modality, do not terminate with “insufficient data.” Offer three
tiers: `do now` using existing data, `next` using the smallest informative addition, and `ideal`
for the claim they ultimately want.

## Writing contract

Writing must preserve the full evidence chain. Never let the abstract or figure legend claim more
than the Methods and validation support.

### Title

- Name the imaging and biological layers actually studied.
- Use “association,” “radiogenomic correlate,” or “linked cellular/spatial evidence” for
  observational work.
- Use “mechanism,” “mediates,” “drives,” “non-invasive biopsy,” “predicts treatment benefit,” or
  “surrogate” only when the corresponding causal, interaction, validation, and utility requirements
  are met.
- Do not name a pathway in the title if it emerged only from post-hoc enrichment in the discovery
  cohort.

### Methods

Report enough detail to reconstruct every bridge:

- cohort intersections and independent units for imaging, bulk, scRNA, spatial, pathology, and
  validation analyses;
- imaging acquisition/reconstruction, preprocessing, registration, segmentation, ROI definition,
  feature/embedding/habitat generation, software/version, and stability;
- train/validation/test separation and where harmonisation, feature selection, thresholds, and
  model fitting occurred;
- patient–lesion–tissue–block/section mapping, timing, intervening treatment, and registration
  uncertainty;
- assay-specific QC, data layer, annotations/references, batch, inferential unit, and whether each
  molecular quantity is measured, deconvolved, mapped, imputed, or predicted;
- primary estimand, covariates, volume/site/scanner/treatment handling, multiplicity family,
  missingness, baselines, sensitivity analyses, and validation plan;
- how competing mechanisms and negative controls were defined before interpretation where
  possible.

### Results

Use this order:

1. matched cohort and mapping quality;
2. image phenotype reproducibility and technical sensitivities;
3. primary image–biology effect size with uncertainty and multiplicity correction;
4. donor/patient, site, volume, treatment, segmentation, and batch robustness;
5. cellular/spatial/pathological triangulation, including discordant and null evidence;
6. independent, longitudinal, or perturbational validation;
7. bounded conclusion and claim grade.

Report effect sizes, confidence intervals, adjusted P values, matched patient counts, and direction
consistency. A list of enriched pathways is not a mechanism. “Activation” requires an assay and
design that can support activity; otherwise write “a transcriptomic signature enriched for” or
“expression consistent with.”

### Figure legends

Every legend must state:

- number of independent patients and, separately, lesions/sections/cells/spots;
- ROI/habitat and image feature definition, direction, units, and whether it is derived/predicted;
- molecular data layer and whether values are measured, deconvolved, mapped, imputed, or predicted;
- mapping level and relevant registration or section sampling;
- statistical test, covariates, multiple-testing correction, sidedness, error-bar definition, and
  exact meaning of symbols/colours;
- discovery versus validation status and any repeated-measure structure.

An attention map or saliency overlay must be labelled as model attribution, not as a histological
or mechanistic localisation map.

### Discussion

Build the interpretation link by link:

1. state the reproducible imaging–biology finding and validation status;
2. explain the compatible image physics and tissue architecture;
3. identify cellular and molecular support and its measurement status;
4. discuss at least two biological alternatives and the main technical/sampling alternative;
5. state spatial, temporal, scale, treatment, and cohort limitations;
6. give the highest defensible claim and one experiment that could falsify it;
7. explain clinical relevance without implying replacement or utility not tested.

Example wording for different, non-sequential evidence configurations:

- Too strong: “High CT entropy reflects hypoxia-driven intratumour heterogeneity.”
- Discovery: “CT entropy was associated with a bulk hypoxia-related expression score.”
- Triangulated: “The replicated association and spatial enrichment of hypoxia-related expression
  in high-entropy regions were consistent with, but did not establish, a hypoxia-linked tissue
  phenotype.”
- Perturbation-supported mechanism: stronger language requires perturbation or another design showing that altering the
  candidate process changes the relevant tissue property and image phenotype.

## Reviewer checklist

Return `yes / partial / no / not reported`, the evidence location, consequence, verdict, and repair.

### Scientific and causal frame

- Is the image phenotype and intended biological/clinical claim explicit?
- Is the biological data-generating direction distinguished from the investigative evidence path?
- Are at least two biological explanations and one technical/sampling explanation considered?
- Does the study test a mechanism or merely name one after association?

### Imaging phenotype

- Are acquisition, reconstruction, preprocessing, ROI, segmentation, extraction, and software
  reconstructable?
- Are feature/embedding/habitat stability, scanner/site effects, and volume dependence tested?
- For deep models, are shortcut, pretraining overlap, strong baselines, calibration, and external
  transport assessed?

### Mapping, scale, and time

- Are matched counts reported at patient, lesion, sample, section, and validation levels?
- Does the tissue correspond to the imaged lesion/region and time?
- Are treatment, registration uncertainty, biopsy/section sampling, and scale mismatch explicit?

### Molecular and pathological evidence

- Does the chosen assay answer the claimed program, cell, location, or function question?
- Are raw versus normalised/integrated/imputed/deconvolved/predicted layers distinguished?
- Is the patient the inferential unit, with appropriate handling of cells/spots/repeated samples?
- Are assay QC, batch, references/annotations, multiplicity, and sensitivity analyses adequate?

### Integration and validation

- Is fusion or feature selection leakage-safe and compared with clinical/imaging-only baselines?
- Do modalities provide independent evidence, or are generated estimates being cross-confirmed?
- Are discordant results and negative controls reported?
- Does the validation rung match the headline claim?

### Writing and learner support

- Do Title, Abstract, Results, legends, and Discussion use the same claim strength?
- Are measured, derived, estimated, predicted, and perturbed evidence labelled?
- Does every major criticism include why it matters, alternatives, trade-offs, and an executable
  next step?
- Does the response preserve valid work and show the learner how to improve it rather than only
  rejecting the study?

## Standard output contract

For a mechanism-bridge request, return the following in the user's language unless another format
is requested:

1. **Task and claim target** — one sentence defining the phenotype, population, endpoint, and
   desired evidence level.
2. **Input/data contract** — known, missing, inferred, and blocking fields; matched n at each level.
3. **Gate table** — MB0–MB8 `PASS / CONDITIONAL / STOP`, evidence, consequence, and repair.
4. **Mechanism Bridge Canvas** — physical, tissue, cell, molecular, functional, and clinical links.
5. **Competing hypothesis portfolio** — H1/H2/H3, predictions, falsifiers, and ranking rationale.
6. **Evidence and discordance map** — what imaging, bulk, scRNA, spatial, pathology, longitudinal,
   and perturbation data each support or contradict.
7. **Constraint ledger** — mapping, scale, time, treatment, site/scanner, volume, segmentation,
   batch, sampling, and missingness.
8. **Claim ceiling** — current evidence grade and wording that is permitted or prohibited.
9. **Review findings** — severity, evidence location, why it matters, and exact correction.
10. **Guidance plan** — `do now | next | ideal`, with trade-offs, expected information gain, and
    concrete deliverables.
11. **Writing help** — revised Title/Methods/Results/legend/Discussion text when requested.
12. **One decisive next step** — the smallest feasible analysis or experiment most likely to
    distinguish the leading explanations.

If no raw data are available, do not pretend that execution was audited. Provide a design/manuscript
review, mark assumptions, and state what artifacts would be needed to raise confidence.

## Progressive-disclosure routes

Open only the references needed for the active bridge:

- [radiomics-pipeline.md](radiomics-pipeline.md) for image feature, deep feature, habitat,
  harmonisation, and stability details;
- [sample-to-image-mapping.md](sample-to-image-mapping.md) for patient/lesion/region/section mapping;
- [radiopathology-mechanism-validation.md](radiopathology-mechanism-validation.md) whenever the
  bridge uses H&E, tissue blocks, FFPE, IHC, mIF or WSI and therefore needs prespecified selection,
  preanalytical controls, blinded reading, algorithm QC and patient-aware nested inference;
- [transcriptomics-interpretation-framework.md](transcriptomics-interpretation-framework.md) for
  shared bulk/scRNA/spatial gates, claim grading, and writing rules;
- [research-mentoring-and-idea-development.md](research-mentoring-and-idea-development.md) when the
  user needs topic development, resource-tiered options, learning-oriented feedback or a STOP rescue;
- [biological-validation.md](biological-validation.md) for association-to-mechanism boundaries;
- [deep-radiogenomics-fusion-strategies.md](deep-radiogenomics-fusion-strategies.md) for multimodal
  fusion and baseline choices;
- [reviewer-playbook.md](reviewer-playbook.md) for pre-submission and reviewer-response formatting.

The 100-paper transcriptomics corpus supplies the assay-specific decisions inside the bulk,
single-cell, and spatial playbooks. This bridge determines **which uncertainty each assay should
resolve**, whether the image and tissue evidence can legitimately be connected, and what the learner
should do when the ideal evidence is not yet available.
