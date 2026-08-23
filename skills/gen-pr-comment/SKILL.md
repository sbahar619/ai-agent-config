---
name: gen-pr-comment
description: >-
  Draft a short GitHub PR or issue reply from a discussion thread.
  Use when composing a response to a PR or issue conversation.
disable-model-invocation: true
---

# Generate PR/Issue Comment

Draft a short GitHub PR/issue reply. Do not post unless explicitly asked.

## Input

PR/issue URL or pasted thread context — required.
Optional user notes: stance, tone, things to mention.

## Rules

- If no URL or thread context is provided, ask — do not guess
- When a URL is given, fetch the thread with `gh`
- Read the full conversation — understand positions, decisions, open questions
- Infer the user's stance from their prior comments and any notes provided
- Reply is: direct, concise (1–4 sentences), on-topic, moves discussion forward
- Match thread tone — casual for casual, technical for technical; default
  friendly-professional
- No filler or "thanks for the feedback" openers unless the user's style uses them
- Include code snippets only when asked or clearly needed
- Must not — post the comment unless explicitly asked
- Before replying: comment addresses the latest message; nothing restates what
  was already agreed

## Output

`<path>:<line>` (omit for general/issue comments)

> <the comment text, rendered markdown>

- When the thread references a specific file and line, show the code reference above
  the blockquote
- Do not wrap the comment in a fenced code block
- If asked to post: run `gh pr comment` or equivalent and confirm
