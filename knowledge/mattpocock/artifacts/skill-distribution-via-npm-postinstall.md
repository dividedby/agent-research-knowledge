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
`.agent/skills` directory lets one skill set serve multiple tools that each expect
their own conventional path.

This is a sketch Matt floated ("any reason this wouldn't work?"), not yet a
shipped artifact — but the shape is the transferable idea: lean on the team's
existing package/version infrastructure to distribute agent context, treating
skills as code dependencies rather than as files to copy around.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062129440558047545-df93babd.md` — origin: https://x.com/mattpocockuk/status/2062129440558047545
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2062162143944827322-cf318feb.md` — origin: https://x.com/mattpocockuk/status/2062162143944827322
