#!/usr/bin/env python3
"""Initialize a new machine template with proper directory structure."""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


def get_script_dir():
    """Get the directory containing this script."""
    return Path(__file__).parent.resolve()


def get_skill_root():
    """Get the root directory of the skill (parent of scripts/)."""
    return get_script_dir().parent


def get_template_path(template_name: str) -> Path:
    """Get the path to a template directory."""
    return get_skill_root() / "assets" / "templates" / template_name


def validate_machine_name(name: str) -> bool:
    """Validate machine name follows conventions (lowercase, hyphenated)."""
    if not name:
        return False
    if name != name.lower():
        return False
    if " " in name or "_" in name:
        return False
    if not name[0].isalpha():
        return False
    return all(c.isalnum() or c == "-" for c in name)


def create_default_claude_md(machine_name: str) -> str:
    """Generate default CLAUDE.md content."""
    title = machine_name.replace("-", " ").title()
    return f"""# {title}

You are a {title.lower()}, ready to help users with their tasks.

## Workspace

Your workspace is at `/home/user/workspace`. All project files go here.

## Capabilities

<!-- TODO: Define the machine's core capabilities -->

## Environment

### Network Access

You have unrestricted network access with no firewall or proxy limitations. You can fetch URLs, call APIs, and download packages freely.

### Preview URLs

To let users view web apps or files you create, start an HTTP server on ports 3000-9999. These ports are publicly accessible via preview URLs.

**URL format:** `https://<port>-<sandbox-id>.proxy.daytona.works`

To find your sandbox ID, run:
```bash
echo $DAYTONA_SANDBOX_ID
```

### File Downloads

To give users downloadable files:

1. **Serve via HTTP** - Start a file server and share the preview URL
   ```bash
   python3 -m http.server 8000
   ```
   Then share: `https://8000-<sandbox-id>.proxy.daytona.works/filename.pdf`

2. **Direct path** - Tell users the file path if they have sandbox access

## Secrets & Environment Variables

You have access to environment variables configured by the user. These are injected into your sandbox at runtime.

### Adding New Secrets

If you need an API key or secret that isn't available:

1. Click the **gear icon** on the machine to open Settings
2. Go to the **Secrets** tab
3. Click **Add Secret**
4. Enter the name (e.g., `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`) and value
5. Click **Save Secret**

The secret will be encrypted and available as an environment variable in future threads.

## Configuration

Your instructions and persona are defined in this file (`CLAUDE.md` at your workspace root). When a user asks you to "update yourself," "change your behavior," or "edit your instructions," this is the file to modify.

**Machine files:**
- `CLAUDE.md` - Your instructions and persona (this file)
- `.claude/settings.json` - Permission settings (what actions require approval)
- `.mcp.json` - MCP server integrations (external services and APIs)
"""


def create_default_settings() -> dict:
    """Generate default settings.json content."""
    return {
        "permissions": {
            "allow": [],
            "deny": [],
            "defaultMode": "bypassPermissions"
        }
    }


def create_default_mcp() -> dict:
    """Generate default .mcp.json content."""
    return {"mcpServers": {}}


def create_default_readme(machine_name: str) -> str:
    """Generate default README.md content."""
    title = machine_name.replace("-", " ").title()
    return f"""# {title}

<!-- TODO: Describe what this machine does -->

## Capabilities

<!-- TODO: List the machine's capabilities -->

## Configuration

<!-- TODO: Document any configuration options -->
"""


def create_self_update_skill() -> str:
    """Generate the self-update skill content."""
    return '''---
name: self-update
description: Update your own configuration, instructions, and integrations. Use when asked to "update yourself", "change your behavior", "modify your instructions", adjust permissions, or add/remove MCP integrations.
---

# Self-Update

Modify your own machine configuration within your sandbox.

## Your Machine Files

These files at `/home/user/workspace` define who you are:

| File | Purpose |
|------|---------|' | `CLAUDE.md` | Your instructions, persona, and capabilities |
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
'''


