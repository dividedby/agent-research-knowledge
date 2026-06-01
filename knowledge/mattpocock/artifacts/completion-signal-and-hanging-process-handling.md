# Completion signal detection with hanging process recovery

Sandcastle employs a two-phase timeout strategy that differentiates between an agent that hasn't started and an agent that has signaled completion but whose process won't exit. The **completion signal** (`<promise>COMPLETE</promise>` by default) marks when all actionable work is done, but subprocesses the agent spawned (like `gh` calls or MCP servers) may inherit stdout and prevent clean exit. Rather than discarding work, the framework switches from an **idle timeout** that fails on expiry to a **completion timeout** that succeeds with a warning.

## Two-phase timeout architecture

The orchestrator scans every line of agent output for any configured completion signal. Once detected, the timeout switches contexts:

- **Pre-signal (idle phase)**: `AgentIdleTimeoutError` on expiry after no output for `idleTimeoutSeconds` (default 10 minutes). This is a failure — the agent is genuinely stuck.
- **Post-signal (completion phase)**: Successful resolution with a hanging-process warning after no output for `completionTimeoutSeconds` (default 60 seconds). The work is complete; only cleanup is lingering.

The completion timeout resets on every subsequent output line, so trailing data (token usage, terminal events, structured output tags) is still captured without extending the grace window indefinitely.

## Signal detection over terminal events

Rather than key on provider-specific terminal stream events (which vary between Claude Code's single `result`, Codex's many synthesized events, and OpenCode's different patterns), Sandcastle scans the accumulated text output directly. The signal is provider-agnostic and works with any completion marker the workflow chooses — or multiple signals for different completion conditions.

The signal match uses simple string containment (`accumulatedOutput.includes(signal)`) against the buffer of all text and result output seen so far, making the detection robust to agents that self-correct or emit the signal multiple times.

## Hanging process vs stuck agent distinction

A **hanging process** has completed work but won't exit due to inherited file descriptors from spawned children. This is distinguished from a **stuck agent** that produces no output mid-work. The completion timeout only activates after the signal is observed — processes that hang before emitting any completion marker still ride the full idle timeout and fail as genuine stuck states.

This preserves the fail-fast behavior for truly broken agents while recovering successfully from the common case where work is done but cleanup is stalled by subprocess inheritance patterns outside the agent's direct control.

## Implementation consequences

Force-completing abandons the hanging process in place. Container-based providers kill it during teardown (`docker rm -f`), but the no-sandbox provider has no explicit process cleanup, creating a potential leak for abandoned agents and their children on the host. The framework trades this operational risk for the ability to recover completed work rather than discarding it.

## Sources

- `sources/mattpocock/sandcastle/docs-adr-0019-completion-timeout-for-hanging-process.md-e5c97644.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0019-completion-timeout-for-hanging-process.md
- `sources/mattpocock/sandcastle/src-Orchestrator.ts-686b2711.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/src/Orchestrator.ts