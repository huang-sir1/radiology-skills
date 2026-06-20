# Chinese-author workflow（中文作者工作流）

面向中文母语影像作者：把中文/中英混排的实验记录，转成符合 _Radiology_ 习惯的英文稿。
核心原则：**翻译意图与论证，而不是逐句直译**。

## Principles
- Translate **argument and intent**, not clause order. Chinese drafts often front
  background and bury the claim; English (and _Radiology_) wants **claim-first**.
- Restructure to the _Radiology_ shape (article-architecture.md), then write English.
- Keep technical terms, gene/model names, units, and citation markers intact.
- Surface missing reporting elements the Chinese draft omits (CI, split unit, ethics,
  scanner) as questions — don't invent them.

## Common 中→英 fixes
| 中文习惯 | 改为（_Radiology_） |
|---|---|
| 长句、多分句串联 | 切分为短句；一句一义 |
| "本研究首次……" | 去掉"首次/novel"，除非可证实；用具体贡献 |
| 结果与讨论混写 | Results 只报数（含 95% CI），解释放 Discussion |
| "有较好的诊断价值" | 给出 AUC/敏感度/特异度 + 95% CI + 阈值来源 |
| 被动堆叠、主语缺失 | 适度主动语态，主语明确（_Radiology_ 接受主动语态） |
| PPV/NPV 未报患病率 | 报患病率；富集样本须换算并说明 |
| 训练/测试划分未写单位 | 明确**按患者划分**、测试集未参与调参 |

## Output for Chinese users
1. **English draft** in _Radiology_ shape.
2. **中文说明** — 结构选择、verb 强度、被删去的 overclaim、需要补充的报告项。
3. **待确认清单（中文）** — 只有作者能回答的问题（如：测试集是否按患者划分？是否有外部验证队列？
   伦理审批号？）。

## 注意
不替作者编造数据、指标、p 值、文献或伦理信息；缺失即标注为占位符或提问。报告规范核对交给
`radiology-reporting`，统计交给 `radiology-stats`。
