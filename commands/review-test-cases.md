Review only — flag test cases that duplicate both the code branch and runtime concern of another case. No edits, commits, or fixes.

**Input:** The test function or file named in the message.

**Rules**

- Read the test and the code under test — no writes, no git mutations
- For each test case, identify: (1) the code branch it exercises, (2) the runtime concern it validates (e.g. nil safety, type assertion, default behavior, error path)
- A case is unique if it covers a distinct branch OR a distinct runtime concern — it need not cover both
- Flag a case only when it duplicates both the branch and the runtime concern of another case
- Cite the duplicating pair by case name
- Skip style, naming, and structure nits — scope is duplication only
- Before replying: confirm each flagged pair truly shares both branch and concern; drop uncertain flags
- Must not — edit files, apply fixes, refactor, or rewrite tests

**Output**

```
## Test review · `<test function or file>`

### Coverage

| # | Case | Branch | Runtime concern |
|---|------|--------|-----------------|
| 1 | <case name> | <branch exercised> | <concern validated> |
| 2 | ... | ... | ... |

### Duplicates
- **<case A>** ↔ **<case B>** — both exercise `<branch>` for `<concern>`

### Summary
<one-line verdict: clean | N duplicate pairs found>
```

- Omit Duplicates section when none found
- No preamble, summary wrap-up, or filler unless asked
