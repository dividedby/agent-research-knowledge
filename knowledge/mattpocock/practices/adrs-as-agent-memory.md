# ADRs are agent memory: the thinnest layer of what code can't say

Matt's strongest recent claim about documentation for agents is that writing ADRs
"has been such a good decision" — because **capturing the non-obvious decisions in
a codebase makes every agent in your stack that touches it smarter.** An ADR is
"the thinnest layer of docs that captures the stuff code can't": the *why* behind
a gnarly choice, the alternatives rejected, the trade-off that isn't visible in
the diff. Code shows what; ADRs preserve the reasoning a fresh agent would
otherwise re-litigate or quietly violate.

This is the constructive half of his anti-doc-rot stance (see
[[claude-md-is-an-instruction-budget]]): the reason it's safe to delete most
markdown and forbid `/init` is that the one kind of doc worth keeping —
decisions — is exactly the kind code can't regenerate. Asked whether to keep a
sprawling design doc, his answer is blunt: "Absolutely not, that's cruft. Kill it
and write ADRs instead."

## One stack per bounded context, always agent-created

Two organizing rules fall out of treating ADRs as agent memory rather than a
changelog:

- **One stack of ADRs per bounded context** — not one global pile. The decisions
  that make an agent smarter about the billing context are noise in the auth
  context; scoping the stack to the context keeps each decision load-bearing where
  it's read. (This mirrors his per-context `CONTEXT.md` glossary discipline in
  [[shared-language-as-agent-fuel]].)
- **Agent-authored, via the skill** — "always agent-created, with the skill
  above." The human makes the decision; the agent writes the record in the house
  format. The ADR-writing skill is what keeps a hundred records consistent enough
  to be navigable.

His own example is Sandcastle: "only 20 of them so far, but each one captures a
gnarly decision that is essential to remember." That corpus bears the claim out —
its `docs/adr/` reads as exactly the reasoning code can't show: *why* inline prompts
pass through literally (ADR 0008, so forwarded content with `{{…}}` doesn't trip the
template scanner), *why* prompt expansion fails fast instead of retrying (ADR 0020,
the AFK cost of running on a degraded prompt), *why* structured output is separate
from the completion signal and how its error became resumable (ADR 0010). Each is a
trade-off with rejected alternatives written down, so a future agent inherits the
decision instead of re-litigating it — which is what makes the whole
[[thin-fail-fast-harness]] stance legible to anyone (human or agent) who picks the
project up.

## Consumed by exploration, not by preloading

ADRs scale as agent memory only because they aren't all forced into context. "I
don't pass them all into context, I allow the user [and the agent] to explore them
as needed via filenames." The stack is a *discovery tree*, not a system-prompt
dump: a descriptive filename per decision, pulled in just-in-time when a task
touches that area. This is the same progressive-disclosure logic that governs
`CLAUDE.md` and skills — the ADR layer adds durable decisions to the tree without
ever spending the smart zone ([[keep-the-agent-in-the-smart-zone]]) on decisions
the current task doesn't need.

## When a decision earns an ADR

Matt is deliberately stingy about which decisions qualify — the bar is recorded in
[[shared-language-as-agent-fuel]]: hard to reverse, surprising without context,
and the result of a real trade-off with genuine alternatives. ADRs are agent
memory precisely *because* they're rationed; a log of everything that happened
would bury the few decisions that actually keep agents from going wrong.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060454199838544079-01e5ad70.md` — origin: https://x.com/mattpocockuk/status/2060454199838544079
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060454591305527750-5b769f52.md` — origin: https://x.com/mattpocockuk/status/2060454591305527750
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060454870830797230-88824df7.md` — origin: https://x.com/mattpocockuk/status/2060454870830797230
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060456292104204394-00a65029.md` — origin: https://x.com/mattpocockuk/status/2060456292104204394
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060623956533514297-82064a3c.md` — origin: https://x.com/mattpocockuk/status/2060623956533514297
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2060624055288361200-1f17a887.md` — origin: https://x.com/mattpocockuk/status/2060624055288361200
- `sources/mattpocock/sandcastle/docs-adr-0008-inline-prompts-skip-processing.md-5f56cccd.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0008-inline-prompts-skip-processing.md
- `sources/mattpocock/sandcastle/docs-adr-0020-prompt-expansion-fails-fast.md-20cdf35e.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0020-prompt-expansion-fails-fast.md
- `sources/mattpocock/sandcastle/docs-adr-0010-structured-output.md-df5103e4.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0010-structured-output.md
