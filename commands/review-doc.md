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
- Planning/design boundaries — research owns evidence, relevant gaps, and option tradeoffs; requirements own required outcomes, constraints, and success criteria; plans own delivery phasing and may hold brief requirements when no separate file exists; HLDs own architecture decisions and rationale; LLDs own detailed contracts and tests within that architecture; tasks own execution and completion criteria. Flag content that belongs in another layer or duplicates its detail; do not demand another layer's detail as a completeness fix.
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
- One finding per bullet — one concern, one line; add context only when the fix is ambiguous without it
- Reference the specific section or heading for every finding
- Every finding ends with a concrete action (`→ <what to change>`)
- Separate blocking issues from suggestions — never mix in one list
- Review only — propose targeted edits without modifying documents, source code, or Git state; do not rewrite the artifact wholesale
- Skip generic praise; only note strengths that are specific and actionable
- Keep chat to the verdict and actionable findings, ordered by severity; do not recap the artifact or narrate the review

**Output format:**

```
## Summary
<1 sentence verdict: ready / ready with changes / needs rework; note material review limitations>

## Blocking
- [Section] Issue → <action to fix>

## Suggestions
- [Section] Suggestion → <action to fix>

## Open Questions
1. <concrete unresolved question the artifact should answer, ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

- Omit Open Questions when nothing remains unresolved; settled decisions and assumptions are not questions
