---
name: radiology-reader
description: "Build full-paper Chinese-English side-by-side (中英对照), figure/table-aware, source-grounded Markdown readers for imaging-research papers from PDF, DOI, arXiv, publisher HTML, or pasted text. Use whenever the user asks to translate or read an imaging paper, make 中英文对照/原文对照/全文翻译解读, extract figures/tables (including imaging panels and result charts) into the right positions, or keep exact source anchors. Especially attentive to radiology specifics: imaging figures, ROC/forest/KM charts, radiomics/AI methods detail, scanner/protocol tables, and statistical reporting. Must not degrade into a summary-only output unless the user explicitly asks for a summary."
---

# Full-Paper Markdown Reader (imaging-tuned)

Turn an imaging-research paper into a complete, bilingual, source-grounded Markdown reading
artifact. The default output is a paragraph-level **中英对照** companion — not a summary.

## Non-negotiable defaults
When the user asks to read/translate a paper, or says `中英对照 / 原文对照 / 全文翻译 / paper
reader`, produce a **paragraph-level bilingual reader** by default. Do **not** replace it with
a Chinese-only summary, a highlights list, or captions without figure crops.

## What to preserve (and why it matters for imaging papers)
- Full prose, paragraph structure, and section flow (incl. **Materials and Methods** detail —
  scanner/protocol, segmentation, model/feature pipeline, **statistical analysis**).
- Original + faithful Chinese translation at block level; keep technical terms, gene/model
  names, units, p-values, CIs, and citation markers intact.
- **Figures and tables placed near their first substantive mention.** Crop tightly:
  - **Imaging panels** — keep windowing/arrow annotations visible; note the modality/sequence.
  - **Result charts** (ROC, calibration, forest, Kaplan-Meier, DCA) — keep axes/legend legible.
  - **Tables** (cohort characteristics, scanner parameters, performance) — keep near the
    interpreting paragraph.
- Stable anchors on every block (`S###` body, `C###` captions, `F###` figures, `T###` tables).

## Workflow
1. **Identify source & paper type** (DTA / prediction model / radiomics / radiogenomics /
   review) — this sets how tightly to couple text, figures, and stats.
2. **Build a full source map** before translating (page, block type, original, translation,
   reading order, nearby figure/table, confidence). Process the **whole** document, not just
   the abstract.
3. **Translate conservatively** — meaning not style; keep Methods/stats detail; mark
   uncertain OCR rather than guessing; never drop limitations / data-availability / ethics.
4. **Extract & place figures/tables** at first substantive mention; tight crops; keep caption
   + Chinese caption; add a one-line **reading note** (what to inspect — e.g. "AUC and CI in
   panel A; calibration in panel B").
5. **Generate `paper.md`** (primary) + `source_map.json` + `translation_notes.md` + `assets/`.
   Add a terminology table for recurring imaging/AI terms.
6. **Answer follow-ups from the source** with block IDs + page numbers; don't answer from
   memory.

## Block shapes
```markdown
<a id="S001"></a>
**Source:** p.1 S001
**Original:** [source paragraph]
**中文:** [faithful translation]
```
```markdown
<a id="F001"></a>
### Fig 1. [short translated title]
**Placed near:** p.3 S012  **Source:** p.4 C001
![Fig 1](assets/fig1.png)
**Original caption:** [...]
**中文图注:** [...]
**Reading note:** [what to inspect — e.g. modality/window; which metric/CI]
```

## Output contract
- `paper.md` with `**Original:**`/`**中文:**` pairs for all substantive blocks.
- Every figure/table in `assets/` has a Markdown block + source pointer; every link resolves.
- `source_map.json` parses; `translation_notes.md` records skipped/uncertain/draft content.
- Don't hide missing content — label draft mode.

## Tooling & handoffs
- PDF extraction/OCR → load the `pdf` skill first.
- Citation export of the paper's references → `radiology-citation`.
- Want a journal-club deck instead → `radiology-paper2ppt`.
- Quality bar: feels like a paper reader, not a machine-translation dump; reader can move
  between original ↔ translation ↔ source location ↔ figure/table evidence.
