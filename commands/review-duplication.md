Review only — identify repeated implementation of the same rule that is worth sharing. No edits or fixes.

**Input:** The diff, paths, or symbols named in the message.

**Rules**

- Ask at most one question if the target is unclear; do not assume a target from earlier work
- Inspect the supplied scope and relevant counterparts or existing utilities; for a diff, anchor each finding on a changed line
- Read-only — no file writes, Git mutations, or posted comments
- Compare meaning, inputs, outputs, errors, and side effects; similar-looking code alone is not duplication worth removing
- Prefer an existing suitable utility; otherwise recommend the smallest shared helper or loop only when reduced maintenance outweighs added abstraction
- Preserve checks at distinct safety boundaries or against different object versions; do not merge checks with different failure meanings
- Cite the repeated locations and identify the shared rule; avoid generic frameworks or callbacks merely to save a few lines
- Review implementation duplication only; duplicate test-case coverage belongs to the existing review-test-cases command
- Before replying: confirm each finding represents the same rule and a concrete reuse benefit; drop speculative findings and state any inspection limits

**Output**

```text
<Whether a change is needed, in plain language.>
<Recommended next step; include any consequence that changes the decision.>

Want the explanation?
```

- Omit routine process summaries (tools used, checks passing, no writes, or tests not run). Mention a verification gap only when it changes the verdict or next step, and connect it to the specific risk; do not append generic disclaimers
- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- For multiple changes, number them by importance; keep each to the issue and recommended action in short sentences. Include a concise source location when needed to identify the target
- If no changes are needed, say "No changes recommended." without a follow-up offer
- If review is incomplete, state the limitation and how to resolve it; do not claim a clean review
- No edits or implementation are authorized by a request for explanation
