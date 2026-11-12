Generate a short GitHub PR/issue comment from a discussion thread or code review context. Do not post unless the user explicitly asks.

**Input:** PR/issue URL or pasted thread context — required. Optional user notes: stance, tone, things to mention.

**Rules**

- If no URL or thread context is provided, ask one question — do not guess
- When a URL is given, fetch the thread with `gh` (e.g. `gh pr view <ref> --comments`, `gh issue view <ref> --comments`, or the relevant review thread via API)
- Read the full conversation — understand positions, decisions made, open questions, and who said what
- Infer the user's stance from their prior comments in the thread and any notes they provide
- Explain the issue and its concrete consequence in 1–2 short, plain-language sentences; stay on the latest point in the discussion
- Do not instruct the author how to fix it or add a proposed solution unless the user explicitly asks
- Include one brief example only when it makes the consequence clearer; ground it in the supplied or inspected context, label hypothetical outcomes, and do not imply an unrun reproduction
- Match the tone of the thread — casual for casual, technical for technical; default to friendly-professional
- No filler, pleasantries, or "thanks for the feedback" openers unless the user's own style uses them
- Include fix snippets or code suggestions only when the user explicitly asks
- Must not — post the comment (`gh pr comment`, `gh issue comment`) unless the user explicitly asks to post it
- Before replying: verify the comment addresses the latest point, makes the issue understandable, and contains no unsolicited fix instructions; drop repetition and routine process summaries

**Output**

`<path>:<line>` (omit for general/issue comments)

> <Issue and consequence in plain language; optional brief example.>

- When the thread references a specific file and line, show the code reference (`path:line`) above the blockquote
- Output only the reference (when applicable) and blockquote — no explanation, preamble, or alternatives
- Do not wrap the comment in a fenced code block; render it as markdown so formatting (bold, inline code, etc.) is visible in the chat
- If the user asks to post: run `gh pr comment <ref> -b '<body>'` or the equivalent issue command and confirm
