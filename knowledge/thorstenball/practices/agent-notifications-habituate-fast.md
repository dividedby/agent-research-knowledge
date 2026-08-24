# Agent-event notifications habituate within days — kill the broadcast, don't tune it

Piping agent events (a task failed, a task shipped) into a shared channel
produces alert fatigue fast: attention adapts to the notification within days,
after which it's wallpaper nobody reads. Ball's team wired Amp to post into
their Slack whenever something went wrong or shipped; within a couple of days
everyone was glazing over the messages, and they disabled the feed the moment
someone mentioned it — no attempt to tune frequency or wording first.

The reason it decays faster than a typical alert: an agent can fire events far
more often than a human or a CI pipeline would, so the channel floods with
noise before the team has calibrated what's worth reading. Treat agent
notification design like any other alerting system — filter to the events a
human is actually meant to act on, not everything the agent happens to do —
rather than assuming a broadcast will stay useful once it's live.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-96-414473f3.md` — *Joy & Curiosity #96*: "I'm becoming AI-blind" — Amp's Slack notifications on agent events were disabled after a couple of days once the team stopped noticing them (origin: https://registerspill.thorstenball.com/p/joy-and-curiosity-96)
