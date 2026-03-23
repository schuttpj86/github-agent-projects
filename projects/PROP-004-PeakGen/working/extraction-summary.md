# PRD: Peak Gen NESO LT2029 Stability Studies

**Revision 1 -- Updated 2026-03-23** (V6 requirements, tiered quotation structure)

## 1. Client Overview

| Field | Value |
|-------|-------|
| Client | Peak Gen |
| Contact | Karl (technical), client liaison |
| Project | NESO LT2029 Long-Term Stability Services Tender |
| Deadline | Mid to late April 2026 |
| NDA | Signed 2026-03-11 |

## 2. Client Requirement Summary

Peak Gen requires DNV to:
1. **Perform stability studies** per NESO LT2029 specifications (Feasibility Study Requirements V6)
2. **Provide simulation models** using RMS dynamic simulations (mandated for GBGF-S)
3. **Complete NESO proformas** (Section B of Technical Proforma V5, Q44-Q149)
4. **Author Feasibility Study Reports** per NESO Feasibility Study Template V3
5. **Enable tender submission** with a modular/tiered quotation to cover site permutations

### REV1: Tiered Quotation Structure

Per client email (2026-03-23), Peak Gen have not yet finalised their site selection and design options. They require a **tiered quotation** with 5 mutually exclusive line items:

| Line Item | Description |
|-----------|-------------|
| 1 | Setting up study model and scripts for reporting (one-time) |
| 2 | 2 sites x 1 option per site -- modelling, reports, NESO data entry |
| 3 | 4 sites x 1 option per site -- modelling, reports, NESO data entry |
| 4 | 6 sites x 2 options per site -- modelling, reports, NESO data entry |
| 5 | Future bid and design support on call-off T&M basis |

**Interpretation:** Lines 2/3/4 are mutually exclusive alternatives. Client selects Line 1 (setup) + one of Lines 2/3/4, optionally adding Line 5 for future support. Line 4 receives a volume discount reflecting automation efficiency gains.

## 3. Sites and Configurations

### Known Sites (from original RFP)

| # | Site | Grid Entry Point | Connection | Config Options | Models |
|---|------|------------------|------------|----------------|--------|
| 1 | Landulph | LAND2B 400kV | AIS, 1-2km HV cable | 4 or 8 RS4 | 2 |
| 2 | Indian Queens | INDQ2Q 400kV | AIS, 1-2km HV cable | 4 or 8 RS4 | 2-3 |
| 3 | Aberthaw | ABER2B 400kV | GIS, 1-2km HV cable | 4 or 8 RS4 | 2-3 |
| 4 | Wilton | WILT2B 400kV | AIS, 1-2km HV cable | 4 or 8 RS4 | 2-3 |

### REV1: Additional Sites (TBD)

The client email references up to **6 sites** but has not yet confirmed the 2 additional sites. The Effectiveness Sheet V7 lists 260+ eligible connection points across GB; the client will fix their site selection next week. The tiered quotation covers the permutation range.

**"2 options per site" (Line 4):** This likely refers to different RS4 configurations (e.g., 4 RS4 vs 8 RS4 per site), meaning each site would have 2 solution variants modelled.

### Site Data from Effectiveness Sheet V7

| Site | Sk'' (MVA) | X/R | Top Effectiveness | Reference Node |
|------|-----------|-----|-------------------|----------------|
| Wilton 275kV (WILT2) | ~3,870-3,879 | ~21 | 99.12% | Lackenby |
| Aberthaw 275kV (ABTH2) | 4,271 | 14.37 | 68.28% | Seabank |
| Indian Queens 400kV (INDQ4) | 4,325 | 12.06 | 100% | Indian Queens |
| Landulph 400kV (LAND4) | 4,278 | 12.38 | 91.5% | Exeter Main |

## 4. Equipment: GE RS4 Rotating Stabilizer

| Parameter | Value |
|-----------|-------|
| Type | Synchronous condenser (GBGF-S) |
| Rated MVA | 65 MVA per unit |
| Reactive range | +65/-40 MVAr |
| Inertia (H) | 2.5 s (per unit) |
| Stored energy | 162.5 MWs per unit |
| Short circuit | 5.9 kA (3-phase), 8.4 kA (1-phase) |
| Response time | <5 ms (inherent synchronous) |

### Per-Site Totals (8 RS4 configuration)
- **MVA:** 520 MVA
- **Reactive:** +520/-320 MVAr
- **Inertia:** 1,300 MWs
- **Fault current:** ~47 kA (aggregate)

## 5. NESO Technical Requirements (Updated to V6)

### 5.1 Service Categories
Per Technical Specification V3, stability services are:
- **Short Circuit Current Injection** -- Fault current contribution
- **Inertia** -- RoCoF response, stored energy
- **Voltage Stability** -- Reactive power, FRT capability

### 5.2 Study Requirements (per Feasibility Study Requirements V6)

