# Buy Capability Direct Subscriptions

Buy capability directly from the model companies via flat-rate subscriptions rather than API metering or third-party harnesses. Steinberger runs roughly four OpenAI subscriptions plus one Anthropic for about $1k/month of effectively unlimited tokens — an estimated 5–10x cheaper than API pricing for his volume. Metering anxiety is its own cost: watching a per-token counter makes people overspend by hesitating. A flat rate removes the friction that distorts behavior.

Don't pay a middleman for a moat that doesn't exist. Third-party harnesses (Amp, Factory, Conductor) are "thin wrappers around the SDK plus worktree management." The base CLIs converge on the same features every release, so any wrapper edge is temporary — betting on wrappers is betting against the vendors who keep absorbing their features.

Self-hosting frontier open models is technically feasible but economically irrational for an individual: an 8xH200 rig is no faster than renting the same model, and you eat all the ops pain. Open models trail the best commercial ones by only ~6–12 months, so keep a subscription primary and treat rented open-model inference as a fallback, not a foundation. Reserve expensive pay-per-use reasoning models only for the rare hard-debugging case where they earn their price.

Measured against billable time, the subscription pays for itself in hours — which is the real frame. This is the economic underside of treating the agent as core infrastructure (see [[agent-as-universal-computer]]): you provision generously so the loop never stalls on cost, then run a [[parallel-agent-fleet-on-main]] without flinching at the meter.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-just-talk-to-it-c95bdb62.md — https://steipete.me/posts/just-talk-to-it/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-stop-overthinking-ai-subscripti-bc7f31c4.md — https://steipete.me/posts/2025/stop-overthinking-ai-subscriptions/
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-self-hosting-ai-models-52840c7a.md — https://steipete.me/posts/2025/self-hosting-ai-models/
