# Diagnose the environment before blaming the model

When a model's output looks like "slop," check whether it's actually a correct
adaptation to a constraint in the environment before concluding the model is
bad. Someone accused Opus 4.8 of generating slop for using a plain-text column
instead of a database enum; Matt's diagnosis was that the "bug" wasn't a model
failure at all — "SQLite doesn't have enums." The model picked the only option
that actually works in that database; reading it as sloppiness mistakes a
correct environment-aware choice for carelessness.

## The fix for an environment gap is a steering-doc rule, not a worse opinion of the model

Once the real cause is identified — here, that the project wanted enum-like
safety enforced a different way (a `CHECK` constraint, as the reporter later
added by hand in Drizzle) — the fix is to write that down where the agent will
read it next time: "now you've got a simple rule you can encode in a steering
doc and it'll never happen again." A rule the agent didn't know about isn't a
capability gap to route around case-by-case; it's a one-time addition to
`CLAUDE.md` (or, if it's mechanically enforceable, a hook — see
[[deterministic-hooks-over-prose-rules]]) that closes the gap permanently.

## Don't over-correct into never blaming the model either

Matt is explicit this diagnostic step isn't a blanket excuse: "although
sometimes you can blame the model, ofc." The discipline is doing the diagnosis
*first* — is this actually explainable by a constraint the model correctly
respected, or is it genuinely a bad decision the model made unprompted — rather
than defaulting to either verdict. Only once you know which one you're looking
at do you know whether the fix is a steering-doc rule or a different model/
prompt.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080573297557721316-13e4a49e.md` — origin: https://x.com/mattpocockuk/status/2080573297557721316
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080576449933644071-b5704544.md` — origin: https://x.com/mattpocockuk/status/2080576449933644071
