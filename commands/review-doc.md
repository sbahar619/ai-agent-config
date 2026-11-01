---
description: Review a document, design, plan, task write-up, or other non-code artifact for clarity, completeness, correctness, and risk.
---

**Review the provided artifact end-to-end before giving any feedback.** Identify what kind of artifact it is (document, design, plan, task write-up, proposal, or other) and adapt the lens accordingly, but ground every comment in what's actually written — never assume intent that isn't on the page.

**Review context:**
- Note the artifact's stated goal and audience if given; if absent, state the gap rather than guessing.
- Read relevant linked documents and source evidence to check the artifact's claims; keep this inspection within its stated purpose and requested scope. Report unavailable evidence as a review limitation, not a confirmed defect.

**Evaluate against these dimensions:**
- Clarity — is the writing unambiguous, with its purpose, consequential decisions, obligations, and open questions easy to find? Flag repetition and unnecessary detail; recommend clearer sections or independently reviewable scopes without removing essential constraints, failure cases, rationale, or acceptance criteria.
- Completeness — are there missing sections, open questions, or unstated assumptions?
- Correctness — are there factual, logical, or technical errors?
- Risk — what could go wrong if this is approved or implemented as-is, and how severe?
- Scope — does it try to cover too much or too little for its stated purpose?
- Product documentation — user-facing guidance must explain behavior without internal delivery-phase/task IDs or planning-document references; flag dependencies on that context without removing useful public API or product references
- Planning/design boundaries — research owns evidence, relevant gaps, and option tradeoffs; requirements own required outcomes, constraints, and success criteria; plans own delivery phasing and may hold brief requirements when no separate file exists; HLDs own architecture decisions and rationale; LLDs own detailed contracts and tests within that architecture; tasks own outcomes, brief file scope, dependencies, and completion criteria; optional implementation companions own private APIs, algorithms, and detailed verification for their matching task file. Flag content that belongs in another layer or duplicates its detail; do not demand another layer's detail as a completeness fix.
- Implementation splits — check matching links between `tasks/` and `implementation/`, task IDs, concise shared notes, and separation of `implementation/history.md` from current guidance. For folder moves, check incoming references and relative design/source links; preserve legacy paths unless migration was requested. Keep schemas, compatibility, failures, risks, and acceptance obligations visible in the design/task review; verify relocated details preserve obligations, not just working links. Do not require a companion for sufficient small tasks or recommend one monolithic file for multiple task groups.
- Requirements review — check necessity, unambiguous and verifiable wording, stable unique IDs, traceability to goals or evidence, compatibility and non-goals, conflicting obligations, missing constraints, and unintended design decisions; do not invent acceptance thresholds
- Requirements coverage — when a requirements document is supplied or referenced, check that in-scope plan/design outcomes satisfy its requirements or explicitly identify deferrals; flag silent scope changes
- Planning/design references — verify relative links resolve to the intended files and sections and support the associated claims; check relevant parent-source links without demanding missing document layers
- Decision consistency — compare decisions and constraints with their owning documents; cite both sides of a conflict and identify which owner needs resolution. Do not assume the newest document overrides an agreed requirement or architecture decision.
- Assumption freshness — check assumptions against the stated baseline and relevant later evidence; distinguish contradicted assumptions from those still unverified. Reopen settled decisions only with evidence of a conflict or changed premise.
- Phase mappings — verify phase documents identify the delivery plan, phase number, and title; flag missing or conflicting mappings, including cross-domain ambiguity. Preserve explicitly documented legacy folder mappings; do not equate rollout stages or task-batch numbers with delivery phases.
- Planning/design state — distinguish decisions, assumptions, and unresolved questions; approval or saving a document is not evidence of implementation or validation
- Work-status evidence — proposed work must not read as completed behavior; implemented claims need code evidence at a stated revision or working-tree state, validated claims need relevant passing checks with scope and tested state, and merged claims need confirmed inclusion in a named target branch. Flag unsupported claims and validation evidence for a different state; merge evidence does not establish validation.
- Coding-standards compliance — for design docs that propose interfaces, functions, or types: check that proposed symbols don't duplicate existing repo logic **or** framework/library built-ins (cobra/pflag, gin, client-go, etc.); prefer using what exists over reimplementing; verify naming follows repo conventions

**Constraints:**
- Give one numbered recommendation per suggested change, ordered by severity; mark blocking changes with `Blocking:`
- Reference the specific section or heading and state the concrete edit; add a brief reason only when needed to understand it
- Review only — propose targeted edits without modifying documents, source code, or Git state; do not rewrite the artifact wholesale
- Keep the output as short and simple as possible; omit praise, summaries, recaps, and review narration
- Mention material review limitations in one short sentence; do not present unverified concerns as confirmed defects

**Output format:**

```
1. Blocking: [Section] <specific required change; brief reason if needed>
2. [Section] <specific suggested change; brief reason if needed>
```

- Number recommendations consecutively, with blocking changes first; omit headings and empty items
- If no changes are needed, say `No changes recommended.`
