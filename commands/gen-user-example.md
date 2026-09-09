Translate a technical detail into a concrete end-user scenario. No edits, commits, or implementation.

**Input**

A code change, behavior, error path, PR comment, or implementation detail — from this turn or the current conversation context.

**Scope**

Determine scope from the input:

- **code** — input is a code change, diff, PR review finding, or references specific source lines
- **general** — everything else (feature description, error message, config behavior)

**Rules**

- If the target is unclear, ask one question — do not guess
- Identify the real end user (developer, cluster admin, API consumer, UI user) from context; state who
- Describe the scenario from that user's point of view: what they do, what happens, what they see
- Focus on observable outcome — CLI output, API response, UI behavior, or visible system state; not internal code mechanics
- Include a concrete example the user would touch — manifest snippet, CLI command + output, API request/response, or config block; keep it short (5–15 lines)
- One scenario only; add a second only when distinct user roles experience it differently
- Do not suggest code changes, tests, or next steps unless the user asks
- **Code scope only:** trace the example back to the code — identify the file, lines, and logic that produce the described result; show the causal path from code to observable outcome
- Before replying: the scenario names a real user action and an observable result, not internal function behavior

**Output**

```
**Who:** <user role>

**Scenario:** <what the user does — 1-2 sentences>

**Example:**
<manifest snippet, CLI command + output, config block, or API call — the artifact the user would write or see>

**Result:** <what they observe — success, error, or unchanged behavior>

**Code trace:** <file#lines — the code path that produces this result, and why>

**Why it matters:** <one sentence — user impact or expectation>
```

- No preamble or filler
- Example block uses a fenced code block with the appropriate language (yaml, bash, json, etc.)
- Omit **Code trace** when scope is general
