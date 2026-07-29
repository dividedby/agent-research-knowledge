# Two install paths encode two philosophies: fork vs subscribe

The skill set ships through two installers that trade the same content for
opposite ownership models. **skills.sh** (`npx skills@latest add
mattpocock/skills`) copies the skill files into the target repo — editable,
"hack around with them, make them your own," the repo owns its copy from that
point on. The **Claude Code plugin** (`claude plugins install
mattpocock-skills`, or `/plugin install mattpocock-skills` from inside a
session) installs the same promoted set as a managed, read-only bundle that
updates in place whenever a new version ships — "you subscribe rather than
fork." Neither path is strictly better; they serve opposite intents —
customize-and-diverge versus stay-current-and-don't-touch — and offering both
means a user doesn't have to choose ownership over currency or vice versa. The
launch announcement names one more subscribe-side benefit beyond auto-updates:
every installed skill is namespaced under `mattpocock:` (e.g.
`mattpocock:code-review`), specifically so it never collides with a built-in
Claude Code command of the same name.

The choice is orthogonal to which agent you run. The README now presents
three doors, not two: Claude Code (plugin), Codex and other agents
(skills.sh), and explicitly a third, "for tinkerers" — the same skills.sh
installer, run *on Claude Code itself*, for anyone who wants editable files
rather than a subscription even though the plugin is available to them. The
philosophy split is fork-vs-subscribe, not Claude-Code-vs-everyone-else — a
Claude Code user can pick either one on purpose.

## The marketplace is scoped to the promoted set, mechanically

The repo is its own single-plugin Claude Code marketplace:
`.claude-plugin/marketplace.json` lists the one `mattpocock-skills` plugin,
and `.claude-plugin/plugin.json`'s `skills` array is exactly the promoted
bucket set (`engineering/` + `productivity/` — see
`buckets-and-promotion-discipline`). The plugin can't drift from what's
advertised elsewhere, because both draw from the same folder-driven
promotion gate rather than a separately-maintained list.

## Version sync is a manual obligation with a mechanical check

`plugin.json`'s `version` field must be bumped in lockstep with
`package.json`'s, because Claude Code reads the plugin manifest's version to
decide whether an already-installed subscriber sees an update — a forgotten
bump silently withholds a release from every plugin user. `claude plugin
validate . --strict` is run after touching either manifest as the mechanical
backstop for that easy-to-forget step, the same pattern as any invariant that
can't be enforced by the folder structure alone: pair the manual obligation
with a command that catches the human forgetting it.

## The fork path stays maintainable: `npx skills update`

Forking doesn't have to mean the copy quietly rots. `npx skills update` is
the one command that pulls the fork path's copy back to current — including
removing skills that have since been retired — so "customize and diverge"
still has a maintained path back to what's current, invoked on demand rather
than automatically. That's the deliberate difference from the plugin path:
subscribing gets the pull done *for* you on every release; forking gets the
same pull available *to* you, at a time of your choosing.

## Getting into the official marketplace removes a step, not a philosophy

Installing the plugin used to be two commands: add the `mattpocock/skills`
marketplace, then install the plugin from it. It's now one —
`claude plugins install mattpocock-skills` — because the plugin is listed in
Claude Code's own official marketplace, so there's nothing to add first and
updates keep arriving automatically. This is a friction fix on the subscribe
side only: the repo is still the single-plugin marketplace described above
(`.claude-plugin/marketplace.json`), just reachable without a manual add
step. It doesn't change what "subscribe" means, only how many commands it
costs to opt in.

## He resisted the plugin path, then found a way to keep it configurable

The plugin wasn't Matt's first instinct. Asked why it took so long to ship, he
is direct about his own reluctance: **"Initially I was opposed to it — I
didn't like the idea of people having a managed installation they couldn't
tinker with. But I caved to popular demand."** What made caving workable,
rather than just accepting the "you lose editability" trade-off above, was a
technical fix on the subscribe side: **"I found a way to configure the skills
without modifying them, which really helped."** — some means of steering a
managed, read-only bundle's behavior without forking it, closing the gap
between "subscribe" and "no control at all" that made him hesitate in the
first place.

## The plugin path is Claude-only for now, by explicit deferral

Codex and other Agent-Skills-standard harnesses are already served today —
by the skills.sh path, which installs into them the same way it does Claude
Code. A native Codex plugin equivalent to the Claude Code one is deferred,
not ruled out, and the reasoning lives in a dedicated ADR
(`.agents/adr/0002-ship-as-a-claude-code-plugin.md`) rather than being
re-litigated in the README each time someone asks. Setup is identical either
way: `/setup-matt-pocock-skills` runs once per repo regardless of which
install path put the skills there.

## Sources

- `sources/mattpocock/skills-repo/AGENTS.md.md` — origin: https://github.com/mattpocock/skills/blob/66898f60e8c744e269f8ce06c2b2b99ce7660d5f/AGENTS.md
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/CLAUDE.md (revision 2026-07-14, origin https://github.com/mattpocock/skills/blob/254f520acbddff5cbf5d1203015c553f6f0ac1ca/CLAUDE.md)
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md (revision 2026-07-14, origin https://github.com/mattpocock/skills/blob/8fcce1075ee773494f6d08ac88b82709107cb15a/README.md — the "Install as a Claude Code plugin" section; revision 2026-07-28, origin https://github.com/mattpocock/skills/blob/24a8852d50d166d354978b737c565ab2a51e5bec/README.md — the merged "Installation" section: single-command plugin install via the official marketplace, and the "For tinkerers" third path)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078096614044946565-687d88b7.md` — origin: https://x.com/mattpocockuk/status/2078096614044946565
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078234654293774540-9b392145.md` — origin: https://x.com/mattpocockuk/status/2078234654293774540
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082028549125624164-d2bef758.md` — origin: https://x.com/mattpocockuk/status/2082028549125624164
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082043744736485442-85538ba5.md` — origin: https://x.com/mattpocockuk/status/2082043744736485442
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082043793704960236-d93966f8.md` — origin: https://x.com/mattpocockuk/status/2082043793704960236
