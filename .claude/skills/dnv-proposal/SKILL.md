---
name: dnv-proposal
description: "Create DNV technical proposals from tender documents. ALWAYS use this skill when: creating a DNV proposal, filling a DNV template, responding to an RFQ/RFP/tender, writing a quotation, preparing a NESO submission, drafting stability studies proposals, grid connection proposals, technical consultancy bids, or ANY task involving DNV proposal templates or professional engineering proposals. Trigger even if user just mentions 'proposal', 'quote', 'tender response', or 'bid'. This skill reads PDFs/spreadsheets, extracts requirements, and fills the official DNV template with tracked changes, working iteratively with user approval at each section."
---

# DNV Proposal Generator

Create professional DNV technical proposals through an iterative, user-approved process.

## Core Principle: No Surprises

**This skill operates section-by-section with explicit user approval at each stage.**

Never generate a complete proposal in one shot. Each section must be:
1. Drafted in readable markdown
2. Presented to the user for review
3. Revised based on feedback
4. Only then written to the template

The user controls the pace. Wait for explicit approval before proceeding.

## Critical Outputs

**The FINAL deliverable is a completed DOCX file with tracked changes** - NOT just markdown.

- Markdown drafts are intermediate working documents for review
- The goal is always to produce a Word document the user can open, review tracked changes, and finalize
- Stage 4 (Template Integration) is mandatory, not optional

---

## Project Folder Structure

```
projects/PROP-XXX-ClientName/
├── proposal-tracker.json       # STATE FILE - tracks all progress
├── DNV Proposal Template.docx  # Blank template
├── initial proposal.md         # User context/notes
├── rfp/                        # Tender source documents
├── working/                    # Section drafts, extraction-summary.md
├── budget/                     # tasks.json, budget-breakdown.xlsx
└── output/                     # Final deliverables only
```

### Proposal Tracker

The `proposal-tracker.json` is the most important file:
- Tracks progress through all stages
- Stores the approved "PRD" after Stage 2
- Enables resuming in new sessions
- Maintains audit trail

See `references/proposal-tracker.md` for full schema and initial JSON template.

### At Session Start

**ALWAYS check for existing tracker first.** If found, report status and ask to resume:

```
RESUMING PROJECT: PROP-004-PeakGen
Status: in_progress (Section 3: Scope of Work)
Completed: ✓ Setup ✓ Inputs ✓ PRD ✓ Section 1 ✓ Section 2
Shall I continue from where we left off?
```

---

## Workflow Overview

```
STAGE 0: Project Setup
    └── Create folders, init tracker → USER CHECKPOINT

STAGE 1: Gather Inputs
    └── List tender docs → USER CHECKPOINT: "Complete?"

STAGE 2: Extract & Approve PRD
    └── Extract requirements → USER CHECKPOINT: "Approve PRD?"

STAGE 3: Section-by-Section Drafting (1-8)
    └── For each: Draft → USER CHECKPOINT → Save if approved
    └── Section 5 uses [TBD] placeholder until Stage 6

STAGE 4: Template Integration
    └── Edit .docx with tracked changes → USER CHECKPOINT

STAGE 5: Refinement
    └── Address feedback → USER CHECKPOINT

STAGE 6: Budget Generation
    └── Hours → USER CHECKPOINT → Generate → USER CHECKPOINT → Update Section 5
```

**Section 5 Timing:** Draft structure in Stage 3, finalize pricing after Stage 6.

---

## Stage 0: Project Setup

Create folder structure if needed:
```bash
mkdir -p "projects/PROP-XXX-ClientName/{rfp,working,budget,output}"
```

Initialize `proposal-tracker.json` (see `references/proposal-tracker.md` for template).

**Checkpoint:** "Is this the correct project folder?"

---

## Stage 1: Gather and Validate Inputs

List all files found:
```
INPUTS FOUND:
- Template: DNV Proposal Template.docx
- Tender Documents: [list PDFs, spreadsheets]
- Context: initial proposal.md (if present)
```

**Checkpoint:** "Are these inputs complete?"

After approval, update tracker: `inputs.approved_at`, `stages.inputs.status = "completed"`

---

## Stage 2: Extract and Approve PRD

Read tender documents (use subagents for >20 pages). Save to `working/extraction-summary.md`.

See `references/proposal-structure.md` for extraction template format.

**Checkpoint:** "This becomes the PRD (scope contract). Do you approve?"

After approval:
- Set `prd.approved = true` in tracker
- PRD is now authoritative for all sections

**PRD Changes:** If scope changes later, ask for explicit confirmation, log the change, identify affected sections.

---

## Technical Validation (CRITICAL)

**Before drafting technical sections (especially Section 2 and 3), validate key technical claims against source documents.**

