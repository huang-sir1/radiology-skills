# radiology-ethics

面向医学影像和影像多组学研究的伦理、知情同意、隐私和数据共享治理 skill。它帮助作者把 retrospective / prospective / multi-center / registered study 的伦理表述写清楚，并让 Ethics、Consent、Data Availability 和数据共享承诺彼此一致。

## 它能做什么

- 起草 **approval & consent** 表述：伦理委员会名称、批准号、日期、知情同意取得或豁免、分中心审批。
- 评估 **re-identification risk**：DICOM metadata、burned-in pixel PHI、face reconstruction、日期/年龄、小病种队列、基因组数据。
- 规划 **governance & sharing**：HIPAA / GDPR / PIPL、DUA、controlled access、受限共享和不可共享理由。
- 输出 submission-ready statements，并列出必须由作者或 IRB 确认的事实。

## 典型触发

- “帮我写伦理审批、知情同意豁免和隐私表述。”
- “回顾性多中心研究 consent waiver 应该怎么写？”
- “影像 + 基因组数据共享时有什么再识别风险？”

## 参考文件

| File | 用途 |
|---|---|
| `references/approval-consent.md` | 研究类型到 consent model，approval statement 模板 |
| `references/reidentification-risk.md` | 风险来源、缓解措施、基因组数据说明 |
| `references/governance-sharing.md` | HIPAA / GDPR / PIPL、DUA、access tiers、一致性检查 |

## 下游衔接

`radiology-data`（去标识化、仓库、availability statements）· `radiology-radiogenomics`（受控组学队列）· `radiology-reporting`（open-science checklist items）· `radiology-grant`（伦理与可行性写法）。

## 边界

该 skill 提供科研文本和风险提示，不提供法律意见。伦理批准、同意状态、DUA 和机构要求必须由作者团队与 IRB / 机构确认。
