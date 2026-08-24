# Frontier-parallel implementer subagents in worktrees land a whole spec as one PR

`implement-spec` treats a spec's tickets as a **task graph**, not a flat list:
blocking relationships between tickets create a **ready frontier** of
everything currently unblocked, and the skill's job is keeping that frontier
as wide as possible by running one **implementer subagent per ticket**, each
in its **own worktree and branch**, backgrounded for concurrency. A **merger
subagent** lands each completed ticket onto the shared PR branch as it
finishes, and every merge re-evaluates the frontier — closing one ticket can
unblock others, which fire immediately rather than waiting for the whole
batch to complete. This is dynamic, continuous fan-out, not a fixed
round-per-iteration like sandcastle's batch loop
([[sandcastle-plan-execute-merge-loop]]): here the frontier can widen
mid-run, not just once at the top of a bounded outer loop.

## Sparse context, not shared conversation

Subagents don't talk to each other directly, and the skill is explicit they
shouldn't need to: communication stays sparse, through **context pointers** —
the spec, the tickets, prior research notes, and previous commits — rather
than duplicating information into each subagent's prompt. An optional
**exploration subagent** front-loads this: it investigates the codebase or
external docs once, up front, and saves its findings as markdown notes
*outside the repo* so every implementer subagent that follows can read them
instead of re-exploring the same ground independently. This generalizes
[[research-as-delegated-background-reading]]'s single-reader pattern — a
background agent's cited artifact feeding one downstream decision — into a
shared read by an arbitrary number of concurrent siblings.

## The worktree-per-subagent answer to a known gap

[[implement-trusts-upstream-without-reverifying]] documents that the plain
`/implement` skill has no concept of a second session running concurrently in
the same checkout — sessions sharing one working directory corrupt each
other's commits and stashes, and worktrees alone are only a partial
community workaround (`refs/stash` is still shared across worktrees).
`implement-spec` is the shipped fix at the skill-authoring level: every
implementer subagent gets its own worktree *and* its own branch, so
concurrent implementation no longer depends on the caller remembering to
isolate sessions by hand.

## One final review pass, not one per ticket

Only after every ticket completes does the skill run a single `/code-review`
pass over the whole PR branch, fixed by one implementer subagent — review
happens once, against the assembled result, not once per ticket mid-flight.
Worktrees are torn down as the last step, once the PR is marked ready.

## Firsthand trial: numbers and a stated philosophy

Trying the skill himself, Matt frames its ambition directly: it "should be
able to smash out huge chunks of work autonomously with minimal supervision"
— the point of the frontier fan-out above is unattended throughput, not just
concurrency for its own sake. A single real run reports concrete numbers:
"ran for 1hr 20, built 6 tickets, 120K context in the main orchestrator (with
some inefficiencies I can cull)... Overall, I like it" — the orchestrator's
own context is the resource under pressure here, not any individual
implementer subagent's. Asked how conflicts are handled when multiple
implementers touch the same code, his answer names the two mechanisms this
doc already covers: "Worktrees. And a merger agent that merges them back
in." A smaller aside on why the skill stays easy to tweak: "Markdown is a
lot simpler of an API than code."

He also states the operating philosophy behind reaching for a heavy
multi-agent implementer at all: the goal of his skills is "to make people
feel comfortable with the agents doing the work AFK" — "heavy up front
alignment," then "prototyping and then a long implementation session, and
then review at the end." Pressed by a skeptic on whether anything can
reliably produce a large change in one go, he ties the claim directly to this
skill: "it's pretty good as long as you do a lot of alignment work upfront."
That's not a universal rule, though — "For certain kinds of work you may
really need to watch the agent like a hawk," especially "when you're getting
started with AFK workflows." `implement-spec`'s design (agreed spec and
tickets in, one review pass at the end, out) sits at the heavy-alignment-
then-hands-off end of that spectrum, not the only mode Matt endorses.

## Trade-offs: convenient, but a deliberate step down from determinism

Matt is explicit that the convenience comes at a cost. Weighing
`implement-spec` after the trial: "What I like about this is that it's easy
to use, pretty foolproof, and having an agent orchestrate this smooths things
over. What I hate is that it's definitely slower, has a scaling limit (the
orchestrator's context window) and replaces what should be a deterministic
system with an agent, which is always worse." He ranks the approaches on an
explicit tier list — "S: / A: Deterministic orchestrator / B: /implement-spec
/ C: / F: /goal" — placing a not-yet-built deterministic orchestrator above
the agent-orchestrated version he actually shipped and tried, and both well
above `/goal`'s unscoped rolling-context approach (see the AFK-only chunking
argument in [[spec-and-tickets-plan-split]]). The skill reads as a
considered stepping stone toward a system he'd rather build deterministically,
not an endpoint.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-implement-spec-SKILL.md-ca6452a8.md` — origin: https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/in-progress/implement-spec/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090744569960824949-d9f86190.md` — origin: https://x.com/mattpocockuk/status/2090744569960824949
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090746680551383294-7aeb5959.md` — origin: https://x.com/mattpocockuk/status/2090746680551383294
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090747462973571302-5ee3753b.md` — origin: https://x.com/mattpocockuk/status/2090747462973571302
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090748122896924840-b45a9c1a.md` — origin: https://x.com/mattpocockuk/status/2090748122896924840
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090747237114507617-d03ee59b.md` — origin: https://x.com/mattpocockuk/status/2090747237114507617
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090749578983157861-ee02d24b.md` — origin: https://x.com/mattpocockuk/status/2090749578983157861
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090749766925787353-26768850.md` — origin: https://x.com/mattpocockuk/status/2090749766925787353
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090750179259380066-87389871.md` — origin: https://x.com/mattpocockuk/status/2090750179259380066
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2090761149268533710-54d540be.md` — origin: https://x.com/mattpocockuk/status/2090761149268533710
