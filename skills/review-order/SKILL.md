---
name: review-order
description: >-
  Build a dependency-aware prioritized review order from changed files.
  Use when deciding which files to review first based on import and test
  dependencies.
disable-model-invocation: true
---

# Review Order

Analyze changed files, build a test-based dependency graph, and output a
prioritized review order so lowest-level changes are reviewed first.

## Input

Working directory changes — use `git diff --cached` (staged) if it has output,
otherwise fall back to `git diff` (unstaged). Do not use branch diffs or accept
paths from the message.

## Rules

- Run `git diff --cached --name-only` first; if empty, run `git diff --name-only`
- Never ask for scope — always derive from the working directory
- Read-only — no edits, commits, or fixes
- Changed files only — only include files present in the diff
- Build graph from imports and test coverage:
  - Source A → Source B: A imports B (review B first)
  - Test T → Source S: T tests/imports S (review S before T)
  - Only edges between changed files; edges to unchanged files noted but don't
    affect order
- Topological sort: leaves (no in-graph dependencies) come first
- Tie-break: non-test file before test file
- Cycles — flag and pick a reasonable break point
- Before replying: every file listed is in the diff; every edge reflects a real
  import or test relationship

## Output

```
## Review Order · staged | unstaged

1. `path/to/a.go`
2. `path/to/b.go`
3. `path/to/c.go`
4. `path/to/c_test.go`
```

- One file per line, numbered, no extra prose
- Cycle — flag after the list: `⚠ cycle: a.go ↔ b.go`
