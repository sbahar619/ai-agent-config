Review only — identify repeated implementation of the same rule that is worth sharing. No edits or fixes.

**Input:** The diff, paths, or symbols named in the message.

**Rules**

- Ask at most one question if the target is unclear; do not assume a target from earlier work
- Inspect the supplied scope and relevant counterparts or existing utilities; for a diff, anchor each finding on a changed line
- Read-only — no file writes, Git mutations, or posted comments
- Compare meaning, inputs, outputs, errors, and side effects; similar-looking code alone is not duplication worth removing
- Prefer an existing suitable utility; otherwise recommend the smallest shared helper or loop only when reduced maintenance outweighs added abstraction
- Preserve checks at distinct safety boundaries or against different object versions; do not merge checks with different failure meanings
- Cite the repeated locations and identify the shared rule; avoid generic frameworks or callbacks merely to save a few lines
- Review implementation duplication only; duplicate test-case coverage belongs to the existing review-test-cases command
- Before replying: confirm each finding represents the same rule and a concrete reuse benefit; drop speculative findings and state any inspection limits

**Output**

```text
Recommendation: <one short next step>

1. <path:line; counterpart path:line> — <shared rule and maintenance cost> → <suggested reuse>.

Limitations: <missing context affecting confidence>
```

- Number findings by importance; state each reason and action once
- Aim for at most 100 words for routine reviews; preserve material findings and limitations
- Omit Limitations when empty; when clean, output only "No worthwhile changes found in <scope>."
- If inspection is incomplete, state the limitation instead of claiming a clean review
- No preamble, code rewrites, approval gates, or closing recap
