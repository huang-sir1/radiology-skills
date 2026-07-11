---
name: radiology-skills
description: >-
  Use when planning, auditing, writing, or revising radiomics, medical imaging AI,
  and radiology deep learning studies for Radiology/RSNA, Nature-portfolio, Lancet,
  Cell, npj, European Radiology, or similar venues. Trigger for research frontiers, literature,
  CT/MRI/PET/ultrasound datasets, ROI/masks/segmentation annotation, radiomics
  features, CNN/Transformer/foundation models, trustworthy AI, FUTURE-AI,
  uncertainty/OOD/interpretability, radiogenomics and multi-omics mechanisms,
  statistics, figures, pre-submission review, reproducibility,
  multicenter validation, public datasets, ethics/privacy, clinical translation,
  validation/leakage, CLAIM/CLEAR/RQS/IBSI/TRIPOD+AI/PROBAST+AI/STARD-AI,
  manuscript writing, journal selection, NSFC/provincial/international grants, reviewer response, and
  Chinese-English support.
---

# Radiology Skills

## Overview

Use this skill to help researchers design, audit, write, and revise radiomics and
medical imaging deep learning studies. Keep the work grounded in the user's data,
clinical question, imaging modality, target venue, validation plan, and reporting
standard.

This skill is bilingual-aware. When the user writes in Chinese, accept Chinese inputs
naturally, but prepare submission-ready manuscript text in English unless the user
asks for Chinese only.

The bundled module set covers Radiology/RSNA-style imaging manuscripts and
Nature-portfolio/npj-style imaging AI papers, plus Lancet-family, Cell Reports Medicine,
European Radiology, grant, and clinical-translation workflows where relevant. Verify
current journal, reporting, and grant requirements when the final output depends on a
live policy.

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
- If the target venue is known, apply the correct venue family: Radiology/RSNA defaults
  differ from Nature-portfolio/npj rules for abstract shape, panel-letter case, figure
  dimensions, Reporting Summary, Source Data, and reference style.

## First move

Identify the task mode, then load only the relevant reference file. If the
request needs deeper module-specific rules, load the matching internal module
under `modules/`.

| User intent | Module | Open |
|---|---|---|
| What should I ask or collect first? | 入口 | `references/intake.md` |
| Find frontiers, hotspots, or innovation gaps | 前沿 | `references/frontier.md` |
| Search, screen, or organize literature | 文献 | `references/literature.md` |
| Use curated 2023-2026 high-impact literature evidence for frontiers, project design, or journal fit | 证据 | `references/literature-evidence-2023-2026.md`, `references/frontier-patterns-2023-2026.md`, `references/journal-patterns-2023-2026.md` |
| Use TCIA, TCGA, GEO, CPTAC, IDC, or other public datasets | 公库 | `references/public-datasets.md` |
| Traditional radiomics workflow | 组学 | `references/radiomics.md` |
| Deep learning, segmentation, foundation models, uncertainty, OOD, interpretability, trustworthy AI | 深度 | `references/deep-learning.md`, and if detailed: `modules/radiology-deep-learning/SKILL.md` |
| Interpret radiomics or imaging AI models with transcriptomics, single-cell RNA-seq, spatial transcriptomics, or multi-omics data | 机制 | `references/mechanism.md` |
| Turn data into a feasible study | 设计 | `references/study-design.md` |
| Polish or restructure NSFC/provincial/institutional/international grant proposals for imaging AI projects | 基金 | `references/grant-writing.md`, and if international eligibility is involved: `modules/radiology-grant/SKILL.md` |
| Plan or audit ROI, VOI, masks, readers, segmentation annotation, and reader agreement | 标注 | `references/annotation.md` |
| Plan or audit sample size, feature selection, modeling statistics, metrics, survival analysis, calibration, and DCA | 统计 | `references/statistics.md` |
| Check validation, leakage, metrics, calibration | 验证 | `references/validation.md` |
| Handle multicenter data, center effects, harmonization, domain shift, or center-held-out validation | 多中心 | `references/multicenter.md` |
| Pick reporting checklist or audit compliance | 规范 | `references/checklists.md` |
| Data, privacy, DICOM/NIfTI/ROI/masks, sharing | 数据 | `references/data.md` |
| Ethics approval, consent waiver, privacy, and data-use limitations | 伦理 | `references/ethics.md` |
| Reproducibility, code, feature tables, model parameters, and supplementary materials | 复现 | `references/reproducibility.md` |
| Manuscript wording and structure | 写作 | `references/writing.md` |
| Design manuscript figures, tables, legends, graphical workflows, or venue-specific figure sets | 图表 | `references/figures.md`, and if target venue is Nature/npj/Lancet/Cell/European Radiology: `modules/radiology-figure/SKILL.md` |
| Simulate reviewer/methodology pre-submission audit before journal submission | 预审 | `references/pre-submission.md` |
| Choose target journals and submission tiers after a manuscript is drafted | 选刊 | `references/journal-selection.md` |
| Clinical utility, reader study, prospective validation, workflow integration, or deployment framing | 转化 | `references/clinical-translation.md` |
| Reviewer response and revision strategy | 回复 | `references/response.md` |
| Chinese author notes and terminology | 中文 | `references/chinese.md` |
| Guideline/source provenance | 依据 | `references/sources.md` |

