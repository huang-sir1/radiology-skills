# Global research-intent routing

This is the product-level router for the independently published `radiology-skills` suite. Route by
the user's **current scientific decision or requested artifact**, not by whichever manuscript section
or tool name happens to appear in the prompt.

## Routing contract

1. Select exactly one **primary owner** for the current decision.
2. Add collaborators only for separable work with an explicit handoff artifact.
3. Preserve the domain context, independent unit, evidence state, Claim IDs and source locators in
   every handoff.
4. Do not turn a collaborator into a hidden prerequisite: a user may enter any bounded route
   directly with incomplete materials.
5. If an ambiguity changes the estimand, independent unit, evidence boundary or requested artifact,
   resolve it from the supplied context first; ask only about the material ambiguity that remains.
   Otherwise choose the narrowest reasonable route and proceed. Do not repeat answered questions.
6. Complete or freeze the current decision before moving to a later writing, review or submission
   stage.

## Unique primary-owner map

| Current user intent / decision | Primary owner | Collaborators when needed | Primary output | Must not be swallowed by |
|---|---|---|---|---|
| receive academic coaching when the immediate decision is unclear, spans stages, or requires learner-state continuity | `radiology-pipeline` | one unique specialist after the decision boundary is known | tutor state, bounded decision, specialist handoff and next learning check | a prematurely guessed mechanism, analysis or writing route |
| coordinate, resume or audit a whole research project | `radiology-pipeline` | all stage owners | passport, dashboard, artifact/gate state and next decision | a writing-only route |
| identify frontier/gap/novel question | `radiology-frontier` | `radiology-search`, then scope design owner | ranked question options with evidence/feasibility boundary | journal selection or prose polish |
| discover/retrieve/deduplicate papers or datasets and build a search corpus/gap matrix | `radiology-search` | `radiology-citation` for claim-level verification/export; `radiology-systematic-review` owns formal protocol/screening/synthesis | reproducible query log, corpus and gap matrix | citation formatting or a full formal review |
| design/run/audit a formal scoping review, systematic review, evidence synthesis or meta-analysis | `radiology-systematic-review` | `radiology-search`, `radiology-citation`, `radiology-stats`, `radiology-reporting`, `radiology-writing` through explicit artifacts | protocol, screening/extraction/RoB records, synthesis decision and evidence-bounded writing handoff | ordinary literature discovery or routine statistics |
| assess imaging feasibility and lock question/estimand/design | `radiology-design` | `radiology-stats`, domain execution owner | feasibility verdict, study blueprint, validation plan, protocol lock | frontier trend scanning |
| add disease/organ-specific clinical context, endpoint/reference-standard/treatment-timeline constraints or expert mentoring | `radiology-clinical-domain` | `radiology-design`, active imaging/mechanism owner, `radiology-translation` | domain playbook, clinical-context lock, review flags and learner decision memo | general study design or individual clinical advice |
| qualify image series/phases/sequences, acquisition, contrast/tracer, reconstruction, quantitative transforms, artifacts, dose, phantom/test-retest or protocol drift | `radiology-acquisition-qc` | `radiology-clinical-domain`, `radiology-data`, `radiology-annotation`, downstream imaging owner, `radiology-stats` | frozen imaging measurement/acquisition-QC passport, accepted-image gate, deviations and claim ceiling | cohort inventory, annotation, downstream preprocessing or generic method review |
| interpret standalone bulk/scRNA/spatial/pathology/perturbation mechanism evidence, lock a mechanism claim, or audit an imaging–mechanism bridge | `radiology-radiogenomics` | execution/design owner, `radiology-design` for imaging design, domain/statistics owners | alternative-mechanism, bridge, causal-boundary and claim-ceiling artifact | pure radiomics, transcriptomics execution, generic writing/prereview or rebuttal |
| build cohort/data dictionary, provenance, availability or de-identification/share plan | `radiology-data` | `radiology-ethics` for governance; `radiology-search` for repositories/datasets | cohort/data artifact and availability/de-identification plan | analysis or ethics prose alone |
| design ROI/VOI/mask/reference annotation and geometric QC | `radiology-annotation` | `radiology-data`, `radiology-radiomics`/`radiology-deep-learning` | annotation SOP, QC and reproducibility plan | general model-method review |
| resolve ethics, consent, privacy or governance | `radiology-ethics` | `radiology-data` | verified/conditional ethics and governance artifact | data availability writing |
| audit authorship/contributor eligibility, undisclosed COI/AI use, selective reporting, plagiarism or text/data/image integrity concerns | `radiology-research-integrity` | `radiology-ethics`, `radiology-prereview`, institutional/journal integrity owners | allegation-neutral concern ledger, evidence class, due-process route and bounded verdict | ethics approval, ordinary scientific prereview or misconduct adjudication |
| plan or audit multicentre delivery, roles/RACI, milestones, dependencies, resources, freezes, risks, deviations and closeout | `radiology-research-ops` | scientific owner, `radiology-data`, `radiology-ethics`, site/institutional owners | versioned operational plan, responsibility/dependency/risk ledgers and escalation/closeout receipt | scientific design, grant merit, regulatory approval or project orchestration alone |
| design or audit a Delphi/nominal-group/consensus statement or evidence-to-recommendation guideline | `radiology-consensus-guideline` | `radiology-systematic-review`, `radiology-reporting`, clinical/ethics/equity owners | scope/panel/COI/evidence-to-decision/voting/recommendation/update packet | evidence synthesis alone, checklist completion or informal expert opinion |
| configure or audit a hand-crafted radiomics pipeline | `radiology-radiomics` | `radiology-annotation`, `radiology-method-evaluation`, `radiology-stats` | executable pipeline/configuration and leakage audit | general method evaluation or statistics |
| configure, train or audit an imaging deep-learning pipeline | `radiology-deep-learning` | `radiology-annotation`, `radiology-method-evaluation`, `radiology-stats` | model/training/validation spec or execution record | method-evaluation-only route |
| plan, build, run or domain-audit a real bulk/sc/snRNA/spatial transcriptomics pipeline, including a method-specific controlled rerun | `radiology-transcriptomics-analysis` | `radiology-data`, `radiology-method-evaluation`, `radiology-stats`, then `radiology-radiogenomics` for claims; independent replay evidence goes to `radiology-reproducibility` | modality plan/code/run manifest, QC/exclusion ledger and verified result artifacts | mechanism interpretation, method defensibility or cross-domain replay certification |
| design, mentor, audit or interpret functional wet-lab mechanism validation | `radiology-experiment-design` | `radiology-radiogenomics`, `radiology-method-evaluation`, `radiology-stats`, `radiology-ethics` | hypothesis-discriminating experiment/control plan, gate audit or evidence-bounded interpretation | computational perturbation, generic mechanism narrative or laboratory SOP execution |
| judge parameter provenance, metric fit, method fit, benchmark fairness, ablation or sensitivity | `radiology-method-evaluation` | active domain owner; `radiology-stats` for inference | separate parameter/metric/method ledgers, robustness/failure result and claim verdict | statistics, full prereview or writing |
| plan, compute or report statistical inference | `radiology-stats` | domain owner; `radiology-method-evaluation` when comparison design is unresolved | estimand/test/CI/multiplicity/code/reporting handoff | general methodology judgement |
| design clinical use, reader study, prospective/real-world validation or deployment | `radiology-translation` | `radiology-design`, `radiology-stats`, `radiology-deep-learning` | use scenario, reader/prospective/workflow plan | paper translation/reading |
| design/audit interviews, focus groups, observation, think-aloud, reflexive qualitative analysis or genuine mixed-methods integration | `radiology-qualitative-mixed-methods` | `radiology-design`, `radiology-stats`, `radiology-translation`, `radiology-ethics` | qualitative/mixed-methods passport, sampling/fieldwork/analysis trail, joint display and discordance ledger | usability notes, stakeholder management or quantitative inference alone |
| design/audit cost-effectiveness, cost-utility, budget impact, decision model, QALY/ICER, PSA or value-of-information analysis | `radiology-health-economics` | `radiology-clinical-domain`, `radiology-design`, `radiology-stats`, `radiology-translation` | decision problem, pathway/model, input ledger, incremental/uncertainty results and HTA handoff | grant budget, decision-curve net benefit or reimbursement authorization |
| audit/package executable provenance, environments, manifests, frozen tolerances and independent computational replay | `radiology-reproducibility` | execution owner, `radiology-data`, `radiology-stats`, `radiology-translation` | replay package/receipt and per-result evidence ladder | data availability, repository presence, scientific validity or external clinical validation |
| plan/create/audit a scientific figure | `radiology-figure` | source domain, `radiology-stats` | traceable render plus source-data/visual QA | table or manuscript prose |
| plan/create/audit a publication table | `radiology-table` | source domain, `radiology-stats` | editable table plus value/source reconciliation | figure or prose writing |
| draft/restructure manuscript argument or sections from fixed evidence | `radiology-writing` | scientific owner, `radiology-method-evaluation`, `radiology-stats` | claim-bound section architecture and prose | language polish or scientific review |
| build/audit a monograph or article-based thesis (学位论文), thesis prereview or defense deck | `radiology-writing` | `radiology-prereview` (thesis-prereview), `radiology-paper2ppt` (defense deck) | thesis mode/rule passport, contribution spine and chapter package | institutional regulations and examiner decisions (external human authority) |
| tighten/copyedit existing prose without changing science | `radiology-polishing` | `radiology-writing` when restructuring is needed | polished text plus scientific-drift check | new manuscript drafting |
| find or verify support for a specific manuscript claim and export references | `radiology-citation` | `radiology-search` for broad discovery | claim-source verification and reference-manager file | broad literature review |
| select and complete reporting/quality checklists | `radiology-reporting` | domain owner, `radiology-prereview` | item-level compliance matrix | scientific validity or upload-package audit |
| run whole-manuscript imaging scientific prereview | `radiology-prereview` | `radiology-radiogenomics` for mechanism; `radiology-method-evaluation` for focused criteria | digest-bound findings and closure criteria | checklist or file-format audit |
| adjudicate decision letters, draft rebuttal and verify revision closure | `radiology-response` | original scientific/finding owners | commitment/result/location/boundary response ledger | initial manuscript review or generic writing |
| select a target journal/submission ladder | `radiology-journal` | `radiology-search`, `radiology-reporting` | reach/target/safety fit with live-scope verification | submission-file audit |
| audit all final submission files, file types, formats and portal package | `radiology-submission` | `radiology-journal`, `radiology-reporting` | fail-closed upload manifest/readiness receipt | scientific prereview or journal selection |
| draft, review or revise a grant proposal; triage a live call; or run a criterion-based mock panel | `radiology-grant` | question/design/domain/statistics/ethics/data owners | call passport, criterion findings, aim–evidence–risk contract and revision-closure ledger | manuscript prereview or proposal-defense slide production |
| audit one exact funder/cycle/application's final system fields, files, attachments and institutional handoff | `radiology-grant` | scientific/budget owners and the authorized institutional research office | version-bound funder package inventory ending at `HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED` | portal action, institutional attestation, post-award reporting or an external submission claim |
| create a source-grounded bilingual paper reader | `radiology-reader` | `radiology-citation` | full paper reader with figure/table anchors | clinical reader-study design |
| plan, create, edit or repair a scientific presentation from papers, proposals or project evidence | `radiology-paper2ppt` | frozen source owner, `radiology-reader`, `radiology-figure`, `radiology-table`, `radiology-stats` | audience/decision passport, source-grounded slide deck, rehearsal and render-QA receipt | grant-content review, manuscript drafting or standalone figure creation |
| plan/audit evidence-bounded public or professional dissemination such as posters, plain-language summaries, press/social copy, policy or stakeholder briefs | `radiology-dissemination` | scientific owner, `radiology-paper2ppt`, `radiology-figure`, integrity/data owners | audience/channel passport, claim-source/derivative ledger, accessibility/privacy/release plan | slide production, manuscript prose or evidence-free promotion |
| design/audit a reproducible bibliometric or research-impact assessment, author/institution disambiguation, normalization or responsible metric interpretation | `radiology-bibliometrics` | `radiology-search`, `radiology-citation`, library/research-evaluation owner | identity-resolved corpus, query/date snapshot, normalized indicator matrix and interpretation limits | literature review, scientific quality rating or individual assessment by one metric |
| assess disclosure, prior-art/search handoff, inventorship/ownership boundaries, software/data rights and non-confidential innovation-transfer readiness | `radiology-innovation-transfer` | `radiology-translation`, `radiology-research-integrity`, data/legal/institutional owners | innovation-state passport, rights/evidence/risk map and authorized-owner handoff | clinical translation, publication search, grant writing or legal clearance opinion |
| decide how patient/public/stakeholder involvement or equity evidence changes the question, endpoint, burden, threshold, protocol or dissemination plan | `radiology-design` | `radiology-qualitative-mixed-methods`, `radiology-ethics`, `radiology-data`, `radiology-stats`, `radiology-translation`, `radiology-research-ops`, `radiology-reporting`, `radiology-dissemination` for their separable decisions | PPI/stakeholder/equity decision ledger and protocol-impact record | qualitative inference, consent authorization, subgroup inference, implementation evidence or one-way engagement |
| resolve a post-publication error/integrity signal and correction/retraction escalation | `radiology-research-integrity` | publisher/editor, institution/RIO, scientific owner, `radiology-citation` | allegation-neutral evidence/version chain and authorized correction/retraction handoff | current-citation lookup, ordinary debate/new evidence or misconduct adjudication |
| verify a published work's current version/status and issue a corrected claim-level citation | `radiology-citation` | `radiology-research-integrity` when an error/integrity signal exists | current publisher/version locator and corrected citation/claim-source state | correction authority or whole-project staleness propagation |
| audit production proofs/queries, accepted-manuscript or public-access deposit files and publisher-requested package items | `radiology-submission` | `radiology-writing`, `radiology-figure`, `radiology-table`, `radiology-data`, authorized author/institutional owner | versioned production/deposit file manifest and human-action gate | scientific rewriting, repository access decisions or external submission action |
| handle a post-publication data/code/model request, repository update, controlled access, retention or destruction decision | `radiology-data` | `radiology-ethics`, `radiology-reproducibility`, repository/institutional owner | authority/request/release or retention/closeout receipt | production-file audit, scientific validity or an inferred sharing permission |
| run living-review surveillance, update transition or evidence-product retirement | `radiology-systematic-review` | `radiology-search`, `radiology-citation`, `radiology-stats`, `radiology-dissemination` | new-search/corpus/change/synthesis/certainty ledger and update/retirement state | bibliometric attention snapshot or a one-time citation check |
| correct, reissue, withdraw or update a public/patient/clinical/policy/media derivative after its source changes | `radiology-dissemination` | source scientific owner, `radiology-research-integrity`, `radiology-data` | affected-derivative ledger, corrected artifact plan and release/withdrawal gate | correction authority for the source publication or deployed-system change control |
| monitor, change, roll back or retire a deployed intervention after publication/release | `radiology-translation` | `radiology-research-ops`, `radiology-data`, safety/regulatory/institutional owners | production/CAPA/revalidation/rollback/retirement evidence state | ordinary project closeout or public communication alone |
| track post-award conditions, amendments, annual/interim/final reports, sponsor deliverables or closeout obligations | `radiology-research-ops` | funder/institutional owner, `radiology-data`, `radiology-reproducibility`, original scientific owners | award-term/report/amendment/retained-obligation ledger ending at a human funder-action gate | pre-award proposal/package review, scientific truth, funder acceptance or financial sign-off |
| propagate a published-source/version change across the whole project and identify the earliest stale gate | `radiology-pipeline` | each affected unique owner | cross-artifact staleness map and bounded owner handoffs | correction adjudication, citation verification or specialist artifact repair |

