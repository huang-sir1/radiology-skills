# radiology-writing

面向影像、radiogenomics 与 standalone bulk RNA/scRNA/spatial/perturbation 论文的期刊族路由写作 skill。它从“论证链”而不是单句润色开始，把中文实验记录、中英混排草稿、结果表和图表说明，转成符合已选择期刊族结构的 manuscript prose；_Radiology_ 形状只在 RSNA 路由使用。

## 它能做什么

- 起草或重构 title、abstract、Introduction、Methods、Results、Discussion，以及目标期刊确实要求的 front matter。
- 将中文实验记录和组会笔记转成 submission-ready English，保留科研意图而不是逐词翻译。
- 按 RSNA/Radiology、Nature/npj、Cell Press、JAMA Network 或 Advanced/Wiley 等已验证的期刊族形状组织论证；目标未定时保持可逆的 journal-neutral spine。
- 标出缺失数据、待确认信息和不能凭空补的统计量或引用。

## RSNA / Radiology 路由形状

以下元素仅在该路由或当前目标期刊指南明确要求时使用：

- **Summary statement**：一句话概括主发现。
- **Key Results**：最多 3 条，最多 75 words，包含 summary data，不用模糊语言或未定义缩写。
- **Structured abstract**：Background、Purpose、Materials and Methods、Results、Conclusion。
- **Structured Discussion**：首段概括关键结果，限制明确，结论有边界。

## 参考文件

```text
references/
├── article-architecture.md                section order、argument flow、manuscript skeleton
├── structured-abstract.md                 abstract、Summary statement、Key Results 模板
├── methods.md                             影像/AI/radiomics Materials and Methods 顺序
├── results.md                             Results narrative、CIs、comparisons、validation
├── discussion.md                          structured Discussion pattern
├── chinese-author-workflow.md             中文/混排笔记到 submission-ready English
├── nature-family-shape.md                 Nature 系形状：unstructured abstract、无 Summary statement/Key Results、Methods 位置不同
├── cell-jama-wiley-shape.md               Cell Press、JAMA Network、Advanced/Wiley 的分流形状
├── argument-spine-and-stage-gates.md      全文重建/拒稿挽救：argument spine、stage gates、results-as-validation
├── journal-family-writing-style.md        期刊家族写作风格（author guide / 经典文章解析）
├── section-contract-and-style-profile.md  整节 section contract、多作者与 author-voice 校准
└── examples/                              worked section examples
```

## 典型触发

- “根据这些结果写 structured abstract + Summary statement + Key Results。”
- “把这段中文实验记录写成 CT radiomics Methods。”
- “我的 Discussion 只是重复结果，帮我按 Radiology 逻辑重构。”
- “根据这些图表和统计结果写 Results。”

## 边界

不会编造数据、指标、CI 或引用。缺失信息会以待确认或占位形式暴露，并可交给 `radiology-reporting` 做规范核对。
