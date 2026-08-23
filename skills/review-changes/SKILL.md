---
name: review-changes
description: >-
  Full local git-diff review with severity-ranked inline findings. Use when
  reviewing staged, branch, or named-path changes locally.
disable-model-invocation: true
---

# Review Changes

Full git diff review (staged, branch, or named paths). No edits, commits,
or fixes.

## Input

The staged changes, branch diff, or paths to review.

## Rules

- Read and inspect as needed — no writes, no git mutations
- Changed lines only — comment on diff hunks, not untouched code
- Apply applicable project rules on changed lines when they indicate real risk
- Do not guess — say when context is missing
- Skip style nits unless they hide a real bug
- Must not — file edits, fixes, refactors, or rewriting the diff
- Check for — correctness and edge cases · security (injection, auth, secrets) ·
  error handling · missing tests for new behavior · breaking API/contract changes ·
  performance or resource leaks
- Before replying: every finding cites a changed hunk (`path#Lstart-Lend`);
  drop speculative findings; verdict consistent with findings

## Output

```
## Review · `<scope>`
`branch-name` | staged | `path/...`

## Verdict · Approve | Request changes | Block
<one-line rationale>

**Findings:** <n> blocking · <n> major · <n> minor · <n> nit

---

### Blocking
(none — omit section when empty)

**1.** `path/to/file.go#L123-L130`
<what + why + suggested fix>

### Major
...

### Minor
...

### Nit
...

---

### Strengths
- <2–4 bullets; omit when nothing notable>

### Before merge
- [ ] <action items; omit section when empty>
```

- Verdict — Block: security/correctness/data-loss; Request changes: missing tests
  or regressions; Approve: only minor/nit
- Findings — group by severity; omit empty sections
- Numbering — one global sequence (1…n); prefix **N.**
- Clean diff — Approve, all counts zero: omit Findings and Before merge;
  "No issues found on the diff."
