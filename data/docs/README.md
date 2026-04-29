# Corpus README

This folder contains the starter local document corpus for **LunaHabitat Planner**.

The current corpus is intentionally small and curated. Its purpose is to support a class project demonstration of Retrieval-Augmented Generation (RAG) in a lunar habitat operations planner.

## Current Corpus Topics

- `construction-zone-safety.md`
- `oxygen-recycler-checks.md`
- `lunar-comms-windows.md`
- `crew-time-budget-policy.md`
- `emergency-response-protocol.md`

## What These Documents Are

These files are **local operational guidance documents** written in a realistic technical style for project use. They are meant to provide retrievable rules, warnings, constraints, and escalation conditions that can later influence scheduling behavior.

They are suitable for:

- retrieval demonstrations
- grounded scheduling explanations
- warning and guardrail behavior
- evaluation scenarios

## What These Documents Are Not

These files are not official NASA or mission-certified procedures.

For the final project README, it is best to describe them honestly as:

- a curated local corpus
- inspired by real habitat operations themes
- designed for a course demonstration of retrieval-backed planning

## Topic Intent

### `construction-zone-safety.md`

Supports construction and expansion planning by defining:

- prerequisites
- conflict conditions
- monitoring expectations
- escalation rules

### `oxygen-recycler-checks.md`

Supports life-support planning by defining:

- daily diagnostic checks
- priority rules
- warning conditions
- blocking conditions for unsafe expansion work

### `lunar-comms-windows.md`

Supports communications planning by defining:

- preferred comms timing
- conflict rules with noisy construction
- priority differences between emergency and routine uplinks

### `crew-time-budget-policy.md`

Supports schedule generation by defining:

- time-budget thresholds
- priority ordering
- when to include or defer lower-priority work

### `emergency-response-protocol.md`

Supports guardrails and emergency replanning by defining:

- trigger conditions
- emergency scheduling rules
- communications requirements
- recovery rules

## How To Use This Corpus

A simple first retrieval pipeline can:

1. load each markdown file
2. split by heading or paragraph blocks
3. score chunks by keyword overlap with the task or scenario
4. return the top matching chunks
5. use those chunks to justify schedule decisions and warnings

## Recommended Future Expansion

Later versions of the corpus can add:

- source-backed notes derived from NASA or scholarly references
- metadata per chunk such as topic, hazard, or document type
- structured data for communications windows or mission constraints

## Submission Guidance

This folder is suitable to include in the final submitted repository as long as the project documentation clearly states that it is a **curated local corpus for demonstration purposes**.
