# Generate branch name

Generate one recommended git branch name from the user's goal or current changes. Do not create or checkout a branch unless the user explicitly asks.

**Input**

| Priority | Source |
|----------|--------|
| 1 | User-stated goal, ticket, or task description |
| 2 | `git diff` / `git diff --staged` when the user wants a name from current work and no goal was given |

Optional: issue or ticket id (e.g. `LIN-123`, `#42`).

**Rules**

- If neither a goal nor a diff is available, ask for a one-line description of the work
- Infer primary intent and pick one Conventional Commit–aligned prefix: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`, `build`, `perf`, `revert`
- Slug: lowercase kebab-case; 2–5 words; outcome or area, not file or symbol names
- When a ticket id is given, prefix the slug: `<ticket>-<slug>` (keep ticket casing as provided)
- Must not — spaces, uppercase in the slug, trailing slash, or characters outside `[a-z0-9-/.]`
- Must not — create, checkout, rename, or delete branches unless the user explicitly asks
- Before replying: output is exactly one branch name in the template; no alternates or ranked list

**Output**

```
<type>/<slug>
```

- Output only the fenced code block — no text before or after
- Inside the block: exactly one line — `<type>/<slug>` or `<type>/<ticket>-<slug>` when a ticket was given
- Prefer the shortest name that still uniquely describes the work
