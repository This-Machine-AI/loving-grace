---
name: self-update
description: Update your own configuration, instructions, and integrations. Use when asked to "update yourself", "change your behavior", "modify your instructions", adjust permissions, or add/remove MCP integrations.
---

# Self-Update

Modify your own machine configuration within your sandbox.

## Your Machine Files

These files at `/home/user/workspace` define who you are:

| File | Purpose |
|------|--------|
| `CLAUDE.md` | Your instructions, persona, and capabilities |
| `.claude/settings.json` | Permission settings (what requires approval) |
| `.mcp.json` | MCP server integrations (external services) |

When a user asks you to "update yourself," "change your behavior," or "modify your instructions," edit these files.

## Updating Instructions (CLAUDE.md)

Your CLAUDE.md defines your persona and capabilities. Common modifications:

### Change Your Persona
Edit the opening section to adjust your role:
```markdown
# My Machine Name

You are a [role description] specializing in [domain].
```

### Add/Remove Capabilities
Update capability sections to reflect what you can do:
```markdown
## Capabilities

- Capability one
- Capability two
```

### Adjust Communication Style
Add style guidance:
```markdown
## Communication Style

- Be concise and direct
- Use technical terminology when appropriate
- Always explain your reasoning
```

### Add Domain Expertise
Include domain-specific sections:
```markdown
## Domain Knowledge

### Topic Area
- Key concept one
- Key concept two
```

## Updating Permissions (.claude/settings.json)

Control what operations require user approval.

### Unrestricted (Default)
Full autonomy - no approvals needed:
```json
{
  "permissions": {
    "allow": [],
    "deny": [],
    "defaultMode": "bypassPermissions"
  }
}
```

### Standard
Requires approval for file edits:
```json
{
  "permissions": {
    "allow": [],
    "deny": [],
    "defaultMode": "allowEdits"
  }
}
```

### Minimal (Read-Only)
Only allow specific operations:
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "WebSearch",
      "WebFetch"
    ],
    "deny": [
      "Bash",
      "Write",
      "Edit"
    ]
  }
}
```

### Available Tools
Tools that can be allowed/denied: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash`, `WebSearch`, `WebFetch`, `Task`, `TodoWrite`, `LSP`

### Pattern Matching
Use patterns for fine-grained control:
```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(npm *)"
    ]
  }
}
```

## Updating Integrations (.mcp.json)

Add MCP servers to extend your capabilities.

### Empty (Default)
No additional integrations:
```json
{
  "mcpServers": {}
}
```

### GitHub Integration
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### Database Integration (PostgreSQL)
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${DATABASE_URL}"
      }
    }
  }
}
```

### Memory / Persistent Context
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### Web Search (Brave)
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

**Note:** Use `${VAR_NAME}` to reference secrets. Users add secrets via Settings > Secrets tab.

## Important Notes

1. **Changes take effect next thread** - Modifications to CLAUDE.md apply when a new conversation starts
2. **Validate JSON** - Always ensure settings.json and .mcp.json are valid JSON before saving
3. **Preserve structure** - Keep the Configuration section in CLAUDE.md so you can always find yourself
4. **Test incrementally** - Make small changes and verify they work as expected
