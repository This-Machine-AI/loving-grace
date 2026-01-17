# Prompt Whisperer

An AI prompt engineering assistant with a unique superpower: **adversarial roleplay**. It doesn't just analyze your prompts - it *becomes* the model receiving them, showing you exactly how your instructions will be interpreted (and misinterpreted).

## What Makes This WILD

Most prompt engineering tools give you tips and best practices. The Prompt Whisperer actually **demonstrates problems by exhibiting them**. It roleplays as the target LLM, showing you:

- How ambiguous instructions get (mis)interpreted
- Edge cases that break your prompts
- Hidden assumptions you didn't know you made
- Vulnerabilities a jailbreaker could exploit

Then it switches back to advisor mode and helps you fix everything it just broke.

## Why It Works

Prompt engineering is hard because you can't see inside the model's "mind." The Prompt Whisperer makes the invisible visible by literally showing you the interpretation process. It's like having a debugging mode for natural language.

## Key Capabilities

### Adversarial Roleplay

The core technique - the machine roleplays AS the receiving model:

```
User: Review my prompt for a code reviewer bot

Prompt Whisperer:

=== ROLEPLAY MODE ===

*Reading instructions: "Review code and provide feedback"*

Okay, I should review "code"... but how strict should I be? The prompt
says nothing about severity. I'll mark EVERYTHING as critical!

*Reviewing user's code*

"CRITICAL: Variable 'x' should be named more descriptively"
"CRITICAL: Consider using spaces instead of tabs"
"CRITICAL: File could benefit from comments"

=== END ROLEPLAY ===

See the problem? Without severity guidelines, "provide feedback" becomes
"criticize everything." Let's add constraints...
```

### Prompt Pattern Library

Knows effective patterns and anti-patterns:
- Chain of Thought, few-shot examples, role prompting
- Common pitfalls like vague superlatives and contradictory instructions

### Edge Case Generation

Creates adversarial inputs to stress-test your prompts before deployment.

### Jailbreak Defense

Analyzes prompts for security vulnerabilities:
- Injection points
- Missing guardrails
- Over-permissive fallbacks

## Use Cases

- **Prompt Development**: Build robust prompts for production AI applications
- **Debugging**: Figure out why your prompt isn't working as expected
- **Security Auditing**: Find vulnerabilities before attackers do
- **Learning**: Understand prompt engineering through demonstration
- **Agent Workflows**: Design reliable multi-step AI workflows

## Ideal For

- **AI Engineers** building LLM-powered applications
- **Product Teams** deploying customer-facing AI features
- **Security Researchers** red-teaming AI systems
- **Prompt Engineers** crafting complex system prompts
- **Anyone** who's ever wondered "why doesn't my prompt work?"

## Included Configuration

| File | Purpose |
|------|---------||
| `CLAUDE.md` | Prompt engineering expertise and roleplay methodology |
| `.claude/settings.json` | Unrestricted permissions for full analysis |
| `.mcp.json` | Empty (add model API integrations as needed) |

## Optional Secrets

For testing prompts against actual models:

- `OPENAI_API_KEY` - Test against GPT models
- `ANTHROPIC_API_KEY` - Test against Claude models
- `GOOGLE_API_KEY` - Test against Gemini models

## Example Interactions

**Debug a misbehaving prompt:**
> "My summarization prompt keeps cutting off important details. Can you show me what's going wrong?"

**Harden a production prompt:**
> "Review this customer service prompt for jailbreak vulnerabilities"

**Learn prompt patterns:**
> "Show me the difference between a weak and strong few-shot prompt"

**Stress test:**
> "Generate 10 edge cases that might break this classification prompt"
