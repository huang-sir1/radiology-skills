# 预审

Use this file when the user asks for pre-submission review, simulated reviewer
critique, manuscript risk audit, top-journal readiness, or final checks before
submitting a radiomics or medical imaging AI manuscript.

## Core goal

预审模块要像审稿人和方法学编辑一样工作：先找会导致拒稿或大修的硬伤，再给可执行修改方案。

## First questions

- 目标期刊或期刊梯队是什么？
- 文章题目、摘要、Methods、Results 和 Discussion 是否已有？
- 研究是单中心、多中心、外部验证、前瞻性还是回顾性？
- 主要终点、样本量、事件数、模型性能和验证方式是什么？
- 是否有伦理、数据可用性、代码可用性、报告 checklist？
- 作者最担心的问题是什么：外部验证、样本量、模型新颖性、临床价值，还是机制解释？

## Audit priority

### Level 1: possible rejection-level issues

- no clear clinical question
- no patient-level split
- train/test leakage
- feature selection before splitting
- no independent validation despite strong claims
- unclear endpoint or label source
- unclear segmentation or no mask QC
- very small event count with complex model
- unsupported clinical utility claim
- missing ethics approval/waiver statement
- fabricated or unverifiable data/code availability

### Level 2: major revision issues

- no calibration
- no DCA when clinical decision support is claimed
- no confidence intervals
- no baseline clinical model
- no comparison with combined clinical-imaging model
- weak external validation description
- incomplete image acquisition details
- incomplete radiomics extraction parameters
- incomplete deep learning training details
- no limitations addressing retrospective design and generalizability

### Level 3: polish and positioning

- title overclaims clinical deployment
- abstract conclusion stronger than results
- discussion repeats results without explaining clinical meaning
- figures do not support narrative
- tables missing cohort counts or event counts
- terminology inconsistent
- checklist not cited or incompletely addressed

## Target-journal readiness

For high-impact journals, check whether the manuscript has at least several of:

- clinically meaningful question
- multicenter or external validation
- transparent and leakage-resistant methods
- calibrated prediction and decision-curve analysis
- clinically interpretable comparison to standard variables or radiologists
- prospective, reader-study, or workflow evidence for translation
- data/code/model transparency appropriate to privacy constraints
- careful limitations and no deployment overclaim

Do not promise suitability for a journal based only on AUC.

## Output format

```text
投稿前预审结论
- 当前档位：
- 最大硬伤：
- 最容易补强的点：

高风险问题
| 优先级 | 问题 | 为什么危险 | 建议修改 |

Methods 必改
- [data split, segmentation, preprocessing, model, validation, ethics]

Results 必补
- [CI, calibration, DCA, subgroup, external validation, failure cases]

Discussion 降调
- [overclaims and limitations]

投稿前清单
- [checklist, data/code availability, figures, tables, cover letter points]
```

## Revision language

Use direct wording:

- “This is a likely reviewer concern because...”
- “This claim should be softened unless...”
- “This analysis should be moved from exploratory to supplementary unless...”
- “The manuscript should not claim clinical readiness without...”

## Red lines

- Do not rubber-stamp a manuscript as ready when validation or leakage is unresolved.
- Do not hide limitations by wording.
- Do not invent analyses, ethics approval, external validation, or code availability.
- Do not recommend a top-tier target without explicitly stating validation and clinical-utility gaps.
- Do not treat checklist compliance as a substitute for sound study design.
