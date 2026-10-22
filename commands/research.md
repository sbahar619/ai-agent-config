# Research only

Research only — investigate with evidence; return one next step. No source edits, commits, or implementation.

**Input**

A question, idea, or problem.

**Rules**

- If scope, codebase context, or constraints are unclear, ask all clarifying questions in one numbered list and wait for answers before proceeding; user may answer by number
- Read-only — no source edits, git mutations, or implementation
- Scope — own evidence and gaps relevant to the question, option tradeoffs, and one recommended next step; do not turn findings into agreed requirements, delivery phases, architecture decisions, or detailed contracts
- Updates — revise only affected findings and recommendations; identify follow-up for another document in the recommended next step without editing that document.
- Sources — use what the question needs: repo (code, history), project docs, web/external docs; cite everything (path:line, command output, URL); label guesses
- Bugs — reproduce or refute first; state root cause only if evidenced
- Existing first — search for overlap, prior attempts, ecosystem solutions (well-known libraries, canonical patterns, community conventions), and simpler options before recommending new work
- Solution ownership — before recommending work in this project, evaluate whether the problem is better solved elsewhere (another service, the caller/frontend, an existing tool, or no code at all); include the alternative in Findings with evidence for or against
- Disconfirm — actively look for reasons not to proceed (duplicate, misfit, already solved, constraint violation, wrong layer)
- Next step — recommend requirements definition before planning when multiple phases, compatibility constraints, or unresolved outcomes warrant a separate agreement; for small clear changes, keep requirements with the plan. Do not generate or approve requirements as part of research.
- Facts vs inference — verified findings cite evidence; keep assumptions, settled decisions, and unresolved questions distinct; a proposed or approved design is not evidence of implementation
- Document references — cite relevant existing sections instead of repeating their contents; use relative paths in the saved file and verify linked files and sections exist
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
**Purpose:** Establish evidence and relevant gaps, compare options, and recommend one next step; requirements agreement, delivery phasing, and solution design are outside this document's scope.

## Issue
<one sentence>

## Findings
- <fact> — <evidence>
- (2–5 bullets; include negatives and alternatives)

## Recommendation
<one next step, such as requirements definition or planning when warranted, or "no action: <why>">

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
