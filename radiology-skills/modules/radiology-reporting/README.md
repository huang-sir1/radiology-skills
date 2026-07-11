# radiology-reporting

面向医学影像研究投稿前的报告规范与质量清单审计 skill。它是 `radiology-skills` 的合规骨架：把 AI、radiomics、prediction model、diagnostic accuracy、reader study、systematic review 等研究路由到正确 guideline stack，并逐项判断稿件是否满足审稿人会检查的要求。

## 它能做什么

1. **Classify** 研究类型：任务、设计、endpoint、模型开发/验证状态。
2. **Route** 到正确 reporting guideline 与 quality / risk-of-bias 工具组合。
3. **Audit** 每个 checklist item：`PRESENT / PARTIAL / MISSING / NA`，并给出稿件位置和具体修复动作。
4. **Prioritise** 修改：Blocker / Should-fix / Polish，并说明对应 reviewer risk。

## 覆盖的规范

| Guideline | 适用范围 |
|---|---|
| **CLAIM** | 医学影像 AI 研究 |
| **TRIPOD+AI** | 诊断/预后 prediction model |
| **PROBAST / PROBAST-AI** | Prediction model risk of bias |
| **CLEAR** | Radiomics reporting |
| **METRICS** | Radiomics methodological quality |
| **RQS / RQS 2.0** | Radiomics quality score / readiness |
| **IBSI** | 标准化 radiomic features 与图像处理 |
| **STARD** | Diagnostic accuracy studies |
| **PRISMA-DTA** | Diagnostic test accuracy systematic reviews |
| **QUADAS-2 / QUADAS-C** | DTA risk of bias |
| **STROBE** | Observational studies |
| **CONSORT-AI / SPIRIT-AI** | AI clinical trials / protocols |
| **DECIDE-AI** | Early-stage clinical evaluation of decision-support AI |

使用时应实时核对 guideline 当前版本和目标期刊要求。

## 参考文件

```text
references/
├── guideline-router.md          decision tree 与 hybrid studies 的 guideline stack
├── claim-2024.md                CLAIM 2024 Update，按章节拆解
├── tripod-ai-probast.md         TRIPOD+AI items 与 PROBAST(-AI) domains
├── clear-metrics-rqs.md         CLEAR、METRICS、RQS / RQS 2.0
├── ibsi-features.md             IBSI 图像处理与特征可复现性
├── stard-prisma-quadas.md       diagnostic accuracy、DTA reviews、risk of bias
└── radiology-submission-map.md  每个 item 在 Radiology 稿件中的位置
```

## 典型触发

- “按 CLAIM 2024 审计这篇 manuscript，给出缺口和修改建议。”
- “我做的是 CT radiomics 预测 IDH，需要哪些 checklist？”
- “我的特征提取是否 IBSI-compliant？必须报告什么？”
- “帮我填 TRIPOD+AI abstract checklist。”
- “这个 DTA review 的 QUADAS-2 风险在哪里？”

## 边界

不会为了好看而把缺失项标为合规，也不会编造实验、指标或材料。缺口会交给 `radiology-writing`（补写）、`radiology-stats`（统计）和 `radiology-data`（availability wording）等下游技能处理。
