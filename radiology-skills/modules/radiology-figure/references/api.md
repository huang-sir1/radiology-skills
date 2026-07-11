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

# Column widths (inches): _Radiology_-family single ~3.35 in (85 mm), double ~6.7 in (170 mm)
SINGLE, DOUBLE = 3.35, 6.7
# Nature-family single 89 mm / double 183 mm (see nature-figure-spec.md) — swap in for that venue:
SINGLE_NATURE, DOUBLE_NATURE = 89/25.4, 183/25.4

# Color-blind-safe (Okabe-Ito)
PALETTE = {"blue":"#0072B2","orange":"#E69F00","green":"#009E73","vermillion":"#D55E00",
           "skyblue":"#56B4E9","yellow":"#F0E442","purple":"#CC79A7","black":"#000000",
           "grey":"#999999"}

def save(fig, stem):
    fig.savefig(f"{stem}.svg")                 # primary, editable vector
    fig.savefig(f"{stem}.png", dpi=600)        # raster companion (or .tiff)

def panel_letter(i, case="upper"):
    """Single source of truth for panel labels — don't hardcode chr(65+i) per script.
    case="upper" -> A, B, C  (_Radiology_-family default, radiology-figure-guidelines.md)
    case="lower" -> a, b, c  (Nature-family default, nature-figure-spec.md)
    Always bold, top-left of the panel, in every figure of the same manuscript — pick ONE case
    for the whole figure set and pass it explicitly; never let it default silently per script.
    """
    letter = chr(97 + i) if case == "lower" else chr(65 + i)
    return letter

def add_panel_letter(ax, i, case="upper", **kwargs):
    style = dict(transform=ax.transAxes, fontsize=10, fontweight="bold", va="top", ha="left")
    style.update(kwargs)
    ax.text(0.02, 0.98, panel_letter(i, case), **style)
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

---

## House palettes (NPG / Morandi) + semantic roles

Use Okabe-Ito (above) when color-blind-safety is required. For a "Nature-journal" or soft house
look use one of these — but keep **one** palette for the whole paper and map color→meaning, not
color→figure (see `color-systems.md`).

```python
NPG = {"red":"#E64B35","blue":"#4DBBD5","green":"#00A087","navy":"#3C5488","orange":"#F39B7F",
       "slate":"#8491B4","teal":"#91D1C2","brightred":"#DC0000","brown":"#7E6148","tan":"#B09C85"}

MORANDI = {"low":"#6F9BB5","high":"#C56B5A","mid":"#D8B265","neutral":"#A2B189","grey":"#A7AAB0"}

# Map ROLES once, then reuse in every figure (example, Morandi):
C = {"Low":MORANDI["low"], "High":MORANDI["high"],                  # 2-group / risk endpoints
     "G1":MORANDI["low"], "G2":MORANDI["mid"], "G3":MORANDI["high"], # 3-level ordered ramp
     "clinical":MORANDI["low"], "augmented":MORANDI["high"],         # incremental-value comparison
     "neutral":MORANDI["neutral"]}
```
For **on-screen / teaching decks** bump the print ladder up (e.g. `font.size` 12-15, titles 16-18,
panel letters 20, `axes.linewidth` 1.6-1.8) and keep it uniform across the deck.

## Kaplan-Meier, publication-grade (numbers-at-risk + censor control + flat extension)

