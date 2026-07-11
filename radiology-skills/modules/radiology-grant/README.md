# radiology-grant

面向国自然、区域/省自然和院内基金的影像科研标书重构 skill。它解决的是很多影像 AI / radiomics 项目常见的基金痛点：只有“建一个模型”的工程目标，却缺少清晰科学问题、机制逻辑、创新分类、技术路线闭环和可行性证据。

## 它能做什么

- 将 paper logic 转成 grant logic：把“提高准确率”重构为机制、泛化规律、临床决策或方法学科学问题。
- 起草或重排：题目、摘要、立项依据、研究目标/内容、关键科学问题、技术路线、创新点、可行性、预期成果。
- 打磨 **innovation point**：明确属于 question / data / method / validation / mechanism 哪一类创新，并与 gap 绑定。
- 闭合 **technical route**：从临床需求到科学问题、aims、实验设计、验证路径、预期结果和风险预案形成闭环。
- 预判常见拒绝理由：创新虚、工程化过重、预实验薄、路线开环、承诺过满、aims 发散。

## 典型触发

- “把我的研究改写成国自然标书，帮我写立项依据、科学问题、技术路线、创新点。”
- “这个创新点和可行性够不够强？”
- “把 build a model 改成可资助的科学问题。”

## 参考文件

| File | 用途 |
|---|---|
| `references/grant-architecture.md` | 各部分结构、摘要与立项依据模板 |
| `references/reframe-and-innovation.md` | 工程目标到科学问题，创新分类 |
| `references/feasibility-and-pitfalls.md` | 可行性证据、路线闭环、常见拒绝原因 |

## 下游衔接

`radiology-design`（支撑 aim 的研究设计）· `radiology-frontier` / `radiology-search`（gap 与实时验证）· `radiology-stats`（样本量）· `radiology-ethics` / `radiology-data`（伦理与数据可行性）· `radiology-polishing`（英文润色）。

## 边界

不会编造预实验结果或引用。基金指南、字数、附件、伦理和限项要求每年可能变化，正式提交前必须核对当前官方申报指南。
