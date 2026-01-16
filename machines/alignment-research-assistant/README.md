# Alignment Research Assistant

A specialized machine for AI safety and alignment researchers. Designed to support rigorous research on ensuring advanced AI systems are safe and beneficial.

## Capabilities

| Capability | Description |
|------------|-------------|
| Literature Review | Analyze papers, summarize contributions, identify research gaps |
| Argument Analysis | Map argument structures, identify cruxes, steel-man positions |
| Technical Support | Review ML code, assist with experiments, implement interpretability techniques |
| Writing Assistance | Draft papers, structure arguments, improve clarity and rigor |
| Web Access | Fetch papers, access APIs, download packages |
| File Serving | Share documents and visualizations via preview URLs |

## Research Areas

- **Technical Alignment**: RLHF, scalable oversight, reward modeling, corrigibility
- **Interpretability**: Mechanistic interpretability, sparse autoencoders, circuit analysis
- **AI Governance**: Compute governance, evaluation frameworks, deployment safety

## Included Configuration

| File | Purpose |
|------|---------||
| `CLAUDE.md` | Research assistant instructions and domain knowledge |
| `.claude/settings.json` | Permission configurations |
| `.mcp.json` | MCP server configurations (empty by default) |

## Example Use Cases

- Review a draft alignment paper for technical accuracy and clarity
- Summarize recent interpretability research from arXiv
- Analyze arguments in an Alignment Forum post
- Debug a mechanistic interpretability experiment
- Draft a research proposal for a new safety technique

## Customization

### Adding Research Tools

Edit `.mcp.json` to add MCP servers for:
- Reference managers (Zotero)
- Note-taking systems (Notion, Obsidian)
- Code repositories (GitHub)
- Database access for experiment tracking

### Extending Focus Areas

Edit `CLAUDE.md` to add:
- Specific research agendas or frameworks
- Lab-specific conventions and practices
- Custom evaluation criteria
- Additional domain knowledge
