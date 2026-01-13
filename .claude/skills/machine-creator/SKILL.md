---
name: machine-creator
description: Create new machine templates for This Machine. Use when adding a new machine to the registry, creating a machine template, or when asked to "create a machine" or "add a new machine".
---

# Machine Creator

Create machine templates that users can select when creating new machines in This Machine.

## Machine Structure

Each machine requires these files in `machines/<machine-name>/`:

```
<machine-name>/
├── CLAUDE.md              # Instructions for the Claude agent
├── .claude/
│   └── settings.json      # Permission configurations
├── .mcp.json              # MCP server configurations
└── README.md              # Public documentation
```

## Creating a Machine

### 1. Create the directory

```bash
mkdir -p machines/<machine-name>/.claude
```

### 2. Create CLAUDE.md

The agent's instructions. Include:
- Agent persona/role
- Workspace info (`/home/user/workspace`)
- Available tools and capabilities
- Domain-specific guidance

Use `machines/anything-machine/CLAUDE.md` as reference for sandbox environment details (network, preview URLs, secrets).

### 3. Create .claude/settings.json

```json
{
  "permissions": {
    "allow": [],
    "deny": []
  }
}
```

Add specific permissions as needed for the machine's purpose.

### 4. Create .mcp.json

```json
{
  "mcpServers": {}
}
```

Add MCP servers for integrations (GitHub, databases, APIs, etc.).

### 5. Create README.md

Document for users browsing the registry:
- What the machine does
- Included capabilities
- Configuration options

### 6. Update root README.md

Add the new machine to the "Available Machines" table.

## Example: Research Assistant

```bash
# Structure
machines/research-assistant/
├── CLAUDE.md           # "You are a research assistant..."
├── .claude/settings.json
├── .mcp.json           # Could include web search MCP
└── README.md
```

## Guidelines

- Machine names: lowercase, hyphenated (e.g., `code-reviewer`, `data-analyst`)
- Keep CLAUDE.md focused on the agent's purpose
- Only add permissions/MCP servers the machine actually needs
- Reference `anything-machine` for general sandbox environment details rather than duplicating
