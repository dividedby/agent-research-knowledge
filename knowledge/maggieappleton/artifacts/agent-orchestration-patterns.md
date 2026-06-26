# Agent-orchestration patterns sketched by Gas Town

Steve Yegge's Gas Town — a chaotic, vibe-designed orchestrator running dozens of
coding agents — is read here as *speculative design fiction*: not a tool to use
(it isn't), but a provocation that "sketches out the shape of constraints we'll
face as agentic coding systems mature." Stripped of the zoomorphic naming, four
underlying patterns fall out that future orchestration systems will likely adopt.

**Specialised roles with hierarchical supervision.** Every agent has a permanent,
specialised role it knows on spin-up. A single concierge agent (the "Mayor") is
the human's only interface — it never writes code; it breaks work into tasks and
assigns them to ephemeral grunt workers, while supervisor agents nudge stuck or
idle workers along. Single-job agents can be prompted more precisely, scoped to
touch less, and run in parallel without colliding. The hierarchy solves a
coordination *and* attention problem: one interface means the human stops tab-
switching between dozens of agents to track who's stuck, idle, or blocked. The
obvious extension is diversifying the cast beyond generalist coders into on-demand
specialists (dev-ops, PM, front-end debugger, accessibility checker, docs writer).

**Roles and tasks persist; sessions are ephemeral.** The hard limit on current
coding agents is context — context rot degrades output before the window even
fills. The pattern: make each session disposable by design, and store the durable
state (agent identities + assigned work) *outside* the agent, in Git. Sessions
get liberally killed and respawned; a fresh session is told its identity and
current task and continues. State lives in tiny trackable units of work — issues,
stored as JSON in Git alongside the code, each with an id, description, status,
and assignee (agent identities are stored the same way, giving each worker a
persistent address that survives crashes). This is the same approach Anthropic
described for long-running-agent harnesses — tracking atomic tasks in structured
storage *outside* agent memory — and is expected to land in mainstream tools.

**Continuous streams of work.** Each worker has a queue and a pointer to its
current task; finishing one pulls the next to the front, and the orchestrator
keeps the queues full by decomposing high-level human orders into atomic tasks.
The catch is real: current models are trained as polite assistants that *wait*
for instructions, not workers that independently pull from a queue. Gas Town's
band-aid is aggressive prompting and a heartbeat of supervisor "nudges" that jolt
quiet agents back to their queue — a sign that reliable on-task autonomy is an
unsolved problem, not a configuration detail.

**Merge queues and agent-managed conflicts.** Parallel agents on separate
branches guarantee conflicts, worse the later an agent finishes. A dedicated merge
agent works the queue one change at a time, resolving conflicts and — when so much
has changed the original work no longer makes sense — creatively *re-implementing*
the change to fit the new codebase, or escalating to a human. A complementary
structural fix Gas Town lacks: ditch chunky PRs for **stacked diffs** — small,
atomic, individually-reviewed changes that rebase automatically when an earlier
change updates. This fits how agents already work (tiny focused changes), and
continuous high-volume agent merges need interfaces purpose-built for it.

A meta-note from the same source: generative models are still bad at *illustrative
diagrams* — cluttered, wrong-direction arrows, missing key information — so
auto-generated architecture diagrams of a system like this actively mislead.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-gastown-31a465e3.md` — origin: https://maggieappleton.com/gastown/
