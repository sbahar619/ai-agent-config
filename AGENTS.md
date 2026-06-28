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

State explicitly what the artifact does and must not do. Put shared conventions
in one place (this file or a parent rule), not repeated across files.

### Prompt formatting

Full conventions: `docs/prompt-formatting.md`. In brief:

- Open with one direct task line
- Separate major concerns with clear section headers (Input, Rules, Gates, Output)
- One bullet per constraint; fold pre-reply checks into Rules as a `Before replying:` bullet
- Keep Gates as its own section with a step / prompt / `n` table — do not fold gate workflow into Rules
- Wrap output templates in fenced code blocks; put omit-empty / numbering rules as bullets after the block
- Keep Input minimal — behavioral rules belong in Rules
