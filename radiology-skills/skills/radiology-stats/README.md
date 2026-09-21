# radiology-stats

面向医学影像研究的统计设计、模型评价和结果报告 skill。它帮助作者把统计问题从“该用哪个检验”推进到“这个估计、CI、p 值、校准、DCA、样本量和多重比较是否足以支撑文章结论”，并按 _Radiology_ 审稿人期望的方式报告。

## 它能做什么

- Diagnostic accuracy：sensitivity、specificity、PPV、NPV、LR 及正确 CI。
- AUC 比较：**DeLong**、bootstrap、paired McNemar。
- Reader agreement：Cohen / weighted / Fleiss kappa、ICC、Bland-Altman，以及 **MRMC** reader study。
- Prediction-model evaluation：calibration slope/intercept、Brier score、decision-curve analysis、threshold selection。
- High-dimensional radiomics / omics：Bonferroni / Holm / BH-FDR、nested CV、bootstrap optimism、leakage-aware statistics。
- Survival / prognosis：Kaplan-Meier、Cox、C-index、time-dependent ROC、competing risks。
- Meta-analysis inference：通用/依赖效应随机效应模型、DTA bivariate/HSROC、比例/发生率、HR/OR/RR、ICC/kappa/agreement、prediction performance/calibration。
- Experimental inference/power：连续、二元、计数端点，donor/litter/cage/cluster 分配，重复测量/混合模型、attrition 和输入驱动功效/精度规划。
- Sample-size / power / precision：基于 estimand、方差/基线率、聚类、重复测量和可接受精度，不使用通用 EPV/事件数/重复数阈值。

## 参考文件

```text
references/
├── diagnostic-accuracy.md                 sens/spec/PPV/NPV/LR、CI 方法、McNemar
├── model-evaluation.md                    ROC/AUC、DeLong vs bootstrap、calibration、Brier、DCA、thresholds
├── incremental-value.md                   联合模型 vs 组件模型的增量证明（LRT、ΔAUC、校准、DCA、NRI/IDI 纪律）
├── agreement-mrmc.md                      kappa、ICC 模型选择、Bland-Altman、MRMC
├── high-dimensional-omics.md              multiplicity、CV/nested CV、optimism、harmonisation stats
├── survival-prognostic.md                 KM、Cox 假设、C-index、time-dependent AUC、competing risks
├── sample-size.md                         输入驱动的 accuracy/AUC/prediction/MRMC 样本量、功效和精度
├── analysis-hierarchy-and-missingness.md  多病灶/多时点/多读者层级、嵌套/重复数据、缺失数据、排除与分析计划偏离
├── meta-analysis-inference.md             meta-analysis 模型、依赖效应、异质性、敏感性和停止门
└── experimental-inference-and-power.md    实验端点、分配层级、混合模型、attrition 和功效输入
```

## 常用计算环境

Python：`numpy scipy pandas scikit-learn statsmodels lifelines`。  
R：`pROC`、`irr`、`rms`、`dcurves`、`RJafroc`（MRMC）等。

## 典型触发

- “同一批 300 例上比较两个 ROC 曲线，并写出结果句。”
- “3 位读者测量连续大小，ICC 应该用哪个模型？”
- “1200 个 radiomic features、90 个病例，怎样处理多重比较和过拟合？”
- “设计 6 名读者的 AI-vs-no-AI MRMC reader study。”
- “要证明 sensitivity ≥ 0.90，prevalence 0.15，需要多少样本？”

## 边界

不会编造数值、CI、p 值、协方差、ICC、方差、基线率、attrition 或样本量输入。所有请求至少返回可执行 statistical brief；条件不足时使用 `BIOSTATISTICIAN_REQUIRED`，不伪装成已计算结果。绘图交给 `radiology-figure`，规范对齐交给 `radiology-reporting`。监管级研究仍应由专业生物统计师审阅。
