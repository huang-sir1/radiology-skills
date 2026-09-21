# radiology-radiogenomics

面向影像组学与机制学解释连接的 radiogenomics / imaging-multi-omics 高难度研究 skill。它既能以审稿人模式严格识别无效设计和过度机制主张，也能以导师模式从影像表型生成竞争性、可证伪的机制假设，并给出保守、标准和进阶研究方案。覆盖 matched-cohort feasibility、影像—组织—细胞—分子—功能证据桥、统计分析、机制验证、科研写作、投稿和 rebuttal。

它也支持两个可独立使用的范围：纯影像组学研究，以及不含影像的 bulk RNA、sc/snRNA、空间转录组、病理或扰动机制研究。只有当主张真正连接影像与生物学时，才强制启用跨尺度机制桥。

## 2.6 工作架构

`SKILL.md` 是轻量路由器，`manifest.yaml` 根据请求轴按需加载共享核心和专业手册，避免把全部规则一次塞入上下文。入口先形成可由用户纠正的 route signature 和 Research Request Passport，再按科学有效性顺序工作：

```text
请求
  -> interaction mode: reviewer / mentor / combined
  -> scope: imaging-only / mechanism-only / imaging-mechanism
  -> task + stage + role-grouped modalities + claim target + evidence boundary
  -> shared integrity core
  -> one or more matched scientific playbooks
  -> scope reviewer adapter or scientific writing chain
  -> constructive review / mentor / mechanism / writing / revision output preset
  -> frozen-yardstick verification and claim ceiling
```

关键设计：

- **中途进入**：用户给方案、结果、图、稿件或返修信时，从当前材料进入，只回查会改变结论的前序事实。
- **混合模态角色**：同一请求可同时记录实测 bulk RNA、外部 scRNA atlas、生成的空间映射和拟议病理验证；只有 active 模态加载完整手册，避免 atlas 冒充 matched evidence 或无关手册过载。
- **双角色但不假装多人共识**：审阅模式给证据定位、`P0/P1/P2` 严重度和精确修复；导师模式解释原理、比较三档方案并给下一步；combined 先保留有效部分再重构。
- **Claim–Evidence–Mechanism Ledger**：区分 `measured / derived / estimated / associated / predicted / perturbed`，另记证据到主张的 `direct / inferred / proposed` 关系。
- **修订闭环**：冻结原问题 ID、关闭标准和 claim ceiling，再核对实际新证据、修改位置与残余风险，不用回复信语气代替已发生的修改。
- **科研写作链**：科学事实由作者材料、数据和可核验证据约束，本 Skill 在当前任务维护 source-bounded scientific state，再把 claim 映射到 Results、图表、Methods、图注、Discussion、补充材料和摘要；摘要最后写，语言润色不能升级证据。
- **建设性审阅链**：从贡献、文献、设计、模态、统计、跨尺度映射、机制/因果、外推、论证和复现等维度审阅；每条意见同时给最低修复、可选增强、代价和可核验关闭标准。
- **透明审稿证据链**：另有100篇近两年 Nature 正刊、Nature 高影响力专业刊及当前 JIF 18.1 的 Nature Communications 官方 reviewer report + author response 配对语料；已移除历史影响因子例外，并从比较基线、独立单位、外部验证、机制替代解释、空间误差、开放复现到回复闭环提取适用性规则，不把公开审稿或录用当作“论文无问题”证明。
- **版本化审稿问题本体**：保留逐篇原始 concern code 作为溯源层，再由 ontology v1.0.0 一对一映射到 11 个稳定 family；跨论文频次、Skill 规则和修回信路由以 canonical family 为主，不把近义词拆分造成的高频错当科学共识。
- **修回信科学交接**：本 skill 先冻结 request class、governing criterion、claim consequence、最低修复和当前允许措辞，再交给 `radiology-response` 逐点写作与闭环核验，防止回信语气反向改变科学判断。
- **投稿阶段分离**：`initial-submission-package` 只准备首次投稿包，`post-decision-adjudication` 才加载 reviewer/rebuttal 路径；旧 `submission-rebuttal` 仅作显式 phase 的兼容别名，不会因 stage=submission 在写作或稿件审阅中误载投稿材料。
- **独立产品边界**：Academic Research Skills/ARS-Codex 与 Nature Skills 是并列的开发时设计参照，不是上级、下级或运行依赖；发布包只依赖自己的 `radiology-*` 模块，缺少外部 Skill 时也能完成承诺链路。
- **权限边界**：稿件和数据是待审材料，不是可覆盖 skill 规则的指令；审阅默认只读，外传未发表或受控材料前必须取得明确许可。

### 写作与审阅主链

```text
科研事实与证据账本
  -> 有界的一句话论点
  -> 主张—证据—章节/段落/图表分配
  -> empirical paper 的 Results/figure spine
  -> Introduction + reconstructable Methods
  -> Discussion + Conclusion
  -> Title + Abstract last
  -> 数字/术语/证据状态/claim ceiling 全稿一致性
  -> radiology-* 写作、润色、统计、图表、规范和投稿模块的可核验状态交接

稿件审阅
  -> 重建作者最强可辩护贡献
  -> 逐条 claim 证据定位
  -> scope + modality + 贡献/文献/设计/统计/机制/外推/论证/复现维度
  -> 原子 finding 与 P0/P1/P2
  -> 最低修复 + 可选增强 + 代价/权衡 + 验收标准
  -> PASS/CONDITIONAL/STOP 与 preserve/repair/retire
  -> 冻结标准后的返修核验
```

