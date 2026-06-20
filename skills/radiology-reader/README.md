# radiology-reader

**Full-paper bilingual (中英对照), figure/table-aware, source-grounded Markdown reader** for
imaging-research papers. Default output is a paragraph-level original/translation companion —
never a summary-only dump.

## What it does
- Whole-paper 中英对照 at block level, preserving Methods/statistics detail.
- Extracts and **places figures/tables near their first mention**, cropped tightly —
  imaging panels (with windowing/arrows), result charts (ROC/KM/forest/calibration), and
  cohort/scanner/performance tables.
- Stable source anchors on every block; `source_map.json` for traceability.
- Imaging-tuned reading notes (what metric/CI/window to inspect in each figure).

## Outputs
`paper.md` (primary) · `source_map.json` · `translation_notes.md` · `assets/`
(optional `reader.html` only if a browser preview is requested).

## Example prompts
- "把这篇 Radiology 论文做成中英对照全文阅读。"
- "Translate this radiomics paper into a full markdown reader, keep the Methods detail."
- "Read this paper and place the ROC and KM figures next to where they're discussed."

## Handoffs
PDF extraction → `pdf` skill; references export → `radiology-citation`; journal-club slides →
`radiology-paper2ppt`.
