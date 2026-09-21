# radiology-deep-learning

面向医学影像深度学习研究的 **CLAIM 2024 对齐设计与审计工作流**。它关注的不只是模型架构，而是高水平期刊真正会追问的证据链：patient-level split、外部验证、输入泄漏、训练协议、超参数选择、校准、临床比较和可复现性。

## 它能做什么

- 选择并解释 **model design**：2D / 2.5D / 3D CNN、Transformer / ViT、U-Net / nnU-Net、检测、分割、预后 head、foundation-model transfer。
- 定义 **input spec**：图像、mask、临床变量、报告文本、分子数据如何进入模型，以及 early / intermediate / late fusion。
- 规范 **training protocol**：transfer / self-supervised / from-scratch、patient-level split、nested CV、augmentation、class imbalance、optimizer、schedule、seed、checkpoint rule。
- 审计 **leakage & validity**：slice-level leakage、patient overlap、post-outcome variables、fit-on-training、调参和评估集污染。
- 补齐 **可解释性、不确定性量化与可信 AI**：Grad-CAM / SHAP / attention 有边界报告，MC dropout / ensemble / conformal 不确定性估计，robustness / OOD / fairness 检查，foundation-model 适配与 FUTURE-AI 框架。
- 输出 CLAIM-aligned Methods 段落和需要补齐的 reporting 项。

## 典型触发

- “帮我设计影像深度学习课题，CNN / Transformer / 3D / 分割 / 预后怎么选？”
- “Transfer learning、self-supervised 和 from scratch 哪个适合我的队列？”
- “帮我审查 DL Methods 是否有 slice-level leakage 或 patient overlap。”

## 参考文件

| File | 用途 |
|---|---|
| `references/architecture-choice.md` | 维度、模型家族、任务 head、容量与样本量匹配 |
| `references/training-protocol.md` | 预训练、划分、augmentation、imbalance、调参、seed |
| `references/multimodal-inputs.md` | 多模态输入、fusion、missing-modality 规则 |
| `references/dl-leakage-audit.md` | 深度学习 leakage 与有效性审计清单 |
| `references/interpretability-uncertainty.md` | 可解释性（Grad-CAM/SHAP/attention）有边界报告、不确定性量化（MC dropout/ensemble/conformal）、robustness/OOD、FUTURE-AI |
| `references/foundation-models-trustworthy-ai.md` | Foundation models、ViT、SSL、VLM/报告生成、adapter/LoRA、部署级可信 AI |
| `references/experiment-and-model-card.md` | 实验溯源冻结、model/data card、run manifest、阴性结果、test-set 访问记录、可复现包 |

## 下游衔接

`radiology-radiomics`（特征对照）· `radiology-reporting`（CLAIM / TRIPOD+AI）· `radiology-stats`（指标、CI、校准、MRMC、样本量）· `radiology-design`（验证类型）· `radiology-radiogenomics`（深度特征生物学）· `radiology-translation`（读者研究/前瞻验证）· `radiology-figure`（架构图、ROC、Grad-CAM）。
