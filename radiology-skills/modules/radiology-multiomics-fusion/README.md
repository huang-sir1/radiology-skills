# radiology-multiomics-fusion

**五维融合架构师**：用于设计和审查影像、临床、病理、bulk 分子组学、单细胞/空间组学五个维度的联合建模与融合分析。

## 它能做什么

- 建立 patient-by-modality availability matrix，先看每个患者到底有哪些数据维度。
- 评估五维完整匹配样本量、事件数、中心数和缺失模式是否支撑复杂融合。
- 选择 early fusion、intermediate fusion、late fusion、graph fusion、latent-factor fusion 等架构。
- 规划 MOFA、SNF、DIABLO、iCluster、多块 PLS、深度多模态表征等方法的适用边界。
- 处理缺失模态、批次效应、中心效应、嵌套特征筛选、模态贡献和消融实验。
- 区分监督预测分支和无监督分型分支，避免把探索性结构过度写成临床预测。

## 典型触发

- “我有影像、临床、病理、转录组、单细胞，想做五维融合模型。”
- “五个模态不全，能不能做多组学融合？”
- “MOFA、DIABLO、SNF、iCluster 哪个适合我的数据？”
- “帮我设计五维多组学融合的消融实验和外部验证。”

## 边界

融合模型不能超过匹配样本量和事件数能支撑的复杂度。若五维数据不完整，应明确写成 reduced-dimensional variant，并优先选择更稳健的简单基线或 late fusion。
