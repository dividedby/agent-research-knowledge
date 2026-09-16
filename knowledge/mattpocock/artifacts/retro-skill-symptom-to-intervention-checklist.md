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
  have caught the mistake. Read the repo's own check command first (its
  `package.json`/build-tool `lint`/`check` scripts, its CI workflow) so a
  check that already exists but sits unwired or silently broken is the
  finding, not a reinvention. Trigger: the agent made an error a check would
  have caught, **or** the repo has no guardrail at all — no pre-commit hook
  and no CI job running its lint/typecheck/test command. A repo with no
  guardrail is itself a finding: an un-linted repo is a standing missed
  opportunity, not a neutral default.
- **Coding standards** — the reviewer agent needs a new rule, or an existing
  one needs clarifying or removing. Classify the violation first: a
  **mechanical** one (a fixed syntactic pattern, a banned API, an import
  shape, a file-location rule) gets a deterministic check, full stop — a
  custom rule in the repo's own linter, a new pre-commit hook, or a new CI
  job, whichever the repo's language and existing guardrail make cheapest.
  `CODING_STANDARDS.md` prose is reserved for genuine **judgement calls**
  (cross-file consistency, "matches the surrounding style") that no
  guardrail could ever substitute for — default to building the check over
  writing the rule. Trigger: the reviewer failed to catch a mistake.
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

## Three targets, and what distinguishes it from `improve-codebase-architecture`

Matt's own compressed framing of the skill's purpose: it "gives you
opportunities to improve your codebase, skills, and steering over time based
on actual session data" — three targets (codebase, skills, steering docs), all
gated on having real session history to mine, which is the concrete
distinction from its sibling `improve-codebase-architecture`: "I would say
that improve codebase architecture requires zero inputs, whereas `/retro`
needs a session history to work well." The two skills look similar on the
surface — both surface improvement opportunities — but one works cold on the
codebase alone and the other only has something to say once a session has
actually happened.

## `/retro` stays human-in-the-loop by design

Responding to skepticism that an agent can reliably self-improve without a
knowledgeable person driving it, Matt agrees rather than pushing back: "Agree,
`/retro` is HITL." This is the same discipline the seven-category schema above
enforces structurally — candidates are proposed and ranked, never applied
unattended — restated directly as a design commitment rather than left
implicit in the mechanism.

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

## A later revision adds a classification test inside two categories

A subsequent edit to the same `SKILL.md` sharpens two of the seven triggers
rather than adding an eighth category. For "automated checks", it forces a
lookup step before the finding is allowed to fire: check the repo's *actual*
check command (its build tool's lint/check scripts, its CI config) so a
control that already exists but is unwired or silently broken gets surfaced
as the real bug, instead of the retro re-proposing a check the repo already
has. It also promotes "no guardrail exists at all" from a non-finding to a
finding in its own right — absence of a CI-enforced lint/typecheck/test gate
is treated as a standing gap, not a neutral baseline.

For "coding standards", it inserts a classification test ahead of the
category's existing implementation/review routing (above): is the violation
**mechanical** (a fixed syntactic pattern, banned API, import shape,
file-location rule) or a **judgement call** (cross-file consistency, "matches
the surrounding style")? Mechanical violations skip prose entirely and go
straight to a deterministic check — this is the same "if it can be enforced
mechanically, make it a hook/lint rule, not a `CLAUDE.md` sentence" instinct
`deterministic-hooks-over-prose-rules` documents as a general rule; here it's
codified as the retro skill's own gate on when to write a
`CODING_STANDARDS.md` rule versus build a check. Only genuine judgement calls
— the kind no guardrail could substitute for — still earn prose.

## The composition, stated directly: `/retro` writes, `/code-review` reads

The implementation/review routing argument above (retro's coding-standards
category defers to the reviewer, not the implementer) has a concrete
mechanical counterpart Matt states as a plain fact about the two skills:
"`/retro` can create it. `/code-review` reads it." — "it" being a
`CODING_STANDARDS.md` entry. The observation-driven feed mechanism
`review-skill-two-axis-with-smell-baseline` documents ("Notice the agent is
doing something bad, write it in `CODING_STANDARDS.md`") doesn't have to be a
manual step a human performs after noticing a pattern across sessions —
`/retro`'s own coding-standards category is the automated version of the same
noticing, writing the correction at session-end so `/code-review` has a new
rule to enforce on the very next diff.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2099960207098966073-ef27384f.md` — origin: https://x.com/mattpocockuk/status/2099960207098966073
- `sources/mattpocock/skills-repo/skills-in-progress-retro-SKILL.md-95ca61b1.md` — origin: https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/in-progress/retro/SKILL.md (revision 2026-09-16, origin https://github.com/mattpocock/skills/blob/f2d3b53dbed2104c61dd8a23f867ec8533542112/skills/in-progress/retro/SKILL.md)
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-08-25, origin https://github.com/mattpocock/skills/blob/c4745476a77d0b34af2933a01cf13f9bcd22fc30/skills/in-progress/README.md — `retro` listed as a STUB)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2097972745023754353-653b2e18.md` — origin: https://x.com/mattpocockuk/status/2097972745023754353
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2098062605407461744-a5f92d77.md` — origin: https://x.com/mattpocockuk/status/2098062605407461744
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2098063469572415819-5b9203f5.md` — origin: https://x.com/mattpocockuk/status/2098063469572415819
