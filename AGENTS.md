# AGENTS.md

Guidance for AI coding agents (Claude Code, OpenCode, Codex, etc.) working in this repository.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and editor prompt. There is no build step, and the repo should avoid wording that limits support to one or two harnesses.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `metadata.version`) followed by the canonical, numbered pattern list with before/after examples. **This is the source of truth.**
- `README.md` — for humans: installation, usage, a summary table of the patterns, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest. Its `"skills": ["./"]` key points the plugin loader at the repo root; without it, Claude Desktop installs the plugin but finds no skill. Keep `SKILL.md` a single regular file at the root rather than reintroducing a `skills/humanizer/SKILL.md` symlink, which upstream tried and then reverted.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add jooray/humanizer` works.
- `scripts/validate-package.py` — dependency-free package and synchronization checks used locally and in CI.

## The maintenance contract

`SKILL.md` and `README.md` must stay in sync. When you change behavior or content:

- **Patterns:** the skill currently defines **54 numbered patterns**, of which #45-54 apply only to Slovak and Czech text and two of them (#45, #46) deliberately override English-only rules. `validate-package.py` derives the count from `SKILL.md` and requires the README table and its "N Patterns Detected" heading to match, so update all three in the same change. Keep numbering stable unless you are deliberately renumbering.
- **Size:** `SKILL.md` has an 800-line portability budget (raised from 500 in 2.11.0 to fit the Slovak and Czech section and the imported patterns). The whole prompt loads into context on every invocation, so treat the budget as real. If a future change needs substantially more room, the fix is to move conditional material into `references/` files that load on demand rather than to raise the ceiling again.
- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`, `README.md` has a "Version History" section, and `.claude-plugin/plugin.json` has a `version` field. Bump them together so package metadata matches the skill. Keep the skill version under `metadata`; a top-level `version` key is not portable across Agent Skills hosts. (`marketplace.json` intentionally omits a version so `plugin.json` stays the package source of truth.)
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and other harnesses are examples, not limits.
- **Validation:** run `python3 scripts/validate-package.py`, `npx skills add . --list`, and `claude plugin validate .` before publishing.
- **Upstream:** this fork has diverged on purpose. Upstream `blader/humanizer` rewrote its prompt in Plain Language for 2.11.0 and renumbered to 35 patterns, so a plain `git merge origin/main` is not the way to take upstream work; port the individual patterns and packaging fixes and record what was skipped in the README version history. Both repos also used the numbers 2.11.0 and 2.11.1 for unrelated releases, so upstream version numbers are not comparable to this fork's.
- **Non-obvious fixes:** if you change the prompt to handle a tricky failure mode (a repeated mis-edit, an unexpected tone shift), add a short note to the README version history explaining what was fixed and why.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code.
