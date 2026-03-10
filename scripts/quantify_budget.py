#!/usr/bin/env python3
"""Quantify budgets using DNV 2026 rates and proposal estimates.

Uses DNV 2026 discounted bill rates (EUR) for budget calculations and computes 
hours and additional PM and stakeholder engagement costs for each project 
section from the attached DNV budgetary proposal.

DNV 2026 Discounted Rates (EUR):
- Professional (Grade 5-7): €145/hour
- Senior (Grade 8-9): €189/hour
- Principal (Grade 10-11): €231/hour

Assumptions (configurable via CLI):
- Staff mix: 70% professional, 20% senior, 10% principal
- PM hours: 15% of the core delivery hours (billed at senior rate)
- Stakeholder engagement hours: default 8 hours per project (billed at senior rate)

Example:
    python scripts/quantify_budget.py --stakeholder-hours 8

"""
from __future__ import annotations
import argparse
from typing import Dict
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter


# DNV 2026 Discounted Bill Rates (EUR) - from rate card attachment
DNV_RATES = {
    "professional": 145,  # Grade 5-7, Discounted column
    "senior": 189,        # Grade 8-9, Discounted column
    "principal": 231,     # Grade 10-11, Discounted column
}

DEFAULT_STAFF_MIX = {
    "professional": 0.70,  # Consultant/Professional role
    "senior": 0.20,
    "principal": 0.10,
}


# Task breakdown structure for each project
# Each task specifies hours by consultant level (professional, senior, principal)
PROJECT_TASKS = {
    "1": {
        "name": "Angerlo – Ravenstein",
        "budget_range": (10500, 13500),
        "tasks": [
            {
                "section": "2.1 Project Management & Stakeholder Engagement",
                "subtasks": [
                    {"name": "Project Management & Meetings", "hours": {"professional": 12, "senior": 5, "principal": 2}},
                    {"name": "Stakeholder Consultation & Data Gathering", "hours": {"professional": 5, "senior": 3, "principal": 0}},
                ]
            },
            {
                "section": "2.2 Comprehensive Modeling & Analysis",
                "subtasks": [
                    {"name": "Build Detailed Models (380kV TenneT DTC-DOD, 50kV TenneT BML-NM)", "hours": {"professional": 28, "senior": 18, "principal": 4}},
                    {"name": "Model 4x 10kV Cable Parallelisms (Liander B/C, ProRail I/II)", "hours": {"professional": 8, "senior": 4, "principal": 1}},
                    {"name": "AC Corrosion & Touch Voltage Calculations", "hours": {"professional": 6, "senior": 4, "principal": 1}},
                ]
            },
            {
                "section": "2.3 Final Reporting & Close-out",
                "subtasks": [
                    {"name": "Final Report Preparation & Presentation", "hours": {"professional": 10, "senior": 6, "principal": 2}},
                    {"name": "Contingency", "hours": {"professional": 5, "senior": 2, "principal": 1}},
                ]
            }
        ]
    },
    "2": {
        "name": "Ravenstein – Boxtel",
        "budget_range": (14500, 18500),
        "tasks": [
            {
                "section": "2.1 Project Management & Stakeholder Engagement",
                "subtasks": [
                    {"name": "Project Management & Meetings", "hours": {"professional": 14, "senior": 6, "principal": 2}},
                    {"name": "Stakeholder Consultation & Data Gathering", "hours": {"professional": 6, "senior": 4, "principal": 0}},
                ]
            },
            {
                "section": "2.2 Comprehensive Modeling & Analysis",
                "subtasks": [
                    {"name": "Build Complex Models (Multiple 380kV, 110kV, 150kV Lines)", "hours": {"professional": 38, "senior": 22, "principal": 6}},
                    {"name": "Model 3x 10kV Cable Parallelisms (Enexis A, Liander A/B)", "hours": {"professional": 10, "senior": 5, "principal": 1}},
                    {"name": "AC Corrosion & Touch Voltage Calculations", "hours": {"professional": 8, "senior": 5, "principal": 2}},
                ]
            },
            {
                "section": "2.3 Final Reporting & Close-out",
                "subtasks": [
                    {"name": "Final Report Preparation & Presentation", "hours": {"professional": 12, "senior": 7, "principal": 2}},
                    {"name": "Contingency", "hours": {"professional": 7, "senior": 3, "principal": 2}},
                ]
            }
        ]
    },
    "3": {
        "name": "Zweekhorst – Ommen",
        "budget_range": (7500, 9500),
        "tasks": [
            {
                "section": "2.1 Project Management & Stakeholder Engagement",
                "subtasks": [
                    {"name": "Project Management & Meetings", "hours": {"professional": 10, "senior": 4, "principal": 1}},
                    {"name": "Stakeholder Consultation & Data Gathering", "hours": {"professional": 4, "senior": 2, "principal": 0}},
                ]
            },
            {
                "section": "2.2 Comprehensive Modeling & Analysis",
                "subtasks": [
                    {"name": "Build Models (150kV TenneT OS-UD, OST-BXT Cables 1+2)", "hours": {"professional": 18, "senior": 12, "principal": 3}},
                    {"name": "Model 1x 10kV Cable Parallelism (Liander B)", "hours": {"professional": 4, "senior": 2, "principal": 0}},
                    {"name": "AC Corrosion & Touch Voltage Calculations", "hours": {"professional": 4, "senior": 3, "principal": 1}},
                ]
            },
            {
                "section": "2.3 Final Reporting & Close-out",
                "subtasks": [
                    {"name": "Final Report Preparation & Presentation", "hours": {"professional": 8, "senior": 5, "principal": 1}},
                    {"name": "Contingency", "hours": {"professional": 4, "senior": 2, "principal": 1}},
                ]
            }
        ]
    }
}


