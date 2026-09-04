# Distributing skills as a versioned npm package

For a JS/TS team that already lives in npm, Matt's proposed distribution
mechanism for shared skills reuses the package manager rather than inventing a
sync tool: **ship the skills as an npm package, and on `postinstall` run a script
that symlinks them into `.claude/skills`.** Installing the package is installing
the skills; `package.json` pins which version of the skill set a repo runs.

The appeal is that it inherits npm's existing affordances for free — semantic
versioning, lockfile reproducibility, a registry, an upgrade path — instead of a
bespoke distribution channel. Skills become a normal dependency: a team publishes
its conventions once and every consuming repo picks them up at a pinned version.

The symlink (rather than a copy) keeps the installed skills pointing back at the
package, so an upgrade is a reinstall, not a manual re-vendor. The same symlink
trick generalizes across agent harnesses: pointing `.claude/skills` at a shared
`.agents/skills` directory lets one skill set serve multiple tools that each expect
their own conventional path. In practice Matt treats `.agents/skills` as the
canonical home — most harnesses already read from it, and the few with a bespoke
layout get a symlink pointed back at it, so one authored skill set serves every
tool without duplication.

This is a sketch Matt floated ("any reason this wouldn't work?"), not yet a
shipped artifact — but the shape is the transferable idea: lean on the team's
existing package/version infrastructure to distribute agent context, treating
skills as code dependencies rather than as files to copy around.

The multi-harness symlink half of the sketch has since shipped, just via a
plainer mechanism: the skills repo itself ships `scripts/link-skills.sh`,
which (re)links every skill into both `~/.claude/skills` and `~/.agents/skills`
from a single git clone — no npm package, no registry, just `git pull` plus a
re-run of the script after adding, removing, or renaming a skill. It confirms
the same core bet (one authored set, symlinked into every harness's expected
path) without needing the npm-specific machinery this sketch proposed.

The script later stopped linking every skill unconditionally: it now excludes
`deprecated/` and `misc/`, the two buckets that are neither promoted (see
`buckets-and-promotion-discipline`) nor useful to have live-installed locally.
The distinction the script draws isn't the same one the publication invariant
draws — `in-progress/` is unpromoted but still gets linked, because a local
symlink install is how Matt tries a beta skill himself, while `misc/` and
`deprecated/` skills are ones he's already decided not to reach for. Local
linking follows "would I actually invoke this," not "is this advertised."

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062129440558047545-df93babd.md` — origin: https://x.com/mattpocockuk/status/2062129440558047545
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062162143944827322-cf318feb.md` — origin: https://x.com/mattpocockuk/status/2062162143944827322
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2071159019058647144-771bdb97.md` — origin: https://x.com/mattpocockuk/status/2071159019058647144
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/31a854fc1d37464d373218be58588ea8691a01c3/CLAUDE.md (revision 2026-06-17, `scripts/link-skills.sh`)
- `sources/mattpocock/skills-repo/AGENTS.md.md` — origin: https://github.com/mattpocock/skills/blob/728a8b63e9c91bf16483cde6a5060463b831f334/AGENTS.md (revision 2026-09-04 — `link-skills.sh` excludes `deprecated/` and `misc/`)
- `sources/mattpocock/skills-repo/CLAUDE.md.md` — origin: https://github.com/mattpocock/skills/blob/728a8b63e9c91bf16483cde6a5060463b831f334/CLAUDE.md (revision 2026-09-04, same change)
