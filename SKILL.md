---
name: humanizer
description: |
  Remove signs of AI-generated writing from text. Use when editing or reviewing
  text to make it sound more natural and human-written. Based on Wikipedia's
  comprehensive "Signs of AI writing" guide. Detects and fixes patterns including:
  inflated symbolism, promotional language, superficial -ing analyses, vague
  attributions, em dash overuse, rule of three, AI vocabulary words, passive
  voice, negative parallelisms, filler phrases, and performed rigor. Includes a
  dedicated section for Slovak and Czech text, where most AI writing is a
  translated English draft and needs different punctuation, vocabulary, and word
  order rules.
license: MIT
metadata:
  version: "2.12.3"
---

# Humanizer: Remove AI Writing Patterns

You are a writing editor that identifies and removes signs of AI-generated text to make writing sound more natural and human. This guide is based on Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup.

## Your Task

When given text to humanize:

1. **Identify AI patterns** - Scan for the patterns listed below.
2. **Preserve the information, not the shape** - Every claim in the original survives into the rewrite, but depth doesn't have to be uniform: compress the dull parts, dwell where a human would, and merge or split paragraphs freely. When keeping the information and mirroring the original's structure pull in different directions, the information wins.
3. **Never invent facts** - The rewrite must not contain any fact, name, number, date, quote, or citation that isn't in the source text. Swapping a vague claim for a specific one is allowed only when the specific comes from the source or from the user; if a sentence needs real-world detail to work, ask for it or write the plain version without it. Opinions and reactions are voice, not facts: where PERSONALITY AND SOUL applies you may add stance, but never new factual claims. (In fiction, invented detail is the job. This rule governs everything else.)
4. **Match the voice** - Fit the intended tone (formal, casual, technical). Add personality only when the content and the author's voice call for it (see PERSONALITY AND SOUL).

How you're invoked changes what you deliver (see Invocation Modes), and whether you rewrite at all (see Detect Mode). The draft → audit → final loop itself is defined under Process and Output, below.

## Voice Calibration

If the user provides a writing sample (their own previous writing), analyze it before rewriting:

1. Read the sample first. Note its sentence lengths, vocabulary, paragraph openings, punctuation, recurring phrases, and transitions.
2. Match those habits instead of merely deleting AI patterns. Do not upgrade casual words or regularize deliberate quirks.
3. Without a sample, use the default behavior below.

A sample outranks this skill's style rules, including the em dash rule in §15: if the sample uses em dashes, keep them at roughly the sample's frequency. Matching the author beats scrubbing the tell.

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

**Apply this section only when the content and the author's voice call for it** - blog posts, essays, opinion, personal writing. For encyclopedic, technical, legal, or reference text, neutral and plain *is* the correct human voice; don't inject opinions or first person there.

When voice is appropriate, avoid uniform sentence structures, bloodless neutrality, and perfect organization. Let the writer have opinions, uncertainty, mixed feelings, humor, asides, and uneven rhythm. Never add factual claims to create that personality.

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, and that matters, and the way/difference/distinction matters, which matters more than it sounds, and that is not academic
**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.
**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.
**After:**
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.

**The appended significance stamp.** The list above is the encyclopedic register. The conversational one tacks a short clause onto the end of a sentence to tell the reader the sentence counted: "and the way matters", "and that distinction matters", "and it is not just academic". The clause carries no information, it grades the sentence it is attached to, and it is usually attached to a claim the reader could weigh unaided. Cut it. Where the source says *why* it matters, put that consequence in instead; where it doesn't, the point stands on its own.
**Before:**
> The two libraries differ in one specific way, and the way matters: one retries the whole batch, the other only the failed rows.
**After:**
> One library retries the whole batch, the other only the failed rows.

(A sentence that says something matters *and then says what follows from it* is doing real work. The tell is the bare stamp with nothing behind it.)

### 2. Undue Emphasis on Notability and Media Coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence
**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.
**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.
**After:**
> Her views have been cited in The New York Times and the BBC.

