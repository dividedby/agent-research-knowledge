# Packaging MCP servers as one-click Desktop Extensions

Local MCP servers unlock real capability (local apps, private data, dev tools, all
on-machine) but their installation friction — install a runtime, hand-edit a JSON
config, restart, debug dependency conflicts — kept them inaccessible to
non-developers. Desktop Extensions (`.mcpb` files, formerly `.dxt`) remove that
friction by bundling **an entire MCP server plus all its dependencies** into a
single installable zip the user drags into the app.

The artifact is a zip whose only required file is a **`manifest.json`**: it
declares metadata (name, version, author), the server config (type `node`/
`python`/`binary`, entry point, launch command/args), the tools and prompts the
server exposes, runtime/platform compatibility, and — the part that does the heavy
lifting — **`user_config`**. The manifest can declare configuration the host must
collect from the user (API keys, allowed directories, numeric limits with
min/max/defaults); the host blocks enabling the extension until required values are
supplied, stores sensitive ones in the OS secret vault, and substitutes them at
launch via **template literals** like `${user_config.api_key}`, `${__dirname}`
(the unpacked extension dir), and system vars like `${HOME}`/`${TEMP}`. The same
mechanism handles platform-specific overrides (`win32`/`darwin` command and env
differences).

The toolchain is `npx @anthropic-ai/mcpb` — `init` interactively generates a
manifest from an existing server, `pack` bundles everything into the `.mcpb`
archive. The spec, toolchain, and schemas are open-sourced (versioned 0.1,
deliberately, to evolve with the community) so the format can serve other AI
desktop apps, not just Claude — the same portability bet as MCP itself.

Two notes that connect to broader practice. Anthropic found Claude itself is good
at *building* these extensions with minimal intervention, given a prompt that
points it at the README/MANIFEST specs and examples and asks for defensive,
production-ready code — an instance of the "give the agent the docs, let it build
the artifact" pattern. And extensions are a new security surface for enterprises,
handled with directory curation and managed-deployment controls.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-desktop-extensions-e9c7e2b1.md` — https://www.anthropic.com/engineering/desktop-extensions
