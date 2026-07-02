Move the current agent session to the worktree at the path given by the user.

**Input:** An absolute path to a worktree directory, provided as the argument to this command.

**Rules**

- Read the `move_agent_to_root` MCP tool schema before calling it
- Call `move_agent_to_root` with `rootPath` set to the path the user provided
- If the path is relative, resolve it against the user's home directory or ask for clarification
- Do not use `move_agent_to_cloned_root` — that is only for `cursorfs-clone` destinations
- Do not make any file edits, commits, or other changes; only switch the root
