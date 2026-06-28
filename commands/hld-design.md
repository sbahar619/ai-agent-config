# HLD only

HLD only — concise architecture doc (what/why, components, flows) under `docs/`. No source edits, commits, or implementation.

**Input**

A goal or path to a plan doc.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed — no source writes until create gate
- HLD only — write and edit architecture docs under `docs/` after approval
- Short — bullets, ~1 page; what/why, components, flows
- Mirror a nearby HLD (`docs/**/design/hld/**` or repo norm)
- Mermaid only when it clarifies; state assumptions when info is missing
- Stay within stated scope
- Must not — source code edits, implementation, git mutations, high-level phased goals without architecture detail, or low-level deliverable detail (ordered steps, API contracts, per-phase tests)
- Authoring — pick sections by relevance; justify include/skip in the doc plan. Usually include: Summary, Goals / Non-goals, Architecture; add when relevant: Data model / APIs, Workflow / Sequence, Rollout / phasing, Failure modes, Security, Observability
- Before each gate reply: doc plan has path under `docs/`; every included/skipped section justified; after create, HLD matches approved doc plan; assumptions stated where info is missing; output matches the template for the current gate — no extra sections

**Gates**

Skip when the user already approved that step or said skip create.

| Step | Prompt | n |
|------|--------|---|
| Doc plan | Happy with this doc plan? (y/n) | Revise; stay here |
| Create | Create this doc? (y/n) | Revise doc plan |
| HLD review | Happy with this HLD? (y/n) | Refactor; re-ask |

**Output**

**Doc plan:**

```
## Goal
<one sentence>

## Doc plan
- Path: docs/...
- Include: <section> — <why>
- Skip: <section> — <why or N/A>

## Phasing
1. **<title>** — <what + why / dependency>
2. ...

## Key decisions · Open questions
- ...

## Next
Happy with this doc plan? (y/n)
```

**After create:**

```
## HLD saved
- Path: docs/...
- Phases: <count + titles>

## Summary
<2–4 bullets: main decisions and scope>

## Next
Happy with this HLD? (y/n)
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Goal in doc plan
