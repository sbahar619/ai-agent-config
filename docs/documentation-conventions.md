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
| Research | Evidence, relevant gaps, option tradeoffs, and one recommended next step | Requirements agreement, delivery phasing, and solution design |
| Requirements | Required outcomes, constraints, compatibility, and success criteria | Architecture choices, delivery phasing, and implementation detail |
| Plan | Delivery outcomes, their order, and why they matter; brief requirements when no separate file exists | Architecture decisions, detailed contracts, tests, and task-level steps |
| HLD | Architecture decisions, components, flows, rationale, and tradeoffs | Detailed contracts, implementation steps, and per-phase tests |
| LLD | Technical deliverables, detailed contracts, and tests within the architecture | Resolving architecture decisions, execution tracking, or source implementation |
| Tasks | Ordered work, files, dependencies, and completion criteria | New architecture or contract decisions, or repeated design rationale |

**Updates**

- Apply new information at the target document's level of responsibility; change
  only affected content within the requested scope.
- Identify follow-up for another document instead of expanding the target's scope.

**Layout**

- Default to `docs/plans/<topic>/`; use `<topic>/<domain>/` when the domain is
  requested or already established. Preserve existing document paths.
- Use `research.md`, `requirements.md`, `plan.md`, `hld.md`, `lld.md`, and `tasks.md`
  at the selected scope. For an explicitly selected phase, place its LLD and tasks
  in `phase-N/` beneath that scope; keep shared HLDs above phase folders.
- Read applicable topic-level requirements and architecture for domain work;
  reference inherited content rather than duplicating or overriding it.
- These are destinations, not a required document set; create only the requested artifacts.
- Use a separate requirements document when scope spans phases or needs a stable
  agreement on outcomes and compatibility; for small changes, a brief Requirements
  section in the plan is sufficient. Avoid maintaining both copies.

**References**

- Cite evidence for research findings; label assumptions explicitly.
- Reference relevant existing documents and sections instead of duplicating their content.
- Use relative paths from saved documents and verify that linked files and sections exist.
- Give requirements stable IDs and observable success criteria; plans and designs
  reference those IDs without duplicating or silently changing the requirements.

**Lifecycle**

- Follow the invoking command's approval and save gates; resolve questions requiring
  user input before requesting approval.
- Keep decisions, assumptions, and unresolved questions distinct; omit empty question sections.
- Saving or approving a document does not establish implementation or validation of its contents.
- Research may recommend requirements definition next; acceptance of research
  findings does not approve requirements. Requirements can also start from a direct
  goal and constraints without prior research or another command.
- Review requirements for necessity, clarity, consistency, verifiability, traceability,
  compatibility, non-goals, and accidental design decisions before planning against them.
