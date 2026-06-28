# Implement only

Implement only — source code changes for one scoped task. No commits, push, amend, or PRs.

**Input**

| Source | Description |
|--------|-------------|
| Doc    | Path to a design or plan doc + optional phase number(s) or title |
| Direct | Concrete task — fix, small feature, localized change |

Read referenced docs from the repo; treat as the spec.

**Rules**

- Ask at most one clarifying question if scope is unclear; otherwise state your assumption and proceed
- Scoped work — only what the doc or task specifies; stop and explain if the spec is insufficient
- Follow applicable user/project rules (coding and test standards) for files you will touch
- Run lint/tests as you go; fix failures caused by your changes; stop and report failures that appear unrelated to your changes (pre-existing, environmental, or config issues)
- Suggested branch — one kebab-case name in completion output only
- Must not — commit, push, amend, or open/update a PR; modify architecture or plan docs; work outside the stated spec
- Before replying: changed files match the spec; validation run and reported; output matches the Done template — no extra sections

**Gates**

One gate only. Done gate always runs.

| Step | Prompt                           | n                        |
|------|----------------------------------|--------------------------|
| Done | Happy with implementation? (y/n) | Fix per feedback; re-ask |

**Output**

```
## Implementation complete
- Scope: <summary>
- Files: <paths>
- Validation: <commands> → <pass | fail — exit code N>
- Suggested branch: `<kebab-case-name>`

## Next
Happy with implementation? (y/n)
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections
