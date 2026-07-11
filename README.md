# Radiology Skills · 影像科研全链路技能包

本skills由黄sir组学工作室的核心成员开发，三位成员为发表过《Radiology》原创性研究的第一作者（Huang Yuhong、Gu Wenchao、Song Xinyang），对影像组学领域有深刻认知。这是一个面向影像组学、影像深度学习和医学影像 AI 研究的全开源 Codex skill，用于帮助研究者完成前沿选题、文献梳理、课题设计、ROI/mask 标注规范、统计分析、图表规划、影像基因组学机制解析、多中心验证、公共数据库使用、伦理与复现、论文写作、投稿预审、选刊投稿、基金申报、临床转化和返修回复等。

基于 2023-2026 高水平文献，整理了 Radiology、Radiology: Artificial Intelligence、The Lancet Oncology、The Lancet Digital Health、Nature Medicine、Nature Cancer、Nature Communications、Science Advances、eClinicalMedicine、eBioMedicine、Cell Reports Medicine、npj Digital Medicine 等高影响力期刊中医学影像 AI、影像组学、影像深度学习、影像基因组学和临床转化相关研究的发表规律。这个证据层可用于辅助选题、投稿选刊、前沿设计、课题设计和基金申报等任务。

**让论文和标书在投出去之前，先过一遍审稿人的眼光。**

> 审稿人拒稿，往往只需要三个问题：测试集是不是按患者划分的？外部验证在哪里？校准曲线呢？
> 多数影像 AI、放射组学稿件不是败在工作量，而是败在设计和写作阶段没人用审稿人的标准提前审过一遍——
> 等收到大修甚至直接拒稿才发现，已经晚了一整轮周期。`radiology-skills` 就是提前替你把这一关过掉的那双眼睛。

面向中国高水平医学影像科研团队的 Claude / Codex 技能包：以 **_Radiology_（RSNA）级别、以及 Nature 系列**（Nature Medicine、Nature Biomedical Engineering、Nature Communications、npj Digital Medicine 等）**级别的研究设计、方法学规范、统计呈现和投稿要求**为目标，把影像 AI、深度学习、放射组学、影像基因组学与多组学研究，拆解成 22 位"虚拟专科顾问"、可以随时调用的专业工作流。

`radiology-skills` 不是泛泛的"论文写作提示词合集"。它解决的是医学影像科研中最容易卡壳、也最容易被高水平期刊审稿人当场击中的问题：课题到底能不能做、创新点站不站得住、样本量和外部验证撑不撑得起结论、标注和建模流程有没有数据泄漏、统计报告齐不齐全、图表符不符合投稿标准、论文满不满足国际通行的报告规范，深度学习模型有没有可解释性和不确定性证据，以及审稿意见能不能被逐条、可追溯地回应。

> 开发团队长期从事影像组学、影像深度学习和医学影像 AI 研究，规则来自真实投稿、真实审稿意见和真实基金评审的一线经验。它不是把通用论文写作建议套壳，而是把“审稿人会怎么追问”前置到课题设计、统计验证、图表和投稿材料中。

---

## 核心卖点，30 秒说清楚

- **全链路一次装好**：22 个技能、90 余份模块化规则文件，覆盖从"这批数据到底能不能做"到"基金标书怎么写"的完整科研链路，不用在十几个工具、公众号文章和往届师兄师姐的经验之间来回拼凑。
- **双期刊规格内置**：同一套技能同时懂 _Radiology_ 家族和 Nature 系列的投稿规矩——摘要结构、图表尺寸、图版字母大小写、Reporting Summary、Extended Data 该放哪——不用自己再去猜哪本期刊要什么格式。
- **审稿人视角前置**：数据泄漏审计、CLAIM / TRIPOD+AI / CLEAR 等报告规范逐条核查、投稿前模拟严审——把审稿人真正会问的问题，在投出去之前先自己问一遍。
- **三位 _Radiology_ 一作坐镇**：规则来自真实投稿和真实评审经验，不是把"如何写好论文"这类通用建议套壳成产品。
- **诚信是底线，也是卖点**：缺什么就明确标注"待确认"，绝不编造数据、文献、合规性或申请资格——这恰恰是通用 AI 工具最容易栽跟头、也是让你论文/标书翻车的地方。

