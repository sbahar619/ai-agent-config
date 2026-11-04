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
- Before replying: ensure every in-scope feature and subfeature was assessed, recommendations trace to evidence and real needs, and every proposed reduction states its downside; disclose any coverage gaps

**Output**

```text
1. <Simplify | Defer | Drop> <plain-language feature> — <recommended change and why>. Gain: <benefit>; cost: <downside or accepted limitation>. <source location>
```

- Output only numbered recommended changes, ordered by importance; omit Keep recommendations, verdicts, inventories, and summaries
- Use everyday language and concrete consequences; state each reason and tradeoff once
- Aim for 150 words or fewer for routine reviews; remove repetition before exceeding this to preserve material changes or limitations
- Include any assumption requiring confirmation within the affected recommendation; requirement changes remain proposals, not accepted requirements
- When no changes are recommended, output exactly "No changes recommended."
- If inspection is incomplete, state the material limitation in one short sentence instead of claiming a completed review
- No preamble, code rewrites, approval gates, or closing recap
