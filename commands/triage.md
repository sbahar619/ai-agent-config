# Triage plan

Triage a plan doc — assess complexity per phase and recommend the workflow path for each. Read-only; no edits, commits, or implementation.

**Input**

Path to a plan doc (e.g. from `/plan`).

**Rules**

- Discovery — read the plan and resolve its topic/domain scope from its path and references. Recursively inventory that directory for `requirements.md`, `plan.md`, `hld.md`, `lld.md`, and `tasks*.md`, including nested domains and phases; also inspect applicable ancestor documents up to the topic root and explicitly linked sources.
- Artifact matching — read candidates whose stated scope and phase mapping cover the assessed work; do not select by basename or folder number alone. Report ambiguous ownership or incomplete discovery under Existing artifacts and recommend resolving it before creating potentially duplicate documents.
- Classify each plan phase independently using these signals:
  - **Light** — single concern, no new types/APIs/contracts, test-only or mechanical change, ≤ 1 file cluster
  - **Medium** — multiple files but well-scoped, clear boundaries, no new external contracts, 2–3 concerns
  - **Heavy** — new APIs/types/contracts, cross-component coordination, open questions or blockers, needs design decisions not yet captured
- Workflow selection — HLDs resolve architecture decisions, LLDs specify contracts and tests, and task lists split execution. Reuse existing coverage across all task batches; recommend a document only when it resolves an identified gap. Sufficient supplied context can go directly to implementation regardless of complexity; do not require a complete document chain.
- Phase mapping — match phase folders to the delivery plan by explicit plan link, phase number, and title; report missing or conflicting mappings under Existing artifacts and recommend resolving them before phase-specific work. Do not equate HLD rollout stages or folder numbers alone with delivery phases.
- Document state — an existing or approved document does not establish implemented work or passing tests; require evidence before treating a delivery phase as complete
- Work status — distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Read-only — no file writes, git mutations, or implementation
- Must not — change the plan, produce implementation detail, or skip phases without justification
- Before replying: every phase has a classification with at least one signal cited; each recommended document addresses a concrete gap; existing artifacts noted; output matches the template

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

### Recommended next step
{what to run next, on which phase, and the exact existing document path to reuse; propose a new path only for uncovered work, preserving the discovered hierarchy}
```

- Workflow paths are per-phase — adjacent phases with the same path may be grouped (e.g. "phases 1–2: medium")
- No preamble, summary, or filler unless asked
- Omit empty sections except the table and next step
