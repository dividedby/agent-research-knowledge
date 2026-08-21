# Split the plan: a spec for the destination, tickets for the journey

For big chunks of work, Matt recommends splitting a single plan document into
two: a **spec** (where you're going) and **tickets** (the steps on the journey
there). The split exists to make a specific failure cheap: plans change
mid-implementation, and a monolithic plan doc conflates "what we're building"
with "what's left to do," so a change of direction forces you to untangle both
at once. Keeping them separate means you can pivot the destination without
re-deriving the whole journey.

## The procedure when the plan changes

If you discover mid-implementation that the destination itself needs to
change: edit the spec, delete every ticket that hasn't been completed yet, and
create new tickets from the revised spec. Completed tickets stay as a record;
only the unwalked path gets thrown away and re-derived — because the spec, not
any individual ticket, retains the destination.

## Ticket-sizing and the point of clearing between them

Each ticket is scoped to **one coding session**. That sizing is what makes
clearing context between tickets safe and cheap: because the spec (not your
head, not the previous ticket's session) is what retains the destination, you
can `/clear` between tickets without losing the plan — or `/compact` instead
if you'd rather not double-pay for re-exploring the codebase from scratch.
**Clearing context between each ticket is the main, load-bearing benefit of
`/to-tickets`** — routing tickets through something that skips this (e.g. a
`/goal` command that keeps rolling context forward) throws away exactly the
property that makes the split worth doing.

The skills for this are `/to-spec` and `/to-tickets`, both in Matt's public
skills repo. The normal sequencing is to run `/to-tickets` immediately after
`/to-spec`, in the same session — you don't need a fresh session to make the
jump from destination to steps. The one exception is when the tracker is
GitHub issues specifically: there, clearing or starting a new thread before
`/to-tickets` is worth doing, likely because writing tickets as GitHub issues
benefits from a clean context rather than one still carrying the spec-writing
conversation.

## Specs are disposable, not a living SDD document

Matt deletes every spec once the work it describes is done — and is explicit
that this isn't spec-driven development in the sense the term is usually meant:
**"I delete all specs once completed. That ain't SDD."** SDD as commonly
practiced treats the spec as a durable, living artifact that keeps describing
the system after the work lands; Matt's spec is scaffolding for *getting to* the
implementation, not documentation *of* it. Pressed on whether a human needs to
review the spec, his answer draws the same line from the other side: **"Just an
agent doc"** — it exists to give the implementing agent (and `/code-review`) a
checkable target, not to serve as a human-facing artifact that needs sign-off or
long-term upkeep. Once the build matches the spec, the spec has done its job and
gets thrown away rather than maintained — the code, not the spec, is the record
that survives.

## It isn't spec-driven development — it needs its own name

Matt pushes back explicitly on the label people keep reaching for: "Everyone
always confuses my skills with spec-driven-development. It really annoys me.
The specs my skills create are intended to be deleted immediately — not kept
around, or treated as source code... They're just a projection of the
decisions made during grilling." Even Birgitta Boeckeler's narrower
"spec-first" framing (in a guest piece on Martin Fowler's site, which Matt
amplifies as a recommended read) still groups his approach under the SDD
umbrella, and he disagrees with that grouping too — floating "grill-driven
development" instead, half-seriously, precisely because SDD as a term implies
the spec is the thing that matters, when for him it's the grilling that
mattered and the spec is just what fell out of it. Pressed on whether this
pushback is a knock against SDD itself, he draws the line explicitly: "I'm not
disparaging it, I'm just saying that my approach isn't SDD" — the objection is
to the label being applied to his workflow, not to spec-driven development as
a legitimate approach for people who actually want a durable spec.

Asked directly what he'd call it instead, in a different exchange, one
framing he's offered in passing lands closer to a familiar-to-devs category
than a new methodology name: "IMO a spec is a RFC" — a checkable proposal
document, not a durable spec-as-source artifact, which is the same "documents
are for the model, not the human" naming instinct below applied to the term
itself.

## Why specs go stale: they're a cache, not a source

The reasoning behind deleting specs rather than archiving them as living docs:
"Specs are a cached representation of the code. As soon as a new commit
arrives, the cache will likely go stale. Agents reading that stale cache will
take it for ground truth. So, archive your specs." A spec is a snapshot of a
decision at the moment it was made; the codebase keeps moving after that
moment, and nothing re-derives the spec when it does. An agent that treats an
un-refreshed spec as authoritative is reading a cache invalidated by every
commit since — which is the concrete failure mode "specs are disposable" (above)
exists to prevent, restated as a caching argument rather than a process one.

## Documents are for the model, not the human

Pressed on why the spec/tickets split exists at all — isn't it just Jira with
extra steps? — Matt's answer reframes the whole vocabulary: **"Every 'document'
I use is designed for the constraints of models, not for humans… I'm using the
terms 'spec' and 'tickets' because they are familiar to devs — not because I am
trying to mimic Jira."** Each document earns its place by what it does for the
model, not by resembling a human process:

- **The spec exists to define the destination in a checkable artifact** — one
  `/code-review` can later verify the build against.
- **Tickets exist to split work into smart-zone-shaped sizes** — the same
  session-sized chunking `wayfinder` applies to open-ended planning
  (`decision-mapping-fog-of-war`), here applied to already-settled work.

This is explicitly an **AFK-only optimization**: Matt reports experimenting with
skipping tickets entirely — just a spec plus `/goal` — and getting worse
results, because an AFK agent without pre-scoped chunks doesn't reliably stay
in the smart zone on its own. The split isn't process for its own sake; it's a
chunking mechanism sized to a constraint the model has and a human doesn't.

## Archive, don't delete: the concrete mechanic

A later exchange sharpens "specs are disposable" into something more precise
than outright deletion: **"hence why I say 'archive', not delete."** Closed
GitHub issues are, in Matt's words, "just right for this" — the spec stays
retrievable but is no longer live. The concrete three-step mechanic: put the
code in a PR, mark the PR as `closes #X` against the issue holding the spec,
and the spec is auto-archived the moment the PR merges — no separate cleanup
step. The spec itself lives in the GitHub issue, not as a version-controlled
file that gets stripped from the repo by automation on merge; asked directly
whether it's version-controlled in-repo during the PR and stripped out
afterward, Matt's answer is simply "No, the spec is in a GitHub issue." Some
practitioners prefer storing archived specs somewhere the agent can find them
via grep — i.e. in the repo itself — which Matt agrees is fine as a variant,
so long as it's still an archive, not a live document.

The archive earns its keep as a review aid, not just a paper trail: reviewing
a merged PR usually means reviewing "the literal commits that implemented the
spec," and having the original spec sitting in the closed issue makes that an
"essential tool" — `/code-review` reviews the build against exactly this
archived target. This is also why Matt is unmoved by the argument that an
agent needs to keep reading a cached representation of the code to stay
effective: "I am happy with the agent itself being a seam, no need for it to
read a cached representation to make it effective" — the agent re-exploring
the live code is a better source of truth than an aging document, which is the
same "cache, not source" reasoning as the section above.

**Even an archived spec still drifts before it's archived.** The danger isn't
only post-merge staleness — often a spec is already out of date *before*
release, because QA surfaces edge cases that push the implementation away from
what was written down: "the spec was wrong to begin with." Archiving preserves
a historical snapshot, not a guarantee the snapshot was ever fully accurate.

**Regulated work is the explicit exception to "keep it thin."** For teams that
answer to compliance, an extremely detailed, implementation-exposing spec —
closer to a changelog than a design doc — is "well worth the time and tokens
to produce... if it's to meet regulations." Matt's blanket "specs are
disposable, keep them thin" advice assumes no external audit requirement;
where one exists, "it's a whole different kettle of fish" and the thin-spec
default doesn't apply.

**Archiving isn't a promise to keep everything forever, either.** Asked what
to do with old archived specs that have accumulated, Matt's answer keeps the
same "does this still say something" test as anywhere else in the discipline:
"delete the ones that no longer say anything of value." Archive first so the
spec survives long enough to be useful during review; prune later, once it
genuinely isn't.

## Wayfinder's map is a decision record, too fat to double as the spec

Asked whether the routing is always `Wayfinder → spec → ticket → implement`,
even once a wayfinder map already looks complete, Matt confirms the default
order holds — "in general, yes" — and names why the map can't just stand in
for the spec despite covering the same ground: "Wayfinder tends to be a
record of all decisions made, which is a bit too fat for a spec." The two
documents solve different problems even when built from the same discussion:
the map is comprehensive by design (every decision, the full fog-of-war
trail), the spec is a lean, checkable destination. A correspondent reported
their own Claude agents skipping the spec step, arguing the map's GitHub
issues already covered it; Matt treats that as the agent drifting from the
intended shape rather than a legitimate shortcut — the map is useful to
*reference* from the spec when a decision needs its full context, but writing
the spec is still the right move, not a step the map can absorb.

## A back-of-envelope heuristic for ticket count

When you're unsure how finely to slice `/to-tickets`, Matt offers a concrete
heuristic: estimate the total tokens the task will take (experience helps
here; when unsure, estimate high), divide by ~150k (the smart zone — see
`keep-the-agent-in-the-smart-zone`), and that's roughly the number of tickets
to aim for — a 1M-token refactor is "6.66 smart zones, so 7 tickets." He's
explicit it's a **rule of thumb, not a benchmarked number**: asked whether
150k was measured or "just vibes," his answer was simply "Rule of thumb." He
also frames it as something a human should see rather than something the
skill should compute and hide: asked why not bake the estimate into
`/to-tickets` itself, he called it "probably a useful number to surface for
the human making that judgement" — the estimate informs the human's sizing
call rather than replacing it.

## Several ideas at once: run each through the main flow, sized by weight

Asked how to avoid losing good suggestions when several ideas surface at once
(e.g. from a prototype session) without treating every one as equally
weighty, Matt's answer is not to batch them into one plan: run each idea
through the same main flow as normal, and let its own size decide which
branch it takes — "if it's small, grill and implement directly. If it's big,
use a spec and break it into tickets." One flow handles both cases; the size
of the idea, not a separate process per idea, is what decides the branch.

## `/to-spec` doesn't interview — grilling already happened upstream

Its predecessor `/to-prd` carried an interview step it would run if no prior
grilling had happened. The renamed `/to-spec` drops that step deliberately:
"Crucially, it does *not* interview you. The grilling already happened, so
`/to-spec` just synthesizes what's already in the conversation." Its workflow
shrank to three steps — explore the repo to ground the spec in the current
code, sketch the seams the feature will be tested at and check they match
expectations, then write the spec from a template — because reaching alignment
is now `grill-with-docs`'s or `wayfinder`'s job (see
`align-before-building-grilling`), not something the spec-writer re-does as a
fallback. Splitting "reach alignment" from "write it down" keeps each skill
doing exactly one job instead of one skill quietly absorbing the other's work
whenever the human skipped a step.

## Why this pairs naturally with AFK agents

The `/to-spec` / `/to-tickets` split "plugs into an AFK agent beautifully":
because each ticket is a self-contained, one-session unit of work anchored to
a durable spec, an AFK agent can pick up a ticket cold, complete it, and stop
— the same shape `durable-briefs-for-afk-agents` describes for issue-tracker
briefs, arrived at here from the planning side rather than the brief-writing
side.

## Seams get agreed at the spec, not invented downstream

Before `to-spec` writes a word, it sketches the seams the feature will be
tested at and checks them with the user — preferring seams that already exist
over new ones, and taking the highest one it can reach (the ideal count across
a whole change is one). Those agreed seams then travel through the rest of the
chain by reference rather than by re-confirmation: `tdd` is told to work only
at the seams the spec already settled, and `code-review` checks afterward that
only the agreed-upon seams were actually used. The binding is indirect — it
runs entirely through the spec document — which is exactly why the seam
conversation is worth taking seriously at this step rather than deferring it
to whichever skill happens to write the first test.

## `ready-for-agent` on the spec issue is a trap for AFK runners

The label `to-spec` applies to a published spec means "no further triage
needed" — an input designation, not a work order — but an AFK agent polling
the tracker for `ready-for-agent` can't see that distinction. Left unguarded,
it will try to build the entire spec in one run instead of picking up the
ticket-sized slices `to-tickets` derives from it afterward. This is the
most-reported rough edge on the skill, and the workaround is on the caller: 
exclude the parent spec issue explicitly in the AFK agent's prompt, or strip
the label from the spec once `to-tickets` has run over it.

## The template assumes a feature; an architectural change fights it

`to-spec`'s template leans on user stories, which is the wrong shape for a
refactor or a module-boundary change — the result is stories nobody asked for,
written around decisions that are really about interfaces and invariants. The
documented workaround is to lean on the implementation-decisions and
testing-decisions sections instead of the user-story frame, and let the
durable architectural calls land as ADRs via `grill-with-docs` rather than
trying to make the spec template carry them.

## Blocking edges are the point of a `to-tickets` artifact, not decoration

`to-tickets` doesn't just list tickets — every ticket declares its **blocking
edges**, the other tickets that must close before it can start, and those
edges are what let a tracker (or a human) compute the **frontier**: whichever
tickets have no open blockers left, and are therefore takeable right now, in
parallel if wanted. On GitHub this is meant to ride the tracker's own native
sub-issue and blocking-relationship support (`gh issue create --parent <n>`,
`gh issue create --blocked-by 12,15`), both available since `gh` v2.94 — but
in practice this is reported broken across a dozen runs and several models,
worse on Codex than on Claude: tickets land as plain siblings instead of
sub-issues, and a "Blocked by" line gets written into the issue body as prose
instead of a real blocking link (one report even had the agent assert GitHub
has no native blocking relationship at all, which is false). Because blocker
numbers are always known at creation time — blockers are published first — the
reliable move today is wiring the parent links and native blocking by hand
after a run, rather than trusting the template to have set them.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-to-spec-8b6729bc.md` — origin: https://www.aihero.dev/skills-to-spec
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-to-tickets-c067d73f.md` — origin: https://www.aihero.dev/skills-to-tickets
- `sources/mattpocock/aihero/https-www.aihero.dev-5-agent-skills-i-use-every-day-056774d5.md` — origin: https://www.aihero.dev/5-agent-skills-i-use-every-day (revision 2026-07-26 — the `/to-prd`→`/to-spec`, `/to-issues`→`/to-tickets` rename and the "does not interview" workflow change)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079926515257520400-ce5571da.md` — origin: https://x.com/mattpocockuk/status/2079926515257520400
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079926855788855524-9cb40b6e.md` — origin: https://x.com/mattpocockuk/status/2079926855788855524
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079926961313345825-47140eae.md` — origin: https://x.com/mattpocockuk/status/2079926961313345825
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079952609419407431-e86145f7.md` — origin: https://x.com/mattpocockuk/status/2079952609419407431
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2079999765350171119-255baf64.md` — origin: https://x.com/mattpocockuk/status/2079999765350171119
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080000544102375889-1d1b71fa.md` — origin: https://x.com/mattpocockuk/status/2080000544102375889
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080001909486682311-76073172.md` — origin: https://x.com/mattpocockuk/status/2080001909486682311
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080183646254752194-41f4e9ad.md` — origin: https://x.com/mattpocockuk/status/2080183646254752194
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2081655893427450117-c3eb72e3.md` — origin: https://x.com/mattpocockuk/status/2081655893427450117
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082527279511450028-e4f6dc2f.md` — origin: https://x.com/mattpocockuk/status/2082527279511450028
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082537296964792734-55952a54.md` — origin: https://x.com/mattpocockuk/status/2082537296964792734
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082716789557928007-49de553a.md` — origin: https://x.com/mattpocockuk/status/2082716789557928007
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082746319873913337-939eef47.md` — origin: https://x.com/mattpocockuk/status/2082746319873913337
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083563195671667176-12baec39.md` — origin: https://x.com/mattpocockuk/status/2083563195671667176
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083563358180012470-9d929ea2.md` — origin: https://x.com/mattpocockuk/status/2083563358180012470 (repost/endorsement: Birgitta Boeckeler's "spec-first" article on martinfowler.com, amplified by Matt as a recommended read, not his own claim)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083565169313980721-edb22ad9.md` — origin: https://x.com/mattpocockuk/status/2083565169313980721
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083580395291898351-fd95d407.md` — origin: https://x.com/mattpocockuk/status/2083580395291898351
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083586712291229754-8d4a76eb.md` — origin: https://x.com/mattpocockuk/status/2083586712291229754
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083600889281995187-3c39f827.md` — origin: https://x.com/mattpocockuk/status/2083600889281995187
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083601222464848256-e006bb1c.md` — origin: https://x.com/mattpocockuk/status/2083601222464848256
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083602954024587381-1e696e99.md` — origin: https://x.com/mattpocockuk/status/2083602954024587381
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083603074594033907-0a17ca86.md` — origin: https://x.com/mattpocockuk/status/2083603074594033907
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083604826231836675-3881e6c8.md` — origin: https://x.com/mattpocockuk/status/2083604826231836675
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083607411319833069-9127d586.md` — origin: https://x.com/mattpocockuk/status/2083607411319833069
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083607591762931728-8b34010c.md` — origin: https://x.com/mattpocockuk/status/2083607591762931728
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083650552936669328-5a67257a.md` — origin: https://x.com/mattpocockuk/status/2083650552936669328
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083842093630324743-fde70b59.md` — origin: https://x.com/mattpocockuk/status/2083842093630324743
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083842523772957132-cf5db06d.md` — origin: https://x.com/mattpocockuk/status/2083842523772957132
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2083862208795050365-882e642f.md` — origin: https://x.com/mattpocockuk/status/2083862208795050365
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087111966854730148-dab0316e.md` — origin: https://x.com/mattpocockuk/status/2087111966854730148
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087120207428907471-e2310da6.md` — origin: https://x.com/mattpocockuk/status/2087120207428907471
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087183449266196671-bade10ec.md` — origin: https://x.com/mattpocockuk/status/2087183449266196671
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087150963140255805-5a01a8ab.md` — origin: https://x.com/mattpocockuk/status/2087150963140255805
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087462098724950453-a0cd9f53.md` — origin: https://x.com/mattpocockuk/status/2087462098724950453
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090159967567245685-227fdea3.md` — origin: https://x.com/mattpocockuk/status/2090159967567245685
