# Explain

**Explain only** — short comprehension of code, flow, or concept. No edits, commits, or implementation.

## Input

Whatever the user names in this turn: path, symbol, error, selection, or concept. Ask at most 1–2 questions only if the target is unclear.

## Rules

- Read and inspect as needed — no writes, no git mutations
- **Be concise** — half a screen or less; bullets over prose
- Cite repo code with `path:line` when referencing it; say when guessing
- Include a **Trace** only when a walkthrough clarifies (multi-step flow, call chain, pipeline, state machine, async job, error path) — omit for simple or single-location targets
- Trace: high level, 5–10 numbered steps max — entry → key steps → outcome; real symbols/paths, not line-by-line narration
- Include an **Example** when a concrete illustration clarifies (sample call, request body, config snippet, or values) — omit when obvious
- Do not recommend next steps unless the user explicitly asks what to do

## Self-verify

Before replying, confirm the explanation against the repo:

- Re-read every cited `path:line` — symbols, behavior, and flow match
- For **Trace**, spot-check entry and at least one middle step in source
- When uncertain, run a targeted read or search — do not guess
- If a check fails, fix the output; note corrections only when material

## Output

Use this structure. Keep each section to 1–3 lines or bullets.

```
Objective: <one sentence — what it does and why it exists>

How:
- <core mechanism>
- ... (2–4 bullets)

Trace:
1. <entry>
2. <key step>
...
(omit when not useful)

Example:
- <concrete illustration — sample call, request, config, or values>
(omit when not useful)

Touches:
- <entry points, key files, dependencies — omit when obvious>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except **Objective**
