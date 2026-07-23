Generate a short GitHub PR/issue comment from a discussion thread or code review context. Do not post unless the user explicitly asks.

**Input:** PR/issue URL or pasted thread context — required. Optional user notes: stance, tone, things to mention.

**Rules**

- If no URL or thread context is provided, ask one question — do not guess
- When a URL is given, fetch the thread with `gh` (e.g. `gh pr view <ref> --comments`, `gh issue view <ref> --comments`, or the relevant review thread via API)
- Read the full conversation — understand positions, decisions made, open questions, and who said what
- Infer the user's stance from their prior comments in the thread and any notes they provide
- Generate a reply that is: direct, concise (1–4 sentences), on-topic, and moves the discussion forward
- Match the tone of the thread — casual for casual, technical for technical; default to friendly-professional
- No filler, pleasantries, or "thanks for the feedback" openers unless the user's own style uses them
- Include code snippets or suggestions only when the user asks or the reply clearly needs one
- Must not — post the comment (`gh pr comment`, `gh issue comment`) unless the user explicitly asks to post it
- Before replying: verify the generated comment addresses the latest message in the thread; drop anything that restates what was already agreed upon

**Output**

```
<the comment text, ready to copy-paste or post>
```

- Output only the fenced block — no explanation, preamble, or alternatives
- If the user asks to post: run `gh pr comment <ref> -b '<body>'` or the equivalent issue command and confirm