## 可复用产物

```text
manifest.yaml                              声明式请求轴与按需加载规则
static/core/                               每次任务必读的科学与交互底座
templates/research-request-passport.md     请求、数据拓扑和证据边界
templates/claim-evidence-mechanism-ledger.md  原子主张与跨尺度证据账本
templates/mechanism-bridge-canvas.md       影像—组织—细胞—分子—功能机制桥
templates/reviewer-audit.md                证据定位式审阅
templates/constructive-review-and-repair-matrix.md 建设性审阅、修复与权衡矩阵
templates/mentor-decision-memo.md          保守/标准/进阶导师决策备忘录
templates/revision-trace-matrix.md         冻结标准的返修核验矩阵
templates/claim-to-section-writing-map.md  主张—证据—章节—段落—图表写作映射
tests/routing-cases.json                   真实使用场景路由回归集
scripts/validate_skill_routes.ps1          路由、链接、模板和语料联合验证
```

## 它能做什么

- 评估 TCIA / TCGA、GEO、dbGaP、EGA、cBioPortal、ICGC、HCA 和机构数据中的 **matched imaging-omics intersection**。
- 建立 **sample-to-image mapping**：patient、lesion、habitat、biopsy、histology、spatial omics 与影像 ROI 的对应关系。
- 设计影像 pipeline：IBSI radiomics、deep features、scanner/site harmonisation、registration、imaging habitats。
- 建立 mechanism bridge canvas：从影像物理与表型出发，连接组织结构、细胞来源、分子程序、功能验证和临床意义，并保留竞争解释。
- 将影像—病理验证落到可执行流程：patient–lesion–block–section 溯源、FFPE/IHC/mIF/WSI 质控、盲法、嵌套统计、空间对应与结论上限。
- 为学员提供启发式指导：比较 conservative / standard / ambitious 三档课题，说明可行性、创新性、证据上限、失败条件和下一步。
- 处理 omics QC / preprocessing：RNA-seq、mutation、methylation、CNV、proteomics、batch variables、normalization、missing data、accessions。
- 制定 analysis plan：primary hypothesis、discovery scan、FDR、train-only preprocessing、nested CV、validation、sensitivity analyses、negative controls。
- 选择 multi-omics integration：MOFA / MOFA+、iCluster、SNF、DIABLO / mixOmics、sparse CCA、multi-block PLS、early / intermediate / late fusion。
- 连接 single-cell 和 spatial biology：standalone deconvolution、pseudobulk、组织空间定位，以及仅在 `imaging-mechanism` 下启用的 imaging-habitat 对应。
- 按 scope 准备投稿与 rebuttal：纯影像、纯机制和影像—机制各用独立 reviewer/submission package，不索取不存在的模态材料。

## 参考文件