## Internal modules

Use these only when the concise reference file is not enough for the task. Each
module is bundled inside this same `radiology-skills` skill; do not ask the user
to install it separately.

| Task need | Open for detailed rules |
|---|---|
| Frontier direction and publication-pattern evidence | `modules/radiology-frontier/SKILL.md` |
| Study feasibility and validation design | `modules/radiology-design/SKILL.md` |
| Literature, public dataset, DOI/PMID, or source search | `modules/radiology-search/SKILL.md` |
| ROI, VOI, mask, segmentation, reader protocol, or annotation QC | `modules/radiology-annotation/SKILL.md` |
| Data availability, DICOM de-identification, repositories, or FAIR | `modules/radiology-data/SKILL.md` |
| Ethics, consent, privacy, or data governance | `modules/radiology-ethics/SKILL.md` |
| Hand-crafted radiomics and IBSI/CLEAR workflows | `modules/radiology-radiomics/SKILL.md` |
| CNN, Transformer, foundation model, segmentation, interpretability, uncertainty, OOD, or trustworthy deep-learning design | `modules/radiology-deep-learning/SKILL.md` |
| Radiogenomics, transcriptomics, single-cell, spatial, or multi-omics mechanism | `modules/radiology-radiogenomics/SKILL.md` |
| ROC, calibration, DCA, MRMC, survival, sample size, or high-dimensional statistics | `modules/radiology-stats/SKILL.md` |
| Publication figures, Radiology/Nature/Lancet/European-style charts, or imaging panels | `modules/radiology-figure/SKILL.md` |
| CLAIM, TRIPOD+AI, CLEAR, RQS/RQS 2.0, IBSI, STARD, PRISMA-DTA, PROBAST, FUTURE-AI, Nature Reporting Summary, or compliance audit | `modules/radiology-reporting/SKILL.md` |
| Manuscript drafting or section reconstruction for Radiology, Nature, Lancet, Cell, European Radiology, or npj-style venues | `modules/radiology-writing/SKILL.md` |
| Radiology/Nature-family English polishing and statistical style | `modules/radiology-polishing/SKILL.md` |
| Full-paper bilingual reading | `modules/radiology-reader/SKILL.md` |
| Citation retrieval or reference export | `modules/radiology-citation/SKILL.md` |
| Pre-submission mock review | `modules/radiology-prereview/SKILL.md` |
| Journal selection and submission tiering | `modules/radiology-journal/SKILL.md` |
| Reviewer response and revision strategy | `modules/radiology-response/SKILL.md` |
| Clinical translation, reader study, prospective validation, or deployment | `modules/radiology-translation/SKILL.md` |
| NSFC, provincial, institutional, NIH/ERC/Wellcome-style grant writing and eligibility triage | `modules/radiology-grant/SKILL.md` |
| Imaging paper to Chinese journal-club PPT | `modules/radiology-paper2ppt/SKILL.md` |

## Standard workflow

1. **Route.** Classify the request as `frontier`, `literature`, `radiomics`,
   `public-datasets`, `radiomics`, `deep-learning`, `mechanism`, `study-design`,
   `grant-writing`, `annotation`, `statistics`, `validation`, `multicenter`,
   `checklist`, `data`, `ethics`, `reproducibility`, `writing`, `figures`,
   `pre-submission`, `journal-selection`, `clinical-translation`, `response`,
   or `mixed`.
