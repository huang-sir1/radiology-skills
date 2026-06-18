# 统计

Use this file when the user asks about statistical analysis plans, sample size,
feature selection, modeling, metrics, survival analysis, calibration, decision curve
analysis, confidence intervals, or statistical reporting for radiomics and medical
imaging AI studies.

## Core goal

统计模块的目标是把模型结果从“看起来 AUC 很高”变成“设计、分析和报告都可审查”。优先检查
数据单位、事件数、验证方式、特征筛选位置、指标完整性和结论强度。

## First questions

- 研究任务是诊断、分型、分期、预后、复发、疗效预测、分割，还是检测？
- 统计单位是 patient、lesion、slice、scan、time point，还是 patch？
- 样本量、阳性/阴性数量、事件数、删失比例、随访时间是多少？
- 训练、验证、测试、外部验证如何划分？是否按患者级和中心级划分？
- 特征筛选、标准化、缺失值填补、ComBat、阈值选择发生在哪个数据集内？
- 模型有哪些：临床模型、影像组学模型、深度学习模型、联合模型？
- 主要指标和预设主要终点是什么？
- 是否有校准、DCA、置信区间、敏感性分析和亚组分析？

## Study type to analysis route

| Task | Core model families | Main metrics | Must check |
|---|---|---|---|
| Binary classification | logistic regression, SVM, RF, XGBoost, neural net | AUC, sensitivity, specificity, PPV, NPV, calibration, DCA | threshold selection and leakage |
| Multiclass classification | multinomial models, tree ensembles, deep learning | macro/micro AUC, F1, balanced accuracy, confusion matrix | class imbalance |
| Prognosis | Cox, penalized Cox, RSF, DeepSurv | C-index, time-dependent AUC, calibration, KM | events per variable and censoring |
| Treatment response | logistic/Cox, delta-radiomics, longitudinal models | AUC, ORR/pCR metrics, PFS/OS metrics | response definition and time window |
| Segmentation | U-Net variants, nnU-Net, SAM-style models | Dice, IoU, Hausdorff, surface Dice | test-set independence and small lesions |
| Detection | detection networks, CAD pipelines | FROC, sensitivity per lesion, false positives per scan | lesion-level vs patient-level reporting |

## Sample size and events

- Start from number of patients, not number of images or slices.
- For binary prediction, report class counts and event fraction.
- For survival analysis, report number of events, median follow-up, censoring rate.
- For radiomics feature models, high-dimensional features require aggressive internal validation and shrinkage.
- Avoid many predictors with few events; if events are limited, prefer simpler models, fewer features, penalization, or prespecified features.
- Do not claim adequate power without a study-specific calculation or rationale.

## Leakage-sensitive pipeline

Every preprocessing or selection step must be fit inside training data only:

1. Split by patient first.
2. Fit imputation on training data.
3. Fit scaling/normalization on training data.
4. Fit harmonization parameters without leaking test labels; be cautious with ComBat.
5. Run feature stability filtering using training data or prespecified reproducibility data.
6. Run univariable screening, correlation filtering, LASSO/mRMR/RFE only inside training folds.
7. Tune hyperparameters inside validation or inner cross-validation.
8. Lock the final model before touching the test set.
9. Use external validation only once for final assessment.

## Feature selection

Common options:

- Variance or near-zero variance filter.
- Reproducibility filter by ICC.
- Correlation filter for redundancy.
- mRMR or mutual information.
- LASSO or elastic net.
- Recursive feature elimination.
- Tree-based importance.
- Clinical-prior feature set.

Warnings:

- Do not run feature selection on the full dataset before splitting.
- Do not report selected features as biologically important without stability or external evidence.
- Do not select features based on test-set performance.
- Repeat selection inside every resampling fold when reporting cross-validation performance.

## Metrics and reporting

### Classification

Minimum:

- AUC with 95% CI
- sensitivity, specificity, PPV, NPV
- threshold selection method
- confusion matrix
- calibration curve or calibration slope/intercept
- decision curve analysis when clinical utility is claimed

Optional:

- PR-AUC for imbalanced data
- Brier score
- net reclassification improvement only when justified
- subgroup analysis by center, scanner, stage, sex, age, treatment

### Survival

Minimum:

- C-index with 95% CI
- time-dependent AUC at clinically meaningful time points
- calibration at fixed time points
- hazard ratio with CI if risk groups are used
- Kaplan-Meier curves with number at risk
- proportional hazards assumption check when using Cox

Do not dichotomize risk score by an optimized full-cohort cut-off. If a cut-off is used,
derive it in training data and apply unchanged to validation data.

### Segmentation and detection

- Report patient-level and lesion-level metrics separately when both are relevant.
- Include confidence intervals or bootstrap uncertainty.
- Report failure cases and small-lesion performance if clinically important.
- Do not use validation data for model selection and then call it an independent test set.

## Output format

```text
统计定位
- 任务类型：
- 分析单位：
- 样本量/事件数：
- 当前模型：

主要风险
- [leakage, low events, class imbalance, missing calibration, weak validation]

推荐统计路线
- 数据划分：
- 特征筛选：
- 模型：
- 指标：
- 敏感性/亚组：

Methods/Results 需要补充
- [specific missing details]

需要作者确认
- [numbers and analysis facts]
```

## Red lines

- Do not equate image/slice count with independent sample size.
- Do not allow feature selection, scaling, imputation, or threshold tuning on test data.
- Do not treat AUC alone as sufficient evidence of clinical value.
- Do not fabricate p-values, confidence intervals, event counts, cut-offs, or sample-size calculations.
- Do not recommend complex models when event count and validation design cannot support them.
