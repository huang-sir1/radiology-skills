# radiology-skills · 影像科研全链路技能包

**围绕具体科学问题，协助设计、分析、审阅和表达医学影像研究。**

研究类型决定该检查什么：二分类预测、删失生存、分割测量、机制实验和证据综合需要不同的
方法与证据。先确定研究主张，再选择适用的规范、比较方法和验证设计。

面向中国高水平医学影像科研团队的 Claude / Codex 技能包：以 **_Radiology_（RSNA）级别、以及 Nature 系列**（Nature Medicine、Nature Biomedical Engineering、Nature Communications、npj Digital Medicine 等）**级别的研究设计、方法学规范、统计呈现和投稿要求**为目标，把影像采集与重建、影像 AI、深度学习、放射组学、影像基因组学、多组学、系统综述、机制验证、科研治理、成果影响与发表后维护，拆解成 40 位“虚拟专科顾问”、可以随时调用的专业工作流。

`radiology-skills` 不是泛泛的“论文写作提示词合集”。它解决的是医学影像科研中最容易卡壳、也最容易被高水平期刊审稿人或基金评审人当场击中的问题：课题能不能做、创新点站不站得住、样本量和外部验证撑不撑得起结论、标注和建模有没有泄漏、标书是否符合当年 call、科研 PPT 和传播衍生物是否保留证据边界，以及诚信、运行、复现、指南共识、定性/经济评价、创新转化、投稿与发表后更新能不能闭环。

由 Huang Yuhong、Gu Wenchao、Song Xinyang 联合开发。规则来源包括正式指南、方法学原始文献、
公开审稿材料和团队经验；这些来源的权威性与适用范围分别标注。当前能力状态见下方机器目录：
结构及契约检查通过，不代表已完成真实模型表现的独立评估，也不承诺论文录用或基金获批。

---

## 主要能力

- **40 个专业模块**：覆盖测量与质控、研究设计、分析、机制、证据综合、写作投稿、标书/PPT、治理、转化与发表后维护，按当前任务调用。
- **影像研究专属检查**：采集/重建、参考标准、患者与病灶层级、多中心差异、泄漏、外部独立性、定量重复性和跨尺度机制证据。
- **按研究类型选规范**：CLAIM、TRIPOD+AI、STARD-AI、CLEAR、IBSI 等各有适用范围，报告完整度与方法有效性分别审阅。
- **按当前目标核验规则**：期刊、文章类型、投稿阶段、基金年度和具体项目分别读取适用要求；历史快照不能替代当次核验。
- **明确证据状态**：已提供、已执行、已核验、尚缺失和存在冲突分别记录；实际行为仍需结合具体案例审查。

---

## 适合谁

- 已经有 CT、MRI、PET、超声、乳腺钼靶或多模态影像数据，但还不确定"这批数据到底能做成什么课题"的临床科研团队。
- 正在冲击 _Radiology_、Radiology: AI、Lancet Digital Health、Nature Medicine、European Radiology 等高水平期刊的影像 AI、放射组学、影像组学研究者。
- 需要把中文实验记录、组会思路、初稿或审稿意见转化为英文投稿文本、规范补充材料、图表和回复信的作者。
- 正在准备国自然、省自然或院内基金，想把"做一个模型"升级为有科学问题、机制逻辑和可验证路径的基金标书；也包括同步筹备 NIH、ERC、Wellcome 等国际基金、需要先弄清楚自己到底有没有申请资格的团队。
- 需要做组会/读片会、会议报告、标书答辩、论文答辩或项目进展汇报，希望从证据链到真实 PPTX 与演练质检一次完成的研究者。
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
| 标书看起来完整，但不知道会评会如何攻击 | 冻结当年 call/资格/附件，再按评审准则和影像研究硬门禁做分项审阅、模拟会评与修订闭环 |
| 科研 PPT 只是把论文/标书缩短，缺少受众和证据主线 | 先锁定受众要做的决策，再用一页一主张的证据叙事，保留影像显示/去标识与来源链，最后逐页渲染、可访问性和超时演练 QA |

---

## 如何配合科研团队使用

对单一问题，直接调用对应模块并提供现有材料；只有完整项目管理才需要维护研究护照、阶段和
交接记录。学术辅导可以采用直接解释或引导练习，按用户的实际需要切换。

生物统计师、领域合作者、科研管理部门和伦理委员会继续承担各自的专业判断。套件提供问题、
证据与修改位置之间的映射，便于这些判断落实到具体研究材料。尚无受控对照证据证明本套件
优于其他工具或服务；响应时间和质量取决于材料、任务、所用模型与工具能力。

---

## 全链路架构

```text
                         radiology-pipeline
                研究护照 · 阶段门 · 证据/数值/材料一致性
                                  │
 ① 立题与证据               ② 数据 · 标注 · 伦理          ③ 建模 · 组学 · 实验
   frontier ─ design        annotation ─ data           radiomics ─ deep-learning
   clinical-domain              └ ethics                 transcriptomics-analysis
   search ─ systematic-review                            radiogenomics ─ experiment-design
                                                         method-evaluation ─ stats
        │                          │                          │
        └──────────────►  ④ 写作 · 图表 · 报告规范  ◄─────────┘
                            writing · figure · table · polishing
                            reporting · reader · citation
                                       │
                                       ▼
                          ⑤ 投稿 · 回复 · 转化 · 基金 · 演示
                            journal · submission · prereview · response
                            translation · grant · paper2ppt
                                      │
             ⑥ 治理 · 运行 · 复现    ⑦ 共识 · 定性 · 经济    ⑧ 传播 · 影响 · 创新
                research-integrity       consensus-guideline       dissemination
                research-ops             qualitative-mixed-methods bibliometrics
                reproducibility          health-economics          innovation-transfer
```

上图只是面向读者的导航视图，不是强制线性流程。权威拓扑见
[`research-lifecycle-capability-map.md`](skills/radiology-pipeline/references/research-lifecycle-capability-map.md)：它把主生命周期、横向保障面、非线性分支、D0–D9 科学决策状态与 Stage 0–11 制品门分开表达，并允许修回、部署或发表后事件重新打开较早的科学决策。

每个技能都包含"下一步去哪个技能"的衔接说明，因此既可以单独调用某一个技能，也可以让一个研究项目沿着链路推进；但是否前进、回退、转向或停止，以当前开放决策、证据状态和唯一 owner 为准。

