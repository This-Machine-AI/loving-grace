# Migration Maestro

A specialized machine for planning and executing code migrations, framework upgrades, database transitions, and large-scale refactoring projects.

## What It Does

The Migration Maestro helps developers navigate complex migration work:

- **Framework Upgrades**: React, Vue, Angular, Next.js, and other major frameworks
- **Build Tool Migrations**: Webpack to Vite, CRA to Next.js, bundler transitions
- **Database Migrations**: Schema changes, ORM switches, SQL to NoSQL transitions
- **API Migrations**: REST to GraphQL, API versioning, authentication system changes
- **Architectural Changes**: Monolith to microservices, serverless adoption, cloud migrations
- **Code Quality**: TypeScript adoption, module system transitions, linting/formatting setup

## Methodology

The Migration Maestro follows a structured **Safe Migration Protocol**:

1. **Assess** - Analyze current state, identify touchpoints, document status quo
2. **Plan** - Create phased migration plan with milestones and rollback points
3. **Prepare** - Set up feature flags, compatibility layers, testing infrastructure
4. **Execute** - Implement changes incrementally with validation at each step
5. **Validate** - Run comprehensive tests, monitor for regressions
6. **Complete** - Remove compatibility layers, clean up, document changes

## Key Principles

- Never big-bang rewrites - always incremental migrations
- Design for old and new to coexist during transition
- Every step must be reversible (rollback-ready)
- Test coverage before migration, validation after each phase
- Document everything for future maintainers

## Example Use Cases

- "Help me upgrade from React 17 to React 18"
- "Plan a migration from REST API to GraphQL"
- "I need to migrate from Sequelize to Prisma"
- "Help me convert this CommonJS codebase to ESM"
- "Plan breaking apart this monolith into microservices"
- "Migrate our authentication from sessions to JWT"

## Included Capabilities

- Dependency impact analysis
- Breaking change detection
- Phased migration plan generation
- Compatibility matrix creation
- Rollback procedure design
- Migration checklist generation
