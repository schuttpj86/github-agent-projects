# DNV 2026 Rates Reference

## DNV 2026 Discounted Bill Rates (EUR)

| Grade | Role | Hourly Rate |
|-------|------|-------------|
| 5-7 | Professional | €145/hour |
| 8-9 | Senior | €189/hour |
| 10-11 | Principal | €231/hour |

These are the **discounted** rates from the DNV 2026 rate card.

## Typical Staff Mix

For most technical projects, a reasonable default staff mix is:
- **70%** Professional (Grade 5-7)
- **20%** Senior (Grade 8-9)
- **10%** Principal (Grade 10-11)

Adjust based on project complexity:
- Simple/routine work: Higher Professional ratio
- Complex/strategic work: Higher Senior/Principal ratio

## Budget Engine Usage

The budget engine is located at: `scripts/budget_engine.py`

### Create a Task Configuration

Create a JSON file with your task breakdown:

```json
{
  "name": "Project Name",
  "budget_range": [15000, 25000],
  "tasks": [
    {
      "section": "1.1 Project Management",
      "subtasks": [
        {
          "name": "Kick-off and coordination",
          "hours": {"professional": 8, "senior": 4, "principal": 2}
        },
        {
          "name": "Progress meetings and reporting",
          "hours": {"professional": 6, "senior": 3, "principal": 1}
        }
      ]
    },
    {
      "section": "1.2 Technical Analysis",
      "subtasks": [
        {
          "name": "Stability studies and modelling",
          "hours": {"professional": 40, "senior": 20, "principal": 8}
        },
        {
          "name": "Model validation and review",
          "hours": {"professional": 16, "senior": 12, "principal": 4}
        }
      ]
    },
    {
      "section": "1.3 Reporting",
      "subtasks": [
        {
          "name": "Report preparation",
          "hours": {"professional": 12, "senior": 8, "principal": 2}
        },
        {
          "name": "Contingency",
          "hours": {"professional": 5, "senior": 3, "principal": 1}
        }
      ]
    }
  ]
}
```

### Run the Budget Engine

```bash
# Generate Excel output
python scripts/budget_engine.py --config budget/tasks.json --output budget/budget-breakdown.xlsx

# Generate template JSON file (for reference)
python scripts/budget_engine.py --template budget/template.json

# Interactive mode (prompts for input)
python scripts/budget_engine.py --interactive --output budget/budget-breakdown.xlsx
```

### Output

The Excel file includes:
- Detailed task breakdown with hours by level
- Formulas that auto-calculate costs when you edit hours
- Rate cells that can be adjusted (costs recalculate automatically)
- Client summary section with work package overview

## Hour Estimation Guidelines

### Project Management Tasks

| Activity | Professional | Senior | Principal |
|----------|--------------|--------|-----------|
| Kick-off meeting | 4-8h | 2-4h | 1-2h |
| Progress meetings (per meeting) | 2h | 1h | 0.5h |
| Data collection and review | 8-16h | 4-8h | 0-2h |
| Stakeholder coordination | 4-8h | 2-4h | 1-2h |

### Technical Analysis Tasks

| Activity | Professional | Senior | Principal |
|----------|--------------|--------|-----------|
| Build model (per system) | 16-40h | 8-20h | 2-8h |
| Simulation runs (per scenario set) | 8-16h | 4-8h | 1-2h |
| Results analysis | 8-16h | 4-8h | 2-4h |
| Technical review | 4-8h | 4-8h | 2-4h |

### Reporting Tasks

| Activity | Professional | Senior | Principal |
|----------|--------------|--------|-----------|
| Draft report | 12-24h | 6-12h | 2-4h |
| Review and revisions | 4-8h | 4-8h | 2-4h |
| Final QA | 2-4h | 2-4h | 1-2h |
| Presentation prep | 4-8h | 2-4h | 1-2h |

### Contingency

Add 5-10% contingency to total hours, split across levels.

## Quick Cost Estimation

For rough budgeting, use the blended rate:

**Blended rate (70/20/10 mix):** €159/hour

```
Quick estimate = Total hours × €159
```

For more accurate estimates, use the budget engine with specific hour allocations.

## Proposal Section 5 Format

After budget is approved, format for Section 5 (Compensation):

```
5.2 Lump Sums

| Task | Description | Amount |
|------|-------------|--------|
| Task 1 | Project Management | €X,XXX |
| Task 2 | Technical Analysis | €X,XXX |
| Task 3 | Reporting | €X,XXX |
| **Total** | | **€XX,XXX** |

Prices are quoted in EUR, exclusive of VAT.
```
