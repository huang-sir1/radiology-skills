# Imaging panels — montages, annotation, de-identification

Imaging figures are evidence. Build them legible, annotated, and **de-identified**.

## De-identification (do this first, always)
- Remove burned-in PHI: patient name, MRN, accession, dates, institution from DICOM
  overlays and image corners.
- Strip DICOM overlay planes / annotation layers; export pixel data only.
- No identifiable faces: **deface** 3-D renderings and face-region MR.
- Keep a record that the displayed images contain no PHI (CLAIM/ethics).

## Windowing & display
- State **window level / window width** (WL/WW) per image (e.g. "lung window, WL −600 WW
  1500"); keep windowing consistent across a comparison row.
- Grayscale for anatomy; reserve color for overlays/parametric maps with a **labelled
  colorbar** (units!).
- Do not over-compress (JPEG artefacts); export from source resolution.

## Annotation
- **Arrows / arrowheads / asterisks** to mark findings; one symbol = one meaning; define all
  in the legend.
- **Insets / magnifiers** for small findings (draw the source box on the overview).
- **Scale bar** or stated FOV whenever lesion size matters.
- Keep annotations off the finding itself; use consistent arrow style/size.

## Layout
```python
import matplotlib.pyplot as plt
def montage(images, rows, cols, labels=None, wlww=None, panel_letters=True, figw=6.7):
    fig, axs = plt.subplots(rows, cols, figsize=(figw, figw*rows/cols))
    for i, ax in enumerate(axs.ravel()):
        ax.axis("off")
        if i < len(images):
            ax.imshow(images[i], cmap="gray", vmin=0, vmax=255)
            if panel_letters:
                ax.text(0.04, 0.96, chr(65+i), transform=ax.transAxes, color="w",
                        fontsize=10, fontweight="bold", va="top")
            if labels: ax.set_title(labels[i], fontsize=8)
    fig.subplots_adjust(wspace=0.02, hspace=0.06)
    return fig
```
- Align panels on a grid; equal gutters; label **A, B, C** (white text, top-left, bold).
- For before/after or multi-sequence, keep the same crop, zoom, and window across panels.

## Overlays (segmentation / parametric maps / habitats)
- Show the base grayscale and the overlay (e.g. contour or semi-transparent mask); include a
  low-alpha fill + crisp contour so anatomy stays visible.
- Habitat maps: discrete categorical colors with a legend; keep the same color↔habitat
  mapping across the whole paper.

## Caption must define
modality/sequence, plane, WL/WW, arrows/symbols, scale, overlay meaning + colorbar units, and
that images are de-identified. (Prose → `radiology-writing`.)