## High-risk disambiguation rules

If a prompt matches a registered `clarification_cases` entry, first read its supplied and prior
conversation context. Return `CLARIFY` and wait for the user's choice only while a material ambiguity
remains; present only the unresolved meanings. A previously selected purpose or a supplied artifact
can already resolve the route. Do not guess a different scientific decision, repeat an answered
question, or require a ceremonial choice before proceeding. Clarification is a pre-route action;
once the decision is known, choose exactly one primary owner.

- “像导师一样带我学/我还不知道该问什么/帮我梳理整个课题” → `radiology-pipeline` tutor
  entry; once the current decision is explicit, hand one isolated task to its unique specialist.
- “直接给方案/答案” uses `direct-expert`; “引导我思考/苏格拉底式/检查我是否学会” uses
  `guided-learning`. Neither phrase authorizes simulation or file creation.
- “参数怎么设置并训练/运行” → domain execution owner. “这个参数/范围/选择过程能否支撑结论”
  → `radiology-method-evaluation`. “这些配置差异的 CI/P 值” → `radiology-stats`.
- “搭 bulk/scRNA/空间流程或真实运行” → `radiology-transcriptomics-analysis`; “解释生物
  机制或影像—机制桥” → `radiology-radiogenomics`; “评价 normalization/integration/空间尺度
  是否合理” → `radiology-method-evaluation`.
