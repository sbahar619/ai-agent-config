"""Regression checks for command extraction and generated-skill freshness."""

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "generate_review_skill", ROOT / "scripts/generate-review-skill.py"
)
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


class GenerateReviewSkillTests(unittest.TestCase):
    def test_embeds_all_selected_criteria_without_per_command_gates(self):
        rendered = generator.render(ROOT)
        for name in generator.COMMANDS:
            with self.subTest(command=name):
                self.assertIn(f"### {name}\n", rendered)
                self.assertIn(f"Source: commands/{name}.md", rendered)
        self.assertIn("A case is unique if it covers a distinct branch OR", rendered)
        self.assertIn("No commits, push, amend, or PRs.", rendered)
        self.assertNotIn("Show the table report?", rendered)
        self.assertNotIn("Want the explanation?", rendered)
        self.assertEqual(rendered.count("Happy with implementation?"), 1)

    def test_rule_changes_propagate_with_optional_frontmatter(self):
        source = (ROOT / "commands/review-clarity.md").read_text()
        rule = "- Preserve the documented public contract"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-clarity.md"
            path.write_text("---\ndescription: Example\n---\n" + source.replace(
                "**Rules**", f"**Rules**\n\n{rule}"
            ))
            rendered = generator.render_command(path)
        self.assertIn(rule, rendered)
        self.assertNotIn("description: Example", rendered)

    def test_changed_structure_or_adaptation_fails(self):
        source = (ROOT / "commands/review-test-cases.md").read_text()
        variants = (
            source.replace("**Rules**", "**Criteria**"),
            source.replace("wait for approval before showing", "ask before showing"),
            "---\ndescription: Unclosed header\n" + source,
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-test-cases.md"
            for variant in variants:
                with self.subTest(source=variant[:80]):
                    path.write_text(variant)
                    with self.assertRaises(ValueError):
                        generator.render_command(path)

    def test_check_detects_drift_without_overwriting_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "commands", root / "commands")
            (root / "scripts").mkdir()
            for name in ("generate-review-skill.py", "review-and-fix.template.md"):
                shutil.copy2(ROOT / "scripts" / name, root / "scripts" / name)
            command = [sys.executable, str(root / "scripts/generate-review-skill.py")]
            subprocess.run(command, check=True, capture_output=True, text=True)
            subprocess.run(command + ["--check"], check=True, capture_output=True, text=True)
            output = root / "skills/review-and-fix/SKILL.md"
            original = output.read_text()
            source = root / "commands/review-clarity.md"
            source.write_text(source.read_text().replace("**Rules**", "**Rules**\n\n- New criterion"))
            result = subprocess.run(command + ["--check"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("stale", result.stderr)
            self.assertEqual(output.read_text(), original)
            source.unlink()
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_text(), original)


if __name__ == "__main__":
    unittest.main()
