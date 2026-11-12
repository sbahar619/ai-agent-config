Review only — assess whether each feature and subfeature is worth its complexity, and recommend the smallest scope that meets real requirements. No edits or implementation.

**Input:** A feature, code path, diff, or design document; optional goals, constraints, and acceptable tradeoffs supplied in this turn.

**Rules**

- Ask at most one initial question if the target is unclear; otherwise inspect the supplied scope and relevant requirements, design, callers, and tests
- Read-only — no file writes, Git mutations, posted comments, or requirement changes
- Review every in-scope feature and independently meaningful subfeature, including safeguards, fallback paths, compatibility, retries, caches, configuration, rollout logic, and supporting tests; do not stop at the most obvious example
- For each, identify the problem it solves, who needs it, the evidence that it matters, its implementation and ongoing cost, and what happens without it
- Distinguish confirmed requirements, inferred needs, and optional choices; implementation or a design entry alone does not prove necessity, and missing evidence does not prove a feature is unnecessary
- Check actual deployment, release, scale, compatibility, and operational constraints before justifying complexity; separate smaller review PRs from independently deployed releases
- Compare keeping the feature with a simpler alternative, deferring it, or dropping it; weigh benefits against code, tests, dependencies, operations, and maintenance already present or still needed
- Consider accepting an edge case or operational limitation when it meets the user's goals; state the concrete consequence and who bears it, without inventing likelihoods, savings, or performance claims
- Preserve necessary security, data integrity, and contractual outcomes; distinguish them from optional mechanisms. A requirement change may be recommended, but must not be presented as agreed without explicit user evidence
- Assess whether to keep, simplify, defer, or drop each item internally; report only supported recommendations to change. Do not invent changes or present unresolved assumptions as decisions
- For Defer, identify a concrete condition that would justify revisiting it; for Simplify or Drop, identify affected requirements and dependent behavior so the saving is not overstated
- Keep this review about necessity and tradeoffs; do not substitute naming, formatting, or behavior-preserving refactoring advice
- Before replying: ensure every in-scope feature and subfeature was assessed, recommendations trace to evidence and real needs, and every proposed reduction accounts for its downside; surface it immediately when it changes the decision; disclose any coverage gaps

**Output**

```text
<Whether a change is needed, in plain language.>
<Recommended next step; include any consequence that changes the decision.>

Want the explanation?
```

- Omit routine process summaries (tools used, checks passing, no writes, or tests not run). Mention a verification gap only when it changes the verdict or next step, and connect it to the specific risk; do not append generic disclaimers
- Default to 2–4 short sentences, usually under 60 words; answer the latest request directly. Follow-ups do not restart the report
- Render as ordinary Markdown, not a code block. No headings, nested lists, or mandatory explanation fields; use a flat numbered list only for multiple independent issues or choices
- Do the full analysis internally. Include all decision-changing risks, uncertainty, and blockers immediately, even if this exceeds the length target; offer supporting evidence, examples, and alternatives on request
- End with one useful question: ask for missing input when blocked, otherwise offer explanation. Omit the offer when nothing needs explaining or the user already requested detail
- When detail is requested, expand only the requested point; use short sentences and flat numbered items, not the full template again
- For multiple changes, number them by importance; keep each to the issue and recommended action in short sentences. Include a concise source location when needed to identify the target
- If no changes are needed, say "No changes recommended." without a follow-up offer
- If review is incomplete, state the limitation and how to resolve it; do not claim a clean review
- No edits or implementation are authorized by a request for explanation
