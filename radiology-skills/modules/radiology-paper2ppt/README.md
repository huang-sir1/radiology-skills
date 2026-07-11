# radiology-paper2ppt

面向组会、读片会、文献汇报和 journal club 的影像论文转中文 PPT skill。它不是把论文逐段搬进幻灯片，而是提炼研究问题、证据链、关键图表、方法学优缺点和可供讨论的审稿视角，生成可以直接汇报的 `.pptx`。

## 它能做什么

- 判断论文类型：diagnostic accuracy、prediction model、radiomics、radiogenomics、review 等，并按证据链组织 slide flow。
- 选择并裁剪真正支撑论点的图表：影像 panel、ROC / KM / calibration / forest、cohort table、scanner table。
- 写中文 slide text 和 speaker notes，构建真实 `.pptx`，并进行 package QA。
- 增加方法学点评 slide：CLAIM / CLEAR 合规、外部验证、leakage、calibration、可复现性、临床意义。

## 典型触发

- “把这篇 Radiology 论文做成读片会 PPT，中文，带演讲者备注。”
- “组会汇报这篇 radiomics 论文，重点讲方法和验证。”
- “把这篇影像 AI 论文做成 10 分钟 journal club。”

## 边界

不会编造结果、数字或图表细节；来源不完整时会明确标记缺口。PPT 构建交给 `pptx` skill，图表提取交给 `pdf` / `radiology-reader`。
