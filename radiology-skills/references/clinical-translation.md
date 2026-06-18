# 转化

Use this file when the user asks about clinical translation, clinical utility, reader
studies, prospective validation, workflow integration, deployment, PACS/RIS reporting,
decision support, implementation barriers, or real-world evaluation of radiomics and
medical imaging AI models.

## Core goal

转化模块的目标是把模型从“回顾性预测性能”推进到“可能改变临床流程”的证据设计。临床转化不是一句
“可用于临床”，而是使用场景、用户、阈值、收益、风险和前瞻验证的组合。

## First questions

- 模型服务哪个临床决策：筛查、诊断、分型、分期、预后、疗效、随访、手术/放疗计划？
- 使用者是谁：放射科医生、临床医生、MDT、研究者，还是自动化后台？
- 模型在什么时间点使用：检查前、报告前、治疗前、治疗中、随访后？
- 输出是什么：风险分数、类别、分割 mask、热图、建议，还是报告辅助文字？
- 当前证据是回顾性、外部验证、前瞻性、读者研究，还是真实世界部署？
- 有无校准、DCA、reader study、医生+AI 增益、失败案例和安全边界？

## Translation pathway

### Stage 1: retrospective model

Required:

- clear target population
- locked input and output
- patient-level validation
- calibration and uncertainty
- limitations on use

### Stage 2: external and workflow validation

Required:

- independent external cohort
- center/scanner subgroup performance
- integration into plausible workflow
- comparison with clinical baseline or radiologist performance
- decision curve or net benefit

### Stage 3: reader study

Design:

- define readers and experience levels
- randomize case order
- compare unaided vs AI-assisted performance
- washout period for crossover design
- measure time, confidence, sensitivity/specificity, AUC, agreement
- include failure and boundary cases

### Stage 4: prospective or real-world validation

Required:

- prespecified protocol
- locked model and threshold
- monitoring for data drift
- safety and override rules
- subgroup fairness check if relevant
- patient outcome or workflow endpoint when possible

## Reader study template

```text
Readers first interpreted each case without model assistance and then reinterpreted
the same or randomized cases with access to the model output after a washout period.
The primary endpoint was [reader-level metric], and secondary endpoints included
[time/confidence/inter-reader agreement]. Performance was compared using [appropriate
paired method] while accounting for reader and case clustering when possible.
```

Use only after study facts are supplied.

## Clinical utility

Clinical utility requires more than AUC:

- threshold linked to action
- net benefit or decision curve
- false-positive and false-negative consequences
- calibration at clinically relevant risk ranges
- comparison with current standard of care
- workflow burden and interpretability
- prospective evidence before deployment claims

## Discussion wording

Safer:

- “may support risk stratification”
- “could help identify patients who may benefit from...”
- “requires prospective validation before clinical implementation”
- “showed potential incremental value over clinical variables”

Avoid unless proven:

- “ready for clinical use”
- “can replace radiologists”
- “improves patient outcomes”
- “provides causal explanation”

## Output format

```text
转化定位
- 使用场景：
- 使用者：
- 当前证据阶段：

临床路径
- 回顾性验证：
- 外部验证：
- 读者研究：
- 前瞻/真实世界：

临床实用性
- 阈值和动作：
- net benefit：
- 风险和失败场景：

Discussion 文本
[only when facts are supplied]
```

## Red lines

- Do not claim clinical readiness from retrospective AUC alone.
- Do not claim patient outcome improvement without prospective or real-world evidence.
- Do not claim replacement of radiologists unless directly studied and ethically framed.
- Do not ignore false positives, false negatives, workflow burden, or threshold consequences.
- Do not treat saliency maps or SHAP as sufficient clinical interpretability evidence.
