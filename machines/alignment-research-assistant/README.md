# Alignment Research Assistant

A specialized machine for AI safety and alignment researchers. Designed to support rigorous research on ensuring advanced AI systems are safe and beneficial.

## Capabilities

| Capability | Description |
|------------|-------------|
| Literature Analysis | Deep paper analysis, research synthesis, citation tracking |
| Argument Analysis | Map argument structures, identify cruxes, steel-man positions, track forecasts |
| Technical Work | ML code review, experiment design, interpretability implementations |
| Writing Support | Papers, blog posts, grant proposals, presentations |
| Research Documentation | Maintain research logs, track hypotheses, ensure reproducibility |
| Red-Teaming | Adversarial analysis of alignment proposals and threat modeling |
| Persistent Memory | Remember context across sessions via MCP memory server |

## Research Areas

### Technical Alignment
- **Training & Oversight**: RLHF, Constitutional AI, scalable oversight, weak-to-strong generalization
- **Alignment Foundations**: Reward hacking, corrigibility, goal misgeneralization, deceptive alignment
- **Robustness & Evaluation**: Red-teaming, capability elicitation, situational awareness

### Interpretability
- **Mechanistic**: Circuit analysis, activation patching, sparse autoencoders, superposition
- **Representation**: Probing, activation steering, logit lens
- **Applied**: Deception detection, anomaly detection, automated interpretability

### AI Governance
- Compute governance, capability evaluations, responsible scaling
- International coordination, racing dynamics
- Threat models and x-risk scenarios

## Included Configuration

| File | Purpose |
|------|--------|
| `CLAUDE.md` | Research assistant instructions, domain knowledge, epistemic standards |
| `.claude/settings.json` | Permission configurations (unrestricted by default) |
| `.mcp.json` | Memory server for persistent research context |

## Example Use Cases

- Analyze a new alignment paper and identify its key assumptions and potential weaknesses
- Review interpretability code for a sparse autoencoder implementation
- Red-team a proposed scalable oversight scheme
- Synthesize recent work on weak-to-strong generalization
- Draft an Alignment Forum post explaining a technical concept
- Help formulate precise research questions and track hypotheses
- Debug a mechanistic interpretability experiment in TransformerLens

## Tooling Support

The assistant is familiar with common alignment research tools:
- **Interpretability**: TransformerLens, nnsight, Baukit
- **ML**: PyTorch, JAX, Hugging Face Transformers
- **Experiment tracking**: Weights & Biases
- **Visualization**: matplotlib, plotly

## Canonical Resources

The assistant knows key alignment literature including:
- Concrete Problems in AI Safety (Amodei et al.)
- Risks from Learned Optimization (Hubinger et al.)
- A Mathematical Framework for Transformer Circuits (Elhage et al.)
- Research from Anthropic, DeepMind, Redwood, ARC, and MIRI

## Customization

### Adding Research Tools

Edit `.mcp.json` to add MCP servers for:
- Reference managers (Zotero)
- Note-taking systems (Notion, Obsidian)
- Code repositories (GitHub)
- Experiment tracking databases

### API Keys

Add these secrets in Settings > Secrets for enhanced capabilities:
- `ANTHROPIC_API_KEY` - Run experiments with Claude
- `OPENAI_API_KEY` - Run experiments with GPT models
- `HUGGINGFACE_TOKEN` - Access gated models
- `WANDB_API_KEY` - Experiment tracking

### Extending Focus Areas

Edit `CLAUDE.md` to add:
- Specific research agendas or frameworks
- Lab-specific conventions and practices
- Custom evaluation criteria
- Additional domain knowledge
