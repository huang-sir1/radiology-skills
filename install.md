# Installation

`radiology-skills` can be used as either a single all-in-one Codex skill or as a set of 22 independent `radiology-*` skills.

## Option A: Install the single entry skill

Windows PowerShell:

```powershell
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\radiology-skills "$env:USERPROFILE\.codex\skills\"
```

macOS or Linux:

```bash
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
mkdir -p ~/.codex/skills
cp -R radiology-skills ~/.codex/skills/
```

## Option B: Install the modular suite

Windows PowerShell:

```powershell
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\radiology-* "$env:USERPROFILE\.codex\skills\"
```

macOS or Linux:

```bash
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
mkdir -p ~/.codex/skills
cp -R skills/radiology-* ~/.codex/skills/
```

Restart Codex or reload skills after copying.

## Optional dependencies

Some modules can work better with additional tools:

- `radiology-search` and `radiology-citation`: web search or an academic-search MCP for PubMed, Crossref, arXiv, DOI, and PMID verification.
- `radiology-figure` and `radiology-stats`: Python packages such as `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`, `statsmodels`, and `lifelines`.
- `radiology-paper2ppt`: Python PPTX tooling when a real `.pptx` deck is requested.

These dependencies are optional for the instruction layer. The skill should not invent PMIDs, DOIs, metrics, p-values, accession numbers, or performance results when tooling or source data are unavailable.
