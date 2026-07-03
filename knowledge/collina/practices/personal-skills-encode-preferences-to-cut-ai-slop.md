# Repeated corrections are a signal to externalize preferences into a skill

When you find yourself repeatedly correcting the same AI mistakes, that's a
signal to externalize your preferences into a reusable reference the agent
can load — rather than re-explaining them in every session. Repeated
correction means the knowledge is durable (years of hard-won patterns,
tools, and gotchas), but the agent has no memory of it across sessions;
writing it once as a loadable skill turns "the same argument every session"
into "read once, apply always."

Matteo Collina built his own skills collection for exactly this reason,
naming the underlying frustration directly: *slop* — AI output that
technically works but doesn't match the standards a specific, experienced
maintainer expects — and the volume of corrections that costs. The skills
are grouped by domain and each draws on specific hard-earned experience
rather than generic advice (Fastify hooks/plugin conventions from years on
Fastify core, Node.js event-loop and test-runner patterns, advanced
TypeScript generics, git/GitHub workflows via the `gh` CLI, documentation
structured around the Diátaxis framework). The format follows the open
Agent Skills standard's progressive disclosure: an agent loads a skill's
metadata first, and only pulls in the full instructions when the task
actually calls for that domain — which is what keeps a growing pile of
accumulated preferences cheap for the agent to carry instead of bloating
every prompt.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-my-personal-skills-for-ad4f27d2.md` — origin: https://adventures.nodeland.dev/archive/my-personal-skills-for-ai-assisted-nodejs/
