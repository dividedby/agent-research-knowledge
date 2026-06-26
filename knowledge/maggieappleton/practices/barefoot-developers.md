# Barefoot developers and home-cooked software

When parts of software development get faster, cheaper, and more accessible, the
interesting effect isn't on professional developers (whose problems are
comparatively boring and well-served) — it's the rise of a new class of builder.
**Barefoot developers** (by analogy to China's 1960s barefoot doctors) are the
technically-savvy middle: teachers building elaborate Notion systems, students
making over-the-top dashboards, planners pushing spreadsheets to their limits.
They want agency over computers but never cross the "command-line wall" into the
terminal. Deeply embedded in their communities, they're perfectly placed to solve
**local, home-cooked software** problems — the long tail of needs industrial,
VC-funded software will never touch because there's no market in it.

The bottleneck has been skill: today the Venn diagram of people who *can* build
home-cooked software and people who are professional developers is essentially a
single circle. Language models change the economics by letting people describe
interfaces and functionality in natural language and get working code back
(generative-interface prototypes like V0 and Make Real demonstrate the shape).

But the sharp, transferable insight is the constraint: **language-model legos
need glue**. Models hand you disconnected pieces — interface elements, state
management, API calls, basic logic — but not how to assemble them into a deployed,
data-persisting, multi-user application. Bridging that gap still requires
professional knowledge (what a database is, how to deploy, how to add auth and
multiplayer). The glue comes in two forms: (1) **orchestrator agents** designed
to guide a non-expert through writing a technical spec and working out which
tools a piece of software needs, and (2) **tools designed to talk to those
orchestration agents** — default toolsets (databases, deployment pipelines,
collaboration infra) the agent already knows how to call. Whatever defaults get
baked into those agents and tools will silently make most of the architectural
decisions for barefoot developers, who won't know to ask for them — so the
defaults are a values choice (the talk's specific plea: make those defaults
local-first, so users keep ownership of their data and software).

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-home-cooked-software-41ab8b8c.md` — origin: https://maggieappleton.com/home-cooked-software/
