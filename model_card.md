# Model Card

## Project

LunaHabitat Planner

## Status

Draft for the AI110 Unit 8 final project.

## Base Project

This project extends **Module 2: PawPal+**, which originally modeled pet-care scheduling with structured tasks, prioritization, conflict detection, and explanation output.

## Current System Description

The current version is a reframed scheduler for lunar habitat operations. It supports entering habitat resources and operational tasks, then building a daily plan based on time and priority constraints.

## Planned AI Feature

The required AI feature for the final project will be **Retrieval-Augmented Generation (RAG)**.

The planned workflow is:

`user task request -> retrieve local mission guidance -> generate schedule explanation -> show warnings or uncertainty when context is weak`

## Intended Use

LunaHabitat Planner is intended as a course project that demonstrates grounded planning support for a fictional lunar habitat. It is not intended for real aerospace, medical, or safety-critical deployment.

## Known Limitations

- Retrieval has not been added yet in this draft.
- The current domain model still uses inherited class names from PawPal+.
- The planner is a simplified scheduling system, not an engineering simulator.

## Risks And Misuse

- Users could overtrust generated schedules if the system appears more authoritative than it is.
- A small local corpus could omit important safety context.
- Fictional mission guidance may look realistic without being complete.

## Evaluation Plan

Later commits should add:

- retrieval relevance checks
- guardrail tests for missing guidance
- example scenarios covering maintenance, expansion, monitoring, and communications

## AI Collaboration Notes

This file will be expanded later with reflection on how AI tools helped and where they were imperfect during development.
