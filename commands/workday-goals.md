# Workday goals only

Workday goals only — assess workspace reports, suggest new goals where warranted, and draft paste-ready individual goals (new or in-progress updates). No edits outside the reply, commits, or Workday API access.

**Input**

| Input | Required |
|-------|----------|
| Request | No — new, update, retire/revise; omit to assess and suggest |
| My notes | No — bullets, progress, or rough draft |

For updates, paste the existing goal text or name it from workspace exports.

**Rules**

- Ask at most 1–2 questions only if reports and notes are too thin to suggest honestly
- Read and inspect as needed — no writes, no git mutations
- Browse the workspace for all report exports — goals, Quarterly Connection, talent assessments, written examples, goal-writing guidelines — newest first; do not assume fixed paths or filenames
- Recent reports matter most; older exports are background only
- Suggest — compare active, in-progress, and recently completed goals against latest QC priorities, accomplishments, and manager feedback; propose only where reports show a gap; respect workspace active-goal count guidance (typically 1–3)
- Draft — paste-ready text; user submits in Workday; follow workspace guidelines and match recent goal-export structure and voice
- New — outcome-focused; no duplicate of an active goal in exports
- In-progress update — keep existing goal text unless user asks to revise; refresh progress note from notes and recent reports
- Ground every suggestion in report evidence; do not invent projects, certs, or metrics
- Must not — Workday API, credentials, Quarterly Connection answers, or fabricating facts not supported by reports or user notes
- Before replying: recent goal exports and Quarterly Connection reports reviewed before suggesting; each suggestion tied to report evidence; output matches template — no extra sections

**Output**

```
## Assessment
<active goals, recent QC priorities, gaps — bullets>

## Suggested goals
1. **<title>** — <why, tied to a specific report or note>
2. ...

## Goal
<title line>
• Specific: ...
• Measurable: ...
• Achievable: ...
• Relevant: ...
• Time-bound: ...
Progress note:
<only when initial progress exists; else omit>

## Goal update
<goal title — unchanged unless revision requested>
Progress note:
<paste-ready update>

## Notes
<optional: goals to retire, facts still needed>
```

- Include Assessment and Suggested goals unless the user asked for a single goal update only
- Expand a suggestion into Goal when the user picks one or names it in Request
- No preamble, summary wrap-up, or filler unless asked
