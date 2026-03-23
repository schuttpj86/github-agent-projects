# Section 2: The DNV Proposed Solution

**2.1 Approach**

DNV will execute a desktop-based analytical modelling study using DIgSILENT PowerFactory. The methodology is designed to meet the accelerated tender deadline by leveraging automated batch simulations. As the GE RS4 machines are classified as Grid Forming Synchronous (GBGF-S) assets operating at 0 MW, the study will utilise RMS dynamic simulations in accordance with the NESO Feasibility Study Requirements V6.

> **Reference:** NESO 05.2 LT2029 Stability Feasibility Study Requirements V6, Page 8: "For GBGF-S solutions RMS models are required."

The study will be conducted in three phases:

- **Modelling Phase:** Construction of the site-specific network models, including the Grid Entry Point (GEP) equivalents, export cables, step-up transformers, and integration of GE-provided RS4 machine and control models. Grid impedance data will be sourced from the NESO Stability Effectiveness Sheet V7.

- **Simulation Phase:** Development of a Python-based automation script to interface with the PowerFactory API. This script will execute the required simulations (21 per variant) with high-resolution data capture at 1ms intervals while eliminating manual execution errors. Test 2 simulations will be performed with voltage control enabled to maintain GEP voltage at 1 pu per V6 requirements.

- **Compliance Phase:** Automated extraction of performance metrics (short-circuit current at 40ms and inertia values per NESO Equation 1) to populate the NESO technical returns and verify compliance with the Stability Technical Specification. Feasibility Study Reports will follow the mandatory NESO Template V3, including withstand mode indication for all Test 3 simulations per V6.

---

## Simulation Count Derivation (NESO V6 for Zero-MW GBGF-S)

The GE RS4 operates at **0 MW active power** (synchronous condenser). NESO V6 specifies reduced test requirements for zero-MW solutions (unchanged from V5):

### Test 1: Short-Circuit Events
| Steps | Requirement | Reference |
|-------|-------------|-----------|
| Steps 1-4 | **SKIPPED** - "can be omitted for solutions that do not have the capability to export or import MW" | NESO V6, Page 9 |
| Steps 5-8 | **REQUIRED** (4 steps) | NESO V6, Page 12: "minimum of 4 (Steps 5-8) for zero MW solutions" |

**Test 1 Total: 4 simulations per variant**

### Test 2: Frequency/Inertia Events
| Steps | Requirement | Reference |
|-------|-------------|-----------|
| Steps 1-4 | **SKIPPED** - MW import/export conditions | NESO V6, Page 14 |
| Steps 5-12 | **REQUIRED** (8 steps) | NESO V6, Page 14: "only steps 5-12 and 14 are required" |
| Step 13 | **SKIPPED** - "does not need to be completed by 0MW solutions" | NESO V6, Page 18 |
| Step 14 | **REQUIRED** (1 step) | NESO V6, Page 18 |
| Step 15 | **SKIPPED** - "does not need to be completed by 0MW solutions" | NESO V6, Page 19 |

**Test 2 Total: 9 simulations per variant** (NESO V6, Page 20)

### Test 3: Voltage Angle Events
| Steps | Requirement | Reference |
|-------|-------------|-----------|
| All MW steps | **SKIPPED** - only zero-MW operating points required | NESO V6, Page 22 |
| Steps 5, 6, 11, 12, 17, 18, 23, 24 | **REQUIRED** (8 steps) | NESO V6, Page 22: "only steps 5, 6, 11, 12, 17, 18, 23 and 24 are required" |

**Test 3 Total: 8 simulations per variant** (NESO V6, Page 28)

---

### Summary: Simulation Count

| Test | Steps Required | Count | NESO V6 Reference |
|------|----------------|-------|-------------------|
| Test 1 (Short-Circuit) | 5, 6, 7, 8 | **4** | Page 9, 12 |
| Test 2 (Frequency/Inertia) | 5, 6, 7, 8, 9, 10, 11, 12, 14 | **9** | Page 14, 20 |
| Test 3 (Voltage Angle) | 5, 6, 11, 12, 17, 18, 23, 24 | **8** | Page 22, 28 |
| **Total per variant** | | **21** | |

**Tiered simulation totals:**

| Line Item | Variants | Total Simulations |
|-----------|----------|-------------------|
| Line 2 (2 sites x 1 option) | 2 | 42 |
| Line 3 (4 sites x 1 option) | 4 | 84 |
| Line 4 (6 sites x 2 options) | 12 | 252 |

> **Note:** Test 1 Step 8 involves remote faults at reference nodes. Depending on site-specific reference node requirements, additional Step 8 variants may apply.

---

**2.2 Deliverables**

The Client will receive the following deliverables per selected tier:

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | Technical Feasibility Study Report | Per NESO Feasibility Study Template V3, with narratives, time-series plots, and performance discussion for all 21 tests per variant |
| 2 | Completed Technical Proforma | Section B of LT2029 Stability Technical Proforma V5 (Q44-Q149) per variant |
| 3 | Simulation Datasets | CSV/Excel files with positive sequence RMS results, 1ms resolution, per NESO format |
| 4 | PowerFactory Models | Finalised project files (.pfd) for all site configurations in the selected tier |

> **Reference:** NESO Proforma V5 Section B (Feasibility Simulation) contains 106 questions (Q44-Q149), with response columns supporting up to 6 solutions.

**2.3 Alternative and Optional Work**

The following services are excluded from the line item scope but available on request (via Line Item 5 or separate instruction):

- **EMT Sensitivity Analysis:** Detailed EMT studies in PSCAD or PowerFactory if NESO/NGET requires sub-cycle transient verification for specific cable topologies.
- **Reactive Power Optimisation:** Sensitivity studies on transformer tap settings or impedances affecting regional effectiveness factors.

---
**Status:** REVISION 1 -- PENDING APPROVAL (2026-03-23)
