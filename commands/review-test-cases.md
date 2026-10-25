Review only — flag test cases that duplicate both the code branch and runtime concern of another case. No edits, commits, or fixes.

**Input:** The test function or file named in the message.

**Rules**

- Read the test and the code under test — no writes, no git mutations
- For each test case, identify: (1) the code branch it exercises, (2) the runtime concern it validates (e.g. nil safety, type assertion, default behavior, error path)
- A case is unique if it covers a distinct branch OR a distinct runtime concern — it need not cover both
- Flag a case only when it duplicates both the branch and the runtime concern of another case
- In the detailed report, cite each duplicating pair by case name
- Skip style, naming, and structure nits — scope is duplication only
- Before replying: confirm each flagged pair truly shares both branch and concern; drop uncertain flags; keep the initial response within the summary cap and wait for approval before showing the table report
- Must not — edit files, apply fixes, refactor, or rewrite tests

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Report | Show the table report? (y/n) | Stop; do not output the report |

**Output — initial summary**

```
<reviewed scope>: <No duplicate cases found | N duplicate pairs found>.

Show the table report? (y/n)
```

- At most 60 words across the verdict and gate; no tables, case lists, or detailed findings before approval
- Complete the review before summarizing; if inspection is incomplete, state that limitation instead of claiming no duplicates
- Wait for the answer; approval authorizes the detailed report only, not edits

**Output — table report after approval**

```
## Test review · `<test function or file>`

### Coverage

| # | Case | Branch | Runtime concern |
|---|------|--------|-----------------|
| 1 | <case name> | <branch exercised> | <concern validated> |
| 2 | ... | ... | ... |

### Duplicates
- **<case A>** ↔ **<case B>** — both exercise `<branch>` for `<concern>`

```

- Omit Duplicates section when none found
- Include every reviewed case in Coverage; the initial summary cap does not apply to the approved report
- No preamble, summary wrap-up, or filler unless asked
