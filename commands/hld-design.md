# HLD only

HLD only — concise architecture doc (what/why, components, flows) for a topic or domain. No source edits, commits, or implementation.

**Input**

A goal or path to a plan doc, with optional domain scope.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed, including topic-level architecture for domain work; surface conflicts instead of overriding shared decisions. No source writes until approval.
- HLD only — write and edit architecture docs after approval
- Short — bullets, ~1 page; what/why, components, flows
- Location — save `hld.md` in `docs/plans/<topic>/`, or `docs/plans/<topic>/<domain>/` when the domain is requested or already established; keep shared architecture above phase folders, preserve existing document paths, and show concrete paths in output
- Requirements — read supplied requirements and `requirements.md` in the selected scope and its topic root when present; explain how the architecture satisfies in-scope requirements by ID and surface conflicts for resolution without changing them. A separate requirements file is not mandatory.
- References — link relevant existing document sections instead of repeating their contents; use relative paths in the saved file and verify linked files and sections exist
- Rollout stages — label architectural sequencing as stages, not delivery phases; when a delivery plan exists, map stages to its phases by plan link, number, and title without assuming a one-to-one match. Stage labels do not determine `phase-N` folder names.
- Document state — describe proposed architecture as proposed; approval or saving the HLD does not establish implementation or validation
- Mermaid only when it clarifies; state assumptions when info is missing
- Open questions — use the question + recommendation format below; keep decisions and assumptions separate; if any need user input, wait for answers before asking for approval
- Updates — revise only affected content within the stated scope; identify follow-up for another document in Next without editing that document.
- Must not — source code edits, implementation, git mutations, high-level phased goals without architecture detail, or low-level deliverable detail (ordered steps, API contracts, per-phase tests)
- Authoring — pick sections by relevance; justify include/skip in the doc plan. Usually include: Summary, Goals / Non-goals, Architecture and decisions (choices, rationale, tradeoffs); add when relevant: Data model / APIs (concepts and boundaries only), Workflow / Sequence, Rollout stages, Failure modes, Security, Observability
- Document header — begin the saved HLD with: `**Purpose:** Describe the architecture, components, flows, and design rationale; detailed API contracts, implementation steps, and per-phase tests are outside this document's scope.`
- Before each gate reply: doc plan has a concrete path matching the selected scope; every included/skipped section justified; after approval, HLD matches approved doc plan; assumptions stated where info is missing; output matches the template — no extra sections

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
- Path: <resolved HLD path>
- Include: <section> — <why>
- Skip: <section> — <why or N/A>

## Rollout stages
- **Stage A — <title>** — <what + why / dependency>; delivery: <linked plan phase(s), when defined>
- ...

## Key decisions
1. <settled decision and rationale>

## Assumptions
- <unverified assumption>

## Open questions
1. <concrete unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>

## Next
{follow-up for another document, only when needed}
{if questions need user input: request answers and stop; otherwise: Happy with this doc plan? (y/n)}
```

**After approval (auto-created and saved):**

```
## HLD saved
- Path: <resolved HLD path>
- Rollout stages: <count + titles, when applicable>

## Summary
<2–4 bullets: main decisions and scope>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except Goal in doc plan
