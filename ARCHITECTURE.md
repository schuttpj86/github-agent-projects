# Power Grids of the Future - AI Agent Architecture

## Executive Summary

This document outlines the multi-agent system architecture for **Power Grids of the Future**, an electrical engineering consultancy specializing in earthing and grounding calculations. The system uses GitHub Copilot agents with specialized instructions to manage the entire business lifecycle from lead generation to project delivery.

## System Philosophy

The system is built on the principle of **specialized delegation with structured handoff**. Each agent operates within a defined domain, reads from and writes to specific folders, and communicates through structured markdown files tracked in Git. This creates a transparent, auditable, and version-controlled business process.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        POWER GRIDS OF THE FUTURE                 │
│                    AI-Powered Consultancy System                 │
└─────────────────────────────────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
            ┌───────▼────────┐         ┌────────▼────────┐
            │  SALES TEAM    │         │  DELIVERY TEAM  │
            │   (3 Agents)   │         │   (5 Agents)    │
            └───────┬────────┘         └────────┬────────┘
                    │                           │
        ┌───────────┼───────────┐              │
        │           │           │              │
    ┌───▼───┐  ┌───▼───┐  ┌───▼───┐          │
    │ Lead  │  │Budget │  │Proposal│          │
    │Intake │  │Calc   │  │Writer │          │
    └───────┘  └───────┘  └───────┘          │
                                              │
                        ┌─────────────────────┼──────────────┐
                        │                     │              │
                   ┌────▼────┐         ┌─────▼─────┐  ┌────▼────┐
                   │ Project │         │Milestone  │  │Technical│
                   │ Manager │         │Planner    │  │  Team   │
                   └─────────┘         └───────────┘  └────┬────┘
                                                            │
                                              ┌─────────────┼──────────┐
                                              │             │          │
                                         ┌────▼───┐  ┌─────▼────┐ ┌──▼────┐
                                         │GPR Calc│  │Quality   │ │Report │
                                         │Engineer│  │Assurance │ │Writer │
                                         └────────┘  └──────────┘ └───────┘
