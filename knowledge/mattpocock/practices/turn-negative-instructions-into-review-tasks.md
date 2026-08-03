# Turn negative instructions into review tasks

LLMs are "notoriously bad at following negative instructions" — telling a model
"don't do these footguns" upfront is weaker steering than the same list applied
as a search-and-eliminate pass after generation. Matt's fix is structural, not
a wording tweak: move the prohibition out of the prompt entirely and into
`/code-review`, where "don't do X" becomes "find and eliminate X" — a framing
the model is much better at executing, because it's now a positive detection
task instead of a suppressed-behavior instruction. Precisely because negative
instructions don't hold, he removed them from his harness rather than trying to
phrase them more forcefully.

## Why review, not the prompt

A "don't" has to suppress a behavior the model might otherwise produce, with no
way to verify the suppression worked. A review pass instead asks the model to
actively hunt for and remove specific footguns already present in a diff —
the same list of concerns, reframed as a checklist to search against rather
than a rule to obey while generating. Asked when to stop hunting for more
footguns (an agent will keep finding *something* if asked repeatedly), Matt's
answer is that one pass is usually enough — the review isn't meant to be run
to exhaustion, it's a single deliberate elimination pass over the diff that
just landed.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082880629092347942-29a9d801.md` — origin: https://x.com/mattpocockuk/status/2082880629092347942
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082886149333258415-b3589886.md` — origin: https://x.com/mattpocockuk/status/2082886149333258415
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082925086546235461-c7c7c159.md` — origin: https://x.com/mattpocockuk/status/2082925086546235461
