# LunaHabitat Planner

LunaHabitat Planner is a Streamlit mission-operations planner for a lunar habitat. It helps an operator manage habitat tasks, sort them into a daily schedule, and explain why those tasks were chosen under limited crew time.

This repository extends **Module 2: PawPal+**. The original project focused on pet-care scheduling with structured tasks, prioritization, conflict detection, and explanations. This final project keeps that scheduler backbone and reframes it around lunar habitat operations as the foundation for later RAG integration.

## Commit 1 Scope

This first reframe commit focuses on:

- renaming the project around lunar habitat operations
- updating user-facing app language
- keeping the existing scheduling backbone intact
- adding professional project scaffolding for `assets/`, `data/docs/`, and `model_card.md`

RAG retrieval is not implemented yet in this commit.

## Current Features

- Add mission resources and operations tasks from the Streamlit app
- Store habitat operator, resource, and task data in backend Python classes
- Generate a daily plan based on time budget, task time, and priority
- Sort tasks chronologically and filter out completed work
- Detect same-time conflicts and show warnings in the UI
- Create the next occurrence automatically for daily and weekly recurring tasks
- Run a CLI demo through `main.py` to verify the logic outside Streamlit

## System Design

The project currently uses the original four scheduling classes:

- `Owner`: stores the operator's name, available time budget, preferences, and tracked resources
- `Pet`: currently reused as a generic tracked resource record for modules, systems, or work zones
- `Task`: stores title, time, duration, priority, frequency, date, and completion state
- `Scheduler`: sorts tasks, builds plans, flags conflicts, and handles recurring tasks

This naming will likely be cleaned up in a later refactor, but it is sufficient for the first project-reframing commit.

## Lunar Habitat Task Categories

The app is now framed around these mission task categories:

- maintenance
- expansion
- monitoring
- communications

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

To preview the backend in the terminal:

```bash
python main.py
```

## Testing

Run the automated tests with:

```bash
python -m pytest
```

The current test suite still covers the inherited scheduler behavior:

- task completion
- task addition
- chronological sorting
- recurring task creation
- exact-time conflict detection

## Starter RAG Corpus

The repository now includes a starter local document corpus under `data/docs/` for future retrieval:

- `construction-zone-safety.md`
- `oxygen-recycler-checks.md`
- `lunar-comms-windows.md`
- `crew-time-budget-policy.md`
- `emergency-response-protocol.md`

These documents contain compact rules, warnings, and scheduling constraints that will be used in the next commit when retrieval is integrated into planning explanations.

## Planned Next Steps

1. Integrate retrieval into planning explanations
2. Add guardrails and evaluation for retrieval-based planning
3. Refine the domain model after the first RAG-backed workflow is working

## Project Structure

```text
assets/
data/
  docs/
tests/
app.py
main.py
pawpal_system.py
model_card.md
README.md
```