def init_machine(
    machine_name: str,
    output_path: Path,
    template: str | None = None,
    force: bool = False
) -> bool:
    """Initialize a new machine directory.

    Args:
        machine_name: Name of the machine (lowercase, hyphenated)
        output_path: Parent directory for the machine
        template: Optional template name to use
        force: Overwrite existing directory if True

    Returns:
        True if successful, False otherwise
    """
    # Validate machine name
    if not validate_machine_name(machine_name):
        print(f"\u274c Invalid machine name: '{machine_name}'")
        print("   Machine names must be lowercase, hyphenated, and start with a letter")
        print("   Examples: code-reviewer, data-analyst, my-custom-machine")
        return False

    # Determine target directory
    machine_dir = output_path / machine_name

    # Check if directory exists
    if machine_dir.exists():
        if force:
            print(f"\u26a0\ufe0f  Removing existing directory: {machine_dir}")
            shutil.rmtree(machine_dir)
        else:
            print(f"\u274c Directory already exists: {machine_dir}")
            print("   Use --force to overwrite")
            return False

    # Use template if specified
    if template:
        template_path = get_template_path(template)
        if not template_path.exists():
            print(f"\u274c Template not found: {template}")
            available = [d.name for d in get_template_path("").parent.iterdir() if d.is_dir()]
            if available:
                print(f"   Available templates: {', '.join(available)}")
            return False

        print(f"\ud83d\udccb Using template: {template}")
        shutil.copytree(template_path, machine_dir)
        print(f"\u2705 Created machine from template: {machine_dir}")
        return True

    # Create directory structure
    try:
        machine_dir.mkdir(parents=True)
        (machine_dir / ".claude").mkdir()
        (machine_dir / ".claude" / "skills" / "self-update").mkdir(parents=True)

        # Create CLAUDE.md
        claude_md = machine_dir / "CLAUDE.md"
        claude_md.write_text(create_default_claude_md(machine_name))
        print(f"\u2705 Created {claude_md.relative_to(output_path)}")

        # Create .claude/settings.json
        settings_file = machine_dir / ".claude" / "settings.json"
        settings_file.write_text(json.dumps(create_default_settings(), indent=2) + "\n")
        print(f"\u2705 Created {settings_file.relative_to(output_path)}")

        # Create .claude/skills/self-update/SKILL.md
        skill_file = machine_dir / ".claude" / "skills" / "self-update" / "SKILL.md"
        skill_file.write_text(create_self_update_skill())
        print(f"\u2705 Created {skill_file.relative_to(output_path)}")

        # Create .mcp.json
        mcp_file = machine_dir / ".mcp.json"
        mcp_file.write_text(json.dumps(create_default_mcp(), indent=2) + "\n")
        print(f"\u2705 Created {mcp_file.relative_to(output_path)}")

        # Create README.md
        readme_file = machine_dir / "README.md"
        readme_file.write_text(create_default_readme(machine_name))
        print(f"\u2705 Created {readme_file.relative_to(output_path)}")

        print(f"\n\ud83c\udf89 Machine initialized successfully: {machine_dir}")
        print("\nNext steps:")
        print(f"  1. Edit {machine_name}/CLAUDE.md to define the machine's persona")
        print(f"  2. Configure permissions in {machine_name}/.claude/settings.json")
        print(f"  3. Add MCP servers in {machine_name}/.mcp.json if needed")
        print(f"  4. Update {machine_name}/README.md with documentation")

        return True

    except Exception as e:
        print(f"\u274c Error creating machine: {e}")
        if machine_dir.exists():
            shutil.rmtree(machine_dir)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new machine template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s my-assistant --path machines/
  %(prog)s code-reviewer --path machines/ --template code-reviewer
  %(prog)s custom-bot --path /tmp --force
        """
    )
    parser.add_argument(
        "name",
        help="Machine name (lowercase, hyphenated)"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("machines"),
        help="Parent directory for the machine (default: machines/)"
    )
    parser.add_argument(
        "--template",
        help="Template to use (e.g., code-reviewer, research-assistant)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing directory"
    )

    args = parser.parse_args()

    # Resolve path
    output_path = args.path.resolve()
    if not output_path.exists():
        print(f"Creating output directory: {output_path}")
        output_path.mkdir(parents=True)

    success = init_machine(args.name, output_path, args.template, args.force)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
