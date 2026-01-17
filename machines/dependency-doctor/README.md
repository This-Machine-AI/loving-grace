# Dependency Doctor

A specialized machine for dependency management, security vulnerability assessment, and upgrade planning.

## Description

The Dependency Doctor helps developers maintain healthy, secure, and up-to-date project dependencies. It provides expertise across multiple package managers and ecosystems, with a focus on making informed decisions rather than blindly updating everything.

## Key Capabilities

### Dependency Analysis
- Audit direct and transitive dependencies
- Identify outdated, abandoned, or unmaintained packages
- Detect version conflicts and duplicate dependencies
- Analyze dependency tree complexity

### Security & Vulnerabilities
- Scan for known CVEs and security advisories
- Assess severity and exploitability
- Prioritize remediation based on actual exposure
- Suggest patches, upgrades, or alternative packages

### Upgrade Planning
- Distinguish safe updates from breaking changes
- Create phased upgrade plans for large dependency gaps
- Research changelogs and migration guides
- Generate codemods for common migrations

### Multi-Ecosystem Support
| Ecosystem | Package Managers |
|-----------|------------------|
| JavaScript/TypeScript | npm, yarn, pnpm |
| Python | pip, poetry, pipenv, conda |
| Ruby | bundler |
| Go | go mod |
| Rust | cargo |
| JVM | maven, gradle |
| System | apt, brew, nix |

## Use Cases

- **Security audits**: Identify and remediate vulnerabilities before they become incidents
- **Upgrade planning**: Plan major framework or language version upgrades
- **Tech debt assessment**: Understand how far behind your dependencies are
- **New project setup**: Configure package management best practices from the start
- **Incident response**: Quickly assess exposure to newly disclosed CVEs

## Included Configuration

| File | Purpose |
|------|--------|
| `CLAUDE.md` | Dependency management expertise and workflows |
| `.claude/settings.json` | Unrestricted permissions for package commands |
| `.mcp.json` | Empty MCP config (add security scanning integrations) |

## Optional Secrets

For enhanced capabilities, you can configure these secrets in your machine settings:

- `GITHUB_TOKEN` - Access private repos and higher API rate limits
- `NPM_TOKEN` - Access private npm packages
- `SNYK_TOKEN` - Snyk vulnerability database integration
- `SOCKET_TOKEN` - Socket.dev supply chain analysis

## Example Interactions

**Audit a project:**
> "Audit my project's dependencies and tell me what needs attention"

**Plan an upgrade:**
> "I need to upgrade from React 17 to React 18. What's involved?"

**Security response:**
> "We got flagged for CVE-2024-XXXXX. How exposed are we and what should we do?"

**Health check:**
> "How healthy are our dependencies? What's our technical debt situation?"
