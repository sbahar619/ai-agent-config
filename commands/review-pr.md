# Review PR only

**Review PR only** — GitHub pull request via `gh`; inline comments on changed
lines. No edits, commits, or fixes.

## Input

User provides a PR reference — required; do not fall back to staged or branch diff.

| Form | Example |
|------|---------|
| URL | `https://github.com/org/repo/pull/123` |
| Repo + number | `org/repo#123` |
| Number | `#123` or `123` — current workspace repo via `gh repo view` |

Ask only if no PR reference is given or scope is ambiguous.

## Rules

- Read and inspect as needed — no writes, no git mutations
- **PR scope only** — ignore local staged/uncommitted changes unless part of the PR diff
- **Changed lines only** — comment on diff hunks, not untouched code
- Resolve with `gh pr view <ref> --json baseRefName,headRefName,title,url` — stop
  on error; fetch diff with `gh pr diff <ref>`
- Read changed files in workspace when paths exist; if workspace is not the PR
  repo, review from the diff and note missing local context
- Apply applicable **user/project rules** on changed lines when they indicate real risk
- Do not guess — say when context is missing
- Skip style nits unless they hide a real bug
- **Must not** — file edits, fixes, refactors, local diff review without a PR ref

## Check for

Correctness and edge cases · security (injection, auth, secrets) · error
handling · missing tests for new behavior · breaking API/contract changes ·
performance or resource leaks introduced by the change

## Self-verify

Before replying:

- Review source is the PR diff from `gh`, not local-only changes
- Every finding cites a changed hunk (`path#Lstart-Lend`)
- Drop speculative findings without evidence from the diff or minimal context
- Verdict consistent with findings

## Output

```
## Review · `<pr-title>`
<pr-url>

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

- **Verdict** — `Block` security/correctness/data-loss; `Request changes` missing
  tests or real regressions; `Approve` when only minor/nit
- **Findings** — group by severity (Blocking → Major → Minor → Nit); omit empty
  sections
- **Numbering** — one global sequence (1…n) in severity order; prefix `**N.**`
- **Comment block** — `**N.**` + location(s), blank line, body (~3 lines max);
  multi-location: join with ` · `
- **Clean diff** — `Approve`, all counts zero: omit Findings and Before merge;
  one line under Verdict: `No issues found on the diff.`
- No preamble, summary wrap-up, or filler unless asked
