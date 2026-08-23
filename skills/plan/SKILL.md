---
name: plan
description: >-
  High-level phased plan (what/why, not how). Use when the task requires
  planning before design or implementation.
disable-model-invocation: true
---

# Plan

High-level phased plan. No source edits, commits, or implementation.

## Input

A goal or problem — feature, refactor, bug, CI failure, or improvement.

## Rules

- Read and inspect as needed — no source writes
- High level — what and why, not how; no architecture, APIs, or file-level detail
- Short and concise — bullets over prose; skip empty sections
- Phased — prefer 2–4 phases; 1 when the change is already small; each one line:
  title — what + why now
- Bias toward the smallest useful next step
- Must not — file paths, commands, config snippets, git/PR language, diagrams,
  or validation steps in the plan
- Persist — after approval, save under `docs/plans/` (or match repo layout)
- Before replying: each phase is one line; count is 1–4; strip anything
  implementer-shaped (paths, commands, git/PR, config)

## Interactive gates (when used in a session with a user)

| Step | Prompt | On rejection |
|------|--------|--------------|
| Plan | Happy with this plan? (y/n) | Revise per feedback; re-ask |
| Persist | Save to `<path>`? (y/n) | End with chat plan only |

When used non-interactively, produce the plan and persist under `docs/plans/`.

## Output

```
## Goal
<one sentence>

## Plan
1. **<title>** — <what + why now>
2. ...

## Blockers
<only if any — else omit>
```
