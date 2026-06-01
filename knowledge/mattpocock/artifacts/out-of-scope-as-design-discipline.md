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

## Why this is an artifact, not just a policy

Writing refusals down — in-repo, versioned, with prior-request citations — turns
scope discipline into something an agent can read and apply. A maintainer (human or
agent) triaging a new feature request checks `.out-of-scope/` the way it checks
ADRs, and the escape hatches (`local markdown` / `other/custom` trackers; "tell the
setup skill to verify") are documented right beside the refusal, so "no" always
ships with a "here's what to do instead."

## Sources

- `sources/mattpocock/skills-repo/.out-of-scope-mainstream-issue-trackers-only.md-0903b7c1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/.out-of-scope/mainstream-issue-trackers-only.md
- `sources/mattpocock/skills-repo/.out-of-scope-question-limits.md-9a585ab5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/.out-of-scope/question-limits.md
- `sources/mattpocock/skills-repo/.out-of-scope-setup-skill-verify-mode.md-3a88b4b1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/.out-of-scope/setup-skill-verify-mode.md
- `sources/mattpocock/sandcastle/.out-of-scope-custom-base-image-abstraction.md-27495145.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/custom-base-image-abstraction.md
- `sources/mattpocock/sandcastle/.out-of-scope-provider-error-retry.md-19d09e74.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/provider-error-retry.md
- `sources/mattpocock/sandcastle/.out-of-scope-multi-repo-sandbox.md-68d2d235.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/.out-of-scope/multi-repo-sandbox.md
