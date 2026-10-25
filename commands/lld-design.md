# LLD only

LLD only — concise low-level design (deliverables, contracts, tests) for a topic, domain, or selected phase. No source edits, commits, or implementation.

**Input**

An architecture document path or supplied architecture description, plus optional delivery-phase selection (plan path, number, and title when known).

**Rules**

- Ask at most 1–2 questions only if scope is unclear
- Read the supplied architecture and applicable topic/domain HLDs when present; surface conflicts instead of overriding shared decisions. Sufficient inline architecture does not require a separate HLD file. Inspect further as needed.
- Draft for review — write the full LLD to the selected path before requesting content approval; show the file link and a brief overview in chat, marking the draft as awaiting review. Keep gate prompts and review commentary outside the file.
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Scope — covers all phases of the selected topic or domain by default (`<scope-dir>/lld.md`); for an explicitly selected phase, use `<scope-dir>/phase-N/lld.md`, with the shared HLD above phase folders
- Phase mapping — for a single phase, identify its delivery plan, number, and title; use that number for new `phase-N` folders, never an HLD rollout-stage label. Preserve existing folder names and record their mapping explicitly; resolve missing or conflicting mappings before the gate.
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only affected content within the selected scope. Identify follow-up for another document in the chat overview without editing that document.
- Reviewability — keep scope, consequential contracts, and acceptance criteria easy to scan; group necessary detail by deliverable. Remove repetition before proposing independently reviewable scopes; preserve essential constraints, failure cases, rationale, and tests rather than cutting them to fit a length target.
- Requirements — read supplied requirements and `requirements.md` in the selected scope and its topic root when present; link deliverables and acceptance criteria to relevant requirement IDs, and surface conflicts for resolution without redefining requirements. A separate requirements file is not mandatory.
- References — include an Architecture line in the saved LLD linking source architecture sections, including applicable topic/domain HLDs; for inline input, briefly identify the supplied architecture instead of inventing a link. Retain relevant requirement links; use relative paths and verify targets without copying content or creating missing parent documents.
- Document state — approval or saving the LLD does not establish implementation or passing tests
- Work status — distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Open questions — use the question + recommendation format below; keep decisions and assumptions separate; if any need user input, wait for answers before asking for approval
- Match repo API names and reconcile patterns
- Before proposing a new function or type, check the repo for existing symbols **and** the framework/library API (cobra/pflag, gin, client-go, etc.) for built-in equivalents; prefer using what exists over reimplementing — per coding-standards; cite what was checked
- Must not — source code edits, implementation, git mutations, architecture-only docs (components and flows without deliverable detail), resolving architecture decisions, or work outside the stated scope
- Authoring — typical sections: Scope, Goals, Deliverables (technical behavior and choices within the architecture, status/condition contracts with types/reasons/messages, resource naming/ownership/labels when relevant, tests); task IDs, per-task file inventories, task ordering, and completion tracking belong in tasks
- Before replying: the linked draft is complete and matches the selected scope; assumptions are stated where info is missing; chat stays within the output template

**Gates**

| Step | Prompt | n |
|------|--------|---|
| LLD | Happy with this LLD? (y/n) | Revise the draft per feedback; re-ask |

**Output**

**Chat:**

```
**Draft:** [lld.md](<resolved path>) — awaiting review
- <consequential contract, deliverable, or verification criterion>
```

- At most three short overview bullets; on revisions, use them for changed contracts, obligations, or open questions instead
- Request answers when user input is needed; otherwise show the LLD gate
- Do not repeat the full document in chat unless asked

**File:**

```
**Purpose:** Specify implementable deliverables, contracts, and tests within the stated scope; revisiting the architecture or implementing source code is outside this document's scope.

**Delivery phase:** [<plan title>](<relative plan path>) — <number>: <title>
**Architecture:** <relative links to source sections, or identification of supplied inline architecture>
**Requirements:** <relative links and IDs when applicable>

## Goal and scope
<intended outcome and boundaries>

## Deliverables
### <deliverable>
<technical behavior, contracts, rationale for non-obvious choices, and tests>

## Assumptions
- <unverified assumption>

## Open questions
1. <concrete unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

**After approval:**

```
## LLD approved
- Path: <resolved LLD path>
```

- No preamble, summary wrap-up, or filler unless asked
- Include Delivery phase only for a single selected phase; omit Requirements when none apply
- Omit empty sections except `Goal and scope` and `Deliverables`
