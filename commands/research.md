# Research only

Research only — investigate with evidence; return one next step. No source edits, commits, or implementation.

**Input**

A question, idea, or problem.

**Rules**

- If scope, codebase context, or constraints are unclear, ask all clarifying questions in one numbered list and wait for answers before proceeding; user may answer by number
- Read-only — no source edits, git mutations, or implementation
- Sources — use what the question needs: repo (code, history), project docs, web/external docs; cite everything (path:line, command output, URL); label guesses
- Bugs — reproduce or refute first; state root cause only if evidenced
- Existing first — search for overlap, prior attempts, ecosystem solutions (well-known libraries, canonical patterns, community conventions), and simpler options before recommending new work
- Solution ownership — before recommending work in this project, evaluate whether the problem is better solved elsewhere (another service, the caller/frontend, an existing tool, or no code at all); include the alternative in Findings with evidence for or against
- Disconfirm — actively look for reasons not to proceed (duplicate, misfit, already solved, constraint violation, wrong layer)
- Facts vs inference — verified findings cite evidence; assumptions are labeled explicitly
- Concise — half a screen or less; bullets over prose; stop when there's enough to recommend; omit empty sections
- Render — output findings as rendered markdown in chat; research body matches what is written to the file (gate prompt is chat-only)
- Open blocks save — do not prompt the Save gate while the Open section has unanswered items; wait for user responses, update findings if answers change anything, then proceed to the gate
- Persist — after the user approves the Save gate, write to `docs/plans/<topic>/research.md`; saved file uses the same body shown in chat

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Save | Save findings? (topic name to save, or n to skip) | Skip; no file written |

**Output**

```
**Purpose:** Evaluate the question using evidence, compare options, and recommend one next step; detailed architecture and implementation design are outside this document's scope.

## Issue
<one sentence>

## Findings
- <fact> — <evidence>
- (2–5 bullets; include negatives and alternatives)

## Recommendation
<one next step, "plan next" if multi-step, or "no action: <why>">

## Open
1. <blocking unknown — omit section if none>
```

No preamble, filler, or closing summary.
Omit empty sections except Issue and Findings.

**After user approves the Save gate:**

```
## Research saved
- Path: docs/plans/<topic>/research.md
```
