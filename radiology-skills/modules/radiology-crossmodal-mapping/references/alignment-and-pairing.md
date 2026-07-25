# Alignment and Pairing

Use this reference to determine what is actually paired, select the defensible shared analysis
unit, and limit the biological inference accordingly.

## Mapping hierarchy

Trace every proposed link through:

```text
patient -> lesion -> specimen -> section -> region -> cell
```

| Level | Required link | Common failure | Defensible response |
|---|---|---|---|
| Patient | Stable cross-system patient key | Different or duplicated subjects | Resolve provenance; exclude unresolved links |
| Lesion | Imaging lesion matches sampled lesion | Multiple lesions or metastases treated as interchangeable | Use lesion IDs; aggregate only under a prespecified patient-level estimand |
| Specimen | Biopsy/resection provenance and date | Tissue assumed to represent the whole lesion | Record sampling route and tissue fraction; lower claim level |
| Section | Assay and histology section relationship | Adjacent or distant sections called identical | State section distance/orientation and registration uncertainty |
| Region | ROI, habitat, spot, tile, or neighborhood correspondence | Whole-slide or whole-tumor averages assigned to a local region | Register regions or aggregate to a shared coarser unit |
| Cell | Measured cell, segmented cell, or inferred state | Transferred/deconvolved labels called direct measurements | Label inferred quantities and propagate uncertainty |

Use the **finest common unit with verified correspondence; coarsen until defensible**. Evidence at
a coarser unit cannot be promoted to a finer one. Repeated lesions, sections, regions, spots, or
cells remain nested within the patient for splitting and inference.

## Mapping-unit table

Create one row per proposed imaging-to-cellular link. Include:

- source-system record IDs and stable patient ID;
- lesion, laterality, anatomy, primary/metastatic status, and sampling target;
- imaging date, acquisition phase/sequence, and phenotype or habitat definition;
- biopsy/resection date, treatment or disease change between time points, and acceptable time window;
- specimen, block, slide/section, assay, spatial region/spot/tile, and cell-state definition;
- registration method, landmarks, transforms, resolution, spatial tolerance, and quality measure;
- link correspondence (direct, weak, unpaired, or unresolved), finest verified common unit, missing
  or ambiguous keys, and planned exclusion/aggregation;
- scanner/site, assay platform, processing batch, and other variables that could encode the link;
- uncertainty source and whether it is modelled, stratified, or handled in sensitivity analysis.

Keep the raw correspondence table versioned and separate from any resolved analysis table. Resolve
identity, provenance, eligibility, and modality availability before splitting without consulting
outcomes, expression, cell states, imaging phenotypes, apparent biological correspondence, or model
performance. Do not silently select a convenient record.

## Link-level correspondence

Classify each proposed link independently of how complete the cohort is:

| Link status | Minimum correspondence | Suitable analyses | Permitted inference |
|---|---|---|---|
| **Direct** | Same verified patient and correspondence documented through the claimed lesion/specimen/section/region, with acceptable timing | Association or supervised mapping at the verified common unit | “Associated with” or “correlated with” at the verified unit; “co-localized with” only for directly registered regional evidence |
| **Weak** | Same verified patient key, but lesion, specimen, section, region, or timing correspondence is incomplete or indirect | Patient-level aggregation, multiple-instance or uncertainty-aware mapping | Patient-level association or concordance only; not local co-occurrence or cellular attribution |
| **Unpaired** | Different patients/cohorts, or no verified shared patient key, including disease-, anatomy-, or time-matched records and public atlases | Cohort-level enrichment, distribution alignment, reference support, or hypothesis generation | “Concordant across cohorts,” “reference-supported,” or “hypothesis-generating”; never patient-level mapping or mechanism |
| **Unresolved** | Keys or provenance conflict or are insufficient to decide | Metadata resolution; exclusion or prespecified missing-link handling | No direct mapping claim until resolved without biology- or outcome-driven choices |

Disease, anatomy, and time-window similarity do not make different patients weakly paired. Weak
pairing requires a shared verified patient key.

## Cohort completeness

Classify completeness separately from link status:

| Completeness | Definition | Reporting consequence |
|---|---|---|
| **Fully paired** | Every eligible analysis unit has the required modalities and a prespecified usable direct or weak link | Report counts by link status and the common unit; completeness does not upgrade weak links |
| **Partially paired** | Only a subset of eligible units has both modalities or usable links; others have missing modalities or unresolved correspondence | Report availability and link-status counts; analyze the paired subset and missingness/selection separately |

