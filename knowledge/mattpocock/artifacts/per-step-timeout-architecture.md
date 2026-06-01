# Per-step timeouts: bounded execution for every lifecycle operation

Sandcastle wraps every lifecycle step in individual timeouts rather than relying on a single global timeout. Container start, git operations, hooks, sync operations — each gets its own `timeoutFail` with a dedicated error type carrying step-specific context. This prevents any single operation from hanging the entire workflow indefinitely while providing precise failure diagnostics.

## Timeout boundaries align with operational boundaries

Each discrete operation that could potentially hang gets its own timeout boundary:
- Container lifecycle operations (start, stop)
- Git operations (clone, checkout, commit, format-patch)
- Hook execution (setup, cleanup)
- Sync operations (in, out)
- Agent idle time (distinguished from other steps)

This granularity means a slow network connection only affects container pulls, not the entire run. A hanging git operation fails specifically as a git timeout, not as a generic workflow timeout.

## Error types carry operational context

Rather than a generic `TimeoutError`, each step gets its own `Data.TaggedError` with relevant context. `ContainerStartTimeoutError` includes the image name and startup time. `GitOperationTimeoutError` carries the command that timed out. `AgentIdleTimeoutError` (renamed from the generic `TimeoutError`) includes the idle duration.

This specificity makes timeout failures actionable — a container start timeout suggests network or image issues, while a git operation timeout points to repository or filesystem problems. The error message includes the step-specific context needed for diagnosis.

## Defaults are internal, not user-configurable

Timeout values are baked into the framework rather than exposed as configuration knobs. Container start gets 2 minutes, git operations get 30 seconds, agent idle gets 10 minutes — these are internal implementation decisions about reasonable operational bounds, not user preferences to tune.

This follows the thin harness principle: the framework owns what it controls (reasonable timeouts for known operations) but doesn't expose configuration for decisions it can't make intelligently (how long should your specific setup wait for your specific container on your specific network?).

## Breaking boundary for idle timeout naming

The rename from `TimeoutError` to `AgentIdleTimeoutError` is a breaking change that clarifies the distinction between agent idle time and operational step timeouts. Code that caught the generic timeout now must be explicit about whether it's handling agent idle specifically or operational failures generally.

This breaking change enforces the operational boundary — agent idle timeout is semantically different from infrastructure timeout, and consumers should handle them differently (retry infrastructure, investigate agent behavior).

## Sources

- `sources/mattpocock/sandcastle/docs-adr-0001-per-step-timeouts.md-9a548708.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0001-per-step-timeouts.md