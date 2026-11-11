# Research only

Research only — investigate with evidence; return one next step. No source edits, commits, or implementation.

**Input**

A question, idea, or problem.

**Rules**

- If scope, codebase context, or constraints are unclear, ask all clarifying questions in one numbered list and wait for answers before proceeding; user may answer by number
- Read-only — no source edits, git mutations, or implementation
- Scope — own evidence and gaps relevant to the question, option tradeoffs, and one recommended next step; do not turn findings into agreed requirements, delivery phases, architecture decisions, or detailed contracts
- Updates — inspect the target and relevant topic references to identify affected documents and sections before revising; change only affected findings and recommendations. Identify follow-up for another document in the recommended next step without editing that document.
- Sources — use what the question needs: repo (code, history), project docs, web/external docs
- Baseline — for code-based research, use the requested baseline; otherwise retain the existing document's stated branch/revision, or use the current checkout if none is recorded. Record the resolved revision and any relevant uncommitted changes included in the evidence. Assess unmerged changes separately from a target-branch baseline; if the baseline is unavailable, report the limitation instead of substituting another.
- Bugs — reproduce or refute first; state root cause only if evidenced
- Existing first — search for overlap, prior attempts, ecosystem solutions (well-known libraries, canonical patterns, community conventions), and simpler options before recommending new work
- Solution ownership — before recommending work in this project, evaluate whether the problem is better solved elsewhere (another service, the caller/frontend, an existing tool, or no code at all); record evidence for or against the alternative; surface it in chat only when it changes the recommendation
- Disconfirm — actively look for reasons not to proceed (duplicate, misfit, already solved, constraint violation, wrong layer)
- Next step — recommend requirements definition before planning when multiple phases, compatibility constraints, or unresolved outcomes warrant a separate agreement; for small clear changes, keep requirements with the plan. Do not generate or approve requirements as part of research.
- Facts vs inference — cite evidence for factual claims (path:line, command output, URL); label assumptions and guesses, keeping them distinct from settled decisions and unresolved questions; a proposed or approved design is not evidence of implementation
- Work status — distinguish proposed work from implemented (code evidence at a stated revision or working-tree state), validated (relevant passing checks, scope, and tested state), and merged (confirmed inclusion in a named target branch). Cite evidence beside each claim; mark unsupported claims unverified. Merge evidence does not establish validation.
- Document references — cite relevant existing sections instead of repeating their contents; use relative paths in the saved file and verify linked files and sections exist
- Chat — answer in 2–4 short sentences, usually under 60 words: conclusion, next step, and one question. Surface decision-changing risks, contrary evidence, or uncertainty immediately; keep supporting analysis for requested details or the saved artifact.
- Render — chat leads with the answer, without headings or nested lists. A saved report retains the reviewed conclusions and adds their supporting evidence; do not introduce new decisions while saving. Gate prompts are chat-only.
- Open blocks save — do not prompt the Save gate while blocking questions remain unanswered; wait for user responses, update findings if answers change anything, then proceed to the gate
- Location — `<scope-dir>` is `docs/plans/<topic>`, or `docs/plans/<topic>/<domain>` when the domain is requested or already established; preserve existing document paths and show concrete paths in output
- Persist — after the user approves the Save gate, write to `<scope-dir>/research.md`; use the report template below, retaining evidence, baseline, alternatives, and limitations behind the reviewed conclusion
- On revisions, briefly identify changed findings or recommendations outside the document body; omit a separate recap

- Explain with a source-grounded example only when requested or needed in the saved report; label illustrative values and never imply an unrun reproduction

**Gates**

| Step | Prompt | n |
|------|--------|---|
| Save | Save findings? (topic or topic/domain to save, or n to skip) | Skip; no file written |

**Output — chat**

```text
<Direct conclusion or what remains uncertain.>
<One recommended next step; include a decisive limitation if needed.>

Want the evidence, or save these findings?
```

- Ask a blocking question instead of offering details or saving when input is required; otherwise the combined offer uses the existing Save gate
- Follow-ups answer the latest request without restarting the report. Use flat numbered items for independent questions or findings; no nested lists
- Show supporting evidence, options, and examples only when requested; preserve decision-changing risks in the short answer
- A request for evidence alone does not authorize saving; an explicit save request authorizes the Save gate

**Output — requested detail or saved report**

```markdown
**Purpose:** Research <question and scope>.

**Answer:** <conclusion>

**Baseline:** <inspected branch/revision and relevant working-tree changes>

**Findings:**

1. <fact or relevant alternative, with evidence and tradeoff>

**Next:** <one recommended next step>

**Open:**

1. <unresolved question ending in ?>
   Recommendation: <proposed answer and brief rationale>
```

- Saved reports retain material evidence, contrary findings, and limitations; omit Baseline when no code applies and Open when empty
- Requested explanations cover only the point asked about; do not print the full report unless requested
- After saving, confirm with one linked path, without repeating the findings
