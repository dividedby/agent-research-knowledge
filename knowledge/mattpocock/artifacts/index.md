# Artifacts — mattpocock

How Matt Pocock's skills/agents are built: structure, conventions, and how the
pieces compose. One concept per file; this index lists them, one line each.

- [skill-anatomy-and-progressive-disclosure](./skill-anatomy-and-progressive-disclosure.md) — a skill is a directory of tiered context: routing description → short body → linked resources, loaded only when needed.
- [buckets-and-promotion-discipline](./buckets-and-promotion-discipline.md) — six lifecycle buckets where the folder mechanically decides whether a skill is advertised in README + plugin.json.
- [setup-seeded-config-and-dependency-tiers](./setup-seeded-config-and-dependency-tiers.md) — a setup skill seeds per-repo config; skills declare hard vs soft dependence on it (ADR 0001).
- [skills-compose-by-handoff](./skills-compose-by-handoff.md) — small skills invoke, hand off to, and share data (the issue tracker) rather than forming one monolith.
- [manual-invocation-control](./manual-invocation-control.md) — `disable-model-invocation` and the description's "Use when" clause govern whether the model may auto-fire a skill.
- [enforced-architecture-vocabulary](./enforced-architecture-vocabulary.md) — a fixed module/interface/depth/seam vocabulary with forbidden substitutes and operational tests (deletion test, etc.).
- [explore-then-confirm-loop](./explore-then-confirm-loop.md) — stateful skills share an explore → present → confirm → write skeleton that defers irreversible writes behind a human checkpoint.
- [out-of-scope-as-design-discipline](./out-of-scope-as-design-discipline.md) — `.out-of-scope/` records deliberate non-features (ADRs for "no"): refuse maintenance surface, prefer natural-language steering over knobs, fix the symptom's real cause.
- [label-driven-agent-ci-pipeline](./label-driven-agent-ci-pipeline.md) — GitHub labels are the state machine; `agent-*.yml` workflows transition/refuse/block, chain phases by label (PAT, not GITHUB_TOKEN), and push-with-lease.
- [structured-output-with-session-retry](./structured-output-with-session-retry.md) — agent↔pipeline seam is one validated `<output>` block; separate work from report, and resume the same session to re-emit on extraction failure without redoing work.
- [sandcastle-plan-execute-merge-loop](./sandcastle-plan-execute-merge-loop.md) — the batch AFK factory: bounded loop of plan → bounded-parallel implement+review in per-branch Docker sandboxes → one merge agent.
- [thin-fail-fast-harness](./thin-fail-fast-harness.md) — a harness owns only what it controls: invert control to the user, refuse to wrap provider interfaces, fail fast over degrade, keep the retry loop in the consumer.
- [triage-state-machine](./triage-state-machine.md) — issue workflow as explicit state machine with category/state role labels, grilling as state refinement, and refusal with explanation for safety.
- [stateful-teaching-workspace](./stateful-teaching-workspace.md) — file-backed learning workspace with mission grounding, progressive glossary building, and zone-of-proximal-development calculation from learning records.
- [production-automation-workflows](./production-automation-workflows.md) — production deployment through third-party service integration chains that coordinate file sync, webhooks, and content scheduling.
- [completion-signal-and-hanging-process-handling](./completion-signal-and-hanging-process-handling.md) — two-phase timeout strategy differentiating stuck agents from completed work with hanging subprocesses; completion signal switches from idle timeout (failure) to grace timeout (success with warning).
- [per-step-timeout-architecture](./per-step-timeout-architecture.md) — individual timeouts for every lifecycle step (container, git, hooks) with dedicated error types carrying operational context, preventing any single operation from hanging the workflow.
- [filesystem-backed-session-requirement](./filesystem-backed-session-requirement.md) — resumable sessions only supported for agents storing conversation state as discrete files, not databases; prioritizes opaque file transfer over schema coupling.
- [isolated-sandbox-sync-tracking](./isolated-sandbox-sync-tracking.md) — sandbox-owned refs track patch base for git format-patch/am cycles, solving SHA rewrite coordination between sandbox and host without exposing infrastructure refs to user.
- [context-compression-and-handoff-mechanics](./context-compression-and-handoff-mechanics.md) — split concerns across independent agent sessions through context compression; enables focused work without losing critical information while addressing smart zone limitations.
- [ralph-loop-implementation-patterns](./ralph-loop-implementation-patterns.md) — autonomous agent execution through simple bash loop patterns; adapts for different task sources and output formats while maintaining fresh context windows.
- [skill-distribution-via-npm-postinstall](./skill-distribution-via-npm-postinstall.md) — ship shared skills as a versioned npm package whose postinstall symlinks them into `.claude/skills`, reusing npm's versioning instead of a bespoke sync tool.