---

## 适合谁

- 已经有 CT、MRI、PET、超声、乳腺钼靶或多模态影像数据，但还不确定"这批数据到底能做成什么课题"的临床科研团队。
- 正在冲击 _Radiology_、Radiology: AI、Lancet Digital Health、Nature Medicine、European Radiology 等高水平期刊的影像 AI、放射组学、影像组学研究者。
- 需要把中文实验记录、组会思路、初稿或审稿意见转化为英文投稿文本、规范补充材料、图表和回复信的作者。
- 正在准备国自然、省自然或院内基金，想把"做一个模型"升级为有科学问题、机制逻辑和可验证路径的基金标书；也包括同步筹备 NIH、ERC、Wellcome 等国际基金、需要先弄清楚自己到底有没有申请资格的团队。
- 希望在投稿前提前发现方法学、统计、伦理、数据共享、报告规范和临床转化证据短板的 PI、博士后、研究生与科研秘书团队。

## 重点解决的科研痛点

| 常见痛点 | `radiology-skills` 的处理方式 |
|---|---|
| 有数据但不知道课题能不能做 | 先判断可行性、任务天花板、样本量/事件数/外部验证瓶颈，再给出最小可行方案与升级版设计 |
| 追热点但创新点空泛 | 把基础模型、多模态、纵向影像、联邦学习、影像基因组学等趋势转成可执行问题，并要求实时核验文献依据 |
| 模型看起来准确但经不起审稿 | 对患者级别数据划分、仅在训练集拟合、特征筛选、调参、外部验证、校准曲线、决策曲线、多阅片者研究等做数据泄漏和可信度审计 |
| 病灶勾画、标注协议写不清楚 | 输出勾画范围、阅片者盲法与共识流程、一致性评价（ICC / Dice / Hausdorff）、掩膜几何一致性等标准操作流程 |
| 论文不符合报告规范 | 自动路由到 CLAIM 2024、TRIPOD+AI、CLEAR、METRICS、RQS、IBSI、STARD、PRISMA-DTA、QUADAS 等清单逐项审计 |
| 统计结果和图表表达不专业 | 规范 AUC 比较（DeLong / bootstrap）、95% 置信区间、P 值、校准、决策曲线、生存分析、阅片者一致性和可发表图件 |
| 中文思路难转成高水平英文稿 | 将中文/中英混排笔记转成 _Radiology_ 风格的结构化摘要（含一句话结论与要点框），或 Nature 系列的非结构化摘要，及对应的方法、结果、讨论部分 |
| 投稿前不知道自己的短板在哪 | 模拟严苛审稿，按致命问题 / 大修意见 / 小修意见分级，输出可执行修改清单 |
| 审稿回复缺少证据链 | 把每条审稿意见拆成稳定编号、修改动作、稿件位置、补充分析和可追溯回应 |
| 临床转化证据不足 | 设计临床使用场景、阈值到临床动作的映射、多阅片者对照研究、前瞻验证、PACS/RIS 接入和上线后漂移监测 |
| 深度学习模型没有可解释性/不确定性证据 | 规范化报告显著图、特征归因方法与不确定性量化（蒙特卡洛丢弃、深度集成、保形预测），鲁棒性与分布外检测，并对齐 FUTURE-AI 可信 AI 框架 |
| 想投 Nature 系列但不知道格式差在哪 | 摘要结构、图表尺寸与图版字母大小写、Reporting Summary、Extended Data / Source Data、数字格式与参考文献体例的逐项对照 |
| 只想做国自然，但也想留一条国际基金的路 | 国自然为主线，同时提供 NIH R01 / ERC / Wellcome 的结构改写，并**先核查申请资格**——不让你在进不去的赛道上浪费精力 |

---

