# `.out-of-scope/` — refusals are a first-class, versioned artifact

The skills repo keeps an `.out-of-scope/` directory: one markdown file per feature
the project has **deliberately decided not to build**, each stating the refused
request, *why* it's out of scope, the escape hatches that already cover the need,
and a "Prior requests" list citing the issue numbers that asked for it. It's the
inverse of a roadmap — a durable record of "no" so the same request doesn't get
re-litigated every time someone files it. In effect these are ADRs for
non-features ([[adrs-as-agent-memory]]): the reasoning a maintainer would
otherwise repeat in a hundred issue comments, written down once.

## The recurring reasons a feature is refused

Three captured refusals (issue-tracker breadth, a question-count cap on grilling, a
verify mode for the setup skill) rhyme on the same principles:

- **Every feature is permanent maintenance surface.** A new issue-tracker backend
  "hard-codes a CLI shape into the skills" and must keep being tested against
  `/to-prd`, `/to-issues`, `/triage` as that CLI evolves. The cost is only worth
  paying for things a meaningful fraction of users actually have — "mainstream" is
  a judgement call ("would a typical engineer recognise this and plausibly have
  chosen it?"), not a stars/age threshold.
- **Natural language is the control surface, not numeric knobs.** `/grill-me`
  refuses a hard cap on questions because grilling is intentionally open-ended —
  "some plans need three questions, some need fifty," and a fixed cap "would either
  cut off useful exploration or feel arbitrary." The steering already exists: the
  user can stop the session or tell the model to wrap up. Adding a counter
  hard-codes what conversation already handles.
- **Don't split a feature's surface across two code paths.** A `--verify` flag or a
  sibling verify skill is refused because the prompt-driven setup skill already
  does it in conversation — "run `/setup-…` and tell it to verify." A flag or
  second skill would "split the surface area of a feature that's already
  expressible through the natural-language entry point," and the two would drift as
  templates evolve.

## Refuse the symptom's real cause, not the surface

The sharpest move is diagnostic: a hard question cap "would conflate two different
failure modes" — a model asking many questions because the plan is genuinely
under-specified (working as intended) versus a model asking redundant, low-value
questions (a prompt-quality bug). "The fix for the latter belongs in the skill
prompt, not in a counter." Saying no well means naming which underlying problem a
requested knob would actually paper over, and fixing that instead.

## The same discipline, applied to a framework

Sandcastle keeps its own `.out-of-scope/`, and its refusals share the spine while
adding a framework-level principle — **don't take on what the user or the provider
owns**. It declines a Dockerfile-composition abstraction ("Control is inverted
towards the user. Sandcastle scaffolds a sensible default; the user owns the
result"), declines provider-error retry ("Sandcastle shells out to provider
CLIs — it doesn't own the API connection… Sandcastle fails fast"), and defers
multi-repo sandboxes as a substantial future refactor rather than a current
priority — each note pointing at the escape hatch that covers the need today
(edit the Dockerfile; handle retries in the provider layer; bind-mount extra repos
via `mounts`). The "why" behind these refusals is the harness design stance in
[[thin-fail-fast-harness]].

## The built-in set is curated; the public interface is where the long tail lives

A second cluster of Sandcastle refusals share one move: *don't grow a curated
built-in set on request — point at the exported seam instead.* It declines new
built-in agent providers (beyond Claude Code, Codex, Cursor, OpenCode, Copilot,
Pi), new built-in sandbox providers (beyond Docker, Podman, Vercel, Daytona,
`noSandbox`), bespoke per-feature `docker()` options (custom context, port
publishing, …), large bundled workflow templates (a "superpowers"/"freecc" pack),
and a configurable `sandcastle` namespace prefix. The shared reasoning: **every
built-in is permanent maintenance surface** — each agent CLI's stream format and
auth, each sandbox's provisioning/exec semantics, each Docker flag, each bundled
template's drift against its upstream must be tracked and tested forever, and these
spaces are effectively unbounded, so pulling the tail in-tree grows the surface
faster than it can be kept correct.

The escape hatch is the design's whole point: `AgentProvider` and `SandboxProvider`
are **public, exported interfaces** (re-exported from `src/index.ts`, alongside
`createIsolatedSandboxProvider`/`createBindMountSandboxProvider`). A built-in is not
required to use one — anyone can implement the interface in their own project, pass
it as `agent`/`sandbox`, and version it on their own cadence rather than pinned to
Sandcastle's releases. Routing an existing CLI at a different backend (Claude at
Vertex/Bedrock) is likewise env/config plumbing behind that seam, not a new factory.
For Docker's huge surface the hatch is `dockerCompose()` (the user's
`docker-compose.yml` owns container config; Sandcastle injects only the per-run
worktree mount, workdir, env) or a custom provider. The same logic refuses a
configurable namespace prefix: collision-avoidance (timestamped names) and
project isolation (per-repo `.sandcastle/`) are already handled, so the cosmetic
gain doesn't justify threading a `namespace` through every entry point. This is the
inversion-of-control stance ([[thin-fail-fast-harness]]) hardened into a triage
rule — the curated set stays small *because* the seam carries the rest.

