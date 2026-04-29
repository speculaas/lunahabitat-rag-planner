# Model Card

## Project

LunaHabitat Planner

## Status

Submission-ready draft for the AI110 Unit 8 final project.

## Base Project

This project extends **Module 2: PawPal+**, which originally modeled pet-care scheduling with structured tasks, prioritization, conflict detection, and explanation output.

## Current System Description

LunaHabitat Planner is a retrieval-augmented lunar habitat operations planner. It accepts a resource and task, retrieves relevant local guidance from a curated corpus, and then produces a schedule explanation with a citation or an uncertainty warning when no relevant guidance is found.

## AI Feature

The current AI feature is a lightweight **Retrieval-Augmented Generation (RAG)** pipeline.

Current workflow:

`user task request -> retrieve local mission guidance -> generate schedule explanation -> show citation or uncertainty warning`

This version uses keyword-based retrieval and template-based explanation generation instead of an LLM. Even so, retrieval is integrated into the application logic and changes the system's output.

## Intended Use

LunaHabitat Planner is intended as a course project that demonstrates grounded planning support for a fictional lunar habitat. It is not intended for real aerospace, medical, or safety-critical deployment.

## Known Limitations And Biases

- The retriever is keyword-based rather than semantic, so it may miss relevant guidance when wording differs.
- The explanation text is template-driven rather than generated from deeper reasoning.
- The local corpus is small and curated, so it reflects the assumptions and priorities chosen by the developer.
- The current domain model still uses inherited class names from PawPal+, which is workable but not ideal for long-term maintainability.
- The planner is a simplified scheduling system, not a real mission simulator or safety-certified planning tool.

## Risks And Misuse

- Users could overtrust the schedule because the citations make the system appear more authoritative than it really is.
- The small corpus could omit important safety conditions and create false confidence.
- A fictional operations planner could be misunderstood as real aerospace guidance if its limitations are not stated clearly.

To reduce misuse, the project:

- restricts grounding to a visible local corpus
- shows citations with each explanation
- shows an uncertainty warning when no supporting guidance is found
- states clearly in the README and model card that the system is a course demonstration

## Evaluation And Reliability

The repository includes:

- automated unit tests for scheduler behavior
- retrieval-focused tests for matched and unmatched guidance behavior
- `evaluate_planner.py`, a scenario-based evaluation script

Current evaluation result:

- `4/4` evaluation cases passed

The current evaluation checks:

- oxygen-related tasks retrieve `Oxygen Recycler Checks`
- construction tasks retrieve `Construction Zone Safety`
- emergency tasks retrieve `Emergency Response Protocol`
- unmatched tasks trigger `No matching guidance` and the uncertainty guardrail

## What Surprised Me During Testing

One surprising result during testing was how easily a simple keyword retriever can produce accidental matches if the token filtering is too loose. Early retrieval behavior matched unrelated policy text because of generic words rather than meaningful terms. Tightening the token handling made it clearer that even lightweight RAG systems need careful evaluation and guardrails.

## What This Project Taught Me About AI And Problem Solving

This project showed me that adding AI to an application is not only about calling a model. It also involves designing the corpus, deciding how retrieval changes behavior, exposing uncertainty clearly, and testing the system so the outputs are inspectable. I learned that a smaller, more transparent retrieval system can still be useful if it is honest about its limits.

## AI Collaboration Reflection

I used AI tools during planning, design, and writing.

One helpful AI contribution was suggesting a stronger final-project framing: instead of trying to force a generic space-construction idea into PawPal+, the project was reframed into **LunaHabitat Planner**, which preserved the original scheduling backbone while creating a clearer RAG use case around habitat operations.

One flawed AI contribution was that early suggestions risked making the project sound more advanced than it actually was, especially around the word "RAG." That forced me to refine the implementation and documentation so the current version is described honestly as a lightweight local RAG pipeline with keyword retrieval and template-based explanations.

That experience reinforced an important lesson: AI can help with ideation and structure, but its suggestions still need to be checked carefully for scope, accuracy, and truthful framing.

## What This Project Says About Me As An AI Engineer

This project shows that I care about building AI systems that are understandable, testable, and honest about uncertainty. I am interested not only in adding AI features, but also in making sure those features are grounded in evidence, evaluated with clear scenarios, and documented in a way that helps users understand both the value and the limitations of the system.