## 为什么不直接用通用 AI，或找论文中介？

这是一笔值得算清楚的账，不是营销话术：

| 对比维度 | 通用 AI 直接问 | 论文润色 / 基金中介 | 自己啃指南 | `radiology-skills` |
|---|---|---|---|---|
| 方法学规则（患者级别划分、报告规范版本） | 靠运气，容易给出泛泛而谈的建议 | 多数只做语言润色，很少同时具备方法学审计能力 | 需要自己追踪 20 多份国际报告规范及其更新 | 内置且持续核对当前版本（CLAIM 2024、CLEAR 2023、METRICS 2024、RQS 2.0 等） |
| 投稿格式（_Radiology_ 家族 vs Nature 系列） | 不区分期刊家族，容易套错模板 | 少数具备双规格能力，且按篇加价 | 需要逐刊翻查最新作者须知 | 摘要结构、图表尺寸、图版字母大小写等按目标期刊自动切换 |
| 复用性 | 每次对话从零开始，规则不持久 | 按篇、按字数计费 | 一次性学习成本高，但长期可复用 | 一次安装，覆盖立题到基金申报的每一篇后续论文 |
| 响应速度 | 快但不可靠 | 以天、周计 | 以周、月计（学习曲线） | 分钟级出可执行清单 |
| 诚信底线 | 可能编造文献、合规性、统计量而不自知 | 依赖具体经办人的经验和责任心 | 取决于个人严谨程度 | 明确写入每个技能：不编造数据、置信区间、文献编号、伦理号、样本量；缺什么就标注"待确认"，绝不装作齐全 |

`radiology-skills` 要做的不是取代生物统计师、临床合作者或伦理委员会，而是在把稿子/标书交给他们之前，先帮你把能自己查清楚的部分都查清楚——省下的是反复返工的那几轮周期，而不是省掉该有的专业把关。

---

## 全链路架构

```text
 ① 立题与设计               ② 数据 · 标注 · 伦理          ③ 建模与分析
   frontier ─ design        annotation ─ data           radiomics ─ deep-learning
        └ search                 └ ethics                 radiogenomics ─ stats
        │                          │                          │
        └──────────────►  ④ 写作 · 图表 · 报告规范  ◄─────────┘
                            writing · figure · polishing
                            reporting · reader · citation
                                       │
                                       ▼
                          ⑤ 投稿 · 回复 · 转化 · 基金
                            journal · prereview · response
                            translation · grant · paper2ppt
```

每个技能都包含"下一步去哪个技能"的衔接说明，因此既可以单独调用某一个技能，也可以让一个研究项目沿着链路推进：先判断数据能不能做，再补齐标注和伦理，之后设计建模和统计，最后进入写作、投稿、回复与转化。

---

## 技能索引

**22 位虚拟专科顾问**——把这 22 个技能想象成一支科研智囊团：每一位都只管自己最擅长的一段，交接清楚，不越界，也不漏项。技能标识（英文，用于实际调用）配一个好记的中文角色名。

### ① 立题与设计

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-frontier`](radiology-skills/modules/radiology-frontier/README.md) · **选题雷达** | 测试版 | 找前沿方向和创新点；把热点转成适合当前数据的可投稿科学问题；实时核验文献依据 |
| [`radiology-design`](radiology-skills/modules/radiology-design/README.md) · **课题诊断师** | 稳定版 | 判断数据可行性，形成完整研究设计蓝图，并设计内部、时间、地域、多中心、外部或联邦验证方案 |
| [`radiology-search`](radiology-skills/modules/radiology-search/README.md) · **文献猎手** | 测试版 | 多源检索文献与公共数据集（PubMed、arXiv、Crossref、TCIA、GEO 等），并验证 DOI / PMID / 数据集编号 |

### ② 数据、标注与伦理

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-annotation`](radiology-skills/modules/radiology-annotation/README.md) · **标注质检员** | 测试版 | 设计病灶勾画标准操作流程、阅片者协议、一致性评价和掩膜几何质控 |
| [`radiology-data`](radiology-skills/modules/radiology-data/README.md) · **数据合规官** | 测试版 | 数据/代码可用性声明、DICOM 去标识化、仓库选择、FAIR 与可复现包；Nature 系列的 Extended Data / 补充材料 / Source Data 划分 |
| [`radiology-ethics`](radiology-skills/modules/radiology-ethics/README.md) · **伦理顾问** | 测试版 | 伦理审批、知情同意/豁免、隐私与共享治理，保证伦理声明与数据可用性声明前后一致 |

