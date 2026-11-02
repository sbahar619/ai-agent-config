# Implement only

Implement only — source code changes for one scoped task. No commits, push, amend, or PRs.

**Input**

| Source | Description |
|--------|-------------|
| Doc    | Path to a design or plan doc + optional phase number(s) or title |
| Direct | Concrete task — fix, small feature, localized change |

Read referenced docs from the repo; treat as the spec.

**Rules**

- Ask at most one clarifying question if scope is unclear; otherwise state your assumption and proceed
- Implementation context — read the selected task, linked design sections, matching implementation companion, and referenced shared constraints in `implementation/README.md`. Resolve task links across sibling `tasks/` and `implementation/` folders, preserving legacy layouts; `implementation/history.md` is archival. Load only relevant sections; companions are optional when the supplied spec is sufficient. Archived instructions are historical evidence, not current work.
- Document conflicts — stop and surface conflicts between task criteria, design contracts, and implementation notes; notes must not silently override agreed behavior or reopen historical work
- Scoped work — only what the doc or task specifies, plus environment repairs needed to implement or validate it; stop and explain if the spec is insufficient
- Explain the purpose — opening update and completion lead with the concrete problem and intended or achieved behavior in plain language; task IDs, symbols, and file lists are supporting detail. Use a brief before/after example when it makes the change clearer.
- Report only achieved benefits — distinguish this task's result from benefits requiring later work; name the remaining dependency when needed to understand the result. Do not imply a defect existed or performance improved without evidence.
- Progress updates — report meaningful findings, blockers, or changed scope briefly; omit routine edit-by-edit narration
- Follow applicable user/project rules (coding and test standards) and language/ecosystem conventions for files you will touch
- Product documentation — write source comments and user-facing guidance in terms of behavior, contracts, and rationale; keep internal delivery-phase/task IDs and planning-document references in planning artifacts, not product content
- Run lint/tests as you go; fix failures caused by your changes; stop and report unrelated product defects
- Environment issues — diagnose and fix setup, dependency, tooling, or configuration issues blocking implementation or validation; use the smallest necessary repair, rerun the blocked step, and continue. Respect permissions; report a blocker only when repair requires unavailable access, credentials, or a user decision, and continue independent work where possible. Include repairs and any remaining validation limits in completion output.
- Suggested branch — one kebab-case name in completion output only
- Must not — commit, push, amend, or open/update a PR; modify architecture or plan docs; work outside the stated spec except for necessary environment repairs
- Before replying: changed files match the spec; diff reviewed for coding-standards compliance (duplication, naming, locality); validation run and reported; the reader can tell why the change matters and what it delivers now; output matches the completion template

**Gates**

One gate only. Done gate always runs.

| Step | Prompt                           | n                        |
|------|----------------------------------|--------------------------|
| Done | Happy with implementation? (y/n) | Fix per feedback; re-ask |

**Output**

```
**<Implemented | Partially implemented | Blocked> — <task ID if supplied>: <plain-language outcome>**

<One or two sentences: what problem prompted the change, what happens now, and why that helps.>

- Remaining: <material limitation or benefit awaiting a named later task>
- Validation: <commands> → <pass | fail — exit code N>
- Suggested branch: `<kebab-case-name>`

Happy with implementation? (y/n)
```

- Aim for at most 120 words; preserve material failures, limitations, and requested detail
- Link the main changed code where it supports the explanation; omit exhaustive file inventories and symbol lists
- Omit Remaining when the scoped outcome is complete and no deferred benefit needs clarification; omit the task ID and its separator for direct requests
- Validation — group passing checks on one line; state failed, blocked, or unrun checks explicitly, with the relevant reason
- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections
