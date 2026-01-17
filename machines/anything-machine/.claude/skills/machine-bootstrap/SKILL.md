---
name: machine-bootstrap
description: Bootstrap and configure Claude machines for any use case through guided conversation. Use when users want to set up a new machine, customize personality and communication style, configure external integrations (MCP servers), enable skills, set permission modes, or optimize their Claude for specific workflows. Triggers on "help me set up this machine", "configure my machine", "bootstrap", "customize how you work", "add integrations", "set up MCP servers", "personalize this machine".
---

# Machine Bootstrap

Guide users through configuring their Claude machine for any use case. This skill gathers requirements, researches prior art from popular GitHub repos, and generates configuration by adapting proven patterns.

## Workflow

### Phase 1: Understand Intent

Use AskUserQuestion to understand the user's goals. Ask one question at a time.

**Question 1: Primary Purpose**
```
What will you primarily use this machine for?
- Personal assistant (organization, planning, daily tasks)
- Learning & education (tutoring, study help, skill development)
- Creative projects (writing, art direction, brainstorming, content)
- Work tasks (research, analysis, reports, communication)
- Something else (describe)
```

**Question 2: Communication Style**
```
How should I communicate with you?
- Professional & precise (formal, thorough, structured)
- Friendly & casual (conversational, approachable)
- Brief & direct (concise, to the point)
- Detailed & explanatory (comprehensive, educational)
```

**Question 3: Working Approach**
```
How should I handle tasks?
- Ask before acting (confirm approach, seek clarification)
- Work autonomously (make reasonable assumptions, complete end-to-end)
- Plan first (create plans for approval before executing)
```

**Question 4: External Services**
```
Do you want to connect external services? (can skip)
- Email & Calendar (Gmail, Outlook, Google Calendar)
- Notes & Docs (Notion, Obsidian, Google Drive)
- Messaging (Slack, Discord)
- Project management (Linear, Jira, GitHub)
- Browser automation (web research, form filling)
- None right now
```

### Phase 2: Research Prior Art

After gathering requirements, actively search for and analyze existing Claude configurations that match the user's needs.

**Step 1: Search GitHub for relevant CLAUDE.md files**

Use WebSearch to find configurations matching the use case:

```
WebSearch("CLAUDE.md site:github.com [use-case keywords]")
```

Example searches based on purpose:
- Personal assistant: `"CLAUDE.md" site:github.com assistant productivity`
- Learning: `"CLAUDE.md" site:github.com tutor education learning`
- Creative: `"CLAUDE.md" site:github.com creative writing content`
- Work: `"CLAUDE.md" site:github.com research analysis professional`

**Step 2: Fetch and analyze top results**

Use WebFetch to read actual CLAUDE.md content from promising repos:

```
WebFetch("https://raw.githubusercontent.com/[owner]/[repo]/main/CLAUDE.md")
```

Also check these known high-quality sources:
- `https://raw.githubusercontent.com/anthropics/claude-code/main/CLAUDE.md`
- Search results from awesome-claude-code or similar curated lists

**Step 3: Extract relevant patterns**

From fetched configs, identify and extract:
- System prompt structures that match the use case
- Communication style guidelines
- Working approach patterns
- Useful custom commands or workflows
- Domain-specific instructions

**What to copy/adapt:**
- Section headers and organization patterns
- Phrasing for communication guidelines
- Permission configurations
- Workflow descriptions
- Any domain expertise relevant to the use case

**What NOT to copy:**
- Project-specific details (file paths, API endpoints)
- Credentials or secrets
- Overly technical coding-specific instructions (unless relevant)
- Sections that don't match the user's stated purpose

### Phase 3: Generate Configuration

Combine user requirements with researched patterns to create configuration files.

**CLAUDE.md Structure:**
```markdown
# [Machine Name]

## Purpose
[1-2 sentence description based on Phase 1]

## Communication Style
[Adapt from researched patterns + user preferences]

## Working Approach
[Adapt from researched patterns + user preferences]

## Integrations
[List of configured integrations, if any]

## Available Skills
[Relevant skills for this use case]

## [Additional sections copied/adapted from research]
[Include any useful patterns found in Phase 2]
```

**.claude/settings.json:**
```json
{
  "permissions": {
    "allow": [],
    "deny": [],
    "defaultMode": "[based on working approach]"
  }
}
```
- "Ask before acting" -> `"acceptEdits"`
- "Work autonomously" -> `"bypassPermissions"`
- "Plan first" -> `"plan"`

**.mcp.json (if integrations selected):**
See references/mcp-integrations.md for specific configs.

### Phase 4: Apply and Guide

1. **Show the user what you found** - Briefly mention which repos/patterns you drew from
2. **Write configuration files** - Create/update CLAUDE.md, settings.json, .mcp.json
3. **Summarize what was configured** - Overview of the final configuration
4. **Guide secrets setup** - If integrations selected: "Go to Settings (gear icon) > Secrets to add your API keys"
5. **Suggest first interaction** - Recommend a task to test the setup

## Research Sources

### Primary Sources (always check)
- anthropics/claude-code - Official Claude Code patterns
- anthropics/skills - Official skills structure

### Search Strategies by Use Case

**Personal Assistant:**
- Search: `CLAUDE.md assistant productivity organization`
- Look for: scheduling patterns, reminder systems, task management

**Learning/Education:**
- Search: `CLAUDE.md tutor learning education`
- Look for: explanation patterns, progress tracking, quiz/exercise formats

**Creative Projects:**
- Search: `CLAUDE.md creative writing brainstorm`
- Look for: ideation workflows, feedback patterns, iteration approaches

**Work/Professional:**
- Search: `CLAUDE.md research analysis professional`
- Look for: documentation patterns, review processes, communication templates

## Important Notes

- **Cite your sources**: Tell users which repos you drew patterns from
- **Adapt, don't copy blindly**: Customize found patterns to match user's specific needs
- **Preserve existing config**: If CLAUDE.md exists, ask before overwriting
- **Never collect secrets in chat**: Always direct to Settings > Secrets UI
- **Fallback to templates**: If research yields poor results, use references/use-case-templates.md

## Reference Files

- **Personality patterns**: references/personality-patterns.md - communication styles and tones
- **Use case templates**: references/use-case-templates.md - fallback pre-built configurations
- **MCP integrations**: references/mcp-integrations.md - external service configs
- **Curated configs**: references/curated-configs.md - known good sources to search
