# The SDLC is the bottleneck, not the model

Complaints about token cost are usually a symptom, not the real problem: the
organization is paying for intelligence it is structurally unable to use,
because the software development lifecycle a task flows through was designed
for a world where code was expensive to write and mistakes were slow to catch.
Ticket-shaped, sprint-sized tasks — the shape most companies still feed their
agents — were saturated a model generation ago; a five-minute agent run that
takes five more days to deploy gets no benefit from the next, faster model,
because the bottleneck has moved from "how fast can it write the code" to
"how fast can the process around the code let it ship."

Why the old SDLC needs re-deriving, not just trimming: review gates, approval
chains, and rules like "two reviewers required" aren't arbitrary — they're the
rational output of an evolutionary process tuned to a world where mistakes were
expensive and hard to reverse. That trade-off has inverted now that code is
cheap to produce, so the right response to risk inverts too: from
mistake-*prevention* (gates, careful review) to mistake-*tolerance* — isolation
over permission, quick reversibility over careful review, parallelism instead
of queues. (The concrete shape of each tactic: see
[disposable-environments-unlock-parallel-agents](./disposable-environments-unlock-parallel-agents.md),
[version-control-as-the-safety-net](./version-control-as-the-safety-net.md), and
[ship-constantly-own-what-you-merge](./ship-constantly-own-what-you-merge.md).)

Evidence this isn't just theory: after Amp rebuilt its own SDLC around this —
pushing straight to main, CI/CD reshaped for it, agents running in ephemeral,
parallel cloud sandboxes (Orbs) — commit velocity rose 65% in a month, with
over 85% of commits now originating from Orbs rather than local dev. The
takeaway generalizes past Amp: rebuilding the process the agent's output flows
through is as large a lever as the model upgrade itself — arguably larger,
since it's the lever most organizations haven't touched yet.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-pave-the-road-bafad361.md` — origin: https://ampcode.com/notes/pave-the-road
