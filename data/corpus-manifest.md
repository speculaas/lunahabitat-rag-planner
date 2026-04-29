# Corpus Manifest

This file summarizes the intent of the local RAG corpus and how each document should function in retrieval.

## Corpus Strategy

The first version of the corpus is a **small curated local guidance set** rather than a large source archive.

This is intentional because it:

- keeps retrieval behavior easy to explain
- makes testing simpler
- helps the project stay within scope
- supports cleaner demos in the final presentation

## Topic Priority

### Highest-value topics for retrieval

1. `emergency-response-protocol`
2. `oxygen-recycler-checks`
3. `crew-time-budget-policy`

These are the most naturally procedural and most likely to produce useful retrieval-backed planning behavior.

### Supporting topics

4. `construction-zone-safety`
5. `lunar-comms-windows`

These are still important, but `lunar-comms-windows` may eventually work best as a mix of RAG and structured scheduling data rather than text-only retrieval.

## Manifest Entries

### `construction-zone-safety.md`

- `topic`: construction-zone-safety
- `document_type`: local guidance
- `system`: construction
- `hazards`: dust, vibration, shielding continuity, work-zone conflicts
- `best use`: construction prerequisites and blocking warnings

### `oxygen-recycler-checks.md`

- `topic`: oxygen-recycler-checks
- `document_type`: local guidance
- `system`: life support
- `hazards`: oxygen purity, seal integrity, degraded filtration
- `best use`: priority boosts and safety-first scheduling

### `lunar-comms-windows.md`

- `topic`: lunar-comms-windows
- `document_type`: local guidance
- `system`: communications
- `hazards`: noisy overlap, missing dedicated uplink time
- `best use`: communications scheduling rules and conflict warnings

### `crew-time-budget-policy.md`

- `topic`: crew-time-budget-policy
- `document_type`: local guidance
- `system`: crew operations
- `hazards`: overloaded schedules, displaced critical work
- `best use`: deciding what fits into the daily plan

### `emergency-response-protocol.md`

- `topic`: emergency-response-protocol
- `document_type`: local guidance
- `system`: emergency operations
- `hazards`: pressure loss, contamination, structural instability, comms outage
- `best use`: emergency reprioritization and unsafe-plan detection

## Suggested Future Metadata Schema

If the retriever becomes more advanced later, a useful chunk schema would include:

```json
{
  "topic": "emergency-response-protocol",
  "doc_type": "local_guidance",
  "system": "emergency_ops",
  "mission_phase": "surface_ops",
  "hazard": "pressure_loss",
  "priority_hint": "high",
  "citation_label": "Emergency Response Protocol"
}
```

## Submission Guidance

This manifest is suitable to keep in the final repo because it documents the design of the local corpus. It should not claim that the corpus is an official mission document set. The final README should describe the corpus honestly as curated project material.
