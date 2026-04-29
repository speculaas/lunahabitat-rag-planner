# Project Testing Guide

This note describes how to test the current LunaHabitat Planner project.

## 1. Set Up The Environment

From the project root:

```bash
cd /Users/watney/git/zimmnotes/chat/codepath/ai110/w8/lunahabitat-rag-planner
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run The Unit Tests

Run the full test suite:

```bash
python3 -m pytest
```

Run the scheduler and retrieval tests with verbose output:

```bash
python3 -m pytest tests/test_pawpal.py -v
```

## 3. Run The Scenario Evaluation

Run the evaluation script:

```bash
python3 evaluate_planner.py
```

Expected current result:

```text
Summary: 4/4 cases passed
```

This checks:

- oxygen tasks retrieve `Oxygen Recycler Checks`
- construction tasks retrieve `Construction Zone Safety`
- emergency tasks retrieve `Emergency Response Protocol`
- unmatched tasks trigger `No matching guidance` and an uncertainty warning

## 4. Run The CLI Demo

```bash
python3 main.py
```

Look for:

- a mission schedule printed to the terminal
- a citation shown for each task
- warnings shown only when appropriate

## 5. Run The Streamlit App

```bash
streamlit run app.py
```

Then test these manual scenarios:

### Scenario A: Matching guidance

- use resource `Oxygen Recycler`
- use task `Oxygen recycler diagnostics`
- click `Generate schedule`

Expected behavior:

- the schedule item includes citation `Oxygen Recycler Checks`
- no uncertainty warning is shown

### Scenario B: Another matching guidance case

- add a resource like `Habitat Shell`
- add task `Expansion scaffold inspection`
- click `Generate schedule`

Expected behavior:

- the schedule item includes citation `Construction Zone Safety`

### Scenario C: Missing guidance

- add a resource like `Art Bay`
- add task `Art mural touch-up`
- click `Generate schedule`

Expected behavior:

- citation is `No matching guidance`
- uncertainty warning is shown

## 6. What To Record For The README Or Loom

Capture at least:

- one example with a matching citation
- one example with a different matching citation
- one example that triggers the uncertainty guardrail
- the `4/4` result from `evaluate_planner.py`