```python
import numpy as np
def km_estimate(t, e, tmax):
    """KM survival extended flat to last follow-up (<=tmax)."""
    t=np.asarray(t,float); e=np.asarray(e,int); tt=np.sort(np.unique(t[e==1]))
    S=1.; xs=[0.]; ys=[1.]
    for x in tt[tt<=tmax]:
        at=(t>=x).sum(); d=((t==x)&(e==1)).sum()
        S*= (1-d/at) if at>0 else 1; xs.append(x); ys.append(S)
    last=min(t.max(), tmax)                         # extend flat to last follow-up
    if last>xs[-1]: xs.append(last); ys.append(ys[-1])
    return np.array(xs), np.array(ys)

def km_panel(axK, axR, df, group_col, order, C, ticks=(0,1,2,3,4,5), max_ticks=14):
    """axK=curve axes, axR=numbers-at-risk axes (shared x). df has columns DMFS, evt, group_col."""
    t=df["DMFS"].values; e=df["evt"].values.astype(int); g=df[group_col].values; xmax=max(ticks)
    for grp in order:
        m=g==grp; xs,ys=km_estimate(t[m],e[m],xmax)
        axK.step(xs,ys,where="post",color=C[grp],lw=2.2,solid_capstyle="round",zorder=3)
        ct=t[(e==0)&m]; ct=ct[ct<=xmax]                          # censoring ticks (thinned, not deleted)
        if len(ct)>max_ticks:
            rng=np.random.default_rng(abs(hash((grp,group_col)))%2**32)
            ct=np.sort(rng.choice(ct,max_ticks,replace=False))
        for cx in ct:
            i=np.searchsorted(xs,cx,side="right")-1
            axK.plot([cx,cx],[ys[i]-0.013,ys[i]+0.013],color=C[grp],lw=1.1,zorder=4)
    axK.set(xlim=(0,xmax), ylim=(0.5,1.004)); axK.set_xticks(ticks); axK.tick_params(labelbottom=False)
    axR.set(xlim=(0,xmax), ylim=(-0.4,len(order)-0.3)); axR.set_xticks(ticks); axR.set_yticks([])
    for s in ("top","right","left"): axR.spines[s].set_visible(False)
    axR.annotate("Number at risk", xy=(0,1.02), xycoords="axes fraction", fontweight="bold")
    tr=axR.get_xaxis_transform()
    for i,grp in enumerate(order):
        yy=len(order)-1-i
        axR.text(-0.5, yy, grp, color=C[grp], fontweight="bold", ha="right", va="center", clip_on=False)
        for x in ticks:
            axR.text(x, yy, str(int((t[g==grp]>=x).sum())), color=C[grp], ha="center", va="center")
    # real, censoring-aware at-risk above. For a teaching no-tick figure swap to the
    # complete-follow-up convention:  N_group - cumulative events (see survival-figures.md)
```
Annotate each panel with log-rank P and HR (95% CI) vs a reference; if the reference group has
~0 events (unstable HR/CI), show per-group k-year survival % instead of an exploding HR.

## Time-dependent discrimination / calibration / utility (survival endpoints)

```python
def _km_censor(t,e):                                # KM of the censoring distribution G(t)
    return km_estimate(t, 1-np.asarray(e,int), float(np.max(t)))
def _Geval(xs,ys,q):
    idx=np.searchsorted(xs,np.asarray(q,float),side="right")-1; return ys[np.clip(idx,0,len(ys)-1)]

def td_auc(t,e,score,horizon):                      # IPCW cumulative/dynamic AUC at a horizon
    t=np.asarray(t,float); e=np.asarray(e,int); s=np.asarray(score,float)
    gx,gy=_km_censor(t,e); cases=(e==1)&(t<=horizon); ctrl=t>horizon
    if cases.sum()==0 or ctrl.sum()==0: return np.nan
    w=1/np.clip(_Geval(gx,gy,t[cases]),1e-6,None); sc=s[cases]; sd=s[ctrl]
    num=sum(wi*((sd<si).sum()+0.5*(sd==si).sum()) for si,wi in zip(sc,w))
    return num/(w.sum()*len(sd))

def breslow_S0(t,e,lp,grid):                        # baseline survival for a Cox linear predictor
    o=np.argsort(t); t,e,lp=t[o],e[o],lp[o]; eb=np.exp(lp); H=0.; xs=[0.]; H0=[0.]
    for x in np.unique(t[e==1]):
        risk=t>=x; d=((t==x)&(e==1)).sum(); denom=eb[risk].sum()
        H+= d/denom if denom>0 else 0; xs.append(x); H0.append(H)
    xs=np.array(xs); H0=np.array(H0); idx=np.searchsorted(xs,np.asarray(grid,float),side="right")-1
    return np.exp(-H0[np.clip(idx,0,len(H0)-1)])
# predicted risk at t:  1 - breslow_S0(...)**exp(lp_centered)
# survival calibration: bin predicted risk; plot mean predicted vs (1 - km_at(t)) per bin vs y=x
# survival DCA at t: nb(p) = (n_flag/N)*( ev - (1-ev)*p/(1-p) ), ev = 1 - KM_t within {risk>p};
#                    clip the y-axis to the decision band (treat-all dives steeply negative)
```
Statistics (AUC 95% CI by bootstrap, C-index, NRI/IDI, calibration slope) -> `radiology-stats`;
this file renders them. KM/ROC/calibration/DCA must use the **same** palette roles as the rest of
the figure set (`figure-set-consistency.md`).
