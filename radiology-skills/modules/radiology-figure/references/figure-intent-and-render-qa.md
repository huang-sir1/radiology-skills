# Figure intent and render QA

Use this reference when building a full figure set, revising crowded figures, preparing a graphical abstract, or fixing problems such as overlapping labels, clipped ticks, DCA layout issues, sparse whitespace, or "数字穿模".

## Figure intent table

Before drawing, define the role of each panel:

| Figure/Panel | Question answered | Claim supported | Data source | Variables | Expected pattern | Exception/risk | Manuscript location |
|---|---|---|---|---|---|---|---|
| Fig 2A | Does the model discriminate? | External AUC is clinically useful | test predictions | sensitivity/specificity | curve above comparator | CI overlap | Results primary performance |
| Fig 3B | Is the model calibrated? | Predicted risk matches observed risk | validation cohort | risk deciles | near diagonal | sparse high-risk bins | Results calibration |
| Fig 4C | Is there clinical utility? | net benefit in practical threshold range | predictions/outcome | threshold/net benefit | model above treat-all/none | axis crowding | Discussion clinical value |

If a panel has no claim, remove it or move it to supplement.

## Figure contract before code

Before plotting, write a one-line contract:

```text
This figure should convince the reader that [claim] because [visual evidence] in [cohort/data], with the caveat that [boundary].
```

If the contract cannot be written, the figure is not ready to draw. Route back to `radiology-writing` or `radiology-stats` to clarify the claim.

## WALTER narration for each panel

Use this lightweight narration to convert a chart into manuscript text:

| Step | Question |
|---|---|
| Hypothesis | What should the reader expect if the claim is true? |
| Axes | What do x, y, color, size, and facets encode? |
| Look here | Which region, threshold, subgroup, or timepoint matters most? |
| Trend | What pattern supports the claim? |
| Exception | What visible caveat, overlap, or subgroup weakens the claim? |
| Result | What exact sentence should appear in Results or the legend? |

The `Result` sentence must match the manuscript and source-data crosswalk. Do not let the figure imply a stronger claim than the text.

## Source-data crosswalk

Every published panel should be traceable:

| Figure/Panel | Source file/table | Columns used | Transform | n/events | Check status |
|---|---|---|---|---|---|
| Fig 2A | predictions_external.csv | y_true, p_model, p_clinic | ROC + bootstrap CI | n=... | pass / needs input |

For Nature-family manuscripts, prepare Source Data or equivalent tables when required.

## Caption takeaways

Each legend should contain:

1. What the panel shows.
2. What data/cohort it uses.
3. The key metric or visual takeaway.
4. Any uncertainty/CI or threshold context needed to interpret it.

Avoid legends that merely restate axis labels.

## Render QA at final size

Always inspect the exported figure at the journal's final physical size, not only in a notebook.

Checklist:

- White background for academic publication figures unless the target venue explicitly requests otherwise.
- No text overlaps, clipping, or collision between tick labels, legends, panel labels, numbers-at-risk, annotations, or inset labels.
- No text is trapped inside a shape that is too small.
- Axis labels and units remain legible at final column width.
- Legends do not cover data; if needed, use external legend columns or direct labels.
- DCA curves do not collide with threshold ticks; net-benefit labels and treat-all/treat-none labels are readable.
- Kaplan-Meier numbers-at-risk align with x-axis ticks and do not overlap row labels.
- Heatmap row/column labels are either legible, grouped, or moved to a supplemental table.
- Panel letters are placed consistently and do not touch plot borders.
- Exported SVG/PDF preserves text as text where possible; raster is at least 300 dpi.

If any item fails, revise layout, not just font size. Use a denser grid, better legend placement, shorter labels, panel splitting, or supplemental relocation.

## Academic aesthetic rules

- Prefer a white or near-white canvas and clean axes.
- Use contrast, hierarchy, and spacing instead of decorative gradients or dark backgrounds.
- Avoid excessive empty space; let panels occupy the figure area with consistent margins.
- Use one palette across the figure set, with color mapped to the same meaning everywhere.
- Let annotation serve interpretation: highlight the clinically important threshold/risk group/result, not every value.

## Final figure audit

Return these notes with the figure set:

| Item | Status | Notes |
|---|---|---|
| Figure intent table complete | pass / fail | ... |
| Source-data crosswalk complete | pass / fail | ... |
| Final-size render inspected | pass / fail | ... |
| No overlap/clipping | pass / fail | ... |
| Journal size/label case correct | pass / fail | ... |
| Data are real or simulation clearly marked | pass / fail | ... |