def compute_task_costs(hours: Dict[str, float]) -> Dict:
    """Calculate cost for a task given hours by consultant level."""
    prof_cost = hours.get("professional", 0) * DNV_RATES["professional"]
    sr_cost = hours.get("senior", 0) * DNV_RATES["senior"]
    pr_cost = hours.get("principal", 0) * DNV_RATES["principal"]
    total_cost = prof_cost + sr_cost + pr_cost
    total_hours = hours.get("professional", 0) + hours.get("senior", 0) + hours.get("principal", 0)
    
    return {
        "hours": hours,
        "costs": {"professional": prof_cost, "senior": sr_cost, "principal": pr_cost},
        "total_cost": total_cost,
        "total_hours": total_hours
    }


def compute_project_breakdown(project_id: str) -> Dict:
    """Compute full breakdown for a project."""
    project = PROJECT_TASKS[project_id]
    
    section_results = []
    total_prof_hours = 0
    total_sr_hours = 0
    total_pr_hours = 0
    total_cost = 0
    
    for section in project["tasks"]:
        section_tasks = []
        section_prof_hours = 0
        section_sr_hours = 0
        section_pr_hours = 0
        section_cost = 0
        
        for subtask in section["subtasks"]:
            task_result = compute_task_costs(subtask["hours"])
            task_result["name"] = subtask["name"]
            section_tasks.append(task_result)
            
            section_prof_hours += subtask["hours"].get("professional", 0)
            section_sr_hours += subtask["hours"].get("senior", 0)
            section_pr_hours += subtask["hours"].get("principal", 0)
            section_cost += task_result["total_cost"]
        
        section_results.append({
            "section": section["section"],
            "tasks": section_tasks,
            "totals": {
                "professional": section_prof_hours,
                "senior": section_sr_hours,
                "principal": section_pr_hours,
                "cost": section_cost,
                "hours": section_prof_hours + section_sr_hours + section_pr_hours
            }
        })
        
        total_prof_hours += section_prof_hours
        total_sr_hours += section_sr_hours
        total_pr_hours += section_pr_hours
        total_cost += section_cost
    
    return {
        "project_id": project_id,
        "project_name": project["name"],
        "budget_range": project["budget_range"],
        "sections": section_results,
        "totals": {
            "professional": total_prof_hours,
            "senior": total_sr_hours,
            "principal": total_pr_hours,
            "total_hours": total_prof_hours + total_sr_hours + total_pr_hours,
            "total_cost": total_cost
        }
    }


