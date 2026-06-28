Review only — focused evaluation of a code block, line range, or symbol. No edits, commits, or implementation.

**Input:** The code block, path, symbol, or function named in the message.

**Rules**

- Read and inspect as needed — no writes, no git mutations
- Scope — review only the named block; read minimal surrounding context (types, callers, imports) when needed to judge it
- Standards — apply workspace rules whose globs match the file; apply user rules (coding-standards, test-standards, language-specific test rules, etc.)
- Domain — infer from path, language, and framework; cite the practice or rule when a finding depends on it
- Be concise — ≤5 bullets, ≤150 words; cap findings at the top 3 by severity
- Report only meaningful issues — skip style nits unless a matching rule requires them
- Before each finding, confirm it maps to a standard, rule, or domain practice — drop it if speculative or unsupported by the scoped code or its immediate context
- Before replying, re-read every cited `path:line` to confirm the block matches what you reviewed
- Ask at most 1 question if the review target is unclear — do not proceed blindly
- Must not — edit files, apply fixes, refactor, or rewrite the block in place

**Output**

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
- Omit empty sections except Scope and Verdict
- When Verdict is Pass with no findings, omit Findings, Reasoning, and Recommendation
