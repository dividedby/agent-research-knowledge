# Not every AI coding asset belongs in git

Working with an agent generates a class of intermediate assets — **PRDs, research
files, decision maps, implementation plans** — and Matt's open position is that
most of them *don't belong checked into the repo's git history*. They are
scaffolding for a change, not the change; committing them clutters the tree with
process artefacts that outlive their usefulness and that the next reader has to
wade past to find the code.

Where they go instead is unsettled, but his current split is concrete:

- **PRDs and implementation plans → GitHub issues.** The issue tracker is the
  natural home for a spec or a plan: it is durable, linkable, and already the seam
  his skills hand work across (`to-prd → to-issues`), so the plan lives beside the
  work it describes without polluting the source tree.
- **Research files → still unresolved.** He checks these into git today only
  because he has nowhere better to put them; he is openly considering an
  **external knowledge base** instead, and notes that parking research in a
  GitHub issue is "a bit awkward." He has held this idea for months without
  building it — uncertain whether no one has tried it because it is good, or
  because it sucks.

A sharper version of the "not in git" position adds the concrete failure mode
that makes local markdown the wrong choice, not just a messier one: with a
plan document as a local file, **merge conflict resolution becomes a thing** —
multiple branches or worktrees editing the same plan file diverge and have to
be reconciled by hand. Issues sidestep this because the tracker, not the
working tree, owns the document. Matt's blunt gloss on the alternative: "it's
a waste to keep them locally." This is the same reasoning `spec-and-tickets-plan-split`
applies specifically to specs and tickets — the artefact needs a home that
survives concurrent branches, and a git-tracked file in the repo isn't it.

This isn't a blanket "nothing goes in git" rule, though — asked which docs
should make the jump from a local session into the codebase, Matt names
`CONTEXT.md` and ADRs specifically, and is explicit that "these should be
PR'd to the repo." The distinction is exactly the one `adrs-as-agent-memory`
and `shared-language-as-agent-fuel` already draw: durable *decisions and
vocabulary* earn a permanent, git-tracked home because future agents need to
inherit them; transient *plans and tickets* don't, because they describe a
route being walked, not a fact about the codebase.

The unifying instinct is the same one behind treating the agent as an amnesiac and
keeping `CLAUDE.md` to a tight budget: be deliberate about *which* durable surface
each kind of generated artefact lands on, rather than defaulting everything into
the repo. A related preference falls out of it — for most workflows Matt keeps the
agent's "brain" / knowledge store **stateless**, rather than building a persistent
personal memory the agent carries between tasks.

## Remote, shareable state is the bar for a tracker

Asked for his stance on Beads (steveyegge's dependency-aware issue tracker)
as an alternative to GitHub issues, Matt names the exact criterion this
doc's GitHub-issues preference already implies: "I prefer my issue tracker
state to be remote so I can easily share it." A local-only tracker fails
that bar the same way a local plan file does — it isn't durable or shareable
the way a remote store is (see the merge-conflict argument above). Learning
that Beads can also persist its state directly to GitHub was enough to
satisfy him — "In that case, great!" — confirming the requirement is about
*where the state lives*, not brand loyalty to a specific tool.

## Stateless by choice, not by default

Matt states the stateless preference more sharply elsewhere: **"I also hate
memory systems — I much prefer my harness stateless, so I can work from a
consistent base that I control."** The reasoning is control, not just
simplicity — a stateful memory layer means the agent's starting point shifts
run to run in ways the user doesn't fully see or steer, where a stateless
harness always starts from the same, inspectable base. He's also skeptical
that the alternative currently works: responding to a harness that claims
automatic context management removes the need to think about this, his
assessment is "all harnesses promise to handle this and I've not seen one that
actually works yet" — automatic memory/context management is a claim to be
distrusted until demonstrated, not a solved problem to defer to.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069698109492343101-6d683ee8.md` — origin: https://x.com/mattpocockuk/status/2069698109492343101
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069698238685294858-6c3f48d8.md` — origin: https://x.com/mattpocockuk/status/2069698238685294858
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069698455195263459-5c40425e.md` — origin: https://x.com/mattpocockuk/status/2069698455195263459
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069728413896585249-6c940188.md` — origin: https://x.com/mattpocockuk/status/2069728413896585249
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069741439349633054-d92739c9.md` — origin: https://x.com/mattpocockuk/status/2069741439349633054
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080042422688481454-1d93730c.md` — origin: https://x.com/mattpocockuk/status/2080042422688481454
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080044920501342366-0d2f7927.md` — origin: https://x.com/mattpocockuk/status/2080044920501342366
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080048263667831027-d81dc7d0.md` — origin: https://x.com/mattpocockuk/status/2080048263667831027
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079949437254705436-14e0aa6c.md` — origin: https://x.com/mattpocockuk/status/2079949437254705436
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079925132001194205-0e6f0200.md` — origin: https://x.com/mattpocockuk/status/2079925132001194205
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085024586706321637-f43187cf.md` — origin: https://x.com/mattpocockuk/status/2085024586706321637
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085025125582184894-3f6ba0ac.md` — origin: https://x.com/mattpocockuk/status/2085025125582184894