### ③ 建模与分析

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-radiomics`](radiology-skills/modules/radiology-radiomics/README.md) · **组学工程师** | 测试版 | 按 IBSI / CLEAR 设计放射组学流程：预处理、特征提取、训练集内筛选、建模与数据泄漏审计、delta 放射组学、体模/重复扫描稳定性 |
| [`radiology-deep-learning`](radiology-skills/modules/radiology-deep-learning/README.md) · **深度学习审查员** | 测试版 | 按 CLAIM 2024 设计或审查影像深度学习研究：架构、输入、多模态、训练协议、外部验证、可解释性、不确定性量化与鲁棒性 |
| [`radiology-radiogenomics`](radiology-skills/modules/radiology-radiogenomics/README.md) · **影像基因组顾问** | 测试版 | 影像 × 多组学研究：匹配队列、TCIA-TCGA、多组学整合方法、单细胞/空间组学与机制验证 |
| [`radiology-stats`](radiology-skills/modules/radiology-stats/README.md) · **统计军师** | 稳定版 | 影像统计与模型评价：ROC 比较（DeLong）、一致性分析（ICC/多阅片者研究）、校准、决策曲线、多重比较、生存分析和样本量 |

### ④ 写作、图表与报告规范

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-writing`](radiology-skills/modules/radiology-writing/README.md) · **论文架构师** | 测试版 | 构建 _Radiology_ 风格（结构化摘要、一句话结论、要点框）或 Nature 系列风格（非结构化摘要）稿件：方法、结果、讨论 |
| [`radiology-figure`](radiology-skills/modules/radiology-figure/README.md) · **图表设计师** | 稳定版 | 生成投稿级统计图和影像图版：ROC 曲线、森林图、校准曲线、生存曲线、决策曲线、患者筛选流程图、MRI/CT 图版、图文摘要；同时支持 _Radiology_ 与 Nature 系列两套尺寸/字母规格 |
| [`radiology-polishing`](radiology-skills/modules/radiology-polishing/README.md) · **定稿抛光师** | 稳定版 | 按 _Radiology_ 或 Nature 系列行文规范润色英文，校准统计表达（含期刊相关的数字格式差异）、语气、时态，标出结论夸大之处 |
| [`radiology-reporting`](radiology-skills/modules/radiology-reporting/README.md) · **规范审计员** | 稳定版 | 将稿件路由到正确报告规范并逐项审计：CLAIM、TRIPOD+AI、CLEAR、METRICS、RQS、IBSI、STARD 等，Nature 系列另加 Reporting Summary，并可对齐 FUTURE-AI 可信 AI 框架 |
| [`radiology-reader`](radiology-skills/modules/radiology-reader/README.md) · **双语精读官** | 测试版 | 生成影像论文中英对照全文阅读材料，保留图表、统计和原文定位标记 |
| [`radiology-citation`](radiology-skills/modules/radiology-citation/README.md) · **引文核验官** | 测试版 | 为论点检索并验证影像期刊参考文献，导出 RIS / EndNote / BibTeX 格式 |

