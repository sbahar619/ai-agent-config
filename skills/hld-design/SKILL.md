---
name: hld-design
description: >-
  Author a concise HLD architecture doc (what/why, components, flows) under
  docs/. Use when the task requires high-level design before implementation.
disable-model-invocation: true
---

# HLD Design

Concise architecture doc (what/why, components, flows) under `docs/`. No source
edits, commits, or implementation.

## Input

A goal or path to a plan doc.

## Rules

- Read and inspect as needed — no source writes until approved
- HLD only — write and edit architecture docs under `docs/`
- Short — bullets, ~1 page; what/why, components, flows
- Mirror a nearby HLD (`docs/**/design/hld/**` or repo norm)
- Mermaid only when it clarifies; state assumptions when info is missing
- Stay within stated scope
- Must not — source code edits, implementation, git mutations, low-level
  deliverable detail (ordered steps, API contracts, per-phase tests)
- Sections — pick by relevance: Summary, Goals / Non-goals, Architecture;
  add when relevant: Data model / APIs, Workflow / Sequence, Rollout / phasing,
  Failure modes, Security, Observability

## Interactive gates (when used in a session with a user)

| Step | Prompt | On rejection |
|------|--------|--------------|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |
| Create | Create this doc? (y/n) | Revise doc plan |
| HLD review | Happy with this HLD? (y/n) | Refactor; re-ask |

When used non-interactively, self-validate each gate: doc plan has path under
`docs/`; sections justified; HLD matches approved plan; assumptions stated.

## Output — doc plan

```
## Goal
<one sentence>

## Doc plan
- Path: docs/...
- Include: <section> — <why>
- Skip: <section> — <why or N/A>

## Phasing
1. **<title>** — <what + why / dependency>
2. ...

## Key decisions · Open questions
- ...
```

## Output — after create

```
## HLD saved
- Path: docs/...
- Phases: <count + titles>

## Summary
<2–4 bullets: main decisions and scope>
```
