# Explain

Explain only — short comprehension of code, flow, or concept. No edits, commits, or implementation.

**Input**

Whatever the user names in this turn: path, symbol, error, selection, or concept.

**Rules**

- Ask at most 1–2 questions only if the target is unclear
- Read and inspect as needed — no writes, no git mutations
- Be concise — aim for 100–150 words for routine explanations; use fewer when sufficient and expand only for necessary detail or a requested walkthrough
- Cite repo code with `path:line` when referencing it; say when guessing
- Include a Trace only when a walkthrough clarifies (multi-step flow, call chain, pipeline, state machine, async job, error path) — omit for simple or single-location targets
- Trace: replace How with a high-level sequence, usually 3–5 steps — entry → key steps → outcome; real symbols/paths, not line-by-line narration
- Include an Example when a concrete illustration clarifies (sample call, request body, config snippet, or values) — omit when obvious
- Do not recommend next steps unless the user explicitly asks what to do
- Before replying: re-read every cited `path:line` — symbols, behavior, and flow match; for Trace, spot-check entry and at least one middle step; when uncertain, run a targeted read or search — do not guess; fix output if a check fails; note corrections only when material

**Output**

```
Objective: <one sentence — what it does and why it exists>

How:

- <core mechanism>

Example:
<short sample call, request, config, or values>
```

- No preamble, summary wrap-up, or filler unless asked
- How: 1–3 bullets, or replace with Trace and numbered steps when a walkthrough helps; never include both
- Cite relevant files inline instead of adding a Touches inventory; omit Example when it adds no clarity
- Omit empty sections except Objective