产品级路由以“用户此刻要做的科研决策/产物”为准，而不是看到某个工具名就抢任务：
统一 owner、边界和交接规则见
[`research-intent-routing.md`](skills/radiology-pipeline/references/research-intent-routing.md)。科研本身采用
D0–D9 决策循环，覆盖问题/estimand、可行性、假设、最小判别实验、锁定、执行、参数与方法评价、
解释、继续/优化/复现/转向/停止以及可复现归档，见
[`research-decision-cycle.md`](skills/radiology-pipeline/references/research-decision-cycle.md)；写作和投稿是其中的输出，而不是替代科研判断的主线。

### 独立发布边界

`radiology-skills` 是面向医学影像、放射组学、转录组机制与影像—机制研究的独立产品。
Academic Research Skills/ARS-Codex 与 Nature Skills 是开发时并列参考的产品，不是本项目的
上级、下级或运行依赖。我们借鉴其渐进式路由、证据到段落映射、Results-first、最短充分
证据链、建设性审阅和一致性复核等设计，再用本项目的领域规则与真实审稿语料重新约束。

安装本仓库自身的 `radiology-*` 技能即可完成科研设计、分析解释、机制判断、统计、写作、
润色、投稿前审阅、修回和全文件投稿审计；未安装任何外部 Academic/Nature Skill 时，链路
也不得降级或中断。外部 Skill 可以由用户另行调用作第二视角，但不能成为隐藏前置条件，
也不能覆盖本产品冻结的证据与结论边界。

---

## 技能索引

**40 位虚拟专科顾问**——把这 40 个技能想象成一支科研智囊团：每一位只管自己最擅长的一段，交接清楚，不越界，也不漏项；其中 `radiology-pipeline` 是通用学术导师和多阶段总入口，并在获得写入授权后维护全项目的研究护照、阶段门和材料一致性。技能标识（英文，用于实际调用）配一个好记的中文角色名。

### ⓪ 全项目总控

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-pipeline`](skills/radiology-pipeline/SKILL.md) · **学术导师与科研总控台** | EXPERIMENTAL | 接收模糊或跨阶段的学员问题，提供 direct-expert / guided-learning 指导并交给唯一专科 owner；完整项目在明确授权后维护研究护照、阶段门与断点续作，教学不自动授权模拟或写文件 |

### ① 立题与设计

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-frontier`](skills/radiology-frontier/SKILL.md) · **选题雷达** | CONTRACTED | 找前沿方向和创新点；把热点转成适合当前数据的可投稿科学问题；实时核验文献依据 |
| [`radiology-design`](skills/radiology-design/SKILL.md) · **课题诊断师** | CONTRACTED | 判断数据可行性，形成完整研究设计蓝图，并设计内部、时间、地域、多中心、外部或联邦验证方案 |
| [`radiology-clinical-domain`](skills/radiology-clinical-domain/SKILL.md) · **临床领域导航师** | CONTRACTED | 以六个器官 starter route 加急诊、肌骨、儿科、核医学/诊疗一体化四个精细包，把临床路径、参考标准、治疗时间轴、影像协议/伪影、机制假设与结论上限带入设计、审阅和学员指导 |
| [`radiology-search`](skills/radiology-search/SKILL.md) · **文献猎手** | EXPERIMENTAL | 多源检索文献与公共数据集（PubMed、arXiv、Crossref、TCIA、GEO 等），并以哈希收据冻结查询、配置、分页、语料和索引身份 |
| [`radiology-systematic-review`](skills/radiology-systematic-review/SKILL.md) · **证据综合师** | CONTRACTED | 建立范围/系统综述与 meta-analysis 全链：协议、筛选、提取、偏倚/适用性、可合并性、异质性、敏感性、证据确定性和写作交接 |

### ② 采集、数据、标注与伦理

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-acquisition-qc`](skills/radiology-acquisition-qc/SKILL.md) · **影像测量与质控师** | CONTRACTED | 冻结 CT、MRI、PET/SPECT、超声、X-ray/乳腺摄影/DBT 的 series/phase/sequence、采集、重建、定量转换、伪影、剂量、体模、重复扫描和跨站点协议漂移；输出可审计 measurement passport 与结论上限 |
| [`radiology-annotation`](skills/radiology-annotation/SKILL.md) · **标注质检员** | CONTRACTED | 设计病灶勾画标准操作流程、阅片者协议、一致性评价和掩膜几何质控 |
| [`radiology-data`](skills/radiology-data/SKILL.md) · **数据合规官** | CONTRACTED | 数据/代码可用性声明、DICOM 去标识化、仓库选择、FAIR 与可复现包；Nature 系列的 Extended Data / 补充材料 / Source Data 划分 |
| [`radiology-ethics`](skills/radiology-ethics/SKILL.md) · **伦理顾问** | CONTRACTED | 分流 human-subjects、animal-welfare 与 biosafety-biosecurity：IRB/同意/隐私、IACUC/动物福利、IBC/生物安全/双重用途治理分别核验；未知、过期、冲突或越权时 STOP，不猜审批与防护等级 |

### ③ 建模与分析

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-radiomics`](skills/radiology-radiomics/SKILL.md) · **组学工程师** | CONTRACTED | 按 IBSI / CLEAR 设计放射组学流程：预处理、特征提取、训练集内筛选、建模与数据泄漏审计、delta 放射组学、体模/重复扫描稳定性 |
| [`radiology-deep-learning`](skills/radiology-deep-learning/SKILL.md) · **深度学习审查员** | CONTRACTED | 按 CLAIM 2024 设计或审查影像深度学习研究：架构、输入、多模态、训练协议、外部验证、可解释性、不确定性量化与鲁棒性 |
| [`radiology-transcriptomics-analysis`](skills/radiology-transcriptomics-analysis/SKILL.md) · **转录组执行官** | CONTRACTED | 规划、搭建、运行、审计、复现并指导 bulk RNA、sc/snRNA 与空间流程；覆盖 FASTQ→矩阵、donor/sample 层级、QC、命令/环境、日志、真实结果与正式写作交接 |
| [`radiology-radiogenomics`](skills/radiology-radiogenomics/SKILL.md) · **影像与机制科研顾问** | EXPERIMENTAL | 解释独立 bulk/scRNA/空间/病理/扰动证据支持什么机制，并审计影像—组织—细胞—分子—功能跨尺度桥与结论上限；纯影像流程、通用写作/预审/返修分别交给对应专科 owner |
| [`radiology-experiment-design`](skills/radiology-experiment-design/SKILL.md) · **机制实验设计师** | CONTRACTED | 设计、审阅和解释 IHC/mIF、组织、细胞、类器官、动物、遗传/药理扰动、target engagement 与 rescue；锁定对照、重复、随机/盲法、剂量时间、停止规则和因果结论上限 |
| [`radiology-method-evaluation`](skills/radiology-method-evaluation/SKILL.md) · **参数与方法学评估师** | CONTRACTED | 独立设计、审阅或解释参数、评价指标与方法适配；覆盖影像/radiomics/DL、bulk、scRNA、空间、病理、多组学、扰动和跨尺度机制研究的公平 benchmark、消融、敏感性、稳健性、失败边界及论文证据放置 |
| [`radiology-stats`](skills/radiology-stats/SKILL.md) · **统计军师** | EXPERIMENTAL | 单研究推断、meta-analysis 与机制实验统计/功效：DTA/预后/患病率/关联/可靠性/预测性能合并，依赖效应、混合模型、donor/litter/cage/cluster 单位、重复测量与 attrition；关键输入不足时返回 `BIOSTATISTICIAN_REQUIRED` |

