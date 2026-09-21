# Cross-scope research failure modes

Use this hit-list for manuscript and pipeline review in all three scopes. Apply only the modality-
specific rows relevant to `active_modalities`; do not penalize a mechanism-only paper for lacking
imaging or an imaging-only paper for lacking molecular assays.

## 1. Broken independent unit and pseudo-replication

- Cells, spots, tiles, sections, ROIs, aliquots or technical replicates are tested as if they were
  independent patients/donors/animals.
- Repeated lesions, time points or blocks are split across train/test or modeled without clustering.
- A very large observation count hides one or a few biological replicates.

**Gate:** identify the biological unit, nesting and effective n. If identity cannot be reconstructed,
the affected inferential claim is `STOP`.

## 2. Leakage, selection and double use

- Feature/gene selection, scaling, harmonization, imputation, normalization parameters, clustering,
  thresholds or hyperparameters use held-out outcomes or validation distribution.
- The same data nominate and confirm a subtype, niche, pathway or imaging habitat without selective-
  inference control or independent confirmation.
- Cells/regions from one donor appear in both training and test folds.

**Gate:** map every learned step to training-only, fixed-before-split or truly external. Rebuild the
pipeline if any outcome-dependent step crosses the evaluation boundary.

## 3. Batch, site or condition confounding

- Scanner/site/protocol, sequencing platform/batch, tissue preservation, dissociation plate, staining
  run or section is aligned with condition/outcome.
- Correction is presented as proof that an unidentifiable contrast was recovered.

**Gate:** show design overlap, batch/condition table, batch-only or site-only models and sensitivity
analyses. Perfect condition–batch confounding is a design failure, not a parameter-tuning problem.

## 4. Multiplicity and researcher degrees of freedom

- Feature×gene, pathway, cell-state, ligand–receptor, neighborhood, radius, time, subgroup or model
  scans are reported with nominal p values.
- Only favorable analyses are shown, or a selected discovery is described as prespecified.

**Gate:** define the complete claim family, correction and selection history; downgrade unreplicated
selected results to exploratory.

## 5. Measurement state is mislabeled

- Deconvolved cell proportions, transferred labels, imputed genes, trajectories, communication scores,
  saliency maps or virtual knockouts are written as direct observations.
- RNA-derived copy-number estimates are called genomic mutations; co-expression is called regulation;
  spatial proximity is called signaling.

**Gate:** independently record `Primary evidence state`, `Modality subtype` and `Claim-link status`.
Generated/predicted values never become measured because they appear in a high-resolution figure.

## 6. Imaging-specific failures — only when imaging is active

- Unreported acquisition/reconstruction, nonstandard feature definitions, unstable segmentation,
  missing discretization/normalization or site-dominated performance.
- Slice, patch, ROI or repeated lesion leakage across patient-level folds.
- Saliency/attention is treated as localization truth or biological mechanism.

**Gate:** acquisition provenance, IBSI/CLEAR-compatible extraction where relevant, segmentation
stability, patient-aware splitting, train-only preprocessing, calibration and external validation.

## 7. Bulk molecular failures — only when bulk is active

- Library strategy, composition/purity, preservation and count transformation are unclear.
- Technical libraries substitute for biological replicates; paired samples are analyzed as independent.
- Composition changes are interpreted as within-cell pathway regulation.

**Gate:** recover donor–specimen–library mapping, assay QC, design matrix and composition sensitivity;
bound cell-source claims unless supported by deconvolution plus orthogonal evidence.

## 8. Single-cell failures — only when single-cell is active

- Cell count replaces donor count; condition is confounded with donor or processing batch.
- Ambient RNA, doublets, dissociation stress and annotation uncertainty are ignored.
- Cluster markers, trajectories, RNA velocity, GRNs or ligand–receptor scores are presented as causal.
- Random-cell splits are used to claim donor/context generalization.

**Gate:** donor-aware QC and inference, annotation evidence, sensitivity to filtering/reference choice,
explicit trajectory/communication assumptions and held-out donor/dataset/perturbation evaluation.

## 9. Spatial/pathology failures — only when spatial or pathology is active

- Spots, cells or tiles replace patient/specimen n; region selection is outcome-informed.
- Segmentation, stain/scanner variation, registration and neighborhood radius uncertainty are omitted.
- One section is generalized to the lesion or organ; proximity is called interaction.

**Gate:** patient–specimen–block–section–region hierarchy, preanalytics, algorithm QC, blinded/locked
region rules, geometry-aware nulls and sensitivity to section/segmentation/radius.

## 10. Imaging–mechanism bridge failures — only for `imaging-mechanism`

- Molecular tissue comes from another lesion, region, treatment state or time window.
- Whole-lesion radiomics is linked to a tiny unregistered tissue fragment without uncertainty bounds.
- A familiar pathway story is chosen without technical/sampling alternatives.

**Gate:** patient–lesion–ROI/habitat–specimen–block–section–assay–time mapping, matched-intersection n,
at least two biological hypotheses plus one technical/sampling hypothesis, and discriminating evidence.

## 11. Perturbation and causal failures — only when perturbation/causality is active

- Assignment, multiplicity, efficiency, off-target risk, dose/time, controls or target engagement is
  missing.
- Toxicity/stress is mistaken for target mechanism; one experimental replicate is treated as causal
  confirmation.
- A virtual perturbation is reported as an experiment or evaluated only on seen contexts.

**Gate:** assignment and control audit, independent biological replication, target engagement,
phenotype timing, negative/positive controls, rescue or orthogonal perturbation where appropriate, and
simple-baseline plus unseen-context evaluation for predictions.

## 12. Prediction, prognosis and treatment-benefit confusion

- High apparent performance comes from leakage, class imbalance, site/batch signal or selected test data.
- A one-arm outcome association is described as treatment benefit.
- Performance is reported without calibration, CI, intended use or external domain.

**Gate:** locked target and split, simple baselines, calibration/uncertainty, external validation, and a
valid comparator plus biomarker-by-treatment interaction for differential treatment effect.

## 13. Reproducibility and integrity gaps

- Sample/accession mapping, exclusions, software/version, parameters, code or full result tables are
  absent.
- Reported counts/effects conflict across abstract, figures, tables, supplements or response letter.
- Citations do not support the load-bearing claim or data are uploaded outside approved boundaries.

**Gate:** evidence anchors, denominator reconciliation, versioned workflow, data/code availability and
permission-aware sharing. Never infer that an analysis was run from prose saying it was promised.

## 14. Pre-submission self-check

`Scope correct? · independent unit and hierarchy explicit? · usable n reconciled? · active-modality QC complete? · all learned steps leakage-safe? · batch/site overlap credible? · multiplicity family declared? · evidence state and claim link separated? · validation matches the claim? · wording stays below the claim ceiling?`

For each failure, report `P0/P1/P2`, evidence location, scientific consequence, exact repair, claim
verdict (`PASS/CONDITIONAL/STOP`) and the wording allowed before repair. Severity and claim verdict are
different scales.
