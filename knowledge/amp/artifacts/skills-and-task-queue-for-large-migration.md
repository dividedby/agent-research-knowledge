# Skills + task queue for a large migration

A repeatable rig for driving an agent through a large, mechanical-but-entangled
codebase transformation (demonstrated migrating a 30-program COBOL mainframe app
to a stateless REST/cloud system, ~100% of code agent-written). The pattern has
four parts; none is novel alone, but together they let an agent grind a big
migration autonomously.

- **Custom skills = thin CLI wrappers over deterministic analysis.** Rather than
  ask the model to *reason* about a legacy language it barely knows, expose
  deterministic extractors as CLI commands it can call: `parse` (dense per-file
  summary), `deps` (program call graph), `detect-inputs` (find conversational
  loops needing refactor to single-shot), `env-vars`, `data-ref`. The model
  orchestrates; the tools supply ground truth.
- **A map before any edits.** A `generate` command composes those tools into a
  *semantic graph* of programs, files, and control flows — the migration surface
  made explicit. Hidden, implicit dependencies (here, shared-memory buffers
  passed between programs) are surfaced and reused deterministically to
  auto-generate the **target schema** (an OpenAPI manifest mapping each entry
  program to a REST route, converting implicit deps into explicit JSON inputs).
- **A task queue with per-task handoff.** The driving prompt is a loop: "Pop the
  front of the task queue, find the program, do the migration using these skills,
  then **hand off to a new thread for each ready task**." This keeps each unit in
  a fresh context (one program per thread) while the queue and the shared graph
  carry state across them. Issues get **annotated onto the graph**, so the
  artifact accumulates knowledge as the run proceeds.
- **Hard definition-of-done gates with real feedback loops.** Tasks may not be
  marked complete unless explicit machine-checkable conditions pass — phrased in
  caps in the prompt: `DO NOT MARK A TASK AS COMPLETE UNLESS:` the program
  compiles *and* a stdin→stdout smoke test produces expected output against real
  data files. Each agent thus gets a concrete two-step loop (compiler validity +
  behavioral smoke test) and can't declare victory on faith.

The phases mirror normal engineering, gated the same way: first migrate + verify
each unit *in isolation*, then a separate integration pass ("assemble and
validate the full application") with its own DoND gate (`full build completes
with 0 failures`, all smoke tests pass against the OpenAPI contract, annotate and
mark in-progress on failure), then build the frontend/Docker wrapper. The
lesson: large migrations that "require armies of consultants" decompose into a
graph + queue + per-task feedback loops an agent can run as a factory.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-mainframe-magic-ff27eb54.md` — origin: https://ampcode.com/notes/mainframe-magic