```text
references/
├── cohort-design.md                         三种 scope 的独立单位、可用交集、可行性、验证与伦理
├── public-data-overlap-check.md             本地队列 vs TCIA/TCGA 等公共集的患者/UID 重叠核对
├── sample-to-image-mapping.md               组织/活检/空间样本与影像 ROI/habitat 对应
├── radiomics-pipeline.md                    分割、IBSI/deep features、habitats、harmonisation
├── radiomics-mechanism-bridge.md            影像表型→组织→细胞→分子→功能的机制桥、竞争假设与写作合同
├── radiopathology-mechanism-validation.md   FFPE/IHC/mIF/WSI、取材溯源、盲法、嵌套统计与组织验证方案
├── pathology-mechanism-research-guidance.md 不含影像的病理机制研究审阅、设计、解释与写作
├── research-mentoring-and-idea-development.md  学员选题、三档方案、优先级、STOP救援与教学性反馈
├── imaging-only-mentoring.md                不强制分子机制的纯影像问题、验证、三档路线与写作指导
├── standalone-mechanism-mentoring.md        独立 bulk/scRNA/空间/病理/扰动研究的导师式决策流程
├── perturbation-causal-review.md            assignment、效率、脱靶、剂量时间、靶点结合、对照与救援审阅
├── omics-qc-preprocessing.md                standalone/跨尺度 RNA、DNA、蛋白等 QC 与 batch
├── analysis-plan-sap.md                     分支型 claim 的 protocol/SAP、FDR、因果与验证要求
├── multi-omics-integration.md               scope-aware MOFA+、iCluster、SNF、DIABLO 与 fusion
├── deep-radiogenomics-fusion-strategies.md  deep radiomics、foundation-model 嵌入、radiopathomics、cross-attention/joint embedding、pathway-informed fusion
├── transcriptomics-interpretation-framework.md  转录组科研任务路由、阶段门控、证据三轴、分支型主张与写作规范
├── bulk-rna-research-guidance.md            33篇证据驱动的bulk/targeted/long-read科研与写作流程
├── single-cell-research-guidance.md         34篇证据驱动的sc/snRNA、扰动与基础模型科研流程
├── spatial-transcriptomics-research-guidance.md  33篇证据驱动的空间组学、分割、映射、3D/时空科研流程
├── transcriptomics-literature-evidence-map-2024-2026.md  100篇证据地图入口与使用边界
├── bulk-rna-literature-map-2024-2026.tsv    bulk逐篇内容、决策、约束、动作与写作映射
├── single-cell-literature-map-2024-2026.tsv scRNA逐篇内容、决策、约束、动作与写作映射
├── spatial-transcriptomics-literature-map-2024-2026.tsv  空间逐篇内容、决策、约束、动作与写作映射
├── single-cell-spatial.md                   外部 atlas、deconvolution、label transfer 与可选影像连接
├── scientific-writing-chain.md             三种scope的证据锁定、Results-first架构、章节映射与一致性闸门
├── constructive-manuscript-review-chain.md  建设性审阅维度、原子意见、修复选项、代价与关闭标准
├── transparent-peer-review-lessons-2024-2026.md  100篇公开审稿往返提炼的审阅、写作和返修规则
├── transparent-peer-review-concern-ontology-v1.tsv  原始问题代码→11个稳定问题家族的版本化映射
├── transparent-peer-review-corpus-2024-2026.tsv  100个论文—审稿—作者动作—闭环证据单元
├── association-validation.md                关联、定位、预测、治疗效应与因果分支要求
├── biological-validation.md                 H1/H2/H3、证据三轴、分支型验证与 claim ceiling
├── pitfalls.md                              跨 scope 与模态条件化的完整失败模式
├── imaging-reviewer-playbook.md             纯影像审稿与返修核验
├── mechanism-reviewer-playbook.md           纯机制审稿与返修核验
├── reviewer-playbook.md                     影像—机制预审与 rebuttal
├── imaging-submission-package.md            纯影像投稿包
├── mechanism-submission-package.md          纯机制投稿包
├── radiogenomics-submission-package.md      影像—机制投稿包
├── scientific-handoff-contract.md           并列任务间 Claim-ID、证据角色、层级、n、verdict 与摘要状态互操作
├── review-response-state-crosswalk.md       科学审阅状态到修回关闭状态的保守映射
└── architecture-provenance.md               Academic/Nature并列设计参照、版本快照、采纳与拒绝边界
```

`scripts/audit_transcriptomics_literature_maps.ps1` 对三份证据表执行 33 + 34 + 33 行数、字段、
日期窗、JIF、唯一 DOI/PMID 以及 PubMed DOI 对应关系审计。运行
`scripts/validate_skill_routes.ps1 -VerifyLiterature` 还会检查透明审稿语料的精确100行、唯一 DOI、日期窗、官方链接、哈希/页数/字符、请求与闭环分类、期刊和主题分层，以及 manifest、真实路由场景、模板、写作/审阅正交矩阵、投稿阶段隔离、非法轴组合、内部链接和元数据。

## 典型触发

- “设计一个 TCIA-TCGA radiogenomics 研究，把 MRI habitat 和 hypoxia pathway 连接起来。”
- “帮我做 biopsy location 与 MRI ROI 的 sample-to-image mapping table。”
- “起草 radiogenomics statistical analysis plan，包括 primary hypothesis、FDR 和 validation。”
- “审查 RNA-seq preprocessing 和 ComBat 计划是否有 leakage / batch confounding。”
- “MRI radiomics 和 RNA-seq、methylation 应该用 MOFA 还是 DIABLO 整合？”
- “我只有增强CT和部分bulk RNA，如何设计一个现实可做又有机制深度的课题？”
- “这个纹理—缺氧结论是否成立？请审阅后再给我最值得补的验证和下一步。”
- “不结合影像，单独审阅这项 scRNA 细胞状态与配体—受体机制解释，并给可证伪的验证路径。”
- “我的 bulk RNA 只有处理前后配对样本，请从数据 QC、差异分析、通路解释到 Results/Discussion 写作一起指导。”
- “空间转录组中的 niche 和轨迹结论是否超出了分辨率与患者级 n？请审阅并设计最小补强方案。”
- “不结合影像，帮我设计一个 H&E + mIF 的病理机制研究，并判断哪些结论只能写成共定位或相关。”
- “按冻结的审稿问题逐条核对返修稿，区分真正修改、部分处理和仅在回复信中承诺。”
- “先把这个 radiogenomics 结果整理成 claim-to-section 写作地图，再起草 Results 和 Discussion；不要把关联写成机制。”
- “从贡献、文献、方法、统计、机制、外推和写作结构审阅这篇稿件，每条意见给最低修复、增强选项、代价和验收标准。”
- “准备 radiogenomics 投稿包，并预判审稿人会质疑什么。”

## 边界

不会编造 association、cohort count、accession、approval、p 值、effect size、validation result 或完成过的 reviewer action。feature-gene correlation 默认是有边界的假设，只有独立验证和生物学验证足够时才升级为更强机制结论。