### ⑤ 投稿、回复、转化与基金

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-journal`](radiology-skills/modules/radiology-journal/README.md) · **投稿参谋** | 测试版 | 根据文章真实强弱项建立投稿梯队：冲刺、主投、稳妥，并实时核对期刊收稿范围；含 _Radiology_ 家族与 Nature 系列两套投稿前检查清单 |
| [`radiology-prereview`](radiology-skills/modules/radiology-prereview/README.md) · **模拟审稿官** | 测试版 | 投稿前模拟严苛审稿，提前暴露直接拒稿/大修风险 |
| [`radiology-response`](radiology-skills/modules/radiology-response/README.md) · **回复信教练** | 测试版 | 逐条拆解审稿意见，生成可追溯的回复信、修改动作和补充分析路线 |
| [`radiology-translation`](radiology-skills/modules/radiology-translation/README.md) · **临床转化顾问** | 测试版 | 设计临床转化证据链：使用场景、多阅片者对照研究、阈值到临床动作、前瞻验证、PACS/RIS 接入 |
| [`radiology-grant`](radiology-skills/modules/radiology-grant/README.md) · **标书操盘手** | 测试版 | **主线：**将影像研究改写为国自然/省自然标书（科学问题、研究内容、技术路线、创新点、可行性）。**延伸：**同一份研究改写为 NIH R01 / ERC（Starting/Consolidator/Advanced）/ Wellcome 等国际基金申请，先核查 PI/机构申请资格再动笔，避免在进不去的赛道上投入精力 |
| [`radiology-paper2ppt`](radiology-skills/modules/radiology-paper2ppt/README.md) · **组会讲解员** | 测试版 | 将影像论文转成中文读片会/组会 PPT，保留关键图表并加入方法学点评 |

> 状态说明：**草案** = 规则已定义但未充分测试；**测试版** = 已在示例上验证，仍可能有边界情况；**稳定版** = 已在真实影像科研内容中反复校准。

---

## "我现在卡在……"快速选择

| 需求 | 推荐技能 |
|---|---|
| 这批数据能不能做？能做成什么级别？ | `radiology-design` 课题诊断师 |
| 想找近三年前沿方向和创新点 | `radiology-frontier` 选题雷达 + `radiology-search` 文献猎手 |
| 需要系统梳理文献或公共数据集 | `radiology-search` 文献猎手 |
| 需要用 TCIA / TCGA / GEO 做外部验证或机制分析 | `radiology-data` + `radiology-radiogenomics` + `radiology-search` |
| 影像组学流程怕不规范 | `radiology-radiomics` + `radiology-annotation` + `radiology-reporting` |
| 深度学习模型怕数据泄漏或缺少外部验证 | `radiology-deep-learning` + `radiology-design` + `radiology-stats` |
| 深度学习模型没有可解释性/不确定性证据 | `radiology-deep-learning` 深度学习审查员 |
| 模型评价、AUC 比较、校准、决策曲线、样本量不会写 | `radiology-stats` 统计军师 |
| 多中心、外部验证、中心效应、扫描仪差异不知道怎么处理 | `radiology-design` + `radiology-stats` |
| 论文要按高水平期刊规范补齐 | `radiology-reporting` 规范审计员 |
| 想投 Nature 系列但不确定格式差异 | `radiology-writing` + `radiology-figure` + `radiology-reporting` |
| 中文实验记录要变成英文方法/结果/讨论 | `radiology-writing` + `radiology-polishing` |
| 图表和图例需要投稿级输出 | `radiology-figure` 图表设计师 |
| 投稿前想找出致命问题 | `radiology-prereview` 模拟审稿官 |
| 不知道该投哪个期刊 | `radiology-journal` 投稿参谋 |
| 审稿意见很复杂，想逐条回应 | `radiology-response` 回复信教练 |
| 想做阅片者研究、前瞻验证或临床效用评估 | `radiology-translation` 临床转化顾问 |
| 想把论文思路升级成国自然/省自然 | `radiology-grant` 标书操盘手 |
| 想同步申请 NIH / ERC / Wellcome，但不确定自己有没有资格 | `radiology-grant`（国际基金部分） |
| 想把论文做成中文组会/读片会 PPT | `radiology-paper2ppt` 组会讲解员 |

---

## 四个专业支柱

### `radiology-reporting` 规范审计员：报告规范与投稿合规骨架

把每一类影像研究路由到正确清单，并逐项审计是否满足投稿要求：**CLAIM 2024**、**TRIPOD+AI 2024**、PROBAST(-AI)、**CLEAR 2023**、**METRICS 2024**、RQS / RQS 2.0、**IBSI**、**STARD 2015**、PRISMA-DTA、QUADAS-2、CONSORT-AI / SPIRIT-AI 等；投 Nature 系列时再叠加 **Reporting Summary**，并用 **FUTURE-AI**（公平性、普适性、可追溯性、可用性、鲁棒性、可解释性）框架检查部署类声称是否有证据支撑。它回答的问题是：审稿人会按什么标准检查你，你现在还缺什么。

### `radiology-stats` 统计军师：经得起审稿的影像统计

覆盖诊断准确性、AUC 比较（DeLong / bootstrap）、一致性分析（ICC/kappa）、Bland-Altman 一致性界限、多阅片者研究、校准、Brier 评分、决策曲线、多重比较校正、放射组学/多组学高维统计、生存分析和样本量估算。目标不是"算出一个 P 值"，而是让统计方法、报告句式和图表都经得起追问。

### `radiology-radiogenomics` 影像基因组顾问：影像 × 多组学高难度研究链

围绕 TCIA-TCGA、GEO、dbGaP、EGA、cBioPortal 等数据源，处理匹配影像-组学队列、样本与影像对应关系、IBSI 放射组学、批次效应校正、多组学融合方法、单细胞去卷积和空间转录组。重点防止小样本匹配、批次/扫描仪混杂、空间错位、重复取样和生物学结论夸大。

### `radiology-design` 课题诊断师 + `radiology-frontier` 选题雷达：从数据到高水平课题的战略前端

先判断数据能支撑什么，再把前沿趋势转成可执行、可验证、可投稿的研究问题。输出包括可行性结论、最小可行版本与升级版设计对比、验证阶梯、临床使用场景、限制条件和需要实时核验的文献证据。

---

## 共同原则

这七条不是免责声明式的场面话，而是这套技能真正的竞争力所在——大多数通用 AI 工具恰恰在这些地方最容易翻车：

1. **一手来源优先**：以 _Radiology_ 作者须知、Nature Portfolio 编辑政策、国际报告规范（EQUATOR）和同行评议方法学文献为依据。
2. **完整链路而非单点润色**：从立题到回复信再到基金申报，每个阶段既能独立使用，也能向下游衔接。
3. **报告规范前置**：设计、统计、图表和写作都提前对齐审稿人会使用的核查清单。
4. **诚信优先**：不编造数据、P 值、置信区间、文献编号、伦理号、样本量、图表、申请资格或做过的实验——查不到就明确标注"待确认"。
5. **实时核验近期事实**：前沿文献、期刊收稿范围、投稿要求、基金指南和国际基金申请资格会变化，具体条目应实时检索确认。
6. **中英双语友好**：允许中文/中英混排输入，输出可以是中文策略说明、英文投稿文本，或中英对照材料。
7. **面向真实科研决策**：每次输出都尽量指出限制条件、下一步动作和最可能影响文章层级或申请结果的短板。

---

## 安装

这个仓库现在只有一个可安装入口：`radiology-skills/`。

22 个细分模块已经合并到 `radiology-skills/modules/`，由总入口按任务自动读取，不需要单独安装。请复制整个 `radiology-skills/` 文件夹，而不是只复制 `SKILL.md`，因为总入口依赖 `references/`、`modules/`、`scripts/` 和 `agents/`。

更详细的安装说明见 [`install.md`](install.md)。

Windows PowerShell：

```powershell
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\radiology-skills "$env:USERPROFILE\.codex\skills\"
```

macOS 或 Linux：

```bash
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
mkdir -p ~/.codex/skills
cp -R radiology-skills ~/.codex/skills/
```

安装后可以直接用自然语言触发，例如：

```text
Use $radiology-skills to design, audit, or write a radiomics or medical imaging deep learning study.
```

也可以直接用中文提问，例如：

```text
我有 300 例多中心肝癌 MRI，想找近三年前沿方向并设计课题。
帮我审查这个放射组学流程是否符合 IBSI / CLEAR，有没有数据泄漏。
按 CLAIM 2024 审计这篇影像深度学习论文，列出投稿前必须补齐的问题。
投稿前帮我模拟审稿，并给出致命问题/大修/小修分级的修改清单。
把这个研究改写成国自然标书：科学问题、技术路线、创新点、可行性。
我们也想申请 NIH R01，能不能用同一份研究改写？先看看我有没有资格申请。
```

如有需要，重启 Codex 或重新加载 skills。
## 新增技能的约定

```text
radiology-skills/modules/radiology-<主题>/
├── SKILL.md      # 必需：元信息(名称、描述) + 工作流 + 规则 + 下游衔接说明
├── README.md     # 必需：面向人的中文/双语说明
└── references/   # 推荐：模块化规则文件
```

新增后请同步更新本 README 的 [技能索引](#技能索引) 和 [快速选择](#我现在卡在快速选择)，并给新技能起一个符合"虚拟专科顾问"风格的中文角色名。

---

## 更新记录

- **2026-07（三）** — README 全面中文化改写：补齐"核心卖点"独立板块；为全部 22 个技能设计中文角色名（如"课题诊断师""模拟审稿官""标书操盘手"），统一到"虚拟专科顾问团队"的表达框架；技能索引、快速选择、状态标签（测试版/稳定版/草案）等结构性文字全部改为中文，仅保留期刊名、基金机构名、国际标准化报告规范/统计方法的专有名称（如 CLAIM、TRIPOD+AI、ROC、AUC 等——这是国内影像科研领域的通行写法，保留是为了专业性而非疏漏）以及技能标识本身（因涉及实际调用，不能更名）。技术内容与结论未作任何改动。
- **2026-07（二）** — `radiology-grant` 新增国际基金体系（`references/international-grants.md`）：NIH R01、ERC（Starting/Consolidator/Advanced，含 2026 新两段式结构）、Wellcome Trust 的结构与评审标准，以及**面向中国申请人的真实资格核查**（NIH 2025–2026 外籍分包新规、ERC 主持机构须在欧盟/联系国、Wellcome 部分项目的地区限制），并给出更易触达的跨境路径（NSFC 国际合作项目、RGC、MSCA、基金会）。国自然/省自然保持为主线与最成熟的部分。
- **2026-07（一）** — 全套技能审查后的扩展：为写作、图表、报告规范、润色、数据、投稿策略六个技能新增 Nature 系列期刊分支（摘要结构、图表尺寸/图版字母大小写、Reporting Summary、Extended Data/Source Data、数字与参考文献格式的差异，均已标注需按具体期刊实时核实）；为深度学习技能新增可解释性/不确定性量化/鲁棒性（含 FUTURE-AI 框架引用）；为放射组学技能补充 delta 放射组学与体模/重复扫描稳定性；为选题技能补充液体活检/病理基础模型融合等前沿方向；修复图表技能内部图版字母大小写不一致的问题；补充多处技能间的衔接说明。原有的方法学规则与既有 _Radiology_ 家族内容未改动。这些更新已合并进当前 `radiology-skills/modules/`。

---

## 免责声明

这些技能用于科研选题、研究设计、方法学、统计、图表、论文写作、投稿策略、审稿回复和基金文本辅助。它们**不提供医疗建议、临床诊断或个体患者影像判读**，也不能替代生物统计、临床、伦理、监管或法律审查，**不构成基金资助资格的正式认定**。作者仍需对所有数据、分析、结论、伦理审批、投稿材料和基金申报内容的准确性与完整性负责。投稿或申报前，请确认**当前版本**的报告规范、目标期刊投稿要求、Nature Portfolio 编辑政策，以及国自然/省自然或 NIH、ERC、Wellcome 等官方基金申报指南与申请资格——这些规则变化频繁，本工具提供的是结构化的起点，不是最终依据。
