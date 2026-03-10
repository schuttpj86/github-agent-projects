Quantify Budget Script
======================

Purpose
-------
Helper script to convert the DNV proposal budget ranges into estimated hours and total costs using DNV 2026 discounted bill rates.

DNV 2026 Discounted Rates (EUR)
--------------------------------
- **Professional** (Grade 5-7): €145/hour
- **Senior** (Grade 8-9): €189/hour
- **Principal** (Grade 10-11): €231/hour

Usage
-----
Run the script from the repository root:

```bash
python scripts/quantify_budget.py --stakeholder-hours 8 --pm-pct 15
```

Key assumptions
---------------
- Staff mix: 70% professional, 20% senior, 10% principal
- PM hours: 15% of core hours and billed at the senior rate (€189/hour)
- Stakeholder engagement: default 8 hours per project at the senior rate (€189/hour)
- Rates are DNV 2026 discounted rates (already include discount)

Files
-----
- `scripts/quantify_budget.py`: main script with embedded DNV rates
