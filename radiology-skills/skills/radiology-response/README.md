# radiology-response

面向影像、radiomics、radiogenomics、bulk RNA、单细胞、空间、多组学、病理和机制论文 major/minor revision 的逐点审稿回复 skill。它把 response-to-reviewers 当作给编辑和审稿人的“可验证修改记录”，而不是情绪化解释：每条 comment 都要有稳定编号、请求类型、作者决定、对应动作与方法、实际结果、稿件位置、残余边界和关闭证据。

## 它能做什么

- 将 decision letter 拆成 atomic、稳定编号的 comments。
- 将每条意见映射到 action：既包括 `ACCEPT_ANALYSIS`、`NEW_EXPERIMENT`、`SOFTEN_CLAIM`，也包括合法的 `ACKNOWLEDGE_ONLY`、`CROSS_REFERENCE_ONLY`、`NO_CHANGE_JUSTIFIED`；不为显示顺从而虚构分析或改稿。
- 多轮意见使用 canonical issue ID + round-aware source occurrence ID、来源版本/哈希和 reopen/supersede 谱系；科学 request class 与有原文定位的 editorial obligation 分轴记录。
- 最终包用 artifact fulfillment、editorial disposition 和固定的“无科学真值证书”三轴，绑定稿件/图表/补充材料版本；任何占位符或过期定位都会阻断 `READY_FOR_SUBMISSION_ASSEMBLY`。
- 区分真实科学缺陷、需要澄清、可选增强、reviewer preference 和超范围/不可行请求；不因审稿人口气强硬就自动把建议升级成必须实验。
- 强制使用“立场/理由 → 动作与方法 → 结果/证据 → 精确位置 → 残余边界 → closure”回复块；没有结果的“we performed”不算完成。
- 提供接受并补做、澄清既有证据、部分接受、基于证据反驳、不可行替代和阴性结果六类可直接填充但不会虚构内容的英文回信骨架。
- 对外部验证、leakage、calibration、MRMC reader study、IBSI reproducibility、fairness 等影像 AI 常见审稿要求进行路由。
- 对 donor-level replication、batch/composition、cell annotation、trajectory、spatial null、communication、functional validation、perturbation/rescue 等组学与机制审稿要求进行路由。
- 审计回复的完整性、可追踪性、事实性、语气和跨审稿人一致性。
- 先盲核原稿与返修稿，再读取回复信定位证据，防止被流畅措辞替代真实修改。
- 用本地审稿经验注册表沉淀团队真实 decision letter、请求、作者动作、失败与关闭证据；
  严格区分正式期刊规则、跨案例经验模式和单案例启发，不把录用结果倒推成因果。

## 参考文件

```text
references/
├── action-mapping.md             comment 分类到 action 与 manuscript location
├── revision-letter-writing-chain.md 修回信文档结构、逐点段落骨架、语气和稿件联动
├── imaging-reviewer-playbook.md  影像 AI / radiomics 常见审稿要求与困难场景
├── mechanism-reviewer-playbook.md bulk/scRNA/空间/多组学/扰动机制审稿回复路径
├── imaging-mechanism-reviewer-playbook.md 影像—机制桥、matched n、空间时间对应和fusion回复路径
├── transparent-peer-review-response-patterns-2024-2026.md 100篇公开审稿往返提炼的回复策略与反模式
├── transparent-peer-review-response-map-2024-2026.tsv 100条同步的 concern—action—closure 证据地图
├── reject-decision-tree.md       拒稿决策树：决定信分型 → 可争/不可争判定 → appeal / 接受 transfer / 补实验重投 / 降级转投四路线，48 小时行动清单与 appeal 信模板
└── response-audit-gate.md        回复信终审、response ledger、可追踪性与事实性锁定

templates/
├── point-by-point-response-matrix.md       意见拆分、作者裁决与证据先行计划
├── final-response-and-verification-package.md 投稿版逐点回复与独立关闭核验
└── local-reviewer-experience-registry.md  本团队真实审稿/修回案例、证据与适用边界注册表

scripts/
├── audit_response_evidence_map.ps1 100条修回证据与主语料同步审计
└── validate_response_skill.ps1 结构、案例、链接、语义合同与证据地图联合验证
```

## 典型触发

- “根据这些审稿意见和返修稿帮我写 point-by-point response；没有真实结果的地方保留待确认。”
- “帮我检查 rebuttal 的语气、完整性和可追踪性。”
- “两个审稿人意见冲突，怎么回复？”
- “审稿人要求补空间和敲除实验，这对我当前的 bulk RNA 机制主张是否必要？应该如何科学反驳或降级结论？”

## 边界

不会编造实验、分析、引用、行号或已经完成的修改；未完成工作会标记为 pending。新的统计分析交给 `radiology-stats`，新文本交给 `radiology-writing`。
