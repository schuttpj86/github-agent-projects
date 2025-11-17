# GitHub Agent Delegation & Handoff Mechanism

## Overview

This document explains how GitHub Copilot agents work together through **delegation** and **handoff** in the Power Grids of the Future system.

---

## Core Concepts

### 1. Agent Specialization
Each agent has a **narrow, well-defined domain**:
- `@sales-lead` → Lead qualification
- `@sales-budget` → Budget calculation
- `@sales-proposal` → Proposal writing
- `@pm-coordinator` → Project status tracking
- `@pm-planner` → Resource scheduling
- `@tech-gpr` → Engineering calculations
- `@tech-qa` → Quality verification
- `@tech-report` → Report writing

**Why this matters**: Specialized instructions make each agent an "expert" in its domain, improving quality and reducing errors.

---

### 2. File-Based Communication

Agents communicate through **structured markdown files** with YAML frontmatter:

```yaml
---
from_agent: sales-lead
to_agent: sales-budget
timestamp: 2025-11-17T10:30:00Z
status: ready_for_budget
lead_id: LEAD-2025-117
priority: high
---

# Handoff: Budget Request for Metro Power Authority

[Content here...]
```

**Why files?**
- ✅ Human-readable (you can see exactly what agents are doing)
- ✅ Git-trackable (full audit trail)
- ✅ Debuggable (if something breaks, read the file)
- ✅ No complex APIs or databases required

---

### 3. Folder-Based Work Queues

Each agent **monitors specific folders** for incoming work:

| Agent | Monitors Folder | Looks For |
|-------|----------------|-----------|
| `@sales-lead` | `sales/incoming-emails/` | New email dumps |
| `@sales-budget` | `sales/leads/` | Scope drafts with `next_agent: sales-budget` |
| `@sales-proposal` | `sales/budgets/` | Budget files with `next_agent: sales-proposal` |
| `@pm-coordinator` | `projects/*/communications/` | New email dumps |
| `@pm-planner` | `projects/*/milestones.md` | Project plans |
| `@tech-gpr` | `projects/*/specs/` | Technical specifications |
| `@tech-qa` | `projects/*/calculations/` | Calculation results with `status: ready_for_qa` |
| `@tech-report` | `projects/*/qa/` | QA reports with `status: qa_approved` |

**Polling Pattern**:
```markdown
1. Agent checks folder for new files
2. If found, reads file content
3. Performs work
4. Writes output to designated folder
5. Updates frontmatter to trigger next agent
```

---

### 4. Handoff Protocol

**Handoff = Passing work from one agent to another**

#### Example: Lead → Budget → Proposal

**Step 1: Owner dumps email**
```
File: sales/incoming-emails/metro-power-inquiry.md
```

**Step 2: @sales-lead processes**
```
Reads: sales/incoming-emails/metro-power-inquiry.md
Creates: sales/leads/metro-power-scope-draft.md
Creates: sales/crm.md (updates)

Frontmatter in scope-draft.md:
---
next_agent: sales-budget
status: ready_for_budget
---
```

**Step 3: @sales-budget calculates**
```
Reads: sales/leads/metro-power-scope-draft.md
Executes: scripts/budget_calculator.py
Creates: sales/budgets/metro-power-budget.json
Creates: sales/budgets/metro-power-budget.md

Frontmatter in budget.md:
---
next_agent: sales-proposal
status: ready_for_proposal
---
```

**Step 4: @sales-proposal writes**
```
Reads: sales/leads/metro-power-scope-draft.md
Reads: sales/budgets/metro-power-budget.md
Creates: sales/proposals/metro-power-proposal-v1.md

Frontmatter:
---
next_agent: owner
status: ready_for_owner_review
owner_action_required: true
---
```

**Step 5: Owner reviews and sends**
```
Owner reads proposal, approves, sends to client
```

---

### 5. State Transitions

**States** are tracked in file frontmatter:

