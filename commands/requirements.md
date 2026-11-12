# Requirements only

Define concise, reviewable requirements — required outcomes, constraints, and success criteria. No architecture, implementation, or git mutations.

**Input**

A research or requirements document path, pasted findings, or a direct goal with constraints; no prior command or session required.

**Rules**

- Read supplied sources and relevant project context; ask numbered clarifying questions when scope or necessary requirements are unclear, and wait for answers before finalizing
- Inspect existing topic documents first; update an existing requirements file rather than create a competing source of truth
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Domain scope — read topic-level requirements when present; reference inherited obligations by ID instead of copying or overriding them
- Reviewability — use plain-language bullets for obligations, with only enough context to judge them. Aim for roughly one page; preserve essential constraints and uncertainty, and split independently reviewable scopes only when needed. Do not add a summary that repeats the requirements.
- Group functional behavior under Functional requirements and quality attributes or cross-cutting constraints under Non-functional requirements; classify by the obligation, not its topic alone. Do not invent NFRs or thresholds to fill a section.
- Give new requirements stable IDs (`FR01`, `FR02`, ... and `NFR01`, `NFR02`, ...), numbered independently. Preserve existing IDs and linked anchors unless migration is explicitly requested; update affected references when migrating and never reuse retired IDs.
- Each requirement states one necessary, verifiable obligation. Add a separate success criterion only when the wording does not already make success observable; unresolved criteria belong in Open questions, not invented thresholds.
- Trace requirements to supplied goals, research findings, or explicit user constraints; label assumptions and seek agreement on inferred obligations
- Record fixed constraints and compatibility boundaries once, in the applicable requirement; preserve mandated technical constraints without inventing architecture choices
- Keep success criteria at the behavior or outcome level; detailed API contracts, test code, delivery phases, and implementation tasks belong elsewhere
- Use relative links to existing source documents and sections in the saved file; verify targets and avoid repeating research findings
- Keep assumptions and open questions separate from requirements; each question ends in `?` with a recommendation and rationale; resolve questions requiring user input before the approval gate
- Approval of research findings is not approval of requirements; writing or approving requirements does not establish implementation or validation
- Work status — when describing existing behavior, distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Draft for review — write the full requirements to `<scope-dir>/requirements.md` before requesting content approval; show the file link and a brief overview in chat, marking the draft as awaiting review. Keep gate prompts and review commentary outside the file.
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only affected content in the requested requirements document. Identify follow-up for another document outside the requirements body without editing that document.
- Before replying: check necessity, clarity, consistency, verifiability, source traceability, FR/NFR grouping, stable IDs, compatibility, and non-goals; remove duplicated obligations and unintended design decisions

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Requirements | Happy with these requirements? (y/n) | Revise per feedback; re-ask |

**Output**

**Chat:**

```
Draft ready for review: [requirements.md](<resolved path>)
<One short sentence about the outcome or decision needing attention.>
```

- Keep chat to the draft links, one short outcome sentence, and the necessary question or existing gate; usually under 60 words. No sectioned recap or rationale unless requested
- Surface blockers and decision-changing risks immediately; the length target must not hide them
- Follow-ups answer only the latest request; offer explanation only when no question or gate is already pending
- Request answers when user input is needed; otherwise show the Requirements gate
- Do not repeat the full document in chat unless asked

**File:**

```
# <topic> requirements

**Sources:** <relevant research, supplied goal, or explicit user constraints>

## Goal
<intended outcome and included users or behavior, in one sentence>

## Functional requirements

- FR01: <one required behavior with an observable success condition>

## Non-functional requirements

- NFR01 — <quality or constraint>: <one verifiable obligation>

## Out of scope
- <explicit exclusion>

## Assumptions
- <unverified assumption>

## Open questions
1. <concrete unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

- Keep Goal, Functional requirements, and Non-functional requirements; omit other empty sections. If a category has no identified requirements, say so briefly; keep unresolved obligations in Open questions.
- Repeat requirement bullets only as needed. Put shared sources once at the top; add a source or success-criterion sub-bullet only when needed to disambiguate that requirement. Preserve existing IDs and linked anchors on updates.
- No preamble, filler, or closing summary

**After approval:**

```
## Requirements approved
- Path: <resolved requirements path>
```