def format_euro(x: float) -> str:
    return f"€ {x:,.2f}"


def print_project_breakdown(result: Dict):
    """Print detailed task breakdown in tabular format."""
    print(f"\n{'='*120}")
    print(f"Project {result['project_id']}: {result['project_name']}")
    print(f"Proposal Budget Range: {format_euro(result['budget_range'][0])} - {format_euro(result['budget_range'][1])}")
    print(f"DNV 2026 Discounted Rates: Professional €{DNV_RATES['professional']}/h | Senior €{DNV_RATES['senior']}/h | Principal €{DNV_RATES['principal']}/h")
    print(f"{'='*120}\n")
    
    # Header
    print(f"{'Work Package / Task':<60} {'Prof':<8} {'Senior':<8} {'Princ':<8} {'Contract Price':>15}")
    print(f"{'-'*60} {'-'*8} {'-'*8} {'-'*8} {'-'*15}")
    
    for section in result["sections"]:
        # Section header
        print(f"\n{section['section']}")
        
        # Tasks
        for task in section["tasks"]:
            prof_h = task["hours"].get("professional", 0)
            sr_h = task["hours"].get("senior", 0)
            pr_h = task["hours"].get("principal", 0)
            
            print(f"  {task['name']:<58} {prof_h:<8.0f} {sr_h:<8.0f} {pr_h:<8.0f} {format_euro(task['total_cost']):>15}")
        
        # Section subtotal
        print(f"  {'-'*58} {'-'*8} {'-'*8} {'-'*8} {'-'*15}")
        print(f"  {'Subtotal':<58} {section['totals']['professional']:<8.0f} {section['totals']['senior']:<8.0f} {section['totals']['principal']:<8.0f} {format_euro(section['totals']['cost']):>15}")
    
    # Grand total
    print(f"\n{'-'*60} {'-'*8} {'-'*8} {'-'*8} {'-'*15}")
    print(f"{'TOTAL HOURS & COST':<60} {result['totals']['professional']:<8.0f} {result['totals']['senior']:<8.0f} {result['totals']['principal']:<8.0f} {format_euro(result['totals']['total_cost']):>15}")
    print(f"{'Total Hours:':<60} {result['totals']['total_hours']:.1f} hours")
    print(f"\n")