Common technical decisions that MUST be validated against tender specs:
- Study methodology (EMT vs RMS simulations)
- Number of simulations/tests required
- Compliance criteria and thresholds
- Software/tool requirements
- Deliverable formats

**Process:**
1. Identify technical claims that affect scope or pricing
2. Use subagents to search tender PDFs for the authoritative source
3. Quote the source with page number in the proposal
4. Present validation to user before proceeding

**Example - Simulation Count Derivation:**
```
| Test | Steps Required | Count | Source Reference |
|------|----------------|-------|------------------|
| Test 1 | 5, 6, 7, 8 | 4 | NESO V5, Page 8, 11 |
| Test 2 | 5-12, 14 | 9 | NESO V5, Page 13, 19 |
| Test 3 | 5,6,11,12,17,18,23,24 | 8 | NESO V5, Page 20-21, 26 |
| **Total per variant** | | **21** | |
```

**Never assume technical methodology** - always verify against source documents. If uncertain, ask the user or use a subagent to check.

---

## Stage 3: Section-by-Section Drafting

### Rules
1. One section at a time
2. Draft in markdown, not XML
3. Cite sources, flag uncertainties with `[TBD: description]`
4. Wait for explicit approval

### Section Sequence

| # | Section | Checkpoint |
|---|---------|------------|
| 1 | Introduction | "Captures client objective?" |
| 2 | Proposed Solution | "Approach and deliverables correct?" |
| 3 | Scope of Work | "Tasks complete and bounded?" |
| 4 | Schedule | "Timeline realistic?" |
| 5 | Compensation | "Structure correct? (Pricing TBD)" |
| 6 | Project Organisation | "Personnel correct?" |
| 7 | Contractual | "Assumptions appropriate?" |
| 8 | Acceptance | "Any customization?" |

### Draft Format

```
SECTION [N]: [TITLE]
====================
DRAFT CONTENT: [text]
SOURCES: [which tender docs]
UNCERTAINTIES: [TBD items]
CHECKPOINT: [question]
```

### Feedback Handling
- **Approved:** Save to `working/sectionN-name.md`, update tracker, proceed
- **Revision needed:** Revise and present again
- **Skip:** Mark as "skipped", proceed
- **Go back:** Return to previous section

### Fast Mode
Only if user explicitly says "fast mode" or "one shot".

---

## Stage 4: Template Integration

After all sections approved:
1. Unpack template: `python .claude/skills/docx/scripts/office/unpack.py`
2. Edit XML with tracked changes (see `references/template-editing.md`)
3. Repack to `output/`

**Checkpoint:** "Please review the Word file."

---

## Stage 5: Refinement

Address any post-integration changes with tracked changes. Repeat until satisfied.

---

## Stage 6: Budget Generation

See `references/dnv-2026-rates.md` for full budget workflow.

1. Create `budget/tasks.json` from approved Section 3 scope
2. **Checkpoint:** "Are these hours realistic?"
3. Run: `python scripts/budget_engine.py --config budget/tasks.json --output budget/budget-breakdown.xlsx`
4. **Checkpoint:** "Is this total acceptable?"
5. Update Section 5 with final pricing
6. **Checkpoint:** "Final approval?"

---

## Writing Style

See `references/writing-style.md` for full guide.

**DO:** Clear technical language, action verbs (Assess, Perform, Develop), cite sources
**DON'T:** Em-dashes, marketing jargon, assumptions, one-shot generation

---

## Reference Materials

| File | Contents |
|------|----------|
| `references/proposal-tracker.md` | Tracker schema, initial JSON, resume logic |
| `references/proposal-structure.md` | Section content breakdown, extraction template |
| `references/writing-style.md` | Editorial guidelines, forbidden phrases |
| `references/common-placeholders.md` | Placeholder formats |
| `references/template-editing.md` | XML editing, tracked changes |
| `references/dnv-2026-rates.md` | 2026 rates, budget engine usage |

---

## Dependencies

- `docx` skill - Template editing
- `pdf` skill - Reading tender PDFs
- `xlsx` skill - Reading tender spreadsheets
- `scripts/budget_engine.py` - Budget calculation

---

## Quick Reference: Checkpoints

| Stage | Ask | Tracker Update |
|-------|-----|----------------|
| 0 | "Correct folder?" | Initialize |
| 1 | "Inputs complete?" | `inputs.approved_at` |
| 2 | "Approve PRD?" | `prd.approved = true` |
| 3 | "Section approved?" | `sections.N.status` |
| 4 | "Review Word file" | `stages.template.status` |
| 5 | "Feedback addressed?" | Log changes |
| 6a | "Hours realistic?" | `budget.hours_approved` |
| 6b | "Total acceptable?" | `budget.status` |
| 6c | "Final approval?" | `output.final_approved` |

**When in doubt, ask. Never assume approval.**
