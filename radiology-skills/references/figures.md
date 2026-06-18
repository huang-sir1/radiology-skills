# 图表

Use this file when the user asks how to design manuscript figures, tables, graphical
abstracts, workflow diagrams, performance plots, radiomics pipeline figures, deep
learning architecture figures, mechanism diagrams, or figure legends for imaging AI
studies.

## Core goal

图表模块的目标是让图表服务于论文论证，而不是简单堆放 ROC。先明确每张图回答什么问题，再决定图形类型。

## First questions

- 文章核心结论是什么？
- 研究类型是影像组学、深度学习、多模态、机制解析、疗效预测，还是临床转化？
- 目前已有结果有哪些：AUC、C-index、Dice、校准、DCA、KM、SHAP、Grad-CAM、机制分析？
- 是否有外部验证、多中心验证、亚组和失败案例？
- 目标期刊或文章类型是什么？
- 需要主图、补充图，还是投稿前图表审查？

## Recommended figure set

### Core clinical prediction manuscript

| Figure/Table | Purpose | Contents |
|---|---|---|
| Figure 1 | study design | patient flow, centers, splits, modeling and validation |
| Table 1 | cohort description | demographics, clinical variables, endpoints by split |
| Figure 2 | model pipeline | segmentation, feature extraction/modeling, validation |
| Table 2 | model performance | AUC/C-index, CI, sensitivity, specificity, calibration |
| Figure 3 | discrimination | ROC/PR or time-dependent AUC across cohorts |
| Figure 4 | calibration and utility | calibration curves and DCA |
| Figure 5 | interpretation | feature importance, SHAP, saliency, or mechanism evidence |
| Supplement | robustness | subgroup, sensitivity, failure cases, checklist |

### Radiomics manuscript

- ROI examples with overlay on representative images.
- Radiomics workflow: image acquisition -> segmentation -> preprocessing -> feature extraction -> feature selection -> model -> validation.
- Feature selection path: optional LASSO coefficient path or selected feature heatmap.
- Model comparison: clinical, radiomics, combined model.
- Nomogram only when clinically justified and calibrated.
- Calibration and DCA if clinical prediction is claimed.

### Deep learning manuscript

- Architecture overview without unnecessary layer-by-layer clutter.
- Data split and augmentation workflow.
- Representative saliency/Grad-CAM/attention maps only after checking plausibility.
- Segmentation examples: best, typical, and failure cases.
- External validation performance and center subgroup performance.

### Mechanism manuscript

- Evidence chain diagram: imaging phenotype -> molecular pathway -> cell type/spatial niche -> clinical endpoint.
- Heatmap or pathway enrichment for radscore-associated modules.
- Single-cell dot plot/violin/UMAP only if it answers the mechanism question.
- Spatial map linking pathway/cell state to image habitat.
- Avoid decorative omics plots disconnected from the radiomics score.

## Table standards

### Table 1

Include:

- patient count by split and center
- age, sex, disease stage or grade
- key laboratory/clinical variables
- treatment information when relevant
- endpoint distribution and follow-up
- missing values and test used for comparison

Do not overinterpret p-values comparing train/test baseline variables. The table describes
cohort balance, not causal differences.

### Model performance table

Include:

- cohort name and patient count
- model type
- AUC/C-index/Dice with 95% CI
- sensitivity, specificity, PPV, NPV at locked threshold
- calibration metric if available
- clinical model and combined model comparison
- external validation results separately

### Supplementary tables

- image acquisition parameters
- radiomics extraction parameters
- selected features and coefficients
- hyperparameters
- full checklist compliance
- excluded cases and reasons

## Figure legend checklist

Each legend should state:

- cohort or dataset
- sample size and event count
- model or feature being shown
- metric definition
- confidence interval method if plotted
- statistical test if used
- abbreviation definitions

## Common missing figures

- Patient flow diagram.
- External validation performance.
- Calibration curve.
- Decision curve analysis.
- Failure-case visualization.
- Center-specific performance.
- Figure showing how ROI was drawn.
- Supplementary table of image acquisition parameters.
- Reproducibility materials table.

## Output format

```text
图表定位
- 文章类型：
- 核心结论：
- 现有图表：

推荐主图
| 图号 | 目的 | 内容 | 需要的数据 | 风险 |

推荐表格
| 表号 | 目的 | 内容 |

补充材料
- [parameter tables, robustness figures, checklist]

Figure legend 草稿
[only when figure facts are supplied]
```

## Red lines

- Do not design figures around unsupported claims.
- Do not let ROC be the only model-evaluation figure when clinical prediction is claimed.
- Do not use saliency maps as proof of mechanism.
- Do not invent performance values or sample sizes for figure legends.
- Do not place patient-identifiable images in figures.
