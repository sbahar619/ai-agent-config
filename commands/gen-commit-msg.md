# Generate commit message

Generate a Conventional Commit message from staged changes. **Do not commit** unless the user explicitly asks.

## Input

| Priority | Source |
|----------|--------|
| 1 | `git diff --staged` when staged changes exist |
| 2 | User-pasted diff or context when nothing is staged |

If no diff is available, ask for a paste or switch to Agent mode to read it.

Optional user notes: purpose, issue link, risks, follow-ups.

## Process

Inspect staged changes and infer:

- Primary intent (feature, fix, refactor, etc.)
- Impacted area (optional scope)
- User-visible impact, if any
- Why the change was needed, if inferable
- Test updates, if present

Produce the most concise subject that uniquely describes the change. Add a body only when it improves clarity.

## Tone — high level, not implementation detail

Write for someone scanning `git log`, not reviewing the diff.

- Describe **intent, outcome, and user/system impact** — not how the code changed
- Subject: one clear **what changed and why it matters** (behavior, contract, fix)
- Body: **why** when non-obvious — tradeoffs, motivation, risk — not step-by-step edits
- Avoid: file paths, function/type names, variable renames, refactor mechanics, line-level diffs, "add X to Y", internal wiring unless that *is* the change (e.g. extract shared helper with no behavior change → say "extract …" at module level, not symbol names)
- Prefer: "fix timeout when …", "add validation for …", "remove unused …", "migrate config to …"

Good vs bad:

```
fix(auth): reject expired tokens on refresh

Sessions were accepted after expiry when only the access token was checked.
```

```
fix(auth): add checkTokenExpiry in refresh.go and update TestRefresh
```


## Output (required)

Output **only** a fenced code block — no text before or after. No headings like "Subject:" or "Body:".

Inside the block:

- Exactly 1 subject line
- Exactly 1 blank line
- 0+ body lines (wrap to 70 chars)

Example shape:

```
type(scope): imperative summary

Optional body when the change is non-trivial.
```

### Subject line

- Start with `type:` or `type(scope):`
- Conventional Commit types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`, `build`, `perf`, `revert`
- Imperative mood (e.g. "add", "fix", "remove") — no trailing period
- **High level** — behavior or outcome, not files, symbols, or diff mechanics

### Body

- Include only when the change is non-trivial (reasoning, tradeoffs, risks, user-visible impact)
- Stay **high level** — why this change, not what moved where in code
- Short paragraphs or bullets when helpful
- Wrap each line to max 70 chars for copy/paste
