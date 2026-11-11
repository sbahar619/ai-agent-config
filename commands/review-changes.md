Review diff only — full git diff review (staged, branch, or named paths). GitHub-style inline comments on changed lines. No edits, commits, or fixes.

**Input:** The staged changes, branch diff, or paths named in the message.

**Rules**

- Ask at most 1 question if the diff scope is unclear — do not proceed blindly
- Read and inspect as needed — no writes, no git mutations
- Changed lines only — comment on diff hunks, not untouched code
- Concise findings — one concern per finding; state issue, impact, and fix with inline evidence. Aim for 100–150 words total for routine reviews; use fewer when sufficient and exceed when needed to report all material findings or limitations.
- Apply applicable user/project rules on changed lines when they indicate real risk; also flag deviations from language, framework, and ecosystem conventions (idiomatic patterns, well-known libraries, canonical APIs)
- Do not guess — say when context is missing
- Skip style nits unless they hide a real bug
- Must not — file edits, fixes, refactors, or rewriting the diff
- Check for — correctness and edge cases · security (injection, auth, secrets) · error handling · missing tests for new behavior · breaking API/contract changes · performance or resource leaks introduced by the change
- Before replying: scope matches the diff actually read; every finding cites a changed hunk (`path#Lstart-Lend`); drop speculative findings without evidence from the diff or minimal context; verdict consistent with findings

**Output**

```
**Verdict:** Approve | Request changes | Block — <reviewed branch, staged changes, or paths>

**Findings:**

1. **[Blocking|Major|Minor|Nit] <short finding title>** — `path#Lstart-Lend`

   1. **Example:** <concrete trigger/input → actual vs expected outcome>
   2. **Fix:** <specific action>

**Limitations:** <missing context or checks affecting confidence>
```

- Render findings as Markdown, not a code block; use short titles and separate numbered detail items, with a blank line after each title and between findings. Keep each detail to one or two short sentences; readability takes priority over word targets
- Verdict — Block: security/correctness/data-loss; Request changes: missing tests or real regressions; Approve: only minor/nit
- Ground each scenario in inspected code; label illustrative values and do not claim reproduction unless run. Use the scenario to explain impact instead of adding a separate abstract explanation
- Findings — number in severity order (Blocking → Major → Minor → Nit); keep examples and fixes in separate numbered detail items; join multiple locations with ·
- Clean diff — omit Findings; append "No issues found on the diff." to the verdict
- Omit Limitations when none; do not add counts, strengths, a diff recap, or a checklist repeating the fixes
- No preamble, summary wrap-up, or filler unless asked
