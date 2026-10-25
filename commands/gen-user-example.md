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
- Include a concrete example the user would touch — manifest snippet, CLI command + output, API request/response, or config block; use the fewest lines needed, usually no more than 10
- One scenario only; add a second only when distinct user roles experience it differently
- Do not suggest code changes, tests, or next steps unless the user asks
- **Code scope only:** cite the file, lines, and causal logic in one short sentence connecting the code to the observable result
- Before replying: the scenario names a real user action and an observable result, not internal function behavior

**Output**

```
**Scenario:** <user role, action, and observable result — 1–2 sentences>

**Example:**
<manifest snippet, CLI command + output, config block, or API call — the artifact the user would write or see>

**Code trace:** <file#lines — the code path that produces this result, and why>
```

- No preamble or filler
- Do not repeat the scenario's outcome in separate Result or Why it matters sections
- Example block uses a fenced code block with the appropriate language (yaml, bash, json, etc.)
- Omit **Code trace** when scope is general