- “设计 IHC/扰动/rescue/动物或类器官验证” → `radiology-experiment-design`; “解释已有观察
  组学机制” → `radiology-radiogenomics`; “执行本地湿实验 SOP”仍由受训实验室人员负责.
- “正式系统综述/范围综述/meta-analysis 全链” → `radiology-systematic-review`; “找一批文献
  或数据集” → `radiology-search`; “给已定义效应量做统计合并” → `radiology-stats`.
- 裸提示“做个 meta-analysis”必须先澄清是从协议到综合的完整证据综合，还是对已经定义、
  确认可比的效应量行做统计合并；在回答前不得静默选择 owner.
- “疾病/器官特异的临床问题、参考标准和治疗时间轴” → `radiology-clinical-domain`;
  “锁定整项研究 estimand/验证设计” → `radiology-design`.
- “这项疾病应做什么检查/时相/时间窗” → `radiology-clinical-domain`; “现有 series、采集、
  重建、DICOM 定量变换、伪影、剂量或体模是否满足测量结论” → `radiology-acquisition-qc`.
- “影像文件/病例库存、来源与去标识” → `radiology-data`; “哪套图像可进入分析及协议漂移
  如何限制结论” → `radiology-acquisition-qc`; “ROI/标签怎样产生” → `radiology-annotation`;
  “进入分析后的 resampling/normalisation/feature/model 流程” → 对应 radiomics/DL owner.
