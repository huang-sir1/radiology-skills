# Action authorization and execution trace contract

本契约用于记录一次动作**被谁、在什么范围、何时授权，以及实际调用了什么、改变了什么**。
它是宿主无关的审计合同，不扩大用户意图，也不授予任何新权限。模板见
[`../assets/action_authorization_trace.template.json`](../assets/action_authorization_trace.template.json)，
机器校验器见 `../scripts/validate_action_authorization_trace.py`。

> 关键边界：一份格式正确的 JSON、一次校验器 `PASS` 或一段批准文字，都不等于宿主在运行时
> 拦截了未授权工具调用。宿主没有可验证的调用前授权门时，最高只能声明
> `AUDITABLE_CONTRACT`；只有宿主实际阻止越权调用并签发 enforcement receipt，才能声明
> `HOST_ENFORCED`。本仓库校验器只能检查 receipt 的结构和绑定，不能替宿主证明拦截确实发生。

## 1. 选择最高适用动作类别

| `action_class` | 适用动作 | 不能从什么授权推导 |
|---|---|---|
| `READ_ONLY` | 普通资源的读取、列举、检查、哈希或无副作用验证 | 不得掩盖写入；受管临床/监管系统访问仍走 `CLINICAL_REGULATORY` |
| `WORKSPACE_WRITE` | 明确工作区内文件/目录的创建、修改、移动或删除 | 不授权 API、消息、发布、上传或临床/监管状态变化 |
| `EXTERNAL_STATE_CHANGE` | 外部账户、服务或 API 的创建、更新、删除、发送或发布 | 不授权投稿上传，也不授权临床/监管动作 |
| `SUBMISSION_UPLOAD` | 稿件/标书/会议 portal 的上传、替换或撤回 | 准备本地投稿包不等于获准上传；“完成投稿材料”不等于“替我提交” |
| `CLINICAL_REGULATORY` | 受管临床记录/系统访问、患者照护状态变化、监管 portal 提交或更新 | 普通用户批准和项目写权限不能替代机构指定的临床/监管权限 |

同一计划若跨类别，应拆成多个 action record；不能用一个低风险类别包住多个高风险调用。一个动作
同时匹配多类时使用最高风险的专门类别，例如“生成并上传稿件”拆为本地
`WORKSPACE_WRITE` 与独立 `SUBMISSION_UPLOAD`。

允许的 operation 是闭集：

- `READ_ONLY`: `READ`, `LIST`, `INSPECT`, `HASH`, `VALIDATE`
- `WORKSPACE_WRITE`: `CREATE`, `MODIFY`, `MOVE`, `DELETE`
- `EXTERNAL_STATE_CHANGE`: `CREATE_EXTERNAL`, `UPDATE_EXTERNAL`, `DELETE_EXTERNAL`,
  `SEND_MESSAGE`, `PUBLISH`
- `SUBMISSION_UPLOAD`: `UPLOAD`, `REPLACE_UPLOAD`, `WITHDRAW_SUBMISSION`
- `CLINICAL_REGULATORY`: `ACCESS_CLINICAL`, `CHANGE_CLINICAL_STATE`,
  `SUBMIT_REGULATORY`, `UPDATE_REGULATORY`

## 2. 精确 scope，而不是自然语言兜底

`target_scope.targets` 是授权闭集。每项必须有精确 `target_id`、`target_kind` 和明确
`allowed_operations`；不接受 `*`、模板变量或“本项目所有文件”一类开放表达。执行 event 的
`target_id + operation` 必须逐项落在闭集中。`scope_sha256` 是去掉自身后对整个
`target_scope` 做 canonical JSON 的 SHA-256，授权的 `bound_scope_sha256` 必须与之相同。

目标种类也防止降级：工作区写入只能指向 `WORKSPACE_FILE`/`WORKSPACE_DIRECTORY`，外部状态
变化只能指向 `EXTERNAL_RESOURCE`/`EXTERNAL_ACCOUNT`，投稿动作只能指向
`SUBMISSION_PORTAL`/`SUBMISSION_PACKAGE`，临床/监管动作只能指向
`CLINICAL_SYSTEM`/`REGULATORY_PORTAL`/`PATIENT_CARE_STATE`。`READ_ONLY` 不得用于后三类受管目标。

## 3. 授权对象

授权从当前会话的实际请求及仍有效的先前授权判断。用户明确要求“创建这个项目档案”或
“更新这些文件”，已授权完成该结果所需的正常工作区写入；代理可在执行前把范围落实为精确
targets 并记录用户原始指令，无须让用户为同一范围再批准一次。不得把代理整理出的 scope
伪装成用户亲自签过的哈希或宿主 enforcement receipt。用户授权创建档案，也不表示缺失的
终点、拆分或统计计划已经科学上确定；先建立可用记录，仅保持未具备依据的 analysis lock 开放。
仅有“为项目好”“教我怎么做”或紧迫性仍不构成写入授权。新增外部、投稿或临床动作按其实际
类别重新判断范围，不从文件写入推导。

每个 record 都有 `requester.actor_id`；在代理执行场景中 requester 是请求执行的代理/运行时，
而提供许可的人是 approver。对所有可变更动作，二者相同即为自批并失败。

`authorization` 必须绑定 `action_class` 与 `scope_sha256`，并记录：

