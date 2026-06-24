# Review code

**Review only** — focused evaluation of a code block, line range, or symbol. No edits, commits, or implementation.

Does **not** replace diff-wide Bugbot or security review.

## Input

| Priority | Source |
|----------|--------|
| 1 | Editor selection |
| 2 | `path:start-end` or cited block in the message |
| 3 | Path, symbol, or function the user names |

Ask at most 1 question only if the review target is unclear.

## Rules

- Read and inspect as needed — no writes, no git mutations
- **Scope** — review only the named block; read minimal surrounding context (types, callers, imports) when needed to judge it
- **Standards** — apply workspace rules whose globs match the file; apply user rules (`coding-standards`, `test-standards`, language-specific test rules, etc.)
- **Domain** — infer from path, language, and framework; cite the practice or rule when a finding depends on it
- **Be concise** — half a screen or less; bullets over prose; cap findings at the top 3 by severity
- Cite reviewed code with `path:line`; say when guessing
- Report only meaningful issues — skip style nits unless a matching rule requires them
- **Must not** — edit files, apply fixes, refactor, or rewrite the block in place

## Self-verify

Before replying:

- Re-read every cited `path:line` — the block matches what you reviewed
- Confirm each finding maps to a standard, rule, or domain practice (not preference)
- Drop findings that are speculative without evidence from the scoped code or its immediate context

## Output

Use this structure. Keep each section to 1–3 lines or bullets.

```
Scope: <path:lines — symbol or one-line summary>

Verdict: Pass | Minor issues | Needs change

Findings:
- [must|should|nit] <issue> — <why vs standard or domain practice>

Reasoning:
- <1–2 bullets tying verdict to the most important findings>

Recommendation:
- <concrete next step>
- <optional minimal code snippet illustrating the fix — not a full rewrite>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except **Scope** and **Verdict**
- When **Verdict** is Pass and there are no findings, omit **Findings**, **Reasoning**, and **Recommendation**
