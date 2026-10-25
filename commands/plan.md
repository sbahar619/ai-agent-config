# Plan only

Plan only — high-level phased plan. No source edits, commits, or implementation.

**Input**

User provides a goal, problem, or path to research or requirements.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed — investigate silently; no source writes until approval
- High level — own delivery outcomes, their order, and why each matters; architecture decisions, detailed contracts, tests, and task-level steps belong in design or task documents
- Updates — revise only affected content within the plan's scope; identify follow-up for another document in Next without editing that document.
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Requirements — read supplied requirements and `requirements.md` in the selected scope and its topic root when present; surface conflicts for resolution without rewriting requirements
- Coverage — map every in-scope requirement and research gap to a phase outcome using source links, requirement IDs, or brief labels for inline input; otherwise propose its deferral with a reason in Deferred. Research findings outside the agreed scope do not automatically become obligations.
- Small changes — a separate requirements file is optional; when absent, capture necessary obligations and constraints briefly in the plan's Requirements section
- References — include relevant existing research and requirements in the plan's References line, with requirement IDs where applicable; link sections instead of repeating them. Use relative paths from the saved plan and verify targets; omit absent sources without requiring new documents.
- Document state — keep assumptions separate from agreed outcomes; approval or saving the plan does not mean its phases are implemented or validated
- Short and concise — bullets over prose; skip empty sections
- Phased — prefer 2–4 phases; 1 when the change is already small; each phase delivers a useful, reviewable outcome after its prerequisites, without relying on a later phase to make that outcome work. Bundle tightly coupled work and separate unrelated concerns; each one line: title — usable outcome + why now.
- Phase identity — delivery phases are identified by this plan's path, phase number, and title; do not silently renumber phases referenced by other documents. Identify any required remapping in Next.
- Bias toward the smallest useful next step
- Open questions — use the question + recommendation format below; if any need user input, wait for answers before asking for approval
- Must not — implementation file paths, commands, config snippets, git/PR language, diagrams, or validation steps in the chat plan; document references are allowed
- Persist — on approval, auto-save as `<scope-dir>/plan.md`; saved file uses the same plan body shown in chat
- Render — output the plan as rendered markdown in chat; never wrap the plan in a code fence; chat plan body matches what is written to the file (gate prompts are chat-only)
- Before replying: plan matches the output template — no extra sections; each phase is one line; count is 1–4; strip anything implementer-shaped (implementation paths, commands, git/PR, config), retaining relevant document references

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Plan | Happy with this plan? (y/n) | List Goal + phases (number + name); user picks + comments; revise only those; re-ask |

**Output**

**Draft plan** — reproduce as rendered markdown (not a code block); plan body is identical to the persisted file:

```
**Purpose:** Define phased outcomes and why they matter; architecture, API contracts, and implementation details are outside this document's scope.

**References:** {links to relevant research and requirements sections; omit when none exist}

## Goal

{one sentence}

## Requirements

- {brief required outcome or constraint, only when needed and no separate requirements document exists}

## Plan

1. **{title}** — {usable outcome + why now}
2. ...

## Deferred

- {source gap or requirement reference} — {reason for proposed or previously agreed deferral}

## Open questions

1. {concrete unresolved question ending in ?}
   Recommendation: {proposed answer and brief rationale}

## Next

{follow-up for another document, only when needed}
{if questions need user input: request answers and stop; otherwise: Happy with this plan? (y/n)}
```

**After approval (auto-saved):**

## Plan saved

- Path: <resolved plan path>
- Phases: {count + titles}

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Goal and Plan
