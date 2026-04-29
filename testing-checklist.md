# Testing Checklist

## Pytest Commands

Create and activate a virtual environment if needed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the full test suite:

```bash
python3 -m pytest
```

Run only the scheduler tests:

```bash
python3 -m pytest tests/test_pawpal.py
```

Run tests with more detail:

```bash
python3 -m pytest -v
```

If `pytest` is missing, install it directly:

```bash
python3 -m pip install pytest
```

## Commit 1 Verification Checklist

- `README.md` reflects LunaHabitat Planner instead of PawPal+
- `app.py` shows lunar habitat operations language in the UI
- `main.py` uses lunar habitat demo data
- `model_card.md` exists
- `assets/` exists
- `data/docs/` exists
- tests pass after installing dependencies

## Suggested Next Checks

- run the Streamlit app and verify the new labels look correct
- confirm the seeded tasks match the lunar habitat theme
- make sure the repo still has a clean story before adding RAG docs