- “写已有方法评价结果” → `radiology-writing`; “设计/审阅方法评价证据” →
  `radiology-method-evaluation`.
- “检查整稿科学漏洞” → scope-aware prereview; “检查清单条目” →
  `radiology-reporting`; “检查所有上传文件与格式” → `radiology-submission`.
- “查一批文献/数据集” → `radiology-search`; “核实这句话该引哪篇并导出” →
  `radiology-citation`.
- “给现有文字润色” → `radiology-polishing`; “重建论证或从证据起草段落” →
  `radiology-writing`.
- “全文中英对照解读” → `radiology-reader`; “设计 radiologist vs AI 阅片者研究” →
  `radiology-translation` as primary owner, with `radiology-stats` only as an explicit statistical
  design/inference collaborator.
- “审阅/打分/修订标书科学内容” → `radiology-grant`; “把已冻结的标书做成项目答辩 PPT” →
  `radiology-paper2ppt`. The deck owner may expose source weaknesses but must return scientific
  changes to the grant owner instead of silently rewriting the proposal canon.
- “核验本年度基金系统最终字段、正文/预算/附件版本并交科研处” →
  `radiology-grant: funder-package-finalization`, machine state 最高为
  `HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED`; “获批后按 award 条款管理变更、年度/中期/结题
  报告与 sponsor deliverables” → `radiology-research-ops: post-award-funder-reporting`.
  后者只装配和追踪，科学方法/结果/主张仍回到原 scientific owner；两者都不代表机构提交或
  funder 接受.
