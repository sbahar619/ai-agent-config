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

- Inspect the target and relevant topic references before revising to identify
  affected documents and sections; keep the inspection bounded to the requested change.
- Apply new information at the target document's level of responsibility; change
  only affected content within the requested scope.
- Identify follow-up for another document instead of expanding the target's scope.
- Refresh code-based research against the requested baseline, otherwise retaining
  the document's stated branch/revision or using the current checkout when none
  is recorded. State the resolved revision and relevant included uncommitted changes.
  Keep unmerged changes separate from target-branch findings; report unavailable
  baselines instead of silently substituting another. Design intentions remain proposals.

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
- Persist upward links: tasks to covering LLD sections, LLDs to source HLDs,
  HLDs to delivery plans, and plans to research and requirements. Domain HLDs
  also link applicable topic-level architecture; requirements cite their sources.
- Link the nearest relevant existing source when a layer is absent; do not create
  documents just to complete the chain. These links belong in saved artifacts,
  not only chat summaries.
- Use relative paths from saved documents and verify that linked files and sections exist.
- Give requirements stable IDs and observable success criteria; plans and designs
  reference those IDs without duplicating or silently changing the requirements.

**Coverage**

- Map each in-scope research gap and requirement to a plan outcome or an explicit
  deferral with a reason; unrelated findings do not expand the agreed scope.
- Account for every required deliverable in the selected task scope, including
  specified tests and integration work, across new and existing batches. Link
  existing coverage instead of duplicating tasks; record proposed deferrals and
  resolve conflicts with upstream scope before approval.
- Use source links for covered work and concise notes for exceptions; do not
  require a separate coverage document or repeat the source detail.

**Complete deliverables**

- Each phase delivers a useful outcome after its prerequisites; it must not need
  a later phase to make its stated outcome work.
- Each task is the smallest complete, reviewable change, including supporting
  callers, registration, configuration, integration, and appropriate tests.
  Separate unrelated cleanup; do not separate wiring needed for the same outcome.
- Completion criteria describe observable results and relevant verification;
  report required work outside the authorized scope instead of silently omitting it.

**Phase identity**

- Identify delivery phases by plan path, number, and title; do not silently
  renumber phases referenced elsewhere.
- For new `phase-N/` folders, use the delivery-plan number. Each phase LLD and
  task file records a Delivery phase header with a relative plan link, number,
  and title. Preserve existing folder names and state their mapping explicitly.
- Resolve missing or conflicting mappings before approval; unphased work stays
  at topic or domain scope without requiring a delivery plan.
- Label architectural rollout sequencing as stages and map them to delivery
  phases when defined; stages and phases need not correspond one-to-one.

**Task batches**

- Read existing `tasks*.md` in the selected scope or phase directory; revise the
  matching batch and create another only for distinct follow-up work.
- Start with `tasks.md` (batch 1); number new batches above the existing maximum
  as `tasks-02.md`, `tasks-03.md`, etc. Preserve existing filenames; batch numbers
  are independent of delivery-phase numbers. Show the destination before approval.
- Preserve task IDs and continue the existing scheme across batches in the same
  directory; never renumber existing tasks or reuse retired IDs. Cross-batch
  dependencies use relative links to the exact task heading.

**Review**

- Review against the artifact's purpose and ownership boundaries; inspect relevant
  references and evidence without expanding into a whole-topic audit.
- Check duplication, conflicting decisions, stale assumptions, phase mappings,
  and whether links support their associated claims. Cite both sides of conflicts;
  distinguish contrary evidence from unavailable or unverified information.
- Recommend targeted corrections in the owning document; preserve explicit legacy
  mappings and do not require missing document layers or edit artifacts during review.

**Lifecycle**

- Follow the invoking command's approval and save gates; resolve questions requiring
  user input before requesting approval.
- Keep decisions, assumptions, and unresolved questions distinct; omit empty question sections.
- Saving or approving a document does not establish implementation or validation of its contents.
- When reporting work status, distinguish proposed (intended work), implemented
  (code evidence at an identified revision or working-tree state), validated
  (relevant passing checks with scope and tested state), and merged (confirmed
  inclusion in a named target branch). Cite evidence beside each claim before
  advancing it; mark unsupported claims unverified.
- These claims are independent: merged does not imply validated, and checks on
  an earlier state do not validate later changes. Keep evidence scoped to the
  covered work; a partial result does not establish whole-phase completion.
- Include status only when reporting progress or describing existing behavior;
  do not add tracking sections to every document or perform implementation,
  validation runs, or Git mutations merely to fill a status field.
- Research may recommend requirements definition next; acceptance of research
  findings does not approve requirements. Requirements can also start from a direct
  goal and constraints without prior research or another command.
- Review requirements for necessity, clarity, consistency, verifiability, traceability,
  compatibility, non-goals, and accidental design decisions before planning against them.