```yaml
# Lead Processing States
- new → processed (by @sales-lead)
- processed → scope_draft (by @sales-lead)
- scope_draft → ready_for_budget (handoff to @sales-budget)
- ready_for_budget → budget_complete (by @sales-budget)
- budget_complete → ready_for_proposal (handoff to @sales-proposal)
- ready_for_proposal → proposal_draft (by @sales-proposal)
- proposal_draft → ready_for_owner_review (handoff to owner)
- ready_for_owner_review → sent_to_client (by owner)
- sent_to_client → won | lost (by owner)
```

**State Machine Visualization**:
```
[Email] → @sales-lead → [Scope] → @sales-budget → [Budget] → @sales-proposal → [Proposal] → Owner → Client
```

---

### 6. Git as Coordination Layer

**Every agent action = Git commit**:

```bash
# @sales-lead creates scope draft
git add sales/leads/metro-power-scope-draft.md
git commit -m "@sales-lead: Created scope draft for Metro Power (LEAD-2025-117)"

# @sales-budget calculates budget
git add sales/budgets/metro-power-budget.*
git commit -m "@sales-budget: Calculated budget $42.5k for Metro Power (LEAD-2025-117)"

# @sales-proposal writes proposal
git add sales/proposals/metro-power-proposal-v1.md
git commit -m "@sales-proposal: Generated proposal for Metro Power (LEAD-2025-117)"
```

**Benefits**:
- ✅ Full audit trail (who did what, when)
- ✅ Rollback capability (undo mistakes)
- ✅ Version history (compare proposal v1 vs v2)
- ✅ Blame tracking (which agent created this file?)

---

### 7. Pull Requests for Critical Handoffs

For **major decisions** requiring owner approval, use pull requests:

```bash
# @sales-proposal creates PR for owner review
git checkout -b proposal-metro-power
git add sales/proposals/metro-power-proposal-v1.md
git commit -m "Proposal ready for owner review"
git push origin proposal-metro-power
# Create PR: "Proposal for Metro Power - $42.5k - Owner Review Required"
```

**Owner reviews PR**:
- Reads proposal in GitHub UI
- Adds comments if changes needed
- Approves and merges when satisfied
- `@sales-proposal` can update based on feedback

---

### 8. Escalation Mechanism

