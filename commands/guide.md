Produce a clear, complete, step-by-step guide for a given subject.

**Input**
Subject given in this turn — a task, tool, process, or question (e.g. "set up mTLS between two services", "rotate a Kubernetes secret").

**Rules**
- Number steps sequentially; one action per step.
- Order steps so each depends only on steps already completed — no forward references, no skipped prerequisites.
- State prerequisites once, up front, not scattered mid-guide.
- Define any term on first use if it's not standard for the subject's domain.
- Where a step has a way to verify it worked, include it in that step, not as a separate section.
- No filler: no restating the subject, no "in this guide we will," no closing summary.
- Before replying: walk the steps in order and confirm nothing is skipped or assumed.

**Output**
```
# <Subject>

Prerequisites:
- <item>

Steps:
1. <action>
   <verification, if applicable>
2. <action>
   <verification, if applicable>
```
- Omit Prerequisites block if none apply.
- Omit per-step verification lines when there's nothing to check.
