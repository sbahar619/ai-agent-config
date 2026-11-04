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
- Recommend Keep, Simplify, Defer, or Drop for each item; when evidence is insufficient, mark Decide and give a focused question with a provisional recommendation
- For Defer, identify a concrete condition that would justify revisiting it; for Simplify or Drop, identify affected requirements and dependent behavior so the saving is not overstated
- Keep this review about necessity and tradeoffs; do not substitute naming, formatting, or behavior-preserving refactoring advice
- Before replying: ensure every in-scope feature and subfeature was assessed, recommendations trace to evidence and real needs, and every proposed reduction states its downside; disclose any coverage gaps

**Output**

```text
Recommendation: <smallest worthwhile scope and main next step>.

1. <Keep | Simplify | Defer | Drop | Decide> — <plain-language feature>: <why needed or not worth it>. Gain: <benefit of recommendation>; cost: <downside or accepted limitation>. <source location>

Decision needed: <concrete question>? Recommendation: <answer and short reason>.
Limitations: <unreviewed scope or missing evidence>
```

- Lead with the decision; use everyday language and concrete consequences, not symbol inventories or technical review narration
- Number items by decision importance; group straightforward Keep items sharing the same rationale, but do not hide independent tradeoffs
- Aim for 150 words or fewer for routine reviews; remove repetition before exceeding this to preserve material decisions or limitations
- Include only consequential findings in detail; summarize remaining assessed features in one short Keep item so coverage is clear
- Omit Decision needed and Limitations when empty; unresolved decisions remain proposals, not accepted requirements
- When no changes are worthwhile, give a short Keep recommendation with the main reason and cost; do not invent findings
- No full inventory table, code rewrites, approval gates, repeated summary, or closing recap unless requested