### ④ 写作、图表与报告规范

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-writing`](skills/radiology-writing/SKILL.md) · **论文架构师** | CONTRACTED | 构建 _Radiology_ 风格（结构化摘要、一句话结论、要点框）或 Nature 系列风格（非结构化摘要）稿件：方法、结果、讨论 |
| [`radiology-figure`](skills/radiology-figure/SKILL.md) · **图表设计师** | EXPERIMENTAL | 生成投稿级统计图和影像图版：ROC 曲线、森林图、校准曲线、生存曲线、决策曲线、患者筛选流程图、MRI/CT 图版、图文摘要；同时支持 _Radiology_ 与 Nature 系列两套尺寸/字母规格 |
| [`radiology-table`](skills/radiology-table/SKILL.md) · **表格审计师** | EXPERIMENTAL | 制作并核验 Table 1、Cox/Logistic 回归、模型性能、特征筛选/权重、消融、阅片者、影像基因组和补充表，保证数值与正文/图一致 |
| [`radiology-polishing`](skills/radiology-polishing/SKILL.md) · **定稿抛光师** | CONTRACTED | 按 _Radiology_ 或 Nature 系列行文规范润色英文，校准统计表达（含期刊相关的数字格式差异）、语气、时态，标出结论夸大之处 |
| [`radiology-reporting`](skills/radiology-reporting/SKILL.md) · **规范审计员** | CONTRACTED | 将稿件路由到正确报告规范并逐项审计：CLAIM、TRIPOD+AI、CLEAR、METRICS、RQS、IBSI、STARD 等，Nature 系列另加 Reporting Summary，并可对齐 FUTURE-AI 可信 AI 框架 |
| [`radiology-reader`](skills/radiology-reader/SKILL.md) · **双语精读官** | CONTRACTED | 按所需深度精读、总结或翻译影像论文；全文转换须有用户提供的文本或适当许可，保留统计、来源位置和图表再利用边界 |
| [`radiology-citation`](skills/radiology-citation/SKILL.md) · **引文核验官** | CONTRACTED | 为论点检索并验证影像期刊参考文献，导出 RIS / EndNote / BibTeX 格式 |

### ⑤ 投稿、回复、转化与基金

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-journal`](skills/radiology-journal/SKILL.md) · **投稿参谋** | CONTRACTED | 根据文章真实强弱项建立投稿梯队：冲刺、主投、稳妥，并实时核对期刊收稿范围；含 _Radiology_ 家族与 Nature 系列两套投稿前检查清单 |
| [`radiology-submission`](skills/radiology-submission/SKILL.md) · **投稿包管家** | EXPERIMENTAL | 用可执行 intake 精确路由 Radiology、Nature、Lancet、Cell、npj、Advanced Science、JAMA 等 11 刊的指定主要 article type；把研究范围、project state、模态角色、scientific handoff/prereview、analysis/claim/response 冻结摘要带入 schema 2.5，逐文件审计稿件投稿包；另以独立 schema 核验精确会议/年度/类型的 portal 字段、文件、live-call、embargo、披露、隐私、权利与作者批准，并只停在 `HUMAN_PORTAL_ACTION_REQUIRED`；转投/跨年度必须重新画像，未覆盖或不可核验规则一律 fail-closed |
| [`radiology-prereview`](skills/radiology-prereview/SKILL.md) · **模拟审稿官** | EXPERIMENTAL | 投稿前模拟严苛审稿，提前暴露直接拒稿/大修风险 |
| [`radiology-response`](skills/radiology-response/SKILL.md) · **修回信写作与核验** | EXPERIMENTAL | 适用于影像、radiomics、bulk/scRNA、空间、多组学和机制论文；逐条裁决审稿要求，写出 method–result–location–boundary 闭环，并独立核验返修稿 |
| [`radiology-translation`](skills/radiology-translation/SKILL.md) · **临床转化顾问** | CONTRACTED | 设计临床转化证据链：使用场景、多阅片者对照研究、阈值到临床动作、前瞻验证、PACS/RIS 接入 |
| [`radiology-grant`](skills/radiology-grant/SKILL.md) · **标书评审与重构师** | CONTRACTED | 覆盖国自然/省自然/院内基金与 NIH/NSF/ERC/Wellcome：先冻结当年申报要求和资格，再进行概念分诊、分项科学评审、模拟会评、重构起草与修订闭环；影像研究额外检查采集/标注、泄漏、独立单位、外部验证和临床影响 |
| [`radiology-paper2ppt`](skills/radiology-paper2ppt/SKILL.md) · **科研演示架构师** | CONTRACTED | 规划、制作、编辑或修复组会/读片会、文献汇报、会议报告、标书答辩、论文答辩和项目进展 PPTX；从受众与决策目标路由到叙事、证据、影像完整性、可访问性、演练与逐页渲染 QA，并把证据关键数字/表格/公式/引用限定为可编辑对象或可追溯源图，执行 editable-PPTX parity 检查 |

