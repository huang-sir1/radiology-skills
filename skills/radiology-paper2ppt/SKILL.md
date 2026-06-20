---
name: radiology-paper2ppt
description: "Turn an imaging-research paper, preprint, PDF, abstract, or reading notes into a concise Chinese .pptx deck for journal club / 读片会 / 组会 / paper sharing. Use when the user wants a paper PPT, journal-club slides, 读片会/文献汇报 slides, or paper-to-slides for an imaging study. Identifies the paper type and evidence chain, selects only the figures/tables that carry the argument (imaging panels, ROC/KM/calibration), writes Chinese slide text + speaker notes, builds a real .pptx, and runs package QA. Never fabricates results, metrics, or figure details."
---

# Imaging Paper → Chinese Journal-Club Deck

Turn an imaging paper into a concise, faithful Chinese `.pptx` for 读片会 / 文献汇报 / 组会.
The deck follows the paper's **scientific argument**, not its section order.

## Core stance
- **Argument as the spine.** Classify the paper (diagnostic-accuracy / prediction model /
  radiomics / radiogenomics / review), then build the slide flow from its evidence chain.
- **Figures are evidence.** Use the paper's key figures/tables (imaging panels, ROC,
  calibration, Kaplan-Meier, forest); **crop or split** dense panels rather than shrinking
  them unreadable. Keep windowing/arrows visible for imaging panels.
- **Real `.pptx`.** Build an actual deck (use the `pptx` skill), Chinese slide text +
  speaker notes, not a text outline.
- **Integrity.** Never fabricate results, numbers, datasets, mechanisms, or figure details;
  if the source is partial, label gaps.

## When to use
- "把这篇论文做成读片会/文献汇报 PPT。" / "Make journal-club slides from this imaging paper."
- "组会要讲这篇 radiomics/AI 论文，做个中文 PPT。"

## Slide flow (adapt to paper type)
1. **标题页** — title, authors/journal/year, presenter/date.
2. **背景与临床问题** — the gap (1–2 slides).
3. **研究目的/假设**.
4. **方法** — 数据与队列 (n, source, scanner/protocol); 影像分析/参考标准/阅片;
   模型/特征流程 (radiomics: IBSI/分割/谐化; AI: 架构/划分/验证). Use a pipeline figure.
5. **主要结果** — performance **with CIs**; key figure (ROC/KM/calibration) per slide;
   comparison/validation.
6. **关键图** — the decisive imaging panel(s) or chart, cropped legibly.
7. **结论与局限** — bounded conclusion + honest limitations.
8. **点评/讨论** — presenter's critique: 报告规范 (CLAIM/CLEAR), 有无外部验证/泄漏/校准,
   可复现性, 临床意义 — a journal-club value-add (route critique points via radiology-reporting).
9. **(可选) 思考/可借鉴** — what to borrow for our own work.

## Workflow
1. Read/parse the paper (load `pdf` skill for PDFs; or `radiology-reader` for full bilingual
   extraction).
2. Classify paper type; extract the evidence chain and the figures/tables that carry it.
3. Write Chinese slide titles, bullets (concise), captions, takeaways, and **speaker notes**.
4. Build the `.pptx` (load the `pptx` skill); place cropped figures with sources.
5. **QA** — reopen/inspect the package: slide count, embedded images, notes present, no
   unreadable panels, no fabricated content.

## Output contract
1. **`.pptx`** deck (primary deliverable) — Chinese, with speaker notes.
2. **`Slide map`** — title → message → figure used, per slide.
3. **`QA`** — slide count, embedded media, notes, any rendering limits or missing source
   content.

## Handoffs
PDF/figure extraction → `pdf` / `radiology-reader`; deck construction → `pptx`; critique
points (reporting/stats) → `radiology-reporting` / `radiology-stats`.
