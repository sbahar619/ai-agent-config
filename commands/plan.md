# Plan only

Plan only — high-level phased plan. No source edits, commits, or implementation.

**Input**

User provides a goal, problem, or path to research or requirements.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed — investigate silently; no source writes until approval
- High level — own delivery outcomes, their order, and why each matters; architecture decisions, detailed contracts, tests, and task-level steps belong in design or task documents
- Updates — revise only affected content within the plan's scope; identify follow-up for another document in Next without editing that document.
- Requirements — when supplied or present in the topic directory, read `requirements.md`; map phases to relevant requirement IDs, covering each in-scope requirement or explicitly proposing its deferral. Surface conflicts for resolution without rewriting requirements.
- Small changes — a separate requirements file is optional; when absent, capture necessary obligations and constraints briefly in the plan's Requirements section
- References — link relevant existing document sections, including requirements by ID, instead of repeating them; use relative paths in the saved file and verify linked files and sections exist
- Document state — keep assumptions separate from agreed outcomes; approval or saving the plan does not mean its phases are implemented or validated
- Short and concise — bullets over prose; skip empty sections
- Phased — prefer 2–4 phases; 1 when the change is already small; each phase is one logical deliverable (independently reviewable and completable — bundle tightly coupled work, separate unrelated concerns); each one line: title — what + why now
- Bias toward the smallest useful next step
- Open questions — use the question + recommendation format below; if any need user input, wait for answers before asking for approval
- Must not — implementation file paths, commands, config snippets, git/PR language, diagrams, or validation steps in the chat plan; document references are allowed
- Persist — on approval, auto-save as `docs/plans/<topic>/plan.md`; saved file uses the same plan body shown in chat
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

## Goal

{one sentence}

## Requirements

- {brief required outcome or constraint, only when needed and no separate requirements document exists}

## Plan

1. **{title}** — {what + why now}
2. ...

## Open questions

1. {concrete unresolved question ending in ?}
   Recommendation: {proposed answer and brief rationale}

## Next

{follow-up for another document, only when needed}
{if questions need user input: request answers and stop; otherwise: Happy with this plan? (y/n)}
```

**After approval (auto-saved):**

## Plan saved

- Path: docs/plans/<topic>/plan.md
- Phases: {count + titles}

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Goal and Plan
