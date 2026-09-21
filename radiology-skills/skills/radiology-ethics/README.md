# radiology-ethics

面向医学影像、影像组学、组学和机制研究的独立科研治理 skill。它不再只处理 human
subjects，而是先判断三个可并行、不可互相替代的分支：

- `human-subjects`：IRB/伦理委员会、知情同意或豁免、隐私、人体样本和数据共享；
- `animal-welfare`：IACUC/动物伦理委员会或本地等效机构、3Rs、福利终点和兽医监督；
- `biosafety-biosecurity`：IBC/本地等效机构、基因操作、潜在感染性材料、病原相关治理及
  dual-use 风险分流。

## 能做什么

- `classify`：从实际活动而非课题标题判断适用分支，识别复合审批；
- `audit`：逐项核对批准文件的编号、日期、适用地点、对象/物料/活动范围和修订记录；
- `draft`：只使用已提供、可追溯的事实起草伦理/动物福利/生物安全声明；
- `mentor`：解释为什么需要某一分支、最低闭环是什么、应由谁确认；
- `submission-handoff`：给最终投稿/修回链提供审批矩阵、证据定位和未闭合 STOP 项。

## 不可越过的边界

- 审批号、日期、豁免、物种/实验范围、IBC/IACUC 决定、containment、培训和本地负责人
  都是 author-only / institution-only facts，不能推断或补写。
- 法域、机构和政策会变化；必须记录当前官方来源、版本/访问日期和本地责任人。
- 任一适用审批缺失、过期、范围不符或相互冲突时，对相应活动/合规声明返回 `STOP`。
- 不分配或猜测生物安全等级，不提供病原改造、逃逸、扩增、释放、规避审查或其他危险
  实验操作细节；只做高层风险分流并交给本地授权机构。
- 写作不能补救未审批或超范围实施的研究。

## 核心材料

| 文件 | 用途 |
|---|---|
| `references/ethics-routing-and-stop-gates.md` | 三分支路由、复合审批、证据状态和 STOP gate |
| `references/approval-consent.md` | human-subjects、IRB/伦理、consent/waiver |
| `references/reidentification-risk.md` | 影像/基因组再识别风险 |
| `references/governance-sharing.md` | consent、DUA、共享承诺一致性 |
| `references/animal-welfare-review.md` | 动物伦理、3Rs、福利/兽医与写作审阅 |
| `references/biosafety-biosecurity-review.md` | 生物安全、基因操作、病原与 dual-use 安全分流 |
| `templates/research-ethics-governance-matrix.md` | 单项目三分支审批与证据矩阵 |
| `templates/local-ethics-oversight-profile.md` | 本地委员会、政策入口、负责人和时效配置 |

实验问题、对照和分析设计交给 `radiology-experiment-design`；本 skill 返回的是治理准入条件，
不是实验 SOP。去标识化与仓库交给 `radiology-data`，法律、兽医、containment 与事故处置仍由
当前本地授权责任人决定。
