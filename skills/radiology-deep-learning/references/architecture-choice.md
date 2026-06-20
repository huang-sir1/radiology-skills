# Architecture choice — match capacity to data and task

The right architecture is the smallest one that fits the task and the cohort. Bigger is not
better on small, single-center imaging data.

## Dimension

| Choice | Use when | Watch-outs |
|---|---|---|
| **2D** | Thick slices, 2D convention, limited data, per-slice labels | Loses 3D context; aggregate slice→patient carefully (no leakage) |
| **2.5D** | Some 3D context cheaply (adjacent slices as channels) | Still not full volumetric |
| **3D** | Volumetric biology, isotropic data, enough cases | Memory-heavy; needs more data; slice-thickness sensitivity |

## Family / task head

| Task | Typical choice | Notes |
|---|---|---|
| Classification / diagnosis | CNN (ResNet/EfficientNet), ViT/Swin if data allows | ViT/Transformers are data-hungry — usually need pretraining |
| Segmentation | U-Net / nnU-Net (strong default), 3D U-Net | nnU-Net is a hard baseline to beat — use it as the comparator |
| Detection | RetinaNet/FCOS/YOLO-family, nnDetection | Report FROC and operating points |
| Prognosis / survival | CNN/Transformer encoder + survival head (Cox/discrete-time) | Event count gates capacity (EPV) |
| Foundation-model transfer | Pretrained medical/general encoder → fine-tune or linear-probe | Compare against task-trained baseline |

## Capacity vs cohort size (orientation)

- **Hundreds of patients, single center:** transfer learning or a strong simple CNN; heavy
  augmentation; nested CV; avoid training large models from scratch.
- **Thousands, multi-center:** larger models, 3D, Transformers, self-supervised pretraining
  become reasonable.
- Always pre-register the **baseline** the proposed model must beat (radiomics/clinical model,
  nnU-Net, simpler CNN, or radiologists).

## Foundation models / self-supervised (when in scope)

- Justify the benefit on *this* data with a fair task-trained baseline.
- Report pretraining data, encoder, fine-tuning vs linear-probe, and that the external test never
  leaked into pretraining.

## Reporting sentence

*"A 3D ResNet encoder (ImageNet-pretrained, fine-tuned) was used for classification; nnU-Net
served as the segmentation baseline. Given the cohort size (n=…), capacity was constrained and
compared against a radiomics LASSO model and two radiologists."*
