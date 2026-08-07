# One computation backs every consumer, so they can never disagree

When a UI warning list, a release-blocking gate, and an agent-facing CLI verb all need to answer the same "is this ready to ship" question, compute the answer once and have all three read that single result — never let each surface implement its own version of the check.

## Publish Readiness: one walk, three readers

Course Video Manager's **Publish Readiness** answers "what stands between this Course and shipping?" for a CourseVersion as four lists: Unexported Videos, course-view lints, invalid Lesson role combos, and incomplete Videos. Only three of the four actually block a release — lints refuse the Publish outright, and invalid combos or incomplete Videos fail the later `course.json` build — while an Unexported Video is rendered by the Publish itself as its export stage, so it blocks nothing. One walk backs three surfaces that each independently needed this answer: the publish gate, the publish page's pre-publish warnings, and the read-only `cvm course readiness` CLI verb an agent can call. Because all three read the same computed lists, "can this ship?" can never come back with three different answers depending on which surface asked.

## Why this has to be a single seam, not three re-derivations

A blocking gate, a warnings panel, and an agent-facing query are typically built by whoever is touching that surface at the time, and it's tempting for each to write its own "is it ready" check inline — a scan of the same clips-and-chapters data, reimplemented three times. That's exactly the setup where the checks drift apart silently: the gate's definition changes, the warnings panel stays in sync only by luck, and an agent calling the CLI verb gets a fourth answer that matches neither. Naming the readiness computation once and having the gate, the UI, and the CLI verb all call it is what makes "can this ship?" a single, load-bearing fact instead of three loosely-correlated guesses — and it's what lets an agent trust the CLI's answer as much as a human trusts the publish page.

## The general shape

Whenever the same yes/no or what's-outstanding question needs answering from more than one entry point — a hard gate, a soft UI hint, and a query surface built for an agent — resist splitting it into "the strict version" and "the informational version" maintained separately. Compute the full underlying state once, and let each consumer decide independently which subset of it blocks and which is merely informational (as Publish Readiness does by marking only 3 of its 4 lists as blocking) — the *computation* stays singular even when its consequences differ by consumer.

## The same shape, in a skill's own logic

The principle isn't limited to a computed value — it applies just as well to
a skill's core procedure. Asked to split `/grill-me` off from
`/batch-grill-me` so each user-invoked entry point could evolve
independently, Matt declines: "I can't, because I need one canonical
`/grilling` skill that `/grill-me`, `/grill-with-docs` and `/wayfinder` rely
on." Three different invocation surfaces need the same underlying grilling
behavior; forking it per surface would let the ask-your-way-to-alignment
logic drift out of sync across all three, exactly the way three re-derived
readiness checks would drift. One canonical implementation, reused by every
consumer, is the only way to guarantee they can't disagree — whether the
shared thing is a computed value or a skill's procedure.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-07-30, new **Publish Readiness** entry)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085290713994953056-25939aa4.md` — origin: https://x.com/mattpocockuk/status/2085290713994953056
