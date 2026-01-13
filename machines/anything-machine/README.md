# Anything Machine

The default general-purpose machine template for This Machine.

## Description

This is the standard template applied to new machines when no custom repository is specified. It provides a fully-capable Claude Code environment with:

- Full network access
- Preview URL support for web applications
- Environment variable/secrets management
- All built-in Claude Code tools (file operations, bash, web search, etc.)

## Included Configuration

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Workspace instructions explaining the sandbox environment |
| `.claude/settings.json` | Empty permission config (no restrictions) |
| `.mcp.json` | Empty MCP server config (add your own integrations) |

## Capabilities

When using this template, Claude has access to:

- **File Operations**: Read, Write, Edit, Glob, Grep
- **Terminal**: Bash command execution
- **Web**: WebSearch, WebFetch
- **Agents**: Task delegation, TodoWrite
- **Code Intelligence**: LSP tools (go-to-definition, references, hover)
- **Documents**: PDF, DOCX, XLSX, PPTX processing (via Anthropic skills)

## Customization

This template is intentionally minimal. Users can:

1. Add MCP servers to `.mcp.json` for additional integrations
2. Update `.claude/settings.json` to configure permissions
3. Extend `CLAUDE.md` with project-specific instructions
