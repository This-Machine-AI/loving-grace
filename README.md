# loving-grace

Official machine registry for [This Machine](https://thismachine.ai).

## What is this?

This repository contains pre-configured machine templates that can be used with This Machine. A **machine** is a Claude Code-powered agent that you can chat with, collaborate on with others, and customize for general or specific purposes.

When you create a new machine without providing your own repository, the default "anything-machine" template is automatically set up for you.

## Available Machines

| Machine | Description |
|---------|-------------|
| [anything-machine](./machines/anything-machine) | General-purpose machine with full Claude Code capabilities |
| [alignment-research-assistant](./machines/alignment-research-assistant) | AI safety and alignment research assistant |
| [chaos-goblin](./machines/chaos-goblin) | Creative chaos agent for breaking out of conventional thinking patterns |
| [code-archaeologist](./machines/code-archaeologist) | Legacy codebase specialist for excavating, documenting, and understanding unfamiliar code |
| [rubber-duck-debugger](./machines/rubber-duck-debugger) | Socratic debugging partner that asks probing questions until you find the bug yourself |
| [security-sentinel](./machines/security-sentinel) | Security-focused code assistant for vulnerability detection and secure development practices |

## Using a Machine Template

Machine templates are automatically applied when you create a new machine without specifying a custom repository. The template provides:

- `CLAUDE.md` - Instructions and context for Claude
- `.claude/settings.json` - Permission configurations
- `.mcp.json` - MCP server configurations

## Contributing

This repo includes a `machine-creator` skill that helps Claude create new machine templates. Just ask Claude to "create a new machine" and it will follow the correct structure.

For manual guidelines, see [machines/README.md](./machines/README.md).

## This Machine Builds Itself

This repository is maintained using [This Machine's recurring tasks](https://thismachine.ai). The same infrastructure that powers machines is used to build, update, and improve the machine templates themselves—so contributions from both humans and machines are welcome.

## License

MIT
