---
name: gen-commit-msg
description: >-
  Draft a Conventional Commit message from staged changes or a pasted diff.
  Use when generating a commit message for current or described changes.
disable-model-invocation: true
---

# Generate Commit Message

Draft a Conventional Commit message from staged changes. Do not commit unless
explicitly asked.

## Input

| Priority | Source |
|----------|--------|
| 1 | `git diff --staged` when staged changes exist |
| 2 | User-pasted diff or context when nothing is staged |

Optional user notes: purpose, issue link, risks, follow-ups.

## Rules

- If no diff is available, ask for a paste or read it
- Inspect changes and infer: primary intent, impacted area (optional scope),
  user-visible impact, why needed, test updates
- Most concise subject that uniquely describes the change; body only when it
  improves clarity
- Write for someone scanning `git log` — intent, outcome, and impact, not how
  the code changed
- Subject: one clear what changed and why it matters (behavior, contract, fix)
- Body: why when non-obvious — tradeoffs, motivation, risk — not step-by-step edits
- Avoid: file paths, function/type names, variable renames, refactor mechanics,
  line-level diffs, "add X to Y", internal wiring unless that is the change
- Must not — commit unless explicitly asked

## Output

```
type(scope): imperative summary

Optional body when the change is non-trivial.
```

- Exactly 1 subject line, 1 blank line, 0+ body lines (wrap to 70 chars)
- Subject: `type:` or `type(scope):`; imperative mood, no trailing period
- Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`, `build`, `perf`, `revert`
