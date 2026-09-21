# Backend and geometry QA

## Backend routing

Reuse the project's existing analysis language when possible; this preserves numerical and package
provenance.

| Need | Preferred route |
|---|---|
| General statistical plots, imaging montages, custom multi-panel assembly | Python: matplotlib/seaborn |
| Survival curves/risk tables, Cox/nomogram ecosystem already in R | R: survival/survminer/rms |
| Complex omics/radiogenomics heatmaps and annotations | R: ComplexHeatmap, or existing Python stack |
| Existing validated code in one backend | Keep that backend; do not redraw in another for style alone |

Do not mix Python and R within one figure unless the final assembly preserves identical fonts, palette,
line weights, dimensions, and source-data/value provenance.

## R publication theme

Use a restrained theme based on `theme_classic()` or `theme_minimal()` with explicit white
backgrounds for plot, panel, and legend. Set physical export size in mm/inches, base type around the
target final-size requirement, and use `ggsave(..., bg = "white", device = cairo_pdf)` for vector
output plus a 300-600 dpi TIFF/PNG.

For survival figures, align the numbers-at-risk table to the same breaks and limits as the main panel.
For nomograms, retain a coefficient/points crosswalk. For ComplexHeatmap, rasterize only the heatmap
body when necessary while keeping labels and annotations vector where possible.

## Geometry checks

The raster audit measures export properties that are easy to miss:

- corner/background whiteness and accidental transparency/dark canvas;
- bounding-box occupancy to flag excessive whitespace;
- non-white pixels touching edges as a clipping-risk signal;
- pixel dimensions and DPI metadata;
- nearly blank output.

Run:

```text
python scripts/audit_figure_export.py figure.png --require-white --min-dpi 300
```

Treat low occupancy as a prompt to inspect layout, not an automatic crop command. Some sparse plots
are scientifically appropriate. Treat edge ink as a risk, then inspect whether it is a legitimate axis
spine or clipped labels.

## Collision audit

Pixel geometry cannot reliably identify overlapping words or a legend covering data. Inspect at the
target physical size and check separately:

- all text, tick, legend, annotation, panel-letter, and numbers-at-risk bounding boxes;
- DCA labels and curves around the clinically relevant threshold range;
- heatmap labels and annotation tracks;
- figure-panel gutters and shared axes;
- any value printed both inside a bar/point and next to it.

When collision occurs, change layout, label strategy, or panel structure before reducing type size.

