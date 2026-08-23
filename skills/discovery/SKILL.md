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
when the plan is complex. Produces artifacts the implement-workflow skill
consumes.

## Workflow

```
research → verify → decide (worth it?) → plan → verify → decide (complex?) → tasks → verify
                          ↓ no                                    ↓ no
                        stop                              hand off to
                                                       implement-workflow
```

## Steps

### 1. Research

Follow the **research** skill. Investigate the problem with evidence.

### 2. Verify research

Follow the **verify** skill against the research output — confirm findings are
evidence-backed, no speculation presented as fact, and the recommendation is
grounded.

Decision gate — present verified findings to the user:
- **Worth the work** → continue to step 3
- **No action needed** → stop; save research output to artifacts folder

### 3. Plan

Follow the **plan** skill. Produce a high-level phased plan from the research
findings.

Persist the plan under the artifacts folder (see Artifacts below).

### 4. Verify plan

Follow the **verify** skill against the plan — confirm phases cover the problem,
no gaps or missing dependencies, scope matches research findings.

Decision gate — review with the user:
- **Simple plan** (1–2 small phases, clear scope) → hand off directly to
  implement-workflow with the plan path
- **Complex plan** (multiple phases, large scope, dependencies) → continue to
  step 5

### 5. Tasks

Follow the **tasks** skill. Break the plan into ordered implementable tasks.

Apply tasks to:
- All plan phases — when the plan is small enough to tackle in one pass
- Individual phases — when phases are large or independent enough to warrant
  separate task breakdowns

Persist tasks under the artifacts folder.

### 6. Verify tasks

Follow the **verify** skill against the tasks — confirm one concern per task,
dependency ordering is correct, no coverage gaps against the plan, and each
task is scoped to one implement invocation.

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

- Follow each referenced skill's own rules and output format
- Interactive — present each decision gate to the user; do not auto-advance
- Carry context forward — each step receives the prior step's output (research
  findings feed into plan input; plan path feeds into tasks input)
- Read-only — this workflow does not edit source code, create branches, or commit;
  it produces planning artifacts only
- Stop early when research shows no action needed — do not plan for the sake of
  planning
