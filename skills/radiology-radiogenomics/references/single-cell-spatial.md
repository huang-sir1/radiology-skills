# Single-cell & spatial omics ↔ imaging

Bulk expression tells you *what* genes; single-cell and spatial omics tell you *which cells*
and *where* — which is what imaging actually sees (heterogeneity, habitats). This is the
frontier of radiogenomics.

## A. Deconvolving bulk from imaged regions
When you have **bulk** RNA-seq from an imaged tumour/region but want cell-type composition:
- **Reference-based deconvolution** estimates cell fractions from bulk using a scRNA-seq
  reference signature.
  - **CIBERSORTx** (signature matrix + batch correction), **BayesPrism**, **MuSiC**, **Bisque**,
    **SCDC**, **EPIC**, **quanTIseq** (immune).
- Tie estimated fractions (e.g. macrophage, T-cell, tumour, stroma) to imaging features /
  habitats: *"higher rim enhancement ↔ higher estimated macrophage fraction."*
- Report the reference used, its provenance, and that deconvolution is an **estimate** with
  uncertainty; validate the key cell type (e.g. IHC) where possible.

```text
Workflow: scRNA-seq reference -> signature matrix -> deconvolve bulk (per imaged region)
          -> cell fractions -> associate with radiomic/habitat features (FDR-controlled)
```

## B. Native single-cell from imaged lesions
If lesions are dissociated and sequenced (scRNA-seq/snRNA-seq):
- Standard QC (doublets, mito%, depth), normalisation, integration across samples
  (Harmony/scVI), clustering, cell-type annotation.
- Aggregate to **pseudobulk** per patient for robust patient-level association with imaging
  (avoids pseudo-replication across cells).

## C. Spatial transcriptomics ↔ imaging habitats (strongest linkage)
Spatial omics preserves location, so it can be **co-registered** to imaging sub-regions:
- Platforms: **Visium / Visium HD** (spot-based), **Xenium / MERFISH / CosMx** (single-cell,
  targeted), **Slide-seq**, **GeoMx** (region-of-interest).
- Register the spatial slide to **histology**, then relate histology/habitat to the
  **radiology habitat** (this multi-scale registration is the hard part — report the method
  and its limits).
- Per-region: cell-type niches, ligand-receptor/neighbourhood analysis (`squidpy`,
  `Seurat`/`Giotto`), spatially-variable genes — then correlate with the matched imaging
  habitat's radiomics.

## Cross-scale caution
- **Registration/co-localisation error** between micron-scale omics and mm-scale imaging is
  the dominant uncertainty; quantify it and bound the claim.
- Single biopsy/section ≠ whole tumour; state the sampling.

## Tools
`scanpy`/`Seurat` (single-cell), `squidpy`/`Giotto`/`semla` (spatial), `CIBERSORTx`/
`BayesPrism` (deconvolution), `scvi-tools`/`Harmony` (integration).

## Reporting sentence
*"Bulk RNA-seq from the resected enhancing core was deconvolved with BayesPrism (Tabula
reference); estimated M2-macrophage fraction correlated with the enhancing-habitat GLCM
contrast (rho = 0.46; FDR < 0.05) and was spatially corroborated by Xenium niches in a
subset (n = 8), acknowledging mm-to-micron registration uncertainty."*
