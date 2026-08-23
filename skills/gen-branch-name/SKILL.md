---
name: gen-branch-name
description: >-
  Generate one Conventional Commit–style git branch name from a goal or diff.
  Use when the task needs a branch name before creating or checking out a branch.
disable-model-invocation: true
---

# Generate Branch Name

Generate one recommended git branch name. Do not create or checkout a branch
unless explicitly asked.

## Input

| Priority | Source |
|----------|--------|
| 1 | User-stated goal, ticket, or task description |
| 2 | `git diff` / `git diff --staged` when no goal was given |

Optional: issue or ticket id (e.g. `LIN-123`, `#42`).

## Rules

- If neither a goal nor a diff is available, ask for a one-line description
- Infer primary intent and pick one Conventional Commit–aligned prefix:
  `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`, `build`, `perf`, `revert`
- Slug: lowercase kebab-case; 2–5 words; outcome or area, not file or symbol names
- When a ticket id is given, prefix the slug: `<ticket>-<slug>` (keep ticket casing)
- Must not — spaces, uppercase in slug, trailing slash, or characters outside `[a-z0-9-/.]`
- Must not — create, checkout, rename, or delete branches unless explicitly asked
- Output is exactly one branch name — no alternates or ranked list

## Output

```
<type>/<slug>
```

- Exactly one line — `<type>/<slug>` or `<type>/<ticket>-<slug>` when a ticket was given
