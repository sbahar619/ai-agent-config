# Markdown Prompt Formatting

Best practices for authoring rules and slash commands in this repo.

For documentation command semantics, use [Documentation Command Conventions](documentation-conventions.md)
while authoring; keep each command's applicable instructions inline so it runs independently.

## Structure

- Open with a single direct description line — sets the task frame, highest model weight
- Use bold headers (`**Section**`) to separate major concerns — prevents the model from blurring Rules into Output
- Keep sections flat — avoid nested headers for small sections; they fragment context that should be read together

## Rules & constraints

- One bullet per constraint — one idea per line reduces ambiguity
- Bold within bullets (`**must not**`) adds little — skip it
- Merge small related sections rather than giving each its own header (e.g. "Check for" inside Rules)
- Fold pre-reply checks into Rules — one `Before replying:` bullet (or `Before each gate reply:` when gates exist); do not use a separate Self-verify section

## Gates

- Use a separate `**Gates**` section when the command has approve / retry workflow — not flat bullets in Rules
- Table columns: Step · Prompt · `n` (what happens on no / retry)
- One intro line when needed (e.g. "Skip when the user already approved that step")
- Gates are workflow state, not constraints — keep the table scannable; do not fold into Rules prose

## Output templates

- Always wrap in a code block — without it the model may treat the template as instructions rather than a format to reproduce
- Trailing format rules (omit empty sections, numbering logic) go as plain bullets after the code block, not inside it
- For routine chat replies, aim for 100–150 words, using fewer when sufficient; this is not a minimum or a hard cap. Preserve all material findings, evidence, limitations, and explicitly requested detail.
- Lead with the answer or verdict; state each finding, its evidence, and its action once. Omit empty sections, generic praise, repeated rationale, and closing recaps.
- Keep full guides, copy-ready text, and saved artifacts as detailed as their purpose requires; use links and short overviews for document commands. Include applicable brevity rules in each command so it works independently.

## Open questions

- Each numbered item must ask a concrete, unresolved question ending in `?`, followed by `Recommendation:` with a proposed answer and brief rationale
- Keep settled decisions and assumptions separate from open questions; never present statements as questions or invent questions to fill the section
- Omit the section when nothing remains unresolved; when user input is required, wait for answers before requesting approval

## Input

- One line is enough if the input is unambiguous — tables only when the input forms are genuinely non-obvious
- Behavioral rules about input (ask 1 question, don't proceed blindly) belong in Rules, not the Input section

## Impact (when editing)

- First line framing: high impact
- Section boundaries: high impact
- Code blocks for templates: essential
- Bold for inline emphasis: low impact, use sparingly
