# Radiology Skills

本skills由黄sir组学工作室的核心成员开发，三位成员为发表过《Radiology》原创性研究的第一作者（Huang Yuhong、Gu Wenchao、Song Xinyang），对影像组学领域有深刻认知，这是一个面向影像组学、影像深度学习和医学影像 AI 研究的全开源 Codex skill，用于帮助研究者完成前沿选题、文献梳理、课题设计、ROI/mask 标注规范、统计分析、图表规划、影像基因组学机制解析、多中心验证、公共数据库使用、伦理与复现、论文写作、投稿预审、选刊投稿、基金申报、临床转化和返修回复等。

基于 2023-2026 高水平文献，整理了 Radiology、Radiology: Artificial Intelligence、The Lancet Oncology、The Lancet Digital Health、Nature Medicine、Nature Cancer、Nature Communications、Science Advances、eClinicalMedicine、eBioMedicine、Cell Reports Medicine、npj Digital Medicine 等高影响力期刊中医学影像 AI、影像组学、影像深度学习、影像基因组学和临床转化相关研究的发表规律。这个证据层可用于辅助选题、投稿选刊、前沿设计、课题设计和基金申报等任务。

## 按需求分类

### 1. 我不知道这个课题能不能做

适合场景：你有一批 CT、MRI、PET/CT、超声、钼靶或多模态影像数据，但还不确定能做什么研究。

它会帮你梳理：

- 疾病、模态、样本量、中心数量、标签来源和终点是否足够支撑研究；
- 数据是适合做诊断、分型、分期、预后、疗效预测、复发预测，还是分割任务；
- 是否有外部验证、时间验证、临床变量、分割 mask、随访信息和病理/分子标签；
- 当前数据最适合走影像组学、深度学习、多模态融合、放射基因组学，还是先做可行性研究。

### 2. 我想找近三年的前沿方向和创新点

适合场景：你想结合自己的数据，从 Radiology、Lancet Digital Health、Nature Medicine、Nature Communications、Lancet Oncology、npj Digital Medicine、npj Precision Oncology 等高影响力期刊中寻找影像 AI 前沿。

它会帮你分析：

- 2023-2026 年 PubMed 验证的代表性高水平种子文献；
- 近三年影像组学和影像深度学习的主要趋势；
- 基础模型、自监督学习、视觉语言模型、多模态融合、放射基因组学、纵向影像、弱监督、域适应、联邦学习等方向是否适合你的数据；
- 哪些方向只是热门但不适合你当前数据；
- 如何把前沿方法转化成可执行、可投稿的研究问题。

### 3. 证据：我想知道这些建议背后有哪些近三年文献依据

适合场景：你不只是想听“前沿方向”，而是想知道这些判断来自哪些近三年高水平文章、哪些期刊发表了什么类型的研究、哪些规律可以迁移到自己的数据。

它会帮你完成：

- 提供 2023-2026 年 PubMed 验证的代表性种子文献表；
- 按报告规范、读者研究/真实世界、临床验证、多中心、影像基因组学、多组学、foundation model、生成式 AI、分布式/异质性数据等主题整理规律；
- 把文献规律转成选题规则：什么数据适合做、什么数据不建议做、最低验证要求是什么；
- 辅助判断 Nature Medicine、Lancet Digital Health、Lancet Oncology、Radiology、Cell Reports Medicine、npj Precision Oncology 等期刊的证据偏好；
- 明确哪些结论需要当天重新检索，避免把种子文献当成完整系统综述。

### 4. 我想系统梳理文献

适合场景：你需要整理影像组学、影像深度学习、医学影像 AI 或某个疾病/模态方向的高水平文献。

它会帮你完成：

- 制定 PubMed、期刊官网、出版社页面和综述的检索策略；
- 按疾病、模态、任务、模型方法、验证方式和临床场景筛选文献；
- 区分直接相关文献、可迁移方法文献、背景文献和弱相关文献；
- 从文献中总结常见研究设计、验证方式、模型路线和创新缺口。

### 5. 公库：我想使用公共数据库做验证或机制解释

