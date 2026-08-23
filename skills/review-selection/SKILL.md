---
name: review-selection
description: >-
  Focused review of a code block or symbol against project standards. Use when
  reviewing a specific function, block, or symbol rather than a full diff.
disable-model-invocation: true
---

# Review Selection

Focused evaluation of a code block, line range, or symbol. No edits, commits,
or implementation.

## Input

The code block, path, symbol, or function to review.

## Rules

- Read and inspect as needed — no writes, no git mutations
- Scope — review only the named block; read minimal surrounding context when
  needed to judge it
- Standards — apply workspace rules whose globs match the file; apply user rules
  (coding-standards, test-standards, language-specific rules)
- Domain — infer from path, language, and framework; cite the practice or rule
  when a finding depends on it
- Concise — ≤5 bullets, ≤150 words; cap findings at top 3 by severity
- Report only meaningful issues — skip style nits unless a matching rule requires them
- Before each finding, confirm it maps to a standard, rule, or domain practice
- Before replying, re-read every cited `path:line` to confirm the block matches
- Must not — edit files, apply fixes, refactor, or rewrite the block

## Output

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

- Omit empty sections except Scope and Verdict
- When Verdict is Pass with no findings, omit Findings, Reasoning, and Recommendation
