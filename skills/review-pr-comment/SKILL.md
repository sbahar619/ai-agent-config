---
name: review-pr-comment
description: >-
  Validate a GitHub PR review comment against current code and draft a reply.
  Use when evaluating whether a reviewer's comment is correct and crafting a
  response.
disable-model-invocation: true
---

# Review PR Comment

Review a single GitHub PR review comment for correctness against the current
code, then recommend next steps and draft a reply. Do not post unless explicitly
asked.

## Input

PR review comment URL — required (e.g. `.../pull/123#discussion_r456`).

## Rules

- If no comment URL is given, ask — do not guess
- Parse owner, repo, PR number, and comment id/type from the URL
- Fetch the comment via `gh api`
- State the reviewer's objective before judging — what is being claimed or requested
- Verify against the current code, not just the comment's `diff_hunk`
- Do not guess — say when referenced code or context can't be found
- Judge correctness on evidence: valid, partially valid, invalid, or needs
  clarification
- Must not — post the reply, edit code, or commit unless explicitly asked
- Before replying: recommendation matches verdict; reply doesn't restate the
  reviewer's own comment

## Output

````
## Comment review · <path>#Lstart-Lend
<comment-url>

**Reviewer's point:** <one-line restatement>

**Verdict:** Valid | Partially valid | Invalid | Needs clarification

<2-4 sentences, evidence from the current code>

**Recommendation:** Code fix | No changes | Clarify with reviewer

<concrete next step>

---

**Reply draft**

```
<short, high-level, clear reply — 1-3 sentences>
```
````

- Reply draft is a fenced code block, plain text, ready to copy-paste
- If asked to post: use `gh api` to reply
