# Explain

Explain only — short comprehension of code, flow, or concept. No edits, commits, or implementation.

**Input**

Whatever the user names in this turn: path, symbol, error, selection, or concept.

**Rules**

- Ask at most 1–2 questions only if the target is unclear
- Read and inspect as needed — no writes, no git mutations
- Cite repo code with `path:line` when referencing it; say when guessing
- Do not recommend next steps unless the user explicitly asks what to do
- Before replying: re-read every cited `path:line` — symbols, behavior, and flow match; for a requested walkthrough, spot-check entry and at least one middle step; when uncertain, run a targeted read or search — do not guess; fix output if a check fails; note corrections only when material

**Output**

```text
<Direct plain-language answer in 2–4 short sentences.>

Want an example or walkthrough?
```

- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- The explanation is the requested result; do not add an unsolicited action recommendation
- If an example or walkthrough was requested, provide it immediately; use numbered steps for a flow and omit the expansion offer. Label illustrative values and never imply an unrun example was reproduced
- Cite relevant code inline when needed; omit file inventories
