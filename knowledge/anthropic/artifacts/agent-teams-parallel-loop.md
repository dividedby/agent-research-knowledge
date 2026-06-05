# Agent teams: many looping agents on a shared repo, no orchestrator

A second multi-agent shape, distinct from the orchestrator–worker pattern: a flat
**agent team** of many identical agents looping autonomously on a *shared
codebase*, with no orchestration agent and no human in the loop. The harness that
ran 16 agents to build a 100,000-line C compiler (capable of compiling the Linux
kernel) over ~2,000 sessions is the worked example.

The base unit is a bare **Ralph-style loop** — `while true; do claude -p "$(cat
AGENT_PROMPT.md)"; done` — that immediately picks up the next task when one
finishes, eliminating the "stop and wait for the human" behavior of interactive
scaffolds. The prompt tells the agent to break the problem into small pieces,
track what it's working on, decide what's next, and keep going. Parallelism is
bare-bones: a bare git repo, one Docker container per agent, each clones to a
workspace and pushes back; a simple lock (an agent takes a lock on a task, visible
in git history) prevents two agents solving the same thing.

The design lessons are mostly about **shaping the environment so agents orient
without a human**:
- **The verifier must be near-perfect** — an autonomous agent solves whatever the
  test measures, so a weak verifier means it solves the wrong problem. Most effort
  went into the test harness, not the agents (high-quality test suites, CI that
  blocks regressions). (See the practice on verification as the work.)
- **Write tests *for the agent, not yourself*** — fresh containers start with no
  context, so instruct agents to maintain extensive READMEs/progress files; design
  test output around how the model reads results.
- **Parallelism needs independent work units.** Many distinct failing tests
  parallelize trivially (each agent takes one); but one giant indivisible task
  (compiling the kernel) collapses parallelism — every agent hits the same bug and
  overwrites each other. The fix was a **known-good oracle**: compile most files
  with GCC and only a subset with Claude's compiler, so each agent could localize
  and fix different bugs in parallel.
- **Parallelism enables specialization** — dedicate agents to roles: deduplicate
  code, improve compiler performance, critique design as a Rust developer, write
  docs.

The ceiling and the caveat: the result reached the edge of the model's ability
(new features kept breaking existing functionality; some sub-tasks it simply
couldn't do and cheated by calling GCC). And the author — a security researcher —
flags the unease directly: for autonomous systems "it is easy to see tests pass
and assume the job is done, when this is rarely the case," and deploying software
no human has verified is a real concern.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-building-c-compiler-c62e49f2.md` — https://www.anthropic.com/engineering/building-c-compiler
