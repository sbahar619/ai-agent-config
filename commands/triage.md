# Triage plan

Triage a plan doc — assess complexity per phase and recommend the workflow path for each. Read-only; no edits, commits, or implementation.

**Input**

Path to a plan doc (e.g. from `/plan`).

**Rules**

- Discovery — read the plan and resolve its topic/domain scope from its path and references. Recursively inventory that directory for `requirements.md`, `plan.md`, `hld.md`, `lld.md`, `tasks*.md`, `*-tasks.md`, `implementation*.md`, and `*-implementation.md`, including `tasks/` and all Markdown in `implementation/` (index, companions, and history), nested domains, and phases; also inspect applicable ancestor documents up to the topic root and explicitly linked sources.
- Artifact matching — read candidates whose stated scope and phase mapping cover the assessed work; do not select by basename or folder number alone. Report ambiguous ownership or incomplete discovery in the short conclusion and recommend resolving it before creating potentially duplicate documents.
- Classify each plan phase independently using these signals:
  - **Light** — single concern, no new types/APIs/contracts, test-only or mechanical change, ≤ 1 file cluster
  - **Medium** — multiple files but well-scoped, clear boundaries, no new external contracts, 2–3 concerns
  - **Heavy** — new APIs/types/contracts, cross-component coordination, open questions or blockers, needs design decisions not yet captured
- Workflow selection — HLDs resolve architecture decisions, LLDs specify contracts and tests, and task lists split execution. Implementation companions hold mechanics and detailed verification per task file; inspect linked shared notes and distinguish archived instructions from current guidance. Reuse existing coverage across all task batches; recommend a document only when it resolves an identified gap. Sufficient supplied context can go directly to implementation regardless of complexity; do not require a complete document chain.
- Phase mapping — match phase folders to the delivery plan by explicit plan link, phase number, and title; report missing or conflicting mappings in the short conclusion and recommend resolving them before phase-specific work. Do not equate HLD rollout stages or folder numbers alone with delivery phases.
- Document state — an existing or approved document does not establish implemented work or passing tests; require evidence before treating a delivery phase as complete
- Work status — distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Read-only — no file writes, git mutations, or implementation
- Must not — change the plan, produce implementation detail, or skip phases without justification
- Before replying: every phase was classified using evidence; each recommended document addresses a concrete gap; material discovery gaps are disclosed; output matches the template
- Assess all phases internally; lead with the next workflow step and surface any blocker that changes it. Show per-phase classifications and signals only when requested

**Output**

```text
<What the plan needs next, or the gap blocking that decision.>
<I recommend the next command and phase, linking the existing document to reuse.>

Want the phase-by-phase assessment?
```

- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- When requested, show a flat numbered list of phases with classification, a brief supporting signal, and matching artifact link; group adjacent phases only when their recommendations match