适合场景：你想使用 TCIA、TCGA、GEO、CPTAC、IDC 或公开单细胞/空间转录组数据，做外部验证、影像基因组学机制解释、背景支持或方法对照。

它会帮你完成：

- 判断公共数据是适合做直接外部验证、配对影像基因组学验证、机制注释，还是只能做背景支持；
- 区分“同一患者/同一病灶/同一时间点配对数据”和“非配对公共组学数据”；
- 设计 TCIA-TCGA、GEO、CPTAC 等数据的检索、纳入排除、样本匹配和引用策略；
- 检查公共数据的疾病、模态、终点、治疗背景和样本量是否与你的研究相容；
- 避免把非配对公共数据写成直接验证，避免把公共数据混入训练集后又称为外部验证。

### 6. 我想做影像组学研究

适合场景：你计划提取 handcrafted radiomics features，使用 Pyradiomics 或类似工具做特征筛选、建模和预测。

它会重点检查：

- ROI/mask 来源、分割一致性、读片者信息和质量控制；
- 重采样、灰度离散化、归一化、滤波和 IBSI 相关设置；
- 特征筛选是否只在训练集内完成；
- 是否存在先提特征、先筛特征、先标准化再划分训练测试集的数据泄漏；
- 模型复杂度、样本量、事件数、校准、决策曲线和外部验证是否匹配。

### 7. 标注：我想把 ROI、VOI 和 mask 标注写规范

适合场景：你已经有 CT、MRI、PET/CT、超声或病理影像的 ROI/mask，但不确定病灶选择、标注流程、读片者一致性和质量控制是否足够支撑投稿。

它会帮你完成：

- 明确 2D、3D、whole tumor、largest slice、peritumoral ring、habitat 或多病灶策略；
- 设计读片者数量、年资、盲法、独立标注、共识处理和第三方裁决流程；
- 规划重复标注、ICC、Dice、Hausdorff、特征稳定性筛选和敏感性分析；
- 检查 mask 与 DICOM、NIfTI、DICOM-SEG、RTSTRUCT 的 spacing、origin、direction 和 slice order 是否一致；
- 帮你写出 Methods 中关于 ROI/mask、软件、质控和一致性评价的规范表述。

### 8. 我想做影像深度学习研究

适合场景：你想做 CNN、Transformer、3D 模型、分割模型、检测模型、预后模型、基础模型迁移、多模态模型或报告辅助模型。

它会帮你设计：

- 2D、2.5D、3D、序列模型、Transformer、基础模型或多模态融合路线；
- 小样本下是否应使用迁移学习、自监督预训练、简单基线或嵌套交叉验证；
- 图像、mask、临床变量、病理/分子标签和报告文本如何进入模型；
- 数据增强、类别不平衡、超参数搜索、基线模型和外部验证如何安排；
- 如何避免切片级随机划分、患者重叠、测试集调参和报告标签噪声。

### 9. 我想解释影像组学模型背后的生物机制

适合场景：你的影像组学模型、radiomics score 或影像深度学习模型已经完成，希望联合 bulk 转录组、单细胞转录组、空间转录组、基因组、蛋白组、代谢组、病理组学或免疫微环境数据，解释影像模型背后的生物学联系。

它会帮你完成：

- 判断组学数据是否与影像数据来自同一患者、同一病灶、同一时间点或同一空间区域；
- 设计从 radiomics score、关键影像特征、影像 habitat 或深度模型特征到基因模块、分子通路、细胞类型和空间生态位的证据链；
- 对 bulk RNA-seq 设计差异表达、GSEA/GSVA、WGCNA、免疫浸润估计和外部验证路线；
- 对单细胞转录组设计细胞注释、marker、module score、细胞状态、细胞比例、拟时序和细胞通讯分析；
- 对空间转录组设计区域差异、空间通路、细胞反卷积、空间邻域、配体-受体和影像 habitat 对应关系；
- 帮你把“影像表型 -> 分子通路 -> 细胞状态/空间生态位 -> 临床终点”的逻辑讲清楚；
- 区分相关性、机制解释、验证证据和因果结论，避免过度表述。

