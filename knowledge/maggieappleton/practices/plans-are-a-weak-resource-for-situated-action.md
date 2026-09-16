# Plans are a weak resource for situated action

A plan cannot predict the journey it's meant to guide — it can only orient the
first step, because the terrain it's planning for only becomes legible once
you're moving through it. Anthropologist Lucy Suchman's *Plans and Situated
Actions* makes the case with Thomas Gladwin's contrast of European and Chuukese
wayfinding: European navigators plot a full course in advance and revise it when
reality intrudes; Chuukese navigators set off toward an objective with no fixed
route and continuously steer from wind, current, and stars. Neither method is
superior — the point is that *everyone* ends up improvising in the moment,
whether or not they started with a plan. "Plans are best viewed as a weak
resource for ad hoc activity."

Agentic coding reproduces the European navigator's mistake, with a twist that
makes it worse: the planner and the traveller are not the same being. Because
the agent has to go on the implementation journey alone, the human is forced to
front-load *every* judgment call into a spec before the agent departs, rather
than making decisions situated, in context, as they arise — the agent has no
human there to consult when it hits the unplanned. This is why plan quality
matters more for agents than it ever did for human collaborators: the plan is
the only channel carrying human intent into territory the human won't be
present for.

Current planning interfaces make this worse, not better: a CLI plan-mode session
walks the human through dozens of multiple-choice questions, but attention
craters by around question eight and the human starts reflexively picking the
recommended option — not because it's right, but because the interface gives no
way to say "go deeper here" or "prototype this before I decide." The plan that
results isn't a distillation of real intent; it's a record of decision fatigue.
Misalignment between what the agent builds and what the human actually wanted
traces back to this upfront-only decision structure, not to sloppy prompting.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-planning-agents-1b47b34a.md` — origin: https://maggieappleton.com/planning-agents/
