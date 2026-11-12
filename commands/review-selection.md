Review only — focused evaluation of a code block, line range, or symbol. No edits, commits, or implementation.

**Input:** The code block, path, symbol, or function named in the message.

**Rules**

- Read and inspect as needed — no writes, no git mutations
- Scope — review only the named block; read minimal surrounding context (types, callers, imports) when needed to judge it
- Standards — apply workspace rules whose globs match the file; apply user rules (coding-standards, test-standards, language-specific test rules, etc.)
- Domain — apply language, framework, and ecosystem conventions (idiomatic patterns, well-known libraries, canonical APIs); cite the practice or rule when a finding depends on it
- Report only meaningful issues — skip style nits unless a matching rule requires them
- Before each finding, confirm it maps to a standard, rule, or domain practice — drop it if speculative or unsupported by the scoped code or its immediate context
- Before replying, re-read every cited `path:line` to confirm the block matches what you reviewed
- Ask at most 1 question if the review target is unclear — do not proceed blindly
- Must not — edit files, apply fixes, refactor, or rewrite the block in place

**Output**

```text
<Pass | Minor issues | Needs change: short conclusion about the reviewed scope.>
<Most important issue and recommended next step, if any; source location.>

Want the review details?
```

- Omit routine process summaries (tools used, checks passing, no writes, or tests not run). Mention a verification gap only when it changes the verdict or next step, and connect it to the specific risk; do not append generic disclaimers
- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- Briefly surface every blocking or decision-changing issue; number independent issues by severity. Do not hide blockers behind the detail offer
- Cite each finding's verified location; for diff reviews, cite a changed hunk. Keep detailed evidence and reproduction examples for requested explanations
- A clean review needs only the verdict and scope; omit the offer. State material inspection limits immediately
- For requested details, explain the concrete trigger, consequence, and fix without repeating the initial answer; label illustrative examples and never claim an unrun reproduction
