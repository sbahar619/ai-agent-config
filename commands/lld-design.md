# LLD only

LLD only — concise low-level design (deliverables, contracts, tests) for a topic, domain, or selected phase. No source edits, commits, or implementation.

**Input**

Path to an architecture doc and optional delivery-phase selection (plan path, number, and title when known).

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read the supplied architecture and applicable topic/domain HLDs; surface conflicts instead of overriding shared decisions. Inspect further as needed; no source writes until approval.
- LLD only — write and edit LLDs after approval
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Scope — covers all phases of the selected topic or domain by default (`<scope-dir>/lld.md`); for an explicitly selected phase, use `<scope-dir>/phase-N/lld.md`, with the shared HLD above phase folders
- Phase mapping — for a single phase, identify its delivery plan, number, and title; use that number for new `phase-N` folders, never an HLD rollout-stage label. Preserve existing folder names and record their mapping explicitly; resolve missing or conflicting mappings before the gate.
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only affected content within the selected scope. Identify follow-up for another document in Next without editing that document.
- Short — bullets, actionable; own detailed contracts, technical deliverables, and tests within the architecture; surface unresolved architecture decisions instead of settling them here
- Requirements — read supplied requirements and `requirements.md` in the selected scope and its topic root when present; link deliverables and acceptance criteria to relevant requirement IDs, and surface conflicts for resolution without redefining requirements. A separate requirements file is not mandatory.
- References — include an Architecture line in the saved LLD linking the source HLD sections, including applicable topic/domain architecture; retain relevant requirement links. Use relative paths and verify targets instead of copying content; do not create missing parent documents.
- Document state — approval or saving the LLD does not establish implementation or passing tests
- Work status — distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Open questions — use the question + recommendation format below; keep decisions and assumptions separate; if any need user input, wait for answers before asking for approval
- Match repo API names and reconcile patterns; state assumptions when info is missing
- Before proposing a new function or type, check the repo for existing symbols **and** the framework/library API (cobra/pflag, gin, client-go, etc.) for built-in equivalents; prefer using what exists over reimplementing — per coding-standards; cite what was checked
- Must not — source code edits, implementation, git mutations, architecture-only docs (components and flows without deliverable detail), or work outside the stated scope
- Authoring — typical sections: Scope, Goals, Deliverables (technical behavior and choices within the architecture, status/condition contracts with types/reasons/messages, resource naming/ownership/labels when relevant, tests); task IDs, per-task file inventories, task ordering, and completion tracking belong in tasks
- Document header — begin the saved LLD with: `**Purpose:** Specify implementable deliverables, contracts, and tests within the stated scope; revisiting the architecture or implementing source code is outside this document's scope.`
- Phase header — for a single phase, follow Purpose with `**Delivery phase:** [<plan title>](<relative plan path>) — <number>: <title>` in the saved LLD
- Before each gate reply: doc plan has a concrete path matching the selected scope; after approval, LLD matches approved doc plan; assumptions stated where info is missing; output matches the template — no extra sections

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |

**Output**

**Doc plan:**

```
## Phase
<linked delivery plan — phase number and title, or all phases of the selected topic/domain>
Architecture: <links to source architecture sections>

## Doc plan
- Path: <resolved LLD path>
- Sections: <outline>

## Key decisions
1. <settled decision and rationale>

## Assumptions
- <unverified assumption>

## Open questions
1. <concrete unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>

## Next
{follow-up for another document, only when needed}
{if questions need user input: request answers and stop; otherwise: Happy with this doc plan? (y/n)}
```

**After approval (auto-created and saved):**

```
## LLD saved
- Path: <resolved LLD path>
- Phase: <linked delivery plan — phase number and title, or all phases of the selected topic/domain>

## Summary
<2–4 bullets: deliverables and contracts>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Phase in doc plan