- “按基金 call/评审准则审未来研究计划” → `radiology-grant`; “检查已完成论文的科学
  漏洞” → `radiology-prereview`. Do not transfer a manuscript rejection rubric to a proposal or
  report a mock funder review as an official panel result.
- “会议报告/组会/论文答辩/项目进展 PPT 的受众、叙事、版式或成品 QA” →
  `radiology-paper2ppt`; “单独制作一张科研图或影像图版” → `radiology-figure`.
- “从冻结证据起草论文段落” → `radiology-writing`; “把冻结证据转成受众特异 PPT” →
  `radiology-paper2ppt`; “核验目标期刊所有上传文件” → `radiology-submission`.
- “能做什么课题/estimand/验证” → scope design owner; “投哪本期刊” →
  `radiology-journal`.
- “作者排序、署名资格、COI/AI披露、选择性报告或图像/数据/文本完整性” →
  `radiology-research-integrity`; “伦理批准/同意/隐私” → `radiology-ethics`; “整稿科学漏洞” →
  `radiology-prereview`. The integrity skill documents and routes concerns but never declares misconduct.
- “里程碑、RACI、站点依赖、资源、冻结、延期和风险台账” → `radiology-research-ops`;
  “整项科研状态从哪一步继续” → `radiology-pipeline`; “研究问题和验证设计” → `radiology-design`.
