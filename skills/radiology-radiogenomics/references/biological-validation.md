# Biological interpretation and validation

Radiogenomics reviewers will accept associations more readily than unsupported mechanisms. Use
this file to strengthen interpretation without overstating causality.

## Claim ladder
Use the strongest claim the evidence supports:

1. **Association**: imaging feature correlates with molecular variable after multiplicity and
   confounder control.
2. **Replicated association**: direction/effect size reproduces in an independent cohort.
3. **Biological concordance**: pathway, cell type, or spatial pattern is consistent with the
   imaging phenotype.
4. **Orthogonal validation**: IHC, multiplex IF, spatial transcriptomics, proteomics, or another
   assay supports the same biology.
5. **Mechanistic evidence**: perturbation or experimental model shows causality. Most clinical
   radiogenomics studies do not reach this level.

## Strengthening a feature-gene result
- Collapse unstable single-gene findings into pathway scores when biologically justified.
- Use curated gene sets and report collection/version, ranking metric, NES or effect size, FDR.
- Validate direction and magnitude in an independent dataset or orthogonal assay.
- Show the association is not explained only by tumour volume, site/scanner, sequencing batch, or
  major subtype imbalance.

## Single-cell and deconvolution validation
- Report reference atlas, cell annotation source, deconvolution method, and uncertainty.
- Prefer patient-level or pseudobulk association to cell-level pseudo-replication.
- Validate key cell types with IHC/multiplex IF/spatial methods when possible.
- State when deconvolution estimates composition rather than direct measurement.

## Spatial validation
- Register spatial data through documented steps: imaging -> gross pathology/histology -> tissue
  section -> spots/cells/regions.
- Quantify or at least bound registration and sampling uncertainty.
- Report whether the spatial subset is representative of the full cohort.
- Avoid whole-tumour claims from one section unless supported by sampling strategy.

## Words to avoid unless evidence supports them
Avoid: "drives", "causes", "mechanism", "surrogate marker", "noninvasive biopsy".

Prefer: "was associated with", "reflected a phenotype enriched for", "was consistent with",
"may capture", "supports the hypothesis that".

## Discussion paragraph pattern
1. Main radiogenomic association, with effect size and validation status.
2. Biological context from pathway/cell-type/spatial evidence.
3. Alternative explanations: batch, volume, subtype, tissue sampling.
4. Why the result is useful: hypothesis generation, stratification, trial enrichment, or
   noninvasive prioritization.
5. Bounded next step: prospective validation, spatially matched sampling, or functional work.