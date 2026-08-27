#!/usr/bin/env python3
"""Validate Humanizer's portable package surfaces without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / "SKILL.md"
SKILL = SKILL_PATH.read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
PLUGIN = json.loads(
    (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
)


def require(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


frontmatter = require(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must start with YAML frontmatter",
).group(1)

for nonportable_key in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(nonportable_key)}", frontmatter):
        raise SystemExit(f"Remove nonportable frontmatter key: {nonportable_key[:-1]}")

skill_version = require(
    re.search(r'(?m)^\s+version:\s*["\']([^"\']+)["\']\s*$', frontmatter),
    "SKILL.md metadata.version is missing",
).group(1)
readme_version = require(
    re.search(r"(?m)^- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README),
    "README version history is missing",
).group(1)

versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(versions) != 1:
    raise SystemExit(f"Version mismatch: {sorted(versions)}")

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Keep exactly one regular SKILL.md at the repo root")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit('plugin.json must set "skills": ["./"] for Claude plugin discovery')

pattern_numbers = [
    int(number)
    for number in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)
]
pattern_count = len(pattern_numbers)
if pattern_numbers != list(range(1, pattern_count + 1)):
    raise SystemExit(
        f"SKILL.md patterns must be numbered 1-N with no gaps, found {pattern_numbers}"
    )

readme_numbers = {
    int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)
}
if readme_numbers != set(range(1, pattern_count + 1)):
    raise SystemExit(
        f"README pattern table must contain patterns 1-{pattern_count}, "
        f"found {sorted(readme_numbers)}"
    )

readme_heading = re.search(r"(?m)^## ([0-9]+) Patterns Detected", README)
if not readme_heading:
    raise SystemExit("README is missing an 'N Patterns Detected' heading")
if int(readme_heading.group(1)) != pattern_count:
    raise SystemExit(
        f"README heading says {readme_heading.group(1)} patterns, "
        f"SKILL.md defines {pattern_count}"
    )

if len(SKILL.splitlines()) > 800:
    raise SystemExit("SKILL.md exceeds the 800-line portability budget")

print(f"Humanizer package v{skill_version} is valid")
