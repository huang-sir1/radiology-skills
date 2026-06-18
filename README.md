# Radiology Skills

`radiology-skills` 是一个面向影像组学、影像深度学习和医学影像 AI 研究的 Codex skill，帮助研究者完成选题、课题设计、方法学审查、论文写作、选刊投稿、基金申报和审稿回复。

它适合放射科、肿瘤科、外科、核医学、超声、病理/组学交叉方向的科研使用。它不提供临床诊断或治疗建议。

## 核心特点

- **文献驱动**：内置 2023-2026 年 PubMed 验证的高水平医学影像 AI 种子文献证据层，用于辅助前沿判断、课题设计和选刊定位。
- **方法学审查**：重点检查数据泄漏、患者级划分、外部验证、ROI/mask 标注、统计分析、校准、DCA、多中心泛化和可复现性。
- **论文与投稿支持**：支持 Methods、Results、Discussion、摘要、标题、图表规划、投稿前预审、选刊和审稿回复。
- **临床医生友好**：支持中文输入，可把临床数据情况转化为研究方案、基金语言和论文逻辑。

## 文献证据层

升级版包含一个 **2023-2026 高水平文献证据层**，覆盖 Radiology、Radiology: Artificial Intelligence、The Lancet Digital Health、Nature Medicine、Nature Communications、eClinicalMedicine、Cell Reports Medicine、The Lancet Oncology、npj Precision Oncology 等期刊中的代表性医学影像 AI、影像组学、影像深度学习、影像基因组学和临床转化研究。

说明：

- 当前证据层是 PubMed 验证的代表性种子文献库，不是完整系统综述。
- 已整理代表性 PMID、期刊规律、前沿方法和选刊信号。
- 用于辅助判断方向，不替代正式投稿前的当天文献检索。

## 功能总览

| 需求 | 模块 | 主要用途 |
|---|---|---|
| 不知道数据能做什么 | 入口 / 设计 | 整理数据条件，判断可做和不建议做的方向 |
| 找近三年前沿方向 | 前沿 / 证据 / 文献 | 根据高水平文献规律匹配可行创新点 |
| 系统梳理文献 | 文献 | 制定检索策略，整理证据图谱和研究空白 |
| 做传统影像组学 | 组学 | 审查 radiomics 提取、特征筛选、建模和泄漏风险 |
| 做影像深度学习 | 深度 | 设计 CNN、Transformer、3D、分割、基础模型和多模态路线 |
| 解释生物机制 | 机制 | 联合 bulk RNA、单细胞、空间转录组、多组学和病理解释模型 |
| 规范 ROI/mask | 标注 | 设计标注 SOP、读片者一致性、ICC/Dice 和 mask 质控 |
| 检查统计分析 | 统计 | 审查样本量、事件数、LASSO、Cox、AUC、C-index、校准和 DCA |
| 检查模型可信度 | 验证 | 检查患者级划分、数据泄漏、外部验证和指标报告 |
| 处理多中心数据 | 多中心 | 设计中心外部验证、harmonization、domain shift 和中心亚组分析 |
| 使用公共数据库 | 公库 | 判断 TCIA、TCGA、GEO、CPTAC 等数据适合验证、机制还是背景支持 |
| 处理数据和隐私 | 数据 / 伦理 | 梳理 DICOM/NIfTI/mask、去标识化、IRB、知情同意和数据共享限制 |
| 提高可复现性 | 复现 | 整理代码、特征表、参数、随机种子、模型权重和补充材料 |
| 写论文和图表 | 写作 / 图表 | 起草论文段落，规划流程图、ROC、校准、DCA、KM、机制图和图例 |
| 投稿前把关 | 预审 / 规范 | 模拟审稿人检查 CLAIM、CLEAR、RQS、IBSI、TRIPOD+AI 等缺项 |
| 选择目标期刊 | 选刊 | 根据稿件强弱和近年发表规律给出投稿梯队 |
| 申报基金 | 基金 | 润色国自然、省自然等申请书的科学问题、立项依据和技术路线 |
| 临床转化 | 转化 | 设计读者研究、前瞻验证、真实世界验证和工作流集成 |
| 回复审稿人 | 回复 | 起草逐点回复、补充分析策略和修改说明 |

## 安装

Windows PowerShell：

```powershell
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\radiology-skills "$env:USERPROFILE\.codex\skills\"
```

macOS / Linux：

```bash
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
mkdir -p ~/.codex/skills
cp -R radiology-skills ~/.codex/skills/
```

安装后重启 Codex，或重新加载 skills。

## 使用示例

可以显式调用：

```text
Use $radiology-skills to design, audit, or write a radiomics or medical imaging deep learning study.
```

也可以直接中文提问：

- 我有 300 例多中心肝癌 MRI，想找近三年前沿方向并设计课题。
- 根据 2023-2026 年高水平期刊文献规律，判断这批数据最适合做什么影像 AI 课题。
- 影像组学模型做完了，我有 bulk RNA、单细胞和空间转录组，帮我设计机制解析路线。
- ROI 是两位医生勾画的，帮我设计标注 SOP 和 Methods 写法。
- 帮我检查 LASSO、Cox、C-index、校准曲线和 DCA 的统计流程是否规范。
- 投稿前帮我模拟审稿人做一次严格预审。
- 我的文章是单中心回顾性影像组学，没有外部验证，判断能不能投 Nature Medicine 或 Lancet Digital Health。
- 我想申报国自然青年基金，帮我润色立项依据和科学问题。
- 审稿人说没有外部验证，帮我写回复和修改策略。

## 边界

这个 skill 是科研设计、方法学审查和写作辅助工具。它不能替代真实数据分析、统计师审查、伦理委员会意见、正式文献系统综述或临床判断。
