# Power Grids of the Future - Repository Instructions

This repository contains an AI-augmented workflow system for an electrical engineering consultancy specializing in substation grounding and earthing analysis per IEEE Standard 80.

## About This Project

Power Grids of the Future is a one-person consultancy that uses specialized GitHub Copilot agents to automate sales, project management, and technical delivery workflows. The system handles everything from lead intake through final report delivery with PE stamp.

## Repository Structure

```
.github/agents/          → Custom agent profiles (8 specialized agents)
sales/                   → CRM, leads, budgets, proposals
projects/               → Active project folders (PROJ-NNN)
resources/              → Team schedules, skills, complexity factors
config/                 → Company info, rates, payment terms
scripts/                → Python calculation engines (budget, GPR)
libraries/              → Reusable calculation modules
templates/              → Document templates
standards/              → IEEE 80 checklists and references
```

## Development Workflow

### Build & Test
```powershell
# Activate Python environment
.\.venv\Scripts\Activate.ps1

# Run budget calculator
python scripts\budget_calculator.py --help

# Run GPR calculations
python scripts\gpr_calculator.py --help

# Run tests (when implemented)
python -m pytest tests/
```

### Python Environment
- **Version**: Python 3.11.9
- **Location**: `.venv/` (virtual environment)
- **Key Dependencies**: numpy, scipy, pandas, matplotlib, sympy, uncertainties

### Code Standards

#### Python
- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Include docstrings for all functions (Google style)
- Use f-strings for string formatting
- Prefer pathlib over os.path for file operations
- Keep functions focused (single responsibility principle)
- Write unit tests for all calculation logic

**Example**:
```python
def calculate_ground_resistance(
    soil_resistivity_top: float,
    soil_resistivity_bottom: float,
    conductor_length: float,
    grid_area: float
) -> float:
    """Calculate ground resistance using Schwarz two-layer equation.
    
    Args:
        soil_resistivity_top: Top layer resistivity in ohm-meters
        soil_resistivity_bottom: Bottom layer resistivity in ohm-meters
        conductor_length: Total conductor length in meters
        grid_area: Grid area in square meters
        
    Returns:
        Ground resistance in ohms
        
    Raises:
        ValueError: If any input parameter is negative
    """
    # Implementation here
```

#### Markdown
- Use ATX-style headers (`#`, `##`, `###`)
- Include YAML frontmatter for all agent-processed files
- Use tables for structured data
- Include code fences with language tags
- Use emoji sparingly (✅ ❌ 🟡 for status only)

#### File Naming
- **Agents**: `kebab-case.agent.md` (e.g., `sales-lead.agent.md`)
- **Python**: `snake_case.py` (e.g., `budget_calculator.py`)
- **Projects**: `PROJ-NNN` (e.g., `PROJ-001`)
- **Leads**: `LEAD-YYYY-NNN` (e.g., `LEAD-2025-117`)
- **Proposals**: `PROP-YYYY-NNN` (e.g., `PROP-2025-045`)

### Git Workflow

#### Commit Messages
Use agent attribution format:
```
@agent-name: Brief description of what was done (Entity ID)

Examples:
@sales-lead: Created scope draft for Metro Power (LEAD-2025-117)
@sales-budget: Calculated budget $42.5k for Metro Power (LEAD-2025-117)
@tech-gpr: Completed GPR calculations for PROJ-001 (compliant)
@tech-qa: QA APPROVED for PROJ-001 - all verifications passed
```

#### Branch Strategy
- `main`: Production-ready, client-facing content
- `feature/[agent]-[description]`: Agent working branches
- `escalation/[issue]`: Owner intervention branches

#### Pull Request Format
When agents create PRs for owner review:
```markdown
## Agent: @sales-proposal
## Lead ID: LEAD-2025-117
## Action Required: Owner review proposal before sending to client

### Summary
Generated proposal for Metro Power Authority - $42,011 - 10 week timeline

### Checklist
- [x] Budget matches approved estimate
- [x] All deliverables clearly scoped
- [x] Payment schedule follows company policy
- [x] Professional formatting applied
- [ ] Owner approval needed

### Files Changed
- `sales/proposals/metro-power-proposal-v1.md` (new)
- `sales/crm.md` (updated with proposal sent date)
```

## Agent Coordination

### Agent Invocation
Use `@agent-name` in GitHub Copilot Chat or assign issues to agents:
```
@sales-lead process new leads in sales/incoming-emails/
@sales-budget calculate budget for LEAD-2025-117
@pm-coordinator update status for PROJ-001
@tech-gpr run calculations for PROJ-001
```

### File-Based Handoffs
Agents coordinate through YAML frontmatter:
```yaml
---
from_agent: sales-budget
to_agent: sales-proposal
status: ready_for_proposal
next_agent: sales-proposal
owner_action_required: false
---
```

