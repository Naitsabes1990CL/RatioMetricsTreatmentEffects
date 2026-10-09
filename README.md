# project-name

Short description of what this project does.

## Structure

```
├── data/            # Raw and processed data (not versioned)
├── logic/           # Core business logic
│   ├── data_io.py   # Load/save helpers
│   └── preprocessing.py
├── notebooks/       # Exploratory notebooks
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

### Initialize Claude Code

```powershell
C:\Users\Sebastian\.local\bin\claude
```

Run this from the project root. Claude will pick up `CLAUDE.md` automatically for project context.
