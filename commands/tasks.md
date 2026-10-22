# Break plan into tasks

Break a plan into ordered, implementable tasks — one concern per task, complete wiring, reviewable diffs.

**Input**

| Source | Description |
|--------|-------------|
| Doc | Path to a plan doc (e.g. from `/plan`) + optional domain and phase filter |
| Inline | Pasted plan or brief goal description in chat |

Read referenced docs from the repo; treat as the source of truth.

**Rules**

- Ask at most 1 question if scope or ordering is unclear; resolve questions requiring user input before requesting approval
- Read relevant source files to understand current state — identify symbols, call sites, and boundaries before splitting
- One concern per task — a task should answer one review question; never mix rename + wiring, removal + addition, or structural + mechanical changes
- Complete wiring — if a task adds, moves, renames, or changes a symbol's signature, it must update every in-scope call site in the same task
- Consumer inventory — each task lists the files/patterns it touches; no file appears in two tasks for the same symbol
- Order by dependency — later tasks may depend on earlier ones; never the reverse
- Bias small — prefer more smaller tasks over fewer large ones; a task should be 1 `/implement` invocation
- Horizontal tasks allowed — uniform mechanical changes across many files (e.g. add nil guard everywhere) may be one task when the concern is single
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Phase mapping — for a single phase, identify its delivery plan, number, and title; use that number for new `phase-N` folders, never an HLD rollout-stage label. Preserve existing folder names and record their mapping explicitly; resolve missing or conflicting mappings before the gate.
- Design-doc links — scan the selected scope for `hld.md`, `lld.md`, and `phase-*/lld.md`, plus topic-level architecture for domain work; for topic-wide work, include relevant domain design docs. For each task, link covering sections in `Docs:` (e.g. `[IB01 — Validation function](lld.md#ib01--validation-function)`); omit when none applies.
- Must not — produce source edits, commits, or implementation; introduce architecture or contract decisions, or repeat design rationale
- Design gaps — if a task needs an unresolved architecture or contract decision, report the gap and wait for its resolution; do not invent the decision in the task list or require a separate design document when the supplied scope is already sufficient
- Updates — revise only tasks affected by agreed scope or design changes; identify follow-up for another document in Next without editing that document.
- Documentation task — if the scope adds or changes user-visible behavior (API, CLI, config, UI), scan for project docs (README, API docs, CLI docs, guides, CLAUDE.md) and include a documentation task when updates are needed; omit when the change is purely internal
- Document state — approval or saving the task list does not complete its tasks; completion claims require implementation and validation evidence
- Before replying: every task has concern + files + done-when; no task mixes concerns; ordering respects dependencies; design-doc links point to real sections; a documentation task is present when user-visible behavior changes; output matches template

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Tasks | Happy with these tasks? (y/n) | Revise per feedback; re-ask |

**Output — chat (high-level summary)**

```
## Tasks — {goal}

**Delivery phase:** [{plan title}]({plan path}) — {number}: {title}

1. **{title}** — {one-line concern}
2. **{title}** — {one-line concern}
…

## Next
{follow-up for another document, only when needed}
Happy with these tasks? (y/n)
```

**Output — file (full detail, auto-saved on approval)**

```
**Purpose:** Break the agreed scope into ordered tasks with files, dependencies, and completion criteria; new architecture decisions and design rationale are outside this document's scope.

**Delivery phase:** [{plan title}]({relative plan path}) — {number}: {title}

## Tasks — {goal}

### T01 — {title}
- Concern: {what this task does — one sentence}
- Files: {paths or glob patterns}
- Docs: [{section name}]({relative path to doc}#{anchor})
- Done when: {observable condition — tests green, no old pattern remains, etc.}

### T02 — {title}
- Concern: …
- Files: …
- Docs: [{section name}]({relative path to doc}#{anchor})
- Depends on: T01
- Done when: …

…
```

- Include Delivery phase in chat and file only for a single selected phase; use the same mapping in both
- Chat shows the phase mapping when applicable, numbered titles, and one-line concerns; no file lists or done-when
- File includes full detail per task (concern, files, docs, depends on, done when)
- Number tasks sequentially (T01, T02, …)
- Include `Depends on:` only when a task requires a prior task's output
- Include `Docs:` only when a relevant design doc section exists; link rather than copy design detail; use relative path from the tasks file to the doc; multiple links allowed (comma-separated)
- Omit empty fields; keep each task 3–6 lines
- Persist — on approval, auto-save as `<scope-dir>/tasks.md`; when scoped to a single phase, save as `<scope-dir>/phase-N/tasks.md`, beneath the shared HLD
- No preamble, summary wrap-up, or filler unless asked