#### Test 1: Short Circuit Events
- Steps 5-8 for zero-MW GBGF-S (4 simulations)
- **Key metric:** Reactive fault current at 40ms (kA) at GEP
- Response time must be ≤5ms
- V6: New "outcome" section making pass/fail criteria explicit (V6, Page 9)

#### Test 2: Frequency/Inertia Events
- Steps 5-12, 14 for zero-MW GBGF-S (9 simulations)
- **Key metric:** Minimum inertia per Equation 1 (MWs)
- Must demonstrate ≥5 successive inertial responses
- **V6 NEW:** Voltage control must be enabled during Test 2 to maintain GEP voltage at 1 pu (V6, Page 13)
- V6: NESO expects full written response on plant performance and limitations (V6, Page 21)

#### Test 3: Voltage Angle Change Events
- Steps 5,6,11,12,17,18,23,24 for zero-MW GBGF-S (8 simulations)
- Phase angle jumps up to 60 degrees
- **V6 NEW:** Must indicate if plant is in withstand mode or not for all simulations (V6, Page 22)
- V6: Detailed Phase Angle Jump assessment criteria added (V6, Pages 30-31)
- V6: Supplementary Guidance Note referenced for PAJ performance

### 5.3 Simulation Count (UNCHANGED from V5)

| Test | Steps (zero-MW GBGF-S) | Count | V6 Reference |
|------|------------------------|-------|-------------|
| Test 1 (Short-Circuit) | 5, 6, 7, 8 | **4** | Page 9, 12 |
| Test 2 (Frequency/Inertia) | 5, 6, 7, 8, 9, 10, 11, 12, 14 | **9** | Page 14, 20 |
| Test 3 (Voltage Angle) | 5, 6, 11, 12, 17, 18, 23, 24 | **8** | Page 22, 28 |
| **Total per variant** | | **21** | |

**Tiered simulation totals:**
- Line 2 (2 variants): 42 simulations
- Line 3 (4 variants): 84 simulations
- Line 4 (12 variants): 252 simulations

### 5.4 Model Requirements
- **Required for GBGF-S:** RMS dynamic simulations (V6, Page 8: "For GBGF-S solutions RMS models are required")
- **EMT:** Only for GBGF-I or Hybrid solutions (not applicable to RS4)
- Time step: ≤1ms for recording (V6, Page 7)
- Must record at Grid Entry Point and terminals

### 5.5 V6 New Requirements Summary

| V6 Addition | Applies to GBGF-S? | Impact on Scope |
|-------------|---------------------|-----------------|
| Voltage control enabled during Test 2 | Yes | Minor configuration detail |
| Withstand mode indication on Test 3 | Yes | Additional reporting per sim |
| "Voltage source behind impedance" in Table 1 | Yes (Tests 2, 3) | Formal criterion, covered by existing tests |
| Detailed PAJ assessment criteria (pp30-31) | Yes | Enhanced narrative in feasibility report |
| 4-point current limiting explanation | No (GBGF-I only) | N/A |
| Full written response on Test 2 performance | Yes | Additional narrative in feasibility report |

### 5.6 Deliverables per Site/Solution
1. **Feasibility Study Report** per NESO Feasibility Study Template V3 (NEW explicit template)
2. Time-series plots for all 21 tests per variant
3. Measurement dataset files (CSV/Excel, 1ms resolution)
4. Completed Section B of Technical Proforma V5 (Q44-Q149)
5. DRC data submission

## 6. Proforma Requirements (Section B, Technical Proforma V5)

**106 questions** (Q44-Q149) -- expanded from V4's 101 questions (Q44-Q144):

| Category | Questions | Key Outputs |
|----------|-----------|-------------|
| General | Q44-Q65 (22 Qs) | Setup validation, simulation type, recording confirmation |
| Test 1 (Fault Current) | Q66-Q111 (46 Qs) | kA at 40ms |
| Test 2 (Inertia) | Q112-Q134 (23 Qs) | MWs minimum |
| Test 3 (Voltage Angle) | Q135-Q149 (15 Qs) | Pass/Fail, withstand indication |

### V5 Proforma Changes from V4:
- 5 new questions added (Q145-Q149, Test 3 section)
- Scoring criteria clarified throughout (Column E: "V5: Scoring Criteria")
- New Q53: Frequency/RoCoF recorded at GEP?
- New Q54: Tap changer positions recorded?
- New Q59: RMS computation explanation provided?
- New Q116: Test 2 performed with voltage control enabled?
- New Q136: Alternative angle for steps 19-24 explained?
- Solutions columns support up to 6 solutions (adequate for all tiers)

## 7. DNV Scope of Work (Tiered Structure)

### Line Item 1: Study Setup (One-Time)
- Project kick-off meeting and coordination
- Review and validate NESO grid data (Effectiveness Sheet V7, Connection Feasibility Reports)
- Assess GE RS4 PowerFactory models for RMS simulation compatibility
- Develop Python automation script (PowerFactory API) for batch simulation execution
- Create reporting framework (automated extraction, time-series plot generation)

