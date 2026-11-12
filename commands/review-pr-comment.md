Review a single GitHub PR review comment for correctness against the current code, then recommend a next step; draft a reply when requested. Do not post unless the user explicitly asks.

**Input:** PR review comment URL — required (e.g. `.../pull/123#discussion_r456`, `#issuecomment-456`, or `#pullrequestreview-456`).

**Rules**

- If no comment URL is given, ask one question — do not guess
- Parse owner, repo, PR number, and comment id/type from the URL
- Fetch the comment: discussion comment → `gh api repos/<owner>/<repo>/pulls/comments/<id>`; issue comment → `gh api repos/<owner>/<repo>/issues/comments/<id>`; review summary → `gh api repos/<owner>/<repo>/pulls/reviews/<id>`
- Recover transient GitHub read failures (connection/DNS errors, timeouts, HTTP 5xx) — retry the failed read up to twice after 2s then 5s; continue on success. Do not apply these retries to posting replies
- If network access is sandbox-restricted, use the tool's supported permission/escalation flow for the failed read; never bypass a denial. Do not change credentials, network settings, or repository state to recover access
- Do not blindly retry authentication, permission, or invalid-URL errors; inspect read-only diagnostics such as `gh auth status` when relevant, without exposing secrets. Honor rate-limit retry timing; if waiting is impractical, report when to retry
- If the comment or current code remains unavailable after applicable recovery, report Unable to review with the failed operation, recovery attempted, and actionable next step; do not infer comment correctness from unavailable data
- Identify the reviewer's objective internally before judging it; do not restate their comment unless clarification is needed
- Verify against the current code, not just the comment's `diff_hunk` — read the referenced file/lines in the workspace, or `gh pr diff <pr>` / `gh api .../contents/<path>` if not checked out locally, since the code may have moved since the comment was posted
- Do not guess — say when the referenced code or context can't be found
- Judge correctness on evidence: valid, partially valid, invalid, or needs clarification
- Must not — post the reply (`gh api .../replies`, `gh pr comment`), edit code, or commit unless the user explicitly asks
- Before replying: recommendation matches the verdict; the consequence is clear; any requested reply is concrete, short, and doesn't restate the reviewer's own comment back to them

**Output**

```text
<Valid | Partially valid | Invalid | Needs clarification | Unable to review> — <plain-language conclusion.>
<Recommended next step, including a decision-changing limitation if present.>

Want the explanation or a reply draft?
```

- Omit routine process summaries (tools used, checks passing, no writes, or tests not run). Mention a verification gap only when it changes the verdict or next step, and connect it to the specific risk; do not append generic disclaimers
- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- Link the comment or relevant code inline when needed; omit a separate source section
- On access failure, state the failed operation, recovery attempted, and how to resume; omit the draft offer
- When explanation is requested, give one minimal source-grounded example; label illustrative values and never claim an unrun reproduction
- When a reply draft is requested, provide a short copy-ready plain-text code block, one short sentence per line; do not imply a proposed fix is complete
- Post only when explicitly requested; for discussion comments use `gh api repos/<owner>/<repo>/pulls/<pr>/comments/<id>/replies`, for issue comments use `gh pr comment <pr>`
