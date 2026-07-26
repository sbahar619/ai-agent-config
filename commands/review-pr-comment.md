Review a single GitHub PR review comment for correctness against the current code, then recommend next steps and draft a reply. Do not post unless the user explicitly asks.

**Input:** PR review comment URL — required (e.g. `.../pull/123#discussion_r456`, `#issuecomment-456`, or `#pullrequestreview-456`).

**Rules**

- If no comment URL is given, ask one question — do not guess
- Parse owner, repo, PR number, and comment id/type from the URL
- Fetch the comment: discussion comment → `gh api repos/<owner>/<repo>/pulls/comments/<id>`; issue comment → `gh api repos/<owner>/<repo>/issues/comments/<id>`; review summary → `gh api repos/<owner>/<repo>/pulls/reviews/<id>`
- State the reviewer's objective in your own words before judging it — what exactly is being claimed or requested
- Verify against the current code, not just the comment's `diff_hunk` — read the referenced file/lines in the workspace, or `gh pr diff <pr>` / `gh api .../contents/<path>` if not checked out locally, since the code may have moved since the comment was posted
- Do not guess — say when the referenced code or context can't be found
- Judge correctness on evidence: valid, partially valid, invalid, or needs clarification
- Must not — post the reply (`gh api .../replies`, `gh pr comment`), edit code, or commit unless the user explicitly asks
- Before replying: recommendation matches the verdict; reply is high-level, short, and doesn't restate the reviewer's own comment back to them

**Output**

````
## Comment review · <path>#Lstart-Lend (omit path for a general/issue comment)
<comment-url>

**Reviewer's point:** <one-line restatement>

**Verdict:** Valid | Partially valid | Invalid | Needs clarification
<2-4 sentences, evidence from the current code>

**Recommendation:** Code fix | No changes | Clarify with reviewer
<concrete next step; if a fix, name it briefly>

---

**Reply draft**

```
<short, high-level, clear reply — 1-3 sentences>
```
````

- Reply draft is its own fenced code block, plain text, ready to copy-paste — no quoting of the original comment back
- If the user asks to post: reply to a discussion comment with `gh api repos/<owner>/<repo>/pulls/<pr>/comments/<id>/replies -f body='<text>'`; reply to an issue comment with `gh pr comment <pr> -b '<text>'`
- No preamble or filler unless asked
