# Proposal Tracker Reference

## Overview

Every proposal project has a `proposal-tracker.json` file that:
1. Tracks progress through all stages
2. Stores approved scope elements (the "PRD")
3. Enables resuming work in a new session
4. Provides audit trail of approvals

## File Location

```
projects/PROP-XXX-ClientName/proposal-tracker.json
```

## Tracker Structure

```json
{
  "meta": {
    "project_id": "PROP-004-PeakGen",
    "project_name": "Peak Gen NESO LT29 Stability Studies",
    "client": "Peak Gen",
    "created": "2026-03-19T10:00:00Z",
    "last_updated": "2026-03-19T14:30:00Z",
    "status": "in_progress"
  },

  "stages": {
    "setup": {"status": "completed", "completed_at": "2026-03-19T10:05:00Z"},
    "inputs": {"status": "completed", "completed_at": "2026-03-19T10:15:00Z"},
    "extraction": {"status": "completed", "completed_at": "2026-03-19T10:45:00Z"},
    "drafting": {"status": "in_progress", "current_section": 3},
    "template": {"status": "pending"},
    "refinement": {"status": "pending"},
    "budget": {"status": "pending"}
  },

  "inputs": {
    "template": "DNV Proposal Template.docx",
    "tender_docs": [
      {"file": "rfp/05 LT2029 Stability Service Technical Specification V3.pdf", "pages": 24},
      {"file": "rfp/05.2 LT2029 Stability Feasibility Study Requirements V5.pdf", "pages": 18},
      {"file": "rfp/2. LT2029 Stability Technical Proforma V4.xlsx", "sheets": 5}
    ],
    "context": "initial proposal.md",
    "approved_at": "2026-03-19T10:15:00Z"
  },

  "prd": {
    "approved": true,
    "approved_at": "2026-03-19T10:45:00Z",
    "summary": "Stability feasibility studies for 4 rotating stabilizer sites for NESO LT29 tender",

    "client_objective": "Submit compliant tender for NESO LT2029 Long-Term Stability Services",
    "dnv_scope": "Perform stability studies, create models, complete NESO proformas",

    "key_parameters": {
      "sites": ["Landulph", "Indian Queens", "Aberthaw", "Wilton"],
      "technology": "GE RS4 Rotating Stabilizers",
      "configurations": ["4x RS4", "8x RS4"],
      "model_outputs": 10,
      "deadline": "Mid to late April 2026"
    },

    "deliverables": [
      "Stability Feasibility Study Reports (per site)",
      "Completed NESO Technical Proforma Tab 4",
      "PSCAD/PSS®E Model Files"
    ],

    "standards": [
      "NESO LT2029 Stability Service Technical Specification V3",
      "NESO LT2029 Stability Feasibility Study Requirements V5",
      "Grid Code CC.6.3.15"
    ],

    "exclusions": [
      "Physical site visits",
      "NESO submission process",
      "Commercial negotiations with NESO"
    ],

    "uncertainties": [
      {"item": "Final site count", "note": "May reduce from 10 to fewer model outputs"},
      {"item": "Transformer specifications", "note": "LV voltage TBD by developer"}
    ]
  },

  "sections": {
    "1_introduction": {
      "status": "approved",
      "draft_file": "working/section1-introduction.md",
      "approved_at": "2026-03-19T11:00:00Z",
      "revisions": 1
    },
    "2_solution": {
      "status": "approved",
      "draft_file": "working/section2-solution.md",
      "approved_at": "2026-03-19T11:30:00Z",
      "revisions": 2
    },
    "3_scope": {
      "status": "in_progress",
      "draft_file": "working/section3-scope.md",
      "revisions": 0
    },
    "4_schedule": {"status": "pending"},
    "5_compensation": {"status": "pending"},
    "6_organisation": {"status": "pending"},
    "7_contractual": {"status": "pending"},
    "8_acceptance": {"status": "pending"}
  },

  "budget": {
    "status": "pending",
    "tasks_file": null,
    "hours_approved": false,
    "total_estimate": null,
    "breakdown_file": null
  },

  "output": {
    "proposal_file": null,
    "final_approved": false,
    "final_approved_at": null
  },

  "log": [
    {"timestamp": "2026-03-19T10:00:00Z", "action": "project_created", "note": "Initial setup"},
    {"timestamp": "2026-03-19T10:15:00Z", "action": "inputs_approved", "note": "User confirmed 8 tender documents"},
    {"timestamp": "2026-03-19T10:45:00Z", "action": "prd_approved", "note": "Requirements extraction approved"},
    {"timestamp": "2026-03-19T11:00:00Z", "action": "section_approved", "section": "1_introduction"},
    {"timestamp": "2026-03-19T11:30:00Z", "action": "section_approved", "section": "2_solution", "note": "Revised deliverables list"}
  ]
}
```

