# radiology-grant

面向国自然、区域/省自然、院内基金及国际基金的影像科研标书审阅与开发 skill。核心不是套模板或“润色得像能中”，而是把当前申报通知、行政受理、同行评审标准和影像研究可行性锁到同一条可核查链路。

## 核心能力

- 建立 **grant call passport**：锁定基金、项目类型、年度、申请人/依托单位、官方版本、资格限项、表单、预算、伦理及 AI 使用规则。
- 对国自然额外锁定“年度—项目类型/亚类—科学部/学科处—年度申请代码—研究属性—专项/临床赛道”六字段，并保留官方文本冲突。
- 严格分开 **行政受理门禁** 与 **科学价值门禁**；通过任一门禁均不代表通过另一门禁。
- 支持 `triage/targeted`、`full audit`、`mock panel`、`revision/resubmission` 四类审阅。
- 将问题、gap、hypothesis、aims、方法、里程碑、风险、预算和 claim ceiling 形成闭环。
- 执行影像专项审计：采集/重建/QC、队列、参考标准、标注、泄漏、统计、跨中心迁移、临床路径、数据/计算/伦理。
- 路由 H18/H27/H28/H29、医学临床专项和历史专项；按任务选择 CLAIM、STARD-AI、TRIPOD+AI、PROBAST+AI、CLEAR/IBSI/METRICS/QIBA 等方法学框架。
- 输出 evidence-anchored `criterion finding`，保留未知、证据状态和模拟评审分歧，不伪造官方评分或中标概率。

## 国自然边界

NSFC 的项目类型、申请结构、页数、限项和预算规则必须在当年官方指南及在线表单中实时核验，不能沿用旧“八股”。2026 年官方规则还禁止使用生成式 AI 直接生成申请书及未经核实的生成内容；因此本 skill 默认提供审阅、结构诊断、证据表和明确标识的作者改写建议，不把 AI 文字伪装成可直接提交的申请书。

## 主要资源

| Resource | 用途 |
|---|---|
| `references/call-and-compliance-gate.md` | 申报通知版本锁、NSFC/NIH 当前官方框架、行政门禁与 AI 边界 |
| `references/nsfc-2024-2026-change-map.md` | 国自然三年变化、冲突门禁、合作协议和伪规则排除 |
| `references/nsfc-application-content-playbook.md` | 2026 三段式下的题目、摘要、立项依据、研究内容和研究基础功能 |
| `references/nsfc-radiology-code-and-call-router.md` | H18/H27/H28/H29、临床专项和专项指南年度路由 |
| `references/imaging-methodology-router.md` | 影像 AI、诊断、预测、放射组学、定量影像和生成式 AI 方法学选择 |
| `references/source-registry.md` | 2024—2026 官方来源与方法学来源台账，真实申报时实时刷新 |
| `references/review-modes-and-criteria.md` | 四种审阅模式、criterion finding、模拟会评与返修闭环 |
| `references/grant-architecture.md` | 不依赖旧标题的 proposal spine、aim 和预算结构 |
| `references/radiology-feasibility-audit.md` | 影像研究专项可行性与 claim ceiling |
| `references/evidence-contract-and-stopping-rules.md` | 证据状态、aim contract 和停止规则 |
| `templates/grant-call-passport.md` | 当前 call 的官方版本与适用性记录 |
| `templates/grant-review-report.md` | 完整标书审阅报告 |
| `templates/aim-milestone-risk-register.md` | aim、里程碑、风险、fallback 与预算追踪 |

## 边界

本 skill 不替代基金委、依托单位科研管理部门、伦理/财务审查或真实评审专家，不保证资格、评分或资助。论文审稿交给相应论文 skill；标书答辩/PPT 仅在 proposal spine 冻结并经作者确认后交给 `radiology-paper2ppt`。
