# MCP Server Integrations

Configuration examples for common external service integrations via Model Context Protocol (MCP).

## How MCP Works

MCP servers extend Claude's capabilities by connecting to external services. Configuration goes in `.mcp.json` at the workspace root.

**Important:** API credentials go in Settings > Secrets, not in the config file. Use `${SECRET_NAME}` syntax to reference them.

---

## Composio (Multi-Service Gateway)

Best for users who need multiple integrations. Single config enables 10,000+ services.

```json
{
  "mcpServers": {
    "composio": {
      "type": "http",
      "url": "https://mcp.composio.ai",
      "headers": {
        "X-Composio-API-Key": "${COMPOSIO_API_KEY}"
      }
    }
  }
}
```

**Provides:** Gmail, Google Calendar, Slack, Notion, GitHub, Linear, Jira, Asana, Discord, and thousands more.

**Secret needed:** `COMPOSIO_API_KEY`

**Setup:**
1. Create account at composio.ai
2. Get API key from dashboard
3. Add `COMPOSIO_API_KEY` in Settings > Secrets
4. Connect individual services in Composio dashboard

---

## Email & Calendar

### Gmail + Google Calendar (via Composio)
Use Composio config above, then connect Google account in Composio dashboard.

### Outlook (via Composio)
Use Composio config above, then connect Microsoft account in Composio dashboard.

---

## Notes & Documents

### Notion (via Composio)
Use Composio config above, then connect Notion workspace in Composio dashboard.

### Google Drive (via Composio)
Use Composio config above, then connect Google account in Composio dashboard.

---

## Messaging

### Slack (via Composio)
Use Composio config above, then connect Slack workspace in Composio dashboard.

### Discord (via Composio)
Use Composio config above, then connect Discord server in Composio dashboard.

---

## Project Management

### GitHub (via Composio)
Use Composio config above, then connect GitHub account in Composio dashboard.

### Linear (via Composio)
Use Composio config above, then connect Linear workspace in Composio dashboard.

### Jira (via Composio)
Use Composio config above, then connect Jira workspace in Composio dashboard.

---

## Browser Automation

### Playwright

For web browsing, form filling, screenshots, and testing.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-playwright"]
    }
  }
}
```

**Provides:** Navigate pages, click elements, fill forms, take screenshots, extract content.

**No secret needed** - runs locally.

---

## Enhanced Web Access

### Fetch Server

For advanced HTTP requests beyond built-in WebFetch.

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-fetch"]
    }
  }
}
```

**Provides:** Custom headers, authentication, complex request patterns.

**No secret needed** - runs locally.

---

## Persistent Memory

### Memory Server

For storing facts and context across sessions.

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-memory"]
    }
  }
}
```

**Provides:** Store entities, facts, relationships; recall across conversations.

**No secret needed** - runs locally.

---

## Databases

### PostgreSQL

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-postgres"],
      "env": {
        "POSTGRES_URL": "${POSTGRES_URL}"
      }
    }
  }
}
```

**Secret needed:** `POSTGRES_URL` (connection string)

---

## Combining Multiple Servers

You can configure multiple MCP servers together:

```json
{
  "mcpServers": {
    "composio": {
      "type": "http",
      "url": "https://mcp.composio.ai",
      "headers": {
        "X-Composio-API-Key": "${COMPOSIO_API_KEY}"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-playwright"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-memory"]
    }
  }
}
```

---

## After Configuration

1. Add required secrets in Settings > Secrets
2. Restart the machine or start a new thread
3. Test the integration with a simple request