### ⑥ 科研治理、运行与复现

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-research-integrity`](skills/radiology-research-integrity/SKILL.md) · **科研诚信审计官** | CONTRACTED | 中立审计署名/CRediT、COI、生成式 AI 使用、选择性报告及文本/数据/影像完整性；记录证据、正当程序和升级路径，不自行裁定 misconduct |
| [`radiology-research-ops`](skills/radiology-research-ops/SKILL.md) · **科研运行经理** | CONTRACTED | 建立多中心 RACI、站点依赖、里程碑、资源、冻结、偏差、风险升级和收尾台账；不替代科学设计或机构授权 |
| [`radiology-reproducibility`](skills/radiology-reproducibility/SKILL.md) · **计算复现审计师** | CONTRACTED | 冻结输入、代码、配置、环境、权重、运行与容差，签发逐结果 replay receipt；计算轴止于独立同数据复现，外部复制/迁移作为独立科学验证轴交回设计/转化 owner |

### ⑦ 共识、定性与经济评价

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-consensus-guideline`](skills/radiology-consensus-guideline/SKILL.md) · **共识与指南方法师** | CONTRACTED | 设计/审计 Delphi、名义组和指南：小组遴选、COI、证据到推荐、匿名投票阈值、异议、外部审阅与更新 |
| [`radiology-qualitative-mixed-methods`](skills/radiology-qualitative-mixed-methods/SKILL.md) · **定性与混合方法师** | CONTRACTED | 设计访谈、焦点小组、观察、think-aloud、抽样充分性、反身性分析及 joint display；保留负例和定量—定性分歧 |
| [`radiology-health-economics`](skills/radiology-health-economics/SKILL.md) · **影像卫生经济学家** | CONTRACTED | 设计/审计 CEA/CUA、成本后果、预算影响、决策树/Markov、QALY/ICER、PSA/情景/VOI 与 CHEERS/HTA 交接 |

### ⑧ 传播、影响与创新转化

| 技能标识 · 角色名 | 状态 | 解决什么问题 |
|---|---|---|
| [`radiology-dissemination`](skills/radiology-dissemination/SKILL.md) · **科研传播策划师** | CONTRACTED | 把冻结证据转成海报、通俗摘要、政策/利益相关方简报和媒体衍生物，绑定来源、版本、隐私、无障碍与撤回计划；reach 不等于 impact |
| [`radiology-bibliometrics`](skills/radiology-bibliometrics/SKILL.md) · **负责任文献计量师** | CONTRACTED | 冻结数据库/检索日期，完成作者机构消歧、计数、归一化、网络和敏感性分析；指标不自动等于科研质量或个人评价 |
| [`radiology-innovation-transfer`](skills/radiology-innovation-transfer/SKILL.md) · **创新转化边界官** | CONTRACTED | 在公开披露/技术转移前整理发明状态、现有技术检索交接、贡献者—发明人边界、软件/数据/IP 权利与机构升级路径；不出具法律意见 |

> 状态由机器 registry 派生：**CONTRACTED** = 入口、边界和内容已成契约，但没有专属可执行能力门或只有静态合同检查；**EXPERIMENTAL** = 专属可执行工件门已在当前树通过，但来源、行为裁决或发布制品证据仍未闭合；**VALIDATED** = 可执行门、来源、合格人工行为裁决和哈希发布制品身份全部闭合。
> 当前 40 个 Skill 的 behavior receipt 均为 `NOT_ADJUDICATED`，所以没有任何 `VALIDATED` 或“稳定版”能力；静态字符串、清单或路由 `PASS` 不会升级成熟度。
> 详细规则见 [`capability maturity and release governance`](skills/radiology-pipeline/references/capability-maturity-and-release-governance.md)，机器事实源见 [`capability-maturity-registry.json`](skills/radiology-pipeline/references/capability-maturity-registry.json)。

---

## "我现在卡在……"快速选择

