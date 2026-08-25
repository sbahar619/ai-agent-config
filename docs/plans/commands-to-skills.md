## Goal

Make current command capabilities available to agents as skills (alongside existing commands), add an orchestration skill, and update `AGENTS.md` to reflect the new layout.

## Plan

1. **Classify and convert** — audit all 25 commands, identify which translate to skills, create `skills/<name>/SKILL.md` mirrors in the project root; commands stay untouched
2. **Discover workflows** — review past Cursor conversations to identify common multi-step patterns, then review with you which orchestration/workflow skills to build
3. **Orchestration skill** — create `skills/orchestrate/SKILL.md` based on the agreed workflows from phase 2
4. **Update AGENTS.md** — add `skills/` to the Layout section, document the commands-vs-skills relationship, and add authoring guidance for skills
