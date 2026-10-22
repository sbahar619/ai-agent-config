# Documentation Command Conventions

Use this guide when maintaining commands that author, update, triage, or review
planning and design documents.

- Keep each command self-contained: include its applicable instructions inline;
  do not require loading this guide, another command, or a shared rule at runtime.
- This guide is the common authoring reference; brief repetition in executable
  prompts is intentional so copied or independently installed commands still work.
- Keep each command's output format, scope, and approval gates explicit; document
  work does not authorize implementation or unrelated document changes.

**Responsibilities**

| Document | Owns | Excludes |
|----------|------|----------|
| Research | Evidence, findings, alternatives, and one recommended next step | Architecture and implementation design |
| Plan | Phased outcomes and why they matter | Architecture, API contracts, and implementation detail |
| HLD | Architecture, components, flows, and rationale | Detailed contracts, implementation steps, and per-phase tests |
| LLD | Implementable deliverables, contracts, and tests | Revisiting architecture or implementing source code |
| Tasks | Ordered work, files, dependencies, and completion criteria | New architecture decisions or design rationale |

**Layout**

- Co-locate a topic's documents under `docs/plans/<topic>/` using `research.md`,
  `plan.md`, `hld.md`, `lld.md`, and `tasks.md` for their respective roles.
- For an explicitly selected phase, place its LLD and tasks in `phase-N/`, keeping
  the filenames `lld.md` and `tasks.md`.
- These are destinations, not a required document set; create only the requested artifacts.

**References**

- Cite evidence for research findings; label assumptions explicitly.
- Reference relevant existing documents and sections instead of duplicating their content.
- Use relative paths from saved documents and verify that linked files and sections exist.

**Lifecycle**

- Follow the invoking command's approval and save gates; resolve questions requiring
  user input before requesting approval.
- Keep decisions, assumptions, and unresolved questions distinct; omit empty question sections.
- Saving or approving a document does not establish implementation or validation of its contents.
