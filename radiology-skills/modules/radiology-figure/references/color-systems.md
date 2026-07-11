# Color systems — one coherent palette for the whole paper

A figure set is judged as a *set*. The fastest way to look amateur is to let one figure use a
bright clinical palette and another a muted one, or to let "high-risk" be red in the KM and
orange in the bar chart. Pick **one** palette, map it to **semantic roles**, and reuse it in
every panel of every figure.

## Decision: which palette

| Need | Use | Why |
|---|---|---|
| Accessibility-critical / general default | **Okabe-Ito** (see api.md) | Color-blind-safe; the safe default for any journal |
| Clean "Nature-journal" look | **NPG** (ggsci-style) | Saturated but harmonious; widely seen in high-impact imaging-AI papers |
| Soft, low-saturation house style (often requested) | **Morandi** | Muted, elegant; pairs well with grayscale imaging panels |

Whichever you pick, **always** run the grayscale + color-blind check (design-theory.md). Morandi
and NPG are not guaranteed color-blind-safe — if a reviewer or the journal needs it, fall back to
Okabe-Ito or add redundancy (linestyle/marker/labels).

## Semantic role mapping (the key idea)

Don't assign colors per-figure. Assign them per-**meaning**, once, then every figure inherits:

| Role | Examples | NPG | Morandi (brighter) |
|---|---|---|---|
| Low / control / reference / favourable | low-risk group, CCR, met-free, habitat-cleared | `#3C5488` navy | `#6F9BB5` dusty blue |
| High / event / index / unfavourable | high-risk group, +marker, metastasis, residual | `#E64B35` red | `#C56B5A` terracotta |
| Intermediate | discordant/mid tertile | `#E8A33D` amber | `#D8B265` ochre |
| Neutral / "no signal" | prognosis-neutral feature, treat-all line | `#8491B4` slate | `#A2B189` sage |

The same red means "high/event" in the KM, the box plot, the ROC, the bar and the Sankey. A
reader learns the code once. Keep a single `C = {...}` dict in the script and never hardcode a
hex inside a plotting call.

## Morandi palette (low-saturation, "brighter" variant)

```python
C = {"low":"#6F9BB5", "high":"#C56B5A", "mid":"#D8B265", "neutral":"#A2B189", "grey":"#A7AAB0"}
# 3-level ordered risk ramp reads low→high as dusty-blue → ochre → terracotta
```
Morandi tones are deliberately greyed. **Risk-ordered groups must still differ in *value*
(lightness), not only hue** — otherwise low/intermediate/high blur together. Put the lightest at
"low", the most saturated/deep at "high". Verify by converting to grayscale: the three should
still read as light→dark.

## NPG palette
```python
NPG = {"red":"#E64B35","blue":"#4DBBD5","green":"#00A087","navy":"#3C5488","orange":"#F39B7F",
       "slate":"#8491B4","teal":"#91D1C2","brightred":"#DC0000","brown":"#7E6148","tan":"#B09C85"}
```

## Hard rules (learned the hard way)

1. **One palette per manuscript.** Two color systems across figures (e.g. a vivid teal KM next
   to a navy/red ROC) is the #1 "looks inconsistent" flaw. Unify before polishing anything else.
2. **Semantic constancy.** Map color→meaning once; reuse everywhere. "Clinical low-risk" and the
   "habitat-cleared" reference can share the same blue on purpose (it signals concordance).
3. **Neutral = grey/sage, on purpose.** A prognosis-neutral feature or a "treat-all" reference
   should be visually muted, not a 4th loud hue.
4. **Diverging data centred at 0** (z-scores, Δ): a diverging map centred at zero, not the
   categorical palette.
5. **Continuous data**: perceptually-uniform (viridis/cividis/magma) — never the categorical
   palette, never rainbow/jet.
6. **Re-check in grayscale and with a CB simulator** after the palette is locked.

## Categorical sets that aren't an ordered ramp

For things like habitat/cell-type/sequence labels (no low→high order), still keep them fixed
across every figure, and prefer one warm + one cool + one neutral so they separate in grayscale.
Example used in a habitat paper: inner high-risk = terracotta, middle prognosis-neutral = sage
grey, outer = ochre — the "neutral" middle is intentionally grey so it recedes.

→ Render preamble and the exact dicts live in `api.md`; cross-figure enforcement in
`figure-set-consistency.md`.
