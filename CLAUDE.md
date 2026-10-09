# CLAUDE.md

## Project Overview
<!-- Describe what this project does -->

## Architecture

```
├── data/                  # All data sources and flat files (CSV, JSON, parquet, etc.)
├── logic/                 # All Python modules and classes
│   ├── __init__.py
│   ├── data_io.py         # Load/save helpers
│   └── preprocessing.py   # Data preprocessing logic
├── notebooks/             # Illustration and exploratory notebooks
├── src/                   # Scripts and entrypoints
├── requirements.txt
├── CLAUDE.md
└── .gitignore
```

## Directory Rules

- **`logic/`** — All Python modules and classes live here. One responsibility per file. This is the only place where reusable code should be written or imported from.
- **`data/`** — All data sources and flat files (CSV, JSON, parquet, Excel, etc.). Never version-control raw data files; only `.gitkeep` is committed.
- **`notebooks/`** — Illustration and exploratory notebooks only. Notebooks must not define reusable logic — import from `logic/` instead.
- **`src/`** — Top-level scripts and entrypoints that orchestrate logic modules.

## Setup
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## Key Conventions
- All reusable code (classes, functions, utilities) belongs in `logic/`
- Notebooks are for illustration only; no business logic defined inside them
- All data files go in `data/`, never scattered across the project root
- Keep raw data out of version control

---

## Python Coding Standards

### PEP 8
Follow the [PEP 8](https://peps.python.org/pep-0008/) style guide:

- **Indentation:** 4 spaces per level. No tabs.
- **Line length:** Max 79 characters for code; 72 for docstrings/comments.
- **Blank lines:** Two blank lines between top-level functions/classes; one between methods inside a class; sparingly within functions.
- **Type hints:** Use PEP 484 type hints with built-in types (`dict`, `list`, `tuple`) instead of `typing.Dict`, `typing.List`, etc.

### File and Function Limits
- Files: max **500 lines**. Refactor into modules if approaching the limit.
- Functions: max **50 lines**, single clear responsibility.
- Classes: max **100 lines**, single concept or entity.
- Organize code into modules grouped by feature or responsibility.

---

## Style & Conventions

### Naming
| Construct | Convention |
|---|---|
| Variables & functions | `snake_case` |
| Classes | `PascalCase` |
| Constants | `UPPER_SNAKE_CASE` |
| Private attributes/methods | `_leading_underscore` |
| Type aliases | `PascalCase` |
| Enum values | `UPPER_SNAKE_CASE` |

### Docstrings
Use **Google-style docstrings** for all public functions, classes, and modules:

```python
def calculate_discount(
    price: Decimal,
    discount_percent: float,
    min_amount: Decimal = Decimal("0.01")
) -> Decimal:
    """
    Calculate the discounted price for a product.

    Args:
        price: Original price of the product
        discount_percent: Discount percentage (0-100)
        min_amount: Minimum allowed final price

    Returns:
        Final price after applying discount

    Raises:
        ValueError: If discount_percent is not between 0 and 100
        ValueError: If final price would be below min_amount

    Example:
        >>> calculate_discount(Decimal("100"), 20)
        Decimal('80.00')
    """
```

---

## Error Handling
- Always use specific exception handling. Never use bare `except:` or `except Exception:` unless re-raising.

---

## Documentation Standards
- Every module must have a docstring explaining its purpose.
- All public functions must have complete Google-style docstrings.
- Complex logic should use inline comments with a `# Reason:` prefix.
- Keep `README.md` updated with setup instructions and examples.

---

## Modelling Approach

Always prefer using an existing module from `logic/` before reaching for an
off-the-shelf implementation. When building any statistical or machine learning
model:

1. **Check `logic/` first** — if a module already implements the needed
   functionality, use or extend it.
2. **Extend before you replace** — if an existing module is close but not
   quite right, extend it rather than writing a parallel implementation.
3. **Only add a new module** when no existing logic covers the need.
4. **Library use** — always use libraries from `requirements.txt` directly.
   Only wrap them in a `logic/` module when there is a clear reason to do so
   (e.g. shared configuration, repeated boilerplate, or hiding complexity used
   in multiple places).
