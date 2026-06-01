# Solution Hoarding and Recombination

Simon Willison advocates for "hoarding things you know how to do" - building collections of working code examples that become powerful inputs for coding agents through recombination.

## Core Philosophy

Understanding what's possible and roughly how things can be accomplished is a big part of software building skill. Key questions include both broad and obscure technical possibilities:
- Can a web page run OCR operations in JavaScript alone?
- Can an iPhone app pair with Bluetooth when not running?  
- Can we process 100GB JSON without loading everything into memory?

## Building Your Code Asset Collection

The best way to be confident in answers is having seen them illustrated by *running code*. Theoretical possibility isn't the same as having seen it done yourself.

### Willison's Collection Methods

- **Blog and TIL blog**: Notes on figured-out solutions  
- **GitHub repositories**: Over 1000 repos with small proof-of-concepts demonstrating key ideas
- **tools.simonwillison.net**: LLM-assisted HTML tools - single-page solutions to specific problems
- **simonw/research**: Larger examples where agents research problems and return working code plus written reports

## Recombination Pattern

One of Willison's favorite prompting patterns: tell agents to build something new by combining two or more existing working examples.

### Case Study: Browser OCR Tool

Combined two existing code snippets:
- **Tesseract.js**: WebAssembly OCR engine callable from JavaScript
- **PDF.js**: Mozilla library that renders PDF pages as images

Full prompt combining examples:
"Build a tool that uses PDF.js to convert PDF pages to images, then Tesseract.js to extract text"

Result: Flawless proof-of-concept that became a useful tool after just a few minutes and iterations.

## Enhanced Value with Coding Agents

Coding agents make solution hoarding even more powerful:

### Internet Access Patterns
- `curl` raw HTML from known working examples
- Search and clone repositories to `/tmp` for reference  
- Reference specific implementations: "Look at how I implemented X in repository Y"

### Documentation Integration
Agents can consult documented examples and use them to solve similar shaped projects. Once a trick is documented with working code, agents can apply it to any future matching scenario.

## Investment Principle

The effort to figure something out once pays dividends when documented somewhere with working code examples. This creates a compound effect where your agent capabilities expand with your documented solution library.

*Sources: [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)*