Review a single GitHub PR review comment for correctness against the current code, then recommend next steps and draft a reply. Do not post unless the user explicitly asks.

**Input:** PR review comment URL — required (e.g. `.../pull/123#discussion_r456`, `#issuecomment-456`, or `#pullrequestreview-456`).

**Rules**

- If no comment URL is given, ask one question — do not guess
- Parse owner, repo, PR number, and comment id/type from the URL
- Fetch the comment: discussion comment → `gh api repos/<owner>/<repo>/pulls/comments/<id>`; issue comment → `gh api repos/<owner>/<repo>/issues/comments/<id>`; review summary → `gh api repos/<owner>/<repo>/pulls/reviews/<id>`
- Recover transient GitHub read failures (connection/DNS errors, timeouts, HTTP 5xx) — retry the failed read up to twice after 2s then 5s; continue on success. Do not apply these retries to posting replies
- If network access is sandbox-restricted, use the tool's supported permission/escalation flow for the failed read; never bypass a denial. Do not change credentials, network settings, or repository state to recover access
- Do not blindly retry authentication, permission, or invalid-URL errors; inspect read-only diagnostics such as `gh auth status` when relevant, without exposing secrets. Honor rate-limit retry timing; if waiting is impractical, report when to retry
- If the comment or current code remains unavailable after applicable recovery, report Unable to review with the failed operation, recovery attempted, and actionable next step; do not infer comment correctness from unavailable data
- State the reviewer's objective in your own words before judging it — what exactly is being claimed or requested
- Verify against the current code, not just the comment's `diff_hunk` — read the referenced file/lines in the workspace, or `gh pr diff <pr>` / `gh api .../contents/<path>` if not checked out locally, since the code may have moved since the comment was posted
- Do not guess — say when the referenced code or context can't be found
- Judge correctness on evidence: valid, partially valid, invalid, or needs clarification
- Must not — post the reply (`gh api .../replies`, `gh pr comment`), edit code, or commit unless the user explicitly asks
- Explain the verdict with one minimal concrete example: input/configuration/action → actual result vs expected result; for non-behavioral comments, show the exact before → proposed after. Ground it in inspected code; label illustrative values and do not claim reproduction unless run
- Aim for 100–150 words total, including the reply draft; preserve material evidence and limitations. Use the example as the explanation, not an extra walkthrough
- Before replying: recommendation matches the verdict; the example makes the consequence clear; reply is concrete, short, and doesn't restate the reviewer's own comment back to them

**Output**

````
## Comment review · <path>#Lstart-Lend (omit path for a general/issue comment)
<comment-url>

**Reviewer's point:** <one-line restatement>

**Verdict:** Valid | Partially valid | Invalid | Needs clarification | Unable to review

**Example:** <specific scenario → actual vs expected outcome; 1–2 sentences with source evidence>

**Recommendation:** Code fix | No changes | Clarify with reviewer

<concrete next step; if a fix, name it briefly>

---

**Reply draft**

```
<plain-language conclusion and proposed action — 1–2 sentences; do not imply a proposed fix is already done>
```
````

- If evidence is insufficient for an example, state what is missing instead of inventing behavior
- Unable to review — omit Example and Reply draft; omit the reviewer's point and path when unavailable; use Recommendation to describe how to restore access and resume review, rather than asking the reviewer to clarify an access failure
- Reply draft is its own fenced code block, plain text, ready to copy-paste — no quoting of the original comment back; use one sentence per line so the block stays readable without horizontal scrolling
- Blank line after every bold label (`**Verdict:**`, `**Recommendation:**`) before its body text — a single newline collapses to a space in rendered markdown
- If the user asks to post: reply to a discussion comment with `gh api repos/<owner>/<repo>/pulls/<pr>/comments/<id>/replies -f body='<text>'`; reply to an issue comment with `gh pr comment <pr> -b '<text>'`
- No preamble or filler unless asked
