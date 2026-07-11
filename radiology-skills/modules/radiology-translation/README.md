# radiology-translation

面向影像 AI / radiomics 模型临床转化证据链的 skill。它帮助作者从 retrospective performance 走向 clinical utility claim：明确模型在流程中的位置、输出如何影响决策、阈值如何对应动作、读者研究如何设计，以及什么时候才有资格谈 prospective deployment。

## 它能做什么

- 定义 **use scenario**：screening、triage、diagnosis、staging、prognosis、response、surveillance、MDT 中的位置、输出类型、决策者和误判代价。
- 设计 **reader / MRMC study**：radiologist alone vs +AI、washout、randomisation、reader experience、time / confidence outcomes、统计方法。
- 建立 **threshold-to-action map**：operating point 到临床动作、net benefit / DCA、calibration prerequisite。
- 规划 **prospective / real-world evaluation**：temporal / prospective / RWE design、PACS/RIS integration、drift monitoring。
- 形成 **claim ladder**：当前证据能支持什么说法，哪些结论还需要补证据。

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

## 下游衔接

`radiology-stats`（MRMC、net benefit、DCA）· `radiology-reporting`（DECIDE-AI / CONSORT-AI）· `radiology-design`（验证队列）· `radiology-figure`（net-benefit / reader plots）。

## 边界

该 skill 规划科研评价和临床转化证据，不提供个体患者诊断或治疗建议。
