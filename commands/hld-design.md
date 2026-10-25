# HLD only

HLD only — concise architecture doc (what/why, components, flows) for a topic or domain. No source edits, commits, or implementation.

**Input**

A goal or path to a plan doc, with optional domain scope.

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read and inspect as needed, including topic-level architecture for domain work; surface conflicts instead of overriding shared decisions.
- Draft for review — write the full HLD to the selected path before requesting content approval; show the file link and a brief overview in chat, marking the draft as awaiting review. Keep gate prompts and review commentary outside the file.
- Reviewability — keep goals, scope, consequential decisions, and tradeoffs easy to scan; use clearly titled sections for necessary supporting detail. Aim for roughly one page, preserving essential constraints, failure cases, and rationale; remove repetition before proposing independently reviewable scopes.
- Location — save `hld.md` in `docs/plans/<topic>/`, or `docs/plans/<topic>/<domain>/` when the domain is requested or already established; keep shared architecture above phase folders, preserve existing document paths, and show concrete paths in output
- Requirements — read supplied requirements and `requirements.md` in the selected scope and its topic root when present; explain how the architecture satisfies in-scope requirements by ID and surface conflicts for resolution without changing them. A separate requirements file is not mandatory.
- References — include a References line in the saved HLD linking its delivery plan and, for domain work, applicable topic-level HLD sections; retain relevant requirement links. Use relative paths and verify targets instead of copying content; omit absent sources without requiring new documents.
- Rollout stages — label architectural sequencing as stages, not delivery phases; when a delivery plan exists, map stages to its phases by plan link, number, and title without assuming a one-to-one match. Stage labels do not determine `phase-N` folder names.
- Document state — approval or saving the HLD does not establish implementation or validation
- Work status — distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Mermaid only when it clarifies
- Open questions — use the question + recommendation format below; keep decisions and assumptions separate; if any need user input, wait for answers before asking for approval
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only affected content within the stated scope. Identify follow-up for another document in the chat overview without editing that document.
- Must not — source code edits, implementation, git mutations, high-level phased goals without architecture detail, or low-level deliverable detail (ordered steps, API contracts, per-phase tests)
- Authoring — add sections only when they support a decision or prevent a likely misunderstanding: Data model / APIs (concepts and boundaries only), Workflow / Sequence, Rollout stages, Failure modes, Security, Observability
- Before replying: the linked draft is complete and matches the selected scope; assumptions are stated where info is missing; chat stays within the output template

**Gates**

| Step | Prompt | n |
|------|--------|---|
| HLD | Happy with this HLD? (y/n) | Revise the draft per feedback; re-ask |

**Output**

**Chat:**

```
**Draft:** [hld.md](<resolved path>) — awaiting review
- <consequential architecture choice, tradeoff, or risk>
```

- At most three short overview bullets; on revisions, use them for changed decisions, constraints, or open questions instead
- Request answers when user input is needed; otherwise show the HLD gate
- Do not repeat the full document in chat unless asked

**File:**

```
**Purpose:** Describe the architecture, components, flows, and design rationale; detailed API contracts, implementation steps, and per-phase tests are outside this document's scope.

**References:** <relative links to relevant parent documents and sections>

## Goal and scope
<intended outcome, boundaries, and non-goals>

## Architecture and decisions
<components, flows, choices, rationale, and tradeoffs>

<additional sections warranted by the scope>

## Assumptions
- <unverified assumption>

## Open questions
1. <concrete unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

**After approval:**

```
## HLD approved
- Path: <resolved HLD path>
```

- No preamble, summary wrap-up, or filler unless asked
- Omit empty sections except `Goal and scope` and `Architecture and decisions`; omit References when no sources apply
