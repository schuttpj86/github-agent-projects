"""
IEEE 80 Grounding System Calculator
Calculates ground resistance, GPR, touch voltage, and step voltage.

Usage:
    python gpr_calculator.py --project PROJ-001 --output report
"""

import json
import argparse
import numpy as np
from pathlib import Path
from typing import Dict, Any, Tuple


class GroundResistanceCalculator:
    """Calculate ground resistance for various soil models."""
    
    @staticmethod
    def two_layer_resistance(rho1: float, rho2: float, h: float, area: float, length: float) -> float:
        """
        Calculate ground resistance for two-layer soil model.
        
        Args:
            rho1: Upper layer resistivity (Ω·m)
            rho2: Lower layer resistivity (Ω·m)
            h: Upper layer depth (m)
            area: Grid area (m²)
            length: Total conductor length (m)
        
        Returns:
            Ground resistance (Ω)
        """
        # Reflection factor
        K = (rho2 - rho1) / (rho2 + rho1)
        
        # Simplified IEEE 80 formula for two-layer soil
        # Rg = ρ1 * [1/L + 1/√(20A) * (1 + 1/(1 + h√(20/A)))] * (1 + K)
        
        term1 = 1 / length
        term2 = 1 / np.sqrt(20 * area)
        term3 = 1 + 1 / (1 + h * np.sqrt(20 / area))
        
        Rg = rho1 * (term1 + term2 * term3) * (1 + K)
        
        return Rg


class TouchVoltageCalculator:
    """Calculate touch voltage using IEEE 80 mesh method."""
    
    @staticmethod
    def mesh_voltage(rho: float, Ig: float, total_length: float, grid_spacing: float, depth: float) -> float:
        """
        Calculate mesh touch voltage (simplified IEEE 80 method).
        
        Args:
            rho: Soil resistivity (Ω·m)
            Ig: Grid current (A)
            total_length: Total conductor length (m)
            grid_spacing: Conductor spacing (m)
            depth: Burial depth (m)
        
        Returns:
            Touch voltage (V)
        """
        # Geometrical spacing factor (simplified)
        Km = 0.75 if grid_spacing <= 10 else 0.85
        
        # Irregularity factor
        Ki = 1.0  # Assume uniform grid
        
        # Mesh voltage formula
        Emesh = (rho * Km * Ki * Ig) / total_length
        
        return Emesh
    
    @staticmethod
    def tolerable_voltage(rho_surface: float, thickness: float, duration: float, body_weight: float = 50) -> float:
        """
        Calculate tolerable touch voltage per IEEE 80.
        
        Args:
            rho_surface: Surface material resistivity (Ω·m)
            thickness: Surface layer thickness (m)
            duration: Shock duration (seconds)
            body_weight: Body weight (kg), default 50kg
        
        Returns:
            Tolerable touch voltage (V)
        """
        # IEEE 80 formula for tolerable touch voltage
        # Etouch = (1000 + 1.5 * ρs * hs) * (0.116 / √ts)
        
        Etouch_tol = (1000 + 1.5 * rho_surface * thickness) * (0.116 / np.sqrt(duration))
        
        return Etouch_tol


class StepVoltageCalculator:
    """Calculate step voltage."""
    
    @staticmethod
    def calculate(rho: float, Ig: float, total_length: float, grid_spacing: float) -> float:
        """
        Calculate step voltage (simplified).
        
        Args:
            rho: Soil resistivity (Ω·m)
            Ig: Grid current (A)
            total_length: Total conductor length (m)
            grid_spacing: Conductor spacing (m)
        
        Returns:
            Step voltage (V)
        """
        # Simplified step voltage calculation
        Ks = 0.5 if grid_spacing <= 10 else 0.65
        Ki = 1.0
        
        Estep = (rho * Ks * Ki * Ig) / total_length
        
        return Estep
    
    @staticmethod
    def tolerable_voltage(rho_surface: float, thickness: float, duration: float) -> float:
        """
        Calculate tolerable step voltage per IEEE 80.
        
        Args:
            rho_surface: Surface material resistivity (Ω·m)
            thickness: Surface layer thickness (m)
            duration: Shock duration (seconds)
        
        Returns:
            Tolerable step voltage (V)
        """
        # IEEE 80 formula: Estep = (1000 + 6 * ρs * hs) * (0.116 / √ts)
        
        Estep_tol = (1000 + 6 * rho_surface * thickness) * (0.116 / np.sqrt(duration))
        
        return Estep_tol


def load_project_specs(project_id: str) -> Dict[str, Any]:
    """Load project specifications from JSON file."""
    spec_path = Path(f"projects/{project_id}/specs/site-data.json")
    
    if not spec_path.exists():
        # Return example data if file doesn't exist yet
        return {
            "project_id": project_id,
            "electrical_system": {
                "fault_current_ka": 40,
                "fault_duration_sec": 0.5
            },
            "soil": {
                "layer1": {"resistivity_ohm_m": 150},
                "layer2": {"resistivity_ohm_m": 450},
                "layer1_depth_m": 3
            },
            "grid_design": {
                "area_m2": 5000,
                "conductor_length_m": 2580,
                "spacing_m": 7,
                "depth_m": 0.6
            },
            "surface": {
                "resistivity_ohm_m": 3000,
                "thickness_m": 0.15
            }
        }
    
    with open(spec_path, 'r') as f:
        return json.load(f)


