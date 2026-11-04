Review only — identify hardcoded values and field names with safer existing constants or typed alternatives. No edits or fixes.

**Input:** The diff, paths, or symbols named in the message.

**Rules**

- Ask at most one question if the target is unclear; do not assume a target from earlier work
- Inspect the supplied scope and minimal surrounding context; for a diff, report findings on changed lines only
- Read-only — no file writes, Git mutations, or posted comments
- Check stdlib, installed dependencies, and existing project definitions for constants, enums, or typed objects that express the same meaning
- Verify the replacement exists in the version used and preserves behavior, including serialization and omitted fields
- Recommend a new named constant only when it clarifies a meaningful domain value or centralizes a shared rule; do not extract every literal or make fixed values configurable without a requirement
- Report only concrete maintenance or correctness benefits; skip incidental literals and unrelated cleanup
- Before replying: verify each location and replacement; drop speculative findings and state any inspection limits

**Output**

```text
Recommendation: <one short next step>

1. <path:line> — <finding and why it matters> → <suggested action>.

Limitations: <missing context affecting confidence>
```

- Number findings by importance; state each reason and action once
- Aim for at most 100 words for routine reviews; preserve material findings and limitations
- Omit Limitations when empty; when clean, output only "No worthwhile changes found in <scope>."
- If inspection is incomplete, state the limitation instead of claiming a clean review
- No preamble, code rewrites, approval gates, or closing recap
