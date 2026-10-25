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
- Reviewability — make each task's outcome, dependencies, and completion criteria easy to scan; keep necessary execution detail in the task and link its design rationale. Remove repetition before proposing independently reviewable scopes; preserve required wiring and verification even when they need more space.
- Horizontal tasks allowed — uniform mechanical changes across many files (e.g. add nil guard everywhere) may be one task when the concern is single
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Discovery — before choosing a destination or splitting work, resolve the selected topic/domain/phase from the input and document references. Recursively inventory its directory for `requirements.md`, `plan.md`, `hld.md`, `lld.md`, and `tasks*.md`, including nested domains and phases; also inspect applicable ancestor documents up to the topic root and explicitly linked sources.
- Artifact matching — read candidates whose stated scope and phase mapping cover the requested work; do not select by basename or folder number alone. Resolve ambiguous ownership before approval; report incomplete discovery instead of treating uninspected documents as absent.
- Task batches — revise the matching batch rather than duplicate its tasks; use a separate batch only for distinct follow-up work
- Phase mapping — for a single phase, identify its delivery plan, number, and title; use that number for new `phase-N` folders, never an HLD rollout-stage label. Preserve existing folder names and record their mapping explicitly; resolve missing or conflicting mappings before the gate.
- Source links — in each task's `Docs:`, link the covering LLD sections discovered for its scope; use relevant HLD or plan sections when no LLD covers the task. Omit when none applies; do not require a missing document layer.
- Coverage — account for every required deliverable in the selected scope, including specified tests and integration work, through new tasks, existing coverage, or a proposed deferral with a reason. Use task concerns and `Docs:` links for new-task mappings; record existing task links or implementation evidence and deferrals in Coverage notes. Do not expand a selected batch to the whole phase or silently waive upstream requirements; resolve scope conflicts before approval.
- Must not — produce source edits, commits, or implementation; introduce architecture or contract decisions, or repeat design rationale
- Design gaps — if a task needs an unresolved architecture or contract decision, report the gap and wait for its resolution; do not invent the decision in the task list or require a separate design document when the supplied scope is already sufficient
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only tasks affected by agreed scope or design changes. Identify follow-up for another document in the chat overview without editing that document.
- Documentation task — if the scope adds or changes user-visible behavior (API, CLI, config, UI), scan for project docs (README, API docs, CLI docs, guides, CLAUDE.md) and include a documentation task when updates are needed; omit when the change is purely internal. User-facing content and source comments must explain behavior without internal delivery-phase/task IDs or planning-document references.
- Document state — approval or saving the task list does not complete its tasks; completion claims require implementation and validation evidence
- Work status — when reporting progress, distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Before replying: no task mixes concerns; ordering respects dependencies; source links point to real sections; documentation tasks cover needed updates for user-visible changes; output matches template

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Tasks | Happy with these tasks? (y/n) | Revise per feedback; re-ask |

**Output — chat**

```
**Draft:** [<task filename>](<resolved path>) — awaiting review
- <consequential outcome, dependency, or coverage exception>
```

- At most three short overview bullets; on revisions, use them for changed task IDs, obligations, dependencies, or open questions instead
- Request answers when user input is needed; otherwise show the Tasks gate
- Do not enumerate every task or repeat the full document in chat unless asked

**Output — file**

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

- Include Delivery phase only for a single selected phase
- Omit Coverage notes when all deliverables map to new tasks
- Task IDs — for new tasks, continue the existing ID scheme above the highest allocated ID across batches in the same directory (`T01`, `T02`, ... for a fresh list); never renumber existing tasks or reuse retired IDs
- Include `Depends on:` only when a task requires a prior task's output; for another batch, use a relative file-and-heading link, not a bare task ID, and verify the target exists
- Include `Docs:` only when a relevant source section exists; link rather than copy its contents; use relative paths from the tasks file and verify targets; multiple links allowed (comma-separated)
- Omit empty fields; aim for 3–6 lines per task, expanding when needed for complete criteria
- Draft for review — write the full task list before requesting content approval, marking it as awaiting review in chat. Use `<scope-dir>/` or, for a single phase, `<scope-dir>/phase-N/`; keep gate prompts and review commentary outside the file. For a fresh list use `tasks.md`; for a new batch use the next unused number above existing batches (`tasks-02.md`, `tasks-03.md`, ...), treating `tasks.md` as batch 1. Batch numbers are independent of phase numbers.
- No preamble, summary wrap-up, or filler unless asked

**After approval:**

```
## Tasks approved
- Path: <resolved task file path>
```