| 需求 | 推荐技能 |
|---|---|
| 这批数据能不能做？能做成什么级别？ | `radiology-design` 课题诊断师 |
| 想从 data 一直做到全部图表、论文和投稿材料 | `radiology-pipeline` 科研总控台 |
| 想找近三年前沿方向和创新点 | `radiology-frontier` 选题雷达 + `radiology-search` 文献猎手 |
| 需要系统梳理文献或公共数据集 | `radiology-search` 文献猎手 |
| 要做正式范围综述、系统综述或 meta-analysis | `radiology-systematic-review` 证据综合师；检索接 `radiology-search`，统计合并接 `radiology-stats` |
| 需要疾病/器官特异的临床问题、参考标准、治疗时间轴和影像伪影约束，含急诊、肌骨、儿科或核医学/诊疗一体化 | `radiology-clinical-domain` 临床领域导航师 |
| 需要用 TCIA / TCGA / GEO 做外部验证或机制分析 | `radiology-data` + `radiology-radiogenomics` + `radiology-search` |
| 要实际搭建、运行或复现 bulk RNA、sc/snRNA、空间转录组流程 | `radiology-transcriptomics-analysis` 转录组执行官 |
| 要解释 bulk RNA、sc/snRNA、空间结果支持什么机制 | `radiology-radiogenomics`（mechanism-only 路由） |
| 要设计 IHC、扰动、target engagement、rescue、类器官或动物验证 | `radiology-experiment-design` 机制实验设计师 |
| 想把影像表型连接到病理、细胞状态、分子程序或扰动证据 | `radiology-radiogenomics`（imaging-mechanism 路由） |
| 需要导师式比较保守/标准/进阶课题，或尚不清楚应从哪个环节开始 | `radiology-pipeline` academic mentor；明确当前决策后交给唯一专科 owner |
| 采集、重建、序列/时相、伪影、剂量或定量测量是否足以支持结论 | `radiology-acquisition-qc` 影像测量与质控师 |
| 影像组学流程怕不规范 | `radiology-radiomics` + `radiology-acquisition-qc` + `radiology-annotation` + `radiology-reporting` |
| 深度学习模型怕数据泄漏或缺少外部验证 | `radiology-deep-learning` + `radiology-design` + `radiology-stats` |
| 深度学习模型没有可解释性/不确定性证据 | `radiology-deep-learning` 深度学习审查员 |
| 参数、超参数、阈值、评价指标、方法比较、消融或敏感性是否合理 | `radiology-method-evaluation` 参数与方法学评估师；需实际配置/运行时再接领域技能，需差值/CI/检验时再接 `radiology-stats` |
| 模型评价、AUC 比较、校准、决策曲线、样本量不会写 | `radiology-stats` 统计军师 |
| 多中心、外部验证、中心效应、扫描仪差异不知道怎么处理 | `radiology-design` + `radiology-stats` |
| 论文要按高水平期刊规范补齐 | `radiology-reporting` 规范审计员 |
| 系统综述要核对 PRISMA 2020、P、ScR、S、LSR、COSMIN 或 DTA | `radiology-reporting` 规范审计员先按 general / protocol / scoping / search / living / measurement-instrument / diagnostic-accuracy 条件路由；科学方法链仍由 `radiology-systematic-review` 负责 |
| 想投 Nature 系列但不确定格式差异 | `radiology-writing` + `radiology-figure` + `radiology-reporting` |
| 中文实验记录要变成英文方法/结果/讨论 | `radiology-writing` + `radiology-polishing` |
| 要精读一篇影像论文并保留中英对照、图表和原文定位 | `radiology-reader` 双语精读官 |
| 需要核验某个论点是否真被文献支持并导出引用 | `radiology-citation` 引文核验官 |
| 要检查 IRB/同意/隐私，或实验的动物伦理、生物安全和治理门禁 | `radiology-ethics` 伦理顾问 |
| 图表和图例需要投稿级输出 | `radiology-figure` 图表设计师 |
| Table 1、Cox/模型性能表、特征权重表需要统一排版和审计 | `radiology-table` 表格审计师 |
| 投稿前想找出致命问题 | `radiology-prereview` 模拟审稿官 |
| 不知道该投哪个期刊 | `radiology-journal` 投稿参谋 |
| 已定期刊，要把所有文件整理成可上传的完整投稿包 | `radiology-submission` 投稿包管家 |
| 已写好会议摘要，要核验当届 portal 最终字段和上传文件 | `radiology-submission`；摘要内容与受众策略仍交 `radiology-dissemination` |
| 审稿意见很复杂，想逐条回应 | `radiology-response` 修回信写作与核验 |
| 想做阅片者研究、前瞻验证或临床效用评估 | `radiology-translation` 临床转化顾问 |
| 想起草、模拟评审或修订国自然/省自然标书 | `radiology-grant` 标书评审与重构师 |
| 想同步申请 NIH / ERC / Wellcome，但不确定自己有没有资格 | `radiology-grant`（国际基金部分） |
| 想做组会、读片会、会议报告、标书/论文答辩或项目进展 PPT | `radiology-paper2ppt` 科研演示架构师；标书内容先交 `radiology-grant` 冻结 |
| 要核查署名、COI、AI 使用、选择性报告或图像/数据/文本完整性 | `radiology-research-integrity` 科研诚信审计官；伦理审批问题仍交 `radiology-ethics` |
| 要管理多中心 RACI、站点依赖、资源、冻结、延期、风险和收尾 | `radiology-research-ops` 科研运行经理 |
| 要证明代码/配置/环境可重跑或做独立 replay | `radiology-reproducibility` 计算复现审计师；数据共享仍交 `radiology-data` |
| 要做 Delphi、共识声明或证据到推荐的指南 | `radiology-consensus-guideline` 共识与指南方法师；证据综合接 `radiology-systematic-review` |
| 要设计访谈、焦点小组、think-aloud 或 mixed-methods joint display | `radiology-qualitative-mixed-methods` 定性与混合方法师 |
| 要做 CEA/CUA、QALY/ICER、预算影响、Markov、PSA 或 VOI | `radiology-health-economics` 影像卫生经济学家；基金经费表仍交 `radiology-grant` |
| 要做会议摘要内容、海报、通俗摘要、政策简报、新闻稿或社交媒体传播 | `radiology-dissemination` 科研传播策划师；最终会议 portal 交 `radiology-submission`，完整 PPTX 仍交 `radiology-paper2ppt` |
| 要做引文网络、作者机构消歧、领域归一化或影响快照 | `radiology-bibliometrics` 负责任文献计量师；找文献仍交 `radiology-search` |
| 要做发明披露、现有技术检索交接、权利边界或技术转移准备 | `radiology-innovation-transfer` 创新转化边界官；法律结论交机构专业人员 |

---

## 核心专业支柱

### `radiology-reporting` 规范审计员：报告规范与投稿合规骨架

把每一类影像研究路由到正确清单，并逐项审计是否满足投稿要求：**CLAIM 2024**、**TRIPOD+AI 2024**、PROBAST+AI 2025、**CLEAR 2023**、**METRICS 2024**、RQS / RQS 2.0、**IBSI**、**STARD 2015 / STARD-AI 2025**、**PRISMA 2020 / P / ScR / LSR / S / COSMIN / DTA**、**QUADAS-3 v1.2**（比较性 DTA 同时使用 QUADAS-C）、CONSORT 2025 / SPIRIT 2025（含 AI 扩展）等——各规范现行版本与出处以 `skills/radiology-reporting/references/guideline-versions.md` 为单一真源；投 Nature 系列时再叠加 **Reporting Summary**，并用 **FUTURE-AI**（公平性、普适性、可追溯性、可用性、鲁棒性、可解释性）框架检查部署类声称是否有证据支撑。它回答的问题是：审稿人会按什么标准检查你，你现在还缺什么。

### `radiology-stats` 统计军师：经得起审稿的影像统计

分三条路由覆盖单研究推断、meta-analysis 和实验推断/功效。除 AUC、校准、DCA、生存、多重性、ICC/kappa、Bland-Altman 与多阅片者外，新增随机效应/依赖效应、DTA bivariate/HSROC、患病率/发病率、HR/OR/RR、agreement 与 prediction-performance pooling；实验侧锁定 donor/litter/cage/animal/cluster 分配单位、连续/二元/计数端点、重复测量/混合模型、attrition 与 assay failure。目标不是“算出一个 P 值”或套用万能样本量，而是输出 estimand、单位、依赖、模型、输入、诊断与敏感性闭环；关键输入不足就停在 `BIOSTATISTICIAN_REQUIRED`。

### `radiology-method-evaluation` 参数与方法学评估师：判断方法学主张是否真的站得住

把论文里常被混成一句“参数设置合理、结果稳健”的内容拆成三份独立判断：参数是否有来源、选择数据、冻结点和失败边界；评价指标是否匹配任务、独立单位、阈值与不确定性；方法是否匹配问题、estimand、数据层级和假设。它既能在实验前设计公平 benchmark、消融、负对照和最小敏感性方案，也能审阅 Methods、配置、日志和真实结果，并把已验证证据准确安排到 Methods、Results、图表、Supplement 和 Discussion。领域模块负责实际配置与运行，统计模块负责差值、CI 和多重性；本模块负责决定这些证据能否支撑“方法更优、组件有效、参数稳健”以及主张必须降到哪里。

### `radiology-radiogenomics` 影像与机制科研顾问：机制解释与跨尺度证据桥

声明式 router 只主责 `mechanism-only` 与 `imaging-mechanism`：前者判断 bulk RNA、sc/snRNA、空间、病理或扰动证据能支持到哪一级机制，后者用 patient–lesion–region–block–section–cell/time 溯源审计影像表型到组织、细胞、分子与功能的证据桥。它负责 competing mechanisms、matched n、证据状态、因果边界和 claim ceiling；纯影像流程、转录组执行、通用写作、整稿预审和返修信分别交给各自唯一 owner。需要通用导师式比较或尚未明确当前决策时，先进入 `radiology-pipeline` academic mentor。

