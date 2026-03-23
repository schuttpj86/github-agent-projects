# Section 3: Scope of Work

The work is organised into five line items aligned with the Client's tiered quotation request. Line Item 1 covers one-time setup activities required regardless of scope. Line Items 2, 3, and 4 are mutually exclusive tiers covering the site-specific modelling, simulation, and reporting scope. Line Item 5 provides ongoing support on a T&M basis.

---

## Line Item 1: Study Setup (One-Time)

This line item covers all preparatory activities that are independent of the number of sites or variants.

- Facilitate a project kick-off meeting to confirm the selected tier, finalise site parameters, and agree the data freeze date
- Review and extract connection asset data from the NGET Connection Feasibility Reports for all sites in the selected tier
- Validate the NESO equivalent grid data, including System Impedance and Fault Impedance from the Stability Effectiveness Sheet V7
- Assess the GE-provided PowerFactory models to ensure compatibility with the RMS simulation environment
- Develop a Python automation script utilising the PowerFactory API for batch simulation execution across all three NESO test types (21 simulations per variant)
- Develop an automated reporting framework for time-series data extraction, plot generation, and NESO proforma population

---

## Line Item 2: 2 Sites x 1 Option (2 Variants)

This line item covers the full modelling, simulation, and reporting scope for 2 sites with 1 design option per site.

**Network Modelling**
- Develop 2 network models in PowerFactory representing the Grid Entry Points (GEP) for the Client's selected sites
- Model the local connection infrastructure including export cables and step-up transformers
- Integrate the GE RS4 synchronous machine models with excitation systems and AVR
- Perform steady-state load flow initialisation to verify pre-fault voltage compliance (0.95-1.05 pu)

**Simulation Execution**
- Execute **42 simulations** (21 tests x 2 variants) using the automation scripts developed under Line Item 1
- Test 2 simulations performed with voltage control enabled per NESO V6
- Record all results at ≤1ms time step resolution

| Test | Per Variant | Description | NESO V6 Reference |
|------|-------------|-------------|-------------------|
| Test 1 | 4 steps | Three-phase faults at GEP (Steps 5-8 for 0MW) | Page 9, 12 |
| Test 2 | 9 steps | Frequency ramp events (Steps 5-12, 14 for 0MW) | Page 14, 20 |
| Test 3 | 8 steps | Phase angle jumps up to 60 degrees (Steps 5,6,11,12,17,18,23,24) | Page 22, 28 |
| **Total** | **21** | | |

**Data Extraction and Proforma Population**
- Extract high-resolution positive sequence RMS time-series data for all parameters
- Calculate performance metrics: reactive short-circuit contribution at 40ms post-fault (kA), effective inertia per NESO Equation 1 (MWs)
- Populate NESO Technical Proforma V5 Section B (Q44-Q149) for 2 variants

**Technical Feasibility Reporting**
- Author 2 Feasibility Study Reports per NESO Template V3, including withstand mode indication for Test 3 per V6
- Generate and format all time-series plots as evidence
- Perform senior technical peer review to ensure all NESO Pass/Fail criteria are addressed

---

## Line Item 3: 4 Sites x 1 Option (4 Variants)

This line item covers the same scope as Line Item 2, scaled to 4 sites with 1 design option per site. **Line Items 2 and 3 are mutually exclusive; the Client selects one.**

- Develop **4 network models** in PowerFactory
- Execute **84 simulations** (21 tests x 4 variants)
- Populate **4 Section B proformas** (Q44-Q149)
- Author **4 Feasibility Study Reports** per NESO Template V3
- Senior technical peer review of all 4 variants

---

## Line Item 4: 6 Sites x 2 Options (12 Variants)

This line item covers the full scope for 6 sites with 2 design options per site (e.g., 4 RS4 and 8 RS4 configurations). **Line Items 2, 3, and 4 are mutually exclusive; the Client selects one.**

- Develop **6 network models** in PowerFactory, each with 2 configuration variants
- Execute **252 simulations** (21 tests x 12 variants)
- Populate **12 Section B proformas** (Q44-Q149)
- Author **12 Feasibility Study Reports** per NESO Template V3
- Senior technical peer review of all 12 variants

A volume discount is applied to this line item reflecting the efficiency gains from reusing the automation scripts and reporting framework across a larger number of variants.

---

## Line Item 5: Future Bid and Design Support (T&M)

Advisory services available on a call-off basis at DNV's standard 2026 T&M rates:

- Additional solution variants or sensitivity studies beyond the selected tier
- NESO query responses and clarification support during tender evaluation
- EMT verification studies if requested by NESO/NGET
- Post-award design support and model updates

---

## Scope Validation Summary

| Item | Line 2 | Line 3 | Line 4 | Source |
|------|--------|--------|--------|--------|
| Sites | 2 | 4 | 6 | Client brief |
| Options per site | 1 | 1 | 2 | Client brief |
| Variants | 2 | 4 | 12 | Sites x Options |
| Tests per variant | 21 | 21 | 21 | NESO V6 (0MW scope) |
| Total simulations | 42 | 84 | 252 | Variants x 21 |
| Proforma questions | Q44-Q149 | Q44-Q149 | Q44-Q149 | NESO Proforma V5 Section B |
| Time step | ≤1ms | ≤1ms | ≤1ms | NESO V6 Page 7 |

---
**Status:** REVISION 1 -- PENDING APPROVAL (2026-03-23)
