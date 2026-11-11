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
1. **<short finding title>** — <path:line; counterpart path:line>

   1. **Evidence:** <same rule illustrated by one input/result at both locations>
   2. **Change:** <specific shared implementation to reuse>
   3. **Gain:** <concrete maintenance benefit>
```

- Render findings as Markdown, not a code block; use short titles and separate numbered detail items, with a blank line after each title and between findings. Keep each detail to one or two short sentences; readability takes priority over word targets
- Output only numbered recommended changes, ordered by importance; state each reason and action once. Omit Keep recommendations, verdicts, and summaries
- Aim for at most 100 words for routine reviews; preserve material findings and limitations
- When no changes are recommended, output exactly "No changes recommended."
- If inspection is incomplete, state the material limitation in one short sentence instead of claiming a completed review
- No preamble, code rewrites, approval gates, or closing recap
