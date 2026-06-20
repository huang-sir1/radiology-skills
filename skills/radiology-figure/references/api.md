# matplotlib API — preamble, palette, helpers

Start every figure script with this preamble so output is editable vector with text-as-text,
journal typography, and a color-blind-safe palette.

## Preamble (always first)
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "Liberation Sans"],
    "svg.fonttype": "none",      # keep text as <text>, not paths
    "pdf.fonttype": 42,          # embed TrueType (editable) in PDF
    "ps.fonttype": 42,
    "figure.dpi": 150,           # on-screen; export raster at >=300
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "font.size": 8,              # ~7-9 pt at final print size
    "axes.titlesize": 9, "axes.labelsize": 8,
    "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
    "lines.linewidth": 1.3,
})

# Column widths (inches): single ~3.35 in (85 mm), double ~6.7 in (170 mm)
SINGLE, DOUBLE = 3.35, 6.7

# Color-blind-safe (Okabe-Ito)
PALETTE = {"blue":"#0072B2","orange":"#E69F00","green":"#009E73","vermillion":"#D55E00",
           "skyblue":"#56B4E9","yellow":"#F0E442","purple":"#CC79A7","black":"#000000",
           "grey":"#999999"}

def save(fig, stem):
    fig.savefig(f"{stem}.svg")                 # primary, editable vector
    fig.savefig(f"{stem}.png", dpi=600)        # raster companion (or .tiff)
```

## ROC (with optional comparison)
```python
from sklearn.metrics import roc_curve, roc_auc_score

def plot_roc(ax, curves):
    # curves: list of dicts {y_true, y_score, label, color, auc_ci=(lo,hi)}
    for c in curves:
        fpr, tpr, _ = roc_curve(c["y_true"], c["y_score"])
        auc = roc_auc_score(c["y_true"], c["y_score"])
        lab = f'{c["label"]} (AUC {auc:.2f}'
        lab += f', 95% CI {c["auc_ci"][0]:.2f}–{c["auc_ci"][1]:.2f})' if c.get("auc_ci") else ')'
        ax.plot(fpr, tpr, color=c.get("color", PALETTE["blue"]), label=lab)
    ax.plot([0,1],[0,1], ls="--", lw=0.8, color=PALETTE["grey"])
    ax.set(xlim=(0,1), ylim=(0,1), xlabel="1 − Specificity", ylabel="Sensitivity")
    ax.set_aspect("equal"); ax.legend(loc="lower right", frameon=False)
```

## Calibration (+ prediction histogram)
```python
from sklearn.calibration import calibration_curve

def plot_calibration(ax, y_true, y_prob, n_bins=10):
    frac, mean = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy="quantile")
    ax.plot([0,1],[0,1], ls="--", lw=0.8, color=PALETTE["grey"], label="Ideal")
    ax.plot(mean, frac, "o-", color=PALETTE["blue"], label="Observed")
    ax.set(xlim=(0,1), ylim=(0,1), xlabel="Predicted probability",
           ylabel="Observed frequency"); ax.set_aspect("equal")
    ax2 = ax.inset_axes([0,-0.28,1,0.18])     # prediction distribution under the plot
    ax2.hist(y_prob, bins=20, color=PALETTE["grey"]); ax2.set_yticks([]); ax2.set_xlim(0,1)
    ax.legend(loc="upper left", frameon=False)
```

## Forest plot
```python
def plot_forest(ax, labels, est, lo, hi, pooled=None):
    y = np.arange(len(labels))[::-1]
    ax.errorbar(est, y, xerr=[np.array(est)-np.array(lo), np.array(hi)-np.array(est)],
                fmt="s", color=PALETTE["blue"], capsize=2, ls="none")
    ax.set_yticks(y); ax.set_yticklabels(labels)
    if pooled:  # (est, lo, hi)
        ax.axvline(pooled[0], ls="--", lw=0.8, color=PALETTE["vermillion"])
        ax.fill_betweenx([-0.8,-0.2], pooled[1], pooled[2], color=PALETTE["vermillion"], alpha=.4)
    ax.set_xlabel("Effect (95% CI)")
```

## Kaplan-Meier with numbers-at-risk
```python
from lifelines import KaplanMeierFitter

def plot_km(ax, groups, times=(0,12,24,36,48,60)):
    # groups: list of dicts {durations, event_observed, label, color}
    kms = []
    for g in groups:
        km = KaplanMeierFitter().fit(g["durations"], g["event_observed"], label=g["label"])
        km.plot_survival_function(ax=ax, ci_show=True, color=g.get("color", PALETTE["blue"]))
        kms.append((g["label"], km, g.get("color", PALETTE["blue"])))
    ax.set(xlabel="Time (months)", ylabel="Survival probability", ylim=(0,1))
    tbl = ax.inset_axes([0,-0.45,1,0.28]); tbl.axis("off")   # numbers-at-risk
    for i,(lab,km,col) in enumerate(kms):
        at_risk = [int(km.event_table.loc[km.event_table.index<=t,"at_risk"].iloc[-1])
                   if (km.event_table.index<=t).any() else 0 for t in times]
        tbl.text(-0.02, 1-0.25*i, lab, color=col, transform=tbl.transAxes, ha="right", fontsize=6)
        for t,n in zip(times, at_risk):
            tbl.text(t/max(times), 1-0.25*i, str(n), transform=tbl.transAxes, fontsize=6, ha="center")
```

## Decision-curve analysis
```python
def plot_dca(ax, thresholds, net_benefit_model, nb_all, nb_none=0):
    ax.plot(thresholds, net_benefit_model, color=PALETTE["blue"], label="Model")
    ax.plot(thresholds, nb_all, color=PALETTE["grey"], lw=0.8, label="Treat all")
    ax.axhline(nb_none, color="k", lw=0.8, label="Treat none")
    ax.set(xlabel="Threshold probability", ylabel="Net benefit")
    ax.legend(frameon=False)
```

Compute the statistics (AUC CIs, DeLong, calibration slope, net benefit) with
`radiology-stats`; this file is about rendering them correctly.
