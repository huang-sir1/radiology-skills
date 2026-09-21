# radiology-reader

面向影像科研论文的精读 skill。用户要求全文对照时，在用户提供全文或有适用再利用依据的条件下，生成段落级原文/译文对照，保留 Methods、统计、图表和 source anchors；用户要求概要或局部讲解时按请求深度输出。仅有 DOI、网页链接或摘要时，不将未获取的正文和图表当作已读证据。

## 它能做什么

- 生成整篇论文的中英对照 Markdown，保留方法学和统计细节。
- 将图表放在首次提及附近：影像 panel、ROC / KM / forest / calibration、cohort / scanner / performance table。
- 为每个 block 保留稳定 source anchors，并输出 `source_map.json` 方便回溯。
- 加入影像科研阅读提示：每张图该看哪个 metric、CI、window、label 或 methodological risk。

## 输出

`paper.md`（主文件）· `source_map.json` · `translation_notes.md` · `assets/`。

## 典型触发

- “把这篇 Radiology 论文做成中英对照全文阅读。”
- “把这篇 radiomics 论文翻译成完整 Markdown reader，保留 Methods 细节。”
- “读这篇论文，把 ROC 和 KM 图放到讨论它们的位置。”

## 下游衔接

PDF 解析交给 `pdf` skill；参考文献导出交给 `radiology-citation`；组会 PPT 交给 `radiology-paper2ppt`。
