# LLD only

LLD only — concise low-level design (deliverables, contracts, tests) co-located with the plan. No source edits, commits, or implementation.

**Input**

Path to an architecture doc and optional phase number (and title if not obvious).

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed — no source writes until approval
- LLD only — write and edit LLDs as `docs/plans/<topic>/lld.md` (or `lld-phase-N.md` for a single phase) after approval
- Scope — covers all phases by default (`lld.md`); when the user explicitly targets a single phase, scope to that phase only (`lld-phase-N.md`)
- Short — bullets, actionable; implementation detail, not architecture
- Co-locate with the plan — save as `docs/plans/<topic>/lld.md` or `docs/plans/<topic>/lld-phase-N.md`
- Match repo API names and reconcile patterns; state assumptions when info is missing
- Before proposing a new function or type, check the repo for existing symbols that serve a similar purpose; prefer extending (optional param, overload, wrapper) over creating a parallel symbol — per coding-standards
- Must not — source code edits, implementation, git mutations, architecture-only docs (components and flows without deliverable detail), or work outside the stated scope
- Authoring — typical sections: Scope, Goals, Deliverables (ordered steps, key decisions, status/condition contracts with types/reasons/messages, resource naming/ownership/labels when relevant, tests)
- Before each gate reply: doc plan has path as `docs/plans/<topic>/lld.md` or `lld-phase-N.md`; scope matches user request; after approval, LLD matches approved doc plan; assumptions stated where info is missing; output matches the template — no extra sections

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |

**Output**

**Doc plan:**

```
## Phase
<N> — <title> · source: docs/plans/<topic>/hld.md

## Doc plan
- Path: docs/plans/<topic>/lld.md (or lld-phase-N.md)
- Sections: <outline>

## Key decisions · Open questions
- ...

## Next
Happy with this doc plan? (y/n)
```

**After approval (auto-created and saved):**

```
## LLD saved
- Path: docs/plans/<topic>/lld.md (or lld-phase-N.md)
- Phase: <N> — <title>

## Summary
<2–4 bullets: deliverables and contracts>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Phase in doc plan
