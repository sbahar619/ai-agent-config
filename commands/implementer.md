# Implement only

**Implement only** — source code changes for one scoped task. No commits, push,
amend, or PRs.

## Input

Ask only if scope is unclear.

| Source | User provides |
|--------|----------------|
| Design doc | Path to a persisted low-level design doc (preferred for phased work) |
| Plan doc | Path to a plan doc + phase number(s) or title |
| Direct | Concrete task — fix, small feature, localized change |

Read referenced docs from the repo; treat as the spec.

## Rules

- **Scoped work** — only what the doc or task specifies; stop and explain if the
  spec is insufficient
- Follow applicable **user/project rules** (coding and test standards) for files
  you will touch
- **Execution plan first** — ordered deliverables and files; no source writes until
  approved
- Run lint/tests as you go; report validation results
- **Suggested branch** — one kebab-case name in completion output only
- **Must not** — commit, push, amend, or open/update a PR; architecture or plan
  docs; work outside the stated spec

## Self-verify

Before each gate reply:

- Execution plan: scope matches spec; deliverables ordered; validation listed
- After implement: changed files match approved plan; validation run and reported
- Output matches the template for the current gate — no extra sections

## Gates

Skip when the user already approved that step or said implement / skip plan.

| Step | Prompt | `n` |
|------|--------|-----|
| Execution plan | Happy with this execution plan? (y/n) | Revise; stay here |
| Done | Happy with implementation? (y/n) | Fix per feedback; re-ask |

## Output

**Execution plan:**

```
## Scope
<one sentence · source: docs/... | direct task>

## Execution plan
1. <deliverable> — <files>
2. ...

## Validation
<commands>

## Next
Happy with this execution plan? (y/n)
```

**After implement:**

```
## Implementation complete
- Scope: <summary>
- Files: <paths>
- Validation: <commands + result>
- Suggested branch: `<kebab-case-name>`

## Next
Happy with implementation? (y/n)
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except **Scope** and **Execution plan** in the plan gate
