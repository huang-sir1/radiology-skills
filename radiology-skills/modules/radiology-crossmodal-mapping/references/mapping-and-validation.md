# Mapping and Validation

Use this reference after link correspondence, cohort completeness, and the verified common unit are
fixed from provenance metadata. Choose the simplest defensible method, then validate the entire
fitted mapping process.

## Method selection

| Method | Appropriate use | Main requirements | Main failure modes |
|---|---|---|---|
| **Pseudobulk** | Aggregate single-cell expression or cell-state counts to patient, lesion, specimen, or region | Enough independent units; prespecified aggregation; library-size and composition handling | Pseudoreplication, loss of rare/spatial states, batch or cell-count confounding |
| **Deconvolution** | Estimate cell-state proportions or expression from bulk/spatial mixtures and link them to imaging | Relevant, frozen reference; identifiable cell states; held-out evaluation | Reference mismatch, collinearity, batch effects, inferred proportions treated as measured cells |
| **Label transfer** | Transfer labels within omics, or across imaging and omics only through a paired bridge, shared measured features, or independently validated cross-modal mapper | Compatible feature space/bridge; training-only anchors; uncertainty/rejection rule | Unsupported direct cross-modal transfer, forced labels, atlas leakage, domain shift, circular validation |
| **Canonical correlation** | Find correlated low-dimensional structure between paired or carefully aligned modality blocks | Adequate independent paired units; regularization; nested component selection | High-dimensional overfit, unstable axes, confounding-driven correlation |
| **Contrastive mapping** | Learn shared embeddings from positive and negative cross-modal pairs | Defensible pair definitions; hard-negative policy; enough independent patients; external testing | False positives/negatives, patient/site shortcuts, test pairs used in representation learning |
| **Graph alignment** | Match spatial neighborhoods, habitats, or cell-state graphs across modalities | Meaningful nodes/edges and comparable topology; training-only graph construction | Arbitrary graph definitions, topology driven by density/batch, non-identifiability |
| **Habitat linkage** | Associate imaging habitats with cellular composition or spatial neighborhoods | Stable habitats; traceable specimen/region link; registration uncertainty; nested analysis | Habitats learned on all data, ecological fallacy, scale mismatch, post hoc region selection |

Use unsupervised canonical correlation, contrastive, or graph methods as exploratory unless
predefined targets and held-out evaluation justify a confirmatory role. A visually convincing
embedding is not validation.

## Label-transfer boundary

Ordinary label transfer assumes a meaningful shared feature space. Imaging pixels or embeddings and
omics measurements do not provide one merely because they describe the same disease. Cross-modal
imaging-to-omics label transfer requires at least one of:

- a paired bridge measured in both modalities at verified common units;
- genuinely shared measured features with established semantics;
- a cross-modal mapper developed independently and validated for the target modality, anatomy,
  population, and label set.

Otherwise transfer labels only within the omics domain, aggregate the resulting cell states at the
verified unit, and test their imaging association separately with held-out validation. Report such
labels as inferred, not directly measured.

## Leakage-safe pipeline

1. Before splitting, use only identity, provenance, modality availability, acquisition dates,
   treatment metadata, and prespecified eligibility rules to audit the hierarchy, classify links,
   and freeze unresolved records. Do not inspect outcomes, expression, cell states, imaging
   phenotypes, apparent biological correspondence, or performance.
2. Freeze the eligible cohort, then define final test patients and, when applicable, held-out
   centers. Keep all lesions, specimens, sections, regions, spots, cells, and repeated time points from one
   patient in the same partition.
3. Any correspondence refinement using image content, omics content, biology, outcomes, or learned
   similarity is a fitted procedure: develop it in training and apply it unchanged to validation.
4. In resampling, fit preprocessing, normalization, batch adjustment, feature filtering, habitat
   discovery, pseudobulk choices, deconvolution tuning, anchors, label transfer, dimensionality
   reduction, canonical components, contrastive encoders, graph construction, thresholding,
   hyperparameters, and calibration on training data only.
5. If a public atlas, cross-modal mapper, or pretrained reference is used, freeze its version and
   audit exact patient overlap with its construction, training, and pretraining data. Independent
   evaluation requires excluding every overlapping patient from the test set or using an
   atlas/model rebuilt without those patients. If absence of overlap cannot be verified or overlap
   cannot be excluded, label the evaluation **non-independent/model-exposed** and do not claim
   independent or external validation. Adaptation to study data is a fitted step.
6. Use grouped or nested resampling for tuning. Keep the final test set untouched until the
   pipeline and analysis plan are locked.
7. Treat center as a transportability unit when claiming multi-center generalization. Prefer
   held-out-center or external-center validation over random mixed-center splits.
