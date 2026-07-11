# radiology-writing

面向影像科研论文主体写作的 _Radiology_ 风格结构化写作 skill。它从“论证链”而不是单句润色开始，把中文实验记录、中英混排草稿、结果表和图表说明，转成符合高水平影像期刊结构的 manuscript prose。

## 它能做什么

- 起草或重构 title、structured abstract、**Summary statement**、**Key Results** box、Introduction、Materials and Methods、Results、structured Discussion。
- 将中文实验记录和组会笔记转成 submission-ready English，保留科研意图而不是逐词翻译。
- 按 _Radiology_ 的 section shape、verb calibration 和 reporting-checklist awareness 组织论证。
- 标出缺失数据、待确认信息和不能凭空补的统计量或引用。

## Radiology 写作形状

- **Summary statement**：一句话概括主发现。
- **Key Results**：最多 3 条，最多 75 words，包含 summary data，不用模糊语言或未定义缩写。
- **Structured abstract**：Background、Purpose、Materials and Methods、Results、Conclusion。
- **Structured Discussion**：首段概括关键结果，限制明确，结论有边界。

## 参考文件

```text
references/
├── article-architecture.md     section order、argument flow、manuscript skeleton
├── structured-abstract.md      abstract、Summary statement、Key Results 模板
├── methods.md                  影像/AI/radiomics Materials and Methods 顺序
├── results.md                  Results narrative、CIs、comparisons、validation
├── discussion.md               structured Discussion pattern
├── chinese-author-workflow.md  中文/混排笔记到 submission-ready English
└── examples/                   worked section examples
```

## 典型触发

- “根据这些结果写 structured abstract + Summary statement + Key Results。”
- “把这段中文实验记录写成 CT radiomics Methods。”
- “我的 Discussion 只是重复结果，帮我按 Radiology 逻辑重构。”
- “根据这些图表和统计结果写 Results。”

## 边界

不会编造数据、指标、CI 或引用。缺失信息会以待确认或占位形式暴露，并可交给 `radiology-reporting` 做规范核对。
