# Mask geometry, physical-space identity, and format integrity

A mask that is shifted, flipped, linked to the wrong series, or interpreted in the wrong physical
space silently corrupts every downstream feature and measurement. A grid mismatch is not, by itself,
permission to resample. First establish object identity and the physical transform; only then decide
whether resampling is valid.

## 1. Identity and physical-space gate

Before comparing arrays or changing a grid, verify and record:

- stable de-identified patient/subject identity and examination identity;
- source image, referenced series/SOP instances, segmentation/RT object and mask version;
- DICOM Frame of Reference UID when available, or the documented DICOM-to-NIfTI provenance that
  carries the same physical coordinate system;
- image and mask size, spacing, origin, direction/orientation, slice/frame order and physical extent;
- fixed and moving objects, transform direction, transform ID/hash, method/version and responsible
  producer for any registration;
- whether the mask is a discrete label map, fractional/probability segmentation or contour object.

Do not use patient names, filenames, row order, lesion numbers or visually similar anatomy as proof
that two objects share an identity or coordinate system. A matching array shape is not proof of a
matching physical space.

## 2. Geometry decision table

| State ID | Required evidence | Allowed action | Verdict |
|---|---|---|---|
| `SAME_SPACE_SAME_GRID` | same patient/exam/object; same FoR or provenance-confirmed physical space; size, spacing, origin and direction match within declared numeric tolerance | preserve the mask without resampling; complete per-case QC | `PASS` |
| `SAME_SPACE_DIFFERENT_GRID` | same patient/exam/object; same FoR or provenance-confirmed physical space; the grid difference is a documented legitimate representation change | resample to the prespecified target grid; nearest-neighbour for discrete labels; record all fields and complete per-case QC | `CONDITIONAL` |
| `CROSS_SPACE_TRUSTED_TRANSFORM` | same patient/exam/target; different FoR/space; a verified transform names fixed/moving objects, direction, method/version and provenance | apply the recorded transform and target grid; call this registration/propagation, not simple grid resampling; complete local boundary QC | `CONDITIONAL` |
| `IDENTITY_OR_TRANSFORM_UNKNOWN` | patient/exam identity is unknown or conflicting; FoR/provenance is absent or conflicting; referenced series is wrong/unknown; or a required transform is missing/untrusted | do not resample, relabel metadata or continue extraction; recover provenance or obtain a verified transform | `STOP_FOR_REPAIR` |
| `METADATA_REWRITE_ONLY` | origin, direction, FoR UID or reference links would be edited merely to make arrays appear aligned | prohibited; restore source metadata and establish the real mapping | `STOP_FOR_REPAIR` |

An identity transform is valid only when both objects are already known to occupy the same physical
coordinate system. It cannot establish that fact. Never use `SetOrigin`, `SetDirection`, copied FoR
UIDs or header edits as an alignment method.

## 3. Format-specific boundaries

- **DICOM to NIfTI:** retain the converter/version and a source-instance-to-output manifest. Different
  converters can change axis convention or slice order; verify the physical affine and source mapping,
  not only the displayed orientation label.
- **DICOM-SEG:** confirm the referenced source instances, FoR, segment number/coded meaning,
  segmentation type and per-frame geometry. DICOM storage does not guarantee that the selected source
  series is correct.
- **RTSTRUCT:** contours are patient-coordinate polygons, not voxel masks. Record the referenced FoR
  and series, rasterizer/version, target grid, contour-plane handling and any interpolation.
- **NIfTI or other detached masks:** recover the DICOM/source provenance or another verified mapping.
  A plausible affine or matching dimensions alone is insufficient.
- **Discrete labels:** use nearest-neighbour when a valid resample/transform is permitted; confirm that
  label values and topology are preserved.
- **Fractional/probability maps:** do not apply the discrete-mask rule automatically. Declare the
  interpolation, range, thresholding and whether thresholding creates a new versioned label object.

## 4. Required resampling or registration receipt

For every permitted transformation record:

```text
patient/exam/object IDs -> source image and mask IDs/hashes -> referenced series/SOP set ->
source FoR/affine/grid -> target FoR/affine/grid -> fixed/moving roles -> transform ID/hash and
direction -> transform producer/method/version -> interpolator and default value -> label semantics ->
pre/post label counts and physical volumes -> per-case machine QC -> per-case visual QC -> reviewer ->
verdict/deviation
```

Do not overwrite the source mask. The transformed mask is a new version linked to the source,
transform and target image.

## 5. Per-case QC, not a sampled visual reassurance

Run machine and visual checks for **every transformed or imported case**:

1. Verify patient/exam/object identity, source references, FoR/affine and transform provenance before
   transformation.
2. Compare physical extents, target overlap, label set, empty/non-empty state, component count and
   pre/post physical volume by label. Investigate changes outside a prespecified task-based tolerance;
   no universal percentage is supplied.
3. Overlay image and mask in axial, coronal and sagittal planes and inspect target boundaries,
   first/last occupied slices and known asymmetric landmarks. A single central slice is insufficient.
4. For registered/propagated masks, inspect local target alignment and deformation plausibility;
   a high global similarity metric does not clear a local failure.
5. Record pass/fail and the responsible reviewer for every case. Keep failed, empty, cropped and
   non-evaluable cases in the denominator and downstream manifest.

Automated sampling may supplement a release-level audit, but it cannot replace per-case geometry
checks for masks that enter measurement, radiomics or model evaluation.

## 6. Stop gates and handoff

Return `STOP_FOR_REPAIR` when patient/exam identity is unresolved, the referenced source series is
wrong or unknown, FoR/affine provenance conflicts, a required transform is absent/untrusted, metadata
was rewritten to mimic alignment, local target alignment fails, or the transformation receipt cannot
be reconstructed.

Return:

`identity/source-reference gate -> physical-space state -> permitted action -> transformation receipt
-> per-case multiplanar/boundary QC -> volume/label change -> PASS/CONDITIONAL/STOP -> downstream
mask version and prohibited upgrade`.

Geometry clearance means that the mask is spatially usable under the verified mapping. It does not
establish biological truth, annotation quality, clinical validity or feature stability.
