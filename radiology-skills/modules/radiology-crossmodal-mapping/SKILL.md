---
name: radiology-crossmodal-mapping
description: "Use when an imaging study must map radiology phenotypes or habitats to single-cell, spatial-omics, or pathology-derived cell states across patients, lesions, specimens, regions, or time points. Designs paired, weakly paired, or unpaired cross-modal mapping; audits alignment, deconvolution, label transfer, contrastive learning, validation, scale mismatch, and biological-claim limits. Never treats unpaired public omics as direct patient-level mechanism proof."
---

# Radiology Cross-Modal Mapping

Use this skill when the central problem is how to align an imaging phenotype or habitat with
single-cell, spatial-omics, or pathology-derived cellular states. Make the mapping unit and its
uncertainty explicit before choosing a method.

## Core stance

- Map at the **finest common unit with verified correspondence; coarsen until defensible**. Never
  promote cohort concordance to patient-, lesion-, region-, or cell-level evidence.
- Classify each link as direct, weak, unpaired, or unresolved; separately classify cohort
  completeness as fully or partially paired.
- Treat registration, sampling, timing, treatment, and spatial-scale mismatch as analysis variables,
  not footnotes.
- Audit identity, eligibility, and provenance metadata before splitting; do not use outcomes,
  biological measurements, or apparent correspondence to resolve links. Then split by patient and,
  when applicable, center, keeping every fitted step inside training data.

## Required intake

Collect the phenotype, assay, anatomy, endpoint, cohorts/centers, hierarchy identifiers, dates,
intervening treatment, registration evidence, modality missingness, batch/site variables, intended
claim, and validation material. Mark unknown or conflicting links as unresolved.

Create a **mapping-unit table** before analysis:

| Imaging record | Verified patient | Lesion | Imaging/time | Specimen/section | Region/cell state | Link correspondence | Finest verified common unit | Uncertainty |
|---|---|---|---|---|---|---|---|---|
| one row per proposed link | ID/none | ID | date/phase | ID(s) | ID/label | direct/weak/unpaired/unresolved | patient/lesion/region | source/magnitude |

Add a cohort summary stating eligible counts, modality availability, and whether completeness is
fully or partially paired. See [alignment and pairing](references/alignment-and-pairing.md) for
definitions, scale mismatch, and permitted inference.

## Workflow

1. **Define the estimand.** State the imaging feature or habitat, cellular state or spatial
   neighborhood, shared unit, endpoint, direction of mapping, and whether the aim is discovery,
   prediction, annotation transfer, or biological corroboration.
2. **Audit metadata before splitting.** Using identity, provenance, modality availability, dates,
   and prespecified eligibility only, trace patient -> lesion -> specimen -> section -> region ->
   cell. Assign link correspondence and cohort completeness; freeze unresolved links. Do not inspect
   outcomes, expression, cell states, imaging features, or biological plausibility.
3. **Split, then align.** Split eligible patients and reserve centers when applicable. Apply the
   prespecified finest common unit with verified metadata correspondence and coarsen until
   defensible; learn any image-, omics-, or biology-driven alignment in training only.
4. **Choose the mapping route.** Match pseudobulk, deconvolution, canonical correlation,
   contrastive mapping, graph alignment, or habitat linkage to the link status, scale, and sample
   size. Transfer labels across imaging and omics only through a paired bridge, shared measured
   features, or an independently validated cross-modal mapper; otherwise transfer within omics and
   validate the imaging association separately.
5. **Lock leakage-safe validation.** Keep feature selection, habitat
   discovery, normalization, anchor learning, label transfer, deconvolution tuning, embedding,
   graph construction, and threshold selection inside training. Add held-out-center or external
   validation when transportability is claimed.
6. **Run controls.** Include mapping permutations, biologically implausible or negative regions,
   null features, method-specific nulls, and site/batch-aware baselines.
7. **Run sensitivity analyses.** Vary registration tolerance, temporal window, aggregation level,
   habitat definition, cell-state reference, preprocessing, covariates, and borderline links.
8. **Validate biology.** Prefer an independent cohort and orthogonal IHC, multiplex
   immunofluorescence, in situ hybridization, pathology, or separately measured spatial evidence.
9. **Bound claims.** Tie each conclusion to its link status, cohort completeness, shared unit, validation, and
   unresolved alternative explanations.

Open [mapping and validation](references/mapping-and-validation.md) to select a method and specify
patient/center separation, negative controls, sensitivity analyses, external validation, and
orthogonal biological validation.

## Output contract

Return the applicable components:

1. **`Mapping question`**: phenotype, cell state, purpose, direction, and estimand.
2. **`Mapping-unit table`**: hierarchy, dates, link status, verified common unit, uncertainty.
3. **`Pairing/alignment audit`**: completeness, mismatch, exclusions, permitted inference.
4. **`Mapping plan`**: method, assumptions, preprocessing, covariates, simple baseline.
5. **`Leakage-safe validation`**: patient/center splits and train-only operations.
6. **`Controls/sensitivities`**: nulls and alternative alignment, timing, aggregation, references.
7. **`Validation plan`**: internal, external, orthogonal evidence, success criteria.
8. **`Bounded claims`**: supported wording, prohibited wording, uncertainty, missing inputs.

## Routes

- Use `radiology-radiogenomics` when general imaging-omics association, integration, prediction,
  or biological interpretation is central and cross-scale alignment is not the primary problem.
- Route annotation/registration to `radiology-annotation`, inference/resampling to
  `radiology-stats`, representation design to `radiology-deep-learning`, reporting to
  `radiology-reporting`, and data provenance/sharing to `radiology-data`.

## Red lines

- Do not treat unpaired public omics or a reference atlas as direct patient-level, lesion-level, or
  mechanistic proof.
- Do not call disease-, anatomy-, or time-matched different patients weakly paired; without a shared
  verified patient key they are unpaired and support cohort-level inference only.
- Do not call deconvolved or transferred labels directly measured cells.
- Do not transfer labels directly between imaging and omics without a paired bridge, shared measured
  features, or an independently validated cross-modal mapper.
- Reserve **co-localized** for directly registered regional evidence; describe patient- or
  lesion-level relationships as associated or correlated.
- Do not call evaluation independent when a test patient appears in an atlas, mapper-training set,
  or pretrained reference. Exclude the overlap or label the evaluation non-independent/model-exposed.
- Do not mix cells, regions, lesions, or time points from one patient across training and test sets.
- Do not fit habitats, anchors, embeddings, thresholds, or feature selection on held-out data.
- Do not use causal or therapeutic language without an appropriate causal or experimental design.
- Never invent identifiers, pairings, registration quality, biological associations, validation
  results, or missing metadata.
