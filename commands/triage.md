# Triage plan

Triage a plan doc — assess complexity per phase and recommend the workflow path for each. Read-only; no edits, commits, or implementation.

**Input**

Path to a plan doc (e.g. from `/plan`).

**Rules**

- Read the plan doc; scan the plan's topic directory (`docs/plans/<topic>/`) for sibling artifacts (`hld.md`, `lld.md`, `lld-phase-*.md`, `tasks.md`)
- Classify each plan phase independently using these signals:
  - **Light** — single concern, no new types/APIs/contracts, test-only or mechanical change, ≤ 1 file cluster
  - **Medium** — multiple files but well-scoped, clear boundaries, no new external contracts, 2–3 concerns
  - **Heavy** — new APIs/types/contracts, cross-component coordination, open questions or blockers, needs design decisions not yet captured
- Account for existing artifacts — if an HLD, LLD, or tasks file already covers a phase, factor that into the recommendation (skip what's done)
- Read-only — no file writes, git mutations, or implementation
- Must not — change the plan, produce implementation detail, or skip phases without justification
- Before replying: every phase has a classification with at least one signal cited; recommended path matches the classification; existing artifacts noted; output matches the template

**Output**

```
## Triage — {plan title}
Source: `{path}`

### Existing artifacts
- {path or "None found"}

### Per-phase assessment

| # | Phase | Complexity | Signals | Path |
|---|-------|------------|---------|------|
| 1 | {title} | Light / Medium / Heavy | {1–2 key signals} | {workflow} |
| 2 | … | … | … | … |

### Workflow legend
- **Light:** plan → implement
- **Medium:** plan → tasks → implement
- **Heavy:** plan → hld → lld → tasks → implement

### Recommended next step
{what to run next and on which phase — e.g. "/tasks docs/plans/foo/plan.md phase 1–2" or "/hld-design docs/plans/foo/plan.md phase 3"}
```

- Workflow paths are per-phase — adjacent phases with the same path may be grouped (e.g. "phases 1–2: medium")
- No preamble, summary, or filler unless asked
- Omit empty sections except the table and next step
