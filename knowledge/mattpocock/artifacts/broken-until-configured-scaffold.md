# Scaffold that ships deliberately broken until an agent configures it

When `sandcastle init` can't fully wire something up itself, it does not scaffold a
plausible-looking-but-wrong default and hope the user notices. The "Custom" issue
tracker option instead scaffolds the project in a **deliberately
broken-until-configured** state, paired with a `.sandcastle/SETUP_ISSUE_TRACKER.md`
prompt the user feeds to their own coding agent — which finishes the wiring by
editing the scaffolded files in place. Init even skips building the container image
for this option (the Dockerfile is intentionally unfinished) and prints the
per-agent setup command in its next steps.

## One real enforcement point, the rest inert markers

The brokenness is concentrated, not smeared across the scaffold. Of the issue
tracker's command slots, only `LIST_TASKS_COMMAND` is a *real shell expression*:

```
echo 'No issue tracker configured — run .sandcastle/SETUP_ISSUE_TRACKER.md through your coding agent.' >&2; exit 1
```

Because Sandcastle's prompt preprocessor expands `` !`command` `` blocks and
**fails the run on a non-zero exit, surfacing stderr** (the fail-fast prompt-
expansion rule — see [[thin-fail-fast-harness]]), this single sentinel is enough to
hard-fail every run with a pointer back to the setup doc. The `VIEW_TASK_COMMAND`
and `CLOSE_TASK_COMMAND` slots are *inert text markers* (`<view command — see …>`),
never executed — they only need to be replaced. So one shell expression carries the
whole enforcement; the rest are signposts.

## Why broken-on-purpose beats a fake default

A scaffold that runs but silently lists nothing (or talks to the wrong tracker)
fails *quietly* — exactly the AFK failure mode Sandcastle designs against, where a
wrong-but-running setup burns iterations before anyone notices. Making the
unconfigured state hard-fail loudly, with the remediation path named in the error,
turns a latent misconfiguration into an immediate, self-explaining stop. The
sentinels are defined as shared constants so the registry entry and the
`SETUP_ISSUE_TRACKER.md` prompt that tells the agent what to replace stay in sync —
the agent and the enforcement point are reading the same source of truth.

This generalizes the setup-pointer instinct of [[setup-seeded-config-and-dependency-tiers]]
to scaffolding: a hard dependency that *can't* be auto-resolved is left provably
broken with a loud pointer, rather than guessed at.

## Sources

- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
- `sources/mattpocock/sandcastle/README.md.md` — origin: github.com/mattpocock/sandcastle (README.md)
- `sources/mattpocock/sandcastle/src-InitService.ts-d49955f9.md` — origin: github.com/mattpocock/sandcastle (src/InitService.ts)
