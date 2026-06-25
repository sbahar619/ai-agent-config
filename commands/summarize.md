# Summarize

**Summarize only** — ultra-short decision brief: scope, what matters, whether action is needed. No edits, commits, or implementation.

## Input

Whatever the user names in this turn: diff, PR, plan, error, selection, path, agent output, or question. Ask at most 1 question only if the target is unclear.

## Rules

- Read and inspect as needed — no writes, no git mutations
- **Be brief** — ≤8 non-blank lines; one line per section; no bullets unless unavoidable
- **Decision-first** — always land on **Action**; this is not a neutral recap
- Cite repo evidence with `path:line` when referencing code; say when guessing
- **Must not** — long summaries, multi-paragraph prose, findings lists, or implementation

## Self-verify

Before replying:

- Confirm **Scope** matches what the user pointed at
- **Action** follows from **Summary** — if Required, **Next** is concrete; if None, omit **Why** and **Next**

## Output

Use this structure. One line per section; **blank line between sections**.

```
Scope: <what this is about>

Summary: <what matters>

Action: None | Optional | Required

Why: <one line — omit when Action is None>

Next: <one concrete step — omit when Action is None>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except **Scope**, **Summary**, and **Action**
