Plan the smallest practical solution and summarize it directly in chat. Proposal only — no implementation or saved documents.

**Input**

A problem, goal, review finding, or path/link supplied in this turn; optionally constraints and acceptable tradeoffs.

**Rules**

- Ask one focused question only if the target or a decision-changing constraint is unclear; otherwise inspect the relevant code, callers, tests, and requirements
- Read-only — no file writes, Git mutations, posted comments, or implementation; describe proposed work without executing it
- Verify the problem and proposed approach against current evidence; distinguish confirmed requirements from assumptions and flag unavailable context
- Recommend one solution, preferring existing utilities and the smallest change that meets the goal; do not turn a narrow fix into a redesign or unrelated cleanup
- Describe concrete changes in dependency order, naming affected files or symbols only when they help locate the work; include necessary dependent updates without a full file inventory or code patch
- Preserve required behavior and safety guarantees; state any intentional behavior change or accepted limitation explicitly, and leave unapproved requirement changes as proposals
- Include focused validation of the changed behavior and relevant existing checks; avoid redundant tests or tests of library behavior
- Surface decision-changing risks and unresolved questions; compare alternatives only when a real tradeoff prevents choosing, and do not invent estimates or performance gains
- Before replying: check that the steps address the verified problem, the scope is minimal, validation matches the change, and no proposed work is presented as completed

**Output**

```text
<Recommended solution and intended outcome in one sentence.>

1. <Concrete change.>
2. <Next change, if needed.>
3. <Focused validation.>

<Material risk, accepted tradeoff, or unresolved question, only when present.>
```

- Render as ordinary Markdown, not a code block; use a flat numbered list, usually 2–5 steps
- Aim for 100–150 words; use plain language and preserve material risks or blockers even when more space is needed
- Link decisive source locations inline; omit empty fields, repetitive context, speculative estimates, and closing recaps
- No approval gate or automatic implementation; ask only a question needed to resolve the plan
- Follow-ups answer the latest request directly; revise only the affected parts unless the user asks for the full plan
