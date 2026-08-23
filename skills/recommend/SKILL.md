---
name: recommend
description: >-
  Read-only inspect and recommend with findings and one concrete next step.
  Use when the task requires evaluation and a recommendation without making
  changes.
disable-model-invocation: true
---

# Recommend

Inspect and recommend — read-only; no unreviewed side effects.

## Rules

- Use read-only tools freely; ask before any action that modifies state
- If a request requires implementation, decline and restate what you can do
- Cite evidence inline; flag guesses with "likely" or "unclear"

## Output

```
**Issue:** one sentence restating the question or goal

**Findings:** facts, options, or tradeoffs — 3–5 bullets max

**Recommendation:** one concrete next step, 1–2 sentences max
```

- Omit empty sections except Issue
