# DNV Proposal: Peak Gen NESO LT29 Stability Studies
**Revision 1 -- 2026-03-23**

---

# Section 1: Introduction

Peak Gen has requested DNV to provide stability study services in support of their submission to the NESO Long-Term 2029 (LT29) Stability Services tender. The project involves up to six sites across England and Wales, each proposing GE RS4 Rotating Stabilizers to provide grid stability services including short circuit current injection, inertia, and voltage support.

DNV will perform RMS dynamic simulations using DIgSILENT PowerFactory per NESO Technical Specification V3 and Feasibility Study Requirements V6. As the RS4 machines are Grid Forming Synchronous (GBGF-S) assets, RMS modelling is the NESO-mandated approach. DNV will complete the required Section B proformas and author Feasibility Study Reports per NESO Template V3 to enable Peak Gen's tender submission, with target completion in mid-April 2026.

This proposal presents a modular quotation with five line items, allowing Peak Gen to select the scope that matches their final site and design option decisions:

| Line Item | Description |
|-----------|-------------|
| 1 | Study setup: model development, automation scripts, and reporting framework |
| 2 | 2 sites x 1 option per site (modelling, reports, NESO data entry) |
| 3 | 4 sites x 1 option per site (modelling, reports, NESO data entry) |
| 4 | 6 sites x 2 options per site (modelling, reports, NESO data entry) |
| 5 | Future bid and design support on call-off T&M basis |

Line Item 1 is required regardless of the selected tier. The Client selects one of Line Items 2, 3, or 4 based on their finalised site portfolio. Line Item 5 provides ongoing advisory support after the initial study phase.

---

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

# Section 4: Schedule

The project schedule depends on the selected line item tier. All tiers share a common setup phase (Line Item 1), with the site-specific work (Lines 2/3/4) scaling in duration with the number of variants. This schedule is designed to facilitate a final tender submission by the mid-to-late April 2026 deadline.

**Indicative Durations from NTP:**

| Tier | Variants | Duration | Target Completion |
|------|----------|----------|-------------------|
| Line 2 (2 sites x 1 option) | 2 | 3-4 weeks | Mid-April 2026 |
| Line 3 (4 sites x 1 option) | 4 | 4-5 weeks | Mid-to-late April 2026 |
| Line 4 (6 sites x 2 options) | 12 | 6-8 weeks | May 2026 |

**Schedule: Line Item 3 (4 variants, representative)**

| Week | Milestone | Activities |
|------|-----------|------------|
| 1 | Project Kick-off and Data Freeze | Receipt of NESO Effectiveness Sheet V7, GE PowerFactory models, final site specifications |
| 2 | Network Modelling Complete | Site-specific models and steady-state initialisation for 4 variants |
| 3 | Simulations Complete | Automated execution of 84 test runs and raw data extraction |
| 4 | Draft Deliverables | Draft Feasibility Study Reports (per NESO Template V3) and populated Section B proformas for Client review |
| 5 | Final Handover | Implementation of final adjustments and delivery of tender-ready documents |

For Line Item 2, Weeks 2-3 compress to a single week. For Line Item 4, Weeks 2-4 extend to accommodate 12 variants, with modelling and simulation activities running in parallel batches.

**Key Dependencies:**

This schedule is strictly dependent upon the timely provision of data by the Client and third parties:

- GE RS4 PowerFactory models (assumed available at project start per PRD)
- NESO Stability Effectiveness Sheet V7 data for selected sites
- Final site cable and transformer specifications

Any delays in receiving input data will result in a corresponding adjustment to the final delivery date.

**Deliverable Schedule (per selected tier):**

| Deliverable | Target |
|-------------|--------|
| Draft Feasibility Study Reports + Section B Proformas | 1 week before completion |
| Final Reports + Proformas | Final week |
| PowerFactory Models | With Final Reports |
| Simulation Datasets | With Final Reports |

---

# Section 5: Compensation

**5.1 Pricing Structure**

DNV proposes a modular fixed-fee quotation with five line items. The Client selects Line Item 1 (required) plus one of Line Items 2, 3, or 4 depending on the finalised site portfolio. Line Item 5 is available as an optional call-off for future support.