- “Delphi/名义组/共识会议/证据到推荐/指南更新” → `radiology-consensus-guideline`;
  “系统检索与证据综合” → `radiology-systematic-review`; “RIGHT/AGREE/ACCORD 条目” →
  `radiology-reporting`.
- “访谈、焦点小组、观察、think-aloud、反身性、饱和度或 joint display” →
  `radiology-qualitative-mixed-methods`; a few usability comments without analysable records stay
  `FORMATIVE_FEEDBACK_ONLY`; implementation planning without qualitative inference → `radiology-translation`.
- “CEA/CUA、QALY、ICER、预算影响、Markov、PSA、VOI” → `radiology-health-economics`;
  “基金经费表” → `radiology-grant`; “DCA net benefit” → `radiology-stats` /
  `radiology-method-evaluation`.
- “代码/配置/环境/数据版本能否重跑、独立重放及容差是否通过” →
  `radiology-reproducibility`; “数据共享/保留/受控访问” → `radiology-data`; 新站离线或回顾性外部队列的
  population、estimand、validation lock → `radiology-design`; 新站前瞻工作流、reader/impact、部署监测或患者结局 →
  `radiology-translation`. Repository presence is not replay evidence.
- 裸提示“做外部验证”必须先澄清是独立队列离线/回顾性验证、新站点前瞻工作流影响验证，
  还是相同冻结输入上的独立重放；三者不能以“外部”一词互相替代.
- A transcriptomics `reproduce` mode owns assay/method-specific controlled rerun and QC diagnosis;
  `radiology-reproducibility` owns the cross-domain frozen package, operator independence, tolerance
  receipt and evidence-ladder claim. A bibliometric `audit-reanalysis` similarly owns counting,
  normalization/network-parameter sensitivity; pure package replay can be handed to reproducibility.
- “海报、通俗摘要、政策简报、新闻稿、社交媒体或利益相关方传播” →
  `radiology-dissemination`; “PPTX 成品、讲者备注和渲染 QA” → `radiology-paper2ppt`;
  “投稿图” → `radiology-figure`. Reach is not research impact.