### `radiology-transcriptomics-analysis` 转录组执行官：把“会解读”延伸到“真实可运行”

将 bulk RNA、sc/snRNA 和空间转录组拆成可执行状态机：既可从矩阵/对象开始，也可走可审计的 FASTQ→矩阵前端，冻结 sample sheet、chemistry、reference/index、命令、日志、cell/spot calling 或影像解码证据；再完成 donor–sample 身份核对、QC、normalization/integration、差异分析/pseudobulk、注释与空间统计。计划、代码就绪、真实运行、运行失败、复现完成严格分开；新增导师三档路线与正式写作交接，细胞、spot、section 和技术重复不会被冒充为患者/供体样本量。

### `radiology-experiment-design` 机制实验设计师：把机制假说变成可证伪实验

围绕“主假说 vs 竞争解释”选择最弱但足够判别的实验体系，覆盖 IHC/mIF、组织检测、细胞、类器官、动物、遗传/药理扰动、target engagement 和 rescue。每个方案同时给最低可判定、增强证据链和资源受限路线，明确阳性/阴性/载体/vehicle/批次/毒性对照、随机盲法、重复层级、剂量时间冻结、失败解释、资源与治理；本地 SOP 和成功经验只在记录的适用边界内复用。

### `radiology-systematic-review` 证据综合师：不是“搜到很多文章”，而是可审计地回答问题

按 scoping、叙事系统综述、诊断准确性、预测/radiomics/AI、预后、干预、组学机制、患病率/发病率、观察性关联、可靠性/一致性/方法比较十条路线建立协议、living/static/retired 状态、检索式同行复核、双人筛选、study-family 去重、提取、设计匹配的偏倚与适用性评估，并在任何森林图之前返回 `POOL / STRATIFY / NARRATIVE / STOP_FOR_REPAIR`。患者、病灶、读者、设备、细胞和 spot 的依赖结构、异质性、敏感性和证据确定性会直接约束结论与写作。

### `radiology-clinical-domain` 临床领域导航师：让方法回答真实疾病问题

以六个器官 starter route 加四个精细 playbook（急诊、肌骨、儿科、核医学/诊疗一体化）把临床场景、人口/终点/参考标准、采集协议与伪影、治疗和时间轴混杂、机制假设、验证阶梯、结论上限、审稿红旗与学员启发问题接到研究链。指南会变化的条目必须实时核验；团队自己的临床专家经验通过可追溯档案积累，不能被写成所有机构都适用的规则。

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

每个 `skills/radiology-*` 文件夹都是一个可安装单元。请复制整个文件夹，而不是只复制 `SKILL.md`，因为大多数技能依赖 `references/` 目录里的规则文件。

### Claude Code / Cowork 插件市场

```bash
/plugin marketplace add <path-or-git-url-to-radiology-skills>
/plugin install radiology-skills
/reload-plugins
```

安装后可以直接用自然语言触发，例如：

```text
这批多中心肝癌 MRI 能不能做研究？帮我判断可行性并设计外部验证方案。
帮我审查这个放射组学流程是否符合 IBSI / CLEAR，有没有数据泄漏。
按 CLAIM 2024 审计这篇影像深度学习论文，列出投稿前必须补齐的问题。
投稿前帮我模拟审稿，并给出致命问题/大修/小修分级的修改清单。
把这个研究改写成国自然标书：科学问题、技术路线、创新点、可行性。
我们也想申请 NIH R01，能不能用同一份研究改写？先看看我有没有资格申请。
根据当年官方 call 对这份国自然影像标书做模拟审阅，按评审准则给出证据锚点、严重度和可闭环修订项。
把已冻结的标书或本团队结果做成 10 分钟答辩/会议 PPTX，保留证据源、影像上下文和演讲者备注，并逐页渲染 QA。
```

### Codex / 其他本地 agent

```bash
mkdir -p ~/.codex/skills
for d in skills/radiology-*; do cp -R "$d" ~/.codex/skills/; done
```

更多安装说明与检索 MCP 配置见 [`install.md`](install.md)。

## 独立发布边界

GitHub/插件发行只采用 [`release-allowlist.txt`](release-allowlist.txt) 中的运行文件；本地
`research/`、`tmp/`、下载 PDF、OCR/依赖缓存和编译产物不属于产品，也不应被打包或默认
再分发。发布前运行 [`scripts/validate_release_boundary.ps1`](scripts/validate_release_boundary.ps1)
与 standalone validator；完整要求见 [`RELEASE.md`](RELEASE.md)。当前工作区是否存在目录
`.git` 不能证明已绑定有效仓库，初始化、远端和待提交清单必须由发布者另行确认。

---

## 新增技能的约定

```text
skills/radiology-<主题>/
├── SKILL.md          # 必需：仅 name/description frontmatter + 精简入口工作流
├── agents/openai.yaml# 推荐：Codex 界面名称、简介和默认调用提示
├── references/       # 按需：详细规则，必须从 SKILL.md 直接路由
├── scripts/          # 按需：重复且需要确定性的检查/生成脚本
└── assets/           # 按需：交付模板与可复用资源；README 为可选的人类说明
```

