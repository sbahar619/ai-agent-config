---
name: summarize
description: >-
  Ultra-short decision brief with action level. Use when the task needs a
  concise summary of a diff, PR, plan, error, or agent output.
disable-model-invocation: true
---

# Summarize

Ultra-short decision brief. No edits, commits, or implementation.

## Input

Diff, PR, plan, error, selection, path, agent output, or question.

## Rules

- Unclear target → ask one question first
- Read/inspect only — no writes, no git mutations
- Decision-first: always land on an Action level
- Cite evidence as path:line; mark inferred as [inferred]
- Action levels: None = no risk/opportunity; Optional = low-stakes improvement;
  Required = risk, breakage, or blocker

## Output

```
Summary: <what matters>
Action: None | Optional | Required
Why: <one line; omit if None>
Next: <one concrete step; omit if None>
```
