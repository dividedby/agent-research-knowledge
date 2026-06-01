# WebAssembly Compilation Workflow

Simon Willison demonstrates a complete workflow for compiling C projects to WebAssembly and building web interfaces around them, using Gifsicle optimization as a case study.

## GIF Optimization Tool Case Study

Building a web interface for Gifsicle (a 30-year-old C command-line GIF optimization tool) through WebAssembly compilation.

## Single Comprehensive Prompt Pattern

```
gif-optimizer.html

Compile gifsicle to WASM, then build a web page that lets you open or drag-drop an animated GIF onto it and it then shows you that GIF compressed using gifsicle with a number of different settings, each preview with the size and a download button

Also include controls for the gifsicle options for manual use - each preview has a "tweak these settings" link which sets those manual settings to the ones used for that preview so the user can customize them further

Run "uvx rodney --help" and use that tool to try your work - use this GIF for testing https://static.simonwillison.net/static/2026/animated-word-cloud-demo.gif
```

## Key Workflow Components

### 1. WebAssembly Compilation Strategy
- **Agent-friendly approach**: "Compile gifsicle to WASM" does substantial work - agents are fantastic at trial and error for complex WASM toolchain issues
- **Emscripten toolchain**: Complex process involving compiler errors that agents can brute-force through
- **Build artifacts**: Include build scripts, diffs, and compiled WASM bundles in commits

### 2. Web Interface Patterns
- **Drag-and-drop zones**: HTML file uploads work, but drag-drop provides better desktop UX
- **Multiple preview generation**: Show GIF compressed with different settings, each with size and download
- **Manual controls**: Provide setting sliders that can be pre-populated from preview configurations

### 3. Testing Integration
- **Browser automation**: `uvx rodney --help` provides agent-friendly testing
- **Real content testing**: Using actual GIF files to verify optimization works correctly
- **Visual validation**: Screenshots and browser inspection to confirm UI works

## Follow-up Enhancement Patterns

### Build Process Documentation
```
Include the build script and diff against original gifsicle code in the commit in an appropriate subdirectory

The build script should clone the gifsicle repo to /tmp and switch to a known commit before applying the diff - so no copy of gifsicle in the commit but all the scripts needed to build the wasm
```

### Asset Management
```
You should include the wasm bundle
```
Ensures compiled WebAssembly (233KB) is committed for GitHub Pages deployment without local builds.

### Attribution
```
Make sure the HTML page credits gifsicle and links to the repo
```
Professional courtesy for wrapping open source projects. Agent added: "Built with gifsicle by Eddie Kohler, compiled to WebAssembly. gifsicle is released under the GNU General Public License, version 2."

## Architectural Outcomes

- **Self-contained tools**: Single HTML pages with embedded JavaScript/CSS solving specific problems
- **Library integration**: Successful combination of complex C libraries with modern web interfaces
- **Deployment simplicity**: Static hosting via GitHub Pages without build requirements

This demonstrates agents' capability to handle complex compilation toolchains while building polished user interfaces.

*Sources: [GIF optimization tool using WebAssembly and Gifsicle](https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/)*