# radiology-federated-learning

**联邦协作工程师**：用于在多中心影像数据不能汇总的情况下，设计可复现、可审计、可投稿的联邦学习研究。

## 它能做什么

- 判断各中心是否具备联邦训练的伦理、治理、合规、计算和网络条件。
- 区分 horizontal FL、vertical FL、split learning、SplitFed、personalized FL 等设计。
- 设计 local-only、centralized oracle/simulation、FedAvg、个性化或异质性自适应方法的基线阶梯。
- 处理 non-IID 中心、扫描仪差异、标注差异、患病率差异、中心权重和掉线问题。
- 规划 secure aggregation、differential privacy、membership inference、gradient inversion、poisoning 等威胁模型。
- 设计 leave-one-site-out、外部中心验证、分中心校准、公平性和可复现审计记录。

## 典型触发

- “多中心医院不能共享原始影像，想做联邦学习。”
- “FedAvg 和 personalized FL 怎么选？”
- “联邦学习能不能算外部验证？”
- “帮我写联邦影像 AI 研究的治理、隐私和评估方案。”

## 边界

联邦学习不是隐私证明，也不是外部验证。参与训练的中心仍属于开发体系；真正的泛化需要冻结模型后在未参与训练的中心或时间队列中验证。
