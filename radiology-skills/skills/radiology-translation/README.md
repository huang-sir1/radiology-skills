# radiology-translation

面向影像 AI / radiomics 临床转化证据链的 skill。规范入口和完整渐进路由以
[`SKILL.md`](SKILL.md) 为准；本页仅作人类快速导览。当前能力覆盖七轴证据状态、受控阅片者与
临床影响研究、人因/实施科学、监管状态、DICOM/IHE 站点验收、生产监测、变更控制和退役。

## 它能做什么

- 定义 **use scenario**：screening、triage、diagnosis、staging、prognosis、response、surveillance、MDT 中的位置、输出类型、决策者和误判代价。
- 设计 **reader / MRMC study**：radiologist alone vs +AI、washout、randomisation、reader experience、time / confidence outcomes、统计方法。
- 建立 **threshold-to-action map**：operating point 到临床动作、net benefit / DCA、calibration prerequisite。
- 规划 **prospective / real-world evaluation**：temporal / prospective / RWE design、PACS/RIS integration、drift monitoring。
- 形成 **evidence-to-claim matrix**：不同设计/证据轴能支持什么说法、依赖哪些假设、哪些结论仍需不同证据。

## 典型触发

- “帮我设计读者研究、医生 + AI 增益、前瞻性验证。”
- “怎样才能声称 clinical utility 或进入部署前验证？”
- “把模型阈值映射到临床动作和 net benefit。”

## 参考文件

| File | 用途 |
|---|---|
| `references/use-scenario.md` | 流程位置、输出、错误代价 |
| `references/reader-study.md` | MRMC 设计：读者、washout、arms、outcomes |
| `references/threshold-to-action.md` | operating point 到 action，net benefit / DCA |
| `references/prospective-deployment.md` | Prospective / RWE、PACS/RIS、drift |
| `references/regulatory-and-deployment-readiness.md` | FDA/EU 监管就绪、silent deployment、locked/adaptive 模型、model card、生命周期监测 |
| `references/clinical-impact-study-design.md` | reader/silent/pragmatic/cluster/ITS 等设计到 claim 的条件路由 |
| `references/human-factors-and-implementation.md` | 用户、使用环境、关键任务、自动化偏差与实施结局 |
| `references/evidence-state-and-translation-lifecycle.md` | 技术、临床验证、影响、监管、经济、实施、生产七轴状态 |
| `references/implementation-science-and-scale-up.md` | CFIR/NASSS、RE-AIM/PRISM、策略、scale-up 与 de-implementation |
| `references/deployment-interoperability-and-site-acceptance.md` | DICOM/IHE/PACS/RIS/EHR 与本地端到端验收 |
| `references/production-monitoring-and-change-control.md` | denominator、label delay、incident/CAPA、rollback、revalidation、retirement |
| `references/source-registry.md` | 权威来源、状态、访问日期与 claim-use 边界 |

## 下游衔接

`radiology-stats`（MRMC、net benefit、DCA）· `radiology-reporting`（DECIDE-AI / CONSORT-AI）· `radiology-design`（验证队列）· `radiology-figure`（net-benefit / reader plots）。

## 边界

该 skill 规划科研评价和临床转化证据，不提供个体患者诊断或治疗建议。
