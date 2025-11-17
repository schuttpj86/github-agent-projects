"""
Budget Calculator for Power Grids of the Future
Calculates project budgets based on scope, complexity, and resource requirements.

Usage:
    python budget_calculator.py --lead-id LEAD-2025-117 --output json
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Any


def load_rates(config_path: str = "config/rates.json") -> Dict[str, Any]:
    """Load billing rates and cost structure."""
    with open(config_path, 'r') as f:
        return json.load(f)


def load_complexity_factors(config_path: str = "resources/complexity-factors.json") -> Dict[str, Any]:
    """Load complexity assessment criteria."""
    with open(config_path, 'r') as f:
        return json.load(f)


def calculate_complexity_score(project_params: Dict[str, Any]) -> float:
    """
    Calculate project complexity score (0-100).
    Returns multiplier based on score.
    """
    complexity_factors = load_complexity_factors()
    
    # Example scoring (simplified)
    score = 0
    
    # Site size scoring
    if project_params.get('site_area_m2', 0) > 20000:
        score += 10
    elif project_params.get('site_area_m2', 0) > 5000:
        score += 8
    elif project_params.get('site_area_m2', 0) > 2000:
        score += 5
    else:
        score += 2
    
    # Soil conditions
    if project_params.get('soil_layers', 1) >= 3:
        score += 12
    elif project_params.get('soil_layers', 1) == 2:
        score += 8
    else:
        score += 2
    
    # Fault current magnitude
    fault_ka = project_params.get('fault_current_ka', 0)
    if fault_ka > 50:
        score += 15
    elif fault_ka > 25:
        score += 12
    elif fault_ka > 10:
        score += 7
    else:
        score += 3
    
    # Timeline pressure
    weeks = project_params.get('timeline_weeks', 12)
    if weeks < 3:
        score += 10
    elif weeks < 6:
        score += 7
    elif weeks < 12:
        score += 3
    else:
        score += 1
    
    # Determine multiplier from score
    if score >= 66:
        return 1.6  # Highly complex
    elif score >= 41:
        return 1.35  # Complex
    elif score >= 21:
        return 1.15  # Moderate
    else:
        return 1.0  # Simple


def calculate_budget(
    senior_hours: int,
    junior_hours: int,
    complexity_multiplier: float,
    timeline_rush: bool = False,
    contingency_level: str = "medium"
) -> Dict[str, Any]:
    """
    Calculate total project budget.
    
    Args:
        senior_hours: Estimated senior engineer hours
        junior_hours: Estimated junior engineer hours
        complexity_multiplier: Complexity adjustment factor (1.0-1.6)
        timeline_rush: True if rush timeline (adds 25% premium)
        contingency_level: "low" (5%), "medium" (10%), or "high" (15%)
    
    Returns:
        Dictionary with detailed budget breakdown
    """
    rates = load_rates()
    
    # Base labor costs
    senior_rate = rates['bill_rates']['senior_engineer']['rate_per_hour']
    junior_rate = rates['bill_rates']['junior_engineer']['rate_per_hour']
    
    senior_cost = senior_hours * senior_rate
    junior_cost = junior_hours * junior_rate
    base_labor = senior_cost + junior_cost
    
    # Apply complexity multiplier
    adjusted_labor = base_labor * complexity_multiplier
    
    # Apply rush premium if applicable
    if timeline_rush:
        adjusted_labor *= 1.25
    
    # Add overhead and profit
    overhead_rate = rates['overhead_and_profit']['overhead_rate']
    profit_margin = rates['overhead_and_profit']['profit_margin']
    
    overhead = adjusted_labor * overhead_rate
    profit = adjusted_labor * profit_margin
    subtotal = adjusted_labor + overhead + profit
    
    # Add contingency
    contingency_rates = {
        'low': rates['contingency']['low_risk'],
        'medium': rates['contingency']['medium_risk'],
        'high': rates['contingency']['high_risk']
    }
    contingency_rate = contingency_rates.get(contingency_level, 0.10)
    contingency = subtotal * contingency_rate
    
    total = subtotal + contingency
    
    # Calculate payment schedule (30/30/25/15)
    payment_terms = rates['payment_terms']
    payment_schedule = {
        'deposit_30pct': total * payment_terms['deposit'],
        'milestone_1_30pct': total * payment_terms['milestone_1'],
        'milestone_2_25pct': total * payment_terms['milestone_2'],
        'final_15pct': total * payment_terms['final']
    }
    
    return {
        'cost_breakdown': {
            'senior_labor': round(senior_cost, 2),
            'junior_labor': round(junior_cost, 2),
            'base_labor': round(base_labor, 2),
            'complexity_adjusted': round(adjusted_labor, 2),
            'overhead': round(overhead, 2),
            'profit': round(profit, 2),
            'subtotal': round(subtotal, 2),
            'contingency': round(contingency, 2),
            'total': round(total, 2)
        },
        'budget_range': {
            'low': round(total * 0.92, 2),  # -8%
            'target': round(total, 2),
            'high': round(total * 1.09, 2)  # +9%
        },
        'payment_schedule': {k: round(v, 2) for k, v in payment_schedule.items()},
        'calculation_inputs': {
            'senior_hours': senior_hours,
            'junior_hours': junior_hours,
            'complexity_multiplier': complexity_multiplier,
            'timeline_rush': timeline_rush,
            'contingency': contingency_level
        }
    }


def main():
    """Main entry point for budget calculator."""
    parser = argparse.ArgumentParser(description='Calculate project budget')
    parser.add_argument('--lead-id', required=True, help='Lead ID (e.g., LEAD-2025-117)')
    parser.add_argument('--senior-hours', type=int, default=60, help='Senior engineer hours')
    parser.add_argument('--junior-hours', type=int, default=80, help='Junior engineer hours')
    parser.add_argument('--complexity', type=float, default=1.35, help='Complexity multiplier (1.0-1.6)')
    parser.add_argument('--rush', action='store_true', help='Rush timeline (adds 25% premium)')
    parser.add_argument('--contingency', default='medium', choices=['low', 'medium', 'high'])
    parser.add_argument('--output', default='json', choices=['json', 'summary'])
    
    args = parser.parse_args()
    
    # Calculate budget
    budget = calculate_budget(
        senior_hours=args.senior_hours,
        junior_hours=args.junior_hours,
        complexity_multiplier=args.complexity,
        timeline_rush=args.rush,
        contingency_level=args.contingency
    )
    
    if args.output == 'json':
        print(json.dumps(budget, indent=2))
    else:
        print(f"\n=== Budget Calculation for {args.lead_id} ===\n")
        print(f"Labor Hours: {args.senior_hours} senior + {args.junior_hours} junior")
        print(f"Complexity Multiplier: {args.complexity}x")
        print(f"Rush Timeline: {'Yes (+25%)' if args.rush else 'No'}")
        print(f"Contingency: {args.contingency} ({budget['cost_breakdown']['contingency']:,.2f})")
        print(f"\n--- Total Budget ---")
        print(f"Base Labor: ${budget['cost_breakdown']['base_labor']:,.2f}")
        print(f"Adjusted Labor: ${budget['cost_breakdown']['complexity_adjusted']:,.2f}")
        print(f"With Overhead/Profit: ${budget['cost_breakdown']['subtotal']:,.2f}")
        print(f"TOTAL: ${budget['cost_breakdown']['total']:,.2f}")
        print(f"\nRecommended Range: ${budget['budget_range']['low']:,.2f} - ${budget['budget_range']['high']:,.2f}")


if __name__ == '__main__':
    main()
