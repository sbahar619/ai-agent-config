---
name: tasks
description: >-
  Break a plan into ordered implementable tasks with dependencies. Use when
  a plan needs to be decomposed into scoped implementation steps.
disable-model-invocation: true
---

# Tasks

Break a plan into ordered, implementable tasks — one concern per task, complete
wiring, reviewable diffs.

## Input

| Source | Description |
|--------|-------------|
| Doc | Path to a plan doc + optional phase filter |
| Inline | Pasted plan or brief goal description |

Read referenced docs from the repo; treat as source of truth.

## Rules

- Read relevant source files to understand current state before splitting
- One concern per task — a task should answer one review question; never mix
  rename + wiring, removal + addition, or structural + mechanical changes
- Complete wiring — if a task adds/moves/renames a symbol, it updates every
  in-scope call site in the same task
- Consumer inventory — each task lists files/patterns it touches; no file appears
  in two tasks for the same symbol
- Order by dependency — later tasks may depend on earlier ones; never the reverse
- Bias small — prefer more smaller tasks; a task should be 1 implement invocation
- Horizontal tasks allowed — uniform mechanical changes across many files may be
  one task when the concern is single
- Must not — produce source edits, commits, or implementation

## Interactive gates (when used in a session with a user)

| Step | Prompt | On rejection |
|------|--------|--------------|
| Tasks | Happy with these tasks? (y/n) | Revise per feedback; re-ask |
| Persist | Save to `<path>`? (y/n) | End with chat summary only |

When used non-interactively, produce tasks and persist under `docs/plans/tasks/`.

## Output — chat

```
## Tasks — <goal>

1. **<title>** — <one-line concern>
2. **<title>** — <one-line concern>
…
```

## Output — file (on persist)

```
## Tasks — <goal>

### T01 — <title>
- Concern: <what this task does — one sentence>
- Files: <paths or glob patterns>
- Done when: <observable condition>

### T02 — <title>
- Concern: …
- Files: …
- Depends on: T01
- Done when: …
```

- Chat shows only numbered titles + one-line concerns
- File includes full detail per task
- Include `Depends on:` only when a task requires a prior task's output
