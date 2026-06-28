# Markdown Prompt Formatting

Best practices for authoring rules and slash commands in this repo.

## Structure

- Open with a single direct description line — sets the task frame, highest model weight
- Use bold headers (`**Section**`) to separate major concerns — prevents the model from blurring Rules into Output
- Keep sections flat — avoid nested headers for small sections; they fragment context that should be read together

## Rules & constraints

- One bullet per constraint — one idea per line reduces ambiguity
- Bold within bullets (`**must not**`) adds little — skip it
- Merge small related sections rather than giving each its own header (e.g. "Check for" inside Rules)

## Output templates

- Always wrap in a code block — without it the model may treat the template as instructions rather than a format to reproduce
- Trailing format rules (omit empty sections, numbering logic) go as plain bullets after the code block, not inside it

## Input

- One line is enough if the input is unambiguous — tables only when the input forms are genuinely non-obvious
- Behavioral rules about input (ask 1 question, don't proceed blindly) belong in Rules, not the Input section

## Impact (when editing)

- First line framing: high impact
- Section boundaries: high impact
- Code blocks for templates: essential
- Bold for inline emphasis: low impact, use sparingly
