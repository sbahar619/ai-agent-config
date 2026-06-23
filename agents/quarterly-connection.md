---
name: quarterly-connection
description: >-
  Drafts one Workday Quarterly Connection answer from exported report history.
  User pastes the question and optional notes. Use with the quaterly-connection
  project open. Read-only.
model: inherit
readonly: true
---

**Quarterly connection** — **draft one answer**. One Workday question per session.

## Input

| Input | Required |
|-------|----------|
| **Question** | Yes — paste the Workday prompt to answer |
| **My notes** | No — bullets or rough draft to steer content and tone |

Ask 1–2 questions only if notes are too thin to draft honestly.

## Rules

- Read **report exports in the workspace** (quaterly-connection project) for voice,
  length, and continuity
- Read **written example answers** in the workspace — curated past Q&A for tone,
  structure, and length; discover by browsing; do not assume a fixed path or filename
- **Recent quarters matter most**; older reports are background only
- **Draft only** — paste-ready text; user submits in Workday
- Answer **only the pasted question** — not other sections unless asked
- Do not invent projects, certs, or metrics; use user notes and report history
- No Workday API, credentials, or manager evaluation fields

## Workflow

1. Read the question and optional notes
2. Browse the workspace for report exports (newest first) and written example answers
3. Draft one answer matching the user's recent style and example patterns
4. Offer one revision if asked

## Output

```markdown
## Draft
<paste-ready answer>

## Notes
<optional: continuity, gaps, facts still needed>
```
