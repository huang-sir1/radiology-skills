# 选刊

Use this file when a manuscript, abstract, or near-complete study is available and
the user asks where to submit, which journal fits, how to rank target journals, or
how to position the paper for submission.

## 核心原则

选刊不是只看影响因子。先判断“文章证据强度”和“期刊发表偏好”是否匹配，再决定冲刺、稳妥和保底梯队。

不要承诺“必中”“容易中”或用过期影响因子做决定。期刊范围、版面费、审稿政策、开放获取政策、影响因子和文章类型要求可能变化；给最终建议前要联网核验目标期刊官网、近期发表文章和投稿须知，并写明检索日期。

## 输入信息

尽量收集：

```yaml
title:
abstract:
study_type:
disease:
modality:
sample_size:
centers:
external_validation:
prospective_or_retrospective:
reader_study:
clinical_endpoint:
main_results:
calibration_or_dca:
code_data_availability:
novelty_claim:
target_region_or_specialty:
article_type:
candidate_journals:
must_avoid:
publication_goal: 冲高分 / 稳妥发表 / 快速发表 / 专科影响力 / 开放获取
```

## 评价维度

| 维度 | 高匹配信号 | 降级信号 |
|---|---|---|
| 临床问题 | 明确临床痛点、目标人群和使用场景 | 只是“建一个模型” |
| 数据强度 | 多中心、外部验证、前瞻/读者研究、清楚标签 | 单中心、小样本、标签弱、无外部验证 |
| 方法可靠性 | 患者级划分、避免泄漏、校准、DCA、亚组和失败案例 | 只报告 AUC 或 Dice |
| 创新性 | 临床工作流、泛化、机制解释、多模态生物学联系 | 仅更换模型结构 |
| 期刊契合 | 近期发表同类主题、栏目匹配、读者群一致 | 主题偏离期刊 scope |
| 可复现性 | 代码、模型、数据或特征表有可用路径 | 数据/代码完全不说明 |

## 期刊梯队逻辑

按稿件证据强度给 3 个梯队：

1. **冲刺期刊**：需要临床问题强、验证强、创新点清楚。通常适合多中心、外部验证、前瞻/读者研究、真实工作流或机制解释充分的文章。
2. **主投期刊**：与疾病、模态、方法和读者群高度匹配，是最现实的投稿目标。
3. **备选期刊**：当创新性、样本量或验证强度不足时，选择专业方向更匹配、方法学要求相对适中的期刊。

影像 AI 常见候选池可以从这些类别开始，再按具体稿件核验：

- 综合医学和数字医学：Nature Medicine、The Lancet Digital Health、npj Digital Medicine、JAMA Network Open、eClinicalMedicine、EBioMedicine。
- 肿瘤和精准医学：The Lancet Oncology、Cell Reports Medicine、npj Precision Oncology、Clinical Cancer Research、European Journal of Cancer。
- 影像和放射学：Radiology、Radiology: Artificial Intelligence、European Radiology、Investigative Radiology、American Journal of Roentgenology、Academic Radiology。
- 专病专科：按疾病选择肝胆、肺癌、乳腺、神经肿瘤、泌尿、消化、核医学或超声方向期刊。
- 方法和工程：Medical Image Analysis、IEEE Transactions on Medical Imaging、IEEE Journal of Biomedical and Health Informatics、Computerized Medical Imaging and Graphics。

不要把这些期刊当成固定推荐清单。必须结合文章主题、近期发表情况、栏目类型、文章长度、开放获取、版面费和投稿政策重新筛选。

## 近期发表情况整合

当用户要求“结合现有文章和发表情况选刊”时：

1. 用文章关键词生成检索式：疾病 + 模态 + 任务 + 方法 + endpoint。
2. 检索近 3-5 年目标期刊同类文章，优先看同疾病/同模态/同任务文章。
3. 提取每篇文章的：期刊、年份、疾病、模态、样本量、验证方式、主要方法、主要结论。
4. 判断用户文章与这些文章相比的强项和短板。
5. 将期刊分为 `高度匹配`、`可尝试`、`不建议优先`。

## 输出格式

```text
投稿定位
- 文章类型：
- 核心卖点：
- 最大短板：
- 适合的读者群：

期刊梯队
| 梯队 | 期刊 | 匹配理由 | 需要补强 | 风险 |

近期发表对照
| 期刊 | 近年同类文章特点 | 与本文相比 |

投稿前修改建议
- 标题/摘要：
- Methods：
- Results：
- Discussion：
- 数据和代码：

不建议投稿的期刊或方向
- [期刊/方向]：原因

需要作者确认
- [缺失事实]
```

## 红线

- 不要只按影响因子排序。
- 不要推荐掠夺性期刊或无法核验的期刊。
- 不要说“这个一定能中”。
- 不要忽略目标期刊是否近期发表过同类研究。
- 不要把无外部验证、小样本、弱标签研究包装成适合顶刊，除非它有其他非常强的设计优势。
