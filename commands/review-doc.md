---
description: Review a document, design, plan, task write-up, or other non-code artifact for clarity, completeness, correctness, and risk.
---

**Review the provided artifact end-to-end before giving any feedback.** Identify what kind of artifact it is (document, design, plan, task write-up, proposal, or other) and adapt the lens accordingly, but ground every comment in what's actually written — never assume intent that isn't on the page.

**Read fully first.**
- Read the entire artifact before writing any feedback; do not comment section-by-section as you go.
- Note the artifact's stated goal and audience if given; if absent, state the gap rather than guessing.

**Evaluate against these dimensions:**
- Clarity — is the writing unambiguous to a reader unfamiliar with the background?
- Completeness — are there missing sections, open questions, or unstated assumptions?
- Correctness — are there factual, logical, or technical errors?
- Risk — what could go wrong if this is approved or implemented as-is, and how severe?
- Scope — does it try to cover too much or too little for its stated purpose?
- Planning/design boundaries — research owns evidence and findings; requirements own required outcomes, constraints, and success criteria; plans own delivery phasing and may hold brief requirements when no separate file exists; HLDs own architecture; LLDs own contracts and tests; tasks own execution and completion criteria. Flag content that belongs in another layer or duplicates its detail.
- Requirements review — check necessity, unambiguous and verifiable wording, stable unique IDs, traceability to goals or evidence, compatibility and non-goals, conflicting obligations, missing constraints, and unintended design decisions; do not invent acceptance thresholds
- Requirements coverage — when a requirements document is supplied or referenced, check that in-scope plan/design outcomes satisfy its requirements or explicitly identify deferrals; flag silent scope changes
- Planning/design references — verify referenced files and sections exist, with paths relative to the containing document; flag copied detail that should link to an existing source
- Planning/design state — distinguish decisions, assumptions, and unresolved questions; approval or saving a document is not evidence of implementation or validation
- Coding-standards compliance — for design docs that propose interfaces, functions, or types: check that proposed symbols don't duplicate existing repo logic **or** framework/library built-ins (cobra/pflag, gin, client-go, etc.); prefer using what exists over reimplementing; verify naming follows repo conventions

**Constraints:**
- One finding per bullet — one concern, one line; add context only when the fix is ambiguous without it
- Reference the specific section or heading for every finding
- Every finding ends with a concrete action (`→ <what to change>`)
- Separate blocking issues from suggestions — never mix in one list
- Propose targeted edits only — do not rewrite the artifact wholesale
- Skip generic praise; only note strengths that are specific and actionable

**Output format:**

```
## Summary
<1 sentence verdict: ready / ready with changes / needs rework>

## Blocking
- [Section] Issue → <action to fix>

## Suggestions
- [Section] Suggestion → <action to fix>

## Open Questions
1. <concrete unresolved question the artifact should answer, ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

- Omit Open Questions when nothing remains unresolved; settled decisions and assumptions are not questions
