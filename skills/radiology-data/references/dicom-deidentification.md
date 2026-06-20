# DICOM de-identification

Imaging cannot be shared until PHI is removed from **both** the DICOM metadata **and** the
pixels. Follow a recognised standard and verify.

## Two surfaces of PHI
1. **DICOM header tags** — patient name (0010,0010), ID (0010,0020), birth date (0010,0030),
   accession (0008,0050), institution (0008,0080), referring physician, study/series dates &
   times, device serial numbers, UIDs, and many private tags.
2. **Burned-in pixel PHI** — text overlaid on the image (name/MRN/date), secondary-capture
   screenshots, ultrasound/again annotations, and **overlay planes** (60xx). Also faces in
   head CT/MRI (3-D reconstructable).

## Standard & profile
- Use the **DICOM PS3.15 Basic Application Level Confidentiality Profile** with appropriate
  options (e.g. Retain Longitudinal Temporal with date **shifting**, Retain Patient
  Characteristics) — keep what research needs (age, sex, dates *relative* via consistent
  shift) while removing identifiers.
- **Consistent date-shifting** per patient preserves intervals (important for longitudinal/
  follow-up) without real dates.
- Keep a **secure linkage key** separately (or destroy it for full anonymisation) per IRB.

## Faces — defacing
- Defacing/skull-stripping for head MRI/CT to prevent facial reconstruction (e.g.
  `pydeface`, `mri_deface`, FSL/AFNI tools). Confirm it doesn't remove ROI.

## Tools
- **CTP (RSNA Clinical Trial Processor)**, **DICOM Library / dcm4che**, **pydicom** scripts,
  **TCIA's de-identification workflow** (if depositing to TCIA — follow their requirements),
  **gdcm**. Verify, don't trust defaults.

## Verification (mandatory)
- Re-scan headers for residual identifiers (incl. **private tags** and UIDs).
- Visually inspect a **sample of pixels** for burned-in text; check secondary captures and
  overlays.
- Document the method + profile + tools in Methods (CLAIM/ethics).

## Checklist
`header tags removed (incl. private/UIDs)? · dates shifted consistently? · pixel PHI/overlays
removed? · faces defaced? · linkage key handled per IRB? · verified on a sample? · method
documented?`
