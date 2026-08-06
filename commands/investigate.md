Trace a reported issue to root cause and propose solutions. Do not modify code.

## Input
- Issue description, error message, stack trace, log excerpt, or link, given in this turn.

## Rules
- Read-only: never edit, create, or delete files.
- Never implement or apply a fix — proposal only, not action.
- State root cause separately from symptom; do not conflate them.
- Note causes considered and ruled out, one line each.
- Rank solutions by tradeoff (effort/risk/scope); don't silently pick one unless only one is reasonable.
- Before replying: confirm every claim in Root cause and Evidence traces to the input or files reachable from it — no speculation presented as fact.

## Gates
| Step | Prompt | n |
|------|--------|---|
| 1 | Reproduction path or sufficient evidence (logs/trace/diff) is available | 1 |
| 2 | Root cause is separable from symptom, with supporting evidence | 1 |
| 3 | Confidence is medium/low → state competing hypotheses instead of asserting one | 1 |

If a gate fails, stop and state what's missing instead of proceeding.

## Output
Render as formatted markdown — do not wrap in a code fence.

```
**Issue:** <one line>

**Root cause:** <one line>
<2-4 line mechanism, not narrative>

**Evidence:**
- <file:line / log / commit ref>

**Confidence:** high | medium | low — <why>

**Suggested solutions:**
1. <option> — <tradeoff>
2. <option> — <tradeoff>
```
- Omit Evidence bullets with no traceable source.
- Number solutions in ranked order; cap at 3.
