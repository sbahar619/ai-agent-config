---
name: gen-user-example
description: >-
  Translate a technical detail into a concrete end-user scenario.
  Use when a change or feature needs a user-facing explanation or example.
disable-model-invocation: true
---

# Generate User Example

Translate a technical detail into a concrete end-user scenario. No edits,
commits, or implementation.

## Input

A code change, behavior, error path, PR comment, or implementation detail.

## Rules

- If the target is unclear, ask one question — do not guess
- Identify the real end user (developer, cluster admin, API consumer, UI user)
- Describe the scenario from that user's point of view: what they do, what
  happens, what they see
- Focus on observable outcome — CLI output, API response, UI behavior, or
  visible system state; not internal code mechanics
- Include a concrete example the user would touch — manifest snippet, CLI
  command + output, API request/response, or config block (5–15 lines)
- One scenario only; add a second only when distinct user roles differ
- Do not suggest code changes or next steps unless asked

## Output

```
**Who:** <user role>

**Scenario:** <what the user does — 1-2 sentences>

**Example:**
<manifest snippet, CLI command + output, config block, or API call>

**Result:** <what they observe — success, error, or unchanged behavior>

**Why it matters:** <one sentence — user impact or expectation>
```
