# Break plan into tasks

Break a plan into ordered, implementable tasks — one concern per task, complete wiring, reviewable diffs.

**Input**

| Source | Description |
|--------|-------------|
| Doc | Path to a plan doc (e.g. from `/plan`) + optional phase filter |
| Inline | Pasted plan or brief goal description in chat |

Read referenced docs from the repo; treat as the source of truth.

**Rules**

- Ask at most 1 question if scope or ordering is unclear
- Read relevant source files to understand current state — identify symbols, call sites, and boundaries before splitting
- One concern per task — a task should answer one review question; never mix rename + wiring, removal + addition, or structural + mechanical changes
- Complete wiring — if a task adds, moves, renames, or changes a symbol's signature, it must update every in-scope call site in the same task
- Consumer inventory — each task lists the files/patterns it touches; no file appears in two tasks for the same symbol
- Order by dependency — later tasks may depend on earlier ones; never the reverse
- Bias small — prefer more smaller tasks over fewer large ones; a task should be 1 `/implement` invocation
- Horizontal tasks allowed — uniform mechanical changes across many files (e.g. add nil guard everywhere) may be one task when the concern is single
- Must not — produce source edits, commits, or implementation; include architecture decisions or design rationale beyond what the plan states
- Before replying: every task has concern + files + done-when; no task mixes concerns; ordering respects dependencies; output matches template

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Tasks | Happy with these tasks? (y/n) | Revise per feedback; re-ask |
| Persist | Save to `<path>`? (y/n) | End with chat output only |

**Output**

```
## Tasks — {goal}

### T01 — {title}
- Concern: {what this task does — one sentence}
- Files: {paths or glob patterns}
- Done when: {observable condition — tests green, no old pattern remains, etc.}

### T02 — {title}
- Concern: …
- Files: …
- Depends on: T01
- Done when: …

…

## Next
Happy with these tasks? (y/n)
```

- Number tasks sequentially (T01, T02, …)
- Include `Depends on:` only when a task requires a prior task's output
- Omit empty fields; keep each task 3–5 lines
- After approval, offer to persist under `docs/plans/` (or match repo layout)
- No preamble, summary wrap-up, or filler unless asked
