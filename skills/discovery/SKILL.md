---
name: discovery
description: >-
  End-to-end discovery workflow: research a potential issue, plan if warranted,
  break into tasks if complex. Use when starting from a problem or idea that
  needs investigation before implementation.
disable-model-invocation: true
---

# Discovery

Research a potential issue, plan if it's worth the work, and break into tasks
when the plan is complex. Produces artifacts under `docs/plans/<feature>/`.

## Workflow

```
research → verify → plan → verify → tasks (if complex) → verify
                ↓ no action
              stop
```

## Steps

### 1. Research

Follow the **research** skill. Investigate the problem with evidence.

### 2. Verify research

Follow the **verify** skill against the research output — confirm findings are
evidence-backed, no speculation presented as fact, and the recommendation is
grounded.

Self-decide:
- Research shows the issue is real and worth the work → continue to step 3
- Research shows no action needed or insufficient evidence → stop; save
  research output to artifacts folder and report the conclusion

### 3. Plan

Follow the **plan** skill. Produce a high-level phased plan from the research
findings. Skip the plan skill's interactive gates — persist directly under the
artifacts folder.

### 4. Verify plan

Follow the **verify** skill against the plan — confirm phases cover the problem,
no gaps or missing dependencies, scope matches research findings.

If verify fails, revise the plan and re-verify. Do not ask the user — fix it.

Self-decide complexity:
- **Simple** (1–2 small phases, clear scope) → skip tasks; workflow is complete
- **Complex** (multiple phases, large scope, dependencies) → continue to step 5

### 5. Tasks

Follow the **tasks** skill. Break the plan into ordered implementable tasks.
Skip the tasks skill's interactive gates — persist directly under the artifacts
folder.

Apply tasks to:
- All plan phases — when the plan is small enough to tackle in one pass
- Individual phases — when phases are large or independent enough to warrant
  separate task breakdowns

### 6. Verify tasks

Follow the **verify** skill against the tasks — confirm one concern per task,
dependency ordering is correct, no coverage gaps against the plan, and each
task is scoped to one implement invocation.

If verify fails, revise the tasks and re-verify. Do not ask the user — fix it.

## Artifacts

Save all outputs under a dedicated folder per feature:

```
docs/plans/<feature-name>/
├── research.md        (step 1 output)
├── plan.md            (step 2 output)
└── tasks/
    ├── <phase-or-all>.md  (step 3 output)
    └── ...
```

- `<feature-name>` — derive from the plan goal; kebab-case
- Create the folder on first artifact; reuse for subsequent steps
- Each file is the verbatim output of the corresponding skill

## Rules

- Follow each referenced skill's rules and output format, but skip their
  interactive gates — this workflow is autonomous
- Autonomous — self-decide at each step using verify as the quality gate; do not
  ask the user for approval between steps
- Carry context forward — each step receives the prior step's output (research
  findings feed into plan input; plan path feeds into tasks input)
- Self-correct — when verify fails, revise and re-verify; do not stop to ask
- Read-only — this workflow does not edit source code, create branches, or commit;
  it produces planning artifacts only
- Stop early when research shows no action needed — do not plan for the sake of
  planning
