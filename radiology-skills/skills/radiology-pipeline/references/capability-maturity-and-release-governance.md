# Capability maturity and release governance

本契约规定 40 个运行时 Skill 的能力状态如何登记、降级和升级。它描述的是**产品工程成熟度**，
不是研究结论的科学有效性、临床效用、合规批准或期刊接收概率。机器可读事实源是
[`capability-maturity-registry.json`](capability-maturity-registry.json)；根 README 的状态仅由该目录派生，
不得凭主观印象写成“稳定版”。

## 1. 两个命名空间

- `skills/<skill-id>/SKILL.md` 是可发现、可调用的运行时能力。这里的 `framework_state` 不得为
  `PLANNED`。
- `roadmap/skills/<capability-id>/` 是未来能力的唯一规划命名空间。规划项不得伪装成可发现的
  Skill，也不得仅为占位而创建空 `SKILL.md`。当前没有规划目录时，registry 的
  `planned_capabilities` 必须为空。
- 从 roadmap 进入 runtime 是一次受控迁移：先完成入口、边界、内容和证据，再移动到 `skills/`，
  更新 registry、README，并运行目录校验。移动目录本身不构成成熟度升级。

## 2. 独立状态轴

| 字段 | 枚举 | 含义 |
|---|---|---|
| `maturity_label` | `CONTRACTED` / `EXPERIMENTAL` / `VALIDATED` | README 展示标签；由下列独立轴推导 |
| `framework_state` | `PLANNED` / `CONTRACTED` | 是否仍在 roadmap，或已成为有正式入口的运行时契约 |
| `boundary_state` | `NOT_DEFINED` / `CONTRACT_DEFINED` / `BOUNDARY_VERIFIED` | owner、输入输出、停止条件与交接是否定义；`VERIFIED` 还要求专门边界证据 |
| `content_state` | `SKELETON` / `PARTIAL` / `IMPLEMENTED` | 内容覆盖程度；不表示内容正确或来源仍新鲜 |
| `executable_test_state` | `NOT_PRESENT` / `STATIC_CONTRACT_ONLY` / `EXECUTABLE_PASS_CURRENT_TREE` | 无专属门、仅静态字符串/文件/路由检查，或专属可执行门已在当前树运行通过 |
| `behavior_state` | `NOT_RUN` / `NOT_ADJUDICATED` / `QUALIFIED_HUMAN_PASS` | 前向行为是否有运行记录及合格人工裁决 |
| `source_state` | `NOT_ASSESSED` / `STATIC_SNAPSHOT` / `LIVE_REFRESH_REQUIRED` / `CURRENT_VERIFIED` / `NOT_APPLICABLE` | 来源没有评估、只有冻结快照、需要实时刷新、已按来源契约核验，或能力确实不依赖外部可变来源 |
| `release_artifact_state` | `NOT_RECORDED` / `HASH_MANIFEST_VERIFIED` | 是否有可复核的发布制品身份、逐文件哈希和重放命令 |
| `release_eligible` | Boolean | 是否满足发布候选的全部门；不是“看起来可用”的同义词 |

每个 evidence 路径都必须是仓库内存在的相对文件。静态门、专属可执行门源码与持久化运行
receipt 分别登记在 `evidence.static_checks`、`evidence.executable_tests` 和
`evidence.executable_receipts`；不得把前者搬到后两者来抬高状态。

## 3. 标签推导规则

### `CONTRACTED`

运行时入口、边界和主体内容已经形成契约，但没有专属可执行能力门，或现有门只检查关键词、
链接、目录、模板存在、路由 case、JSON 字段/枚举等静态合同。即使这些检查全部 `PASS`，也只能
证明合同没有明显漂移，不能证明模型在未见请求中的行为，也不能升级到 `EXPERIMENTAL` 或
`VALIDATED`。

### `EXPERIMENTAL`

除正式入口、边界和内容外，至少有一个专属可执行门在当前工作树中运行真实解析器、审计器、
计算函数或版本绑定工件，并覆盖成功和失败路径。它仍可能缺少来源时效核验、前向行为人工裁决或
发布制品身份。因此 `EXPERIMENTAL` 的 `release_eligible` 必须为 `false`。

