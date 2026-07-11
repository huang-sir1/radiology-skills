# radiology-design

面向“我有数据，但不知道能做成什么课题”的影像科研前端设计 skill。它先给出可行性判断，再把 CT / MRI / PET / US / mammography / 多模态数据转化为可投稿的 study blueprint，并明确真正限制文章层级的关键约束。

## 它能做什么

- 给出 **feasibility verdict**：Feasible as designed、Feasible with changes、Feasibility study only、Not yet collect X first。
- 形成 **study blueprint**：临床问题、目标人群、endpoint / estimand、comparator、clinical-use scenario、MVP 版本与更高阶版本。
- 设计 **validation plan**：internal CV / bootstrap、temporal、geographic / center-held-out、fully external、多中心、federated validation。
- 识别 **binding constraint**：matched n、event count、external-cohort size、labelled cases、center/scanner/batch effect 等真正卡住研究的问题。

## 典型触发

- “我有 300 例多中心肝癌 MRI，这批数据能做什么课题？”
- “帮我把现有数据设计成完整、可投稿的研究。”
- “多中心外部验证应该怎么设计？”
- “我的数据够做预后模型吗，还是只能做 pilot？”

## 参考文件

| File | 用途 |
|---|---|
| `references/feasibility-triage.md` | 任务上限、showstoppers、四类可行性判断 |
| `references/study-blueprints.md` | 七类设计模板，MVP vs stronger version |
| `references/validation-strategy.md` | 验证阶梯、多中心设计、center effect |
| `references/endpoints-and-estimands.md` | 临床问题、endpoint、comparator、threshold logic |

## 下游衔接

`radiology-frontier`（是否新颖/可发表）· `radiology-stats`（样本量、EPV、power）· `radiology-radiomics` / `radiology-deep-learning` / `radiology-radiogenomics`（具体方法设计）· `radiology-annotation`（mask SOP）· `radiology-reporting`（报告规范）· `radiology-ethics`（伦理/共享可行性）· `radiology-translation`（reader study / prospective plan）。

## 边界

该 skill 规划科研设计，不提供临床诊断或个体患者建议。
