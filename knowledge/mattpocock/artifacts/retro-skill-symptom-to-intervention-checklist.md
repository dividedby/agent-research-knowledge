# A retro's output is a symptom mapped to a fixed intervention type

A session-end retrospective is only safe to automate if what it's allowed to
write is bounded in advance — otherwise "record what you learned" degrades
into freeform clutter (see `codebase-is-the-memory-system`'s clutter worry).
The `retro` skill (still a STUB — design notes only, not yet functional)
resolves this by fixing seven intervention categories up front, each keyed to
a concrete "use when" trigger drawn from what actually went wrong in the
session, rather than leaving the model to invent its own remediation:

- **Navigation** — a hidden dependency between files cost a long search → add
  a navigation pointer. Trigger: the session took a long time to find
  something.
- **Automated checks** — lint, typing, tests, or a filesystem linter could
  have caught the mistake. Trigger: the agent made an error a check would
  have caught.
- **Coding standards** — the reviewer agent needs a new rule, or an existing
  one needs clarifying or removing. Trigger: the reviewer failed to catch a
  mistake.
- **Global AGENTS.md** — an instruction belongs in coding standards (or an
  automated check) instead of the always-loaded steering file. Trigger: the
  global file is getting large, in the repo or the user's own global scope.
- **Tool economy** — an expensive tool call, or a token-inefficient custom
  CLI/MCP, could be streamlined. Trigger: the agent made an expensive call.
- **No-ops** — an instruction in a steering file that never actually changed
  behavior. Trigger: the steering files are large and unwieldy.
- **Information access** — the agent lacked a piece of information it needed
  (dev-server logs, readonly access to a third-party service). Trigger: a
  crucial fact wasn't available.

Candidates are then presented to the user ranked by severity — the skill
proposes, it doesn't write unattended. The fixed taxonomy is what makes this
different from unconstrained self-improvement: every finding is forced into
one of seven pre-agreed intervention shapes, so a session can't invent a new
kind of file or a new kind of rule to accrete. This is the concrete design
answer to the risk Matt names elsewhere in the collection — that models are
"REALLY bad at improving their own behavior" unattended — applied at the
schema level rather than as a prose caveat.

## Coding-standards fixes route to review, not implementation

The skill's own rationale for treating "coding standards" as its own category
rather than folding it into a generic AGENTS.md edit: **implementation carries
the most context pressure** (exploration, writing code, debugging), while
**review carries the least** (it receives a diff, no exploration needed) — so
the reviewer, not the implementer, should own enforcing standards. This is the
same budget argument `review-skill-two-axis-with-smell-baseline` documents in
depth for `code-review`'s `CODING_STANDARDS.md` accretion; the retro skill's
category checklist is the generalized, pre-shipped version of that same
routing decision, applied to every kind of session learning rather than to
code smells alone.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-retro-SKILL.md-95ca61b1.md` — origin: https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/in-progress/retro/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-08-25, origin https://github.com/mattpocock/skills/blob/c4745476a77d0b34af2933a01cf13f9bcd22fc30/skills/in-progress/README.md — `retro` listed as a STUB)
