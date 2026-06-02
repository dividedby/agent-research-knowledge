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
- `sources/mattpocock/aihero/https-www.aihero.dev-ai-coding-dictionary-ece441bb.md` — origin: https://www.aihero.dev/ai-coding-dictionary
