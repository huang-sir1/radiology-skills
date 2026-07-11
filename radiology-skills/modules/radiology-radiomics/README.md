# radiology-radiomics

面向手工放射组学研究的 IBSI / CLEAR 对齐设计与审计 skill。它帮助作者把“提取一堆特征做模型”变成可复现、可报告、可经受审稿的 pipeline，并重点排查训练集外泄、特征筛选 double dipping、参数缺失和样本量不足等问题。

## 它能做什么

- 设计 **pipeline spec**：preprocessing、feature extraction、feature selection、modelling、validation，并标出每一步的 leakage control。
- 规范 **IBSI-compliant parameters**：resampling、intensity normalisation、gray-level discretisation、filters、feature families、software + version、PyRadiomics parameter file。
- 规划 **leakage-safe selection & modelling**：ICC / variance / correlation / LASSO / mRMR 均在 training folds 内完成，结合 EPV-aware models、radiomics signature / score 和 nomogram。
- 执行 **leakage audit**：patient-level split、fit-on-training、tuning、reproducibility、evaluation。
- 输出 CLEAR / IBSI aligned Methods 段落。

## 典型触发

- “帮我设计/审查影像组学流程，要求 PyRadiomics 和 IBSI 规范。”
- “bin width 还是 bin count？重采样和滤波参数怎么写？”
- “LASSO 特征筛选怎么避免 leakage？”

## 参考文件

| File | 用途 |
|---|---|
| `references/preprocessing-ibsi.md` | 重采样、归一化、离散化、滤波、IBSI 报告 |
| `references/feature-extraction.md` | 特征家族、PyRadiomics 设置、参数文件 |
| `references/selection-modelling.md` | 训练内筛选、建模、signature / score、EPV |
| `references/leakage-audit.md` | radiomics leakage checklist |

## 下游衔接

`radiology-annotation`（mask 与稳定性）· `radiology-reporting`（IBSI / CLEAR / METRICS / RQS）· `radiology-stats`（CV、calibration、DCA、多重比较、样本量）· `radiology-deep-learning`（deep-feature 对照）· `radiology-radiogenomics`（生物学机制）· `radiology-figure`（ROC、calibration、nomogram）。
