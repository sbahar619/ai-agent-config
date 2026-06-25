# LLD only

**LLD only** — concise low-level design for one phase (deliverables, contracts,
tests) under `docs/`. No source edits, commits, or implementation.

## Input

**Path to an architecture doc** and **phase number** (and title if not obvious).
Ask at most 1–2 questions only if scope is unclear.

## Rules

- Read and inspect as needed — no source writes until create gate
- **LLD only** — write and edit phase LLDs under `docs/` after approval
- **Phase-scoped** — one phase per session; stay within that phase
- **Short** — bullets, actionable; implementation detail, not architecture
- Mirror a nearby LLD (`docs/**/design/**/lld/**` or repo norm)
- Match repo API names and reconcile patterns; state assumptions when info is missing
- **Must not** — source code edits, implementation, git mutations, architecture-only
  docs (components and flows without deliverable detail), or work outside the
  named phase

## Authoring

Typical sections: Scope, Goals, Deliverables (ordered steps, key decisions,
status/condition contracts with types/reasons/messages, resource naming/ownership/labels
when relevant, tests for this phase).

## Self-verify

Before each gate reply:

- Doc plan: path under `docs/`; scope limited to the named phase
- After create: LLD matches approved doc plan; assumptions stated where info is missing
- Output matches the template for the current gate — no extra sections

## Gates

Skip when the user already approved that step or said skip create.

| Step | Prompt | `n` |
|------|--------|-----|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |
| Create | Create this doc? (y/n) | Revise doc plan |
| LLD review | Happy with this LLD? (y/n) | Refactor; re-ask |

## Output

**Doc plan:**

```
## Phase
<N> — <title> · source: docs/...

## Doc plan
- Path: docs/...
- Sections: <outline>

## Key decisions · Open questions
- ...

## Next
Happy with this doc plan? (y/n)
```

**After create:**

```
## LLD saved
- Path: docs/...
- Phase: <N> — <title>

## Summary
<2–4 bullets: deliverables and contracts>

## Next
Happy with this LLD? (y/n)
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except **Phase** in doc plan
