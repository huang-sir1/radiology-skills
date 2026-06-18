# Test: annotation, statistics, figures, pre-submission, and reproducibility modules

## Input

```text
我有一篇肺结节 CT 影像组学文章，ROI 是两位医生手工勾画的，没有写清楚分歧怎么处理。统计部分用了 LASSO 和 logistic 回归，但没有说明是否只在训练集筛特征。图里只有 ROC，没有校准曲线和 DCA。投稿前帮我完整预审一下，并告诉我代码、特征表和参数怎么整理到补充材料里。
```

## Expected behavior

- Use `标注`, `统计`, `图表`, `预审`, `复现`, plus `组学`, `验证`, and `规范` when needed.
- Ask for ROI strategy, reader experience, blinding, repeat annotation, ICC/Dice, split plan, and external validation if missing.
- Identify feature-selection leakage, missing calibration, missing decision-curve analysis, and incomplete reproducibility reporting.
- Produce a prioritized pre-submission risk list and concrete manuscript/table/figure fixes.
- Recommend reproducibility materials: data dictionary, radiomics extraction parameters, feature table, code environment, random seeds, model coefficients, and availability statements.

## Forbidden behavior

- Do not accept unclear segmentation as sufficient.
- Do not treat ROC-only reporting as enough for clinical prediction.
- Do not suggest sharing patient-identifiable DICOM data.
- Do not invent reader agreement values, model coefficients, ethics approval, or code repositories.
