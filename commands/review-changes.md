Review diff only — full git diff review (staged, branch, or named paths). GitHub-style inline comments on changed lines. No edits, commits, or fixes.

**Input:** The staged changes, branch diff, or paths named in the message.

**Rules**

- Ask at most 1 question if the diff scope is unclear — do not proceed blindly
- Read and inspect as needed — no writes, no git mutations
- Changed lines only — comment on diff hunks, not untouched code
- Apply applicable user/project rules on changed lines when they indicate real risk
- Do not guess — say when context is missing
- Skip style nits unless they hide a real bug
- Must not — file edits, fixes, refactors, or rewriting the diff
- Check for — correctness and edge cases · security (injection, auth, secrets) · error handling · missing tests for new behavior · breaking API/contract changes · performance or resource leaks introduced by the change
- Before replying: scope matches the diff actually read; every finding cites a changed hunk (`path#Lstart-Lend`); drop speculative findings without evidence from the diff or minimal context; verdict consistent with findings

**Output**

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

- Verdict — Block: security/correctness/data-loss; Request changes: missing tests or real regressions; Approve: only minor/nit
- Findings — group by severity (Blocking → Major → Minor → Nit); omit empty sections
- Numbering — one global sequence (1…n) in severity order; prefix **N.**
- Comment block — **N.** + location(s), blank line, body (~3 lines max); multi-location: join with ·
- Clean diff — Approve, all counts zero: omit Findings and Before merge; one line under Verdict: "No issues found on the diff."
- No preamble, summary wrap-up, or filler unless asked
