---
name: lld-design
description: >-
  Author a concise LLD for one phase (deliverables, contracts, tests) under
  docs/. Use when the task requires low-level design after HLD is approved.
disable-model-invocation: true
---

# LLD Design

Concise low-level design for one phase (deliverables, contracts, tests) under
`docs/`. No source edits, commits, or implementation.

## Input

Path to an architecture doc and phase number (and title if not obvious).

## Rules

- Read and inspect as needed — no source writes until approved
- LLD only — write and edit phase LLDs under `docs/`
- Phase-scoped — one phase per invocation; stay within that phase
- Short — bullets, actionable; implementation detail, not architecture
- Mirror a nearby LLD (`docs/**/design/**/lld/**` or repo norm)
- Match repo API names and reconcile patterns; state assumptions when info is missing
- Must not — source code edits, implementation, git mutations, architecture-only
  docs without deliverable detail, or work outside the named phase
- Sections — typical: Scope, Goals, Deliverables (ordered steps, key decisions,
  status/condition contracts with types/reasons/messages, resource
  naming/ownership/labels, tests for this phase)

## Interactive gates (when used in a session with a user)

| Step | Prompt | On rejection |
|------|--------|--------------|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |
| Create | Create this doc? (y/n) | Revise doc plan |
| LLD review | Happy with this LLD? (y/n) | Refactor; re-ask |

When used non-interactively, self-validate: doc plan has path under `docs/`;
scope limited to the named phase; LLD matches plan; assumptions stated.

## Output — doc plan

```
## Phase
<N> — <title> · source: docs/...

## Doc plan
- Path: docs/...
- Sections: <outline>

## Key decisions · Open questions
- ...
```

## Output — after create

```
## LLD saved
- Path: docs/...
- Phase: <N> — <title>

## Summary
<2–4 bullets: deliverables and contracts>
```