Agents escalate to owner when:
- ❌ Uncertainty (don't know how to proceed)
- ❌ Errors (calculation failed, data missing)
- ❌ Policy decisions (scope change, pricing negotiation)
- ❌ Safety concerns (compliance issue, technical risk)

**Escalation Format**:
```yaml
---
escalation: true
escalation_priority: high
escalation_reason: "Client requesting scope change - needs pricing approval"
owner_action_required: true
---

# ESCALATION: Metro Power Scope Change Request

**From**: @pm-coordinator
**Date**: 2025-11-20
**Project**: PROJ-001

## Issue
Client emailed requesting 3D electromagnetic modeling (not in original scope).

## Impact
- Additional work: ~20 hours senior engineer time
- Budget increase: ~$8,000
- Timeline impact: +1 week

## Recommendation
Propose as paid add-on per original proposal terms.

## Action Needed
Owner to discuss with client on next Thursday call.
```

---

### 9. Context Awareness

Agents know their **inputs** and **outputs**:

#### @sales-lead
- **Inputs**: 
  - `sales/incoming-emails/*.md` (email dumps)
  - `sales/templates/lead-intake-template.md`
- **Outputs**:
  - `sales/crm.md` (updates)
  - `sales/leads/[client]-scope-draft.md` (creates)

#### @sales-budget
- **Inputs**:
  - `sales/leads/[client]-scope-draft.md`
  - `config/rates.json`
  - `resources/complexity-factors.json`
- **Outputs**:
  - `sales/budgets/[client]-budget.json`
  - `sales/budgets/[client]-budget.md`

#### @tech-gpr
- **Inputs**:
  - `projects/[id]/specs/site-data.json`
  - `projects/[id]/specs/requirements.md`
- **Executes**:
  - `scripts/gpr_calculator.py` (Python calculations)
- **Outputs**:
  - `projects/[id]/calculations/gpr-results.json`
  - `projects/[id]/calculations/gpr-calculation-log.md`
  - `projects/[id]/calculations/plots/*.png`

**This is defined in each agent's `.github/agents/[agent-name].agent.md` file.**

---

### 10. Python Execution

Some agents execute **Python scripts** for calculations:

```python
# @sales-budget invokes Python
import subprocess

result = subprocess.run([
    'C:/AIprojects/github-agent/.venv/Scripts/python.exe',
    'scripts/budget_calculator.py',
    '--lead-id', 'LEAD-2025-117',
    '--senior-hours', '60',
    '--junior-hours', '80',
    '--complexity', '1.35',
    '--output', 'json'
], capture_output=True, text=True)

budget_data = json.loads(result.stdout)
```

**Python provides**:
- ✅ Complex calculations (IEEE 80 formulas)
- ✅ Data validation
- ✅ Repeatability (same inputs → same outputs)
- ✅ Testing capability (unit tests for calculations)

---

### 11. Parallel vs Sequential Handoffs

**Sequential Handoff** (most common):
```
A → B → C → D
```
Example: Lead → Budget → Proposal → Owner

**Parallel Handoff** (rare):
```
      → B1 (Budget Calc)
A →  → B2 (Tech Feasibility)  → C (merge)
      → B3 (Risk Assessment)
```
Example: Multiple engineers reviewing same document simultaneously

**Our system uses mostly sequential** to keep things simple and traceable.

---

### 12. Error Handling

**What if agent fails?**

**Example: @tech-qa rejects calculations**

```yaml
---
from_agent: tech-qa
to_agent: tech-gpr
status: qa_failed
issues_found: 2
return_reason: "Ground resistance discrepancy >15%"
---

# QA FAILURE: PROJ-001 Calculations

**Date**: 2025-11-20
**Reviewer**: @tech-qa

## Issues Found

### Issue 1: Ground Resistance Discrepancy
- Your result: 0.42 Ω
- QA result: 0.68 Ω
- Difference: 62% (exceeds 10% tolerance)

**Suspected Cause**: Conductor length may be incorrect (verify 2580m vs 1600m)

### Issue 2: Safety Factor Below Threshold
- Touch voltage SF: 1.42 (requires ≥1.5)

## Actions Required
1. Re-check conductor length input
2. Re-run calculations
3. Resubmit for QA review

## Status
Returned to @tech-gpr for corrections.
```

**@tech-gpr fixes and resubmits**:
```yaml
---
status: ready_for_qa
qa_resubmission: true
fixes_applied: "Corrected conductor length, recalculated"
---
```

---

### 13. Owner Gates

**Owner review required at**:
1. **Proposal before sending** (all proposals reviewed)
2. **Budget >$50k** (large project approval)
3. **Scope changes** (any deviation from original)
4. **Final report** (PE stamp required)
5. **Escalations** (agent can't proceed)

**Gate Format**:
```yaml
---
owner_review_required: true
review_type: proposal_approval
review_deadline: 2025-11-18
blocking: true  # Work stops until owner reviews
---
```

---

### 14. Success Metrics

**How to measure agent effectiveness**:

| Agent | KPI | Target |
|-------|-----|--------|
| @sales-lead | Lead processing time | <24 hours |
| @sales-budget | Budget accuracy | ±5% of actual |
| @sales-proposal | Win rate contribution | >65% proposal-to-project |
| @pm-coordinator | Status update frequency | Within 2 hours of new email |
| @pm-planner | Task estimate accuracy | ±15% of actual hours |
| @tech-gpr | Calculation correctness | 100% pass QA |
| @tech-qa | Error catch rate | 100% of calculation errors |
| @tech-report | Client satisfaction | Zero revisions requested |

---

### 15. Example: Full End-to-End Flow

**Complete workflow from lead to delivery**:

```
Day 1:
  Owner dumps email → sales/incoming-emails/metro-power.md
  
Day 1 (2 hours later):
  @sales-lead processes
    → Creates: sales/crm.md (new lead entry)
    → Creates: sales/leads/metro-power-scope-draft.md
    → Frontmatter: next_agent=sales-budget

Day 1 (4 hours later):
  @sales-budget calculates
    → Executes: scripts/budget_calculator.py
    → Creates: sales/budgets/metro-power-budget.md
    → Frontmatter: next_agent=sales-proposal

Day 2:
  @sales-proposal writes
    → Reads: scope + budget
    → Creates: sales/proposals/metro-power-proposal-v1.md
    → Frontmatter: owner_review_required=true

Day 2 (owner reviews):
  Owner reads proposal, approves, sends to client

Day 5 (client accepts):
  Owner dumps acceptance email → projects/PROJ-001/communications/

Day 5 (2 hours later):
  @pm-coordinator processes
    → Creates: projects/PROJ-001/status/current-status.md
    → Creates: projects/PROJ-001/action-items.md

Day 6:
  @pm-planner schedules
    → Creates: projects/PROJ-001/task-assignments.md
    → Assigns: Alex (60hrs) + Jennifer (80hrs)

Week 2-3:
  @tech-gpr calculates
    → Executes: scripts/gpr_calculator.py
    → Creates: projects/PROJ-001/calculations/gpr-results.json
    → Frontmatter: next_agent=tech-qa

Week 3:
  @tech-qa verifies
    → Executes: scripts/qa_verification.py
    → Creates: projects/PROJ-001/qa/qa-report.md
    → Result: PASS
    → Frontmatter: next_agent=tech-report

Week 4:
  @tech-report writes
    → Reads: calculations + QA report
    → Creates: projects/PROJ-001/reports/final-report-v1.md
    → Frontmatter: owner_review_required=true

Week 4 (owner reviews):
  Owner reads report, adds PE stamp, delivers to client

Week 5:
  Client receives report, project complete
```

**Total time: Lead to delivery in 4 weeks** (vs 8-12 weeks traditional)

---

## Key Takeaways

### 1. **Agents are specialists**
Each does ONE thing extremely well.

### 2. **Files are the interface**
Structured markdown with YAML frontmatter.

### 3. **Folders are work queues**
Agents poll designated folders for incoming work.

### 4. **Frontmatter triggers handoffs**
`next_agent: sales-budget` tells system who's next.

### 5. **Git provides audit trail**
Every action is committed and traceable.

### 6. **Owner controls critical gates**
Proposals, final reports, scope changes require approval.

### 7. **Python handles complexity**
Calculations, optimization, analysis via scripts.

### 8. **Escalations prevent blocking**
If agent stuck, owner intervenes.

### 9. **QA prevents errors**
Independent verification before client sees anything.

### 10. **System is transparent**
You can read every file and see exactly what agents did.

---

## How to Use This System

### As the Owner:
1. **Dump emails** to designated folders (incoming-emails, communications)
2. **Review agent outputs** at designated gates (proposals, reports)
3. **Approve or reject** handoffs via frontmatter updates
4. **Escalate when needed** by invoking agents with specific questions

### To Invoke Agents:
```bash
# In GitHub Copilot Chat
@sales-lead process new leads
@sales-budget calculate budget for LEAD-2025-117
@pm-coordinator update status for PROJ-001
@tech-gpr run calculations for PROJ-001
```

### To Monitor Progress:
```bash
# Check CRM
cat sales/crm.md

# Check project status
cat projects/PROJ-001/status/current-status.md

# Check task assignments
cat projects/PROJ-001/task-assignments.md
```

---

## Future Enhancements

### Phase 2:
- **Webhooks**: Email → auto-trigger @sales-lead
- **Dashboards**: Visual project status (read from markdown)
- **Notifications**: Slack alerts when owner review needed

### Phase 3:
- **Auto-approval**: Low-risk handoffs don't need owner (e.g., lead → budget)
- **Parallel workflows**: Multiple projects running simultaneously
- **Learning**: Agents improve over time based on historical data

---

**The future of consultancy is collaborative AI agents. Welcome to Power Grids of the Future.**
