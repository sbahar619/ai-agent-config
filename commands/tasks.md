# Break plan into tasks

Break a plan into ordered, implementable tasks — one concern per task, complete wiring, reviewable diffs.

**Input**

| Source | Description |
|--------|-------------|
| Doc | Path to a plan or existing task file + optional domain and phase filter |
| Inline | Pasted plan or brief goal description in chat |

Read referenced docs from the repo; treat as the source of truth.

**Rules**

- Ask at most 1 question if scope or ordering is unclear; resolve questions requiring user input before requesting approval
- Read relevant source files to understand current state — identify symbols, call sites, and boundaries before splitting
- One concern per task — a task should answer one review question; keep the supporting edits needed for that outcome together, including caller updates for a rename, and separate unrelated cleanup
- Complete wiring — include all callers, registration, configuration, and integration needed for the task's stated behavior, plus appropriate tests; a task must not leave that behavior broken or unreachable until a later task. If required wiring falls outside the authorized scope, report the scope conflict before approval.
- Consumer inventory — each task lists the files/patterns it touches; within a batch, no file appears in two tasks for the same symbol
- Order by dependency — later tasks may depend on earlier ones; never the reverse
- Bias small — choose the smallest complete, reviewable change that fits one `/implement` invocation; split only where each task leaves a coherent, verifiable result after its declared dependencies
- Horizontal tasks allowed — uniform mechanical changes across many files (e.g. add nil guard everywhere) may be one task when the concern is single
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Task batches — read existing `tasks*.md` in the selected scope or phase directory before splitting work; revise the matching batch rather than duplicate its tasks. Use a separate batch only for distinct follow-up work.
- Phase mapping — for a single phase, identify its delivery plan, number, and title; use that number for new `phase-N` folders, never an HLD rollout-stage label. Preserve existing folder names and record their mapping explicitly; resolve missing or conflicting mappings before the gate.
- Source links — scan the selected scope for `hld.md`, `lld.md`, and `phase-*/lld.md`, plus topic-level architecture for domain work; for topic-wide work, include relevant domain design docs. In each task's `Docs:`, link the covering LLD sections; use relevant HLD or plan sections when no LLD covers the task. Omit when none applies; do not require a missing document layer.
- Coverage — account for every required deliverable in the selected scope, including specified tests and integration work, through new tasks, existing coverage, or a proposed deferral with a reason. Use task concerns and `Docs:` links for new-task mappings; record existing task links or implementation evidence and deferrals in Coverage notes. Do not expand a selected batch to the whole phase or silently waive upstream requirements; resolve scope conflicts before approval.
- Must not — produce source edits, commits, or implementation; introduce architecture or contract decisions, or repeat design rationale
- Design gaps — if a task needs an unresolved architecture or contract decision, report the gap and wait for its resolution; do not invent the decision in the task list or require a separate design document when the supplied scope is already sufficient
- Updates — revise only tasks affected by agreed scope or design changes; identify follow-up for another document in Next without editing that document.
- Documentation task — if the scope adds or changes user-visible behavior (API, CLI, config, UI), scan for project docs (README, API docs, CLI docs, guides, CLAUDE.md) and include a documentation task when updates are needed; omit when the change is purely internal
- Document state — approval or saving the task list does not complete its tasks; completion claims require implementation and validation evidence
- Work status — when reporting progress, distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Before replying: every task has concern + files + done-when; no task mixes concerns; ordering respects dependencies; source links point to real sections; a documentation task is present when user-visible behavior changes; output matches template

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Tasks | Happy with these tasks? (y/n) | Revise per feedback; re-ask |

**Output — chat (high-level summary)**

```
## Tasks — {goal}

Path: {resolved task file path}

**Delivery phase:** [{plan title}]({plan path}) — {number}: {title}

1. **{title}** — {one-line concern}
2. **{title}** — {one-line concern}
…

## Coverage notes
- {deliverable reference} — {existing coverage link or reason for proposed/approved deferral}

## Next
{follow-up for another document, only when needed}
Happy with these tasks? (y/n)
```

**Output — file (full detail, auto-saved on approval)**

```
**Purpose:** Break the agreed scope into ordered tasks with files, dependencies, and completion criteria; new architecture decisions and design rationale are outside this document's scope.

**Delivery phase:** [{plan title}]({relative plan path}) — {number}: {title}

## Tasks — {goal}

### {task ID} — {title}
- Concern: {what this task does — one sentence}
- Files: {paths or glob patterns}
- Docs: [{section name}]({relative path to doc}#{anchor})
- Done when: {observable outcome and relevant verification, including required wiring; not merely files or symbols added}

### {next task ID} — {title}
- Concern: …
- Files: …
- Docs: [{section name}]({relative path to doc}#{anchor})
- Depends on: {task ID, or relative link to a task in another file}
- Done when: …

…

## Coverage notes
- {deliverable reference} — {existing task link, implementation evidence, or reason for proposed/approved deferral}
```

- Include Delivery phase in chat and file only for a single selected phase; use the same mapping in both
- Chat shows the destination path, phase mapping when applicable, numbered titles, one-line concerns, and coverage notes; no implementation file lists or done-when
- File includes full detail per task (concern, files, docs, depends on, done when)
- Omit Coverage notes when all deliverables map to new tasks; otherwise keep the same existing-coverage and deferral notes in chat and file
- Task IDs — for new tasks, continue the existing ID scheme above the highest allocated ID across batches in the same directory (`T01`, `T02`, ... for a fresh list); never renumber existing tasks or reuse retired IDs
- Include `Depends on:` only when a task requires a prior task's output; for another batch, use a relative file-and-heading link, not a bare task ID, and verify the target exists
- Include `Docs:` only when a relevant source section exists; link rather than copy its contents; use relative paths from the tasks file and verify targets; multiple links allowed (comma-separated)
- Omit empty fields; keep each task 3–6 lines
- Persist — on approval, save to the displayed path in `<scope-dir>/` or, for a single phase, `<scope-dir>/phase-N/`. For a fresh list use `tasks.md`; for a new batch use the next unused number above existing batches (`tasks-02.md`, `tasks-03.md`, ...), treating `tasks.md` as batch 1. Batch numbers are independent of phase numbers.
- No preamble, summary wrap-up, or filler unless asked
