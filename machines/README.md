# Machine Templates

This directory contains machine templates for This Machine. Each subdirectory is a self-contained template that gets copied to a user's workspace.

## Template Structure

Each machine template must include:

```
<machine-name>/
├── CLAUDE.md           # Required: Workspace instructions for Claude
├── .claude/
│   └── settings.json   # Required: Permission configurations
├── .mcp.json           # Required: MCP server configurations
└── README.md           # Recommended: Documentation
```

## Required Files

### CLAUDE.md

The main instructions file that Claude reads when working in the workspace. Should include:
- Environment description (workspace location, network access, etc.)
- Available tools and capabilities
- Any special instructions or context

### .claude/settings.json

Permission configurations for Claude Code:

```json
{
  "permissions": {
    "allow": [],
    "deny": []
  }
}
```

### .mcp.json

MCP (Model Context Protocol) server configurations:

```json
{
  "mcpServers": {}
}
```

## Creating a New Template

1. Create a directory with your machine name (lowercase, hyphenated)
2. Add all required files
3. Add a README.md documenting the template's purpose and capabilities
4. Update the root README.md to list your new machine
5. Submit a pull request
