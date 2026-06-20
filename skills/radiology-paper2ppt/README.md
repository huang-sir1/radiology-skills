# radiology-paper2ppt

**Imaging paper → concise Chinese `.pptx`** for journal club / 读片会 / 文献汇报 / 组会.
Follows the paper's scientific argument, uses its key figures as evidence, and adds a
journal-club critique.

## What it does
- Classifies the paper (DTA / prediction model / radiomics / radiogenomics / review) and
  builds the slide flow from its evidence chain.
- Selects and **crops** the decisive figures/tables (imaging panels with windowing/arrows;
  ROC/KM/calibration/forest charts) instead of shrinking dense panels.
- Writes Chinese slide text + **speaker notes**; builds a real `.pptx`; runs package QA.
- Adds a 点评 slide: reporting compliance (CLAIM/CLEAR), external validation/leakage/
  calibration, reproducibility, clinical relevance.

## Example prompts
- "把这篇 Radiology 论文做成读片会 PPT，中文，带演讲者备注。"
- "组会汇报这篇 radiomics 论文，重点讲方法和验证。"

## Integrity
Never fabricates results, numbers, or figure details; labels gaps if the source is partial.
Builds the deck via the `pptx` skill; extracts figures via `pdf` / `radiology-reader`.
