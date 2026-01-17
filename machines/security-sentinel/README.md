# Security Sentinel

A security-focused code assistant that helps developers build more secure software through vulnerability detection, secure development guidance, and security best practices.

## What It Does

Security Sentinel specializes in:

- **Security Code Reviews** - Identifies vulnerabilities based on OWASP Top 10, language-specific security issues, and API security flaws
- **Secure Development Guidance** - Provides secure coding patterns, authentication/authorization best practices, and cryptography recommendations
- **Threat Modeling** - Helps with STRIDE analysis, attack trees, and risk prioritization
- **Dependency Security** - Analyzes dependencies for known vulnerabilities and provides remediation guidance
- **Security Education** - Explains vulnerabilities clearly so developers understand not just what to fix, but why

## Key Features

### Vulnerability Detection

- OWASP Top 10 coverage (injection, XSS, authentication flaws, etc.)
- Language-specific vulnerability patterns (Python, JavaScript, Java, Go, Rust, C/C++)
- API security issues (broken authentication, IDOR, rate limiting)
- Configuration and infrastructure security

### Pragmatic Security

Security Sentinel prioritizes by real-world exploitability and impact, not theoretical purity. It:

- Considers actual threat models and attack surfaces
- Balances security with developer experience
- Provides actionable fixes with code examples
- Explains the "why" behind security recommendations

### Ethical Boundaries

Security Sentinel helps with authorized security testing and defensive security. It:

- Explains how attacks work to aid defense
- Helps fix vulnerabilities in code you own
- Refuses to create malware or attack systems you don't own
- Follows responsible disclosure principles

## Example Use Cases

- "Review this authentication code for security issues"
- "Is this SQL query vulnerable to injection?"
- "How do I securely store passwords in Python?"
- "Explain the security implications of this JWT implementation"
- "Help me create a threat model for this API"
- "What's the severity of this vulnerability and how do I fix it?"
- "Audit my package.json for vulnerable dependencies"

## Configuration

The machine comes with unrestricted permissions by default, allowing it to freely analyze code and generate security recommendations.

### Useful Environment Variables

- `SNYK_TOKEN` - For enhanced vulnerability scanning
- `GITHUB_TOKEN` - For accessing private repositories and security advisories
- `NVD_API_KEY` - For National Vulnerability Database queries

## Files

- `CLAUDE.md` - Agent instructions and persona
- `.claude/settings.json` - Permission settings
- `.mcp.json` - MCP server integrations
