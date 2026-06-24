# Give the agent your whole toolbox

A consistent Cherny stance: Claude Code is most useful when it can autonomously
reach *every* tool you use — databases, dashboards, chat, the browser — through
whatever interface they already expose. The point is not any single integration
but the disposition: **don't keep the agent walled off from your real working
environment.**

How it shows up:

- **Any data source with a CLI, MCP, or API is fair game.** The team checks a
  BigQuery skill into the codebase and everyone queries metrics on the fly ("ask
  Claude to use the `bq` CLI to pull and analyze metrics"). The rule generalizes:
  *any* database/service that has a CLI, MCP, or API can be driven the same way. A
  dedicated read-only "analysis" worktree is kept for exactly this.
- **Chat as an inbox.** Enable the Slack MCP and paste a bug thread with just
  "fix" — zero context switching. iMessage becomes a channel too; you text Claude
  like a friend from any Apple device.
- **The browser as a verifier.** The Chrome/Chromium extension lets Claude open a
  browser, test UI changes, and iterate (this is also the frontend half of
  [[verification-is-the-number-one-tip]]).
- **Voice and mobile.** Cherny does most of his coding by *speaking* to Claude
  (`/voice`, hold space); he writes a lot of code from the iOS app.
- **Cross-repo reach.** `--add-dir` (or `additionalDirectories` in settings) lets
  Claude see *and* get permissions on other repos when work spans repositories.

The principle: **an agent's capability is bounded by what it can reach.** The same
logic as the "browser" metaphor in verification — an engineer denied tools
produces worse work — applied to the whole toolbox. Pairs with the configuration
discipline in [[customization-checked-into-git]] (these integrations are shared
via committed settings/skills, not set up per-person).

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