### 10. 我想把现有数据设计成一个完整课题

适合场景：你已经知道疾病、模态和样本量，希望形成一个可投稿的研究方案。

它会帮你明确：

- 临床问题、目标人群、预测终点和使用场景；
- 最小可行方法和更强方法；
- 内部验证、时间验证、外部验证或多中心验证方案；
- 主要指标、次要指标、校准、临床实用性和亚组分析；
- 目标期刊更看重临床验证、方法透明性、机制解释还是前沿模型。

### 11. 我想申报国自然、省自然或其他科研基金

适合场景：你准备申报国家自然科学基金、国自然青年/面上/地区项目、省级自然科学基金、院校级课题或其他科研项目，希望把影像组学、影像深度学习或医学影像 AI 方向写得更符合基金申请书的表达习惯。

它会帮你完成：

- 把论文式表述改成基金式逻辑：临床需求 -> 科学问题 -> 研究假设 -> 研究内容 -> 技术路线 -> 创新点 -> 可行性；
- 润色题目、摘要、立项依据、研究目标、研究内容、关键科学问题、技术路线、创新点、可行性分析和预期成果；
- 把“构建模型”“提高准确率”改写成更适合申报书的科学问题和研究主线；
- 强化影像表型、病理/分子标签、疗效、预后、模型泛化、可解释性和临床转化之间的逻辑；
- 识别申请书中证据不足、前期基础不足、创新点虚弱、技术路线不闭环和过度承诺的问题；
- 提醒你按当年国自然或省自然官方申报指南核验格式、字数、附件、伦理和限项要求。

### 12. 我担心模型结果不可信

适合场景：你已经有 AUC、C-index、Dice、敏感度、特异度或其他结果，但不确定是否可靠。

它会帮你审查：

- 是否按患者级划分训练集、验证集和测试集；
- 同一患者的切片、病灶、序列、期相或随访图像是否跨集合泄漏；
- 特征选择、标准化、缺失值填补、harmonization、数据增强是否发生在错误阶段；
- 是否使用测试集做阈值选择、模型选择或早停；
- 是否报告置信区间、校准、决策曲线、亚组分析和失败案例。

### 13. 统计：我想确认统计分析和模型评价是否规范

适合场景：你已经有 LASSO、logistic 回归、Cox、随机森林、SVM、XGBoost、深度学习模型、AUC、C-index、Dice、KM 曲线或 DCA，但不确定统计流程是否正确。

它会帮你审查：

- 样本量、阳性/阴性比例、事件数、删失比例、随访时间和 EPV 是否能支撑模型复杂度；
- 特征筛选、标准化、缺失值填补、阈值选择和超参数调优是否只在训练集或内部验证中完成；
- ROC、PR-AUC、C-index、time-dependent AUC、校准、DCA、Brier score、置信区间是否报告完整；
- 生存分析中 Cox、KM、风险分组、比例风险假设和固定时间点校准是否合理；
- 小样本、多特征、类别不平衡、多重检验和测试集调参等风险。

### 14. 多中心：我想处理多医院、多机器和外部验证

适合场景：你的数据来自多个医院、多个扫描仪、不同扫描协议或不同时间段，希望证明模型有泛化能力。

它会帮你完成：

- 按中心、时间、地域、扫描仪、厂家、层厚、MRI 序列、增强期相梳理数据差异；
- 设计 pooled training、center-held-out validation、temporal validation、geographic validation 或 federated learning 路线；
- 检查随机混合多中心数据是否被错误写成外部验证；
- 规划 ComBat、harmonization、domain adaptation、center-stratified validation 和中心亚组分析；
- 解释中心效应、scanner effect、batch effect 和外部中心性能下降。

### 15. 我想按高水平期刊规范来写

适合场景：你准备投 Radiology、Lancet Digital Health、Nature Medicine、eClinicalMedicine、EBioMedicine、Cell Reports Medicine、npj Digital Medicine 等期刊，需要符合影像 AI 报告规范。

