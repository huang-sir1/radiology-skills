# 多中心

Use this file when the user asks about multicenter imaging datasets, external
validation, scanner/vendor/protocol differences, center effects, harmonization,
domain shift, temporal validation, or generalizability.

## Core goal

多中心模块的目标是把“多个医院的数据”转化为可信的泛化验证，而不是简单混在一起增加样本量。

## First questions

- 有几个中心？每个中心的患者数、阳性/事件数、时间范围是多少？
- 每个中心的扫描仪厂家、型号、层厚、重建核、MRI 序列、增强期相是否一致？
- 中心之间的病例来源、治疗策略、随访方式、标签定义是否一致？
- 哪些中心用于训练，哪些用于外部验证？
- 是否有时间验证或地理验证？
- 是否计划做 harmonization、domain adaptation、federated learning，还是只做外部测试？

## Multicenter design patterns

| Pattern | Use when | Interpretation |
|---|---|---|
| pooled training + internal split | early model development | weak evidence if no center-held-out validation |
| train on center A, test on center B | true external validation | strong but may be underpowered |
| train on multiple centers, hold out one center | generalizability test | useful for center robustness |
| temporal validation | same hospital, later patients | tests time drift, not geography |
| geographic validation | different hospital/region | stronger external validity |
| federated learning | data cannot leave centers | requires strong engineering and governance |

## Center-aware split

Prefer:

1. patient-level grouping always
2. center-level external validation when possible
3. temporal holdout within major centers if enough cases
4. no same-patient leakage across centers or timepoints
5. locked preprocessing and threshold before external validation

Avoid:

- random split after pooling all centers as the only validation
- center imbalance hidden inside aggregate AUC
- tuning model based on external center performance
- reporting only average performance without center-specific failure analysis

## Harmonization and domain shift

Check:

- scanner vendor and field strength
- CT slice thickness, reconstruction kernel, contrast phase
- MRI sequence parameters and vendor-specific differences
- PET reconstruction and SUV normalization
- ultrasound operator and equipment variability
- segmentation protocol consistency

Possible approaches:

- standardize acquisition inclusion criteria
- resampling and intensity normalization
- ComBat or related harmonization for radiomics features
- domain adaptation for deep learning
- center-stratified cross-validation
- center as covariate or random effect when appropriate
- sensitivity analysis with and without harmonization

Warnings:

- Fit harmonization without leaking outcome or test information.
- Do not use external validation data to choose harmonization strategy.
- Report performance before and after harmonization if it materially changes results.

## Reporting

Methods should include:

- center names or anonymized center IDs
- patient counts and event counts per center
- acquisition parameter summary per center
- split logic by center and time
- preprocessing and harmonization details
- whether model selection used any external center information
- center-specific and pooled validation metrics

Results should include:

- overall performance
- center-specific performance
- heterogeneity or subgroup analysis
- failure center discussion
- calibration and DCA in external cohorts when possible

## Output format

```text
多中心定位
- 中心数量和分布：
- 主要差异来源：
- 目标验证类型：

推荐划分
- 训练：
- 内部验证：
- 外部/时间验证：

中心差异处理
- 图像参数：
- 标签/治疗：
- harmonization/domain shift：

报告建议
- 表格：
- 图表：
- Methods 文本：

高风险问题
- [pooled random split, center imbalance, test-center tuning]
```

## Red lines

- Do not call a pooled random split “external validation.”
- Do not hide center-specific poor performance behind a pooled AUC.
- Do not assume harmonization solves all scanner and protocol differences.
- Do not tune models on the external center and still claim independent validation.
- Do not ignore different label definitions, treatment protocols, or follow-up rules across centers.
