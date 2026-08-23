---
name: review-pr
description: >-
  Full GitHub PR review via gh with verdict and inline findings. Use when
  reviewing a pull request on GitHub.
disable-model-invocation: true
---

# Review PR

Full GitHub pull request review via `gh`. No edits, commits, or fixes.

## Input

PR URL — required. Do not fall back to staged or branch diff.

## Rules

- Read and inspect as needed — no writes, no git mutations
- PR scope only — ignore local staged/uncommitted changes unless part of the PR
- Changed lines only — comment on diff hunks, not untouched code
- Resolve with `gh pr view <ref> --json baseRefName,headRefName,title,url,body`;
  fetch diff with `gh pr diff <ref>`
- Derive the user-facing problem from PR body, linked issues, or the diff
- Read changed files in workspace when paths exist; note when local context missing
- Apply applicable project rules on changed lines when they indicate real risk
- Do not guess — say when context is missing
- Skip style nits unless they hide a real bug
- Check for — correctness and edge cases · security · error handling · missing
  tests · breaking API/contract changes · performance or resource leaks
- Must not — file edits, fixes, refactors, local diff review without a PR URL
- Before replying: source is the PR diff from gh; every finding cites a changed
  hunk; verdict consistent with findings

## Output

```
## Review · `<pr-title>`
<pr-url>

**What this solves:** <1–2 sentences>

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
- Clean diff — Approve, all counts zero: "No issues found on the diff."