2. **Build the study card.** Capture disease, modality, sample size, centers,
   labels, endpoint, segmentation, data format, split plan, external validation,
   clinical variables, annotation details, target venue or funding scheme, statistics
   plan, ethics/sharing limits, and intended output.
3. **Choose the strictest useful path.** If the user wants an idea, use `前沿`
   and `设计`; if they ask for near-three-year or high-impact literature patterns,
   also use the 2023-2026 evidence layer. If the user has a draft or methods section,
   use `验证`, `规范`, and the relevant technical module.
   If the user names a target journal family, load the corresponding module branch
   instead of applying Radiology defaults blindly.
4. **Expose risks early.** Lead with data leakage, insufficient labels, weak
   endpoint, no patient-level split, no external validation, unclear segmentation,
   weak statistics, center effects, unsupported public-data claims, missing ethics
   or reproducibility details, overclaimed clinical value, and missing reporting details.
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

For grant proposal polishing, return:

```text
基金申报定位
- 项目类型：
- 核心科学问题：
- 当前短板：

结构补强
- 立项依据：
- 研究目标/内容：
- 技术路线：
- 创新点：
- 可行性/研究基础：
申请资格/政策核验
- [only for international or policy-sensitive schemes; do not assume eligibility]

润色稿
[only rewrite supplied text; do not invent preliminary data]

需要作者确认
- [missing facts before final proposal text]
```

For mechanism/radiogenomics interpretation, return:

```text
机制解析定位
- 影像模型：
- 可用组学：
- 核心生物学问题：

整合路线
- bulk RNA：
- 单细胞：
- 空间转录组：
- 其他组学：

证据链
- 影像表型 -> 分子通路 -> 细胞类型/空间生态位 -> 临床终点

风险和限制
- [matching, batch, multiple testing, causality, validation]
```

For annotation/statistics/figures/pre-submission/reproducibility/multicenter/public
datasets/ethics/clinical translation, return the module-specific structure from the
loaded reference file. If multiple modules are loaded, merge them into one concise
action package:

```text
任务定位
- 主模块：
- 相关模块：
- 当前最大风险：

分模块建议
| 模块 | 关键判断 | 必须补充 | 建议动作 |

可直接使用内容
[only when facts are supplied]

需要作者确认
- [specific missing facts]
```

## Scripts

- `scripts/radiology_audit.py`: quick Markdown audit from a JSON study card.
- `scripts/split_leakage_check.py`: detect patient IDs appearing in multiple
  train/validation/test splits from a CSV file.

Scripts are helpers, not substitutes for manual scientific judgment.

## Red lines

- Do not recommend a frontier method just because it is popular.
- Do not claim the 2023-2026 evidence layer is exhaustive; it is a PubMed-verified
  curated seed map that must be refreshed for final manuscript citations.
- Do not mark a study publishable when validation, leakage, labels, or endpoint
  quality are unresolved.
- Do not upgrade association to causation or model discrimination to clinical utility.
- Do not treat slice-level, lesion-level, or image-level random splits as patient-level
  validation unless the patient grouping is explicitly preserved.
- Do not write final claims from placeholder performance numbers.
- Do not promise acceptance or rank journals only by impact factor.
- Do not invent grant preliminary results, team expertise, publications, ethics approvals,
  equipment, funded projects, collaborations, or official guideline requirements.
- Do not claim biological mechanism from correlation alone; distinguish association,
  mediation, validation, and causal evidence.
- Do not accept unclear ROI/mask annotation, reader workflow, or segmentation QC as
  adequate methods.
- Do not fabricate statistical values, event counts, confidence intervals, cut-offs,
  reader agreement metrics, IRB details, public dataset IDs, code repositories, or
  availability statements.
- Do not call pooled random multicenter splits external validation.
- Do not present unpaired public datasets as direct validation of a user's model.
- Do not recommend public sharing of identifiable imaging, clinical, or omics data.
- Do not claim clinical readiness, workflow benefit, or patient outcome improvement
  from retrospective model performance alone.
- Do not assume NIH, ERC, Wellcome, or other international grant eligibility for a
  China-based applicant or institution; verify the current funder rules first.
- Do not apply Radiology/AMA style rules to a Nature-family manuscript without checking
  venue-specific instructions.
