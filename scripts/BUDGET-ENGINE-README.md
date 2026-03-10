# Budget Engine - Modular Budget Calculation Tool

A flexible, reusable budget calculator that works for any project. Use interactive mode or JSON config files.

## Quick Start

### 1. Interactive Mode (Guided Prompts)
```bash
python scripts/budget_engine.py --interactive --output output/my-project.xlsx
```
You'll be prompted for:
- Hourly rates (or use DNV 2026 defaults)
- Project name and budget range
- Work packages and tasks
- Hours per task (professional/senior/principal)

### 2. JSON Config Mode (Recommended for Reuse)

**Step 1: Generate a template**
```bash
python scripts/budget_engine.py --template config/my-project.json
```

**Step 2: Edit the JSON file** with your project details

**Step 3: Run the calculator**
```bash
python scripts/budget_engine.py --config config/my-project.json --output output/my-project.xlsx
```

### 3. Quick Test with Existing Template
```bash
python scripts/budget_engine.py --config config/project-template.json --output output/test.xlsx
```

## JSON Project File Format

```json
{
  "name": "Your Project Name",
  "budget_range": [10000, 15000],
  "tasks": [
    {
      "section": "1.1 Work Package Name",
      "subtasks": [
        {
          "name": "Task description",
          "hours": {
            "professional": 12,
            "senior": 5,
            "principal": 2
          }
        }
      ]
    }
  ]
}
```

## Output

**Excel file includes:**
- ✅ Detailed breakdown with formulas (editable hours)
- ✅ Subtotals per work package
- ✅ Grand totals
- ✅ Client summary table (high-level view)
- ✅ Live calculations (change hours → costs update)

## Examples

### Create a new project interactively
```bash
python scripts/budget_engine.py -i -o output/acme-substation.xlsx
```

### Use a saved config
```bash
python scripts/budget_engine.py -c config/acme-project.json -o output/acme.xlsx
```

### Just preview (no Excel export)
```bash
python scripts/budget_engine.py -c config/my-project.json
```

## Typical Workflow

1. **First time:** Run `--interactive` to build your project structure
2. **Save the structure:** The script prints everything - you can manually create a JSON
3. **Reuse:** For similar projects, copy the JSON template and modify
4. **Quick updates:** Edit the JSON, re-run the script

## Customizing Rates

### Option 1: Interactive prompts (default)
```bash
python scripts/budget_engine.py --interactive
# Will prompt for rates at the start
```

### Option 2: Add rates to JSON (future enhancement)
Currently rates are prompted or use DNV 2026 defaults:
- Professional: €145/h
- Senior: €189/h
- Principal: €231/h

## Tips

- **Reusing templates:** Copy `config/project-template.json` for new projects
- **Version control:** Save JSON configs in Git for reproducibility
- **Multiple scenarios:** Create different JSON files for low/high estimates
- **Client vs internal:** Excel includes both detailed and summary views

## Files

- `scripts/budget_engine.py` - Main modular calculator
- `scripts/quantify_budget.py` - Original DNV-specific version
- `config/project-template.json` - Template for new projects
- `output/*.xlsx` - Generated Excel files

---

**Need help?** Run `python scripts/budget_engine.py --help`
