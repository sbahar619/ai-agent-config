# cursor-config

Configuration for Cursor and related AI agents: **rules** and **commands**.
Edit config only — not application code.

## Layout

- `rules/` — persistent constraints (`.mdc` + frontmatter)
- `commands/` — slash-command prompts (one role per command; parent session only)

Browse each directory for what exists today; do not duplicate inventories here.

Command scope boundaries live in `docs/plans/agents-to-commands.md` when needed.

## Adding or editing config

Every rule and command should be:

- **Short and concise** — bullets over prose; one clear job; cut filler
- **Best practice** — actionable, scoped, concrete output when the role needs it
- **Independent** — self-contained; no required reads of other commands
- **Stateless** — no assumed prior command, session, or workflow step; input comes
  from the user or paths they give in this turn
- **Non-redundant** — one concern per file; extend or link instead of copying

State explicitly what the artifact **does** and **must not do**. Put shared
conventions in one place (this file or a parent rule), not repeated across files.