## Only *rejected* enhancements belong here — never the already-built

The knowledge base is for refusals, and a sharp boundary protects it: a feature
closed `wontfix` because it is **already implemented** must *not* be written to
`.out-of-scope/` — recording a built feature as a rejection would poison the
dedup check with false negatives, surfacing "we said no to this" when the honest
answer is "this already exists." That close instead points to where the feature
lives. The same `wontfix` label thus splits three ways at triage: rejected
enhancement → write to `.out-of-scope/`; rejected bug → polite close, no KB entry;
already-implemented → close pointing at the existing code, no KB entry. The rule
holds for PRs exactly as for issues — a rejected enhancement *PR* is recorded so
the same request doesn't return as fresh code. And the reason written down must be
**durable, not a deferral**: "we're too busy right now" is not a rejection and
doesn't belong here.

## Why this is an artifact, not just a policy

Writing refusals down — in-repo, versioned, with prior-request citations — turns
scope discipline into something an agent can read and apply. A maintainer (human or
agent) triaging a new feature request checks `.out-of-scope/` the way it checks
ADRs, and the escape hatches (`local markdown` / `other/custom` trackers; "tell the
setup skill to verify") are documented right beside the refusal, so "no" always
ships with a "here's what to do instead."

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-triage-OUT-OF-SCOPE.md-a52875a4.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/triage/OUT-OF-SCOPE.md
- `sources/mattpocock/skills-repo/.out-of-scope-mainstream-issue-trackers-only.md-0903b7c1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/.out-of-scope/mainstream-issue-trackers-only.md
- `sources/mattpocock/skills-repo/.out-of-scope-question-limits.md-9a585ab5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/.out-of-scope/question-limits.md
- `sources/mattpocock/skills-repo/.out-of-scope-setup-skill-verify-mode.md-3a88b4b1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/.out-of-scope/setup-skill-verify-mode.md
- `sources/mattpocock/sandcastle/.out-of-scope-custom-base-image-abstraction.md-27495145.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/custom-base-image-abstraction.md
- `sources/mattpocock/sandcastle/.out-of-scope-provider-error-retry.md-19d09e74.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/provider-error-retry.md
- `sources/mattpocock/sandcastle/.out-of-scope-multi-repo-sandbox.md-68d2d235.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/multi-repo-sandbox.md
- `sources/mattpocock/sandcastle/.out-of-scope-built-in-agent-providers.md-c21076b0.md` — origin: https://github.com/mattpocock/sandcastle/blob/f1aa0809d097db0d5c674e13c9ac3374ba2a629b/.out-of-scope/built-in-agent-providers.md
- `sources/mattpocock/sandcastle/.out-of-scope-built-in-sandbox-providers.md-fa6e2a1f.md` — origin: https://github.com/mattpocock/sandcastle/blob/f1aa0809d097db0d5c674e13c9ac3374ba2a629b/.out-of-scope/built-in-sandbox-providers.md
- `sources/mattpocock/sandcastle/.out-of-scope-docker-provider-bespoke-options.md-09799f82.md` — origin: https://github.com/mattpocock/sandcastle/blob/f1aa0809d097db0d5c674e13c9ac3374ba2a629b/.out-of-scope/docker-provider-bespoke-options.md
- `sources/mattpocock/sandcastle/.out-of-scope-bundled-workflow-templates.md-6ba92b6c.md` — origin: https://github.com/mattpocock/sandcastle/blob/f1aa0809d097db0d5c674e13c9ac3374ba2a629b/.out-of-scope/bundled-workflow-templates.md
- `sources/mattpocock/sandcastle/.out-of-scope-configurable-namespace-prefix.md-0a766b11.md` — origin: https://github.com/mattpocock/sandcastle/blob/f1aa0809d097db0d5c674e13c9ac3374ba2a629b/.out-of-scope/configurable-namespace-prefix.md
