# Generate commit message

Generate a Conventional Commit message from staged changes. Do not commit unless the user explicitly asks.

**Input**

| Priority | Source |
|----------|--------|
| 1 | `git diff --staged` when staged changes exist |
| 2 | User-pasted diff or context when nothing is staged |

Optional user notes: purpose, issue link, risks, follow-ups.

**Rules**

- If no diff is available, ask for a paste or switch to Agent mode to read it
- Inspect staged changes and infer: primary intent, impacted area (optional scope), user-visible impact, why needed, test updates
- Produce the most concise subject that uniquely describes the change; add a body only when it improves clarity
- Write for someone scanning `git log`, not reviewing the diff — intent, outcome, and user/system impact, not how the code changed
- Subject: one clear what changed and why it matters (behavior, contract, fix)
- Body: why when non-obvious — tradeoffs, motivation, risk — not step-by-step edits
- Avoid: file paths, function/type names, variable renames, refactor mechanics, line-level diffs, "add X to Y", internal wiring unless that is the change
- Prefer: "fix timeout when …", "add validation for …", "remove unused …", "migrate config to …"
- Must not — commit unless the user explicitly asks

Good vs bad:

```
fix(auth): reject expired tokens on refresh

Sessions were accepted after expiry when only the access token was checked.
```

```
fix(auth): add checkTokenExpiry in refresh.go and update TestRefresh
```

**Output**

```
type(scope): imperative summary

Optional body when the change is non-trivial.
```

- Output only the fenced code block — no text before or after; no headings like "Subject:" or "Body:"
- Inside the block: exactly 1 subject line, 1 blank line, 0+ body lines (wrap to 70 chars)
- Subject: `type:` or `type(scope):`; types `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`, `build`, `perf`, `revert`; imperative mood, no trailing period; high level — behavior or outcome, not files or symbols
- Body: only when non-trivial; short paragraphs or bullets; wrap each line to max 70 chars
