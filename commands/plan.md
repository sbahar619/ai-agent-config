# Plan only

Plan only — high-level phased plan. No source edits, commits, or implementation.

**Input**

User provides a goal or problem — feature, refactor, bug, CI failure, or improvement.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed — investigate silently; no source writes until approval
- High level — what and why, not how; no architecture, APIs, or file-level detail
- Short and concise — bullets over prose; skip empty sections
- Phased — prefer 2–4 phases; 1 when the change is already small; each phase is one logical deliverable (independently reviewable and completable — bundle tightly coupled work, separate unrelated concerns); each one line: title — what + why now
- Bias toward the smallest useful next step
- Open questions — number each; if any need user input, present them and wait for answers before asking for approval
- Must not — file paths, commands, config snippets, git/PR language, diagrams, or validation steps in the chat plan
- Persist — on approval, auto-save as `docs/plans/<topic>/plan.md`; saved file uses the same plan body shown in chat
- Render — output the plan as rendered markdown in chat; never wrap the plan in a code fence; chat plan body matches what is written to the file (gate prompts are chat-only)
- Before replying: plan matches the output template — no extra sections; each phase is one line; count is 1–4; strip anything implementer-shaped (paths, commands, git/PR, config)

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Plan | Happy with this plan? (y/n) | List Goal + phases (number + name); user picks + comments; revise only those; re-ask |

**Output**

**Draft plan** — reproduce as rendered markdown (not a code block); plan body is identical to the persisted file:

## Goal

{one sentence}

## Plan

1. **{title}** — {what + why now}
2. ...

## Open questions

1. {question — omit section if none}

## Next

{if open questions: ask them and wait for answers before approval}
Happy with this plan? (y/n)

**After approval (auto-saved):**

## Plan saved

- Path: docs/plans/<topic>/plan.md
- Phases: {count + titles}

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Goal and Plan
