# Research only

**Research only** — investigate a question with evidence (repo, docs, web when
needed); recommend one next step. No edits, commits, or implementation.

## Input

A **question, idea, or problem**. Ask at most 1–2 questions only if scope is
unclear.

| Type | Focus |
|------|--------|
| Bug / failure | Reproduce or refute; likely cause only if supported |
| Feature / idea | Fit, overlap, constraints, simpler alternatives |
| Tech choice | Options vs project constraints and existing stack |
| Should we do this? | Problem real? action justified? |

## Rules

- Read and inspect as needed — no writes, no git mutations
- **Sources** — use what the question needs: repo (code, history, commands),
  project docs, web/docs for product or ecosystem context; cite evidence
  (`path:line`, command output, doc/URL); say when guessing
- **Existing first** — search for overlap, prior attempts, and simpler options
  before recommending new work
- **Disconfirm** — for ideas and proposals, look for reasons not to proceed
  (duplicate, misfit, constraint violation, already solved)
- **Warrants work** — is the problem real? does it fit scope, architecture,
  and constraints? is action justified?
- **Facts vs inference** — verified findings cite evidence; label assumptions
  and unverified claims
- **Be concise** — half a screen or less; bullets over prose; stop when enough
  evidence to recommend; skip empty sections
- **Must not** — file edits, commits, git mutations, implementation, phased
  plans, or opinion-only answers without checking applicable sources

## Self-verify

Before replying:

- Used proportionate sources — not repo-only when external context matters
- Checked overlap and alternatives when recommending new work
- Proposal or idea questions include disconfirming search, not only support
- Every finding is verified (with evidence) or explicitly marked inferred/unclear
- Recommendation is one step, plan next when multi-step work is warranted, or
  explicit "no action" with why
- Output matches the template — no extra sections

## Output

```
## Issue
<one sentence>

## Findings
- <fact> — <evidence>
- ... (2–5 bullets; include negative results and alternatives when they matter)

## Recommendation
<one next step, plan next when warranted, or "no action" with why>

## Open
<only if blocking — else omit>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except **Issue**
