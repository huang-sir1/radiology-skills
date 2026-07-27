# radiology-foundation-models

**基础模型调优师**：用于选择、适配、微调和审查医学影像基础模型、视觉-语言模型、promptable segmentation 模型和大规模预训练影像模型。

## 它能做什么

- 审查 model card、checkpoint、license、预训练数据来源和潜在测试集重叠。
- 判断候选基础模型是否适合当前模态、解剖部位、2D/3D 输入、任务和预测时可用信息。
- 设计 zero-shot、linear probe、partial tuning、full fine-tuning、adapter、LoRA、prompt learning、domain adaptation 等适配阶梯。
- 规划冻结测试集、患者级划分、站点/时间外部验证、强基线和公平调参预算。
- 报告计算资源、可复现性、checkpoint hash、推理成本、校准、不确定性、亚组和外部验证。
- 限制“泛化”“临床可用”“公平”“安全”等过度结论。

## 典型触发

- “我想用医学影像基础模型做 MRI 分类，应该 zero-shot 还是 LoRA 微调？”
- “SAM/MedSAM 这类 promptable segmentation 怎么写方法和验证？”
- “基础模型预训练数据可能包含测试集，怎么审查？”
- “帮我设计 foundation model fine-tuning 的基线、外部验证和报告规范。”

## 边界

普通迁移学习不等于基础模型研究。没有足够规模、多样性、算力、治理和外部验证时，不应建议从头训练 foundation model，也不能把未知预训练重叠的测试集写成完全独立验证。