## Key Sections Explained

### meta
Project identification and overall status.
- `status`: "not_started" | "in_progress" | "completed" | "on_hold"

### stages
High-level progress through the 7 workflow stages.
- `status`: "pending" | "in_progress" | "completed" | "skipped"

### inputs
Record of all source documents and when they were confirmed.

### prd (Product Requirements Document)
**This is the "contract" for the proposal.** Once `approved: true`, this defines:
- What the client wants
- What DNV will deliver
- Key technical parameters
- Explicit exclusions
- Known uncertainties

The PRD is populated from Stage 2 (extraction) and locked after user approval.

### sections
Per-section tracking:
- `status`: "pending" | "in_progress" | "approved" | "skipped"
- `revisions`: How many times re-drafted before approval
- Points to the saved markdown file

### budget
Tracks budget generation (Stage 6):
- Hours approval separate from final budget approval
- Links to generated files

### log
Chronological audit trail of all approvals and major actions.

## Workflow Integration

### At Session Start

1. Check if `proposal-tracker.json` exists
2. If yes, load it and report current state:
   ```
   RESUMING PROJECT: PROP-004-PeakGen
   ===================================
   Status: in_progress
   Current stage: drafting (Section 3: Scope of Work)

   Completed:
   ✓ Stage 0: Setup
   ✓ Stage 1: Inputs (8 documents)
   ✓ Stage 2: PRD approved
   ✓ Section 1: Introduction
   ✓ Section 2: Solution

   Next: Continue drafting Section 3 (Scope of Work)

   Shall I continue from where we left off?
   ```
3. If no, create new tracker

### After Each Checkpoint

Update the tracker immediately after user approval:

```python
# Pseudocode
tracker["sections"]["3_scope"]["status"] = "approved"
tracker["sections"]["3_scope"]["approved_at"] = now()
tracker["stages"]["drafting"]["current_section"] = 4
tracker["log"].append({
    "timestamp": now(),
    "action": "section_approved",
    "section": "3_scope"
})
save_tracker()
```

### PRD Approval

The PRD section is special - it defines the scope contract:

1. After extraction (Stage 2), populate `prd` section
2. Present to user for approval
3. Once approved, set `prd.approved = true`
4. The PRD becomes the reference for all subsequent sections
5. If scope changes later, update PRD and log the change

## Status Values

| Field | Values |
|-------|--------|
| `meta.status` | not_started, in_progress, completed, on_hold |
| `stages.*.status` | pending, in_progress, completed, skipped |
| `sections.*.status` | pending, in_progress, approved, skipped |
| `budget.status` | pending, hours_drafted, hours_approved, generated, approved |

## Resume Scenarios

### Scenario 1: Continuing Section Drafting
```json
"stages": {"drafting": {"status": "in_progress", "current_section": 3}}
```
→ Resume drafting Section 3

### Scenario 2: All Sections Done, Template Not Started
```json
"stages": {"drafting": {"status": "completed"}, "template": {"status": "pending"}}
```
→ Ask user if ready to integrate into template

### Scenario 3: Template Done, Budget Pending
```json
"stages": {"template": {"status": "completed"}, "budget": {"status": "pending"}}
```
→ Ask if user wants to proceed to budget generation

### Scenario 4: Everything Done Except Final Approval
```json
"output": {"proposal_file": "output/DNV Proposal PeakGen.docx", "final_approved": false}
```
→ Ask user to review final document

## Creating the Tracker

At project start, create with minimal info:

```json
{
  "meta": {
    "project_id": "PROP-004-PeakGen",
    "project_name": "",
    "client": "",
    "created": "2026-03-19T10:00:00Z",
    "last_updated": "2026-03-19T10:00:00Z",
    "status": "not_started"
  },
  "stages": {
    "setup": {"status": "in_progress"},
    "inputs": {"status": "pending"},
    "extraction": {"status": "pending"},
    "drafting": {"status": "pending", "current_section": 0},
    "template": {"status": "pending"},
    "refinement": {"status": "pending"},
    "budget": {"status": "pending"}
  },
  "inputs": {"template": null, "tender_docs": [], "context": null, "approved_at": null},
  "prd": {"approved": false},
  "sections": {
    "1_introduction": {"status": "pending"},
    "2_solution": {"status": "pending"},
    "3_scope": {"status": "pending"},
    "4_schedule": {"status": "pending"},
    "5_compensation": {"status": "pending"},
    "6_organisation": {"status": "pending"},
    "7_contractual": {"status": "pending"},
    "8_acceptance": {"status": "pending"}
  },
  "budget": {"status": "pending"},
  "output": {"proposal_file": null, "final_approved": false},
  "log": []
}
```

Then populate as you progress through stages.
