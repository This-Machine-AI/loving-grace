# Persona Patterns

Patterns for writing effective CLAUDE.md files that define a machine's persona and capabilities.

## Structure

Every CLAUDE.md should include these sections:

```markdown
# Machine Title

Opening statement defining the machine's role and purpose.

## Workspace
Document the workspace path and file organization.

## Capabilities / Focus Areas
Core competencies and what the machine excels at.

## Environment
Network access, preview URLs, secrets (can reference anything-machine).
```

## Opening Statement Patterns

### Role-First Pattern
Start with a clear role declaration:

```markdown
# Code Reviewer

You are a code reviewer specializing in code quality, security, and best practices.
```

### Purpose-First Pattern
Lead with the value provided:

```markdown
# Research Assistant

Help researchers produce rigorous, impactful work by providing literature analysis,
argument mapping, and writing support.
```

### Domain-Expert Pattern
Establish expertise upfront:

```markdown
# Data Analyst

You are a data analyst with expertise in statistical analysis, visualization,
and deriving actionable insights from complex datasets.
```

## Capability Section Patterns

### Grouped by Domain
Organize capabilities into logical domains:

```markdown
## Research Capabilities

### Literature Review
- Analyze papers from arXiv, journals
- Summarize key contributions
- Identify research gaps

### Technical Analysis
- Review methodology
- Evaluate statistical approaches
- Assess reproducibility
```

### Grouped by Action
Organize by what the machine does:

```markdown
## Capabilities

### Analyze
- Code quality assessment
- Security vulnerability scanning
- Performance profiling

### Generate
- Unit tests
- Documentation
- Refactoring suggestions
```

### Flat List
For simpler machines:

```markdown
## Capabilities

- Write and edit documents
- Research topics online
- Organize information
- Answer questions
```

## Tone and Style Guidance

Include guidance when the machine should communicate in a specific way:

```markdown
## Communication Style

- Be direct and concise
- Explain technical concepts clearly
- Ask clarifying questions when requirements are ambiguous
- Provide actionable recommendations
```

## Constraints and Boundaries

Define what the machine should NOT do:

```markdown
## Scope

This machine focuses on frontend development. For backend work, consider
using a different specialized machine.

## Limitations

- Does not execute code in production environments
- Requires user confirmation before destructive operations
```

## Environment Section

For sandbox environment details, reference the anything-machine rather than duplicating:

```markdown
## Environment

See [anything-machine/CLAUDE.md](../anything-machine/CLAUDE.md) for sandbox
environment details including network access, preview URLs, and secrets.
```

Or include the full environment section if the machine has unique requirements.

## Self-Reference Section

Every CLAUDE.md should include guidance so the machine understands its own identity and configuration. This is critical because users will ask machines to "update yourself" or "change your behavior," and the machine needs to know which file to edit.

```markdown
## Configuration

Your instructions and persona are defined in this file (`CLAUDE.md` at your workspace root). When a user asks you to "update yourself," "change your behavior," or "edit your instructions," this is the file to modify.

**Machine files:**
- `CLAUDE.md` - Your instructions and persona (this file)
- `.claude/settings.json` - Permission settings (what actions require approval)
- `.mcp.json` - MCP server integrations (external services and APIs)
```

This prevents confusion when the machine's workspace contains other CLAUDE.md files (e.g., in a machine registry or when working with nested projects).

## Examples from Existing Machines

### anything-machine
General-purpose, emphasizes capabilities and environment details.

### alignment-research-assistant
Domain specialist with structured focus areas, research practices, and
epistemic standards.
