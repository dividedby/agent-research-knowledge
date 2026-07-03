# Don't make the agent guess

An agent working headless and remote — no local dev environment, no human next
to it explaining things — can still verify its own work end-to-end, if the
environment removes every point where it would otherwise have to guess or ask.
The goal isn't a smarter model; it's an environment that assumes an agent and
tells it "where the light switches are."

The scaffolding that makes this possible:

- **Idempotent bootstrap, not a one-shot script.** A setup step that reuses a
  healthy existing state, restarts a broken one, and starts fresh only if
  nothing's running — so the agent never has to diagnose "what state is this
  environment in" before it can act. Cache the result (snapshot a freshly
  provisioned sandbox and reuse it) so repeat runs are fast, and give the agent
  a matching wake-up hook to re-settle state after the environment goes idle and
  comes back.
- **Documentation discovered on demand, not loaded up front.** Many small,
  directory-scoped docs (Amp's repo carries 41) that the agent reads only when
  it touches that area, rather than one giant onboarding doc competing for
  context budget the agent may not need yet.
- **State exposed as a file, not tribal knowledge.** Write ports, health, and
  config to a machine-readable file (a generated `dev-ports.json`) that other
  scripts and agents read instead of a hardcoded `localhost:2000` — and merge
  logs from every layer (server *and* forwarded browser console output) into one
  place the agent can grep, instead of it having to know which of several
  services to check.
- **Purpose-built escape hatches around human-shaped friction.** Auth flows
  (OAuth, 2FA, passkeys) are built for humans and become a maze for an agent
  with no browser session history. A dev-only sign-in-as-user endpoint, plus a
  JSON readiness/preflight check that names exactly what's missing (secrets,
  workspace, credits, API key) instead of a generic failure, replaces "guess and
  retry" with "read the answer."

The payoff is a cheap act-check-correct loop even with nobody watching: setup,
state, and auth are all idempotent and the sandbox is disposable, so the agent
doesn't need to over-plan around mistakes it can't see coming — it tries
something, observes the result (down to taking its own screenshots as proof),
and corrects. None of these mechanisms individually teach the agent something
new; together they remove the guesswork a human would otherwise have supplied
in person.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-putting-an-agent-in-an-orb-f5be6905.md` — origin: https://ampcode.com/notes/putting-an-agent-in-an-orb
