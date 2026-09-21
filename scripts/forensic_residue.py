#!/usr/bin/env python3
"""Find and remove forensic residue (SKILL.md pattern 40) in Markdown or text.

This is mechanical cleanup, not a writing check. It touches only characters
that are residue in themselves: chatbot citation tokens, chatbot tracking
parameters, invisible characters, and homoglyphs inside Latin words. Every
judgment about prose stays in SKILL.md, which does not know this file exists.

Unfilled templates are reported but never rewritten, because only the author
knows what belongs in the slot.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote_plus


MARKER_START = ""
MARKER_END = ""
MARKER_SEPARATOR = ""
MARKERS = MARKER_START + MARKER_END + MARKER_SEPARATOR

CITATION_RE = re.compile(
    "(?:"
    # Fully delimited payload; the closing marker is required so a stray
    # opening marker cannot swallow the rest of the line.
    f"{MARKER_START}cite{MARKER_SEPARATOR}[^{MARKER_END}\r\n]*{MARKER_END}"
    f"|{MARKER_START}?citeturn\\d+\\w*{MARKER_END}?"
    r"|:?contentReference\[oaicite:\d+\](?:\{index=\d+\})?"
    r"|\boai_citation[\w:-]*"
    ")",
    re.IGNORECASE,
)
URL_RE = re.compile(rf"https?://[^\s<>()\[\]{MARKERS}]+", re.IGNORECASE)
# Bare [date] and [name] are left out on purpose: they are how a real template
# marks a slot, and SKILL.md 22 quotes "as of [date]" as a trigger phrase.
TEMPLATE_RE = re.compile(
    r"\[(?:your name|your company|company name|client name|"
    r"insert [^\]\r\n]{1,40}|x{3,})\]",
    re.IGNORECASE,
)

# Values of utm_source that only a chatbot writes. SKILL.md 40 names these two.
CHATBOT_SOURCES = frozenset({"chatgpt.com", "perplexity", "perplexity.ai"})

# Invisible characters with no job in prose. U+00A0 is deliberately absent:
# Slovak and Czech typography uses it correctly after one-letter prepositions,
# so deciding whether one belongs is an editorial call, not a mechanical one.
INVISIBLE = {
    "​": "zero-width space (U+200B)",
    "­": "soft hyphen (U+00AD)",
    "⁠": "word joiner (U+2060)",
    "﻿": "zero-width no-break space (U+FEFF)",
}
# Joiners are residue between Latin letters and load-bearing everywhere else
# (emoji sequences, Persian, Indic scripts), so they are read in context.
CONTEXT_INVISIBLE = {
    "‌": "zero-width non-joiner (U+200C)",
    "‍": "zero-width joiner (U+200D)",
}
HOMOGLYPHS = {
    "А": "A", "В": "B", "Е": "E", "К": "K", "М": "M",
    "Н": "H", "О": "O", "Р": "P", "С": "C", "Т": "T",
    "Х": "X", "а": "a", "е": "e", "о": "o", "р": "p",
    "с": "c", "х": "x", "у": "y", "ѕ": "s", "і": "i",
    "ј": "j",
    "Α": "A", "Β": "B", "Ε": "E", "Η": "H", "Ι": "I",
    "Κ": "K", "Μ": "M", "Ν": "N", "Ο": "O", "Ρ": "P",
    "Τ": "T", "Υ": "Y", "Χ": "X", "α": "a", "ε": "e",
    "ι": "i", "κ": "k", "ν": "v", "ο": "o", "ρ": "p",
    "τ": "t", "υ": "u",
}
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


@dataclass(frozen=True)
class Finding:
    rule: str
    line: int
    column: int
    text: str
    message: str
    fixable: bool


@dataclass(frozen=True)
class _Candidate:
    start: int
    end: int
    replacement: str | None
    rule: str
    message: str
    report_start: int
    report_text: str


def _mask_text(segment: str) -> str:
    return re.sub(r"[^\r\n]", " ", segment)


def _mask_fences(text: str) -> str:
    fence_char = ""
    fence_length = 0
    output: list[str] = []

    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        if not fence_char:
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})", body)
            if not opening:
                output.append(line)
                continue
            fence_char = opening.group(1)[0]
            fence_length = len(opening.group(1))
            output.append(_mask_text(line))
            continue

        closing = re.match(r"^ {0,3}(`+|~+)[ \t]*$", body)
        output.append(_mask_text(line))
        if (
            closing
            and closing.group(1)[0] == fence_char
            and len(closing.group(1)) >= fence_length
        ):
            fence_char = ""
            fence_length = 0

    return "".join(output)


def _mask_indented_code(text: str) -> str:
    """Mask indented code blocks, leaving indented list continuations alone."""

    list_item = re.compile(r"^ {0,3}(?:[-*+]|\d+[.)])\s")
    indented = re.compile(r"^(?: {4,}|\t)\S")
    output: list[str] = []
    previous_blank = True
    last_content = ""
    in_code = False

    for line in text.splitlines(keepends=True):
        if not line.strip():
            output.append(line)
            previous_blank = True
            continue

        if indented.match(line) and (in_code or (previous_blank and not list_item.match(last_content))):
            in_code = True
            output.append(_mask_text(line))
        else:
            in_code = False
            output.append(line)

        last_content = line
        previous_blank = False

    return "".join(output)


def mask_nonprose(text: str, *, mask_links: bool = True) -> str:
    """Blank out non-prose Markdown regions without moving source coordinates."""

    masked = re.sub(
        r"^(?:﻿)?---[^\S\r\n]*\r?\n[\s\S]*?\r?\n(?:---|\.\.\.)[^\S\r\n]*(?:\r?\n|$)",
        lambda match: _mask_text(match.group(0)),
        text,
        count=1,
    )
    masked = _mask_fences(masked)
    masked = _mask_indented_code(masked)
    masked = re.sub(r"(`+)[^`\r\n]*?\1", lambda m: _mask_text(m.group(0)), masked)
    masked = re.sub(r"<!--[\s\S]*?-->", lambda m: _mask_text(m.group(0)), masked)
    masked = re.sub(
        r"^ {0,3}>.*$", lambda m: _mask_text(m.group(0)), masked, flags=re.MULTILINE
    )

    if mask_links:
        def mask_link(match: re.Match[str]) -> str:
            label, target = match.group(1), match.group(2)
            if label.startswith("!"):
                return _mask_text(match.group(0))
            return label + _mask_text(target)

        masked = re.sub(
            r"(!?\[[^\]\r\n]*\])(\([^\r\n)]*\)|\[[^\]\r\n]*\])", mask_link, masked
        )
        masked = re.sub(
            r"^( {0,3}\[[^\]\r\n]+\]:)([^\r\n]*)$",
            lambda m: m.group(1) + _mask_text(m.group(2)),
            masked,
            flags=re.MULTILINE,
        )
        masked = re.sub(
            r"<(?:https?://|mailto:)[^>\r\n]+>",
            lambda m: _mask_text(m.group(0)),
            masked,
            flags=re.IGNORECASE,
        )
        masked = URL_RE.sub(lambda m: _mask_text(m.group(0)), masked)

    return masked


def _line_column(text: str, index: int) -> tuple[int, int]:
    line = text.count("\n", 0, index) + 1
    line_start = text.rfind("\n", 0, index)
    return line, index - line_start


def _absorb_space(text: str, start: int, end: int) -> int:
    """Take the space in front of a deleted token when it would be left doubled."""

    if start == 0 or text[start - 1] not in " \t":
        return start
    following = text[end] if end < len(text) else "\n"
    if following in " \t\r\n" or following in ".,;:!?)]":
        return start - 1
    return start


def _trim_url(match: re.Match[str]) -> tuple[int, str]:
    trimmed = match.group(0).rstrip(".,;:!?\"'")
    return match.start(), trimmed


def _clean_tracking(url: str) -> tuple[str, str]:
    before_fragment, hash_separator, fragment = url.partition("#")
    base, query_separator, query = before_fragment.partition("?")
    if not query_separator:
        return url, ""

    kept: list[str] = []
    removed: list[str] = []
    for parameter in query.split("&"):
        key, equals, value = parameter.partition("=")
        if (
            equals
            and unquote_plus(key).lower() == "utm_source"
            and unquote_plus(value).lower() in CHATBOT_SOURCES
        ):
            removed.append(parameter)
            continue
        kept.append(parameter)

    if not removed:
        return url, ""
    rebuilt = base + (("?" + "&".join(kept)) if kept else "")
    if hash_separator:
        rebuilt += "#" + fragment
    return rebuilt, removed[0]


def _citation_candidates(text: str, prose: str) -> list[_Candidate]:
    candidates = []
    for match in CITATION_RE.finditer(prose):
        start = _absorb_space(text, match.start(), match.end())
        candidates.append(
            _Candidate(
                start,
                match.end(),
                "",
                "40-citation-token",
                "Remove the machine citation token.",
                match.start(),
                match.group(0),
            )
        )
    return candidates


def _tracking_candidates(text: str, surface: str) -> list[_Candidate]:
    candidates = []
    for match in URL_RE.finditer(surface):
        start, url = _trim_url(match)
        cleaned, parameter = _clean_tracking(url)
        if not parameter:
            continue
        candidates.append(
            _Candidate(
                start,
                start + len(url),
                cleaned,
                "40-tracking-parameter",
                "Remove the chatbot tracking parameter from the URL.",
                start + url.find(parameter),
                parameter,
            )
        )
    return candidates


def _invisible_candidates(text: str, prose: str) -> list[_Candidate]:
    candidates = []
    for index, character in enumerate(prose):
        name = INVISIBLE.get(character)
        if name:
            if character == "﻿" and index == 0:
                continue  # a byte order mark at the head of the file is legitimate
        elif character in CONTEXT_INVISIBLE:
            before = prose[index - 1] if index else " "
            after = prose[index + 1] if index + 1 < len(prose) else " "
            if not (before.isascii() and after.isascii()):
                continue  # emoji sequences and Persian or Indic text need the joiner
            name = CONTEXT_INVISIBLE[character]
        else:
            continue
        candidates.append(
            _Candidate(
                index,
                index + 1,
                "",
                "40-invisible-character",
                f"Remove the {name}.",
                index,
                name,
            )
        )
    return candidates


def _homoglyph_candidates(text: str, prose: str) -> list[_Candidate]:
    candidates = []
    for word in WORD_RE.finditer(prose):
        token = word.group(0)
        confusables = [character for character in token if character in HOMOGLYPHS]
        if not confusables:
            continue
        latin = [character for character in token if character.isascii()]
        if len(latin) < 2:
            continue  # a word in another script, or a lone Greek variable, is not residue
        fixable = all(
            character.isascii() or character in HOMOGLYPHS for character in token
        )
        for offset, character in enumerate(token):
            if character not in HOMOGLYPHS:
                continue
            index = word.start() + offset
            candidates.append(
                _Candidate(
                    index,
                    index + 1,
                    HOMOGLYPHS[character] if fixable else None,
                    "40-homoglyph",
                    f"Replace U+{ord(character):04X} with Latin "
                    f"{HOMOGLYPHS[character]!r} in {token!r}.",
                    index,
                    character,
                )
            )
    return candidates


def _template_candidates(text: str, prose: str) -> list[_Candidate]:
    return [
        _Candidate(
            match.start(),
            match.end(),
            None,
            "40-unfilled-template",
            "Fill in the template slot or delete it.",
            match.start(),
            match.group(0),
        )
        for match in TEMPLATE_RE.finditer(prose)
    ]


def _collect(text: str) -> list[_Candidate]:
    prose = mask_nonprose(text)
    url_surface = mask_nonprose(text, mask_links=False)
    candidates = (
        _citation_candidates(text, prose)
        + _tracking_candidates(text, url_surface)
        + _invisible_candidates(text, prose)
        + _homoglyph_candidates(text, prose)
        + _template_candidates(text, prose)
    )
    return sorted(candidates, key=lambda candidate: (candidate.start, candidate.rule))


def scan_text(text: str) -> list[Finding]:
    findings = []
    for candidate in _collect(text):
        line, column = _line_column(text, candidate.report_start)
        findings.append(
            Finding(
                candidate.rule,
                line,
                column,
                candidate.report_text,
                candidate.message,
                candidate.replacement is not None,
            )
        )
    return sorted(findings, key=lambda finding: (finding.line, finding.column, finding.rule))


def apply_safe_fixes(text: str) -> tuple[str, int]:
    """Apply the mechanical fixes only, and report how many were applied."""

    applied: list[_Candidate] = []
    for candidate in _collect(text):
        if candidate.replacement is None:
            continue
        if applied and candidate.start < applied[-1].end:
            continue  # never let two edits touch the same characters
        applied.append(candidate)

    result = text
    for candidate in reversed(applied):
        result = result[: candidate.start] + candidate.replacement + result[candidate.end :]
    return result, len(applied)


def _write_atomic(path: Path, content: str) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Report or remove forensic residue. It does not judge prose."
    )
    parser.add_argument("path", type=Path, help="UTF-8 Markdown or text file")
    parser.add_argument(
        "--fix", action="store_true", help="remove the residue instead of only reporting it"
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    arguments = parser.parse_args(argv)

    given = arguments.path.expanduser()
    if given.is_symlink():
        parser.error(f"path must be a regular, non-symlink file: {given}")
    path = given.resolve()
    if not path.is_file():
        parser.error(f"path must be a regular, non-symlink file: {path}")

    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            original = handle.read()
    except UnicodeDecodeError as error:
        parser.error(f"path is not valid UTF-8: {error}")

    fixed = 0
    content = original
    if arguments.fix:
        content, fixed = apply_safe_fixes(original)
        if content != original:
            _write_atomic(path, content)

    findings = scan_text(content)
    if arguments.json:
        print(
            json.dumps(
                {
                    "path": str(path),
                    "fixed": fixed,
                    "clean": not findings,
                    "findings": [asdict(finding) for finding in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        if fixed:
            print(f"removed {fixed} artifact(s) from {path}")
        for finding in findings:
            fixable = " [fixable]" if finding.fixable else ""
            print(
                f"{path}:{finding.line}:{finding.column}: {finding.rule}{fixable}: "
                f"{finding.message} ({finding.text!r})"
            )
        if not findings:
            print(f"{path}: clean")

    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
