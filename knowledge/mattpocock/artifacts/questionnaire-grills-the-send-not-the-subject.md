# `to-questionnaire`: grill the send, not the subject

Most of Matt's grilling skills interview the user because the user holds the
answer. `to-questionnaire` is for the opposite case: a decision the user
*can't* answer alone because someone else holds the missing knowledge. The
skill's design move is to invert what gets interviewed — instead of grilling
the user about the subject they can't resolve, it grills them only about the
**send**: who the questionnaire goes to, and what the user needs back. Both
of those the user can always answer, even when the underlying subject is
opaque to them. The output is a Markdown document the user hands to one
person — async, or filled out together in a meeting — whose questions are
aimed squarely at the **gap** between what the recipient knows and what the
user needs, derived from those two send-facing answers rather than from
interviewing the user about the subject itself.

This is a variant of the same align-before-building instinct behind
`grill-me`/`grill-with-docs` (see `align-before-building-grilling`), applied
where the interview technique breaks down: grilling only works when the
interviewee holds the answer, and here they don't. Delegating the actual
questions to a document — rather than trying to grill the user into
answering on behalf of someone else — keeps the skill from silently
inventing an answer the user was never in a position to give.

## Ordering and framing choices that follow from the recipient never having been in the room

Because the recipient wasn't part of the conversation that produced the
questionnaire, the document is written as a **discovery questionnaire**, not
a request for confirmation: a "Context" section orients someone who wasn't
in the user's head, one paragraph, not a page. Questions are ordered
most-important-first specifically because the send is often async — "you may
only get one pass" — so a recipient who only answers the first few still
delivers the highest-value information. Each question is single-idea, never
compound, with an answer stub directly beneath it, and a one-line "why this
matters" only where the question is genuinely ambiguous or invites a
throwaway answer — added selectively, not as boilerplate, to hold down
noise. A closing "Anything else?" catch-all admits the questionnaire's own
questions might not cover everything worth knowing.

## Where the answer lives routes you to the right skill

Four skills split on the same axis — where the missing answer actually is —
and `to-questionnaire` is only the right one when it's in someone else's head:
your own head, unsharpened, is `grill-me`; the codebase is `grill-with-docs`;
nobody's head yet, because the question needs something concrete to react to,
is `prototype`. This is also what separates `to-questionnaire` from
"`grill-me` in batch mode": `grill-me` already delivers its questions as a
whole round rather than one at a time, so front-loading the questions isn't
the differentiator — whose head holds the answers is. The common trigger is a
grilling session that stalls on a question that isn't the user's to answer:
run `to-questionnaire` in that same conversation to take it offline, then
bring the answer back and resume grilling.

## Two shapes considered and deliberately not built

Dependent, branching questions — skip section D if you answered A — were
explored and dropped. The objection is the same one that shows up wherever an
agent is asked to plan multiple steps ahead of a real answer: a model planning
more than two or three questions ahead plans badly, and a branching document
has to plan every branch ahead of every answer it hasn't received yet. Static,
themed, most-important-first beats an adaptive tree it can't reliably build.

The document also stays single-recipient by design: one run produces one
document for one person, even though splitting questions by recipient inside a
single document is a request people have made. If three people hold three
parts of the answer, the fix is to run the skill three times, not to make one
document route sub-questions by role. Both are explicit non-features, not
unfinished gaps — the same "record the deliberate no" instinct as
`.out-of-scope/` elsewhere in the collection (see
`out-of-scope-as-design-discipline`).

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-to-questionnaire-SKILL.md-bf6c9b87.md` — origin: https://github.com/mattpocock/skills/blob/e9fcdf95b402d360f90f1db8d776d5dd450f9234/skills/in-progress/to-questionnaire/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-07-15, origin https://github.com/mattpocock/skills/blob/1d1009ed5d1b2474249aa0e8fa10a7483c248552/skills/in-progress/README.md — `to-questionnaire` listed)
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-to-questionnaire-79e1552f.md` — origin: https://www.aihero.dev/skills-to-questionnaire
