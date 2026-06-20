# Mask geometry & format integrity

A mask that is one voxel off, flipped, or resampled differently from its image silently corrupts
every feature. Verify geometry before extraction.

## The invariants image and mask MUST share

| Property | Must match | Symptom if wrong |
|---|---|---|
| **Spacing** (pixel/voxel size) | Identical | Size/texture features wrong; partial overlap |
| **Origin** (image position patient) | Identical | Mask shifted in space |
| **Direction / orientation** (cosines) | Identical | Axis flips; left/right or sup/inf swap |
| **Dimensions** (rows × cols × slices) | Identical (after any resample) | Index misalignment |
| **Slice order** | Same ordering (watch z-flip) | Mask on wrong slices |
| **Frame of reference** (DICOM) | Same FoR UID | Cross-series misregistration |

## Format conversion pitfalls

- **DICOM → NIfTI:** different converters can flip axes or reorder slices; verify orientation
  after conversion (e.g. overlay mask on image). Keep the converter + version.
- **DICOM-SEG:** segmentation stored in DICOM; preserves FoR — preferred for clinical
  interoperability; confirm the referenced series.
- **RTSTRUCT:** contour-based (polygons), not voxel masks; rasterisation to a binary mask depends
  on resolution and can differ from the viewer — check the rasteriser.
- **Resampling:** if image is resampled (e.g. to isotropic), resample the mask with
  **nearest-neighbour** (never linear) and re-verify alignment.

## Minimal QC checklist (do before extracting features)

1. Load image and mask; assert spacing/origin/direction/dimensions match (print and compare).
2. Overlay mask on image on ≥1 slice per case (or a sampled subset) and eyeball alignment.
3. Confirm slice order / no z-flip (check a known-asymmetric anatomy).
4. After any resample: nearest-neighbour for mask; re-assert geometry.
5. Confirm mask labels (which integer = which region) and that empty masks are flagged.

## Quick programmatic check (SimpleITK)

```python
import SimpleITK as sitk
img  = sitk.ReadImage(image_path)
mask = sitk.ReadImage(mask_path)
for attr in ("GetSize", "GetSpacing", "GetOrigin", "GetDirection"):
    assert getattr(img, attr)() == getattr(mask, attr)(), f"{attr} mismatch"
# resample mask to image grid if needed (nearest neighbour):
mask_rs = sitk.Resample(mask, img, sitk.Transform(), sitk.sitkNearestNeighbor, 0, mask.GetPixelID())
```

## Reporting sentence

*"Masks and images shared spacing, origin, direction, and slice order (verified per case);
images were resampled to 1×1×1 mm and masks resampled by nearest-neighbour interpolation, with
alignment re-verified before IBSI-compliant feature extraction."*