它会帮你选择和应用：

- CLAIM / CLAIM 2024；
- CLEAR、RQS、METRICS 和 IBSI；
- TRIPOD+AI 和 PROBAST+AI；
- STARD-AI；
- CONSORT-AI 和 SPIRIT-AI；
- 目标期刊的数据共享、代码共享和报告要求。

### 16. 我想处理数据、mask、隐私和共享问题

适合场景：你需要整理 DICOM、NIfTI、DICOM-SEG、RTSTRUCT、mask、特征表、临床表或多中心数据。

它会帮你梳理：

- 数据目录、患者 ID、检查 ID、序列 ID、病灶 ID 和时间点；
- 图像、mask、标签、临床变量和模型输出之间的对应关系；
- 去标识化、伦理限制、数据使用协议、医院政策和受控访问；
- 数据、代码、模型权重、特征表和补充材料的可共享程度。

### 17. 伦理：我想把伦理审批、知情同意和隐私写合规

适合场景：你的研究涉及临床影像、病历、病理、基因组、转录组或多中心数据，需要写 Ethics、Consent、Data Availability 或隐私限制。

它会帮你完成：

- 明确研究是回顾性、前瞻性、注册研究还是多中心回顾性分析；
- 梳理伦理审批机构、审批编号、知情同意豁免、中心覆盖范围和数据使用协议；
- 检查 DICOM 元数据、临床表、组学数据和小样本罕见病数据的再识别风险；
- 判断原始影像、mask、特征表、模型权重、代码和组学数据能否公开、受控访问或不能共享；
- 写出不夸大、不编造的 Ethics、Consent 和 Data Availability 文本。

### 18. 复现：我想让代码、特征表和模型参数更可复现

适合场景：你准备投稿或回复审稿人，需要整理 radiomics 参数、深度学习训练配置、模型系数、代码环境、随机种子、数据字典和补充材料。

它会帮你完成：

- 规划数据字典、变量定义、ID 对应、split assignment、缺失值规则和排除病例清单；
- 整理 Pyradiomics 或其他特征提取参数：重采样、灰度离散化、滤波器、feature class、ICC 筛选；
- 整理深度学习参数：模型结构、输入尺寸、增强、loss、optimizer、learning rate、batch size、epoch、checkpoint、随机种子；
- 设计 Supplementary Tables：影像参数表、标注协议表、特征参数表、模型性能表、hyperparameter 表；
- 写 Code Availability、Data Availability 和受限共享说明。

### 19. 我想写论文或修改稿件

适合场景：你需要写 Methods、Results、Discussion、摘要、标题，或把中文作者笔记转成英文稿件内容。

它会帮你完成：

- Methods 的结构化写作；
- Results 中队列、验证集、性能、校准、亚组和失败案例的表达；
- Discussion 中贡献、局限性、临床意义和未来工作的表述；
- 避免把“相关性”写成“因果”，避免把“AUC 高”写成“可临床使用”；
- 中文研究想法到英文投稿语言的转换。

### 20. 图表：我想规划高水平论文的图、表和图例

适合场景：你的文章已经有模型结果，但不知道主图、补充图、Table 1、模型性能表、机制图、ROC、校准曲线、DCA、KM、SHAP 或 Grad-CAM 应该怎么安排。

它会帮你完成：

- 规划研究流程图、患者筛选流程图、radiomics pipeline、deep learning pipeline 和机制图；
- 设计 Table 1、模型性能表、外部验证表、影像参数表、特征表和补充材料表；
- 判断是否缺少校准曲线、决策曲线、失败案例、中心特异性结果、亚组分析或读者研究图；
- 帮你写 figure legend，明确样本量、队列、指标、置信区间和统计检验；
- 避免只放 ROC、图表与结论脱节、可解释性图被过度解释。

### 21. 预审：我想投稿前模拟审稿人挑问题

适合场景：论文已经基本写好，你想在投稿前从方法学、报告规范、图表、统计、数据共享和目标期刊角度做一次严格检查。

它会帮你完成：

