# Design theory — typography, layout, color, honesty

## Information hierarchy (multi-panel)
- One figure tells one story; each panel answers **one** question. No two panels answer the
  same question.
- Order panels by argument: overview → key result → supporting/mechanism. Reading order
  left-to-right, top-to-bottom.
- Composite figures: a schematic/flow panel (A) can orient the reader before data panels.

## Typography
- Sans-serif (Arial/Helvetica). One family throughout. Sizes: labels ~8 pt, ticks ~7 pt,
  titles ~9 pt **at final print size** — build the figure at column width so this holds.
- Avoid: 3-D bars, heavy gridlines, drop shadows, rainbow colormaps for continuous data,
  dual y-axes unless unavoidable.

## Color
- Default **Okabe-Ito** color-blind-safe palette (api.md). Never encode meaning by red/green
  alone; add shape/linestyle redundancy.
- Continuous data: perceptually-uniform maps (viridis/cividis/magma). Diverging data
  (z-scores, log fold-change): a diverging map **centred at 0** (e.g. RdBu) with a labelled
  colorbar.
- Keep category↔color mappings **consistent across all figures** in the paper.

## Honest graphics
- Show uncertainty (CI band/error bars; state what they are). Show n. Show data points for
  small-n group comparisons (don't hide n behind a bar).
- Don't truncate axes to dramatize; if a break is needed, mark it. ROC/calibration use full
  0–1 square axes with the reference diagonal.
- Bars start at 0 for counts/magnitudes; log scale only when justified and labelled.

## Accessibility & reproduction
- Check the figure in grayscale and with a color-blindness simulator.
- Sufficient contrast; line weights ≥ 0.8 pt so they survive printing.
- Vector text remains selectable/translatable (`svg.fonttype='none'`).

## Anti-redundancy
- If two panels would carry the same message, cut one or merge.
- Legends/captions are self-contained but not repetitive of axis labels.
- Tables vs figures: exact values that must be read precisely → table; patterns/comparisons →
  figure. Don't duplicate the same data as both.
