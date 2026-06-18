---
name: radiology-skills
description: >-
  Use when planning, auditing, writing, or revising radiomics, medical imaging AI, and
  radiology deep learning studies. Trigger for requests about imaging research frontiers,
  topic selection, CT/MRI/PET/ultrasound datasets, DICOM/NIfTI/ROI/masks, radiomics
  features, deep learning classification/segmentation/prognosis, multimodal models,
  external validation, data leakage, CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI,
  STARD-AI, METRICS, manuscript Methods/Results/Discussion, target journal selection,
  journal fit, submission strategy, reviewer response, or Chinese-to-English radiology
  manuscript support.
---

# Radiology Skills

## Overview

Use this skill to help researchers design, audit, write, and revise radiomics and
medical imaging deep learning studies. Keep the work grounded in the user's data,
clinical question, imaging modality, validation plan, and reporting standard.

This skill is bilingual-aware. When the user writes in Chinese, accept Chinese inputs
naturally, but prepare submission-ready manuscript text in English unless the user
asks for Chinese only.

## Default stance

- Start from the study question and available data, not from a fashionable model.
- Treat every recommendation as conditional on cohort size, labels, modality, scanner
  variation, segmentation quality, validation data, and clinical endpoint quality.
- Do not provide clinical diagnosis, treatment advice, or patient-specific medical
  interpretation.
- Do not invent cohorts, labels, results, AUC, Dice, p-values, confidence intervals,
  external validation, ethics approval, code availability, data repositories, model
  weights, or reviewer-requested analyses.
- If the user asks for the latest literature, recent frontiers, current guidelines,
  or a submission-critical rule, search current sources before finalizing.

## First move

Identify the task mode, then load only the relevant reference file.

| User intent | Module | Open |
|---|---|---|
| What should I ask or collect first? | 入口 | `references/intake.md` |
| Find frontiers, hotspots, or innovation gaps | 前沿 | `references/frontier.md` |
| Search, screen, or organize literature | 文献 | `references/literature.md` |
| Traditional radiomics workflow | 组学 | `references/radiomics.md` |
| Deep learning, segmentation, foundation models | 深度 | `references/deep-learning.md` |
| Turn data into a feasible study | 设计 | `references/study-design.md` |
| Check validation, leakage, metrics, calibration | 验证 | `references/validation.md` |
| Pick reporting checklist or audit compliance | 规范 | `references/checklists.md` |
| Data, privacy, DICOM/NIfTI/ROI/masks, sharing | 数据 | `references/data.md` |
| Manuscript wording and structure | 写作 | `references/writing.md` |
| Choose target journals and submission tiers after a manuscript is drafted | 选刊 | `references/journal-selection.md` |
| Reviewer response and revision strategy | 回复 | `references/response.md` |
| Chinese author notes and terminology | 中文 | `references/chinese.md` |
| Guideline/source provenance | 依据 | `references/sources.md` |

## Standard workflow

1. **Route.** Classify the request as `frontier`, `literature`, `radiomics`,
   `deep-learning`, `study-design`, `validation`, `checklist`, `data`, `writing`,
   `journal-selection`, `response`, or `mixed`.
2. **Build the study card.** Capture disease, modality, sample size, centers,
   labels, endpoint, segmentation, data format, split plan, external validation,
   clinical variables, and intended output.
3. **Choose the strictest useful path.** If the user wants an idea, use `前沿`
   and `设计`. If the user has a draft or methods section, use `验证`, `规范`,
   and the relevant technical module.
4. **Expose risks early.** Lead with data leakage, insufficient labels, weak
   endpoint, no patient-level split, no external validation, unclear segmentation,
   overclaimed clinical value, and missing reporting details.
5. **Return an actionable package.** Provide recommended study question, method
   route, validation plan, reporting checklist, missing fields, and next actions.

## Output contract

For project design, return:

```text
Study card
- Disease / modality / task:
- Data and labels:
- Current constraint:

Recommended direction
- Research question:
- Why it is timely:
- Model/method route:
- Validation route:
- Main metrics:
- Risks:
- Next actions:
```

For audit/revision, return:

```text
Blocking issues
- [high-risk items first]

Revision plan
- [what to change and where]

Missing information
- [specific facts the author must supply]

Ready-to-use text
[only when enough facts are supplied]
```

For journal selection, return:

```text
投稿定位
- 文章类型：
- 核心卖点：
- 最大短板：

期刊梯队
| 梯队 | 期刊 | 匹配理由 | 需要补强 | 风险 |

投稿前修改建议
- [title/abstract/methods/results/discussion/data-code fixes]

需要作者确认
- [missing facts before final journal advice]
```

## Scripts

- `scripts/radiology_audit.py`: quick Markdown audit from a JSON study card.
- `scripts/split_leakage_check.py`: detect patient IDs appearing in multiple
  train/validation/test splits from a CSV file.

Scripts are helpers, not substitutes for manual scientific judgment.

## Red lines

- Do not recommend a frontier method just because it is popular.
- Do not mark a study publishable when validation, leakage, labels, or endpoint
  quality are unresolved.
- Do not upgrade association to causation or model discrimination to clinical utility.
- Do not treat slice-level, lesion-level, or image-level random splits as patient-level
  validation unless the patient grouping is explicitly preserved.
- Do not write final claims from placeholder performance numbers.
- Do not promise acceptance or rank journals only by impact factor.
