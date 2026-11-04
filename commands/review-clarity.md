Review only — identify unclear names, misleading or redundant comments, and declarations placed far from use. No edits or fixes.

**Input:** The diff, paths, or symbols named in the message.

**Rules**

- Ask at most one question if the target is unclear; do not assume a target from earlier work
- Inspect the supplied scope and minimal surrounding context; for a diff, report findings on changed lines only
- Read-only — no file writes, Git mutations, or posted comments
- Judge names at their call sites: flag ambiguity, misleading meaning, or redundant context; follow language and repository conventions
- Check comments against behavior; retain explanations of intent, constraints, safety, and public contracts, and flag comments that merely repeat obvious code or mislead the reader
- Recommend narrower declaration scope or placement closer to use only when it improves understanding and preserves lifecycle and sharing requirements
- Identify the specific misunderstanding avoided; skip cosmetic preferences, wholesale renaming, and structural refactoring
- Before replying: verify each location and its surrounding usage; drop speculative findings and state any inspection limits

**Output**

```text
1. <path:line> — <finding and why it matters> → <suggested action>.
```

- Output only numbered recommended changes, ordered by importance; state each reason and action once. Omit Keep recommendations, verdicts, and summaries
- Aim for at most 100 words for routine reviews; preserve material findings and limitations
- When no changes are recommended, output exactly "No changes recommended."
- If inspection is incomplete, state the material limitation in one short sentence instead of claiming a completed review
- No preamble, code rewrites, approval gates, or closing recap
