---
name: implement
description: >-
  Implement one scoped task from a doc or direct ask. Lint and test as you go.
  Use when the task requires source code changes for a defined scope.
disable-model-invocation: true
---

# Implement

Source code changes for one scoped task. No commits, push, amend, or PRs.

## Input

| Source | Description |
|--------|-------------|
| Doc | Path to a design or plan doc + optional phase number(s) or title |
| Direct | Concrete task — fix, small feature, localized change |

Read referenced docs from the repo; treat as the spec.

## Rules

- Ask at most one clarifying question if scope is unclear; otherwise state
  assumption and proceed
- Scoped work — only what the doc or task specifies; stop and explain if the
  spec is insufficient
- Follow applicable project rules (coding and test standards) for files touched
- Run lint/tests as you go; fix failures caused by your changes; stop and report
  unrelated failures
- Must not — commit, push, amend, or open/update a PR; modify architecture or
  plan docs; work outside the stated spec

## Interactive gate (when used in a session with a user)

| Step | Prompt | On rejection |
|------|--------|--------------|
| Done | Happy with implementation? (y/n) | Fix per feedback; re-ask |

When used non-interactively, self-validate: changed files match the spec;
validation run and passing.

## Output

```
## Implementation complete
- Scope: <summary>
- Files: <paths>
- Validation: <commands> → <pass | fail — exit code N>
- Suggested branch: `<kebab-case-name>`
```
