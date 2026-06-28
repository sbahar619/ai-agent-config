# Summarize

Ultra-short decision brief: scope, what matters, whether action is needed. No edits, commits, or implementation.

**Input**

Whatever the user names in this turn: diff, PR, plan, error, selection, path, agent output, or question.

**Rules**

- If the target is unclear, ask one question before proceeding
- Read and inspect as needed — no writes, no git mutations
- Decision-first — always land on Action; this is not a neutral recap
- Cite repo evidence as `path:line`; mark inferred references as `[inferred]`
- Action guidance: None = no meaningful risk or opportunity; Optional = low-stakes improvement available; Required = risk, breakage, or blocking issue present
- Must not: long summaries, multi-paragraph prose, findings lists, or implementation
- Before replying: scope matches what the user pointed at; Action level matches the Action guidance above; if Action is Required or Optional, Why and Next are present and concrete

**Output**

```
Scope: <what this is about>

Summary: <what matters>

Action: None | Optional | Required

Why: <one line — omit when Action is None>

Next: <one concrete step — omit when Action is None>
```

No preamble, wrap-up, or filler unless asked. Omit Why and Next when Action is None.
