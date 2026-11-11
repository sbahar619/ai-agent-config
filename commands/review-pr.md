Review PR only — GitHub pull request via gh; inline comments on changed lines. No edits, commits, or fixes.

**Input:** PR URL — required. Do not fall back to staged or branch diff.

**Rules**

- Ask at most 1 question if no PR URL is given or scope is ambiguous — do not proceed blindly
- Read and inspect as needed — no writes, no git mutations
- PR scope only — ignore local staged/uncommitted changes unless part of the PR diff
- Changed lines only — comment on diff hunks, not untouched code
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

```text
<Approve | Request changes | Block: short conclusion about the reviewed scope.>
<Most important issue and recommended next step, if any; source location.>

Want the review details?
```

- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- Briefly surface every blocking or decision-changing issue; number independent issues by severity. Do not hide blockers behind the detail offer
- Cite each finding's verified location; for diff reviews, cite a changed hunk. Keep detailed evidence and reproduction examples for requested explanations
- A clean review needs only the verdict and scope; omit the offer. State material inspection limits immediately
- For requested details, explain the concrete trigger, consequence, and fix without repeating the initial answer; label illustrative examples and never claim an unrun reproduction
- Block means security/correctness/data-loss; Request changes means missing tests or real regressions; Approve means only minor/nit findings
- If access prevents review, say "Unable to review", the failed operation and recovery attempted, and the next step to restore access; do not issue an approval
