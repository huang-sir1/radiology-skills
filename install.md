# 安装 Radiology Skills

本仓库的当前技能包位于 `radiology-skills/`，清单版本 **1.10.1**，包含 **40 个独立技能**。目录结构如下：

```text
radiology-skills/                 # GitHub 仓库根目录
├── README.md
├── install.md
└── radiology-skills/             # 完整插件包
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/
    ├── scripts/
    └── skills/
        ├── radiology-pipeline/SKILL.md
        ├── radiology-design/SKILL.md
        └── ...                  # 共 40 个 radiology-* 目录
```

## 1. 下载当前主分支

安装了 Git 时，在希望保存仓库的位置运行：

```text
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
```

也可以从 [GitHub 仓库主页](https://github.com/huang-sir1/radiology-skills) 选择 **Code → Download ZIP**，解压后进入包含本文件和 `radiology-skills/` 子目录的仓库根目录。

以下命令均从仓库根目录执行。已有 clone 时，可先用 `git pull --ff-only` 获取更新；若 Git 提示本地修改冲突，请先处理本地修改。

## 2. Codex：复制完整技能目录

### Windows PowerShell

```powershell
$RadiologyPackageRoot = Join-Path (Get-Location) 'radiology-skills'
$RadiologySkillSource = Join-Path $RadiologyPackageRoot 'skills'
if (-not (Test-Path -LiteralPath (Join-Path $RadiologySkillSource 'radiology-pipeline\SKILL.md'))) {
    throw '请先进入下载或 clone 后的仓库根目录。'
}
$RadiologySkillsTarget = Join-Path $env:USERPROFILE '.codex\skills'
New-Item -ItemType Directory -Force -Path $RadiologySkillsTarget | Out-Null
Get-ChildItem -LiteralPath $RadiologySkillSource -Directory -Filter 'radiology-*' |
    ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $RadiologySkillsTarget -Recurse -Force
    }
```

### macOS / Linux

```bash
mkdir -p "$HOME/.codex/skills"
for skill_dir in radiology-skills/skills/radiology-*; do
  cp -R "$skill_dir" "$HOME/.codex/skills/"
done
```

每个技能必须保留完整文件夹。插件包根目录本身没有 `SKILL.md`，不要将外层 `radiology-skills/` 文件夹当作单个技能安装。

如果曾安装旧版单入口 `radiology-skills`，或启用了同名的另一套技能，请先备份并移出对应旧目录或停用重复入口，再加载新版，避免重复发现。复制命令会更新同名文件，但不会自动删除旧版本多出的文件。

## 3. 加载与使用

复制完成后重新启动 Codex，并新建任务加载技能。多阶段任务可以调用 `$radiology-pipeline`，单项任务可以直接调用 `$radiology-design`、`$radiology-stats`、`$radiology-writing` 等。

```text
用 radiology-pipeline 帮我梳理这项多中心影像研究，识别现有证据、缺失材料和下一步任务。
用 radiology-radiomics 审查这个影像组学流程的预处理、特征筛选和数据泄漏风险。
用 radiology-prereview 对这篇稿件做投稿前预审，按严重程度列出问题。
```

Windows 可检查总入口文件是否已复制：

```powershell
Test-Path (Join-Path $env:USERPROFILE '.codex\skills\radiology-pipeline\SKILL.md')
```

返回 `True` 说明文件存在；还应在新任务中确认技能能被发现。文件存在不等于模型行为或科研结果已通过验证。

## 4. Claude 与可选依赖

Claude 的本地插件资料、单技能安装示例、检索 MCP、Python/R 依赖和包校验说明见 [技能包安装文档](radiology-skills/install.md)。其中 `C:\radiology-Skill` 是原开发机路径，在本仓库布局下应替换为本地 **`仓库根目录/radiology-skills` 的实际绝对路径**。

完整插件根是包含 `.claude-plugin/` 和 `.codex-plugin/` 的内层目录。仓库已公开发布不代表已登记到任何远程插件市场；请按所用客户端实际支持的本地安装方式操作。

## 5. 文档与使用范围

- [40 个技能的完整介绍与索引](README.md)
- [原始技能包文档](radiology-skills/README.md)
- [打包与校验要求](radiology-skills/RELEASE.md)

技能用于科研辅助。数据、分析、结论、伦理审批和投稿材料仍需由研究团队核验；具体期刊和基金要求应以当次官方规则为准。