- “会议摘要的受众/venue 字段、冻结结果压缩和提交前传播边界” →
  `radiology-dissemination`; “论文 abstract 作为稿件论证” → `radiology-writing`; “会议 portal
  的最终文件/字段核验” → `radiology-submission`; “内部会议纪要、决策、行动项、RACI 与截止日期” →
  `radiology-research-ops`. 裸提示“会议摘要”必须先澄清是大会投稿摘要、论文 Abstract、portal 文件、内部纪要还是会议 PPT.
- 裸提示“帮我看看论文”必须先澄清对象是待投稿整稿还是已发表论文，以及任务是科学预审、
  报告清单、投稿包核验、语言润色还是文献研读；不得把任一项默认为整稿预审.
- “引文网络、领域归一化、作者/机构消歧、数据库覆盖和影响快照” →
  `radiology-bibliometrics`; “找文献” → `radiology-search`; “核验某项主张的引用” →
  `radiology-citation`. A metric is not a quality verdict.
- “发明披露、公开披露时点、现有技术检索交接、inventor/contributor、软件/数据/IP 权利与
  技转准备度” → `radiology-innovation-transfer`; “临床部署证据” → `radiology-translation`;
  novelty search execution → `radiology-search`. Only qualified institutional/legal owners decide rights.
- 裸提示“做 PPI/公平性”必须先澄清是患者/公众共同塑造研究问题与方案、可分析的定性研究、
  参与者权利/同意、已定义 subgroup/equity estimand 的统计推断、部署中的可及性/伤害，还是
  单向公众传播。问题/终点/负担/阈值/方案改变 → `radiology-design`; 访谈/焦点小组和反身性
  分析 → `radiology-qualitative-mixed-methods`; 权利/同意 → `radiology-ethics`; subgroup 估计与
  不确定性 → `radiology-stats`; 工作流可及性/伤害/监测 → `radiology-translation`; engagement
  产品 → `radiology-dissemination`. PPI、participation 和 engagement 不得互相替代.
- “发表后有错误/疑似完整性问题，需要更正、撤回或机构/期刊升级” →
  `radiology-research-integrity`; “核实当前版本并更正引用” → `radiology-citation`; “处理校样、
  production query、accepted-manuscript/public-access deposit 文件” → `radiology-submission`;
  “处理数据/代码/模型请求、仓库更新或保留/销毁” → `radiology-data`.
- “living review 监测、更新或退役” → `radiology-systematic-review`; “更正/撤回患者、政策、
  媒体或公共衍生物” → `radiology-dissemination`; “已部署系统的 CAPA、变更、回滚或退役” →
  `radiology-translation`; “项目/award 的 retained obligations 与 closeout” →
  `radiology-research-ops`; “找出一处发表后变化让整项目哪些产物失效” → `radiology-pipeline`.
  当前引用核验不是更正授权，传播撤回不是源论文撤稿，项目 closeout 也不是部署退役.

## Handoff minimum

Use the smallest handoff that lets the receiver make the requested decision. For a bounded expert
question, carry `current decision | requested output | owner | supplied inputs/locators | evidence
state | material unknowns`. The input may be the user's question itself; a conceptual explanation
does not require a patient-level unit, dataset, Claim ID or project passport. Keep routing internal
when exposing it would add no useful choice for the user. Unknown inputs constrain the conclusion,
but do not block useful explanation or review of the available material.

For a study-level analysis, formal review or persistent project transfer, additionally carry:

`Route ID | current decision | scope/modalities | independent unit/hierarchy | Claim/Evaluation IDs |
inputs and exact locators | evidence state | decisions frozen | unresolved assumptions | requested
output | owner | measurement-passport/receipt IDs and protocol deviations when imaging is active |
acceptance/closure condition`.

For a guided-learning or learner-continuity transfer, also carry:

`interaction style | learning objective | target decision |
demonstrated level | baseline
attempt | misconception IDs | evidence of understanding | mastery status | current tutor state |
next transfer task | support preference | unresolved learner questions`.

Return `HANDOFF_INCOMPLETE` only when an input required for this decision is missing; name that
input and continue any independent work. Never demand all study and learner fields for every task.
Scientific decisions and evidence ceilings remain the same in concise and full project modes.
