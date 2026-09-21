# radiology-prereview

面向投稿前的严苛模拟审稿 skill。它把真实审稿人最可能抓住的问题提前暴露出来，尤其适合影像 AI、radiomics、radiogenomics 文章在投 _Radiology_、Radiology: AI、Lancet Digital Health、Nature Medicine 等高水平期刊前做一次方法学体检。

## 它能做什么

- 模拟方法学、统计、报告规范、图表和数据共享 reviewer 的审查视角。
- 优先寻找 **dealbreakers**：leakage、非 patient-level split、缺少外部验证、label 不清、segmentation 不清、统计不完整、overclaiming、baseline 弱、数据/代码不可用、伦理不一致。
- 输出 reviewer-style report：Blocker / Major / Minor，每条包含稿件位置、对应 guideline item 或方法学风险、可执行修复方案。
- 给出 claims vs evidence 校准，指出哪些结论需要降级或补证据。
- 生成 editor-style recommendation 和按优先级排序的修改路线。

## 典型触发

- “投稿前帮我模拟审稿，做一次严格预审。”
- “帮我找出审稿人一定会抓的问题。”
- “这篇文章现在能投这个期刊吗，必须先修什么？”

## 参考文件

| File | 用途 |
|---|---|
| `references/review-dimensions.md` | 审查维度与严重程度 rubric |
| `references/dealbreakers.md` | 致命问题的识别与修复 |
| `references/review-report-format.md` | reviewer report 与 editor recommendation 结构 |
| `references/pre-submission-hard-gates.md` | 最终投稿就绪 hard gates、拒稿挽救、contribution map、reviewer objection register |
| `references/ai-radiogenomics-pitfall-audit.md` | 影像 AI / radiogenomics 定向陷阱审计：leakage、外部验证、site/scanner 混杂、表面化 XAI、机制过声称 |
| `references/multi-reviewer-panel.md` | 临床 / 统计方法 / 影像 AI 可复现多 reviewer 独立评审与 editor 综合 |

## 下游衔接

`radiology-reporting`（checklist audit）· `radiology-stats`（统计完整性）· `radiology-radiomics` / `radiology-deep-learning`（leakage）· `radiology-design` / `radiology-translation`（验证和 reader study）· `radiology-data` / `radiology-ethics`（共享与伦理）· `radiology-writing` / `radiology-polishing`（overclaiming 和文本）· 后续接 `radiology-journal`（选刊）与 `radiology-response`（真实审稿回复）。

## 边界

这是投稿前彩排和风险排查，不保证录用。
