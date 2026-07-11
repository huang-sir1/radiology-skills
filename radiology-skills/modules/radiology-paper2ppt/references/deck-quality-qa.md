# Deck quality QA

Use this reference when building or repairing a paper-to-PPT deck, especially after the first PPTX export.

## Paper-type arc

Classify the paper before slide design:

| Type | Slide arc |
|---|---|
| Diagnostic / prediction | clinical problem -> cohort/design -> model/test -> performance -> calibration/utility -> critique |
| Radiomics | segmentation/preprocessing -> feature selection -> signature/model -> validation -> reproducibility/leakage critique |
| Radiogenomics | cohort matching -> imaging phenotype -> omics layer -> association/integration -> biological validation -> caveats |
| Deep learning | data split -> architecture -> training/baselines -> validation -> explainability/robustness -> clinical value |
| Review / meta-analysis | question -> search/screening -> evidence map -> key findings -> limitations -> takeaways |

## Terminology ledger

Maintain one ledger while building slides:

| Term | Chinese rendering | Keep literal? | Notes |
|---|---|---|---|
| dataset/model/gene/metric | ... | yes/no | first-slide definition |

Use the same Chinese term across slide titles, bullets, figure callouts, and speaker notes.

## Figure asset QA

| Check | Rule |
|---|---|
| Crop completeness | panel letters, axes, legends, scale bars, arrows, and numbers-at-risk must remain visible |
| Legibility | no important text below readable size in slideshow view |
| Splitting | split dense multipanel figures rather than shrinking them |
| Source | every figure/table slide has paper citation or page/figure source |
| Integrity | do not redraw or reinterpret values unless explicitly marked as recreated from source data |

## Layout QA

- Use a stable grid; align titles, figure frames, captions, and takeaways across slides.
- Avoid large empty areas. Let the figure occupy the slide when it carries the evidence.
- Keep one message per slide. If a slide has two conclusions, split it.
- Remove template-looking filler text and generic AI phrases.
- Speaker notes should explain what to say, not repeat slide bullets verbatim.

## Final audit table

Return this after building the PPTX:

| Item | Status | Notes |
|---|---|---|
| Slide arc matches paper type | pass / fix | ... |
| Key figures complete and legible | pass / fix | ... |
| No text overflow or overlap | pass / fix | ... |
| Chinese terminology consistent | pass / fix | ... |
| Speaker notes present | pass / fix | ... |
| No fabricated numbers or mechanisms | pass / fix | ... |
