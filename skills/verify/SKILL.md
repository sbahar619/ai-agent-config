---
name: verify
description: >-
  Skeptical Pass/Fail validation of claimed-complete work against evidence.
  Use when the task requires verifying that work meets its spec or success
  criteria.
disable-model-invocation: true
---

# Verify

Skeptical validation with evidence; Pass or Fail. No edits, commits, or
implementation.

## Input

| Source | Description |
|--------|-------------|
| Session | Claimed-complete work — goal, deliverables, validation |
| Spec doc | Path to a plan, design, or task description |
| Diff | Staged/uncommitted changes or named paths |

Derive what was claimed complete and success criteria from the source,
referenced docs, and the repo.

## Rules

- Read and inspect as needed — no writes, no git mutations
- Skeptical — require evidence from commands and files; do not trust completion
  claims or prior validation summaries
- Follow applicable project rules when choosing lint and tests
- Pass only when success criteria are met, checks succeeded, and no blocking
  gaps or rule violations remain
- Must not — file edits, fixes, commits, or implementation
- Before replying: success criteria derived from input and spec — not assumed;
  every item has evidence; verdict matches findings

## Output

```
## Scope
<one sentence · source: session | docs/... | diff>

## Success criteria
- ...

## Passed
- <check> — <evidence>

## Failed
- <issue> — <expected vs observed> (or "None")

## Rules
- <passed or violation> — <evidence> (or "None")

## Verdict
**Pass** | **Fail** — <one-line summary>
```

- Omit empty list items; use "None" only where the template shows it
