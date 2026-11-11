# Verify only

Verify only — skeptical validation with evidence; Pass or Fail. No edits, commits, or implementation.

**Input**

| Source | User provides |
|--------|----------------|
| Session | Claimed-complete work in the current chat — goal, deliverables, validation |
| Spec doc | Path to a plan, design, or task description |
| Diff | Staged/uncommitted changes or named paths |

Derive what was claimed complete and success criteria from the source above, referenced docs, and the repo.

**Rules**

- Ask only if scope is unclear
- Read and inspect as needed — no writes, no git mutations
- Skeptical — require evidence from commands and files; do not trust completion claims or prior validation summaries
- Follow applicable user/project rules and language/ecosystem conventions when choosing lint and tests
- Pass only when success criteria are met, checks succeeded, and no blocking gaps or rule violations remain
- Must not — file edits, fixes, commits, or implementation
- Be concise — aim for 100–150 words for routine verification; use fewer when sufficient and exceed when needed for material failures, evidence, or limitations. Group related successful checks; do not repeat criteria as a separate checklist.
- Before replying: success criteria derived from user input and spec — not assumed; every validation claim and finding has evidence from files or command output; verdict matches findings — Fail when any blocking gap remains; output matches the template — no extra sections

**Output**

```
**Verdict:** Pass | Fail — <verified scope and source>

**Validation:** <grouped checks and results, with evidence>

**Findings:**

1. **<unmet criterion or rule violation>**

   1. **Result:** <expected vs observed>
   2. **Evidence:** <source or check result>

**Limitations:** <unverified scope, unavailable checks, or missing evidence>
```

- Render findings as Markdown, not a code block; use short titles and separate numbered detail items, with a blank line after each title and between findings. Keep each detail to one or two short sentences; readability takes priority over word targets
- No preamble, summary wrap-up, or filler unless asked
- Omit Findings and Limitations when empty; do not print "None" or repeat findings in the verdict
