# API Architect

A specialized machine for designing, reviewing, documenting, and evolving APIs. Whether you're building REST APIs, GraphQL schemas, or gRPC services, API Architect helps you create developer-friendly interfaces that are consistent, secure, and built to last.

## What It Does

API Architect combines deep knowledge of API standards with practical implementation guidance:

- **Design APIs from requirements** - Describe what you need, get a complete API specification
- **Review existing APIs** - Get feedback on consistency, usability, security, and best practices
- **Generate documentation** - Create OpenAPI specs, GraphQL schemas, or Protocol Buffers
- **Plan API evolution** - Identify breaking changes, create migration guides, manage deprecations
- **Implement patterns** - Get guidance on auth, pagination, rate limiting, error handling, and more

## Key Features

### Multi-Protocol Support

| Protocol | Capabilities |
|----------|--------------|
| REST | OpenAPI 3.x specs, resource modeling, HATEOAS |
| GraphQL | Schema design, query optimization, federation |
| gRPC | Protocol Buffer definitions, streaming patterns |
| AsyncAPI | Event-driven APIs, webhooks, message queues |

### Design Reviews

API Architect analyzes your APIs for:
- **Consistency** - Naming conventions, response structures, error formats
- **Usability** - Intuitive design, clear documentation, good defaults
- **Security** - Authentication patterns, authorization, input validation
- **Evolvability** - Versioning strategy, backward compatibility

### Practical Patterns

Get implementation guidance for common challenges:
- Authentication (OAuth 2.0, API keys, JWT, mTLS)
- Pagination (cursor-based, offset, keyset)
- Rate limiting and quotas
- Bulk operations and batch endpoints
- Idempotency and retry handling
- Caching strategies

## Example Use Cases

- "Design a REST API for a task management app"
- "Review this OpenAPI spec and suggest improvements"
- "Convert this REST API to GraphQL"
- "What's the best pagination strategy for this use case?"
- "Help me version this API without breaking existing clients"
- "Generate TypeScript types from this OpenAPI spec"
- "Design webhook payloads for order status updates"

## Included Configuration

| File | Purpose |
|------|---------|`
| `CLAUDE.md` | API design principles, patterns, and conventions |
| `.claude/settings.json` | Unrestricted permissions for full flexibility |
| `.mcp.json` | Empty by default (add your integrations) |

## Useful Environment Variables

Add these secrets for enhanced capabilities:

- `GITHUB_TOKEN` - Access private repositories and create PRs with API changes
- `OPENAPI_KEY` - For OpenAPI validation services
- `POSTMAN_API_KEY` - Sync with Postman collections

## Who It's For

- **Backend developers** building new APIs or maintaining existing ones
- **API platform teams** establishing standards and reviewing designs
- **Technical architects** planning API strategies and migrations
- **Developer advocates** creating API documentation and examples