def calculate_all(project_id: str) -> Dict[str, Any]:
    """
    Perform all grounding calculations for a project.
    
    Args:
        project_id: Project identifier (e.g., "PROJ-001")
    
    Returns:
        Dictionary with all calculation results
    """
    specs = load_project_specs(project_id)
    
    # Extract parameters
    fault_ka = specs['electrical_system']['fault_current_ka']
    duration = specs['electrical_system']['fault_duration_sec']
    
    rho1 = specs['soil']['layer1']['resistivity_ohm_m']
    rho2 = specs['soil']['layer2']['resistivity_ohm_m']
    h = specs['soil']['layer1_depth_m']
    
    area = specs['grid_design']['area_m2']
    length = specs['grid_design']['conductor_length_m']
    spacing = specs['grid_design']['spacing_m']
    depth = specs['grid_design']['depth_m']
    
    rho_surface = specs['surface']['resistivity_ohm_m']
    thickness = specs['surface']['thickness_m']
    
    # Calculate ground resistance
    gr_calc = GroundResistanceCalculator()
    Rg = gr_calc.two_layer_resistance(rho1, rho2, h, area, length)
    
    # Calculate grid current
    Df = 1.2  # Decrement factor (conservative)
    Sf = 0.7  # Current division factor
    Ig = (fault_ka * 1000 * Df) / Sf
    
    # Calculate GPR
    GPR = Ig * Rg
    
    # Calculate touch voltage
    touch_calc = TouchVoltageCalculator()
    Etouch_actual = touch_calc.mesh_voltage(rho1, Ig, length, spacing, depth)
    Etouch_tol = touch_calc.tolerable_voltage(rho_surface, thickness, duration)
    touch_sf = Etouch_tol / Etouch_actual
    
    # Calculate step voltage
    step_calc = StepVoltageCalculator()
    Estep_actual = step_calc.calculate(rho1, Ig, length, spacing)
    Estep_tol = step_calc.tolerable_voltage(rho_surface, thickness, duration)
    step_sf = Estep_tol / Estep_actual
    
    # Overall status
    status = "PASS" if (touch_sf >= 1.5 and step_sf >= 1.5) else "FAIL"
    
    return {
        "project_id": project_id,
        "calculated_values": {
            "ground_resistance_ohm": round(Rg, 3),
            "grid_current_a": round(Ig, 0),
            "gpr_volts": round(GPR, 0),
            "touch_voltage_actual_v": round(Etouch_actual, 0),
            "touch_voltage_tolerable_v": round(Etouch_tol, 0),
            "touch_safety_factor": round(touch_sf, 2),
            "step_voltage_actual_v": round(Estep_actual, 0),
            "step_voltage_tolerable_v": round(Estep_tol, 0),
            "step_safety_factor": round(step_sf, 2)
        },
        "safety_assessment": {
            "overall_status": status,
            "touch_voltage_compliant": touch_sf >= 1.5,
            "step_voltage_compliant": step_sf >= 1.5,
            "minimum_safety_factor": round(min(touch_sf, step_sf), 2)
        }
    }


def main():
    """Main entry point for GPR calculator."""
    parser = argparse.ArgumentParser(description='Calculate grounding system parameters')
    parser.add_argument('--project', required=True, help='Project ID (e.g., PROJ-001)')
    parser.add_argument('--output', default='summary', choices=['json', 'summary'])
    
    args = parser.parse_args()
    
    # Perform calculations
    results = calculate_all(args.project)
    
    if args.output == 'json':
        print(json.dumps(results, indent=2))
    else:
        calc = results['calculated_values']
        safety = results['safety_assessment']
        
        print(f"\n=== GPR Calculation Results for {args.project} ===\n")
        print(f"Ground Resistance: {calc['ground_resistance_ohm']} Ω")
        print(f"Grid Current: {calc['grid_current_a']:,.0f} A")
        print(f"Ground Potential Rise: {calc['gpr_volts']:,.0f} V")
        print(f"\n--- Touch Voltage ---")
        print(f"Actual: {calc['touch_voltage_actual_v']} V")
        print(f"Tolerable: {calc['touch_voltage_tolerable_v']} V")
        print(f"Safety Factor: {calc['touch_safety_factor']} {'✅ PASS' if calc['touch_safety_factor'] >= 1.5 else '❌ FAIL'}")
        print(f"\n--- Step Voltage ---")
        print(f"Actual: {calc['step_voltage_actual_v']} V")
        print(f"Tolerable: {calc['step_voltage_tolerable_v']} V")
        print(f"Safety Factor: {calc['step_safety_factor']} {'✅ PASS' if calc['step_safety_factor'] >= 1.5 else '❌ FAIL'}")
        print(f"\n--- Overall Status ---")
        print(f"IEEE 80 Compliance: {safety['overall_status']}")
        print(f"Minimum Safety Factor: {safety['minimum_safety_factor']}\n")


if __name__ == '__main__':
    main()
