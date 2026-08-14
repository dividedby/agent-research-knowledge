# The language is the product

Matt's sharpest framing of domain language pushes past "a glossary helps the
agent" into a stronger claim: **"The language is the product."** Once the
domain language is figured out, "the product kind of builds itself" — meaning
the bottleneck in agent-assisted building isn't typing code, it's arriving at
the precise vocabulary that describes what the product does. This is a claim
about where the *work* is, not just about documentation hygiene: "Domain
language is unbelievably powerful with agents."

## Domain language means language used by domain experts

The term isn't "whatever words you pick" — Matt is specific: domain language
is "language used by domain experts." Getting it right requires becoming one:
his one-line prescription is simply "Become a domain expert." This is a
sharper bar than picking consistent naming; it means the words have to come
from genuine fluency in the problem space, not from guessing at a plausible
vocabulary.

## Encoding it in the harness isn't enough — you have to understand it

Pressed on whether the fix is structural (encode domain language in the
harness/skill so the human doesn't have to hold it), Matt's answer draws a
line the tooling can't cross: "That too, but you need to understand it to
wield it effectively." A glossary file or skill can *store* the vocabulary,
but using it well — knowing which term applies, catching when the agent
reaches for the wrong one, judging whether a generated design actually fits
the domain — still requires the human to actually know the domain, not just
have it captured somewhere the agent can read. Without that understanding,
domain language "becomes meaningless drivel": vocabulary without
comprehension is noise dressed as precision.

## Renaming refactors used to be hard; agents make them cheap

A companion thread sharpens why domain language pays off at the codebase
level, not just the product level: "if you understand the 'shared language'
of your codebase (i.e. the terms used, the names for things, relationships
between them)... AND those terms are used consistently in the codebase, then
you understand the codebase. Whether you read the actual code or not." Reading
the code and understanding the language are alternate routes to the same
comprehension — DDD "has never been more powerful" because there's now a
cheap way to keep the second route open. That "used consistently" clause used
to be the hard part: keeping a legacy codebase's names in sync as vocabulary
evolved was, in Matt's view, "harder than it is now" — "renaming refactors are
pretty simple with agents." What used to be prohibitively expensive busywork
(renaming a concept across every file, table, and variable that touches it)
is now cheap enough to do routinely, which is what makes "used consistently"
achievable instead of aspirational.

## Business-language renames propagate down, and it's worth doing pre-AI too

Asked whether a rename in the business's own vocabulary should cascade all
the way down — classes, properties, database tables — Matt's answer is
unqualified: "Yes, definitely. And even worth doing before AI." The rename
discipline isn't an AI-era invention that only makes sense because agents cut
the labor cost; it was always the right move to keep a codebase's language
matching the business's, agents just remove the excuse not to bother. He adds
one qualifier on pacing: it's "usually... not so all-at-once" — a business
vocabulary shift gets absorbed incrementally, not as a single flag-day
migration.

## Why this compounds: precision compresses everything downstream

This is the human-side counterpart to `CONTEXT.md`-as-agent-fuel (see
`shared-language-as-agent-fuel`): that doc covers the *mechanics* of capturing
and storing a shared vocabulary; this is the claim about *why* the vocabulary
is worth building in the first place — because the language, once precise, is
what generates the product rather than merely describing it after the fact.
It also sits alongside the skill-as-ceiling stance (`strategic-over-tactical-and-skill-as-ceiling`):
where that doc argues your general engineering skill bounds what the agent can
produce, this one narrows the claim to a specific kind of skill — fluency in
the domain's own language — as the lever that does the most work.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083641584705253414-fc65c167.md` — origin: https://x.com/mattpocockuk/status/2083641584705253414
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083650890246865128-68cb736b.md` — origin: https://x.com/mattpocockuk/status/2083650890246865128
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083656999238046186-94605106.md` — origin: https://x.com/mattpocockuk/status/2083656999238046186
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083800837382377867-fc9f1e83.md` — origin: https://x.com/mattpocockuk/status/2083800837382377867
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083800963853254820-a0a5b362.md` — origin: https://x.com/mattpocockuk/status/2083800963853254820
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083944031025782810-cec0ae49.md` — origin: https://x.com/mattpocockuk/status/2083944031025782810
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083944119085285519-efcb744f.md` — origin: https://x.com/mattpocockuk/status/2083944119085285519
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087508057932615740-366c0049.md` — origin: https://x.com/mattpocockuk/status/2087508057932615740
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087510345241727072-10aaafe6.md` — origin: https://x.com/mattpocockuk/status/2087510345241727072
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087523615574987261-211fec49.md` — origin: https://x.com/mattpocockuk/status/2087523615574987261
