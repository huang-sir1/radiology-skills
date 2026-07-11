# radiology-response

面向影像期刊 major revision / revision 的逐点审稿回复 skill。它把 rebuttal 当作给编辑和审稿人的“可验证修改记录”，而不是情绪化解释：每条 comment 都要有稳定编号、问题分类、对应动作、稿件位置和事实边界。

## 它能做什么

- 将 decision letter 拆成 atomic、稳定编号的 comments。
- 将每条意见映射到 action：`ACCEPT_TEXT`、`ACCEPT_ANALYSIS`、`NEW_EXPERIMENT`、`SOFTEN_CLAIM`、`DISAGREE_WITH_REASON`、`AUTHOR_INPUT_NEEDED` 等。
- 对外部验证、leakage、calibration、MRMC reader study、IBSI reproducibility、fairness 等影像 AI 常见审稿要求进行路由。
- 审计回复的完整性、可追踪性、事实性、语气和跨审稿人一致性。

## 参考文件

```text
references/
├── action-mapping.md                comment 分类到 action 与 manuscript location
└── imaging-reviewer-playbook.md     影像 AI / radiomics 常见审稿要求与困难场景
```

## 典型触发

- “根据这些审稿意见帮我写 point-by-point response。”
- “帮我检查 rebuttal 的语气、完整性和可追踪性。”
- “两个审稿人意见冲突，怎么回复？”

## 边界

不会编造实验、分析、引用、行号或已经完成的修改；未完成工作会标记为 pending。新的统计分析交给 `radiology-stats`，新文本交给 `radiology-writing`。
