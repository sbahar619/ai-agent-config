Review only — identify ways to make code easier to follow while preserving behavior. No edits or fixes.

**Input:** The diff, paths, or symbols named in the message.

**Rules**

- Ask at most one question if the target is unclear; do not assume a target from earlier work
- Inspect the supplied scope and minimal surrounding context; for a diff, report findings on changed lines only
- Read-only — no file writes, Git mutations, or posted comments
- Check unnecessary branches, nesting, intermediate state, wrappers, and indirection against actual callers and contracts
- Judge the whole flow: splitting a long function or reducing line count alone is not a benefit; account for added helpers, navigation, and return conventions
- Prefer the smallest behavior-preserving change; keep single-use logic inline unless extraction clearly improves understanding
- Preserve validation, error semantics, ordering, side effects, and safety checks; flag any uncertain behavior instead of assuming equivalence
- Keep scope on control flow and abstraction cost; do not expand into duplication, naming, or cosmetic cleanup
- Before replying: verify each location and explain the concrete simplification benefit; drop speculative findings and state any inspection limits

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