def export_to_excel(results: list[Dict], output_path: str):
    """Export all project breakdowns to Excel with formulas for live calculations."""
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    # Styling
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=11)
    section_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    section_font = Font(bold=True, size=10)
    subtotal_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    subtotal_font = Font(bold=True, size=10)
    total_fill = PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid")
    total_font = Font(bold=True, size=11)
    rate_fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
    rate_font = Font(bold=True, size=10)
    currency_format = '€ #,##0.00'
    number_format = '#,##0'
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    for result in results:
        # Create sheet for each project
        ws = wb.create_sheet(title=f"Project {result['project_id']}")
        
        # Title rows
        ws.merge_cells('A1:E1')
        ws['A1'] = f"Project {result['project_id']}: {result['project_name']}"
        ws['A1'].font = Font(bold=True, size=14)
        ws['A1'].alignment = Alignment(horizontal='left')
        
        ws.merge_cells('A2:E2')
        ws['A2'] = f"Budget Range: {format_euro(result['budget_range'][0])} - {format_euro(result['budget_range'][1])}"
        ws['A2'].font = Font(size=10)
        
        ws.merge_cells('A3:E3')
        ws['A3'] = f"DNV 2026 Rates: Professional €{DNV_RATES['professional']}/h | Senior €{DNV_RATES['senior']}/h | Principal €{DNV_RATES['principal']}/h"
        ws['A3'].font = Font(size=10)
        
        # Column headers with rates in row below
        row = 5
        headers = ['Work Package / Task', 'Professional Hours', 'Senior Hours', 'Principal Hours', 'Contract Price']
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=row, column=col, value=header)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = border
        
        # Add rate row for easy reference and formulas
        row += 1
        ws.cell(row=row, column=1, value="Hourly Rates →").fill = rate_fill
        ws.cell(row=row, column=1).font = rate_font
        ws.cell(row=row, column=1).border = border
        
        rate_cells = {}
        for col, (role, rate) in enumerate([('professional', DNV_RATES['professional']), 
                                             ('senior', DNV_RATES['senior']), 
                                             ('principal', DNV_RATES['principal'])], 2):
            cell = ws.cell(row=row, column=col, value=rate)
            cell.fill = rate_fill
            cell.font = rate_font
            cell.number_format = '€ #,##0'
            cell.alignment = Alignment(horizontal='center')
            cell.border = border
            rate_cells[role] = f"{get_column_letter(col)}{row}"
        
        ws.cell(row=row, column=5, value="(Formulas calculate automatically)").fill = rate_fill
        ws.cell(row=row, column=5).font = Font(italic=True, size=9)
        ws.cell(row=row, column=5).border = border
        
        row += 1
        
        # Data rows with formulas
        task_rows = []  # Track rows for subtotal formulas
        
        for section in result["sections"]:
            # Section header
            ws.merge_cells(f'A{row}:E{row}')
            cell = ws.cell(row=row, column=1, value=section['section'])
            cell.fill = section_fill
            cell.font = section_font
            cell.border = border
            row += 1
            
            section_start_row = row
            
            # Tasks
            for task in section["tasks"]:
                ws.cell(row=row, column=1, value=f"  {task['name']}").border = border
                ws.cell(row=row, column=2, value=task["hours"].get("professional", 0)).border = border
                ws.cell(row=row, column=2).number_format = number_format
                ws.cell(row=row, column=3, value=task["hours"].get("senior", 0)).border = border
                ws.cell(row=row, column=3).number_format = number_format
                ws.cell(row=row, column=4, value=task["hours"].get("principal", 0)).border = border
                ws.cell(row=row, column=4).number_format = number_format
                
                # Formula: hours * rates (referencing the rate cells)
                formula = f"=B{row}*${rate_cells['professional']}+C{row}*${rate_cells['senior']}+D{row}*${rate_cells['principal']}"
                price_cell = ws.cell(row=row, column=5, value=formula)
                price_cell.number_format = currency_format
                price_cell.border = border
                
                task_rows.append(row)
                row += 1
            
            section_end_row = row - 1
            
            # Subtotal with formulas
            for col in range(1, 6):
                ws.cell(row=row, column=col).fill = subtotal_fill
                ws.cell(row=row, column=col).font = subtotal_font
                ws.cell(row=row, column=col).border = border
            
            ws.cell(row=row, column=1, value="  Subtotal")
            
            # Sum formulas for hours and cost
            for col, col_letter in enumerate(['B', 'C', 'D', 'E'], 2):
                formula = f"=SUM({col_letter}{section_start_row}:{col_letter}{section_end_row})"
                cell = ws.cell(row=row, column=col, value=formula)
                if col <= 4:
                    cell.number_format = number_format
                else:
                    cell.number_format = currency_format
            
            row += 1
            
            # Empty row
            row += 1
        
        # Grand total with formulas
        total_row = row
        for col in range(1, 6):
            ws.cell(row=row, column=col).fill = total_fill
            ws.cell(row=row, column=col).font = total_font
            ws.cell(row=row, column=col).border = border
        
        ws.cell(row=row, column=1, value="TOTAL HOURS & COST")
        
        # Grand total formulas - sum all task rows
        first_task_row = 8  # After headers and rate row
        last_task_row = row - 1
        
        for col, col_letter in enumerate(['B', 'C', 'D'], 2):
            # Sum only the task rows, not subtotals
            formula = f"=B{6}*B{total_row}+C{6}*C{total_row}+D{6}*D{total_row}"  # Will be overridden
            # Better approach: sum the subtotals
            ranges = []
            current_row = 8
            while current_row < total_row:
                cell_val = ws.cell(row=current_row, column=1).value
                if cell_val and "Subtotal" in str(cell_val):
                    ranges.append(f"{col_letter}{current_row}")
                current_row += 1
            
            if ranges:
                formula = "=" + "+".join(ranges)
                cell = ws.cell(row=row, column=col, value=formula)
                cell.number_format = number_format
        
        # Total cost formula
        total_cost_formula = f"=B{total_row}*${rate_cells['professional']}+C{total_row}*${rate_cells['senior']}+D{total_row}*${rate_cells['principal']}"
        ws.cell(row=row, column=5, value=total_cost_formula).number_format = currency_format
        
        row += 1
        
        # Total hours summary (formula)
        total_hours_formula = f"=B{total_row}+C{total_row}+D{total_row}"
        ws.cell(row=row, column=1, value=f"Total Hours:")
        ws.cell(row=row, column=1).font = Font(bold=True)
        ws.cell(row=row, column=2, value=total_hours_formula)
        ws.cell(row=row, column=2).font = Font(bold=True)
        ws.cell(row=row, column=2).number_format = '#,##0.0'
        
        # Add client summary section
        row += 3
        
        # Client summary title
        ws.merge_cells(f'A{row}:D{row}')
        ws.cell(row=row, column=1, value="CLIENT SUMMARY - Work Package Overview")
        ws.cell(row=row, column=1).font = Font(bold=True, size=12, color="1F4E78")
        ws.cell(row=row, column=1).fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
        row += 1
        
        # Client summary headers
        summary_headers = ['Work Package', 'Total Hours', 'Cost', 'Notes']
        for col, header in enumerate(summary_headers, 1):
            cell = ws.cell(row=row, column=col, value=header)
            cell.fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
            cell.font = Font(bold=True, color="FFFFFF", size=10)
            cell.alignment = Alignment(horizontal='center')
            cell.border = border
        row += 1
        
        # Track section rows for summary
        summary_start_row = row
        section_row_map = {}
        
        # Find all section subtotal rows from the detailed breakdown above
        search_row = 8  # Start after headers
        section_index = 0
        while search_row < total_row:
            cell_val = ws.cell(row=search_row, column=1).value
            if cell_val and "Subtotal" in str(cell_val) and section_index < len(result["sections"]):
                section_row_map[result["sections"][section_index]["section"]] = search_row
                section_index += 1
            search_row += 1
        
        # Add summary rows for each work package
        for section in result["sections"]:
            section_name = section["section"]
            subtotal_row = section_row_map.get(section_name)
            
            # Work package name (simplified)
            ws.cell(row=row, column=1, value=section_name.split(' ', 1)[1] if ' ' in section_name else section_name)
            ws.cell(row=row, column=1).border = border
            ws.cell(row=row, column=1).alignment = Alignment(horizontal='left')
            
            # Total hours formula (references subtotal row)
            if subtotal_row:
                hours_formula = f"=B{subtotal_row}+C{subtotal_row}+D{subtotal_row}"
                ws.cell(row=row, column=2, value=hours_formula)
            else:
                ws.cell(row=row, column=2, value=section['totals']['hours'])
            ws.cell(row=row, column=2).number_format = '#,##0.0'
            ws.cell(row=row, column=2).border = border
            ws.cell(row=row, column=2).alignment = Alignment(horizontal='center')
            
            # Cost formula (references subtotal row)
            if subtotal_row:
                cost_formula = f"=E{subtotal_row}"
                ws.cell(row=row, column=3, value=cost_formula)
            else:
                ws.cell(row=row, column=3, value=section['totals']['cost'])
            ws.cell(row=row, column=3).number_format = currency_format
            ws.cell(row=row, column=3).border = border
            ws.cell(row=row, column=3).alignment = Alignment(horizontal='right')
            
            # Notes column - describe what's included
            notes = ""
            if "Management" in section_name or "Stakeholder" in section_name:
                notes = "Project coordination, meetings, data collection"
            elif "Modeling" in section_name or "Analysis" in section_name:
                notes = "Technical calculations, simulations, compliance checks"
            elif "Reporting" in section_name or "Close-out" in section_name:
                notes = "Documentation, final report, presentation"
            
            ws.cell(row=row, column=4, value=notes)
            ws.cell(row=row, column=4).border = border
            ws.cell(row=row, column=4).alignment = Alignment(horizontal='left')
            ws.cell(row=row, column=4).font = Font(size=9, italic=True)
            
            row += 1
        
        # Summary total row
        summary_end_row = row - 1
        for col in range(1, 5):
            ws.cell(row=row, column=col).fill = PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid")
            ws.cell(row=row, column=col).font = Font(bold=True, size=11)
            ws.cell(row=row, column=col).border = border
        
        ws.cell(row=row, column=1, value="PROJECT TOTAL")
        ws.cell(row=row, column=1).alignment = Alignment(horizontal='left')
        
        # Sum hours
        ws.cell(row=row, column=2, value=f"=SUM(B{summary_start_row}:B{summary_end_row})")
        ws.cell(row=row, column=2).number_format = '#,##0.0'
        ws.cell(row=row, column=2).alignment = Alignment(horizontal='center')
        
        # Sum cost
        ws.cell(row=row, column=3, value=f"=SUM(C{summary_start_row}:C{summary_end_row})")
        ws.cell(row=row, column=3).number_format = currency_format
        ws.cell(row=row, column=3).alignment = Alignment(horizontal='right')
        
        ws.cell(row=row, column=4, value="")
        
        # Adjust column widths for summary section
        ws.column_dimensions['D'].width = 45
        
        # Adjust column widths
        ws.column_dimensions['A'].width = 60
        ws.column_dimensions['B'].width = 18
        ws.column_dimensions['C'].width = 18
        ws.column_dimensions['E'].width = 18
    
    wb.save(output_path)
    print(f"\n✓ Excel file saved to: {output_path}")
    print(f"  → All costs calculated with formulas - edit hours and costs update automatically!")
    print(f"  → You can also adjust hourly rates in row 6")


def main():
    p = argparse.ArgumentParser(description="Quantify budgets from DNV proposal with detailed task breakdown")
    p.add_argument("--output", "-o", help="Export to Excel file (e.g., budget-breakdown.xlsx)")
    args = p.parse_args()

    print("\n" + "="*120)
    print("BUDGET QUANTIFICATION REPORT - DETAILED TASK BREAKDOWN")
    print("DNV 2026 Discounted Rates (EUR/h)")
    print("="*120)

    results = []
    for project_id in PROJECT_TASKS.keys():
        result = compute_project_breakdown(project_id)
        results.append(result)
        if not args.output:  # Only print if not exporting to Excel
            print_project_breakdown(result)
    
    if args.output:
        export_to_excel(results, args.output)
        print(f"\n✓ Budget breakdown exported to Excel: {args.output}")
        print(f"  You can now open the file in Excel to view and modify hours.")
    else:
        print("\nTip: Run with --output budget.xlsx to export to Excel")


if __name__ == '__main__':
    main()
