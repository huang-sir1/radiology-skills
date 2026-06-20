# Feasibility and common rejection reasons

Feasibility is demonstrated, not claimed. Then pre-empt the reasons imaging-AI grants get
rejected.

## Demonstrating feasibility (可行性)

| Evidence | What it shows | Note |
|---|---|---|
| **Preliminary data** | The approach works at small scale | Use **real** results only — never fabricate; a modest honest pilot beats invented numbers |
| **Data access** | The cohort exists and is reachable | State n, centers, modalities, labels, ethics status |
| **Team capability** | Track record to deliver | Relevant prior publications/methods (→ research basis) |
| **Platform/methods** | Tools/pipelines ready | Named software, compute, collaborators (e.g. bioinformatics for omics) |
| **Ethics** | Governance in place or planned | Approval/consent route (→ radiology-ethics) |

## Close the technical route (技术路线)

A reviewer should trace, without gaps:

```
clinical need → key question → aim1 → method1 → expected result1 ┐
                            → aim2 → method2 → expected result2  ├→ integrated answer → question
                            → aim3 → method3 → expected result3 ┘
                 (validation + risk/contingency at each aim)
```

Mark where internal/external/prospective validation sits and the contingency if an aim's
assumption fails.

## Common rejection reasons (pre-empt each)

| Reason | Symptom | Fix |
|---|---|---|
| **Weak innovation** | "Novel model" with no specific increment | Reframe to a specific, classified innovation tied to the gap |
| **Engineering, not science** | Goal is "build/improve a model" | Reframe to a scientific question (reframe-and-innovation.md) |
| **Thin preliminary data** | No pilot supporting feasibility | Add a real small pilot; state data access |
| **Open-loop route** | Methods listed but not connected to the question/results | Redraw the closed loop with expected results |
| **Over-promising** | Too many aims / clinical deployment in 3 years | Scope to achievable aims; bound expected outcomes |
| **Unfocused aims** | Aims don't share one question | Subordinate all aims to the key scientific question |
| **No validation/generalisability** | Single-center plan claiming broad impact | Add external/prospective validation (→ radiology-design) |
| **Ethics/data gap** | No approval/access plan | Address governance (→ radiology-ethics) |

## Guideline verification (待核验)

Flag for the author to confirm against the **current** official 申报指南:
word/character limits, section format, attachments, ethics requirements, 限项 (application
limits), eligibility, and deadlines. These change yearly — do not rely on memory.