### `VALIDATED`

只有同时满足以下全部条件，才允许登记为 `VALIDATED`：

1. `framework_state=CONTRACTED`、`boundary_state=BOUNDARY_VERIFIED`、
   `content_state=IMPLEMENTED`；
2. `executable_test_state=EXECUTABLE_PASS_CURRENT_TREE`，且存在专属可执行门证据；
3. `behavior_state=QUALIFIED_HUMAN_PASS`，且有可追溯的行为用例、模型/运行身份、裁决者资格、
   裁决记录和失败处理；
4. `source_state` 为 `CURRENT_VERIFIED` 或有充分理由的 `NOT_APPLICABLE`，并有对应证据；
5. `release_artifact_state=HASH_MANIFEST_VERIFIED`，且记录发布制品身份、逐文件哈希、工具链和
   可复核命令；
6. `release_eligible=true`。

此外，`VALIDATED` 条目必须提供结构化 `validation_receipt`。其中五个路径字段
`dedicated_gate_receipt`、`source_verification_receipt`、`behavior_adjudication_receipt`、
`adjudicator_qualification_evidence`、`release_artifact_manifest` 必须指向仓库内可复核文件；
`behavior_run_identity`、`release_artifact_id`、64 位 `release_artifact_sha256` 和
`toolchain_identity` 必须非空。相应路径还必须登记在所属 evidence 轴中，不能用一份泛化 README
冒充专属 receipt；尤其 `dedicated_gate_receipt` 不能只是测试源码，必须登记在
`evidence.executable_receipts`。registry 顶层 `validated_receipt_contract` 固化了这些机器必需字段。

任一条件缺失必须降级。`VALIDATED` 不是永久荣誉：关键来源到期、行为回归失败、工件身份变化、
边界变更或证据不可达时，先把 `release_eligible` 设为 `false`，再降到能被现有证据支持的状态。

## 4. 当前基线与行为裁决

当前 behavior-evals 只有试点用例/运行合同，统一状态为 `NOT_ADJUDICATED`。因此当前 registry
不得包含任何 `VALIDATED` 或 `release_eligible=true` 项。机器 `PASS`、字符串命中、路由 case
命中、作者自评或模型自评，都不能替代合格人工行为裁决。

人工裁决至少应记录：用例版本、输入与期望边界、模型和运行参数、原始输出、关键失败、两名或
更多具备相应方法学/临床资格的裁决者（或预先说明的等效机制）、分歧解决、裁决日期和绑定的
提交/制品身份。只给一个总分或“效果不错”不能升级状态。

## 5. 来源与新鲜度

- `STATIC_SNAPSHOT` 只表示来源和核验日期已冻结，不能宣传为“当前最新”。
- 涉及期刊 call、法规、指南版本、价格、会议字段或其他易变事实的运行，在使用时仍必须执行
  owner Skill 的 live refresh；快照过期时登记为 `LIVE_REFRESH_REQUIRED`。
- `CURRENT_VERIFIED` 必须绑定来源、核验日期、适用范围和失效/复核条件。
- `NOT_APPLICABLE` 需要证据说明该能力为何不依赖外部可变来源，不能作为绕过来源工作的默认值。

## 6. 维护与发布流程

1. 修改能力时先更新 owner Skill 的局部契约与专属证据，避免把 registry 变成替代局部边界的
   “万能路由器”。
2. 更新 JSON registry；README 状态和 canonical `SKILL.md` 链接随后同步。
3. 运行 `scripts/validate_capability_maturity_catalog.py` 和
   `scripts/capability_maturity_catalog_test.py`。这两个检查验证治理合同，不是某个科研能力的行为证据。
4. 若申请 `VALIDATED`，另运行全部专属门、来源复核、人工行为评测与发布制品哈希验证；保存可复核
   receipt 后才能设 `release_eligible=true`。
5. 任何回滚都同时回滚 registry、README 展示和绑定证据；禁止只改宣传状态。

目录校验器故意不修改版本号、发布 manifest 或 release test inventory。是否发布仍由独立发布流程
决定，registry 只提供可审计的资格信号。
