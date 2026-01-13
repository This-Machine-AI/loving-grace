# loving-grace

Official machine registry for [This Machine](https://thismachine.ai).

## What is this?

This repository contains pre-configured machine templates that can be used with This Machine. A **machine** is a Claude Code-powered agent that you can chat with, collaborate on with others, and customize for general or specific purposes.

When you create a new machine without providing your own repository, the default "everything-machine" template is automatically set up for you.

## Available Machines

| Machine | Description |
|---------|-------------|
| [everything-machine](./machines/everything-machine) | General-purpose machine with full Claude Code capabilities |

## Using a Machine Template

Machine templates are automatically applied when you create a new machine without specifying a custom repository. The template provides:

- `CLAUDE.md` - Instructions and context for Claude
- `.claude/settings.json` - Permission configurations
- `.mcp.json` - MCP server configurations

## Contributing

This repo includes a `machine-creator` skill that helps Claude create new machine templates. Just ask Claude to "create a new machine" and it will follow the correct structure.

For manual guidelines, see [machines/README.md](./machines/README.md).

## License

MIT