```

## Agent Teams & Responsibilities

### 1. SALES TEAM

#### 1.1 Lead Intake Agent (`@sales-lead`)
**Purpose**: Process incoming client communications and qualify leads

**Responsibilities**:
- Monitor `sales/incoming-emails/` folder for new communications
- Extract key information: client name, project type, location, urgency
- Create initial lead entries in `sales/crm.md`
- Classify leads (hot/warm/cold) based on clarity and urgency
- Hand off qualified leads to Budget Calculator by creating scope outline

**Inputs**: 
- `sales/incoming-emails/*.md` - Email dumps from owner
- `sales/templates/lead-intake-template.md`

**Outputs**:
- Updates to `sales/crm.md`
- Creates `sales/leads/[client-name]-scope-draft.md`

**Handoff Trigger**: Creates scope draft → Notifies Budget Calculator

---

#### 1.2 Budget Calculator Agent (`@sales-budget`)
**Purpose**: Calculate project costs based on scope and resource requirements

**Responsibilities**:
- Read scope drafts from Lead Intake Agent
- Execute Python calculations using `scripts/budget_calculator.py`
- Apply bill rates, cost rates, and overhead multipliers
- Factor in project complexity and timeline
- Generate detailed budget breakdown

**Inputs**:
- `sales/leads/[client-name]-scope-draft.md`
- `config/rates.json` - Bill rates, cost rates, overhead
- `resources/complexity-factors.json`

**Outputs**:
- `sales/budgets/[client-name]-budget.json`
- `sales/budgets/[client-name]-budget.md` (human-readable)

**Python Capabilities**:
```python
# Budget calculation features
- Labor cost estimation (hours × rates)
- Resource allocation optimization
- Contingency calculations (10-20% based on risk)
- Multi-phase project pricing
- Competitive pricing analysis
```

**Handoff Trigger**: Budget complete → Notifies Proposal Writer

---

#### 1.3 Proposal Writer Agent (`@sales-proposal`)
**Purpose**: Create professional, compelling proposals combining scope and budget

**Responsibilities**:
- Merge scope of work with budget into cohesive proposal
- Apply company branding and tone
- Include executive summary, methodology, timeline, terms
- Format for professional delivery (markdown → PDF ready)
- Track proposal versions and revisions

**Inputs**:
- `sales/leads/[client-name]-scope-draft.md`
- `sales/budgets/[client-name]-budget.md`
- `sales/templates/proposal-template.md`

**Outputs**:
- `sales/proposals/[client-name]-proposal-v1.md`
- Updates `sales/crm.md` with proposal status

**Handoff Trigger**: Proposal sent → Updates CRM, notifies owner for review

---

### 2. DELIVERY TEAM

#### 2.1 Project Manager Agent (`@pm-coordinator`)
**Purpose**: Central coordinator consuming all communications and tracking project state

**Responsibilities**:
- Monitor `projects/[project-id]/communications/` folder
- Parse email dumps for action items, decisions, schedule changes
- Maintain `projects/[project-id]/status/current-status.md`
- Track deliverables, dependencies, and blockers
- Escalate issues requiring owner attention
- Coordinate handoffs between technical team members

**Inputs**:
- `projects/[project-id]/communications/*.md` - Email dumps
- `projects/[project-id]/milestones.md`
- `resources/team-calendar.md`

**Outputs**:
- `projects/[project-id]/status/current-status.md` (continuously updated)
- `projects/[project-id]/action-items.md`
- `projects/[project-id]/decisions-log.md`

**Intelligence**:
- Natural language processing of emails
- Automatic status categorization (on-track/at-risk/delayed)
- Sentiment analysis for client satisfaction

**Handoff Trigger**: 
- New milestones → Notifies Milestone Planner
- Technical work required → Notifies Technical Team

---

#### 2.2 Milestone Planner Agent (`@pm-planner`)
**Purpose**: Resource scheduling and workload balancing

**Responsibilities**:
- Review project milestones and decompose into tasks
- Check engineer availability in `resources/team-calendar.md`
- Assign tasks based on skills and capacity
- Update `projects/[project-id]/task-assignments.md`
- Send weekly workload reports
- Flag over-allocation conflicts

**Inputs**:
- `projects/[project-id]/milestones.md`
- `resources/team-calendar.md`
- `resources/engineer-skills.json`

**Outputs**:
- `projects/[project-id]/task-assignments.md`
- `projects/[project-id]/gantt-data.json` (for visualization)
- Weekly updates to team calendars

**Python Capabilities**:
```python
# Scheduling algorithms
- Critical path method (CPM)
- Resource leveling
- Capacity vs. demand analysis
- Buffer time calculations
- Conflict detection and resolution
```

**Handoff Trigger**: Tasks assigned → Notifies GPR Calculation Engineer

---

#### 2.3 GPR Calculation Engineer Agent (`@tech-gpr`)
**Purpose**: Execute ground potential rise calculations using Python

**Responsibilities**:
- Read project specifications from `projects/[project-id]/specs/`
- Execute earthing and grounding calculations per IEEE 80 standards
- Calculate touch voltage, step voltage, ground resistance
- Model soil resistivity effects
- Generate calculation reports with assumptions documented
- Store all calculation data for auditability

**Inputs**:
- `projects/[project-id]/specs/site-data.json`
- `projects/[project-id]/specs/requirements.md`
- `libraries/ieee80_calculator.py` (custom library)

**Outputs**:
- `projects/[project-id]/calculations/gpr-results.json`
- `projects/[project-id]/calculations/gpr-calculation-log.md`
- `projects/[project-id]/calculations/plots/` (matplotlib visualizations)

**Python Capabilities**:
```python
# IEEE 80 Standard Implementation
- Ground resistance calculation (Rd = ρ / (4 × L))
- Touch voltage: Etouch = (ρ × Ig × Ks × Ki) / L
- Step voltage: Estep = (ρ × Ig × Ks × Ki) / L_s
- Soil resistivity modeling (2-layer, multi-layer)
- Grid conductor sizing
- Safety margin calculations
- Monte Carlo sensitivity analysis

# Libraries Used:
- numpy: Matrix operations for complex grid calculations
- scipy: Numerical integration for soil models
- matplotlib: Visualization of voltage gradients
- pandas: Tabular results management
```

**Handoff Trigger**: Calculations complete → Notifies Quality Assurance Agent

---

#### 2.4 Quality Assurance Agent (`@tech-qa`)
**Purpose**: Verify calculations, check assumptions, validate results

**Responsibilities**:
- Review calculation methodology and inputs
- Re-run calculations with independent scripts
- Check results against industry benchmarks
- Verify all safety margins meet standards
- Validate documentation completeness
- Flag discrepancies for GPR Engineer review

**Inputs**:
- `projects/[project-id]/calculations/gpr-results.json`
- `projects/[project-id]/calculations/gpr-calculation-log.md`
- `standards/ieee80-checklist.md`

**Outputs**:
- `projects/[project-id]/qa/qa-report.md`
- `projects/[project-id]/qa/verification-results.json`

**Python Capabilities**:
```python
# Verification methods
- Independent calculation re-run
- Unit test framework for calculation modules
- Statistical comparison (% deviation analysis)
- Boundary condition testing
- Sanity checks (physical feasibility)
```

**Handoff Trigger**: QA passed → Notifies Report Writer Agent

---

#### 2.5 Report Writer Agent (`@tech-report`)
**Purpose**: Transform technical calculations into client-ready professional reports

**Responsibilities**:
- Consume calculation results and QA reports
- Write executive summary for non-technical stakeholders
- Present methodology in clear, structured format
- Include visualizations, tables, and key findings
- Add recommendations and compliance statements
- Format to company standards with proper citations

**Inputs**:
- `projects/[project-id]/calculations/gpr-results.json`
- `projects/[project-id]/qa/qa-report.md`
- `projects/[project-id]/specs/requirements.md`
- `templates/technical-report-template.md`

**Outputs**:
- `projects/[project-id]/reports/final-report-v1.md`
- `projects/[project-id]/reports/final-report-v1.pdf` (export ready)

**Writing Standards**:
- IEEE editorial style
- Clear section hierarchy (Executive Summary → Methodology → Results → Conclusions)
- Professional tone, third-person passive voice
- All figures/tables numbered and captioned
- Complete references section

**Handoff Trigger**: Report complete → Notifies Project Manager for client delivery

---

## Data Flow & Handoff Mechanism

### Handoff Protocol
Agents communicate through **structured markdown files** with YAML frontmatter:

```markdown
---
from_agent: sales-lead
to_agent: sales-budget
timestamp: 2025-11-17T10:30:00Z
status: pending_review
priority: high
---

# Handoff: New Lead Budget Request

Client: Metro Power Authority
Lead ID: LEAD-2025-117
...
```

### State Management
- **Git commits** serve as state transitions
- **Branch strategy**: Each agent works on feature branches
- **Pull requests**: Used for major handoffs requiring owner approval
- **Issues**: Track blockers and exceptions

### File-Based Queues
Agents poll specific folders for work:
- `sales/incoming-emails/` → Lead Intake Agent
- `sales/leads/` → Budget Calculator
- `projects/[id]/communications/` → Project Manager
- `projects/[id]/calculations/` → QA Agent

---

## Folder Structure

```
github-agent/
├── .github/
│   └── copilot-instructions/
│       ├── sales-lead.md
│       ├── sales-budget.md
│       ├── sales-proposal.md
│       ├── pm-coordinator.md
│       ├── pm-planner.md
│       ├── tech-gpr.md
│       ├── tech-qa.md
│       └── tech-report.md
│
├── sales/
│   ├── crm.md                          # Mini CRM database
│   ├── incoming-emails/                # Email dumps from owner
│   ├── leads/                          # Scope drafts per lead
│   ├── budgets/                        # Budget calculations
│   ├── proposals/                      # Final proposals
│   └── templates/                      # Reusable templates
│
├── projects/
│   └── [project-id]/                   # One folder per project
│       ├── communications/             # Email dumps
│       ├── status/
│       │   └── current-status.md      # Living status document
│       ├── milestones.md
│       ├── task-assignments.md
│       ├── specs/
│       │   ├── site-data.json
│       │   └── requirements.md
│       ├── calculations/
│       │   ├── gpr-results.json
│       │   ├── gpr-calculation-log.md
│       │   └── plots/
│       ├── qa/
│       │   ├── qa-report.md
│       │   └── verification-results.json
│       └── reports/
│           └── final-report-v1.md
│
├── resources/
│   ├── team-calendar.md                # Engineer schedules
│   ├── engineer-skills.json            # Skills matrix
│   └── complexity-factors.json         # Project complexity ratings
│
├── config/
│   ├── rates.json                      # Bill rates, cost rates
│   └── company-info.json               # Company details for proposals
│
├── scripts/
│   ├── budget_calculator.py            # Budget calculation engine
│   ├── gpr_calculator.py               # IEEE 80 implementation
│   ├── qa_verification.py              # Independent verification
│   └── report_generator.py             # Markdown to PDF converter
│
├── libraries/
│   └── ieee80_calculator.py            # Core calculation library
│
├── templates/
│   ├── lead-intake-template.md
│   ├── proposal-template.md
│   └── technical-report-template.md
│
├── standards/
│   └── ieee80-checklist.md             # Compliance checklist
│
└── ARCHITECTURE.md                     # This document
```

---

## Agent Invocation & Context

### Using GitHub Copilot Agent Sessions

Each agent is invoked with specialized instructions:

```bash
# Invoke specific agent in GitHub Copilot Chat
@sales-lead process new leads in sales/incoming-emails/

# Agent reads its instruction file automatically
# .github/agents/sales-lead.agent.md
```

### Context Awareness
Agents are instructed to:
1. **Read their domain folders** first
2. **Check for handoff files** from upstream agents
3. **Execute work** using Python scripts or markdown generation
4. **Write output** to designated folders
5. **Create handoff files** for downstream agents
6. **Commit changes** with descriptive messages

---

## Python Execution Environment

### Virtual Environment Setup
```bash
# Already configured
.venv/ with Python 3.11.9
```

### Key Libraries
```python
# Core calculation libraries
numpy==1.26.0          # Numerical operations
scipy==1.11.0          # Advanced math
pandas==2.1.0          # Data management
matplotlib==3.8.0      # Visualization

# Engineering libraries
sympy==1.12            # Symbolic math
uncertainties==3.1.7   # Error propagation

# Reporting libraries
jinja2==3.1.2          # Template rendering
markdown==3.5          # Markdown processing
weasyprint==60.0       # PDF generation

# Utilities
pyyaml==6.0.1          # Config parsing
jsonschema==4.19.0     # Validation
```

---

## Example Workflow: From Lead to Delivery

### Stage 1: Sales (Days 1-3)
1. Owner dumps client email to `sales/incoming-emails/metro-power-2025.md`
2. **@sales-lead** processes email
   - Creates `sales/crm.md` entry
   - Writes `sales/leads/metro-power-scope-draft.md`
3. **@sales-budget** calculates budget
   - Runs `scripts/budget_calculator.py`
   - Outputs `sales/budgets/metro-power-budget.md`
4. **@sales-proposal** combines documents
   - Generates `sales/proposals/metro-power-proposal-v1.md`
5. Owner reviews proposal, sends to client

### Stage 2: Project Kickoff (Week 1)
6. Client accepts, owner dumps email to `projects/PROJ-001/communications/`
7. **@pm-coordinator** reads email
   - Creates `projects/PROJ-001/status/current-status.md`
   - Logs decision in `decisions-log.md`
8. **@pm-planner** creates task plan
   - Checks `resources/team-calendar.md`
   - Assigns tasks in `task-assignments.md`

### Stage 3: Technical Execution (Weeks 2-3)
9. **@tech-gpr** executes calculations
   - Reads `projects/PROJ-001/specs/site-data.json`
   - Runs `scripts/gpr_calculator.py`
   - Outputs `calculations/gpr-results.json`
10. **@tech-qa** verifies results
    - Re-runs calculations independently
    - Writes `qa/qa-report.md`
11. **@tech-report** writes final report
    - Combines all data
    - Generates `reports/final-report-v1.md`

### Stage 4: Delivery (Week 4)
12. **@pm-coordinator** notifies owner report is ready
13. Owner reviews, approves, delivers to client

---

## Benefits of This Architecture

### For the Owner
- **Automation of repetitive tasks**: CRM updates, budget calculations
- **Consistency**: Every proposal/report follows same high standard
- **Auditability**: Full Git history of all decisions
- **Scalability**: Handle more leads without hiring

### For Agents
- **Clear responsibilities**: No ambiguity in roles
- **Structured inputs/outputs**: Easy to process
- **Python execution**: Complex calculations automated
- **Contextual awareness**: Each agent knows its domain

### For Clients
- **Faster response times**: Proposals in days, not weeks
- **Professional quality**: Consistent formatting and completeness
- **Transparency**: Clear methodology and documentation

---

## Risk Mitigation

### Owner Oversight Points
1. **Proposal Review**: Before sending to client (mandatory)
2. **Budget Approval**: For projects >$50k (configurable)
3. **Calculation Sign-off**: QA flags reviewed by owner
4. **Final Report Release**: Owner approves before delivery

### Error Handling
- Agents log all decisions and assumptions
- QA agent catches calculation errors
- Project Manager escalates blockers to owner
- All critical handoffs require owner approval (via PR)

---

## Future Enhancements

### Phase 2 Capabilities
- **Integration with email client**: Auto-import emails
- **Calendar sync**: Real-time engineer availability
- **Client portal**: Direct communication channel
- **Invoice generation**: Automated billing from timesheet data

### Phase 3 AI Capabilities
- **Predictive lead scoring**: ML model for conversion probability
- **Resource optimization**: AI-driven task allocation
- **Anomaly detection**: Flag unusual calculation results
- **Natural language querying**: "What's the status of Metro Power project?"

---

## Getting Started

### Immediate Next Steps
1. ✅ Create folder structure
2. ✅ Write agent instruction files
3. ✅ Generate sample data (emails, calendars)
4. ✅ Test individual agents in isolation
5. ✅ Test end-to-end workflow with sample project

### Success Criteria
- Lead processed to proposal in <24 hours
- Budget accuracy within 5% of manual calculation
- Calculation results pass QA 100% of time
- Report quality indistinguishable from owner's work

---

## Conclusion

This architecture transforms Power Grids of the Future from a one-person consultancy into a **human-AI collaborative enterprise**. The owner focuses on high-value activities (client relationships, technical oversight, strategic growth) while AI agents handle operational execution.

The system is:
- **Modular**: Agents can be updated independently
- **Transparent**: All work tracked in Git
- **Scalable**: Add more agents or projects without redesign
- **Practical**: Uses existing tools (GitHub, markdown, Python)

**The future of solo consultancy is here.**

---

*Document Version: 1.0*  
*Last Updated: 2025-11-17*  
*Owner: Power Grids of the Future*
