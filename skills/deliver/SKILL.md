---
name: deliver
description: >-
  End-to-end implementation workflow in a git worktree: branch, implement per
  task, self-review, fix, commit, then squash to a clean branch. Use when
  taking a plan or tasks from the discovery skill into code.
disable-model-invocation: true
---

# Deliver

Autonomous implementation loop in a git worktree. Takes a plan or tasks doc
from the discovery skill and produces a clean, squashed feature branch.

## Workflow

```
setup worktree → create dev branch → [implement → review → fix → verify → commit] per task → squash to clean branch
```

## Input

| Source | Description |
|--------|-------------|
| Plan path | `docs/plans/<feature>/plan.md` — for simple plans without tasks |
| Tasks path | `docs/plans/<feature>/tasks/*.md` — for complex plans with task breakdown |

The input comes from the discovery skill's artifacts folder.

## Steps

### 1. Setup worktree

Create a git worktree for isolated work:

```
git worktree add ../<feature-name>-dev main
```

Switch the agent session to the worktree root using `move_agent_to_root`.

### 2. Create dev branch

Follow the **gen-branch-name** skill to derive a branch name from the plan goal.
Append `-dev` suffix.

```
git checkout -b <type>/<slug>-dev
```

### 3. Task loop

For each task (or each plan phase if no tasks file exists), run this loop:

#### 3a. Implement

Follow the **implement** skill. Skip its interactive gate — self-validate that
changed files match the task spec and lint/tests pass.

If the implement skill's self-validation fails (unrelated test failures,
insufficient spec), log the issue in the artifacts folder and skip to the next
task.

#### 3b. Review

Follow the **review-changes** skill against the staged changes. Skip its
read-only constraint on fixes — findings feed directly into step 3c.

#### 3c. Fix

If review found blocking or major issues, fix them. Re-run review until verdict
is Approve or only minor/nit findings remain.

Do not ask the user — fix issues autonomously based on review findings.

#### 3d. Verify

Follow the **verify** skill against the task spec — confirm the implementation
meets the task's done-when criteria and lint/tests pass.

If verify fails, return to step 3a for this task. Cap retries at 2 — on third
failure, log the issue and move to the next task.

#### 3e. Commit

Stage all changes for this task:

```
git add -A
```

Follow the **gen-commit-msg** skill to produce a commit message from the staged
diff. Commit directly — do not ask.

```
git commit -m "<generated message>"
```

### 4. Squash to clean branch

After all tasks are committed on the dev branch:

```
git checkout main
git checkout -b <type>/<slug>
git merge --squash <type>/<slug>-dev
```

Follow the **gen-commit-msg** skill to produce a single commit message that
covers all changes.

```
git commit -m "<generated squash message>"
```

### 5. Final verify

Follow the **verify** skill against the full diff (`git diff main..HEAD`) and
the original plan — confirm all tasks are covered, lint/tests pass, no
regressions.

If verify fails, return to the dev branch, fix, and re-squash. Cap retries at 1.

## Artifacts

Save workflow outputs alongside discovery artifacts:

```
docs/plans/<feature-name>/
├── research.md          (from discovery)
├── plan.md              (from discovery)
├── tasks/               (from discovery)
├── review-task-01.md    (step 3b output per task)
├── verify-task-01.md    (step 3d output per task)
└── verify-final.md      (step 5 output)
```

## Rules

- **Autonomous** — self-decide at every step; do not ask the user for approval
  between steps; use verify and review as quality gates
- **Git operations permitted** — this workflow explicitly creates branches,
  commits, and merges as part of its contract; the user invokes this workflow
  knowing it will write to git
- Follow each referenced skill's rules and output format, but skip their
  interactive gates and "do not commit" constraints — this workflow overrides
  those for the implementation loop
- **Self-correct** — when review or verify finds issues, fix and re-run; do not
  stop to ask
- **Fail gracefully** — log issues per task; skip a task after 2 failed retries
  rather than blocking the entire workflow
- **No push or PR** — commits stay local; do not push to remote or create PRs
  unless the user explicitly asks after the workflow completes
- Carry context forward — plan/tasks feed into implement; implement output feeds
  into review; review findings feed into fix
