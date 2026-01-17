# Incident Commander

A specialized DevOps and SRE assistant for managing production incidents, coordinating response teams, and driving post-incident learning.

## What It Does

The Incident Commander helps engineering teams handle production incidents with structure and clarity:

- **Incident Response**: Declare incidents, classify severity, establish coordination, and track timelines in real-time
- **Communication**: Draft status updates for different audiences—internal teams, executives, and customers
- **Runbook Execution**: Walk through diagnostic and remediation steps methodically, tracking what's been tried
- **Post-Mortems**: Facilitate blameless reviews, identify root causes, and generate actionable follow-ups
- **On-Call Support**: Generate handoff summaries, triage alerts, and help prioritize during busy periods

## Key Features

### Incident Command System (ICS)
Lightweight adaptation of the Incident Command System with clear roles (IC, Tech Lead, Comms Lead, Scribe) and principles for effective coordination.

### Severity Classification
SEV1-SEV4 framework with clear impact definitions and appropriate response levels:
- **SEV1**: Complete outage, all-hands response
- **SEV2**: Major degradation, escalated response
- **SEV3**: Minor degradation, on-call response
- **SEV4**: Minimal impact, normal hours

### Communication Templates
Ready-to-use templates for:
- Status page updates
- Executive summaries
- Customer notifications
- Stakeholder briefs

### Runbook Development
Guidance for creating effective runbooks with symptoms, diagnostics, remediation steps, and verification.

## Use Cases

- Active incident coordination and timeline tracking
- Writing status updates during outages
- Conducting blameless post-mortems
- Creating and maintaining runbooks
- On-call handoffs and shift preparation
- Alert triage and prioritization
- Reliability metrics tracking (MTTR, MTTA)

## Optional Integrations

Configure these in `.mcp.json` with corresponding secrets:

- **PagerDuty** - On-call schedules and incident management
- **Slack** - Incident channel communication
- **Datadog** - Metrics and dashboard queries
- **OpsGenie** - Alert management
- **Statuspage** - Public status updates

## Workspace Structure

The machine organizes incident-related files:

```
workspace/
├── incidents/       # Incident logs and timelines
├── runbooks/        # Diagnostic and remediation playbooks
├── postmortems/     # Post-incident reviews
└── oncall/          # Schedules and escalation paths
```

## Who It's For

- **SRE Teams**: Structured incident response and reliability improvement
- **DevOps Engineers**: On-call support and runbook management
- **Engineering Managers**: Incident coordination and stakeholder communication
- **Platform Teams**: Post-mortem facilitation and systemic improvements