新增后请同步更新本 README 的 [技能索引](#技能索引) 和 [快速选择](#我现在卡在快速选择)，并给新技能起一个符合"虚拟专科顾问"风格的中文角色名。

SKILL.md 正文使用标准骨架：`Core stance` → `When to use`（须含中英文真实用户说法）→ `When to open extra files` → `Workflow` → `Output contract` → `Boundaries` → `Handoffs`。以门禁为中心的技能可使用已批准的变体骨架（`Non-negotiable boundaries` → `Input passport` → `Route by mode` / `Choose the … mode` → `STOP gates` → …）。无论采用哪种骨架，入口文件都必须暴露触发面（`When to use` 或等价的 mode/need 路由表），由 `scripts/test_progressive_disclosure_contracts.py` 机器约束。模板中的待填占位符统一写带括号哨兵 `[AUTHOR_INPUT_NEEDED]`（脚本按裸词匹配，两种写法都会被拦截，但模板内只用带括号形式）。

跨技能引用约定：正文中的 `radiology-xxx/yyy.md` 一律解析为 `skills/radiology-xxx/references/yyy.md`（速写省略 `references/`）；引用本 skill 内部文件时用 `references/yyy.md`。规范版本号不硬编码在各技能里——以 `skills/radiology-reporting/references/guideline-versions.md` 为单一真源并定期核对。

---

## 更新记录

- **2026-09-04** — 修订 1.10.1：全库审阅并交叉复查旧参考与新主入口的冲突。修复删失生存的模型比较、纵向/多病灶/多序列联结键、随访与插补边界、NIH 外国机构直接申请及 ERC Synergy 特例；按任务条件化 DCA、NRI、读者研究、伦理决定、混合研究整合和非临床共识；纠正引用访问深度、全文再利用、选刊承诺及 NSFC 时间线。简单任务采用最小交接，沿用用户已给出的写入授权；图表审阅与创建分开。可粘贴报告模板去除未提供的读者、训练、分析及结果事实，统一实际输入占位。来源新鲜度按逐行 Accessed 检查，支持部分刷新和缩进表格反例；会议投稿正常样例与真实运行日期同步，保留过期/未来日期拒绝检查。冻结行为用例扩至 64 个，仍未将静态检查或多代理审阅当作真实模型的独立行为验证。
- **2026-08（十）** — 发布 1.10.0：行为评测扩至 52 个冻结用例并实现 40 技能 target 全覆盖（补 ambiguous/compound 分布、pipeline 路由/授权及 NSFC 官方冲突与影像代码/方法学越界场景），注册表新增 `release_blocking` 字段与逐技能覆盖硬门；`radiology-grant` 新增 2024—2026 年度变化与来源台账、在职研究生资格冲突和合作协议时点门禁、面上/青年 C 三段式正文方法、H18/H27/H28/H29 与临床专项年度路由，以及 CLAIM/STARD-AI/TRIPOD+AI/PROBAST+AI/CLEAR/IBSI/METRICS/QIBA 按研究任务选择的框架；六个技能补齐 When to use 触发面与中文说法，10 个高频技能 description 加中文关键词；三处所有权接缝（ICC 阈值 provenance、reader-study 设计 vs MRMC 分析、方法级可行性）连同 grant 等下游引用点完成划界；全局路由补齐 12 个 learner handoff 字段与学位论文触发行；dissemination 新增已发布衍生物更正/撤回的 lifecycle 模式；design 可行性四态绑定机器可读 token 与治理三态；reporting 清单审计行统一为六列并修正 QUADAS/TRIPOD+AI 措辞与 stat-reporting 归属；radiogenomics STOP rescue 统一六字段；translation 补齐 Evidence transition register 定义；模板占位符统一为带括号哨兵；behavior-evals 共享哈希/JSON 辅助抽取至 `eval_common.py`；测试套件增加无工具链环境的 skip 守卫；修正 LICENSE 版权人署名、文档个人路径占位符与发布树哈希排序一致性；QUADAS-3 v1.2、NIH 涉外新规、NSFC 2024—2026、STARD-AI 2025 与 FDA 快照等高风险断言经官方一手来源联网复核确认。
- **2026-08（九）** — 发布 1.9.0：建立权威科研生命周期能力图与 40-skill 全覆盖路由边界；补齐 DICOM 全表面去标识、患者级连接基数、掩膜物理空间、MRS/fMRI/DTI 与局部扩展门、radiomics/保形预测/基础模型污染和隐私、合成影像及临床效用等高风险结论边界；新增能力成熟度机器目录、来源新鲜度治理、渐进披露 lint、检索运行回执、动作授权轨迹、实验谱系、真实图表 CLI 测试和双重验证的哈希发布构建器。行为评测仍待真实模型运行与合格人工裁决，因此 0 个能力被标为 `VALIDATED`。
- **2026-08（八）** — 发布 1.8.0：基于原生 Codex 对开源科研 skill 的对照审读和真实提示试跑，增加机器可检的模糊请求澄清门与运行观察→跨运行改进候选闭环；补齐会议 portal 接收能力、compact handoff、bibliometrics→传播交接及 scientific prereview receipt 1.2；科研 PPT 新增证据载体保真等级、可见缺失标记和 editable-PPTX parity；纠正动态来源 URL/版本状态并加入 Crossmark 佐证边界。
- **2026-08（七）** — 发布 1.7.0：新增 P2 科研影响力层 `radiology-dissemination`、`radiology-bibliometrics`、`radiology-innovation-transfer`，并把海报/通俗摘要/政策简报、负责任指标解释、发明披露与技术转移边界接入发表后版本、纠错、更新和退役生命周期；投稿端补齐署名/CRediT、AI 使用与公开获取 handoff，写作端新增 monograph/article-based 学位论文架构和 thesis-to-paper 路由。
- **2026-08（六）** — 发布 1.6.0：新增 `radiology-qualitative-mixed-methods`、`radiology-health-economics`、`radiology-reproducibility`，覆盖访谈/焦点小组/think-aloud、反身性与 mixed-methods integration，CEA/CUA/BIA、QALY/ICER、PSA/VOI，以及 `TRACEABLE → RERUNNABLE → REPLAYED → INDEPENDENTLY_REPRODUCED` 计算复现轴；外部复制/运输另列科学验证轴，不要求先做同数据独立重放。临床转化升级为验证、效用、监管、经济、实施与生产监测相互独立的七轴状态机。
- **2026-08（五）** — 发布 1.5.0：新增 `radiology-research-integrity`、`radiology-research-ops`、`radiology-consensus-guideline`，把署名/COI/AI 使用/选择性报告与图像数据完整性、多中心 RACI/资源/冻结/偏差/风险/收尾、Delphi/名义组/证据到推荐/投票/异议/更新做成独立 owner；同时扩充 living DMP、Registered Reports、PPI/equity、受邀同行评审保密/COI/AI 门禁及治理卫星台账。

- **2026-08（四）** — 发布 1.4.0：不新增重复 owner，将 `radiology-grant` 扩展为“当年 call/eligibility 门禁 → 标准化科学评审/模拟会评 → 修订闭环”的标书评审与重构 skill，并对齐 NSFC 2026 申请书改版及 NIH 等当前评审框架；将 `radiology-paper2ppt` 扩展为组会、会议、标书/论文答辩、项目进展的科研演示路由，新增 audience/decision passport、assertion–evidence 叙事、影像 PHI/显示完整性、可访问性、演练和逐页渲染 QA；全局路由明确区分“审标书”与“做标书答辩”。
- **2026-08（三）** — 发布 1.3.0：新增 `radiology-acquisition-qc` 唯一 owner，以 measurement passport 串联 CT、MRI、PET/SPECT、超声、X-ray/乳腺摄影/DBT 的采集、重建、定量转换、伪影、体模、重复扫描和协议漂移；补齐 detection、segmentation、diagnosis、prognosis、response、reconstruction 与 report/VLM 七类任务契约，以及主研究 protocol/SAP、ground truth、测量学/因果/纵向统计、临床影响与人因实施规则；临床领域新增急诊、肌骨、儿科和核医学/诊疗一体化精细包，并以 D4/D5/D9 开放科学门禁绑定冻结、执行与复用。DTA 偏倚评估主路由升级至 QUADAS-3 v1.2，比较研究配套 QUADAS-C；发现描述仍受 5000 字符本地预算和唯一 owner 回归约束。
- **2026-08（二）** — 发布 1.2.0：扩展为 30 个独立模块，新增 `radiology-clinical-domain`、`radiology-systematic-review`、`radiology-transcriptomics-analysis` 和 `radiology-experiment-design`；补齐疾病/器官领域 playbook、十类正式证据综合、FASTQ→矩阵及 bulk/scRNA/空间执行状态机、导师/写作交接和功能机制实验链。新增本地临床专家、实验能力/机制验证、转录组运行/失败、参数方法与真实审稿修回经验注册表；加入 `evidence-synthesis` 项目态、PRISMA 2020 / P / ScR / S / LSR / COSMIN / DTA 条件路由和独立发行白名单。全局路由明确区分检索 vs 系统综述、执行 vs 机制解释 vs 方法评价、临床语境 vs 总体设计、湿实验设计 vs 物理实验执行，并保持产品运行时独立。
- **2026-08** — 扩展为 26 个独立模块：新增 `radiology-method-evaluation` 参数与方法学评估师，把参数来源/选择/冻结/敏感性、评价指标适配、方法—问题—数据—假设闭环、公平 benchmark、消融、负对照、失败边界和论文证据放置做成可单独调用的科研工作流；同时新增全产品“当前科研决策→唯一主责→明确协作/禁止吞并”路由合同与 26 条正向、10 条边界测试，建立 D0–D9 科研决策循环及研究决策包，覆盖假设登记、判别实验、迭代/test-access、阴性/失败证据、继续/复现/转向/停止与知识复用；修复独立 deep-learning 项目的全局模态合同缺口。Academic Research Skills 与 Nature Skills 仅作为平级设计参考，运行时仍保持完全独立。
- **2026-07（六）** — 第二轮增量复核（以 `guideline-versions.md` 为基准的全库 reconcile + 注册表完整性反查 + 高风险条目在线抽验）：废弃版本串零残留、注册表覆盖完整；抽验更正 RQS 2.0 行为正式版口径（42 条 criteria，手工最高 56 分 / DL 最高 52 分，映射 RRL 1–9——此前沿用了出版前草稿的数字），TRIPOD-LLM 行补全作者与页码。历史审计原始材料不属于当前发行包。
- **2026-07（五）** — 首次全量独立审查后的集中修复：规范版本更新至 2025 现行（STARD-AI 2025 正式纳入路由、CONSORT/SPIRIT 2025、PROBAST+AI 2025 全库更名、CLAIM 2024 更正为 Tejani et al. 与 44 条分母）；修复样本量、公共数据集路由、投稿披露、读者/转化命名等问题，并建立 `guideline-versions.md` 单一真源和插件清单。历史审计原始材料不属于当前发行包。
- **2026-07（四）** — 与外部科研 Skill 平级对照后升级为 25 个模块：新增科研总控台、表格审计师和投稿包管家；加入研究护照、跨材料一致性、模拟数据边界、持续文献语料、三视角预审、运行 provenance、审稿承诺账本和基金停止规则。外部对照工作稿不属于当前发行包。
- **2026-07（三）** — README 全面中文化改写：补齐"核心卖点"独立板块；为全部 22 个技能设计中文角色名（如"课题诊断师""模拟审稿官""标书操盘手"），统一到"虚拟专科顾问团队"的表达框架；技能索引、快速选择、状态标签（测试版/稳定版/草案）等结构性文字全部改为中文，仅保留期刊名、基金机构名、国际标准化报告规范/统计方法的专有名称（如 CLAIM、TRIPOD+AI、ROC、AUC 等——这是国内影像科研领域的通行写法，保留是为了专业性而非疏漏）以及技能标识本身（因涉及实际调用，不能更名）。技术内容与结论未作任何改动。
- **2026-07（二）** — `radiology-grant` 新增国际基金体系（`references/international-grants.md`）：NIH R01、ERC（Starting/Consolidator/Advanced，含 2026 新两段式结构）、Wellcome Trust 的结构与评审标准，以及**面向中国申请人的真实资格核查**（NIH 2025–2026 外籍分包新规、ERC 主持机构须在欧盟/联系国、Wellcome 部分项目的地区限制），并给出更易触达的跨境路径（NSFC 国际合作项目、RGC、MSCA、基金会）。国自然/省自然保持为主线与最成熟的部分。
- **2026-07（一）** — 全套技能审查后的扩展：为写作、图表、报告规范、润色、数据、投稿策略六个技能新增 Nature 系列期刊分支（摘要结构、图表尺寸/图版字母大小写、Reporting Summary、Extended Data/Source Data、数字与参考文献格式的差异，均已标注需按具体期刊实时核实）；为深度学习技能新增可解释性/不确定性量化/鲁棒性（含 FUTURE-AI 框架引用）；为放射组学技能补充 delta 放射组学与体模/重复扫描稳定性；为选题技能补充液体活检/病理基础模型融合等前沿方向；修复图表技能内部图版字母大小写不一致的问题；补充多处技能间的衔接说明。原有的方法学规则与既有 _Radiology_ 家族内容未改动。

---

## 免责声明

这些技能用于科研选题、研究设计、方法学、统计、图表、论文写作、投稿策略、审稿回复和基金文本辅助。它们**不提供医疗建议、临床诊断或个体患者影像判读**，也不能替代生物统计、临床、伦理、监管或法律审查，**不构成基金资助资格的正式认定**。作者仍需对所有数据、分析、结论、伦理审批、投稿材料和基金申报内容的准确性与完整性负责。投稿或申报前，请确认**当前版本**的报告规范、目标期刊投稿要求、Nature Portfolio 编辑政策，以及国自然/省自然或 NIH、ERC、Wellcome 等官方基金申报指南与申请资格——这些规则变化频繁，本工具提供的是结构化的起点，不是最终依据。