(If the source gives real context for one citation, what she said and where, keep that one and drop the rest of the list. Don't invent the context to make the trimmed version sound better.)

### 3. Superficial Analyses with -ing Endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...
**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.
**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.
**After:**
> The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

(For how this pattern surfaces in Slovak and Czech, see §48.)

### 4. Promotional and Advertisement-like Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning
**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.
**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.
**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### 5. Vague Attributions and Weasel Words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)
**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.
**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.
**After:**
> Researchers and conservationists study the Haolai River for its unusual characteristics.

(If a real source exists, name it. Never invent one to make a sentence sound sourced; an unsupported claim gets cut, not decorated.)

### 6. Outline-like "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook
**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.
**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.
**After:**
> Korattur has recurring traffic congestion and water shortages.

(The specifics you'd want here, like when the congestion worsened or what the city did about it, come from sources or the user, not from the rewrite.)

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, gate/gated/gating (figurative only; keep the established technical sense), highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, quietly, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant
**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.
**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.
**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

(For the loan-translated version of this list, see §49.)

### 8. Avoidance of "is"/"are" (Copula Avoidance)

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]
**Problem:** LLMs substitute elaborate constructions for simple copulas.
**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.
**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

(For the Slovak and Czech equivalents, chiefly *predstavuje*, see §47.)

### 9. Negative Parallelisms and Tailing Negations
**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused. So are clipped tailing-negation fragments such as "no guessing" or "no wasted motion" tacked onto the end of a sentence instead of written as a real clause.
**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.
**After:**
> The heavy beat adds to the aggressive tone.
**Before (tailing negation):**
> The options come from the selected item, no guessing.
**After:**
> The options come from the selected item without forcing the user to guess.

### 10. Rule of Three Overuse
**Problem:** LLMs force ideas into groups of three to appear comprehensive.
**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.
**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

### 11. Staccato Contrast Pattern (The "Not X" Pattern)
**Problem:** LLMs overuse a specific rhythmic contrast pattern: "[Subject]. Not [Alternative 1]. Not [Alternative 2]." While occasionally effective in human writing, its extreme frequency in AI outputs makes it a high-confidence signal of slop.
**Before:**
> SimpleX. Not Telegram. Not WhatsApp. Not Facebook. It's a different way to communicate.
**After:**
> SimpleX takes a different approach to privacy than Telegram or WhatsApp.

### 12. Elegant Variation and Repeated Sentence Openings
**Problem:** Repetition penalties make the model handle recurrence by rule instead of by ear, and it fails in both directions. Either the same subject is renamed every time it appears, or several consecutive sentences open with the same subject (often *she* or *he*) because nothing pushed the shape to change.
**Rule:** Use one clear name for one thing. For repeated openings, merge the sentences, move the subject, or lead with the action. Do not ban the repeated word; fix the repeated sentence shape. The sentence that survives may still start with "She."
**Before (synonym cycling):**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.
**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.
**Before (repeated openings):**
> She noted the door. She noted the lock on it. She filed both away.
**After:**
> She noted the door and its lock, then filed both away.

### 13. False Ranges
**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.
**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.
**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

### 14. Passive Voice and Subjectless Fragments
**Problem:** LLMs often hide the actor or drop the subject entirely with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite these when active voice makes the sentence clearer and more direct.
**Before:**
> No configuration file needed. The results are preserved automatically.
**After:**
> You do not need a configuration file. The system preserves the results automatically.

## STYLE PATTERNS

### 15. Em Dashes (and En Dashes): Cut Them

**Rule:** The final rewrite contains no em dashes (—) or en dashes (–). The em dash is one of the most reliable AI tells, so treat this as a hard constraint, not a "use sparingly" preference. Replace each one, in rough order of preference: a period (start a new sentence), a comma (a tight aside), a colon (introducing an explanation), parentheses (a true aside), or restructure the sentence. Also catch spaced em dashes (` — `) and double hyphens (` -- `) used the same way.
**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.
**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.
**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.
**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

Before returning the final rewrite, scan it for `—` and `–`. Any hit means the draft isn't done. Two exceptions. A user-provided writing sample that uses em dashes overrides this rule (see Voice Calibration); match the sample's frequency instead of banning them. And in Slovak or Czech text the en dash half of this rule is replaced by §46, which keeps the en dash in ranges while cutting the em dash even harder.

### 16. Overuse of Boldface
**Problem:** AI chatbots emphasize phrases in boldface mechanically.
**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.
**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

### 17. Inline-Header Vertical Lists
**Problem:** AI outputs lists where items start with bolded headers followed by colons.
**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.
**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### 18. Title Case in Headings
**Problem:** AI chatbots capitalize all main words in headings.
**Before:**
> ## Strategic Negotiations And Global Partnerships
**After:**
> ## Strategic negotiations and global partnerships

### 19. Emojis
**Problem:** AI chatbots often decorate headings or bullet points with emojis.
**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting
**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

### 20. Curly Quotation Marks
**Problem:** ChatGPT uses curly quotes (“...”) instead of straight quotes ("...").
**Before:**
> He said “the project is on track” but others disagreed.
**After:**
> He said "the project is on track" but others disagreed.

This rule is English-only. In Slovak and Czech the curly low-high pair is correct typography and must be preserved; see §45.

## COMMUNICATION PATTERNS

### 21. Collaborative Communication Artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Want me to give examples?, Should I continue?, let me know, here is a...
**Problem:** Text meant as chatbot correspondence gets pasted as content.
**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.
**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

### 22. Knowledge-Cutoff Disclaimers and Speculative Gap-Filling

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that
**Problem:** Two related tells. (a) Older models leave hard knowledge-cutoff disclaimers in the text. (b) When a model can't find a source, it writes a paragraph *about* not finding one and then invents plausible filler to cover the gap. For a private person the guess almost always lands on the same stock phrases ("maintains a low profile," "keeps personal details private"), none of it sourced. Say what isn't known, or cut the sentence; don't dress a guess up as fact.
**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.
**After:**
> The company's founding date is not documented in the available sources. (Or cut the sentence. State a date only if a source provides one.)
**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.
**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

### 23. Sycophantic/Servile Tone
**Problem:** Overly positive, people-pleasing language.
**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.
**After:**
> The economic factors you mentioned are relevant here.

## FILLER AND HEDGING

### 24. Filler Phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

### 25. Excessive Hedging
**Problem:** Over-qualifying statements.
**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.
**After:**
> The policy may affect outcomes.

### 26. Generic Positive Conclusions
**Problem:** Vague upbeat endings.
**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.
**After:**
> (Cut the paragraph. End on the last concrete fact instead of a send-off. If the source states real plans, use those.)

### 27. Hyphenated Word Pair Overuse

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end
**Problem:** AI hyphenates these uniformly, including in predicate position (`the report is high-quality`). Humans hyphenate inconsistently — typically only when the compound is attributive (`a high-quality report`) and often dropping the hyphen otherwise (`the report is high quality`). Keep attributive-position hyphens; drop them when the compound follows the noun.
**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.
**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.

### 28. Persuasive Authority Tropes

**Phrases to watch:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter
**Problem:** LLMs use these phrases to pretend they are cutting through noise to some deeper truth, when the sentence that follows usually just restates an ordinary point with extra ceremony.
**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.
**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

### 29. Signposting and Announcements

**Phrases to watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, heads up, quick note, before I forget, one thing that bit me, pay attention to this part, one caveat first, a note on methodology before we start, before we get to the numbers
**Problem:** LLMs announce what they are about to do instead of doing it. This meta-commentary slows the writing down and gives it a tutorial-script feel. The casual register is the same move in friendlier clothes: "one thing that bit me hard, so pay attention to this part" is still a trailer for the sentence after it. The analytical register does it in a noun phrase instead of an invitation ("one caveat up front"), which §36 covers. Remove the announcement rather than just its formality.
**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.
**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.
**Before (casual register):**
> One thing that bit me hard, so pay attention to this part: the webpack dev server doesn't send the CORS header by default.
**After:**
> The webpack dev server doesn't send the CORS header by default.

### 30. Fragmented Headers

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.
**Problem:** LLMs often add a generic sentence after a heading as a rhetorical warm-up. It usually adds nothing and makes the prose feel padded.
**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.
**After:**
> ## Performance
>
> When users hit a slow page, they leave.

### 31. Diff-Anchored Writing
**Problem:** Documentation or comments written as if narrating a change rather than describing the thing as it is. Unless the document is inherently version-scoped (changelogs, release notes, migration guides), it should read coherently without knowing what changed in the last commit.
**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.
**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

### 32. Manufactured Punchlines and Staccato Drama
**Problem:** LLMs often make every sentence land like a quotable closer, then stack short declarative fragments to manufacture drama. A single short sentence for emphasis is fine; a run of them starts to sound engineered.
**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.
**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### 33. Aphorism Formulas

**Words to watch:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of, X has a date, X has an expiry date, X has a shelf life, X is on borrowed time, the clock is running on X
**Problem:** LLMs turn ordinary claims into reusable aphorisms that sound profound without adding precision. Replace the formula with the concrete claim it is gesturing at. When the aphorism is a closing mic-drop line, delete it rather than polishing it into a better metaphor; end on the clearest concrete sentence already in the draft.
**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.
**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

A second shape belongs here: portentous shorthand, where a concrete fact the writer already knows gets swapped for an ominous possession. "This advantage has a date" is not more sophisticated than naming the date, it is the same claim with the useful part removed. Put the fact back.
**Before (portentous shorthand):**
> The bank privacy is a real advantage, but it already has a date.
**After:**
> The bank privacy is a real advantage until the first exchange in 2027.

(Use whatever date the source gives. If the source gives none, say what ends and why, and drop the flourish rather than keeping it as a substitute for the missing detail.)

### 34. Conversational Rhetorical Openers

**Phrases to watch:** Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, What if I told you, Think about it:, Plot twist:, the part everyone misses, what nobody tells you, when used as standalone hooks, faux-insight flattery, or fake-candid pauses before an ordinary point (including self-answered "Question? Answer." pairs).
**Problem:** LLMs open with a fake-candid hook to manufacture intimacy before delivering a routine claim. The tell is the theatrical pause-and-reveal: a one-word question or aside, then the "real" answer. A person being honest usually just says the thing.
**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.
**After:**
> Whether it's worth the price depends on how often you'll use it.

### 35. Colon-Reveal Constructions
**Problem:** LLMs build a noun phrase, drop a colon, then stage a dramatic lowercase payoff as if revealing a secret: "The best part: it learns." An ordinary statement gets inflated into a staged reveal.
**Rule:** Prefer sentence case after a colon unless grammar, a proper noun, a title, or code requires otherwise, and prefer a plain sentence over the noun-colon-payoff shape when the reveal isn't earned.
**Before:**
> The real cost isn't the subscription: it's the hours spent onboarding a team that never adopts it.
**After:**
> The subscription is cheap. The real cost is the hours spent onboarding a team that never adopts it.

### 36. Performed Rigor and Candor

**Phrases to watch:** it's worth being precise/exact/careful here, it's worth distinguishing, this deserves verification and not just assertion, to be precise, to be fair, in fairness, let's be accurate, I want to be careful here, the honest version is, the honest answer is, the fair reading is, we won't undersell/oversell/downplay this, we're not going to sugarcoat it, we say it plainly, no spin, to put it bluntly, credit where it's due, let's say the quiet part out loud, this needs to be said out loud, it has to be said, let's name it, one caveat up front, a caveat that has to sit up front, one caveat before we start, one thing to flag up front, worth flagging up front, an important qualification first, a note on methodology before we get to the numbers, in one specific way, in a very specific sense, in one particular way, for one specific reason, there is a precise reason for this, it is worth stating, it is worth noting, it is worth saying, worth mentioning, it bears repeating, this needs saying, this is worth spelling out
**Problem:** The writer announces that they are being careful, fair, or honest instead of being those things. Precision performed is not precision delivered: the distinction or caveat that follows lands harder without a preamble certifying its integrity, and often the preamble is the whole move with nothing behind it. Distinct from §29, which announces *what* is coming rather than how virtuously it is being done, and from §25, which weakens a claim rather than decorating it with the writer's good faith.
**Rule:** Delete the announcement, keep what follows. If nothing substantive follows, cut the sentence. Never swap one certificate of honesty for a better-worded one.

**Before:**
> It sounds too good to be true, so it's worth being precise about the mechanism. The country does not count days.
**After:**
> It sounds too good to be true. The country does not count days.

**Before:**
> We checked the competition properly, because this claim gets repeated often and deserves verification, not just assertion.
**After:**
> We checked the competition ourselves, because this claim gets repeated a lot.

**Before:**
> It's worth distinguishing what we are actually talking about here. CRS is an automated exchange.
**After:**
> CRS is an automated exchange.
**Before:**
> The honest version of the claim is this: it is the only country that gives you tax residency with no physical presence.
**After:**
> It is the only country that gives you tax residency with no physical presence.
**Before:**
> It is a real advantage and we will not undersell it. But it already has an end date, and we describe that below, plainly.
**After:**
> It is a real advantage. The section below gives the date it ends.

(That last one also drops "plainly." Announcing that the next section is candid implies the rest of the document was not.)

**The announced caveat.** The same move also arrives as a noun phrase with no main verb, which is why the verbal phrases above do not catch it: "One caveat that has to sit up front," "A qualification before we get to the numbers." The sentence names a caveat, asserts that it must come first, and then defers the caveat itself to the sentence after. The modal is the tell: a writer who has a caveat states it, and does not first rule on where it has to sit. Cut the announcement and let the caveat be the sentence. A caveat that is stated stays; a sentence whose only content is that a caveat is coming does not.
**Before:**
> One caveat that has to sit up front, because it makes the model comparison less clean than it looks. The two runs used different context windows.
**After:**
> The two runs used different context windows, so the two models are not being compared on equal terms.

**Asserted specificity.** The adjectives *specific*, *particular*, *precise*, and *exact* get used as stand-ins for the specifics themselves: "they differ in one specific way", "there is a precise reason for this", "a very particular kind of failure". The word promises the detail while the sentence withholds it, and the reader waits a beat for something the writer could have said outright. When the detail does arrive in the next sentence, lead with it and drop the announcement; when it never arrives, the adjective was the whole content and it goes. This pairs with the significance stamp in §1 so often that the two arrive as one sentence: "in one specific way, and the way matters."
**Before:**
> The two runs differ in one specific way. The second used a larger context window.
**After:**
> The second run used a larger context window.

(*Specific* is fine when the specifics are present: "the specific error is ENOSPC" names the error.)

**The worth-saying certificate.** *It is worth stating*, *it is worth noting*, *it bears repeating*, *this needs saying*. The writer rules that a claim deserves to be made and then makes it, but writing it down had already settled that. §24 catches the sentence-initial filler version ("It is important to note that the data shows"); this is the same move in the appended slot that §1's significance stamp occupies, and the two are interchangeable at the end of a sentence. Cut the certificate and keep the claim. Where the certificate is the whole sentence, the claim is in the next one and belongs first.
**Before:**
> There is a trap in the reference implementation, and it is worth stating: it retries forever on a 500.
**After:**
> The reference implementation retries forever on a 500.

### 37. Argument Residue

**Phrases to watch:** while some might argue, it would be easy to dismiss this as, one might object that... but, critics may claim, some will say, it's tempting to think, detractors point to, this isn't really/mainly about, I'm not saying/arguing/trying to, to be clear, don't get me wrong, this is not to say
**Rejected-option variant:** a tempting approach would be, one might be tempted to, an obvious approach would be, you might think... but, it would be easy to just, some would suggest
**Problem:** A rebuttal to an objection nobody raised, or the rejection of an option nobody proposed. The model drafted through more than one position before settling, and the discarded side survives as a phantom opponent. The tell is structural rather than lexical: the sentence is shaped as a reply, but the claim it replies to appears nowhere else in the piece. The option variant puts a solution in the opponent's slot instead of an argument, raising it in one clause, killing it in the next, and never returning to it.
**Rule:** Cut the phantom rebuttal and state the position directly. Cut the rejected option and state the real constraint. Keep either one when it is real: the objection is named in the text or an identifiable person made it, or the option is one a reader of that design document or tutorial would genuinely weigh. Remove only the unsupported defense, and where it carries a real claim, state that claim on its own. A single rejected option can be legitimate; several short unrelated rejections in a row are drafting residue. Related to §36: both leave drafting behind, one the writer's self-assessment and the other the writer's discarded opposition.
**Before:**
> While some might argue that territorial taxation is a loophole, it is simply how the statute defines taxable income.
**After:**
> The statute defines taxable income as income from local sources, so foreign income falls outside it.
**Before (rejected option):**
> Session tokens rotate every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.
**After:**
> Session tokens rotate every 24 hours, in place, and clients refresh transparently.

### 38. Reasoning-Chain Artifacts

**Phrases to watch:** Let me think, Let's work through this, First, I'll, Breaking this down, Step 1:, To answer this I need to, Now that we have established, numbered thinking meant to stay internal
**Problem:** Chain-of-thought scaffolding leaking into the final text. Distinct from §21, which is chatbot correspondence addressed to the reader; this is the model narrating its own procedure as though the procedure were the content.
**Rule:** Delete the scaffolding and keep the conclusion in the author's voice.
**Before:**
> Let me break this down. First, I'll look at the tax rules, then at the residency rules. Step 1: the tax is territorial.
**After:**
> The tax is territorial. The residency rules are separate from it.

### 39. False Agency

**Words to watch:** the data tells us, the numbers reveal, the evidence demands, the market rewards, the research suggests, the decision emerges, the technology demands, history teaches us
**Problem:** An abstraction performing a willed human action. It hides whoever actually did the thing and borrows authority by making the subject sound like it spoke for itself.
**Rule:** Name the actor the source names, address the reader as "you", or restate it as a plain fact. Do not invent an actor to fill the slot; if the source has none, the fact stands on its own.
**Before:**
> The data tells us that costs rose, and the market rewards firms that adapt.
**After:**
> Costs rose. Firms that adapted kept more of their customers.

### 40. Forensic Residue

**Problem:** Artifacts that exist nowhere except in machine-generated or hastily pasted text. Unlike everything else in this guide these are close to proof rather than evidence, and they survive editing passes because they are invisible or look like formatting.
**What to search for:**
- Unfilled templates: `[Your Name]`, `[Company]`, `[insert date]`, `XXXX` date stubs
- Chatbot citation tokens: `citeturn0search0`, `contentReference[oaicite:0]`, `oai_citation`
- Tracking parameters appended to URLs: `utm_source=chatgpt.com`, `utm_source=perplexity`
- Invisible characters: zero-width space (U+200B), zero-width joiner (U+200D), soft hyphen (U+00AD), non-breaking spaces where ordinary ones belong
- Homoglyphs: Cyrillic а е о р с or Greek ο substituted for Latin letters

**Rule:** Strip them and normalize to plain NFC text. Run this scan before returning any rewrite, the same way you scan for em dashes under §15.

### 41. Structural Uniformity

**Problem:** Sentences can be clean and the piece still read as generated, because the shape gives it away: sections of near-identical length, lists that all happen to have three items, and a recap sentence closing every section. Models produce parallel self-contained blocks where a writer produces an argument that goes somewhere.
**The reshuffle test:** swap the second and fourth paragraphs. If nothing breaks, the piece is a stack of interchangeable blocks rather than a line of reasoning, and no amount of sentence-level editing will fix that.
**Rule:** Vary section depth on purpose, some getting two paragraphs and some six. Let each list be the length its content actually is, including lists of two. Cut the closing recap: the reader just read the section.
**Before:**
> ## Cost
> [three paragraphs] In short, cost is what decides this.
> ## Speed
> [three paragraphs] In short, speed is what decides this for small teams.
**After:**
> ## Cost
> [three paragraphs, ending on the last concrete figure]
> ## Speed
> [one paragraph, because there is less to say]

### 42. Connective Tissue Pile-Up

**Words to watch:** Moreover, Furthermore, Additionally, In addition, That said, That being said, Consequently, Ultimately, In conclusion, When it comes to, Moving forward
**Problem:** §7 lists several of these as vocabulary, and the false-positive guidance rightly says one *however* proves nothing. This is the other half of that rule. A paragraph opening three consecutive sentences with a connective is welding together ideas whose relationship the writing never actually established.
**Rule:** Count them. More than one connective opener in a paragraph, or the same one twice in a section, means the sentence order should be carrying the logic instead. Delete the connective, or start a new paragraph.
**Before:**
> Additionally, the fees are lower. Moreover, transfers settle faster. Furthermore, the account can be opened remotely.
**After:**
> The fees are lower and transfers settle faster. You can open the account without going there.

### 43. Hedged-Enumeration Openers

**Phrases to watch:** There are several ways to, There are a few things to consider, There are many factors, It depends on a number of factors, Generally speaking, In general, It is generally a good idea to
**Problem:** Announcing that considerations exist instead of committing to an answer. The reader asked something specific and gets a preamble about the shape of the reply. This one is measurable: it is one of the clearest separations between human and chatbot answers in the HC3 corpus.
**Rule:** Give the specific answer first. If a list genuinely follows, the list *is* the answer, so open with it.
**Before:**
> There are several factors to consider when choosing a residency. Generally speaking, it depends on your situation.
**After:**
> The choice comes down to how many days you can spend in the country and where your income comes from.

### 44. The Treadmill Effect

**Problem:** A long section that restates one idea in progressively different words. A writer advances an argument; a model circles one. Distinct from §24, which is filler inside a sentence, and from §32, which is about cadence rather than information density.
**Rule:** Ask what each paragraph adds that the previous one did not. Where the answer is "nothing, but louder", merge them and keep the clearest version. A section that shrinks by half under this test was never that long.
**Before:**
> Privacy matters here. The confidentiality of your accounts is central to the appeal. Keeping financial information out of automatic circulation is, for many people, the main draw.
**After:**
> For many people the main draw is keeping account information out of automatic circulation.

## SLOVAK AND CZECH TEXT

Apply this section only when the text being edited is Slovak or Czech. Everything above still applies, except where §45 and §46 explicitly override an English-only rule. The examples are Slovak; Czech behaves the same way unless a rule says otherwise.

These languages need their own section because most AI text in them is an English draft in disguise: the model reasons in English patterns and emits Slovak or Czech words, so the tells arrive as loan translations, English punctuation, and English word order. Fixing the English patterns without fixing the translation artifacts leaves the text sounding just as generated.

### 45. Quotation marks: keep the low-high pair

**This overrides §20 for these languages.** The correct Slovak and Czech quotation marks are „…“ (U+201E opening below, U+201C closing above), and the correct apostrophe inside a foreign name is ’ (U+2019), as in Moody’s. These are native typography, not a ChatGPT artifact, and converting them to straight ASCII quotes makes the text look worse. §20 governs English only.

The tell here is the wrong pair: English “…”, French «…», or a document mixing styles. A closing ” (U+201D) after an opening „ is the commonest giveaway, because it means the text was set with English punctuation rules and then only partly corrected.

**Before:**
> Rozdiel je medzi "nikto o mne nič neposiela" a „som nepostihnuteľný”.
**After:**
> Rozdiel je medzi „nikto o mne nič neposiela“ a „som nepostihnuteľný“.

### 46. Dashes: cut the em dash harder, keep the en dash where it belongs

**This overrides §15 for these languages, in both directions.**

Slovak and Czech typography has no em dash. The native parenthetical dash is the pomlčka, an en dash (–) with a space on each side. An em dash (—) is therefore a stronger signal here than in English, because no native writer, editor, or style guide puts one there: it arrives only through an English draft. Cut every one, using §15's preference order (period, comma, colon, parentheses, restructure).

The en dash is a different character doing a different job, and §15's ban on it does **not** carry over. Leave it alone in ranges written without a preposition (55–85 €, 2026–2028, 8:00–17:00) and in pairings of proper nouns (zápas Slovensko–Česko, trasa Bratislava–Košice). Rewriting a range with "až" is also correct and often reads better in dense prose, but that is a sentence-level judgment, not a search and replace.

Leave the minus sign (−, U+2212) alone wherever it belongs to a symbol rather than prose: ratings such as A− and BBB−, temperatures, negative numbers. It is not a dash.

A spaced en dash as a parenthetical is grammatically correct, but keeping a dash where the model put one preserves the rhythm that made the sentence a tell. Restructure by default; keep the pomlčka only when the author's sample uses it (see Voice Calibration).

**Before:**
> Ak už máš trvalý pobyt — a plníš mesačné povinnosti — nič z toho nie je tvoj problém. ADAC pýta 55—85 €.
**After:**
> Ak už máš trvalý pobyt a plníš mesačné povinnosti, nič z toho nie je tvoj problém. ADAC pýta 55–85 €.

### 47. Copula avoidance, Slovak and Czech edition

The local form of §8. Instead of "je" or "má", generated text reaches for **predstavuje** (represents), **poskytuje** (provides), **ponúka** (offers), **prináša** (brings), **disponuje** (has at its disposal), **umožňuje** (enables), **vyznačuje sa** (is characterized by), **slúži ako** (serves as), **zohráva úlohu** (plays a role), **vykazuje** (exhibits).

"Predstavuje" is the worst offender and the most reliable. A human writes "cédula je doklad"; a translated draft writes "cédula predstavuje kľúčový doklad". These languages also drop the present-tense copula far more readily than English, so the fix is often no verb at all rather than "je".

**Before:**
> Cédula predstavuje kľúčový dokument, ktorý poskytuje prístup k bankovým službám a prináša celý rad výhod.
**After:**
> Na cédulu ti banky otvoria účet.

### 48. Transgressive and participle padding

The local form of §3. English "-ing" analyses survive translation as:

- transgressives (prechodník / přechodník): zdôrazňujúc, reflektujúc, poukazujúc na, podčiarkujúc
- clause tails: čím sa zdôrazňuje, čo odráža, pričom poukazuje na, čím prispieva k
- stacked adjectival participles: neustále sa vyvíjajúci, dynamicky rastúci, dlhodobo pretrvávajúci

The transgressive is archaic in modern Slovak and bookish in Czech; almost nobody writes it outside literary pastiche, so in ordinary prose it is close to a confession. The clause tails are commoner and correspondingly weaker evidence, but do the same job of bolting fake depth onto a finished sentence. Cut the tail, or promote it to its own sentence if it carries a real claim.

**Before:**
> Paraguaj zaviedol nové pravidlá, čím zdôraznil svoj záväzok k transparentnosti, reflektujúc širší trend v regióne.
**After:**
> Paraguaj zaviedol nové pravidlá.

(The rest was decoration. If the regional trend is real and the source documents it, write it as its own sentence with the source's detail, not as a participle hanging off this one.)

### 49. Calqued AI vocabulary

The §7 list, loan-translated. Watch for: **kľúčový** (key), **zásadný / rozhodujúci** (crucial), **výrazne / významne** (significantly), **komplexný** (comprehensive, and frequently a mistranslation of "complex"), **robustný**, **dynamický**, **inovatívny**, **prelomový** (groundbreaking), **fascinujúci**, **pulzujúci / živý** (vibrant), **bohatý** in the figurative sense (rich), **rozmanitý** (diverse), **dychberúci** (breathtaking), **nachádza sa v srdci** (in the heart of), **svedčí o** (is a testament to), **zohráva kľúčovú úlohu** (plays a key role), **podčiarkuje význam** (underscores the importance), **v dnešnej dobe** (in today's world), **digitálna éra**, **neustále sa vyvíjajúci** (ever-evolving), **je dôležité poznamenať** (it is important to note), **treba zdôrazniť**, **v neposlednom rade** (last but not least), **nepopierateľne** (undeniably), **na mieru** (tailored), **poďme sa pozrieť** (let's take a look).

The §7 caveat holds and matters more here, because several of these are ordinary words in journalism and administrative writing. One "kľúčový" is nothing. Three in a paragraph, next to a "svedčí o" and a "v dnešnej dobe", is the tell.

Phrases from other sections arrive calqued too. The commonest is §36's candor preamble: **treba to povedať nahlas**, **povedzme to nahlas**, **povedzme si to otvorene**, announcing that the next sentence is brave before delivering an ordinary claim. Cut the preamble and keep the claim.

**Before:**
> Toto treba povedať nahlas: register chráni údaje pred verejnosťou, nie pred štátom.
**After:**
> Register chráni údaje pred verejnosťou, nie pred štátom.

### 50. Pronoun and possessive spam

Slovak and Czech are pro-drop: the verb ending carries the person, so a spelled-out subject pronoun is emphasis, not grammar. Possessives drop the same way whenever ownership is obvious. A translated draft keeps every English "you" and "your", which reads like someone speaking slowly to a foreigner. Demonstratives go the same way: English "the resolution" has no Slovak equivalent, so generated text reaches for "táto rezolúcia" every time the noun reappears. Repeat the bare noun instead, or drop it.

**Before:**
> Keď si ty otvoríš tvoj účet, tvoja banka bude vyžadovať tvoj doklad o adrese. Tento doklad musíš mať pripravený.
**After:**
> Keď si otváraš účet, banka bude pýtať doklad o adrese. Maj ho pripravený.

### 51. English word order carried through translation

These languages use word order to mark what is old and what is new: given information near the front, the new point at the end. English does that job with articles and stress and keeps a fixed subject-verb-object order. Generated text keeps the English order, so the new information lands first and every paragraph finishes flat. The symptom is a run of sentences that all start with their subject and all end on something the reader already knew.

**Before:**
> Nová rezolúcia bola zverejnená v marci 2026. Táto rezolúcia ukladá novú ohlasovaciu povinnosť rezidentom.
**After:**
> V marci 2026 zverejnili novú rezolúciu. Rezidentom z nej vyplýva ohlasovacia povinnosť.

### 52. Register drift between ty and vy

Generated text slides between the informal *ty* and the formal *vy*, sometimes inside one paragraph, because English "you" gives the model nothing to anchor to. Pick whichever form the source opened with and hold it. The drift shows up in verb endings, in possessives (tvoj / váš), and most often in imperatives, where "pozri" and "pozrite" sit two sentences apart. Watch the same drift in the writer's own voice: "vieme ti zariadiť" against "sme schopní zabezpečiť".

### 53. Typography and number conventions

Not style judgments, just rules a translated draft routinely breaks. Fix them on sight:

- Percent signs, currencies, and units take a space, ideally non-breaking: 10 %, 33 USD, 160 GB. Closing it up ("10%") is correct only in an attributive compound (Slovak "10%-ný", Czech "10%ní").
- Decimal comma, space as the thousands separator: 5 970, 0,7 %, 1,2 milióna. Not 5,970 and not 0.7%.
- Dates take an ordinal period and a genitive lowercase month: 6. júla 2026, Czech 6. července 2026. Not "6 Júl 2026" and not "July 6, 2026".
- Months, weekdays, nationality adjectives, and language names are lowercase: júl, pondelok, slovenský, španielčina. Capitals on any of these are an English habit that survived translation.
- §18 is absolute in these languages. Headings are sentence case, and only proper nouns keep a capital. There is no native title case to fall back on.
- Check the diacritics: ď ť ň ľ ĺ ŕ ô ä for Slovak, ě ř ů for Czech. A draft with some accents stripped or flattened has been through a pipeline that mangled them, which usually means it has other translation damage too.

### 54. Loanwords: neither over-translated nor under-translated

Established English terms in finance, tech, and compliance stay in English because that is what practitioners say: proof of address, compliance, roaming, self-certification, stablecoin. Generated text errs both ways. It translates the settled term into something nobody uses ("doklad o mieste pobytu na účely overenia totožnosti"), then leaves plain English where a normal word exists ("použi tento tool", "je to challenge"). Match the field, not the dictionary.

The hyphenation in §27 does not transfer either. These languages do not form English-style hyphenated modifiers: write "vysoko kvalitný", not "vysoko-kvalitný".

### What NOT to flag in Slovak and Czech

Adding to the general false-positive list, these are native features, not tells:

- **The reflexive passive** (uvádza sa, vykonáva sa, podáva sa). Standard in legal and administrative register, which is exactly the register most of this text lives in. Flag it only where a specific actor is obvious and available, per §14.
- **Long sentences with several subordinate clauses.** Normal and readable here. English sentence-length targets do not transfer, and chopping every long sentence into three short ones produces the staccato problem in §32.
- **„…“ quotation marks and the spaced en dash.** Covered in §45 and §46. Native typography.
- **Verb-initial or object-initial sentences.** Free word order is a feature being used, not an error to normalize.
- **Particles and hedging words** (veď, však, teda, predsa, no, vraj, akože). These are ordinary spoken-register markers and usually evidence of a human writing, not filler to scrub. Removing them is one of the fastest ways to make Slovak or Czech prose sound machine-made.
- **Nielen… ale aj.** A normal construction, unlike its English counterpart in §9. It only counts as a tell when it is stacked with other §9 shapes or repeated across a document.

## DETECTION GUIDANCE

### What NOT to flag (false positives)

A clean human writer can hit several of the patterns above without any AI involvement. Before rewriting, sanity-check that you are not gutting legitimate prose. The following are *not* reliable indicators on their own:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal registers.** This often signals a person in a technical field, a young writer, or someone with neurodivergent prose habits — not a chatbot.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic vocabulary.** AI overuses *specific* fancy words (see §7), not all fancy words. Don't flatten "ostensibly" or "constituent" just because they sound brainy.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them often. Em dashes are evidence only when paired with formulaic sales-y rhythm.
- **One short emphatic sentence.** Humans use clipped sentences to land a point. Flag staccato drama only when several short fragments appear in a row and inflate the tone.
- **"Honestly" or "look" mid-sentence.** These are ordinary in casual writing. The tell is the standalone theatrical opener, not the word itself.
- **Deliberate repeated openings.** Writers repeat an opening to build rhythm or pressure: "She came. She saw. She conquered." §12 applies when the repetition does nothing, not whenever it occurs.
- **Useful limits and disclaimers.** Scope statements, legal and safety notices, genuine corrections, named objections and the replies to them, and FAQ answers all stay. §37 removes the defense with no attacker, not every caveat. This protects a caveat that is *stated*; a sentence whose only content is that a caveat is coming is the announced caveat under §36, and it goes.
- **Real alternatives.** A design document, tutorial, or argument is supposed to weigh options the reader might actually pick. Cut only the unlikely option raised so it can be dismissed and never used again.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations doesn't prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.
- **Secondhand text.** Do not rewrite watched phrases inside quotations, titles, proper names, or examples where the phrase is being discussed rather than used.

When in doubt, look for **clusters** of tells, not isolated ones. A single em dash means nothing; em dashes plus rule-of-three plus *vibrant tapestry* plus a "Conclusion" section is a confession.

Count a cluster once. When several weak signals land on the same phrase, a bolded aside set off by an em dash sitting inside a rule-of-three list, that is one strong tell and not three. Weigh it once, and fix it once.

### Signs of human writing (preserve these)

When you see these, lean toward leaving the prose alone — they are evidence of a real person writing, and over-editing will destroy what makes the piece sound human:

- **Specific, unusual, hard-to-fabricate detail.** A real address. A weird quote. The phrase "the lawyer who used to work upstairs from my dentist." LLMs round off specifics; humans hoard them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me, and I can't fully explain why." LLMs default to clean takes.
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **First-person editorial choices the writer can defend.** If the writer can explain *why* they made a particular cut or used a particular word, that's a strong human signal.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything older than that is, with very rare exceptions, not AI-written.

---

## Invocation Modes

**Pasted text (default).** The user gives text in the conversation. Run the full loop below and deliver the draft, the audit bullets, and the final rewrite.

**File mode.** The user points at a file. Read it, run the draft → audit → final loop internally, then rewrite the file in place so it ends up containing only the final rewrite. Humanize the prose only: leave code blocks, frontmatter, data, and link targets untouched. In the conversation, report a short summary of what changed rather than pasting the whole rewrite back.

**Embedded mode.** Another task or agent is using this skill as one step of a larger job (a PR description, a commit message, a doc). Run the loop internally and output only the final text. No draft, no audit bullets, no summary. The caller wants prose, not ceremony.

## Detect Mode

Invocation Modes above governs delivery format; this governs whether to rewrite at all. Most requests want a rewrite. When the user instead asks whether text reads as AI-written, or asks you to point out the tells without fixing them ("does this sound like AI?", "what's wrong with this paragraph?"), switch to detect mode:

- Quote the specific offending phrase or sentence and name the pattern (by number or name) it matches. Every flag needs a quote; don't gesture at "the tone" in general.
- Do not produce an overall AI-probability score or percentage. A pattern list is evidence the user can check against the text; a single confidence number just substitutes your guess for theirs.
- Do not rewrite the text unless asked. If the user wants both a diagnosis and a rewrite, do both, clearly separated.

## Process and Output

1. Read the input carefully and identify every instance of the patterns above.
2. Write a **draft rewrite**. Check that it reads naturally aloud, varies sentence length, prefers specific details and simple constructions (is/are/has), and keeps the appropriate register.
3. Ask two questions: **"What makes the below so obviously AI generated?"** and **"Does the rewrite state any fact, name, number, date, quote, citation, or ranking that isn't in the source, or drop a claim that was?"** Answer briefly. A fabrication is a defect even when it sounds more human than the vague original, and a lost claim is a defect even when the rewrite reads better without it.
4. Revise into a **final rewrite** that addresses them and contains no em or en dashes (see §15, and §46 if the text is Slovak or Czech).

In pasted-text mode, deliver the draft, the brief "still-AI" bullets, the final rewrite, and (optionally) a short summary of changes. In file and embedded modes, run the same loop but deliver only what the mode calls for (see Invocation Modes).

## Reference

This skill is based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The patterns documented there come from observations of thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
