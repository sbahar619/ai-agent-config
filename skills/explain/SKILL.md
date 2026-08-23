---
name: explain
description: >-
  Short explanation of code, flow, or concept with optional trace and example.
  Use when the task requires understanding a symbol, error, flow, or concept
  before proceeding.
disable-model-invocation: true
---

# Explain

Read-only short explanation — no edits, commits, or implementation.

## Input

Path, symbol, error, selection, or concept to explain.

## Rules

- Read and inspect as needed — no writes, no git mutations
- Concise — half a screen or less; bullets over prose
- Cite repo code with `path:line` when referencing it; say when guessing
- Include a Trace only when a walkthrough clarifies (multi-step flow, call chain,
  pipeline, state machine, async job, error path) — omit for simple targets
- Trace: high level, 5–10 numbered steps max — entry → key steps → outcome;
  real symbols/paths, not line-by-line narration
- Include an Example when a concrete illustration clarifies — omit when obvious
- Do not recommend next steps unless asked
- Before replying: re-read every cited `path:line` — symbols, behavior, and flow
  match; spot-check entry and at least one middle step; fix output if a check fails

## Output

```
Objective: <one sentence — what it does and why it exists>

How:
- <core mechanism>
- ... (2–4 bullets)

Trace:
1. <entry>
2. <key step>
...
(omit when not useful)

Example:
- <concrete illustration — sample call, request, config, or values>
(omit when not useful)

Touches:
- <entry points, key files, dependencies — omit when obvious>
```

- Omit empty sections except Objective