- `state`: `NOT_REQUIRED`, `REQUESTED`, `APPROVED`, `DENIED`, `REVOKED`, `EXPIRED`
- `approver.actor_id` 与 `approver.role`
- `evidence.evidence_id`, `evidence_type`, `locator`, `sha256`
- `approved_at`, `expires_at`, `revoked_at`

可变更动作只有 `APPROVED` 才能产生 execution event，且 `approved_at <= executed_at < expires_at`；
批准前、到期后或撤销后的调用都失败。授权 evidence 必须有不可变哈希，不能只写“用户同意了”。
批准不能跨 target、operation 或 action class 复用。

最低 approver role：

| 类别 | 允许角色 | 补充要求 |
|---|---|---|
| `READ_ONLY` | `POLICY`（`NOT_REQUIRED`）或适用 owner | 无副作用；若本地/机构规则要求批准则用 `APPROVED` |
| `WORKSPACE_WRITE` | `USER`, `WORKSPACE_OWNER` | evidence 不能为 `NOT_APPLICABLE` |
| `EXTERNAL_STATE_CHANGE` | `USER`, `RESOURCE_OWNER` | 精确资源和 operation；不能从一般任务授权推导 |
| `SUBMISSION_UPLOAD` | `SUBMISSION_OWNER` | 必须由负责提交的人显式批准；portal 人工确认仍保留 |
| `CLINICAL_REGULATORY` | `CLINICAL_REGULATORY_AUTHORITY` | evidence 必须是 `INSTITUTIONAL_RECORD`；不替代本地 credential/RBAC |

## 4. 执行与结果证据

`execution` 记录整体 `state`、起止时间、`tool_call_ids`、events 和
`aggregate_result_sha256`。每个 event 必须有连续 sequence、唯一 `tool_call_id`、
`tool_call_id_kind`、执行 actor/time、精确 target/operation、event state、结果 locator，以及：

- `before_sha256`: 调用前工件字节或 canonical state snapshot；创建动作对固定 `ABSENT` marker
  哈希，不能留空。
- `after_sha256`: 调用后工件或状态快照；失败时也应哈希实际残留状态。
- `result_sha256`: 原始工具结果或不可变结果 receipt 的哈希。

三类哈希均为 64 位十六进制。任何已尝试的 event 缺 before、after 或 result hash 都是无效
trace，不得写成 `SUCCEEDED`。`READ_ONLY` event 的 before/after 必须相同。顶层 tool-call ID
列表必须与 event 顺序完全一致；aggregate hash 是 canonical events 数组的 SHA-256。

宿主提供真实调用 ID 时使用 `tool_call_id_kind=HOST`；宿主不暴露 ID 时允许
`LOCAL_CORRELATION`，但它只是本地关联键，不能作为 `HOST_ENFORCED` 的证据。对最终 record，
`trace_digest` 是去掉自身后整个 JSON 的 canonical SHA-256，任何授权、scope 或事件变化都必须
重新签名。

## 5. 执行状态

- `NOT_STARTED`: 没有 event、tool-call ID、起止时间或 aggregate hash。
- `BLOCKED`: 在调用前因缺授权/宿主能力/范围问题停止；同样不得伪造执行 event。
- `SUCCEEDED`, `FAILED`, `CANCELLED`: 至少一个真实 event，且整体状态与 event 状态一致。

`DENIED`、`REQUESTED` 或未满足条件的批准可以形成合法的 `BLOCKED` 审计记录，但不能伴随工具
调用。校验器拒绝无效调用记录，不会自动执行、补批或扩大 scope。

## 6. 宿主 enforcement 声明

`host_enforcement.declared_level` 只有 `AUDITABLE_CONTRACT` 与 `HOST_ENFORCED`：

- `runtime_authorization_enforcement=false` 时必须为 `AUDITABLE_CONTRACT`，enforcement receipt
  字段必须为空。
- `HOST_ENFORCED` 要求宿主明确声明支持调用前拦截，提供 host ID、receipt ID 和 receipt
  SHA-256，并且所有 event 使用真实 `HOST` tool-call ID。
- 校验器通过仅表示 trace 内部一致。它不探测宿主实现，也不把本地 correlation ID、用户消息、
  Skill 文字或 JSON 模板升级为 runtime enforcement。

## 7. 使用方法

1. 在任何可能产生副作用的工具调用前复制 JSON template，选择最高 action class，填写 requester
   和精确 target scope，计算 `scope_sha256`。
2. 获得与 class/scope/expiry 绑定的授权；没有授权时保持 `BLOCKED`，不要调用工具。
3. 每个调用后立即记录 tool-call ID、before/after/result hashes 和 result locator；缺证据即停止。
4. 计算 aggregate 与 trace digests，然后运行：

```text
python scripts/validate_action_authorization_trace.py path/to/trace.json
```

5. 保存 trace 只是审计步骤。实际能否调用仍由当前宿主、账户权限、机构规则和用户授权决定。

模板是结构示例，不是预批准令牌；复制后必须替换全部身份、target、时间、evidence 和 hash，并重新
计算三个 digest。不要把模板内的示例批准或 hash 用于真实动作。

## Design provenance

The [OpenAI Agents SDK guardrails](https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md),
[human-in-the-loop](https://github.com/openai/openai-agents-python/blob/main/docs/human_in_the_loop.md)
and [tracing](https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md) documentation
informed the separation between call approval, pause/resume evidence and execution traces. This
host-neutral schema is not an implementation of that SDK and inherits none of its runtime enforcement.
