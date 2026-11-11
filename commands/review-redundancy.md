Review only — identify code, tests, documentation, and metadata references that serve no justified role in the intended delivery. No edits or fixes.

**Input:** A diff, feature, paths, or artifacts supplied in this turn; optional delivery baseline and supported deployments.

**Rules**

- Ask at most one initial question if the target is unclear; otherwise inspect the supplied scope and relevant requirements, callers, tests, references, and release evidence
- Read-only — no file writes, Git mutations, posted comments, or requirement changes
- Establish the reviewed revision or working-tree state and intended deliverables; distinguish tracked, untracked, and excluded artifacts. File presence does not establish delivery intent
- Separate development code, merged code, released behavior, and supported deployments; commits, implementation phases, and review PRs do not establish independently deployed versions or compatibility obligations
- Check migration paths, compatibility branches, fallbacks, abstractions, configuration, and supporting tests for dependencies on discarded designs or unsupported scenarios; distinguish necessary source adaptation from deployment migration
- Require evidence of a supported consumer, persisted state, or explicit compatibility obligation before treating an earlier design as a migration source. Never shipped does not by itself prove that no supported development deployment or data needs preservation
- Check documentation for obsolete procedures, repeated guidance, unsupported status claims, and dependencies on excluded artifacts; distinguish current instructions from intentionally retained history
- Check task IDs, phase numbers, PR history, and planning links in code comments and product documentation for relevance to the intended reader; preserve useful public API/product references and provenance in planning or historical artifacts
- Trace each candidate to its actual purpose and dependencies; implementation or a design entry alone does not prove necessity, and missing evidence alone does not prove redundancy. Cite both sides when sources conflict
- Recommend the smallest removal or correction with a concrete maintenance or clarity benefit; moving useful content, reducing file count, or shortening code alone is not a benefit
- Preserve required behavior, security boundaries, data integrity, operational guidance, and contractual obligations; account for affected callers, tests, and incoming references before recommending removal
- Keep scope on unnecessary artifacts and changes in the actual delivery; do not substitute repeated-code extraction, behavior-preserving refactoring, cosmetic cleanup, or broader feature tradeoffs
- Before replying: verify each finding's location, evidence, removal consequence, and delivery relevance; distinguish confirmed findings from unresolved assumptions, disclose coverage gaps, and do not recommend deleting a whole artifact because one part is obsolete

**Output**

```text
<Whether a change is needed, in plain language.>
1. <Location: unnecessary content or behavior, evidence, and smallest recommended change; include any material consequence.>
<Material uncertainty or inspection limit, if any.>
```

- Summarize in chat using ordinary Markdown, not a code block; use a flat numbered list only for multiple independent findings, ordered by impact
- Keep routine replies to 2–4 short sentences, usually under 60 words; include every decision-changing issue even when this exceeds the target
- Cite concise source locations supporting each finding; for a diff, anchor findings on changed lines and cite relevant baseline evidence separately
- Omit empty sections; if no changes are needed, say "No changes recommended." If review is incomplete, state the limitation without claiming a clean review
- Offer supporting detail only when useful; follow-ups answer the latest request without restarting the report or authorizing edits
