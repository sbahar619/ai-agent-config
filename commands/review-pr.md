Review PR only — GitHub pull request via gh; inline comments on changed lines. No edits, commits, or fixes.

**Input:** PR URL — required. Do not fall back to staged or branch diff.

**Rules**

- Ask at most 1 question if no PR URL is given or scope is ambiguous — do not proceed blindly
- Read and inspect as needed — no writes, no git mutations
- PR scope only — ignore local staged/uncommitted changes unless part of the PR diff
- Changed lines only — comment on diff hunks, not untouched code
- Concise findings — one concern per finding; state issue, impact, and fix with inline evidence. Aim for 100–150 words total for routine reviews; use fewer when sufficient and exceed when needed to report all material findings or limitations.
- Resolve with `gh pr view <ref> --json baseRefName,headRefName,title,url,body` — stop on error; fetch diff with `gh pr diff <ref>`
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
**Verdict:** Approve | Request changes | Block — [<pr-title>](<pr-url>)

**Findings:**

1. [Blocking|Major|Minor|Nit] `path#Lstart-Lend` — <issue and impact → fix>

**Limitations:** <missing context or checks affecting confidence>
```

- Verdict — Block: security/correctness/data-loss; Request changes: missing tests or real regressions; Approve: only minor/nit
- Findings — number in severity order (Blocking → Major → Minor → Nit); one or two sentences each; join multiple locations with ·
- Clean diff — omit Findings; append "No issues found on the diff." to the verdict
- Omit Limitations when none; do not add counts, strengths, a PR recap, or a checklist repeating the fixes
- No preamble, summary wrap-up, or filler unless asked
