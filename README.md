# RatioMetricsTreatmentEffects

Simulation studies of model-based vs. model-free treatment effects,
after Battey & Edgar (2026) "Treatment effect: a critique", with a
real-world ratio-metric (iROAS) geo-experiment case study.

## Structure

```
├── data/            # Raw and processed data (not versioned)
├── logic/           # Core business logic
│   ├── simulation_engine.py      # Generic Monte Carlo engine + model contract
│   ├── battey_edgar_models.py    # The paper's five worked examples (§4.3)
│   ├── iroas_models.py           # Geo-experiment iROAS case-study DGP
│   ├── likelihoods.py            # MLE / regression fit routines
│   └── treatment_effect_plots.py # Plot helpers for tidy results
├── notebooks/       # Tutorials (illustration only; logic lives in logic/)
│   ├── 01_treatment_effect_critique_tutorial.ipynb
│   └── 02_iroas_geo_experiment_case_study.ipynb
├── papers/          # Markdown conversions + summaries of source papers
├── src/             # Scripts and entrypoints
├── requirements.txt
└── CLAUDE.md        # AI assistant context
```

## Setup

### Virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

Start with the notebooks (in order):

1. **`notebooks/01_treatment_effect_critique_tutorial.ipynb`** — simulates
   the five examples of Battey & Edgar (2026), showing when the model-free
   average treatment effect (eq. 3.1) does and does not recover a stable
   model parameter.
2. **`notebooks/02_iroas_geo_experiment_case_study.ipynb`** — applies the
   same lens to iROAS (incremental revenue / incremental cost) in a
   budget-negativization geo experiment, comparing four estimators.

Minimal programmatic example:

```python
import numpy as np
from logic.simulation_engine import run_study
from logic.battey_edgar_models import (
    ExponentialAdditiveModel, GAMMA_POPULATIONS,
)

model = ExponentialAdditiveModel(GAMMA_POPULATIONS["near_zero"], delta=2.0)
df = run_study(model, n=500, n_reps=300, seed=7)
print(df.groupby("estimator")["estimate"].describe())
```

New data-generating processes plug in by subclassing
`logic.simulation_engine.PotentialOutcomeModel` (implement `draw`,
`estimators`, and optionally `analytic_tau` / `reference_values`); the
engine, plotting helpers, and notebook patterns need no changes.

### Initialize Claude Code

```powershell
C:\Users\Sebastian\.local\bin\claude
```

Run this from the project root. Claude will pick up `CLAUDE.md` automatically for project context.
