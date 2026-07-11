# radiology-radiogenomics

面向影像表型与分子生物学机制连接的 radiogenomics / imaging-multi-omics 高难度研究 skill。它覆盖从 matched-cohort feasibility 到统计分析、机制验证、投稿材料和 rebuttal 的完整链条，重点防止这类研究最容易被审稿人击中的问题：匹配样本过小、batch / scanner 混杂、高维多重比较、组织取样与影像 ROI 空间错配、以及生物学结论过度解读。

## 它能做什么

- 评估 TCIA / TCGA、GEO、dbGaP、EGA、cBioPortal、ICGC、HCA 和机构数据中的 **matched imaging-omics intersection**。
- 建立 **sample-to-image mapping**：patient、lesion、habitat、biopsy、histology、spatial omics 与影像 ROI 的对应关系。
- 设计影像 pipeline：IBSI radiomics、deep features、scanner/site harmonisation、registration、imaging habitats。
- 处理 omics QC / preprocessing：RNA-seq、mutation、methylation、CNV、proteomics、batch variables、normalization、missing data、accessions。
- 制定 analysis plan：primary hypothesis、discovery scan、FDR、train-only preprocessing、nested CV、validation、sensitivity analyses、negative controls。
- 选择 multi-omics integration：MOFA / MOFA+、iCluster、SNF、DIABLO / mixOmics、sparse CCA、multi-block PLS、early / intermediate / late fusion。
- 连接 single-cell 和 spatial biology：deconvolution、pseudobulk、spatial transcriptomics 与 imaging habitats。
- 准备 submission package：supplement tables、checklists、data/code availability、cover-letter angle、suggested reviewers、radiogenomics rebuttal playbook。

## 参考文件

```text
references/
├── cohort-design.md                    数据源、匹配、matched n、验证、伦理
├── sample-to-image-mapping.md           组织/活检/空间样本与影像 ROI/habitat 对应
├── radiomics-pipeline.md                分割、IBSI/deep features、habitats、harmonisation
├── omics-qc-preprocessing.md            RNA/mutation/methylation/proteomics QC 与 batch
├── analysis-plan-sap.md                 protocol/SAP、primary vs discovery、FDR、validation
├── multi-omics-integration.md           MOFA+、iCluster、SNF、DIABLO、sparse CCA、fusion
├── single-cell-spatial.md               deconvolution、pseudobulk、spatial omics 与 habitats
├── association-validation.md            feature-gene/pathway association、signatures、validation
├── biological-validation.md             pathway/cell/spatial/IHC corroboration 与 claim ladder
├── pitfalls.md                          leakage、batch、double-dipping、小样本、空间错配
├── radiogenomics-submission-package.md  稿件、补充材料、清单、数据代码上传包
└── reviewer-playbook.md                 预审与 rebuttal 模式
```

## 典型触发

- “设计一个 TCIA-TCGA radiogenomics 研究，把 MRI habitat 和 hypoxia pathway 连接起来。”
- “帮我做 biopsy location 与 MRI ROI 的 sample-to-image mapping table。”
- “起草 radiogenomics statistical analysis plan，包括 primary hypothesis、FDR 和 validation。”
- “审查 RNA-seq preprocessing 和 ComBat 计划是否有 leakage / batch confounding。”
- “MRI radiomics 和 RNA-seq、methylation 应该用 MOFA 还是 DIABLO 整合？”
- “准备 radiogenomics 投稿包，并预判审稿人会质疑什么。”

## 边界

不会编造 association、cohort count、accession、approval、p 值、effect size、validation result 或完成过的 reviewer action。feature-gene correlation 默认是有边界的假设，只有独立验证和生物学验证足够时才升级为更强机制结论。
