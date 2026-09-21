#!/usr/bin/env python3
"""Tests for the forensic residue cleanup."""

from __future__ import annotations

import importlib.util
import io
import stat
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("forensic_residue.py")
SPEC = importlib.util.spec_from_file_location("forensic_residue", MODULE_PATH)
assert SPEC and SPEC.loader
RESIDUE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = RESIDUE
SPEC.loader.exec_module(RESIDUE)

START, END, SEPARATOR = "", "", ""
REPO_ROOT = MODULE_PATH.parent.parent


class CitationTests(unittest.TestCase):
    def test_removes_every_token_shape(self) -> None:
        text = (
            "One citeturn0search0 two contentReference[oaicite:3]{index=3} "
            f"three oai_citation:1 four {START}cite{SEPARATOR}turn1news2{END} five."
        )

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual(count, 4)
        self.assertEqual(fixed, "One two three four five.")
        self.assertEqual(RESIDUE.scan_text(fixed), [])

    def test_stray_opening_marker_does_not_eat_the_line(self) -> None:
        text = f"Claim {START}cite{SEPARATOR}turn0search0 and the rest of the sentence."

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual(count, 0)
        self.assertEqual(fixed, text)

    def test_reports_position_of_the_token_not_the_absorbed_space(self) -> None:
        findings = RESIDUE.scan_text("Line one.\nA claim citeturn0search0 here.")

        self.assertEqual(
            [(f.rule, f.line, f.column, f.fixable) for f in findings],
            [("40-citation-token", 2, 9, True)],
        )


class TrackingParameterTests(unittest.TestCase):
    def test_keeps_the_rest_of_the_url(self) -> None:
        text = "See https://example.com/a?x=1&utm_source=chatgpt.com&y=2#part."

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual(count, 1)
        self.assertEqual(fixed, "See https://example.com/a?x=1&y=2#part.")

    def test_cleans_link_destinations_and_other_chatbot_sources(self) -> None:
        text = "[source](https://example.com/?utm_source=perplexity.ai)"

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual(count, 1)
        self.assertEqual(fixed, "[source](https://example.com/)")

    def test_leaves_ordinary_campaign_parameters(self) -> None:
        text = "https://example.com/?utm_source=newsletter&utm_medium=email"

        self.assertEqual(RESIDUE.apply_safe_fixes(text), (text, 0))


class InvisibleCharacterTests(unittest.TestCase):
    def test_removes_characters_with_no_job_in_prose(self) -> None:
        text = "so​ft­ly"

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual((fixed, count), ("softly", 2))

    def test_keeps_joiners_that_hold_a_sequence_together(self) -> None:
        text = "family \U0001f468‍\U0001f469‍\U0001f467 here"

        self.assertEqual(RESIDUE.apply_safe_fixes(text), (text, 0))
        self.assertEqual(RESIDUE.scan_text(text), [])

    def test_removes_a_joiner_between_latin_letters(self) -> None:
        self.assertEqual(RESIDUE.apply_safe_fixes("wo‌rd"), ("word", 1))

    def test_keeps_a_byte_order_mark_at_the_head_of_the_file(self) -> None:
        self.assertEqual(RESIDUE.apply_safe_fixes("﻿Title"), ("﻿Title", 0))
        self.assertEqual(RESIDUE.apply_safe_fixes("Title﻿"), ("Title", 1))


class HomoglyphTests(unittest.TestCase):
    def test_repairs_a_latin_word_carrying_cyrillic_letters(self) -> None:
        text = "The Сompany рaid."  # Cyrillic Es and er

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual((fixed, count), ("The Company paid.", 2))

    def test_leaves_words_written_in_another_script(self) -> None:
        for text in ("Москва is a city.", "Use νt in the formula."):
            with self.subTest(text=text):
                self.assertEqual(RESIDUE.apply_safe_fixes(text), (text, 0))

    def test_leaves_accented_latin_alone(self) -> None:
        text = "Toto je príklad, ktorý má diakritiku."

        self.assertEqual(RESIDUE.apply_safe_fixes(text), (text, 0))


class ProtectedRegionTests(unittest.TestCase):
    def test_masks_code_quotes_frontmatter_and_image_payloads(self) -> None:
        text = "\n".join(
            [
                "---",
                "source: citeturn0search0",
                "---",
                "",
                "`citeturn0search0` stays.",
                "",
                "> citeturn1search2",
                "",
                "```text",
                "citeturn2search1 https://e.test/?utm_source=chatgpt.com",
                "```",
                "",
                "    citeturn3search1",
                "",
                "<!-- citeturn4search1 -->",
                "",
                "Real citeturn5search1 residue.",
            ]
        )

        fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual(count, 1)
        self.assertEqual(fixed.count("citeturn"), 6)
        self.assertIn("Real residue.", fixed)

    def test_does_not_mask_an_indented_list_continuation(self) -> None:
        text = "- item\n\n    A citeturn0search0 continuation.\n"

        _fixed, count = RESIDUE.apply_safe_fixes(text)

        self.assertEqual(count, 1)

    def test_this_repository_is_clean(self) -> None:
        for name in ("SKILL.md", "README.md", "AGENTS.md"):
            with self.subTest(file=name):
                text = (REPO_ROOT / name).read_text(encoding="utf-8")
                self.assertEqual(RESIDUE.scan_text(text), [])


class UnfilledTemplateTests(unittest.TestCase):
    def test_reports_without_rewriting(self) -> None:
        findings = RESIDUE.scan_text("Dear [Your Name], signed [insert date].")

        self.assertEqual([finding.rule for finding in findings], ["40-unfilled-template"] * 2)
        self.assertTrue(all(not finding.fixable for finding in findings))
        self.assertEqual(RESIDUE.apply_safe_fixes("Dear [Your Name].")[1], 0)


class FileHandlingTests(unittest.TestCase):
    def test_fix_preserves_crlf_and_file_mode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "draft.md"
            path.write_bytes(b"First.\r\nA citeturn0search0 claim.\r\n")
            path.chmod(0o640)

            with redirect_stdout(io.StringIO()):
                exit_code = RESIDUE.main([str(path)])
                self.assertEqual(exit_code, 1)
                self.assertEqual(RESIDUE.main(["--fix", str(path)]), 0)

            self.assertEqual(path.read_bytes(), b"First.\r\nA claim.\r\n")
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)

    def test_refuses_a_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "real.md"
            target.write_text("citeturn0search0", encoding="utf-8")
            link = Path(directory) / "link.md"
            link.symlink_to(target)

            with self.assertRaises(SystemExit) as raised, redirect_stderr(io.StringIO()):
                RESIDUE.main(["--fix", str(link)])

            self.assertEqual(raised.exception.code, 2)
            self.assertEqual(target.read_text(encoding="utf-8"), "citeturn0search0")


if __name__ == "__main__":
    unittest.main()