8. Report unique patients and centers per split in addition to lesions, regions, or cells.

Do not use batch correction or harmonization to erase the held-out-center identity before
evaluation. Learn any transform without access to test outcomes and describe what information from
the target center is permitted.

## Baselines

Compare the cross-modal method against simple alternatives that expose shortcuts:

- demographic, clinical, anatomy, lesion-size, scanner/site, and assay-batch baselines;
- unimodal imaging-only and cellular-only baselines when prediction is claimed;
- patient- or lesion-level aggregation without complex alignment;
- majority-class, prevalence, nearest-centroid, or linear regularized models as appropriate;
- a mapping that uses only acquisition/site metadata.

An advanced mapping is informative only if it adds stable value beyond these baselines under the
same partitions and tuning budget.

## Negative controls

### Permutation controls

- Permute cross-modal links at the patient or shared-unit level, preserving center, disease,
  anatomy, time-point, and batch strata where needed.
- Re-run the entire fitted pipeline, not only the final statistical test.
- For contrastive mapping, compare the specified positive/negative policy with shuffled pair
  labels and site-matched negatives.

### Negative-region controls

- Test contralateral, distant, non-sampled, histologically incompatible, or otherwise prespecified
  regions that should not carry the proposed local signal.
- Match negative regions for size, acquisition quality, anatomy, and center when possible.
- Do not select negative regions after seeing the results.

### Null-feature controls

- Add noise, permuted, housekeeping, technical-QC, or biologically implausible features suitable
  for the assay and estimand.
- Test whether scanner, site, slide, batch, sequencing depth, cell count, or tissue area predicts
  the embedding or mapped state.
- Use synthetic nulls only when their generation does not leak the target structure.

A failed negative control is evidence against the claimed mapping until the source is explained
and the corrected analysis is independently re-evaluated.

## Sensitivity analyses

Predefine the variants most likely to change the conclusion:

- direct links only versus inclusion of weak links; fully versus partially paired analysis sets;
- same-day or treatment-free pairs versus wider temporal windows;
- patient-, lesion-, specimen-, section-, and region-level aggregation;
- alternative registration landmarks, transforms, spatial tolerances, and exclusion thresholds;
- alternate habitat numbers, clustering seeds, segmentation rules, and boundary definitions;
- alternate cell-state references, annotation granularity, deconvolution tools, or rejection
  thresholds;
- batch/site adjustment choices and leave-one-center-out analysis;
- covariate adjustment for anatomy, lesion size, stage, treatment, purity, cell count, and assay QC;
- removal of ambiguous links, low-quality regions, one lesion at a time, or influential centers;
- reasonable preprocessing, normalization, feature, graph, and embedding specifications.

Report direction, effect size, uncertainty, and validation performance across variants. Do not
summarize sensitivity as “robust” solely because nominal significance remains.

## External validation

External validation requires patients not used for method development and should preferably add a
new center, scanner/protocol distribution, assay batch/platform, or collection period. Freeze:

- mapping hierarchy, link-status rules, and cohort-completeness rules;
- phenotype/habitat definition and segmentation procedure;
- cellular-state vocabulary or reference atlas version;
- preprocessing, transforms, model parameters, thresholds, and aggregation;
- primary metric and success criterion.

Confirm that no external-test patient appears in the atlas, mapper-training data, or model
pretraining data. Exclude exact overlaps from the external test or use a rebuilt/retrained
reference without them; otherwise report the evaluation as non-independent/model-exposed.

Report correspondence failures and exclusions in the external cohort. Re-training or redefining
the target on external data is model updating and must be labelled and followed by a further
evaluation set.

## Orthogonal biological validation

Choose evidence that does not merely repeat the same computational assumptions:

- IHC for cell-type abundance or directly registered multiplex immunofluorescence for
  regional co-localization;
- RNA or DNA in situ hybridization for spatial expression;
- pathology review or quantitative histomorphometry;
- a separately measured spatial-transcriptomic or single-cell assay;
- targeted flow cytometry, proteomics, or experimental perturbation when biologically appropriate.

Predefine markers, regions, scoring, blinding, and concordance criteria. Use orthogonal evidence to
corroborate a specific association; it does not automatically establish causality or generalize
beyond the validated population and shared unit.

## Minimum reporting

Report the hierarchy and mapping-unit table; link-status and cohort-completeness counts; spatial and temporal tolerances;
treatment intervals; unique patients, centers, lesions, specimens, sections, regions, and cells;
method assumptions; every fitted train-only step; partition provenance; negative controls;
sensitivity analyses; external and orthogonal validation; failed mappings; uncertainty; software,
reference-atlas, and model versions; and claim wording tied to link status, cohort completeness, and
the verified common unit.