Partially paired does not mean missing links can be recovered without assumptions. Report unique
patients, lesions, specimens, sections, regions, and cells by link status and availability, not only
the largest row count.

## Design evidence-label crosswalk

Use the four design labels as follows while retaining the operational link-status and
cohort-completeness fields:

| Design evidence label | Explicit definition | Operational representation |
|---|---|---|
| **Paired** | A proposed cross-modal link has direct, verified correspondence at the claimed common unit | Link status = `direct`; this label alone does not state cohort completeness |
| **Partially paired** | The cohort contains a paired subset, while other eligible units have a missing modality, missing link, or unresolved correspondence | Cohort completeness = `partially paired`; each available link still receives `direct`, `weak`, `unpaired`, or `unresolved` status |
| **Weakly paired** | Both modalities share a verified patient key, but spatial, lesion, specimen, section, region, or temporal correspondence is weaker than the intended mapping unit | Link status = `weak`; inference is limited to the verified patient level |
| **Unpaired** | The modalities have no shared verified patient key, even if disease, anatomy, or timing are matched | Link status = `unpaired`; inference is cohort-level only |

Thus, `partially paired` is cohort-level completeness, not a per-link status or a synonym for
`weakly paired`.

## Spatial alignment

Record the coordinate systems and physical scales for imaging voxels, gross specimen slices,
histology sections, spatial-omics spots, pathology tiles, and cells. Choose among:

- **Direct registration** when fiducials, landmarks, specimen orientation, or validated transforms
  provide regional correspondence.
- **Region aggregation** when fine registration is unreliable but both modalities support a common
  anatomical, lesion, or habitat unit.
- **Probabilistic or multiple-instance mapping** when a specimen may correspond to several imaging
  regions and uncertainty can be represented explicitly.
- **Patient-level mapping** when only the patient is shared; do not manufacture region labels.

Report deformation, sectioning distortion, orientation ambiguity, partial-volume effects, spot
diameter, cell segmentation uncertainty, and the ratio between source and target spatial scales.
Never broadcast a specimen- or patient-level molecular value to every voxel, region, or cell and
then treat the resulting rows as independent observations.

## Temporal alignment

Define the acceptable interval from the biological question, not data convenience. Record:

- imaging and sampling dates and the direction of the interval;
- surgery, biopsy, systemic therapy, radiotherapy, steroids, or other interventions between them;
- progression, recurrence, or anatomical change;
- longitudinal time point and whether the same lesion remains measurable;
- same-day, prespecified-window, and treatment-free sensitivity subsets.

When treatment or disease evolution can alter cell states, either restrict to a defensible window,
adjust or stratify under a prespecified model, or downgrade the link status. A long interval is not
repaired by statistical adjustment alone.

## Scale-alignment rules

1. Select the finest common unit with verified correspondence; coarsen until defensible.
2. Aggregate the finer modality to that unit using a prespecified summary: counts, proportions,
   pseudobulk expression, pathway scores, neighborhood abundance, or uncertainty-weighted estimates.
3. Preserve nesting in the analysis model and effective sample size; thousands of cells do not
   replace the number of independent patients.
4. Define how multiple lesions, specimens, sections, and regions are combined or compared.
5. Propagate registration, deconvolution, label-transfer, and sampling uncertainty when feasible.
6. Repeat key analyses across reasonable aggregation and alignment choices.

## Claim calibration

| Evidence state | Preferred wording | Avoid |
|---|---|---|
| Directly registered regional evidence, independently validated | “The imaging habitat was co-localized with the measured cell state in directly registered regions.” | “The habitat causes the cell state” |
| Direct at lesion or patient level only | “The lesion/patient imaging phenotype was associated/correlated with cellular composition.” | “Co-localized,” “this image region contains these cells,” or any regional attribution |
| Partially paired cohort | “The relationship was observed in the paired subset and was consistent in…” | Applying paired-subset certainty to missing or unresolved units |
| Weak link with verified shared patient | “A patient-level concordant pattern was observed.” | Anatomy-level local correspondence or direct lesion, region, or cell attribution |
| Unpaired | “The imaging pattern was consistent with enrichment in an independent reference cohort and is hypothesis-generating.” | Patient-level mechanism proof, co-localization, or clinical biomarker validation |

Even strong paired association does not establish direction, causality, therapeutic response, or
mechanism without appropriate longitudinal, interventional, perturbational, or experimental
evidence.
