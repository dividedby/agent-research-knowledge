# Two install paths encode two philosophies: fork vs subscribe

The skill set ships through two installers that trade the same content for
opposite ownership models. **skills.sh** (`npx skills@latest add
mattpocock/skills`) copies the skill files into the target repo — editable,
"hack around with them, make them your own," the repo owns its copy from that
point on. The **Claude Code plugin** (`/plugin marketplace add
mattpocock/skills` + `/plugin install mattpocock-skills@mattpocock`) installs
the same promoted set as a managed, read-only bundle that updates in place
whenever a new version ships — "you subscribe rather than fork." Neither
path is strictly better; they serve opposite intents — customize-and-diverge
versus stay-current-and-don't-touch — and offering both means a user doesn't
have to choose ownership over currency or vice versa.

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
- `sources/mattpocock/skills-repo/README.md.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/README.md (revision 2026-07-14, origin https://github.com/mattpocock/skills/blob/8fcce1075ee773494f6d08ac88b82709107cb15a/README.md — the "Install as a Claude Code plugin" section)
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078096614044946565-687d88b7.md` — origin: https://x.com/mattpocockuk/status/2078096614044946565
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2078234654293774540-9b392145.md` — origin: https://x.com/mattpocockuk/status/2078234654293774540
