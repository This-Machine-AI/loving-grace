# loving-grace Registry

This is the official machine registry for This Machine.

## Repository Structure

```
machines/
└── <machine-name>/
    ├── CLAUDE.md           # Workspace instructions (copied to user workspace)
    ├── .claude/
    │   └── settings.json   # Permission configurations
    ├── .mcp.json           # MCP server configurations
    └── README.md           # Documentation for this template
```

## Adding a New Machine

1. Create a new directory under `machines/` with your machine name
2. Add the required configuration files (see structure above)
3. Document your machine in its README.md
4. Update the root README.md to list the new machine

## How Templates Are Used

When a user creates a new This Machine without providing their own repository:
1. This registry is cloned to a temporary location
2. The selected machine template is copied to the user's workspace
3. Anthropic's skills repository is also cloned for additional capabilities
