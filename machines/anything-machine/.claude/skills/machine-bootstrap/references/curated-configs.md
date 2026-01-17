# Curated Claude Configurations

Direct URLs and search strategies for finding high-quality Claude configurations to copy and adapt.

## Primary Sources (Always Fetch These)

### Official Anthropic
```
https://raw.githubusercontent.com/anthropics/claude-code/main/CLAUDE.md
```
- Official Claude Code patterns
- Communication guidelines
- Tool usage best practices

### Community Curated Lists
```
https://api.github.com/search/repositories?q=awesome-claude-code&sort=stars
https://api.github.com/search/repositories?q=claude-code-examples&sort=stars
```
- Community-validated patterns
- Domain-specific examples

## Fetch Strategy

### Step 1: Search for relevant repos
```
WebSearch("CLAUDE.md site:github.com [keywords]")
```

### Step 2: Convert GitHub URLs to raw URLs
```
GitHub:  https://github.com/owner/repo/blob/main/CLAUDE.md
Raw:     https://raw.githubusercontent.com/owner/repo/main/CLAUDE.md
```

### Step 3: Fetch and parse
```
WebFetch(raw_url, "Extract the communication style, working approach, and any useful patterns")
```

## Search Queries by Use Case

### Personal Assistant / Productivity
```
CLAUDE.md site:github.com assistant productivity todo
CLAUDE.md site:github.com personal organizer planner
CLAUDE.md site:github.com daily tasks reminder
```

### Learning / Education
```
CLAUDE.md site:github.com tutor learning teaching
CLAUDE.md site:github.com education study help
CLAUDE.md site:github.com quiz flashcard practice
```

### Creative / Writing
```
CLAUDE.md site:github.com creative writing content
CLAUDE.md site:github.com brainstorm ideation
CLAUDE.md site:github.com storytelling narrative
```

### Research / Analysis
```
CLAUDE.md site:github.com research analysis report
CLAUDE.md site:github.com data investigation
CLAUDE.md site:github.com literature review synthesis
```

### Professional / Work
```
CLAUDE.md site:github.com professional business
CLAUDE.md site:github.com email communication
CLAUDE.md site:github.com meeting notes summary
```

## What to Extract

### From any config, look for:

**Communication patterns:**
```markdown
## Communication Style
- Tone guidelines
- Response length preferences
- How to handle uncertainty
```

**Working approach:**
```markdown
## Working Approach
- When to ask vs assume
- How to break down tasks
- How to present options
```

**Useful commands/workflows:**
```markdown
## Commands
Any /commands or workflows that seem useful
```

**Domain knowledge:**
```markdown
## Domain Knowledge
Specific expertise or context
```

## What NOT to Copy

- File paths specific to other projects
- API keys, tokens, or credentials
- References to specific codebases
- Overly technical coding instructions (unless user wants coding help)
- Sections unrelated to user's stated purpose

## Fallback

If searches don't yield good results:
1. Use templates from references/use-case-templates.md
2. Use personality blocks from references/personality-patterns.md
3. Generate config based solely on user's stated preferences
