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

## Composio MCP

You have access to the **Composio MCP**, which provides integration with 100+ third-party APIs and services including GitHub, Slack, Google Drive, Notion, Linear, and more.

### How to Use

1. **Search for tools**: Use `COMPOSIO_SEARCH_TOOLS` to find available actions for a service
2. **Check connections**: Use `COMPOSIO_MANAGE_CONNECTIONS` to see which services are connected
3. **Execute actions**: Use `COMPOSIO_MULTI_EXECUTE_TOOL` to perform actions on connected services

If a service isn't connected yet, the user will need to authenticate through the Composio dashboard first
