# Humanizer

[![skills.sh installs](https://skills.sh/b/blader/humanizer)](https://skills.sh/blader/humanizer)

A portable agent skill that removes signs of AI-generated writing from text, making it sound more natural and human. It is plain Markdown, so it can run in any harness that supports skill-style instructions.

## Installation

### Skills CLI

Install globally with the cross-agent skills CLI so Humanizer is available in every project:

```bash
npx skills add jooray/humanizer --global
```

Update an existing install:

```bash
npx skills update humanizer --global
```

To install globally into every supported agent harness:

```bash
npx skills add jooray/humanizer --global --agent '*'
```

To target one configured harness, pass its agent name:

```bash
npx skills add jooray/humanizer --global --agent <agent-name>
```

Copy-paste versions for three common harnesses:

```bash
npx skills add jooray/humanizer --global --agent opencode
npx skills add jooray/humanizer --global --agent codex
npx skills add jooray/humanizer --global --agent pi
```

Pi also discovers globally installed skills from `~/.pi/agent/skills/`; invoke Humanizer with `/skill:humanizer` or just ask Pi to humanize text.

Omit `--global` for a project-local install that can be committed and shared with collaborators. Start a new agent session or reload skills after installation.

### Claude Code plugin

Claude Code users can also install Humanizer as a plugin:

```
/plugin marketplace add jooray/humanizer
/plugin install humanizer@humanizer
```

The skill is then invoked as `/humanizer:humanizer`.

### Manual

Any agent harness can use the skill directly because the runtime artifact is `SKILL.md`. Install it wherever your harness expects skill directories, or copy `SKILL.md` into an existing skill folder.

For example:

```bash
git clone https://github.com/jooray/humanizer.git /path/to/your/skills/humanizer
```

Or, if you already have this repo cloned:

```bash
mkdir -p /path/to/your/skills/humanizer
cp SKILL.md /path/to/your/skills/humanizer/
```

## Usage

Invoke the skill however your agent harness exposes installed skills. Common forms include a slash command or a direct request:

```
/humanizer

[paste your text here]
```

```
Please humanize this text: [your text]
```

Point it at a file and the skill rewrites it in place:

```
Humanize the prose in docs/launch-post.md
```

### Voice Calibration

To match your personal writing style, provide a sample of your own writing:

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

The skill will analyze your sentence rhythm, word choices, and quirks, then apply them to the rewrite instead of producing generic "clean" output.

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comprehensive guide comes from observations of thousands of instances of AI-generated text.

The skill also includes a final "obviously AI generated" audit pass and a second rewrite, to catch lingering AI-isms in the first draft.

Rewrites follow a no-fabrication rule: they never add facts, names, dates, or citations that aren't in the source text. Specificity has to come from the source or the author, not from the rewrite.

Ask whether text reads as AI-written and the skill switches to detect mode: it quotes the offending phrases and names the patterns instead of rewriting, and it never outputs an overall AI-probability score.

### Key Insight from Wikipedia

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## 54 Patterns Detected (with Before/After Examples)

### Content Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..."; the appended stamp "...and the way matters" | "was established in 1989 as part of a wider decentralization"; cut the stamp |
| 2 | **Notability name-dropping** | "cited in NYT, BBC, FT, and The Hindu" | Trim the list; keep only sourced context |
| 3 | **Superficial -ing analyses** | "symbolizing... reflecting... showcasing..." | Remove, or keep only what the source supports |
| 4 | **Promotional language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague attributions** | "Experts believe it plays a crucial role" | Name a real source or cut the claim |
| 6 | **Formulaic challenges** | "Despite challenges... continues to thrive" | Keep the sourced facts; cut the boosterism |

### Language Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 7 | **AI vocabulary** | "Actually... additionally... testament... landscape... showcasing" | "also... remain common" |
| 8 | **Copula avoidance** | "serves as... features... boasts" | "is... has" |
| 9 | **Negative parallelisms / tailing negations** | "It's not just X, it's Y", "..., no guessing" | State the point directly |
| 10 | **Rule of three** | "innovation, inspiration, and insights" | Use natural number of items |
| 11 | **Staccato contrast** | "SimpleX. Not Telegram. Not WhatsApp." | State the contrast in one sentence |
| 12 | **Synonym cycling / repeated openings** | "protagonist... main character... central figure"; "She noted. She noted. She filed." | One name for one thing; merge or reshape the repeated opening |
| 13 | **False ranges** | "from the Big Bang to dark matter" | List topics directly |
| 14 | **Passive voice / subjectless fragments** | "No configuration file needed" | Name the actor when it helps clarity |

### Style Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 15 | **Em/en dashes** | "institutions—not the people—yet this continues—" | Cut them: periods, commas, colons, or parentheses |
| 16 | **Boldface overuse** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 17 | **Inline-header lists** | "**Performance:** Performance improved" | Convert to prose |
| 18 | **Title Case Headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 19 | **Emojis** | "🚀 Launch Phase: 💡 Key Insight:" | Remove emojis |
| 20 | **Curly quotes** | `said “the project”` | `said "the project"` |

### Communication Patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 21 | **Chatbot artifacts** | "I hope this helps! Let me know if..." | Remove entirely |
| 22 | **Cutoff disclaimers** | "While details are limited in available sources..." | Find sources or remove |
| 23 | **Sycophantic tone** | "Great question! You're absolutely right!" | Respond directly |

### Filler and Hedging

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 24 | **Filler phrases** | "In order to", "Due to the fact that" | "To", "Because" |
| 25 | **Excessive hedging** | "could potentially possibly" | "may" |
| 26 | **Generic conclusions** | "The future looks bright" | Specific plans or facts |
| 27 | **Hyphenated word pairs** | "cross-functional, data-driven, client-facing" | Drop hyphens on common word pairs |
| 28 | **Persuasive authority tropes** | "At its core, what matters is..." | State the point directly |
| 29 | **Signposting announcements** | "Let's dive in", "Here's what you need to know", "one thing that bit me, so pay attention" | Start with the content |
| 30 | **Fragmented headers** | "## Performance" + "Speed matters." | Let the heading do the work |
| 31 | **Diff-anchored writing** | "This function was added to replace..." | Describe what it does, not what changed |
| 32 | **Manufactured punchlines / staccato drama** | "It had no preference. No prior. No nostalgia." | Use varied sentence lengths and concrete claims |
| 33 | **Aphorism formulas** | "Symmetry is the language of trust" | Replace the formula with the actual claim |
| 34 | **Conversational rhetorical openers** | "Honestly? It depends..." | Remove the fake-candid setup |
| 35 | **Colon-reveal constructions** | "The best part: it learns." | State it as a plain sentence |
| 36 | **Performed rigor and candor** | "It's worth being precise here", "the honest version is", "let's say the quiet part out loud", "in one specific way", "it is worth stating" | Delete the announcement, keep the point |
| 37 | **Argument residue** | "While some might argue..." rebutting nobody; "a tempting approach would be..." rejecting an option nobody proposed | Cut the phantom rebuttal or option, state the position |
| 38 | **Reasoning-chain artifacts** | "Let me break this down. Step 1:" | Delete the scaffolding, keep the conclusion |
| 39 | **False agency** | "the data tells us", "the market rewards" | Name the actor or state the fact plainly |
| 40 | **Forensic residue** | `[Your Name]`, `citeturn0search0`, `utm_source=chatgpt.com`, zero-width chars | Strip and normalize to plain NFC text |
| 41 | **Structural uniformity** | Equal-length sections, all lists of three, a recap per section | Vary depth; apply the paragraph reshuffle test |
| 42 | **Connective tissue pile-up** | "Additionally... Moreover... Furthermore..." | Let sentence order carry the logic |
| 43 | **Hedged-enumeration openers** | "There are several factors to consider" | Give the specific answer first |
| 44 | **Treadmill effect** | Three paragraphs restating one idea | Merge; keep the clearest version |

### Slovak and Czech Text

Applied only when the text is Slovak or Czech. Most AI writing in these languages is a translated English draft, so the tells arrive as loan translations, English punctuation, and English word order. Two of these rules deliberately override the English-only rules above.

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 45 | **Quotation marks** (overrides #20) | `„som nepostihnuteľný”` | `„som nepostihnuteľný“` - keep the native low-high pair |
| 46 | **Dashes** (overrides #15) | `pobyt — a povinnosti — nie je`, `55—85 €` | Cut every em dash; keep the en dash in ranges (`55–85 €`) |
| 47 | **Copula avoidance** | "cédula predstavuje kľúčový dokument" | "cédula je doklad", or no verb at all |
| 48 | **Transgressive / participle padding** | "čím zdôraznil... reflektujúc..." | Cut the tail or promote it to a sentence |
| 49 | **Calqued AI vocabulary** | "kľúčový", "svedčí o", "v dnešnej dobe" | Plain equivalents; watch for clusters |
| 50 | **Pronoun and possessive spam** | "keď si ty otvoríš tvoj účet" | "keď si otváraš účet" - these languages are pro-drop |
| 51 | **English word order** | "Nová rezolúcia bola zverejnená v marci" | "V marci zverejnili novú rezolúciu" - new information last |
| 52 | **ty / vy register drift** | "pozri" and "pozrite" two sentences apart | Pick one form and hold it |
| 53 | **Typography and numbers** | "10%", "5,970", "July 6, 2026" | "10 %", "5 970", "6. júla 2026" |
| 54 | **Loanword handling** | "použi tento tool" / over-translated "proof of address" | Match the field's working vocabulary |

The section also carries its own false-positive list: the reflexive passive, long multi-clause sentences, free word order, and particles like *veď* and *však* are native features, not tells.


## Full Example

*(Illustration note: the rewrite below adds specifics, like the month and the neighborhoods, that stand in for details the author would supply. In a real session those come from the user; the skill asks rather than invents.)*

**Before (AI-sounding):**
> I recently spent five unforgettable days in Lisbon, and let me tell you — this city completely stole my heart. From the moment I arrived, I knew I was somewhere truly special.
>
> Nestled along the banks of the Tagus River, Lisbon stands as a vibrant testament to Portugal's enduring spirit, where rich history and modern energy intertwine at every turn. Yes, the famous hills are challenging — my legs certainly felt it! — but every climb rewards you with breathtaking, panoramic views that make it all worthwhile.
>
> No trip would be complete without riding the iconic Tram 28, winding through the city's most historic neighborhoods. And the food? Simply divine. The original pastéis de nata at Pastéis de Belém are a beloved national treasure, and savoring one still warm was a moment I will never forget.
>
> But what truly makes Lisbon special isn't just the sights — it's the feeling. Wander a few steps off the main squares and you'll discover a quieter, more authentic side: sun-drenched alleys, charming tiled facades, and friendly locals going about their daily lives, inviting you to slow down and savor every moment.
>
> Of course, the must-see São Jorge Castle offers stunning views over the rooftops below. The queues can be long, but the experience is absolutely worth it for any history buff or curious traveler.
>
> Would I go back? Absolutely. Lisbon isn't just a place to visit — it's a place to fall in love with, again and again. If you're dreaming of your next getaway, this is one destination that promises memories to last a lifetime. ✨

**After (Humanized):**
> I spent five days in Lisbon last October and still have mixed feelings about it. Beautiful, yes. Also harder on the knees than anyone warned me.
>
> The hills are the whole story and somehow never make the brochures. My hotel was up in Alfama, which photographs beautifully and translates, in practice, to climbing what felt like a six-story staircase every time I wanted coffee. By the second day my calves had opinions. I started planning each walk around which way was downhill, which is a strange way to see a city but probably an honest one.
>
> Everyone says to ride Tram 28, so I did, wedged against a stranger's backpack for forty minutes while three tour groups filmed the same corner. I would walk the route next time, or go before breakfast. The custard tarts, though, earn the fuss. I had one at a plain little place in Graça, still warm, and for about thirty seconds I understood why people build trips around pastry.
>
> What I did not expect was how quiet the city gets away from the main squares. Two blocks uphill from any plaza it turns into laundry lines, chipped tile, open windows, and old men watching football with the sound turned up. That is the Lisbon I keep thinking about, not the castle.
>
> The castle is fine. The view is great, the queue is long, and I spent more time shuffling toward the entrance than looking at anything once I got inside. If I had only two days, I would trade it for an afternoon of getting lost.
>
> I would go back, but in spring and with better shoes. Lisbon does not bend over backward to make things easy for you. I think I liked that, even when my legs disagreed.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Primary source
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - Maintaining organization
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT, © Peter Yang) - Inspired the colon-reveal pattern (#35), the "delete rather than repolish" fix for mic-drop closers (#33), and detect mode's no-score stance
- [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) (MIT) - Source for argument residue (#37), reasoning-chain artifacts (#38), false agency (#39), the forensic-residue checklist (#40), and hedged-enumeration openers (#43), which it grounds in the [HC3 corpus](https://arxiv.org/abs/2301.07597)
- [jpeggdev/humanize-writing](https://github.com/jpeggdev/humanize-writing) (MIT) - Source for structural uniformity (#41), the connective-tissue pile-up rule (#42), the treadmill effect (#44), and the "count a cluster once" consolidation principle in detection guidance

## Version History

- **2.12.5** - Three additions to #49, from annotations on a Slovak newsletter. The *negated triad*: #11's staccato contrast and #10's rule of three arrive comma-joined inside one sentence in Slovak and Czech ("nie bitcoin, nie Bitblik, nie protistranu", "žiadna burza, žiadna registrácia, ani e-mail") rather than split into fragments, so the period-delimited shape #11 looks for never appears; recasting the run in a different negative frame is not a fix, and the guard keeps negative concord and two-item negations. The candor list gains the honesty branch ("buďme úprimní", "úprimne povedané", "povedzme si to na rovinu") next to the "nahlas" phrasings it already had. The vocabulary list gains **dôvod veriť**, a calque of the advertising "reason to believe". A blunt stated opinion ("to je podľa mňa blbá rada") was considered for the candor list and rejected: it is an opinion with an author, which PERSONALITY AND SOUL and the human-writing signs exist to protect. No change to the 54 patterns.
- **2.12.4** - Added the *graded verdict* to #1 and its calqued Slovak form to #49: a clause appended to a sentence that rates the evidence instead of showing it ("and it is pretty unambiguous", "a je dosť jednoznačné"). #1 already covered the appended stamp, but 2.12.2 wrote its list in the significance register ("and the way matters"), so a stamp that graded how conclusive a source is rather than how much it mattered matched nothing. The hedge in front of the absolute is part of the tell, since *pretty* unambiguous concedes that the verdict was not earned; the guard is that *dosť* on its own is ordinary Slovak and Czech, in line with the particles the Slovak section already protects. No change to the 54 patterns.
- **2.12.3** - Added the *worth-saying certificate* to #36: "it is worth stating", "it is worth noting", "it bears repeating", "this needs saying". The writer rules that a claim deserves to be made and then makes it, though writing it down had already settled that. #24 caught only the sentence-initial filler form ("It is important to note that the data shows"), so the appended form went through untouched, and it appears in the same end-of-sentence slot as 2.12.2's significance stamp: "There is a trap in the reference, and it is worth stating." No change to the 54 patterns.
- **2.12.2** - Split the two halves of "in one specific way, and the way matters", a sentence that announces a detail and grades its importance without supplying either. #36 now names *asserted specificity*, where *specific*, *particular*, *precise*, or *exact* stands in for the specifics themselves; the pattern's rule already covered it, but its trigger list was verbal ("to be precise") and never matched the adjectival form. #1 now names the *appended significance stamp*, the conversational register of significance inflation ("and that distinction matters", "and it is not just academic"), which #1's encyclopedic word list missed for the same reason #36's list missed the announced caveat in 2.12.1. Both carry a guard: *specific* with the specifics present stays, and so does a sentence that says what follows from the thing mattering. No change to the 54 patterns.
- **2.12.1** - Named the *announced caveat* in #36: a noun phrase with no main verb that says a caveat is coming and rules on where it has to sit, then defers the caveat itself to the next sentence ("one caveat that has to sit up front, because it makes the comparison less clean than it looks"). Every phrase in #36's trigger list was first-person and verbal ("it's worth being precise", "to be fair"), so the impersonal noun-phrase version matched nothing and survived edits; #29 listed only the casual and tutorial signposts, and #14's fragments carry a fact rather than a promise of one. The 2.12.0 false-positive guard for useful disclaimers was also shielding it, and now distinguishes a caveat that is *stated*, which stays, from a sentence whose only content is that a caveat is coming, which goes. No change to the 54 patterns.
- **2.12.0** - Merged the parts of upstream `blader/humanizer` (through 2.11.2) that this fork was missing, and the OpenCode/Codex/Pi install commands from [@aljazceru](https://github.com/aljazceru). Upstream's 2.11.0 rewrote its whole prompt in Plain Language; that rewrite is deliberately not taken, because it renumbers to 35 patterns and would drop #36-54. Content taken instead: `gated` (figurative) and `quietly` join the #7 vocabulary list; #12 now covers repeated sentence openings as well as synonym cycling, with the caveat that the repeated *word* is not the defect; #29 covers casual-register announcements ("one thing that bit me, so pay attention to this part"), which used to escape because only the formal phrasings were listed; #37 absorbs upstream's rejected-fake-alternatives pattern, the same drafting residue with a discarded option in place of a discarded objection. Three false-positive guards added: deliberate repeated openings, useful disclaimers, and alternatives a reader would really weigh. The final audit now also asks whether the rewrite *lost* a claim. Packaging: `plugin.json` gains `"skills": ["./"]` so Claude plugin installs find the skill at the repo root, and the validator reads files as UTF-8 (fixing validation on Windows-default encodings) and checks both. No change to the 54 patterns.
- **2.11.1** - Extended #36 to name the candor preamble that says the next sentence out loud ("let's say the quiet part out loud", "this needs to be said out loud", "it has to be said", "let's name it"). The rule already covered these, but the trigger list did not, so they survived edits. Added the Slovak and Czech calque of the same move ("toto treba povedať nahlas", "povedzme si to otvorene") to #49. No change to the 54 patterns.
- **2.11.0** - Added pattern #36 (performed rigor and candor): text that announces its own precision, fairness, or honesty ("it's worth being precise here", "deserves verification, not just assertion", "the honest version is", "we won't undersell it", "we say it plainly") instead of delivering it. Extended #33 to cover portentous shorthand, where a concrete fact is swapped for an ominous possession ("it already has a date"). Imported #37-44 from other MIT-licensed humanizer projects (credited under References): argument residue, reasoning-chain artifacts, false agency, forensic residue, structural uniformity, connective-tissue pile-up, hedged-enumeration openers, and the treadmill effect. #41 is the skill's first structural rule, covering the paragraph reshuffle test. Added a Slovak and Czech section (#45-54) with its own false-positive list, because AI text in these languages is usually a translated English draft: #45 and #46 override the curly-quote and en-dash rules, which are wrong for native typography, and the rest cover copula avoidance (*predstavuje*), transgressive padding, calqued vocabulary, pro-drop violations, English word order, ty/vy drift, number and date conventions, and loanword handling. `SKILL.md`'s line budget rose from 500 to 800. 54 patterns total.
- **2.10.0** - Added pattern #35 (colon-reveal constructions) and a Detect Mode that quotes offending patterns instead of rewriting and never outputs an AI-probability score; expanded #34 with more faux-insight/rhetorical-setup phrasing and #33 with a delete-don't-repolish instruction for mic-drop closers. Ideas credited to [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT). 35 patterns total.
- **2.9.2** - Merged upstream's no-fabrication rule, invocation modes, and portability cleanup (nonportable frontmatter removed, package validation added) while keeping this fork's 34th pattern (staccato contrast) and the full worked example in the README. Fixed a long-standing README table that mislabeled several filler/hedging patterns as style patterns. No change to the 34 patterns.
- **2.9.1** - Improved distribution and portability: removed nonportable frontmatter and tool preapprovals, made global installation the documented default, added package validation, and removed the duplicated long-form example from the runtime prompt (kept in this README instead). No change to the 34 patterns.
- **2.9.0** - Added a no-fabrication rule: rewrites may not invent facts, names, dates, or citations not present in the source, and every example that modeled invented specifics was re-cut to use only source information. Replaced paragraph-count parity with an information-over-shape rule, made a user's voice sample outrank the em dash ban, and added invocation modes (pasted text / file / embedded). No change to the 34 patterns.
- **2.8.3** - Moved the skill version from the unsupported top-level frontmatter key to `metadata.version` for Agent Skills and Claude compatibility. No change to the 34 patterns.
- **2.8.2** - Replaced the full before/after example with a first-person Lisbon trip recap. The after now keeps the same topic, perspective, and rough length as the before while removing the AI tells without becoming clipped or slogan-like. No change to the 34 patterns.
- **2.8.1** - Added cross-agent installation docs, optional Claude Code plugin packaging, and a compact secondhand-text false-positive guard. No change to the 34 patterns.
- **2.8.0** - Added style/cadence patterns #32-34 for manufactured punchlines, aphorism formulas, and conversational rhetorical openers; expanded #21 to catch offer-to-continue chatbot closers. 34 patterns total.
- **2.7.0** - Added pattern #31 (diff-anchored writing); made em/en dashes a hard cut rather than "overuse"; expanded #22 to cover speculative gap-filling ("maintains a low profile"); fixed duplicate section numbering (two #13 sections). 31 patterns total.
- **2.6.0** - Cleanup pass: consolidated the duplicated workflow sections, gated the personality guidance to content where voice is wanted, removed the model-fingerprinting subsection, and condensed the worked example. No change to the 29 patterns.
- **2.5.1** - Added a passive-voice / subjectless-fragment rule, raising the total to 29 patterns
- **2.5.0** - Added patterns for persuasive framing, signposting, and fragmented headers; expanded negative parallelisms to cover tailing negations; tightened wording around em dash overuse; fixed frontmatter wording to use "filler phrases"
- **2.4.0** - Added voice calibration: match the user's personal writing style from samples
- **2.3.0** - Added pattern #25: hyphenated word pair overuse; added the staccato contrast pattern (the "Not X" pattern)
- **2.2.0** - Added a final "obviously AI generated" audit + second-pass rewrite prompts
- **2.1.1** - Fixed pattern #18 example (curly quotes vs straight quotes)
- **2.1.0** - Added before/after examples for all 24 patterns
- **2.0.0** - Complete rewrite based on raw Wikipedia article content
- **1.0.0** - Initial release

## License

MIT