- 识别可能导致拒稿或大修的硬伤：无患者级划分、数据泄漏、无外部验证、标签不清、标注不清、统计不完整；
- 检查 CLAIM、CLEAR、RQS、IBSI、TRIPOD+AI、PROBAST+AI、STARD-AI 等规范缺项；
- 审查摘要和 Discussion 是否把 AUC、相关性或回顾性结果写得过强；
- 给出 Methods、Results、Discussion、图表、补充材料和 Data/Code Availability 的修改优先级；
- 按目标期刊风格判断当前稿件更适合冲刺、主投还是备选。

### 22. 我想知道这篇文章适合投哪个期刊

适合场景：文章已经基本写好，你想结合现有同类文章、近年发表情况、目标期刊风格和自己的研究强弱点，判断适合投稿到哪里。

它会帮你完成：

- 从题目、摘要、Methods、Results 和 Discussion 中提炼文章类型、核心卖点和最大短板；
- 结合疾病、模态、任务、样本量、中心数量、外部验证、前瞻性、读者研究、校准和临床实用性判断稿件档位；
- 检索或整理近 3-5 年目标期刊同类文章，看哪些期刊近期发表过相似主题；
- 按“冲刺期刊、主投期刊、备选期刊”给出投稿梯队；
- 说明每个期刊的匹配理由、投稿风险和投稿前需要补强的内容；
- 避免只按影响因子选刊，避免把验证不足的文章包装成顶刊稿件。

### 23. 转化：我想把模型往临床应用、读者研究或前瞻验证推进

适合场景：你的模型已经完成回顾性验证，希望进一步设计临床使用场景、读者研究、医生+AI 增益、前瞻性验证、真实世界验证或工作流集成。

它会帮你完成：

- 明确模型服务的临床场景：筛查、诊断、分型、分期、预后、疗效预测、随访或 MDT 决策；
- 设计模型输出：风险分数、分层、mask、热图、报告辅助或治疗反应概率；
- 规划读者研究：读片者年资、随机顺序、washout、无 AI/有 AI 对比、时间和信心评分；
- 判断是否有校准、DCA、net benefit、阈值对应动作、假阳性/假阴性后果；
- 设计前瞻性验证、真实世界验证、PACS/RIS 工作流位置和部署限制；
- 避免从回顾性 AUC 直接宣称“可临床应用”。

### 24. 我需要回复审稿人

适合场景：审稿人质疑没有外部验证、样本量小、数据泄漏、分割不清楚、缺少校准、缺少临床实用性或报告规范不足。

它会帮你制定：

- 每条审稿意见的回应策略；
- 能补做的分析、不能补做时的合理解释和局限性表述；
- 对 manuscript 的具体修改位置和修改内容；
- 避免承诺没有完成的实验、外部验证、代码公开或新图表。

### 25. 我需要依据和来源

适合场景：你需要知道某个规则、建议或写法来自哪里，或者要确认最新指南和期刊要求。

它会帮你追溯：

- 报告规范和方法学建议的来源；
- 文献检索的时间范围和期刊范围；
- 近三年前沿文献的代表性 PMID；
- 需要重新联网核验的指南、期刊政策或最新文献。

## 安装

这个仓库现在支持两种安装方式：

1. `radiology-skills/`：单体总入口，适合想用一个统一 skill 处理所有影像组学、影像深度学习和医学影像 AI 任务的用户。
2. `skills/radiology-*`：模块化套件，适合想让 Codex 按任务自动触发更细分模块的用户。

更详细的安装说明见 [install.md](install.md)。

### 方式一：安装单体总入口

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

### 方式二：安装 22 个独立模块

Windows PowerShell：

```powershell
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\radiology-* "$env:USERPROFILE\.codex\skills\"
```

macOS 或 Linux：

```bash
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
mkdir -p ~/.codex/skills
cp -R skills/radiology-* ~/.codex/skills/
```

22 个独立模块包括：

