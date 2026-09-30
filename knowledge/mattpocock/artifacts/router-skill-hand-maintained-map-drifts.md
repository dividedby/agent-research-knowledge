# A router skill is a secondary source over the skills it maps

`ask-matt` routes a described situation to the skill or sequence of skills
that fits, plus where the human decisions in that sequence sit — but it is a
**hand-written map** of the skill set, not a live scan of what's installed or
a query against each skill's own `SKILL.md`. That single fact is the source of
its three most-reported failure modes, and the general lesson travels to any
router built the same way: a router is a secondary source over the primary
skills it describes, and it can go stale or simply be wrong exactly as any
other secondary source can (see `context-compression-and-handoff-mechanics`'s
primary/secondary distinction).

## Three failure modes, one root cause

- **It reports skills as not installed when they are.** Most of the skills the
  router routes through set `disable-model-invocation: true`, which means the
  harness leaves them out of the skill list it injects into the agent's
  context. The router reads that injected list as exhaustive and declares the
  missing skills absent — one session had it declare an entire multi-skill
  flow unavailable and reroute to a bare fallback. Thirteen of one plugin's
  twenty-two skills carry the flag, making this the common case rather than an
  edge one. The skills are installed; `.claude-plugin/plugin.json` is the
  authority the router isn't consulting.
- **It asserts a skill's behaviour from its own gloss, not the skill.** The
  router answers from a one-line summary of each skill it carries rather than
  from that skill's actual `SKILL.md` — one detailed report tracked three
  wrong assertions in a single session, including a recommendation to skip a
  downstream step on the strength of a gloss that didn't match what the
  skipped step's file actually said. It verified only after the user pushed
  back, never on its own initiative. The skipped step there cost a real check
  downstream.
- **It lags renames and additions.** A router maintained by hand necessarily
  trails the repo it describes — two skills shipped and were in active use for
  weeks before the router named them at all.

All three share the same root cause: the router's knowledge of the skill set
is a cached, human-maintained account of the thing, not a live read of it, and
none of the three failures self-corrects without an explicit verification
step.

## The mitigation is "make it open the file", not "make it more accurate"

Because the router is a map, not the territory, the durable fix isn't chasing
staleness with more frequent hand-edits — it's treating any load-bearing claim
the router makes about *another* skill's behaviour as unverified until the
router actually opens that skill's file. Practically: when the router asserts
something that changes what you do next, ask it to open the referenced
`SKILL.md` before acting on the claim. The router is explicit about its own
authority ranking on this point — where it and a skill's own file disagree,
the file is right, not the router — which only helps if something actually
triggers the check.

## Advice to edit a `SKILL.md` doesn't survive the next update

A fourth pattern sits next to the three failure modes above, less about the
map going stale and more about where the router points you to fix things.
Asked how to make a downstream skill behave differently, the router's answer
is often "add a line to the skill" — correct in the moment, but not durable:
a plugin install is read-only and `npx skills update` overwrites a forked
copy's edits on the next pull, so the fix quietly disappears the next time
the skill set updates. Standing behaviour belongs in the repo's own
`CLAUDE.md` or `AGENTS.md` instead, or in the invocation itself for a
one-off — both survive an update because they live outside the skill files
the router is pointing at. This is the same fork-vs-subscribe boundary
`two-distribution-philosophies-fork-vs-subscribe` describes for the whole
install: a router that suggests editing a skill is nudging you across that
boundary without saying so.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-ask-matt-54c74f90.md` — origin: https://www.aihero.dev/skills-ask-matt
- `sources/mattpocock/skills-repo/docs-engineering-ask-matt.md-cb27a380.md` — origin: https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/docs/engineering/ask-matt.md (revision 2026-09-30 — the "it told me to edit a SKILL.md" durability caveat)
