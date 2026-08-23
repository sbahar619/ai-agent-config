---
name: review-test-cases
description: >-
  Flag test cases that duplicate both branch and runtime concern of another
  case. Use when auditing a test suite for redundant coverage.
disable-model-invocation: true
---

# Review Test Cases

Flag test cases that duplicate both the code branch and runtime concern of
another case. No edits, commits, or fixes.

## Input

The test function or file to review.

## Rules

- Read the test and the code under test — no writes, no git mutations
- For each test case, identify: (1) the code branch it exercises, (2) the
  runtime concern it validates
- A case is unique if it covers a distinct branch OR a distinct runtime concern
- Flag a case only when it duplicates both the branch and the concern of another
- Cite the duplicating pair by case name
- Skip style, naming, and structure nits — scope is duplication only
- Before replying: confirm each flagged pair truly shares both branch and
  concern; drop uncertain flags
- Must not — edit files, apply fixes, refactor, or rewrite tests

## Output

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
