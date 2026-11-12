#!/usr/bin/env python3
"""Build the self-contained review-and-fix skill from its template and commands."""

import argparse
import hashlib
from pathlib import Path
import re
import sys


COMMANDS = (
    "review-clarity",
    "review-duplication",
    "review-hardcoding",
    "review-redundancy",
    "review-simplify",
    "review-test-cases",
    "review-value",
    "implement",
)

# Only presentation-dependent clauses need rewriting inside retained rules.
# Exact matches make command changes require an explicit adapter review.
ADAPTATIONS = {
    "review-test-cases": (
        "- Before replying: confirm each flagged pair truly shares both branch and concern; drop uncertain flags; keep the initial response within the summary cap and wait for approval before showing the table report",
        "- Before replying: confirm each flagged pair truly shares both branch and concern; drop uncertain flags; return all supported pairs to the parent",
    ),
    "implement": (
        "output matches the completion template",
        "return task results to the parent workflow; its final output and Done gate apply once",
    ),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if output is stale")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    output = root / "skills/review-and-fix/SKILL.md"
    rendered = render(root)
    if args.check:
        if not output.exists() or output.read_text() != rendered:
            raise ValueError("Skill is stale; run python3 scripts/generate-review-skill.py")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered)


def render(root):
    template = (root / "scripts/review-and-fix.template.md").read_text()
    if template.count("{{COMMANDS}}") != 1:
        raise ValueError("Template must contain exactly one {{COMMANDS}} marker")
    commands = [render_command(root / "commands" / f"{name}.md") for name in COMMANDS]
    return template.replace("{{COMMANDS}}", "\n\n".join(commands))


def render_command(path):
    source = path.read_text()
    body = source
    if body.startswith("---\n"):
        header = re.match(r"\A---\n.*?\n---\n", body, re.DOTALL)
        if not header:
            raise ValueError(f"{path.name}: unclosed frontmatter")
        body = body[header.end():]
    # All selected commands have Input, Rules, then Gates and/or Output.
    # Fail on a changed structure instead of silently losing review criteria.
    sections = re.split(r"(?m)^(\*\*(?:Input|Rules|Gates|Output)[^\n]*\*\*[^\n]*)$", body)
    headings = sections[1::2]
    expected = ["Input", "Rules", "Gates", "Output"] if path.stem in ADAPTATIONS else ["Input", "Rules", "Output"]
    names = [re.match(r"\*\*(Input|Rules|Gates|Output)", heading).group(1) for heading in headings]
    # The test review has two output formats.
    if path.stem == "review-test-cases":
        expected.append("Output")
    if names != expected or headings[1] != "**Rules**":
        raise ValueError(f"{path.name}: unexpected command sections; review the adapter")
    retained = "".join(sections[:5]).strip()
    if not sections[4].strip():
        raise ValueError(f"{path.name}: empty Rules")
    if path.stem in ADAPTATIONS:
        old, new = ADAPTATIONS[path.stem]
        if retained.count(old) != 1:
            raise ValueError(f"{path.name}: changed adaptation clause; review the adapter")
        retained = retained.replace(old, new)
    retained = re.sub(r"\A# [^\n]+\n+", "", retained)
    digest = hashlib.sha256(source.encode()).hexdigest()
    return f"### {path.stem}\n\n<!-- Source: commands/{path.name}; sha256: {digest} -->\n\n{retained}"


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        sys.exit(str(error))
