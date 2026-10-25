# Requirements only

Define concise, reviewable requirements — required outcomes, constraints, and success criteria. No architecture, implementation, or git mutations.

**Input**

A research or requirements document path, pasted findings, or a direct goal with constraints; no prior command or session required.

**Rules**

- Read supplied sources and relevant project context; ask numbered clarifying questions when scope or necessary requirements are unclear, and wait for answers before finalizing
- Inspect existing topic documents first; update an existing requirements file rather than create a competing source of truth
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Domain scope — read topic-level requirements when present; reference inherited obligations by ID instead of copying or overriding them
- Reviewability — keep outcomes, scope, and compatibility easy to scan; include only obligations and context needed to judge them. Aim for roughly one page, preserving necessary constraints and success criteria; remove repetition before proposing independently reviewable scopes.
- Give each requirement a stable ID (`R01`, `R02`, ...); preserve existing IDs on updates and never reuse retired IDs
- Each requirement states one necessary, verifiable obligation with an observable success criterion; avoid vague terms and invented thresholds
- Trace requirements to supplied goals, research findings, or explicit user constraints; label assumptions and seek agreement on inferred obligations
- Record fixed constraints and compatibility boundaries; preserve explicitly mandated technical constraints without inventing architecture choices
- Keep success criteria at the behavior or outcome level; detailed API contracts, test code, delivery phases, and implementation tasks belong elsewhere
- Use relative links to existing source documents and sections in the saved file; verify targets and avoid repeating research findings
- Keep assumptions and open questions separate from requirements; each question ends in `?` with a recommendation and rationale; resolve questions requiring user input before the approval gate
- Approval of research findings is not approval of requirements; writing or approving requirements does not establish implementation or validation
- Work status — when describing existing behavior, distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Draft for review — write the full requirements to `<scope-dir>/requirements.md` before requesting content approval; show the file link and a brief overview in chat, marking the draft as awaiting review. Keep gate prompts and review commentary outside the file.
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only affected content in the requested requirements document. Identify follow-up for another document outside the requirements body without editing that document.
- Before replying: check necessity, clarity, consistency, verifiability, source traceability, stable IDs, compatibility, and non-goals; remove duplication and unintended design decisions

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Requirements | Happy with these requirements? (y/n) | Revise per feedback; re-ask |

**Output**

**Chat:**

```
**Draft:** [requirements.md](<resolved path>) — awaiting review
- <required outcome or consequential constraint>
```

- At most three short overview bullets; on revisions, use them for changed IDs, obligations, scope, or open questions instead
- Request answers when user input is needed; otherwise show the Requirements gate
- Do not repeat the full document in chat unless asked

**File:**

```
**Purpose:** Define required outcomes, constraints, and success criteria; architecture, delivery phasing, and implementation details are outside this document's scope.

## Goal
<one sentence>

## Scope
- In scope: <included behavior or users>
- Non-goals: <explicit exclusions>

## Requirements

### R01
- Requirement: <one required behavior or outcome>
- Success criterion: <observable condition demonstrating satisfaction>
- Source: <research section, supplied goal, or explicit user constraint>

### R02
...

## Constraints and compatibility
- <fixed boundary or existing behavior to preserve; avoid repeating numbered requirements>

## Assumptions
- <unverified assumption>

## Open questions
1. <concrete unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

- Omit empty sections except Goal, Scope, and Requirements; include only the requirement IDs needed
- No preamble, filler, or closing summary

**After approval:**

```
## Requirements approved
- Path: <resolved requirements path>
```
