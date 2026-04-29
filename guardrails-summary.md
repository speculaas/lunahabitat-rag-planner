# Guardrails Summary

## Current Guardrails

LunaHabitat Planner currently uses lightweight guardrails around retrieval-backed scheduling.

### 1. Uncertainty Warning On Missing Guidance

If the retriever finds no matching local guidance for a task, the planner does not pretend the result is grounded. Instead it:

- sets the citation to `No matching guidance`
- adds a warning that the item should be reviewed manually
- makes the explanation explicitly say that no matching guidance was retrieved

### 2. Local-Corpus Grounding

The current planner only cites guidance that exists in the local corpus under `data/docs/`. This limits unsupported claims and keeps the behavior inspectable.

### 3. Citation Visibility

The app and CLI both display the citation associated with each scheduled item. That makes it easier to inspect why a task was justified.

## Current Limitations

- The retriever is keyword-based, not semantic.
- The planner uses retrieved guidance to support explanations, but it does not yet rewrite priorities or block unsafe tasks automatically.
- The system does not yet log evaluation runs to a file.

## Evaluation Support

The repository includes `evaluate_planner.py`, which checks whether:

- known task types retrieve the expected corpus document
- unknown tasks trigger the uncertainty guardrail

## Good Final-Project Framing

In the final README and presentation, describe the current system honestly as:

- a lightweight local RAG pipeline
- grounded in a curated document corpus
- using uncertainty warnings when no evidence is found
