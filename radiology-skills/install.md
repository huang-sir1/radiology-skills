# 安装与配置

`radiology-skills` 是一组位于 `skills/` 目录下的独立 skill 文件夹。你可以安装整个插件，也可以只复制某一个子 skill。

本产品不要求安装 Academic Research Skills、ARS-Codex、Nature Skills 或其他外部写作
Skill。它们是开发时的并列设计参考，不是运行依赖；完整安装本仓库的 `radiology-*`
目录即可执行本项目声明的全链路能力。

## A. Claude Code / Cowork 本地插件（本工作区）

```text
# 1. 将当前真实本地目录加入 marketplace（只需一次）
/plugin marketplace add C:\radiology-Skill

# 2. 安装插件
/plugin install radiology-skills

# 3. 重新加载插件
/reload-plugins
```

重新加载后，每个 `radiology-*` skill 都可以通过自然语言触发。下面是常见科研场景示例：

```text
# ⓪ 全项目总控
以 radiology-pipeline 为总控，从这批 radiomics + clinic 数据完成生存分析、全部图表与表格、论文和投稿材料；缺失材料仅用于教学模拟并全程标记。

# ① 立题与设计
这批多中心肝癌 MRI 能不能做研究？帮我判断可行性并设计课题（含外部验证方案）。
找近三年影像 AI 前沿方向和创新点，并说明文献/证据依据。

# ② 数据、标注与伦理
帮我写 ROI/mask 标注 SOP 与一致性评价（ICC/Dice）和 Methods 段落。
帮我写回顾性多中心研究的伦理审批、知情同意豁免和数据共享表述。

# ③ 建模与分析
帮我设计 PyRadiomics 流程，使其符合 IBSI/CLEAR，并审计是否存在数据泄漏。
帮我设计符合 CLAIM 2024 的影像深度学习研究，并检查 patient-level leakage。
比较同一批病例上两个 ROC 曲线（AUC 0.86 vs 0.81），按 Radiology 风格报告。

# ④ 写作、图表与报告规范
按 CLAIM 2024 审计这篇 manuscript，告诉我投稿前缺什么。
根据这些结果写 Radiology structured abstract + Summary statement + Key Results。
把 Table 1、Cox 回归表、模型性能表、特征筛选/权重表做成投稿级可编辑表格并核对数值。

# ⑤ 投稿、回复、转化与基金
投稿前帮我模拟审稿做一次严格预审；再帮我做投稿梯队（冲刺/主投/备选）。
按目标期刊最新指南整理完整投稿包并给出上传清单。
帮我设计 MRMC reader study 和前瞻性验证方案。
根据当年官方 call 审阅这份国自然影像标书：先查资格/格式，再按科学价值、创新性、影响和可行性给出可闭环修订项。
把已冻结的标书或本团队结果做成 10 分钟答辩/会议 PPTX，按受众重构叙事，保留证据源、影像上下文和演讲者备注，并逐页渲染 QA。

# ⑥ 治理、运行与复现
中立审计署名/CRediT、COI、生成式 AI 披露和影像/数据完整性；不要自行裁定 misconduct。
为多中心研究建立 RACI、站点依赖、资源、冻结、偏差和风险升级台账；再由独立团队按冻结环境和容差重放主结果。

# ⑦ 共识、定性与经济评价
设计一项影像实践 Delphi 指南，保留 COI、证据到推荐、匿名投票、异议和更新规则。
设计访谈/think-aloud 与 joint display；另为指定决策者建立 CEA/CUA、预算影响、PSA 和 VOI 方案。

# ⑧ 传播、影响与创新转化
把冻结证据转成患者通俗摘要、政策简报和媒体衍生物；另做作者机构消歧、领域归一化的影响快照。
在公开披露前整理发明状态、现有技术检索交接、贡献者/发明人和软件/数据权利边界，再交机构 TTO/法律人员裁决。
```

本项目当前没有在本文档中登记并验证过的远程仓库 URL，因此不要把示例占位符当成可执行
`git clone` 地址。远程发布前以 `RELEASE.md` 的远端与归档审计为准；现在使用上面的本地路径。

## B. Codex / Windows PowerShell 本地安装

当前可用的源目录是 `C:\radiology-Skill`。以下命令可直接粘贴到 Windows PowerShell；它把
每个完整 skill 文件夹复制到当前用户的 Codex skills 目录：

```powershell
$RadiologySkillsSource = 'C:\radiology-Skill'
$CodexSkillsTarget = Join-Path $env:USERPROFILE '.codex\skills'
New-Item -ItemType Directory -Force -Path $CodexSkillsTarget | Out-Null
Get-ChildItem -LiteralPath (Join-Path $RadiologySkillsSource 'skills') -Directory -Filter 'radiology-*' |
    ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $CodexSkillsTarget -Recurse -Force
    }
```

复制完成后重启 Codex，并新建任务以加载更新后的 skill。仓库根目录现在包含
`.codex-plugin\plugin.json`，用于 Codex 插件包结构和发布校验；本地 manifest 本身不等于已在
远程 marketplace 发布。

