# HLD only

HLD only — concise architecture doc (what/why, components, flows) co-located with the plan. No source edits, commits, or implementation.

**Input**

A goal or path to a plan doc.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed — no source writes until approval
- HLD only — write and edit architecture docs as `docs/plans/<topic>/hld.md` after approval
- Short — bullets, ~1 page; what/why, components, flows
- Co-locate with the plan — save as `docs/plans/<topic>/hld.md`
- Mermaid only when it clarifies; state assumptions when info is missing
- Open questions — number each; if any need user input, present them and wait for answers before asking for approval
- Stay within stated scope
- Must not — source code edits, implementation, git mutations, high-level phased goals without architecture detail, or low-level deliverable detail (ordered steps, API contracts, per-phase tests)
- Authoring — pick sections by relevance; justify include/skip in the doc plan. Usually include: Summary, Goals / Non-goals, Architecture; add when relevant: Data model / APIs, Workflow / Sequence, Rollout / phasing, Failure modes, Security, Observability
- Before each gate reply: doc plan has path as `docs/plans/<topic>/hld.md`; every included/skipped section justified; after approval, HLD matches approved doc plan; assumptions stated where info is missing; output matches the template — no extra sections

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |

**Output**

**Doc plan:**

```
## Goal
<one sentence>

## Doc plan
- Path: docs/plans/<topic>/hld.md
- Include: <section> — <why>
- Skip: <section> — <why or N/A>

## Phasing
1. **<title>** — <what + why / dependency>
2. ...

## Key decisions · Open questions
1. ...

## Next
{if open questions: ask them and wait for answers before approval}
Happy with this doc plan? (y/n)
```

**After approval (auto-created and saved):**

```
## HLD saved
- Path: docs/plans/<topic>/hld.md
- Phases: <count + titles>

## Summary
<2–4 bullets: main decisions and scope>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Goal in doc plan
