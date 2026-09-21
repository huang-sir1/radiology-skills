# radiology-search

面向影像文献与公共数据集的多源检索 skill。它把“找文献/找数据”变成可复现的检索策略：选择合适来源、控制 recall 与 precision、去重、验证 DOI / PMID / arXiv / accession，并为系统综述、选题依据、投稿回复和引用导出提供可靠输入。

## 它能做什么

- 根据问题路由到 PubMed + MeSH、arXiv、Crossref 等来源。
- 检索公共数据集：TCIA、GEO、cBioPortal、OpenNeuro、Grand Challenge、Medical Segmentation Decathlon 等。
- 跨来源去重并验证 DOI / PMID / arXiv / accession。
- 记录系统检索策略，支持 PRISMA-DTA 等场景。

## 参考文件

```text
references/
├── source-tiers.md                       来源路由、fallback order、MeSH、recall/precision、dedup keys
├── dataset-sources.md                    影像与组学数据集注册库及检索方法
├── literature-survey-workflow.md         稿件级文献综合：领域测绘、引言支撑、审稿辩护文献、数据集侦察
└── living-literature-and-acquisition.md  文献库维护、合规全文获取记录、投稿/修回前检索更新、防重复与防陈旧
```

## 典型触发

- “系统检索 CT radiomics 在肺癌诊断中的 PubMed 文献，包含 MeSH。”
- “找一个带 PI-RADS 标签的公开前列腺 MRI 数据集。”
- “核对并去重这 30 条来自两个数据库的结果。”

## 模式

可使用 prompt mode（内置搜索工具，按规则执行），也可连接 academic-search MCP（如 `search_papers` / `get_paper_by_id` / `get_citation` / `lookup_mesh`）。引用导出交给 `radiology-citation`。

## 边界

不会编造 metadata 或 accession，也不会绕过受限域名或访问限制。