本地源目录更新后，用同一段 PowerShell 命令重新复制。本文档不提供未经验证的 `git pull`
或远程 URL。

## C. 只安装单个 skill（Windows PowerShell）

下面以 `radiology-reporting` 为真实示例，并保留该目录中的 `SKILL.md`、`agents/` 及已有的
`references/`、`scripts/`、`assets/`：

```powershell
$RadiologySkillsSource = 'C:\radiology-Skill'
$SingleSkillSource = Join-Path $RadiologySkillsSource 'skills\radiology-reporting'
$ClaudeSkillsTarget = Join-Path $env:USERPROFILE '.claude\skills'
New-Item -ItemType Directory -Force -Path $ClaudeSkillsTarget | Out-Null
Copy-Item -LiteralPath $SingleSkillSource -Destination $ClaudeSkillsTarget -Recurse -Force
```

如果要做 Claude Code subagent wrapper，可以把该 `SKILL.md` 复制到
`$env:USERPROFILE\.claude\agents\radiology-reporting.md`，并确认 frontmatter 中有有效的
`name:` 和 `description:`。

## D. 文献检索 MCP（`radiology-search`，可选）

`radiology-search` 支持两种模式：

1. **Prompt mode（无需额外配置）**：像其他 skill 一样复制整个 `skills/radiology-search/` 文件夹。Agent 使用内置搜索工具，并遵循 `references/` 中的 source-tier、dedup 和 verification 规则。
2. **MCP-server mode（更适合高质量批量检索）**：如果你已经有 academic-search MCP server，可接入支持 `search_papers` / `get_paper_by_id` / `get_citation` / `lookup_mesh` 的服务。PubMed E-utilities 建议配置 contact email；如需更高限速，可配置 `NCBI_API_KEY`，然后重启 agent。

   配置示例（Codex，其他 client 用其各自的 MCP 注册格式）——编辑 `~/.codex/config.toml`：

   ```toml
   [mcp_servers.academic-search]
   command = "<你的-academic-search-server-启动命令>"
   env = { CONTACT_EMAIL = "you@example.com", NCBI_API_KEY = "<可选>" }
   ```

   保存后重启 agent，用 `search_papers` 能否返回来确认接通。

> 本仓库提供的是“检索策略与验证规则层”：来源分级、去重、DOI/PMID/accession 验证、TCIA/GEO/cBioPortal 等数据源检索路线。它不捆绑具体 server binary。

## E. 图表与统计所需 Python 环境

`radiology-figure`、`radiology-table` 和 `radiology-stats` 会使用常见科学计算包生成图表、表格或运行统计分析。典型环境如下：

```bash
pip install numpy scipy pandas scikit-learn matplotlib statsmodels lifelines pillow openpyxl python-docx pypdf pyyaml
# radiomics / harmonisation（按需）
pip install pyradiomics SimpleITK neuroCombat
```

说明：上表是给 agent 即兴分析代码用的宽环境；技能自带脚本实际只依赖其中子集
（`pillow`、`pypdf`、`pyyaml`），缺其他包不影响技能校验脚本运行。

如果你的团队偏好 R，`radiology-stats` 和 `radiology-figure` 会在合适位置提示社区常用 R 包，例如 `pROC`、`irr`、`rms`、`survminer`、`dcurves`、`ggplot2`、`ComplexHeatmap`，以及 MRMC 分析常用的 `RJafroc`。

## F. 验证安装

```powershell
$RadiologySkillsSource = 'C:\radiology-Skill'
$ReleasePython = 'C:\Users\<你的用户名>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'

# 一键发布门：manifest、40 个 skill quick_validate、openai.yaml、链接、静态校验与回归测试
pwsh -NoProfile -File (Join-Path $RadiologySkillsSource 'scripts\validate_release_boundary.ps1') `
    -ProductRoot $RadiologySkillsSource `
    -PythonExecutable $ReleasePython
```

上面的 Codex bundled Python 是本工作站已实际验证的解释器（Python 3.12.13、PyYAML
6.0.3、pypdf 6.10.0）。换到另一台机器时，应传入那台机器上真实存在的 Python 3.10+
路径，并确保可导入 `yaml` 与 `pypdf`；发布校验器会对路径、版本或依赖缺失 fail closed。

公开发布或制作安装归档时不要递归打包当前工作目录；按 `release-allowlist.txt` 建立干净
发行副本，并按 `RELEASE.md` 检查文件清单、Git 远端和再分发权限。

如果触发不稳定，优先检查：

- skill 文件夹是否完整复制，而不是只复制了 `SKILL.md`；
- `references/` 是否仍在原路径下；
- agent 是否已经 reload / restart；
- `SKILL.md` frontmatter 是否保留 `name:` 与 `description:`。
- `agents/openai.yaml` 是否随完整 skill 文件夹一起复制（Codex 界面与默认触发提示使用）。