### Line Item 2: 2 Sites x 1 Option (2 variants)
- Build 2 network models in PowerFactory (GEP, export cables, step-up transformers, RS4 integration)
- Execute 42 simulations (2 x 21 tests per V6)
- Extract data, populate 2 Section B proformas (Q44-Q149)
- Author 2 Feasibility Study Reports per NESO Template V3
- Senior peer review of 2 variants

### Line Item 3: 4 Sites x 1 Option (4 variants)
- Build 4 network models
- Execute 84 simulations (4 x 21)
- Populate 4 proformas, author 4 feasibility reports
- Senior peer review of 4 variants

### Line Item 4: 6 Sites x 2 Options (12 variants)
- Build 6 network models with 2 configuration variants each
- Execute 252 simulations (12 x 21)
- Populate 12 proformas, author 12 feasibility reports
- Senior peer review of 12 variants
- **Volume discount applied** -- automation scripts reused across all variants

### Line Item 5: Future Bid and Design Support (T&M)
- Advisory services on call-off basis at DNV 2026 T&M rates
- Additional variants, sensitivity studies, NESO query responses
- EMT verification if requested by NESO/NGET

## 8. Assumptions and Exclusions

### Assumptions
- GE provides validated RS4 RMS model (PowerFactory compatible, open format)
- NGET connection data available per site
- Client confirms final site/config selection before modelling commences
- Network impedance data from NESO Effectiveness Sheet V7
- Line Item 1 (setup) is required regardless of which tier is selected
- Client selects one of Lines 2/3/4 (mutually exclusive tiers)
- One round of draft review per variant is included

### Exclusions
- Physical site surveys
- Grid Code compliance beyond LT2029 scope
- Post-tender contract negotiations
- Construction or commissioning support
- EMT simulations (GBGF-S does not require EMT per V6)

## 9. Schedule Constraints

| Milestone | Target |
|-----------|--------|
| Client fixes sites and options | Next week (per email) |
| Proposal submission | [TBD] |
| Study commencement | [TBD] |
| Draft results | [TBD] |
| Final deliverables | Mid-April 2026 |
| NESO tender deadline | Late April 2026 |

**Per-tier indicative durations:**
- Line 2 (2 variants): 3-4 weeks from NTP
- Line 3 (4 variants): 4-5 weeks from NTP
- Line 4 (12 variants): 6-8 weeks from NTP

## 10. Commercial Considerations

- **Pricing model:** Tiered modular quotation (5 line items, Lines 2/3/4 mutually exclusive)
- **Line 1:** Fixed fee for one-time setup (kick-off, data review, scripts, framework)
- **Lines 2/3/4:** Fixed fee per tier (modelling, simulation, reporting, proforma)
- **Line 4:** Volume discount applied for automation efficiency on 12 variants
- **Line 5:** T&M call-off at DNV 2026 rates
- **Effort drivers:** Number of variants, additional review cycles, NESO queries

---

## Clarifications (User Approved)

- Model outputs: Base scope defined by selected tier; Lines 2/3/4 are mutually exclusive
- Schedule: Milestones to be defined with customer post-award
- GE models: Expected available at project start (assumption)
- REV1: Lines 2/3/4 are mutually exclusive tiers (user confirmed)
- REV1: Volume discount for Line 4 (user confirmed)
- REV1: Additional site names to be confirmed by client (Effectiveness Sheet V7 checked, lists 260+ eligible sites)

---

## Source Documents

| Document | Key Content Used |
|----------|------------------|
| initial proposal.md | Client brief, sites, timeline |
| 05 LT2029 Stability Service Technical Specification V3.pdf | Service definitions |
| 05.2 LT2029 Stability Feasibility Study Requirements V5.pdf | Test methodology (SUPERSEDED by V6) |
| **05.2 LT2029 Stability Feasibility Study Requirements V6.pdf** | **Test methodology, V6 clarifications** |
| 2. LT2029 Stability Technical Proforma V4.xlsx | Submission requirements (SUPERSEDED by V5) |
| **2. LT2029 Stability Technical Proforma V5.xlsx** | **Submission requirements, Q44-Q149** |
| **05.1 LT2029 Stability Effectiveness Sheet V7.xlsx** | **Grid impedance, fault data, effectiveness factors** |
| **2.1 LT2029 Stability Feasibility Study Template V3.docx** | **Mandatory report format** |
| LT2029 NGET Connection Feasibility Report V1 Final_.pdf | Site/bay details |
| Appendix A_Preliminary RS4 Datasheet.pdf | Equipment parameters |
| Tech note on 2off RS4 machines per Tx secondary.pdf | Configuration options |
| Peak Gen - DNV NDA_20260311_Signed.pdf | NDA |
| RE_ Peak Gen - NESO LT29 Stability Studies Quotation Request/email.md | Tiered quotation request |

---

**PRD Status:** REVISION 1 -- PENDING APPROVAL (2026-03-23)
