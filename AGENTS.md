# cursor-config

Configuration for Cursor and related AI agents: **rules**, **agents**, and
**commands**. Edit config only — not application code.

## Layout

- `rules/` — persistent constraints (`.mdc` + frontmatter)
- `agents/` — subagent role definitions
- `commands/` — slash-command prompts

Browse each directory for what exists today; do not duplicate inventories here.

## Adding or editing config

Every rule, agent, and command should be:

- **Short and concise** — bullets over prose; one clear job; cut filler
- **Best practice** — actionable, scoped, concrete output when the role needs it
- **Independent** — self-contained; no required reads of other agents or commands
- **Stateless** — no assumed prior agent, session, or workflow step; input comes
  from the user or paths they give in this turn
- **Non-redundant** — one concern per file; extend or link instead of copying

State explicitly what the artifact **does** and **must not do**. Put shared
conventions in one place (this file or a parent rule), not repeated across files.
