# Adversarial agent-pairing for triage

When the volume of incoming claims outpaces what a human can evaluate from
scratch, don't trust the agent's first read — force it to argue against
itself before you act on it. Matteo Collina now triages 20-40 security
vulnerability reports a week, most of them AI-written and several duplicates
of each other; the goal of most of that triage isn't to fix a bug, it's to
explain to an AI reporter why the behavior is outside the threat model, so no
maintainer time gets burned chasing a non-issue. His flow pairs with an
agent (Pi or Claude Code with Opus, pulling the report straight from
HackerOne) and pushes back on whatever the agent concludes, repeatedly,
until it can either produce a long, airtight explanation for the reporter or
flip his own judgment that the report is real. The agent isn't a rubber
stamp for a verdict — it's a sparring partner forced to defend its read
before that read gets acted on.

The threshold for accepting an AI-flagged report as genuine is deliberately
high, and earned the hard way: past false positives he waved through cost
him, so he now pushes back harder rather than risk it again. That scrutiny
isn't spent evenly — the moment he detects a competent human behind a
report, he shifts into real engagement, because bot-vs-bot noise and a
genuine human researcher deserve different amounts of attention.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-triaging-the-ai-horde-9b42479f.md` — origin: https://adventures.nodeland.dev/archive/triaging-the-ai-horde/
