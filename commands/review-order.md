Analyze changed files, build a test-based dependency graph, and output a prioritized review order so the lowest-level changes are reviewed before the code that depends on them.

**Input:** Working directory changes — use `git diff --cached` (staged) if it has any output, otherwise fall back to `git diff` (unstaged). Do not use branch diffs or accept paths from the message.

**Rules**

- Run `git diff --cached --name-only` first; if empty, run `git diff --name-only` — use whichever has files
- Never ask for scope — always derive it from the working directory as above
- Read-only — no edits, commits, or fixes
- Changed files only — only include files present in the diff; do not graph untouched files
- Build the graph from imports and test coverage:
  - Source file A → Source file B: A imports B (A depends on B; review B first)
  - Test file T → Source file S: T tests or imports S (review S before T)
  - Only draw edges between changed files — edges to unchanged files are noted but do not affect order
- Topological sort the changed files: leaves (no in-graph dependencies) come first
- When two files have no ordering constraint, list the non-test file before the test file
- Cycles — if a cycle exists among changed files, flag it and pick a reasonable break point
- Before replying: verify every file listed is actually in the diff; verify every edge reflects a real import or test relationship found by reading the files; drop inferred edges without evidence

**Output**

```
## Review Order · staged | unstaged

1. `path/to/a.go`
2. `path/to/b.go`
3. `path/to/c.go`
4. `path/to/c_test.go`
```

- One file per line, numbered, no extra prose
- No preamble or filler
- Cycle — if one exists, flag it in a single line after the list: `⚠ cycle: a.go ↔ b.go`
