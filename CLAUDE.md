# loving-grace

Official machine registry for [This Machine](https://thismachine.ai).

A **machine** is a Claude Code-powered agent that you can chat with, collaborate on with others, and customize for general or specific purposes.

## Repository Structure

```
machines/
└── <machine-name>/
    ├── CLAUDE.md             # Agent instructions
    ├── .claude/settings.json # Permission configurations
    ├── .mcp.json             # MCP server configurations
    └── README.md             # Public documentation
```

## Creating Machines

Use the `machine-creator` skill to create new machine templates. It handles the correct structure and guidelines.

## How Templates Are Used

When a user creates a new machine without providing their own repository:
1. This registry is cloned
2. The selected machine template is copied to the user's machine
3. Anthropic's skills are loaded for additional capabilities
