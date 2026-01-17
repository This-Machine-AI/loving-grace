# Code Archaeologist

A specialized machine for excavating, understanding, and documenting legacy codebases. Perfect for teams inheriting unfamiliar code, planning migrations, or onboarding new developers to complex systems.

## What It Does

The Code Archaeologist helps you understand codebases that lack documentation, have unclear architecture, or have evolved through multiple generations of developers. Like a real archaeologist, it approaches code with patience and systematic methodology—discovering, documenting, and illuminating rather than judging.

### Core Capabilities

**Codebase Mapping**
- Map directory structures and identify architectural patterns
- Build dependency graphs (internal modules and external services)
- Detect technology stacks, frameworks, and build systems
- Find entry points and trace module boundaries

**Code Understanding**
- Trace data flows from input to output
- Follow control flow and execution paths
- Identify design patterns and anti-patterns
- Recognize conventions and detect inconsistencies across different eras of development

**Documentation Generation**
- Create architecture diagrams (Mermaid, ASCII)
- Generate missing documentation from code analysis
- Write onboarding guides for new developers
- Extract business rules from conditional logic
- Produce glossaries of domain terms

**Risk Assessment**
- Inventory technical debt (TODOs, FIXMEs, complexity hotspots)
- Detect fragile code and hidden coupling
- Find security issues (hardcoded secrets, injection vulnerabilities)
- Identify "bus factor" risks and single points of failure

**Migration Support**
- Plan modernization strategies
- Identify strangler fig extraction candidates
- Map dependencies that would block changes
- Guide safe refactoring with step-by-step plans

## Example Use Cases

1. **"What does this codebase do?"** - Get a plain-language overview of any system
2. **"Help me understand how authentication works"** - Trace specific flows end-to-end
3. **"What are the riskiest parts of this code?"** - Get a prioritized risk assessment
4. **"Create onboarding documentation"** - Generate guides for new team members
5. **"Plan a migration to microservices"** - Get incremental extraction roadmaps

## Methodology

The Code Archaeologist follows a four-phase excavation methodology:

1. **Survey** - Broad overview of structure, stack, and existing docs
2. **Shallow Dig** - Entry points, main flows, configuration
3. **Deep Excavation** - Complex flows, integrations, technical debt
4. **Synthesis** - Architecture docs, risk reports, onboarding materials

## Deliverables

- **Codebase Overview** - One-page summary with architecture diagram
- **Dependency Map** - Visual map of internal and external dependencies
- **Risk Register** - Prioritized inventory of technical debt and security concerns
- **Developer Onboarding Guide** - Practical guide for new team members
- **Excavation Log** - Running record of discoveries and recommendations

## Configuration

### Secrets

For analyzing private repositories, add these secrets:

| Secret | Purpose |
|--------|--------|
| `GITHUB_TOKEN` | Clone private GitHub repositories |
| `GITLAB_TOKEN` | Clone private GitLab repositories |
| `BITBUCKET_TOKEN` | Clone private Bitbucket repositories |

### Permissions

This machine runs with full permissions by default, allowing it to:
- Read and analyze any files in the workspace
- Clone repositories
- Run static analysis tools
- Generate documentation files

## Limitations

- **Static analysis only** - Does not execute untrusted code unless explicitly requested
- **Requires workspace access** - Private repos must be cloned or copied to the workspace
- **Historical context** - Some architectural decisions require human knowledge to explain
- **Scope matters** - Deep archaeology of large codebases takes proportionally more time

## Best Practices

1. **Start broad, then narrow** - Let the archaeologist survey first before asking specific questions
2. **Provide context** - Share what you already know about the codebase's history
3. **Set clear scope** - For large codebases, focus on specific modules or questions
4. **Iterate** - Use findings from early phases to guide deeper investigation
