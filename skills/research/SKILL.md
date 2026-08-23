---
name: research
description: >-
  Evidence-based research returning findings and one next step. Use when the
  task requires investigation with sources before acting.
disable-model-invocation: true
---

# Research

Investigate with evidence; return one next step. No edits, commits, or
implementation.

## Input

A question, idea, or problem.

## Rules

- If scope or constraints are unclear, ask all clarifying questions in one
  numbered list and wait for answers
- Read-only — no file writes, git mutations, or implementation
- Sources — use what the question needs: repo (code, history), project docs,
  web/external docs; cite everything (path:line, command output, URL); label guesses
- Bugs — reproduce or refute first; state root cause only if evidenced
- Existing first — search for overlap, prior attempts, and simpler options before
  recommending new work
- Disconfirm — actively look for reasons not to proceed (duplicate, misfit,
  already solved, constraint violation)
- Facts vs inference — verified findings cite evidence; assumptions labeled
- Concise — half a screen or less; bullets over prose; stop when there's enough
  to recommend

## Output

```
## Issue
<one sentence>

## Findings
- <fact> — <evidence>
- (2–5 bullets; include negatives and alternatives)

## Recommendation
<one next step, "plan next" if multi-step, or "no action: <why>">

## Open
<blocking unknowns only — omit if none>
```
