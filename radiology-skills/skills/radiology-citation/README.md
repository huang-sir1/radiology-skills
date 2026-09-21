# radiology-citation

面向影像论文写作和审稿回复的 **可验证参考文献工作流**。它把“这句话需要什么证据”拆成可检索、可验证、可导出的引用任务，优先覆盖 Radiology、Radiology: AI、RadioGraphics、AJR、European Radiology、JACR 等影像期刊，同时在方法学或生物学问题上扩展到更合适的来源。

## 它能做什么

- 将段落拆成需要引用支撑的 claim，并为每个 claim 寻找候选文献。
- 验证 DOI / PMID / arXiv / 期刊元数据，避免把错误或不存在的引用写进稿件。
- 区分证据强度：strong、partial、background、limiting。
- 按 RIS / EndNote / BibTeX 导出可直接导入文献管理器的文件。

## 典型触发

- “给这段 Discussion 找影像期刊文献，并导出 RIS。”
- “帮我核对这 12 个 DOI，生成干净的 BibTeX。”
- “这句话说外部验证很重要，有没有 Radiology / Radiology: AI 的依据？”

## 参考文件

```text
references/
├── radiology-journal-scope.md    影像期刊范围与 venue ranking
├── export-formats.md             RIS / ENW / BibTeX 字段映射与完整性检查
├── claim-verification-gate.md    投稿前逐条 claim 核查、doc-only/source-limited 审计、数值与图表 claim 验证
└── reference-integrity-audit.md  书目逐字段审计、DOI/年份/页码/作者冲突消解与修正记录
```

## 边界

无法验证的 identifier 会被删除或标记，不会编造 DOI、页码、卷期或作者信息。实时检索交给 `radiology-search`。