| 模块 | 用途 |
|---|---|
| `radiology-frontier` | 前沿方向、创新点和高水平期刊发表规律 |
| `radiology-design` | 课题可行性、研究设计和验证策略 |
| `radiology-search` | 文献和公共数据检索、PMID/DOI 核验 |
| `radiology-annotation` | ROI/VOI/mask 标注 SOP、一致性和质控 |
| `radiology-data` | DICOM 脱敏、数据共享、代码和 FAIR |
| `radiology-ethics` | 伦理、知情同意、隐私和数据治理 |
| `radiology-radiomics` | 传统影像组学流程、IBSI/CLEAR、泄漏检查 |
| `radiology-deep-learning` | 影像深度学习、CNN/Transformer/基础模型设计 |
| `radiology-radiogenomics` | 影像基因组学、多组学、单细胞和空间转录组机制解析 |
| `radiology-stats` | ROC、DeLong、校准、DCA、MRMC、生存和样本量 |
| `radiology-figure` | Radiology 风格图表、统计图和影像 panel |
| `radiology-reporting` | CLAIM、TRIPOD+AI、CLEAR、RQS、IBSI、STARD 等规范 |
| `radiology-writing` | Radiology 风格论文结构、摘要、Methods、Results、Discussion |
| `radiology-polishing` | 英文润色、统计表述和过度结论检查 |
| `radiology-reader` | 医学影像论文中英对照精读 |
| `radiology-citation` | 影像期刊范围内的引用检索和 RIS/ENW/BibTeX 导出 |
| `radiology-prereview` | 投稿前模拟审稿和 blocker/major/minor 问题清单 |
| `radiology-journal` | 选刊、投稿梯队和期刊匹配判断 |
| `radiology-response` | 审稿意见逐点回复和返修策略 |
| `radiology-translation` | 临床转化、读者研究、前瞻验证和部署路径 |
| `radiology-grant` | 国自然、省自然和院级课题申报写作 |
| `radiology-paper2ppt` | 影像论文中文汇报 PPT |

如有需要，重启 Codex 或重新加载 skills。

## 使用

可以这样向 Codex 提问：

```text
Use $radiology-skills to design, audit, or write a radiomics or medical imaging deep learning study.
```

也可以直接用中文提问，例如：

- 我有 300 例多中心肝癌 MRI，想找近三年前沿方向并设计课题。
- 根据 2023-2026 年高水平期刊文献规律，帮我判断这批数据最适合做什么影像 AI 课题。
- 结合近三年 Radiology、Lancet Digital Health、Nature Medicine、npj Precision Oncology 等期刊发表规律，帮我找创新点。
- 影像组学模型做完了，我有 bulk RNA、单细胞和空间转录组，帮我设计机制解析路线。
- 我想申报国自然青年基金，帮我润色立项依据和科学问题。
- ROI 是两位医生勾画的，帮我设计标注 SOP 和 Methods 写法。
- 帮我检查 LASSO、Cox、C-index、校准曲线和 DCA 的统计流程是否规范。
- 帮我规划主图、补充图、Table 1、ROC、校准曲线和 figure legend。
- 投稿前帮我模拟审稿人做一次严格预审。
- 帮我整理代码、特征表、模型参数和补充材料，提高可复现性。
- 我有 4 家医院的数据，帮我设计多中心外部验证和中心差异分析。
- 我想用 TCIA、TCGA 或 GEO 做外部验证和机制解释，帮我判断怎么用。
- 帮我写伦理审批、知情同意豁免和数据共享限制的表述。
- 帮我设计读者研究、前瞻性验证和临床转化路径。
- 帮我检查这段影像组学 Methods 有没有数据泄漏。
- 我想做 CT 深度学习预后模型，帮我设计验证方案。
- 我的文章已经写好了，帮我结合近年发表情况选刊。
- 我的文章是单中心回顾性影像组学，没有外部验证，结合近三年高水平期刊规律判断能不能投 Nature Medicine 或 Lancet Digital Health。
- 审稿人说没有外部验证，帮我写回复和修改策略。

## 注意

这个 skill 用于研究设计、方法学审查和论文写作辅助，不提供临床诊断、治疗建议或针对具体患者的医学影像解读。
