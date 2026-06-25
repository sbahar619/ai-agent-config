# Verify only

**Verify only** — skeptical validation with evidence; Pass or Fail. No edits,
commits, or implementation.

## Input

Ask only if scope is unclear.

| Source | User provides |
|--------|----------------|
| Session | Claimed-complete work in the current chat — goal, deliverables, validation |
| Spec doc | Path to a plan, design, or task description |
| Diff | Staged/uncommitted changes or named paths |

Derive what was claimed complete and success criteria from the source above,
referenced docs, and the repo.

## Rules

- Read and inspect as needed — no writes, no git mutations
- **Skeptical** — require evidence from commands and files; do not trust
  completion claims or prior validation summaries
- Follow applicable **user/project rules** when choosing lint and tests
- **Pass** only when success criteria are met, checks succeeded, and no
  blocking gaps or rule violations remain
- **Must not** — file edits, fixes, commits, or implementation

## Self-verify

Before replying:

- Success criteria derived from user input and spec — not assumed
- Every Passed/Failed/Rules item has evidence from files or command output
- Verdict matches findings — Fail when any blocking gap remains
- Output matches the template — no extra sections

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

- No preamble, summary wrap-up, or filler unless asked
- Omit empty list items; use "None" only where the template shows it
