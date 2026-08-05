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
