# Re-identification risk in imaging + omics

Re-identification is a spectrum. Identify the specific risks in the data and the mitigation for
each. De-identification *mechanics* live in `radiology-data`; this file is the *risk read*.

## Risk sources

| Source | Risk | Mitigation |
|---|---|---|
| **DICOM metadata** | Names, IDs, dates, institution, device serials, private tags | De-id headers to a standard (e.g. DICOM PS3.15 profile); remove/replace; keep an audit |
| **Burned-in pixel text** | PHI rendered into the image (US, screenshots) | Detect and redact pixel PHI before sharing |
| **Facial reconstruction** | Some head CT/MRI can permit facial reconstruction or matching | Perform a **risk- and use-specific** facial-risk assessment; apply a validated defacing method when needed, or use controlled access when transformation would be inadequate or would damage the measurement |
| **Skull stripping** | Brain-extraction preprocessing removes non-brain anatomy for some analyses, but is not designed or validated as a privacy control | Treat separately from defacing; **skull stripping is not a synonym or substitute for defacing** and must not be represented as such |
| **Dates & ages** | Exact dates + rare events can re-identify | Apply the approved jurisdiction- and use-specific transformation or access control; HIPAA Safe Harbor age/date rules apply only when that route is the governing determination |
| **Small / rare-disease cohorts** | Few patients → uniqueness | Aggregate, suppress small cells, or controlled access |
| **Geography / site** | Small-area + rare disease | Coarsen location; avoid identifying small centers |
| **Genomic data** | Inherently identifying; cannot be fully anonymised | **Controlled access** (dbGaP/EGA); never open-post raw germline |
| **Linkage** | Combining quasi-identifiers across tables | Minimise shared quasi-identifiers; review joint risk |

## Imaging-specific release decisions

1. Strip DICOM header PHI (and private tags) to a recognised profile.
2. Remove burned-in pixel PHI.
3. For head imaging, assess facial reconstruction/matching risk against anatomy, resolution,
   population, linkage context, intended recipients and release model. Use validated **defacing**
   when the risk/use decision requires it. Do not call skull stripping defacing, and do not assume
   either operation authorizes sharing.
4. Apply the approved date and age treatment for the governing jurisdiction and release model; do
   not universalize one de-identification route.
5. Re-check after conversion (NIfTI metadata can re-introduce identifiers).

## Measurement sensitivity and access boundary

Privacy transformation is part of the measurement provenance. For the intended task, compare native
and transformed data on a prespecified, task-matched sample and record method/version, failure rate and
material changes in geometry, field of view, intensities, quantitative maps, segmentations,
radiomics, model outputs or reader-visible anatomy as applicable. A visual spot check alone cannot
establish measurement neutrality, and a successful defacing run does not prove zero re-identification
risk.

Keep any identifiable native copy only under the approved security and retention controls. If the
validated transformation removes clinically or scientifically required anatomy, has a material or
unknown measurement effect, fails on relevant cases, or leaves unacceptable residual risk, do not
silently weaken either privacy or measurement validity. Use a controlled access alternative with
documented authorization, data-use terms, recipient controls and auditability, or mark the proposed
release `STOP` until the responsible governance owner decides. The decision is risk- and use-specific;
open release is not the default endpoint for every de-identified image.

## Genomics + imaging (radiogenomics) note

- Genomic data are **not** anonymisable; pairing them with imaging raises joint risk.
- Default to **controlled access** for the molecular layer (dbGaP/EGA), with a data-access
  committee; imaging may be shareable separately after de-identification.
- The consent must cover genomic data generation and sharing (→ approval-consent.md).
- If human material also creates a laboratory biological risk, route biosafety applicability to the
  current IBC/biosafety-equivalent owner; human-subjects approval does not substitute for that review.

## Risk-read output

```
Data types & identifiers present:
Re-identification risks (ranked):
Mitigations applied / planned:   [de-id profile, risk/use-specific defacing decision, date/age rule, suppression, controlled access]
Transformation sensitivity:     [task, sample, method/version, failures, measurement effects]
Residual risk & access model:    [open / registered / controlled / not shareable]
```

## Reporting sentence

*"Imaging was processed under [approved profile/release determination]; burned-in PHI was assessed
and removed where present. Facial-risk mitigation for head imaging used [method/version or controlled
access rationale], selected for the intended use, with task-matched transformation sensitivity
reported in [locator]. Date/age handling followed [governing determination]. Residual-risk review
supported [open/registered/controlled] access. Genomic data are available under controlled access
([repository/accession]) via [authorized process], consistent with participant consent."*
