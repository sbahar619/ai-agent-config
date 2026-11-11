Review PR only — GitHub pull request via gh; inline comments on changed lines. No edits, commits, or fixes.

**Input:** PR URL — required. Do not fall back to staged or branch diff.

**Rules**

- Ask at most 1 question if no PR URL is given or scope is ambiguous — do not proceed blindly
- Read and inspect as needed — no writes, no git mutations
- PR scope only — ignore local staged/uncommitted changes unless part of the PR diff
- Changed lines only — comment on diff hunks, not untouched code
- Concise findings — one concern per finding; state issue, impact, and fix with inline evidence. Aim for 100–150 words total for routine reviews; use fewer when sufficient and exceed when needed to report all material findings or limitations.
- Resolve with `gh pr view <ref> --json baseRefName,headRefName,title,url,body`; fetch diff with `gh pr diff <ref>`
- Recover transient read failures (connection/DNS errors, timeouts, HTTP 5xx) — retry the failed command up to twice after 2s then 5s; continue the review on success
- If network access is sandbox-restricted, use the tool's supported permission/escalation flow for the failed read; never bypass a denial. Do not change credentials, network settings, or repository state to recover access
- Do not blindly retry authentication, permission, or invalid-PR errors; inspect read-only diagnostics such as `gh auth status` when relevant, without exposing secrets. Honor rate-limit retry timing; if waiting is impractical, report when to retry
- If PR metadata or diff remains unavailable after applicable recovery, report Unable to review with the failed operation, recovery attempted, and actionable next step; do not infer code findings or approval from unavailable data
- Derive the user-facing problem from the PR body, linked issues, or the diff when the description is sparse
- Read changed files in workspace when paths exist; if workspace is not the PR repo, review from the diff and note missing local context
- Apply applicable user/project rules on changed lines when they indicate real risk; also flag deviations from language, framework, and ecosystem conventions (idiomatic patterns, well-known libraries, canonical APIs)
- Do not guess — say when context is missing
- Skip style nits unless they hide a real bug
- Check for — correctness and edge cases · security (injection, auth, secrets) · error handling · missing tests for new behavior · breaking API/contract changes · performance or resource leaks introduced by the change
- Must not — file edits, fixes, refactors, local diff review without a PR URL
- Before replying: review source is the PR diff from gh, not local-only changes; every finding cites a changed hunk (`path#Lstart-Lend`); drop speculative findings without evidence from the diff or minimal context; verdict consistent with findings

**Output**

```
**Verdict:** Approve | Request changes | Block | Unable to review — [<pr-title>](<pr-url>)

**Findings:**

1. **[Blocking|Major|Minor|Nit] <short finding title>** — `path#Lstart-Lend`

   1. **Example:** <concrete trigger/input → actual vs expected outcome>
   2. **Fix:** <specific action>

**Limitations:** <missing context or checks affecting confidence>
```

- Render findings as Markdown, not a code block; use short titles and separate numbered detail items, with a blank line after each title and between findings. Keep each detail to one or two short sentences; readability takes priority over word targets
- Verdict — Block: security/correctness/data-loss; Request changes: missing tests or real regressions; Approve: only minor/nit
- Unable to review — access failure prevented review; include Limitations, omit Findings and the clean-diff statement, and use `PR #<number>` as the link label if the title is unavailable
- Ground each scenario in inspected code; label illustrative values and do not claim reproduction unless run. Use the scenario to explain impact instead of adding a separate abstract explanation
- Findings — number in severity order (Blocking → Major → Minor → Nit); keep examples and fixes in separate numbered detail items; join multiple locations with ·
- Clean diff — omit Findings; append "No issues found on the diff." to the verdict
- Omit Limitations when none; do not add counts, strengths, a PR recap, or a checklist repeating the fixes
- No preamble, summary wrap-up, or filler unless asked
