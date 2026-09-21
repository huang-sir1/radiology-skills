# radiology-frontier

面向影像 AI、放射组学和影像基因组学的前沿方向与创新点筛选 skill。它不只是罗列热点，而是把 foundation model、self-supervised learning、vision-language、多模态融合、纵向影像、联邦学习、radiogenomics 等趋势，转化为与用户真实数据匹配的可执行研究问题。

## 它能做什么

- 生成 **frontier shortlist**：识别近年高影响力期刊偏好的方向，并判断用户数据是否能承载。
- 提供 **evidence layer**：解释推荐背后的 publication-pattern 依据，例如 _Radiology_、Radiology: AI、Lancet Digital Health、Nature Medicine、Nature Communications、npj Digital Medicine 等期刊通常奖励什么证据。
- 输出 **executable questions**：把 2-4 个最佳方向转成 endpoint、comparator、最低证据门槛和目标期刊层级。
- 标记 **hot-but-unsuitable**：指出看似热门但当前数据不适合做的方向，避免为了追热点牺牲可信度。

## 诚信规则

该 skill 编码的是稳定的发表模式，而不是固定文献清单。具体近期论文、PMID、DOI 和期刊 scope 必须通过 `radiology-search` 实时检索验证；不能凭记忆引用。

## 典型触发

- “结合我的数据，找近三年的影像 AI 前沿方向和创新点。”
- “单中心 CT 队列适合做 foundation model 吗？”
- “为什么你建议做外部验证，有什么文献依据？”

## 参考文件

| File | 用途 |
|---|---|
| `references/frontier-themes.md` | 前沿主题、数据前提、fit test |
| `references/evidence-layer.md` | 期刊发表模式、verify-live discipline |
| `references/idea-to-question.md` | 趋势到可执行问题，创新性包装 |
| `references/ai-radiogenomics-frontier-map.md` | 未来 12-24 个月影像 AI / radiogenomics 方向图谱：foundation models、SSL、VLM、多模态融合、联邦学习、UQ/XAI 选型 |

## 下游衔接

`radiology-design`（完整设计）· `radiology-search`（验证 gap 与 seed papers）· `radiology-journal`（目标期刊层级）· `radiology-radiomics` / `radiology-deep-learning` / `radiology-radiogenomics`（方法适配）· `radiology-citation`（导出已验证引用）· `radiology-grant`（方向更适合或同时走基金申请）。
