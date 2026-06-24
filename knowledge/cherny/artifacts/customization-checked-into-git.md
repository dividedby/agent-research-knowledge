# Customization is configuration — checked into git

Cherny's framing of how to *build* a team's Claude Code setup: the harness is
"built to work great out of the box" (his own setup is "surprisingly vanilla"),
and every customization you do make should be **a file checked into source
control so the team benefits too.** Customization is configuration, not
per-developer dotfiles.

What lives as committed config:

- **`settings.json`** — the central artifact. Pre-allowed/blocked commands
  (`/permissions`), env vars (the `"env"` field, to avoid wrapper scripts),
  `additionalDirectories`, marketplace registrations, spinner verbs, output styles.
  Configurable at several scopes: whole codebase, a sub-folder, just yourself, or
  **enterprise-wide policies.**
- **Slash commands** — workflows you run many times a day, checked in under
  `.claude/commands/`, shared with the team, and usable by Claude itself. They turn
  repeated prompting into a named command.
- **Custom agents** — `.md` files in `.claude/agents/`, each with a name, color,
  tool set, pre-allowed/disallowed tools, permission mode, and model; selected via
  the `"agent"` field, `--agent`, or `/agents`.
- **Skills** — created once and committed (`.claude/skills/` per-project,
  `~/.claude/skills/` global) so they reuse across every project. See
  [[skills-as-the-unit-of-reuse]].
- **Plugins & marketplaces** — install LSPs, MCPs, skills, agents, hooks from the
  Anthropic marketplace *or your company's own*; check `settings.json` in to
  auto-add the marketplaces for the team.
- **Hooks** — see [[hooks-deterministic-lifecycle-integration]].

The design principle: **configuration is the team's shared, version-controlled
substrate, not individual setup.** A customization that isn't committed only helps
one person and drifts; committing it makes the whole team's agents converge and
makes the setup reproducible. This is the build-side counterpart to
[[give-the-agent-your-whole-toolbox]] (the integrations) and
[[compounding-memory]] (CLAUDE.md, the other committed living artifact).

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
