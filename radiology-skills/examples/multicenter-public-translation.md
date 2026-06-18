# Example: multicenter design with public datasets, ethics, and translation

## User request

```text
我们有 4 家医院的乳腺 MRI 数据，想预测新辅助治疗 pCR。还想找 TCIA/TCGA/GEO 数据做外部验证或机制解释。请帮我设计多中心方案、公共数据库使用、伦理数据共享写法，以及后续读者研究和临床转化路线。
```

## Expected module route

- `多中心`
- `公库`
- `伦理`
- `转化`
- `设计`
- `统计`
- `验证`
- `数据`
- `机制`

## Expected output shape

```text
任务定位
- 主模块：多中心
- 相关模块：公库、伦理、转化、设计、统计、验证、数据、机制
- 当前最大风险：中心差异、终点一致性、公共数据是否可配对、临床转化证据不足

分模块建议
| 模块 | 关键判断 | 必须补充 | 建议动作 |

需要作者确认
- 每中心样本量和 pCR 数量
- MRI 序列和扫描协议
- 治疗方案和 pCR 定义
- 公共数据是否有影像-组学配对
- IRB/consent waiver/data-use agreement
- 读者研究目标和使用场景
```
