---
name: machine-creator
description: Create and manage machine templates for This Machine. Use when creating a new machine, scaffolding machine directories, validating an existing machine template, configuring permissions or MCP servers, or designing machine personas. Supports quick scaffolding with init_machine.py, template-based creation, and interactive guided workflows.
---

# Machine Creator

Create machine templates that users can select when creating new machines in This Machine.

## Quick Start

### Scaffold a New Machine

```bash
python scripts/init_machine.py <machine-name> --path machines/
```

This creates a complete machine directory with all required files.

### Use a Template

```bash
python scripts/init_machine.py <machine-name> --path machines/ --template code-reviewer
```

Available templates: `general-purpose`, `code-reviewer`, `research-assistant`, `writing-assistant`, `data-analyst`

### Validate a Machine

```bash
python scripts/validate_machine.py machines/<machine-name>
```

## Machine Structure

Every machine requires these files in `machines/<machine-name>/`:

```
<machine-name>/
├── CLAUDE.md              # Instructions for the Claude agent
├── .claude/
│   └── settings.json      # Permission configurations
├── .mcp.json              # MCP server configurations
└── README.md              # Public documentation
```

## Creation Workflows

### 1. Quick Scaffold (Recommended for simple machines)

Run `init_machine.py` to create the directory structure, then customize the generated files.

### 2. Template-Based (Recommended for specialized machines)

Use `--template` flag to start from a pre-configured archetype:

| Template | Best For |
|----------|----------|
| `general-purpose` | Flexible, no constraints |
| `code-reviewer` | Code quality and PR reviews |
| `research-assistant` | Literature review and analysis |
| `writing-assistant` | Content creation and editing |
| `data-analyst` | Data exploration and visualization |

### 3. Guided Creation (For custom machines)

When the user wants a custom machine, gather information:

1. **Name**: Lowercase, hyphenated (e.g., `my-custom-machine`)
2. **Purpose**: What should this machine do?
3. **Capabilities**: What should it excel at?
4. **Permissions**: How much autonomy? (See references/permission-presets.md)
5. **Integrations**: What MCP servers needed? (See references/mcp-integrations.md)

Then create the machine using `init_machine.py` and customize the CLAUDE.md.

## File Guidelines

### CLAUDE.md

The agent's instructions. Include:
- Agent persona/role
- Workspace info (`/home/user/workspace`)
- Capabilities and focus areas
- Domain-specific guidance

For detailed patterns, see **references/persona-patterns.md**.

For sandbox environment details (network, preview URLs, secrets), reference `machines/anything-machine/CLAUDE.md` or copy the Environment section from the general-purpose template.

### .claude/settings.json

Permission configuration. Options:

```json
// Unrestricted (default)
{
  "permissions": {
    "allow": [],
    "deny": [],
    "defaultMode": "bypassPermissions"
  }
}
```

For detailed presets, see **references/permission-presets.md**.

### .mcp.json

MCP server integrations:

```json
{
  "mcpServers": {}
}
```

For common integrations (GitHub, databases, etc.), see **references/mcp-integrations.md**.

### README.md

Documentation for users browsing the registry:
- What the machine does
- Included capabilities
- Configuration options

## After Creation

1. **Validate**: Run `validate_machine.py` to check completeness
2. **Update registry**: Add the machine to the root README.md table
3. **Test**: Try the machine to verify it works as expected

## Naming Conventions

- Machine names: lowercase, hyphenated
- Start with a letter
- Examples: `code-reviewer`, `data-analyst`, `my-custom-machine`

## Reference Documentation

Load these files when you need detailed guidance:

- **references/persona-patterns.md** - How to write effective CLAUDE.md files
- **references/permission-presets.md** - Permission configuration options
- **references/mcp-integrations.md** - Common MCP server configurations
- **references/machine-types.md** - Guide to machine archetypes
