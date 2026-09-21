# Multimodal inputs — how data enters the model

Declare exactly how each modality enters, where it fuses, and how missing modalities are handled.
Vague "we combined imaging and clinical data" is a reviewer magnet.

## Inputs and how they enter

| Input | Entry | Watch-outs |
|---|---|---|
| **Images** | Channels (sequences/phases stacked), or separate encoders | Co-register before stacking; state crop/resize |
| **Masks** | As an extra channel, or to crop/attention-gate the ROI | If mask gates input, the mask must be available at inference too |
| **Clinical variables** | Concatenate at the fusion layer (after normalisation fit on train) | Don't include post-outcome variables (leakage) |
| **Text (reports)** | Text encoder → fused embedding | **Report leakage**: the report may contain the label — exclude or mask it |
| **Molecular** | Late-fusion embedding | Only if matched per patient (→ radiology-radiogenomics) |

## Fusion strategies

- **Early fusion** — combine raw inputs/channels before the encoder. Simple; assumes alignment.
- **Intermediate (feature) fusion** — separate encoders → combine embeddings. Flexible; common.
- **Late fusion** — separate models → combine predictions. Robust to missing modalities.

State which, and why. Compare the multimodal model against the **best single modality** — fusion
must earn its complexity.

## Missing-modality handling (declare a rule)

- Drop cases (state how many; check it doesn't bias the cohort), impute embeddings, modality
  dropout during training, or a late-fusion model that tolerates absence.
- Whatever the rule, it must be the same at training and inference and not peek at the outcome.

## Leakage traps specific to multimodal

- **Report text** containing the diagnosis the model predicts.
- **Clinical variables** recorded *after* the outcome.
- Normalising clinical features on the whole cohort.
- A mask/ROI available only because a human already found the lesion (state the intended workflow).

## Reporting sentence

*"T1c, T2, and ADC were co-registered and stacked as input channels to a shared 3D encoder;
clinical variables (age, stage), normalised on training data, were concatenated at the penultimate
layer (intermediate fusion). Radiology reports were excluded to prevent label leakage. The
multimodal model was compared against the best single-modality model; cases missing a sequence
were handled by modality dropout."*
