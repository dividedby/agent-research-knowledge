# Practices — steipete

How Peter Steinberger (PSPDFKit founder; firsthand agentic-coding practitioner
since 2025, working primarily in Claude Code) approaches building and working
with coding agents: his hype-free working model for driving agents, concrete
day-to-day workflow, and how he reads streamed agent output. One concept per
file; this index lists them, one line each.

- [stay-in-the-loop-active-steering](./stay-in-the-loop-active-steering.md) — watch live and interrupt the moment a run overshoots its blast-radius estimate; visibility is the point, so reject background/async agents you can't course-correct.
- [blast-radius-sizing](./blast-radius-sizing.md) — size every task by files-touched × time; keep changes small for atomic commits and cheap resets, and let blast radius set how many agents you parallelize.
- [parallel-agent-fleet-on-main](./parallel-agent-fleet-on-main.md) — run 3–8 agents in the same folder on main, isolated by non-overlapping work selection and disciplined commits rather than worktrees.
- [work-on-main-no-ceremony](./work-on-main-no-ceremony.md) — solo speed means committing straight to main with tight atomic commits; skip PRs, trackers, worktrees, and click-through approvals (team caveat noted).
- [reroll-and-revert-over-repair](./reroll-and-revert-over-repair.md) — agents are slot machines; re-execute unchanged or revert to fresh context instead of fighting a confused run, because cheap code makes repair the wrong default.
- [just-talk-to-it-minimal-prompting](./just-talk-to-it-minimal-prompting.md) — with a capable model on a read codebase, prompts shrink to 1–2 rambling sentences; intuition built by volume beats prompt-engineering ceremony.
- [less-is-more-tooling](./less-is-more-tooling.md) — tooling around the agent is mostly a context tax working around inefficiencies the model will obsolete; bet on the raw model and the thinnest surface.
- [cli-over-mcp](./cli-over-mcp.md) — almost every MCP should have been a CLI: zero context until invoked, self-documenting via --help, composable, already known to the model.
- [images-as-high-bandwidth-context](./images-as-high-bandwidth-context.md) — a screenshot is the densest, cheapest context channel; half his prompts carry one, and a screenshot tool lets the agent self-correct.
- [voice-as-primary-input](./voice-as-primary-input.md) — dictation lowers the activation energy of interacting, letting you dump half-formed thoughts the agent makes sense of; the bottleneck is intent, not keystrokes.
- [model-dialects-and-strengths](./model-dialects-and-strengths.md) — portable prompts are a fiction; tune to each model's dialect and temperament, match model to task by trying both, otherwise keep config simple.
- [adversarial-and-cross-model-spec-refinement](./adversarial-and-cross-model-spec-refinement.md) — harden a spec with a fresh critic context and a different/stronger reviewing model; reviewing a plan is far cheaper than reviewing the code.
- [match-spec-rigor-to-uncertainty](./match-spec-rigor-to-uncertainty.md) — under-spec and iterate visually for UI/exploration; reserve heavyweight spec-driven development for high-uncertainty, high-blast features.
- [tests-in-the-warm-context](./tests-in-the-warm-context.md) — write tests right after the feature, in the same context, as a separate step; the value is surfacing bugs in just-written code, not the tests themselves.
- [refactoring-as-a-phase](./refactoring-as-a-phase.md) — agents make a mess and clean it equally well, so schedule batched refactor days (jscpd/knip) rather than chasing per-commit purity.
- [playbook-driven-migration](./playbook-driven-migration.md) — blind "convert all of this" reproduces the old idiom in new syntax; hand the agent a before/after playbook and run a tight compile-commit loop with precise scope.
- [engineer-the-codebase-for-agents](./engineer-the-codebase-for-agents.md) — design the codebase for the agent, not yourself: small files, conventional names, force-loaded docs, CLI-first, agent-friendly stacks.
- [feed-agents-current-docs-as-markdown](./feed-agents-current-docs-as-markdown.md) — convert authoritative docs to clean Markdown and hand them over rather than letting the agent reason from a stale cutoff; keep a reusable agent-rules library.
- [buy-capability-direct-subscriptions](./buy-capability-direct-subscriptions.md) — flat-rate subscriptions beat API metering and moatless third-party wrappers; self-hosting frontier models is uneconomical for an individual.
- [judgment-migrates-up](./judgment-migrates-up.md) — agent management is senior engineering; automating the typing raises the bar, relocating value to architecture and judgment — not slop, not replacement.
- [agent-as-universal-computer](./agent-as-universal-computer.md) — reframe the CLI agent as a universal computer you state intent to; pre-authorize execution (backed by snapshots) so permission prompts don't shatter flow.
- [the-agentic-slot-machine](./the-agentic-slot-machine.md) — the intermittent-reward loop that makes agents productive also makes them addictive; sustainability is a real, deliberately-managed practice concern.
