# radiology-research-agent

**科研智能体架构师**：用于设计和审查面向医学影像科研流程的 LLM Agent / 多智能体系统，例如文献检索、数据集发现、方案规划、证据 RAG、分析编排、报告规范审计、论文写作和可复现工件管理。

## 它能做什么

- 设计单智能体或多智能体架构，明确 planner、retriever、analyst、verifier、writer、supervisor 等角色。
- 建立证据来源、claim-to-source 映射、文献核验、数据集记录、代码和图表工件清单。
- 规划工具 allowlist、typed input/output、状态机、checkpoint、idempotency、恢复和审计日志。
- 防范 hallucination、prompt injection、data exfiltration、secret leakage、unauthorized write 等风险。
- 设计人工审批门槛，尤其是投稿、邮件、共享、上传、删除和权限变更等外部写操作。
- 评估 citation accuracy、numerical consistency、reproducibility、human correction rate、cost、latency 和 time saved。

## 典型触发

- “我想做一个自动帮我找文献、写方案、查规范的影像科研智能体。”
- “怎么让 Agent 自动整理文献但不胡编引用？”
- “多智能体能不能帮我完成影像组学论文的预审和返修？”
- “帮我设计科研 Agent 的权限、审批、审计和安全边界。”

## 边界

这个模块只用于科研流程自动化。它不允许自主临床诊断、治疗建议、患者级临床决策，也不允许未经明确授权执行投稿、发信、共享、上传、删除或任何外部写操作。
