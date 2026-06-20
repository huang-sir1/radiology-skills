# Mapping molecular samples to imaging phenotypes

The central radiogenomics question is not only whether a patient has both imaging and omics, but
whether the molecular sample plausibly corresponds to the imaged region.

## Required mapping table
Create a table before analysis:

`Patient | Imaging study ID | Imaging date | Modality/sequence | Lesion/region segmented | Tissue event date | Tissue source | Block/biopsy location | Molecular sample ID | Time gap | Treatment between scan and tissue? | Mapping level | Usable? | Reason`

## Mapping levels
- **Patient-level**: one tumour-level imaging vector matched to one patient-level omics sample.
  Acceptable for broad discovery, but claims must be bounded to patient-level association.
- **Lesion-level**: the sequenced lesion is the lesion segmented on imaging. Needed for
  multifocal disease.
- **Region/habitat-level**: biopsy block or spatial section is linked to an imaging habitat or
  subregion. This is stronger for mechanistic interpretation.
- **Section/spot-level**: spatial transcriptomics or histology regions are registered to tissue
  and then related to imaging habitats. This requires explicit registration uncertainty.

## Timing rules
- Prefer pre-treatment imaging closest to tissue acquisition.
- Record surgery, biopsy, radiation, systemic therapy, steroids, anti-angiogenic therapy, or any
  intervention between imaging and tissue. These can change both imaging and molecular state.
- Define an allowed time window. Out-of-window cases should be excluded or sensitivity-tested.

## Spatial mismatch traps
- Whole-tumour radiomics paired with a small biopsy can dilute or misrepresent regional biology.
- Necrotic, enhancing, edematous, invasive-margin, and viable tumour regions are biologically
  different; state which was sampled and which was segmented.
- A single histology section does not represent the whole tumour. Do not write as if it does.
- Micron-scale spatial omics cannot be claimed to map exactly to millimetre-scale MRI/CT without
  quantified registration uncertainty.

## Practical strategies
- If tissue location is unknown, use patient-level language and avoid spatial mechanism claims.
- If biopsy coordinates or block location are known, define a matching ROI/habitat and report the
  mapping protocol.
- If multiple samples exist per patient, pre-specify one primary sample or use patient-level
  aggregation; do not treat multiple samples as independent patients.
- For spatial transcriptomics, register slide to histology first, then relate histology regions to
  imaging habitats. Report each registration step and its uncertainty.

## Reporting language
Strong: "The sequenced enhancing-core biopsy was matched to the enhancing MRI habitat segmented
from the preoperative scan."

Bounded: "Because tissue sampling coordinates were unavailable, analyses were performed at the
patient level and interpreted as tumour-level associations rather than region-specific mechanisms."