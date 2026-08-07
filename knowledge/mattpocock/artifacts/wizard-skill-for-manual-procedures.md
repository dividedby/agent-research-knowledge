# The wizard skill: automating the human's side of a manual procedure

`wizard` targets a job none of the other skills do: a **manual procedure a
human must perform** — third-party service setup, a one-off migration, an A→B
state transition — that's tedious to do by hand and equally tedious to
re-explain to an AI every time it recurs. Rather than the agent doing the work,
it generates a **bash script that walks the human through it**: opening each
URL, saying exactly what to click and copy, capturing values, writing them
where they belong, and confirming at every stage.

## The library/stages split makes every wizard consistent

The delightful part of the UX — progress counted in stages, confirmation
gates, cross-platform URL opening (including WSL), hidden secret entry,
idempotent `.env` upserts, `gh secret`/`gh variable` writes, a closing summary
— is solved once in a shared `template.sh` **library**, identical across every
generated wizard and never hand-edited. A later revision drops the library's
original time-remaining estimate (`TOTAL_MINUTES`) in favour of stage counting
(`TOTAL_STAGES`) alone — a per-step minute guess is a number the author has to
invent and gets wrong, where "step 2 of 5" is exact and costs nothing to keep
honest. The author's only job is to scope the
procedure and write the **stages** below a fixed marker, using library helpers
(`stage`, `say`/`step`, `open_url`, `ask`/`ask_secret`, `write_env`,
`set_secret`/`set_var`, `pause`/`confirm`). This is the same "fix the
mechanism once, let authors only vary content" move as the wizard-*generating*
skill's own library/stages split in `template.sh` — consistency is the point,
not an accident.

## Scope by reading the repo, not by asking cold

Before drafting stages, the skill inventories the repo for every value the
procedure will need to produce: `.env`/`.env.example`, README, docker-compose,
framework config, and every `secrets.*`/`vars.*` reference across
`.github/workflows/*` — each one is a value the wizard must eventually
capture. Only after that inventory does it show the user the ordered stage
list and confirm, rather than interviewing them from a blank slate. This
mirrors `setup-matt-pocock-skills`' explore-before-ask posture
(`explore-then-confirm-loop`) applied to a different artifact: config-scaffold
there, a runnable script here.

## Ephemeral by default, honest about the UI it doesn't know

A wizard is disposable — built for one run, saved to scratch or `scripts/`,
deleted once the job's done — and committed only if the user wants a
repeatable path. It never invents interaction it hasn't verified: where the
author doesn't actually know the current dashboard UI or exact command, the
skill says so and asks or checks docs, rather than fabricating plausible-looking
steps. Verification before handoff is static, not a live run — `bash -n`,
`shellcheck`, tracing that every captured value lands where scoping said it
would and every `set_secret` name matches a real `secrets.*` reference in
CI — because the script itself blocks on human input and opens browsers, so
the agent can't safely execute it end-to-end.

## Graduated to model-invoked: the agent reaches for it unprompted

`wizard` shipped twice over in the same release: out of `in-progress/` into
`engineering/`, and from user-invoked to model-invoked (the axis is
`invocation-axis-user-vs-model`). Model-invocation only adds reach — typing
`/wizard` still works exactly as before — but it retires a specific failure
mode: the agent hitting a credentials wall mid-build and dumping six numbered
steps into the chat, where they scroll away, instead of building the human a
script that holds the state for them.

## The security boundary is who executes, not who authors

Because the agent writes the script but a human runs it, secrets never pass
through the model's context by construction — hidden terminal entry captures
each value straight into `.env`/`gh secret` on the human's own machine. The one
gap this doesn't close: a key pasted into chat while scoping the procedure is
ordinary text, in context like anything else pasted there. And because a
wizard runs its stages forward-only with no back button, cheap re-running is
the recovery path for a wrong entry, not correction: every value already
captured is offered back as the default on Ctrl-C-and-rerun, so fixing one
mistake costs pressing Enter through the stages already right, not restarting
the whole procedure — the payoff the idempotent `.env` upserts above are
actually for.

## Sources

- `sources/mattpocock/skills-repo/skills-in-progress-wizard-SKILL.md-e3abd6f3.md` — origin: https://github.com/mattpocock/skills/blob/801dca688564c529fa84f247f64472520d9ebe28/skills/in-progress/wizard/SKILL.md
- `sources/mattpocock/skills-repo/skills-in-progress-wizard-template.sh-6dda7f17.md` — origin: https://github.com/mattpocock/skills/blob/801dca688564c529fa84f247f64472520d9ebe28/skills/in-progress/wizard/template.sh
- `sources/mattpocock/skills-repo/skills-in-progress-README.md-7e74a106.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/in-progress/README.md (revision 2026-06-30)
- `sources/mattpocock/skills-repo/skills-engineering-wizard-template.sh-f562dbf5.md` — origin: https://github.com/mattpocock/skills/blob/c0fd1e973e040347d424e09934099f1bd6c2dee0/skills/engineering/wizard/template.sh (revision 2026-08-07 — `TOTAL_MINUTES`/time-remaining dropped for stage counting)
- `sources/mattpocock/skills-repo/CHANGELOG.md.md` — origin: https://github.com/mattpocock/skills/blob/c0fd1e973e040347d424e09934099f1bd6c2dee0/CHANGELOG.md (revision 2026-08-07, PR #783)
- `sources/mattpocock/aihero/https-www.aihero.dev-skills-wizard-bfb2761c.md` — origin: https://www.aihero.dev/skills-wizard