| Line Item | Description | Variants | Hours | Fee |
|-----------|-------------|----------|-------|-----|
| 1 | Study Setup (model, scripts, reporting framework) | -- | 112h | **EUR 18,596** |
| 2 | 2 sites x 1 option (modelling, reports, NESO data entry) | 2 | 151h | **EUR 24,737** |
| 3 | 4 sites x 1 option (modelling, reports, NESO data entry) | 4 | 292h | **EUR 48,062** |
| 4 | 6 sites x 2 options (modelling, reports, NESO data entry) | 12 | 540h | **EUR 88,314** |
| 5 | Future bid and design support | -- | -- | T&M rates |

**Total fees (Line 1 + selected tier):**

| Combination | Hours | Total Fee |
|-------------|-------|-----------|
| Line 1 + Line 2 (2 variants) | 263h | **EUR 43,333** |
| Line 1 + Line 3 (4 variants) | 404h | **EUR 66,658** |
| Line 1 + Line 4 (12 variants) | 652h | **EUR 106,910** |

**5.2 Fee Breakdown by Line Item**

Detailed hour and cost breakdowns per line item:

**Line Item 1: Study Setup**

| Activity | Hours | Amount |
|----------|-------|--------|
| Project kick-off and coordination | 7h | EUR 1,189 |
| Data review (NGET reports) | 12h | EUR 1,916 |
| Validate NESO grid data (Effectiveness Sheet V7) | 7h | EUR 1,189 |
| GE RS4 model assessment | 14h | EUR 2,378 |
| Automation script development (PowerFactory API) | 26h | EUR 4,294 |
| Reporting framework (data extraction, plots, proforma) | 19h | EUR 3,105 |
| GE RS4 model integration and AVR setup | 20h | EUR 3,336 |
| Contingency (5%) | 7h | EUR 1,189 |
| **Line 1 Total** | **112h** | **EUR 18,596** |

**Line Item 2: 2 Sites x 1 Option (2 Variants)**

| Activity | Hours | Amount |
|----------|-------|--------|
| Network modelling and validation (2 sites) | 36h | EUR 5,832 |
| Simulation execution (42 runs) | 30h | EUR 4,790 |
| Data extraction and proforma population (2 variants) | 32h | EUR 5,252 |
| Feasibility reporting (2 reports) and plots | 28h | EUR 4,874 |
| Peer review and finalisation | 16h | EUR 2,466 |
| Contingency (5%) | 9h | EUR 1,523 |
| **Line 2 Total** | **151h** | **EUR 24,737** |

**Line Item 3: 4 Sites x 1 Option (4 Variants)**

| Activity | Hours | Amount |
|----------|-------|--------|
| Network modelling and validation (4 sites) | 73h | EUR 11,895 |
| Simulation execution (84 runs) | 56h | EUR 9,273 |
| Data extraction and proforma population (4 variants) | 58h | EUR 8,937 |
| Feasibility reporting (4 reports) and plots | 56h | EUR 9,168 |
| Peer review and finalisation | 33h | EUR 5,163 |
| Contingency (5%) | 16h | EUR 2,626 |
| **Line 3 Total** | **292h** | **EUR 48,062** |

**Line Item 4: 6 Sites x 2 Options (12 Variants)**

| Activity | Hours | Amount |
|----------|-------|--------|
| Network modelling and validation (6 sites, 2 options each) | 107h | EUR 17,265 |
| Simulation execution (252 runs) | 112h | EUR 17,853 |
| Data extraction and proforma population (12 variants) | 113h | EUR 18,223 |
| Feasibility reporting (12 reports) and plots | 110h | EUR 17,874 |
| Peer review and finalisation | 69h | EUR 10,326 |
| Contingency (5%) | 29h | EUR 4,773 |
| **Line 4 Total** | **540h** | **EUR 88,314** |

> **Note:** Line Item 4 includes a volume discount reflecting automation efficiency gains across 12 variants. The per-variant cost for Line 4 (EUR 7,360) is approximately 39% lower than Line 3 (EUR 12,016 per variant).

Prices are quoted in EUR, exclusive of VAT.

**5.3 Line Item 5: T&M Rates**

Future bid and design support under Line Item 5 will be invoiced on a time and materials basis at DNV's standard 2026 rates:

| Grade | Role | Hourly Rate |
|-------|------|-------------|
| 5-7 | Professional | EUR 145/hour |
| 8-9 | Senior | EUR 189/hour |
| 10-11 | Principal | EUR 231/hour |

**5.4 Payment Terms**

| Milestone | % of Fee | Applies To |
|-----------|----------|------------|
| Project Kick-off (NTP) | 30% | Line 1 + selected tier |
| Draft Deliverables | 40% | Line 1 + selected tier |
| Final Handover | 30% | Line 1 + selected tier |

Line Item 5 (T&M) will be invoiced monthly in arrears.

**5.5 Validity**

This quotation is valid for 60 days from the date of issue.

---

# Section 6: Project Organisation

**6.1 Project Team**

| Role | Name | Responsibility |
|------|------|----------------|
| Project Manager | [TBD] | Overall delivery, client liaison, schedule management |
| Lead Engineer | [TBD] | Technical direction, model review, report authorship |
| Power Systems Engineer | [TBD] | Network modelling, simulation execution, data extraction |
| Reviewer | [TBD] | Independent QA of models and deliverables |

**6.2 Client Responsibilities**

The Client shall provide:
- Timely access to GE RS4 PowerFactory models
- Final site and design option selection (tier confirmation) before modelling commences
- Review comments on draft deliverables within 5 working days
- Single point of contact for technical queries

**6.3 Third Party Interfaces**

| Party | Interface | Purpose |
|-------|-----------|---------|
| GE | Model provision | RS4 machine and control models |
| NESO | Data provision | Effectiveness factors, proforma clarifications |
| NGET | Data provision | Connection data per Feasibility Report |

**6.4 Communication**

- Kick-off meeting: Week 1 (virtual or in-person)
- Progress updates: Weekly email summary
- Draft review meeting: 1 week before completion
- Final handover: per tier schedule

---

# Section 7: Contractual

**7.1 Assumptions**

This proposal is based on the following assumptions:

- GE RS4 PowerFactory models are provided in a validated, simulation-ready state at project start
- NESO Stability Effectiveness Sheet V7 data and connection data sheets are available before modelling commences
- Client confirms the selected line item tier and site/design option selection before Week 1 data freeze
- Line Item 1 (study setup) is required regardless of the selected tier
- Lines 2, 3, and 4 are mutually exclusive; the Client selects one based on their finalised site portfolio
- One round of draft review comments per variant is included; additional review cycles may incur additional fees
- All simulations are performed using DIgSILENT PowerFactory; alternative software platforms are excluded
- Feasibility Study Reports will be authored per NESO Feasibility Study Template V3
- Technical Proforma V5 Section B (Q44-Q149) will be completed per variant

**7.2 Limitations**

- DNV's services are limited to desktop simulation studies; no physical site activities are included
- Results are based on the models and data provided; DNV does not warrant actual field performance
- Grid Code compliance assessment is limited to the NESO LT2029 requirements per Feasibility Study Requirements V6; broader ECC compliance is excluded
- DNV is not responsible for delays caused by late provision of third-party data
- The volume discount on Line Item 4 is conditional on all 12 variants being confirmed at NTP; partial activation is not supported

**7.3 Intellectual Property**

- Deliverables (reports, proformas, datasets) become Client property upon final payment
- PowerFactory models remain DNV intellectual property with perpetual licence to Client for this project
- GE RS4 models remain GE intellectual property

**7.4 Confidentiality**

This work is subject to the executed NDA between DNV and Peak Gen dated 11 March 2026.

**7.5 Terms and Conditions**

DNV's standard Terms and Conditions for consultancy services apply unless otherwise agreed.

---

# Section 8: Acceptance

**8.1 Proposal Acceptance**

To accept this proposal, please sign and return a copy of this document or issue a Purchase Order referencing this proposal number.

**8.2 Validity Period**

This proposal is valid for 60 days from the date of issue. After this period, DNV reserves the right to revise pricing and availability.

**8.3 Acceptance Signatures**

| | DNV | Client |
|---|-----|--------|
| **Name** | [TBD] | |
| **Title** | [TBD] | |
| **Date** | | |
| **Signature** | | |

**8.4 Contact**

For questions regarding this proposal, please contact:

**DNV Energy Systems**
[DNV Contact Name]
[Email]
[Phone]
