# Token economics: the bill is asymmetric, and you control the output side

The unit you are billed in is the token — the atomic chunk a model encodes text
into, roughly word-sized but not exactly. Two facts about how tokens are priced
turn into a concrete working lever, and Matt's "what are tokens" primer states
both plainly.

## What actually counts as input

Every model-provider request sends an *input* that is more than your latest
message: it is the whole conversation history, the system prompt, and the tool
definitions — all re-sent on each request, because the model is stateless and
carries nothing forward on its own. This is the mechanical reason context hygiene
is an economic concern, not just a quality one: a bloated system prompt or a long
accumulated history is re-billed on *every* turn, which is the same pressure that
makes [[claude-md-is-an-instruction-budget]] and [[keep-the-agent-in-the-smart-zone]]
matter for cost as well as for reasoning.

## Measure the payload before you trim it

The input side is invisible by default — you never see the tool definitions and
system-prompt scaffolding riding along with every message, only your own text.
So the fix starts with instrumentation, not guessing. Claude Code's `/context`
command breaks the window down by category (system prompt, system tools, MCP
tools, memory, messages), but it reports tools as one aggregate figure, not a
ranking; to find which *specific* tool or bundled skill is the expensive one,
put a transparent logging proxy between the CLI and the API — it forwards every
request unmodified and just records what passed through, so the CLI never
notices — and read its size-ranked output. Only once you know which line item
is large is trimming a targeted cut instead of a guess.

## Two levers, coarse then fine

Trimming then works top-down. A `disable*` setting (`disableBundledSkills`,
`disableWorkflows`, etc.) removes an entire feature and everything it bundles
in one flag — the first, coarsest pass, for a whole feature that isn't earning
its place. `permissions.deny` with a **bare tool name** then picks off
individual tools the flags don't reach. The distinction that makes or breaks
this lever: a scoped deny rule (`"Bash(rm *)"`, `"Skill(dataviz)"`) blocks the
matching call but leaves the tool's full definition — and its token cost — in
every request; only a bare name (`"NotebookEdit"`) strips the definition
itself. The goal isn't "stop the tool from running," it's "stop paying to
describe it on every turn," so a scoped rule silently fails to save anything.
Re-run `/context` afterward to confirm the number actually moved — measurement
brackets the change on both ends rather than trusting that the settings did
what they were supposed to.

## Output is the expensive half, and it's the half you steer

Input and output tokens are billed at different rates, and output is the dearer
one — generating a token costs more compute than reading one. The practitioner
move follows directly: **design prompts so the model produces fewer output
tokens.** You have less direct control over input (history and the standing brief
accrete), but you can shape a request to return a terse answer, a diff, or a
structured block rather than a discursive essay — and that asymmetry is where the
savings live. (Provider-side prefix caching cuts the input side too, re-billing an
unchanged prefix at a much lower rate — a reason to keep the stable part of a
prompt stable.)

## Match the format to the agent, not to the human habit

The same output-shaping logic governs *format* choice, not just length. Matt's
rule: **any to-agent communication should be in a token-efficient format** — which
is why he wants the recurring "HTML vs Markdown" debate dead. The mistake he calls
out is treating "put input into a richer format" as a golden hammer that hits every
nail; a richer, more verbose representation that helps a human (or a rendering
layer) is dead weight when the consumer is a model paying per token. The resolution
is not one winner but *right format per purpose*: a stack uses HTML for the things
that need it and Markdown for the things that don't — you pick the cheapest
representation the consumer can act on, rather than standardizing on the prettiest.

## Why vocabulary size sits underneath all of this

Tokenization is learned bottom-up from a corpus — characters, then frequent
character groups, then groups-of-groups — so a larger vocabulary splits a given
word into *fewer* tokens (a rare coinage like "Frabjous" fragments into many).
The payoff loops back to the same place as Matt's language discipline: common,
canonical terms tokenize cheaply and predictably, which is one more reason a
[[shared-language-as-agent-fuel|precise shared vocabulary]] makes an agent both
sharper and cheaper to run.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-what-are-tokens-61b05ccd.md` — origin: https://www.aihero.dev/what-are-tokens
- `sources/mattpocock/aihero/https-www.aihero.dev-how-to-kill-the-bloat-in-claude-codes-s-6eff38d4.md` — origin: https://www.aihero.dev/how-to-kill-the-bloat-in-claude-codes-system-prompt
- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061888307231945005-94786110.md` — origin: https://x.com/mattpocockuk/status/2061888307231945005
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061888451700486547-e7f2ccaf.md` — origin: https://x.com/mattpocockuk/status/2061888451700486547
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061888589542162693-79619669.md` — origin: https://x.com/mattpocockuk/status/2061888589542162693
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2061889988761960787-38e06b2c.md` — origin: https://x.com/mattpocockuk/status/2061889988761960787