### Escalation Protocol
If any agent encounters issues requiring owner intervention:
1. Create escalation file in appropriate folder
2. Set `owner_action_required: true` in frontmatter
3. Set escalation priority (high/medium/low)
4. Provide clear action items for owner

## Technical Standards

### IEEE 80 Compliance
All grounding calculations must follow IEEE Standard 80-2013:
- Use Schwarz equations for two-layer soil models
- Include crushed rock surface layer (3000 Ω·m typical)
- Calculate both touch and step voltages
- Verify safety factors ≥1.5
- Document all assumptions clearly

### Calculation Validation
- All calculations must pass independent QA review
- Use consistent SI units throughout
- Round appropriately (ground resistance to 0.001 Ω, voltages to 1 V)
- Generate plots for visual verification
- Compare to hand calculations or simplified formulas for sanity checks

### Report Quality
- Executive summary for non-technical audiences
- Complete methodology section with equations
- Results presented in tables
- Compliance matrix clearly showing pass/fail
- Professional recommendations section
- PE certification and stamp placeholder

## Data Management

### Input Data Sources
- **Soil resistivity**: Client test reports (Wenner 4-pin method)
- **Fault current**: Client fault studies (symmetrical RMS)
- **Site data**: Survey drawings, as-built plans
- **Standards**: IEEE 80-2013, NESC, local codes

### Output Deliverables
- **Proposals**: Markdown → PDF conversion for client delivery
- **Reports**: Markdown with LaTeX math → PDF with PE stamp
- **Calculations**: JSON (machine-readable) + MD (human-readable)
- **Plots**: PNG files (300 DPI minimum for reports)

### Version Control
- Track all calculation versions
- Maintain audit trail of QA approvals
- Archive completed projects (don't delete)
- Keep proposals and reports together

## Project Lifecycle

### Phase 1: Sales (Weeks 0-2)
1. **Lead intake** → `@sales-lead` processes emails
2. **Budget calc** → `@sales-budget` runs Python script
3. **Proposal** → `@sales-proposal` writes client-ready doc
4. **Owner review** → Approve and send
5. **Client accepts** → Move to delivery

### Phase 2: Kickoff (Week 1)
1. **Project setup** → `@pm-planner` creates plan
2. **Data collection** → Client provides soil/fault data
3. **Validation** → Engineers verify data completeness

### Phase 3: Technical (Weeks 2-7)
1. **Calculations** → `@tech-gpr` runs IEEE 80 analysis
2. **QA review** → `@tech-qa` verifies independently
3. **Grid design** → Recommendations for construction

### Phase 4: Reporting (Weeks 8-10)
1. **Report draft** → `@tech-report` writes professional doc
2. **PE review** → Owner reviews and stamps
3. **Client delivery** → Final PDF sent

### Phase 5: Closeout
1. **Payment** → Final invoice sent
2. **Archive** → Project moved to archives/
3. **Lessons learned** → Update complexity factors if needed

## Owner Responsibilities

The owner (you) must handle:
- **Email processing**: Dump client emails to appropriate folders
- **Decision gates**: Approve proposals, scope changes, final reports
- **PE stamp**: Review and stamp all technical reports
- **Client calls**: Weekly check-ins, relationship management
- **Escalations**: Resolve issues agents can't handle
- **System tuning**: Update agent instructions based on learnings

## Best Practices

### For Efficiency
- Batch similar work (process all leads together)
- Use templates consistently
- Leverage Python for all calculations (no manual spreadsheets)
- Maintain clean folder structure
- Archive completed projects promptly

### For Quality
- Never skip QA review
- Document all assumptions
- Use version control religiously
- Keep client communications professional
- Maintain audit trail for regulatory compliance

### For Client Satisfaction
- Weekly status updates (even if "no changes")
- Respond to emails within 24 hours
- Deliver on promised dates
- Explain technical concepts clearly
- Proactively flag risks early

## Troubleshooting

### Python Environment Issues
```powershell
# Recreate venv if corrupted
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Agent Not Responding
1. Check if agent file exists in `.github/agents/`
2. Verify YAML frontmatter is valid
3. Ensure `next_agent` field matches agent name exactly
4. Check file is in agent's monitored folder

### Calculation Errors
1. Verify input data units (SI units required)
2. Check for missing parameters in JSON
3. Review QA report for specific issues
3. Compare to hand calculation for simple cases

## Additional Resources

- **ARCHITECTURE.md**: Complete system design
- **AGENT-HANDOFF-GUIDE.md**: Detailed agent coordination explanation
- **README.md**: Project overview and quick start
- **IEEE 80-2013**: Official standard (purchase from IEEE)

---

**Remember**: This system automates routine work so you can focus on engineering judgment, client relationships, and growing the business. Let the agents handle the paperwork!
