# radiology-stats

面向医学影像研究的统计设计、模型评价和结果报告 skill。它帮助作者把统计问题从“该用哪个检验”推进到“这个估计、CI、p 值、校准、DCA、样本量和多重比较是否足以支撑文章结论”，并按 _Radiology_ 审稿人期望的方式报告。

## 它能做什么

- Diagnostic accuracy：sensitivity、specificity、PPV、NPV、LR 及正确 CI。
- AUC 比较：**DeLong**、bootstrap、paired McNemar。
- Reader agreement：Cohen / weighted / Fleiss kappa、ICC、Bland-Altman，以及 **MRMC** reader study。
- Prediction-model evaluation：calibration slope/intercept、Brier score、decision-curve analysis、threshold selection。
- High-dimensional radiomics / omics：Bonferroni / Holm / BH-FDR、nested CV、bootstrap optimism、leakage-aware statistics。
- Survival / prognosis：Kaplan-Meier、Cox、C-index、time-dependent ROC、competing risks。
- Sample-size / EPV / Riley minimum sample size planning。

## 参考文件

```text
references/
├── diagnostic-accuracy.md     sens/spec/PPV/NPV/LR、CI 方法、McNemar
├── model-evaluation.md        ROC/AUC、DeLong vs bootstrap、calibration、Brier、DCA、thresholds
├── agreement-mrmc.md          kappa、ICC 模型选择、Bland-Altman、MRMC
├── high-dimensional-omics.md  multiplicity、CV/nested CV、optimism、harmonisation stats
├── survival-prognostic.md     KM、Cox 假设、C-index、time-dependent AUC、competing risks
└── sample-size.md             accuracy/AUC 样本量、EPV、Riley minimum sample size
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

不会编造数值、CI 或 p 值。会区分 primary 与 exploratory analyses。绘图交给 `radiology-figure`，规范对齐交给 `radiology-reporting`。监管级研究仍应由专业生物统计师审阅。
