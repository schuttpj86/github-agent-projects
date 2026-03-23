# DNV Proposal Structure Reference

This document details each section of the standard DNV proposal template and what content belongs in each.

## Cover Page

The cover page contains document metadata. Fill in these fields:

| Field | Source | Notes |
|-------|--------|-------|
| Proposal Title | Tender documents | Use client's project name |
| Customer Reference | Tender documents | RFQ/RFP reference number |
| DNV doc No | Auto-generated or placeholder | Format: XXXX-XXXX-X |
| Date of first issue | Current date | YYYY-MM-DD format |
| Validity | Standard 3 months | "3 months from date of issue" |
| Customer Details | Tender documents | Name, address, contact person |
| DNV Details | Template standard | Usually pre-filled |

## Section 1: INTRODUCTION

Three paragraphs maximum. Structure:

**Paragraph 1 - Client Objective:**
State what the client wants to achieve. Source this directly from the tender/RFQ background section. Example:
> "Peak Gen is pursuing participation in the NESO LT29 Long-Term Stability Services tender, which requires completion of system stability studies for four proposed rotating stabilizer sites across the UK transmission network."

**Paragraph 2 - DNV Understanding:**
State what DNV understands the specific problem to be and the boundaries of the scope. Example:
> "To support this submission, Peak Gen requires an engineering partner to perform the stability feasibility studies and model submissions as specified in the NESO LT2029 Stability Service Technical Specification V3."

**Paragraph 3 - Submission Statement:**
Standard closing. Example:
> "DNV is pleased to submit this proposal to provide the requested engineering and advisory services."

## Section 2: THE DNV PROPOSED SOLUTION

### 2.1 Approach

Explain the methodology DNV will use. Key elements:
- Phased or sequential approach (if applicable)
- Desktop study vs. site work
- Modelling tools and standards
- Interaction with client and third parties

**CRITICAL: Validate methodology against tender spec.** For example:
- NESO stability studies: Verify EMT vs RMS requirement (GBGF-S uses RMS, GBGF-I may require EMT)
- Grid code compliance: Verify which standards apply

Always quote the source:
> "DNV will utilise RMS dynamic simulations in accordance with the NESO Feasibility Study Requirements V5, which states: 'For GBGF-S solutions RMS models are required' (Page 7)."

**Include derivation tables for scope calculations:**

If the number of tests/simulations is derived from spec, include a reference table:

```
### Simulation Count Derivation (per NESO V5)

| Test | Steps Required | Count | NESO V5 Reference |
|------|----------------|-------|-------------------|
| Test 1 (Short-Circuit) | 5, 6, 7, 8 | 4 | Page 8, 11 |
| Test 2 (Frequency/Inertia) | 5-12, 14 | 9 | Page 13, 19 |
| Test 3 (Voltage Angle) | 5,6,11,12,17,18,23,24 | 8 | Page 20-21, 26 |
| **Total per variant** | | **21** | |
| **Base scope (N variants)** | | **N×21** | |
```

Example structure:
> "DNV proposes to complete the stability studies in accordance with the NESO requirements using the following approach..."

### 2.2 Deliverables

Bulleted list of tangible outputs. Be specific about:
- Document titles
- Formats (report, spreadsheet, model files)
- What each deliverable contains

Example:
```
- Technical Report: Stability Feasibility Study for [Site Name]
- Completed NESO Technical Proforma (Tab 4)
- PSCAD/PSS®E Model Files (as applicable)
```

### 2.3 Alternative and/or Optional Work

List 1-3 services that are related but outside base scope. These are value-adds the client may want. Include:
- Brief description
- Why it would benefit the client
- That it would be quoted separately

## Section 3: SCOPE OF WORK

The most detailed section. Structure work into sequential Tasks.

**Task Naming Convention:**
- Task 1: Project Initiation / Data Gathering
- Task 2: [Primary technical work]
- Task 3: [Secondary technical work]
- Task N: Reporting / Deliverable Compilation

**Each Task Should Include:**
- Task number and title (bold)
- 2-4 bullet points with specific activities
- Begin bullets with action verbs (Assess, Perform, Develop, Specify, Evaluate, Validate, Review, Prepare)
- Reference specific standards (IEC, IEEE, NESO specs)
- Reference specific deliverables from Section 2.2

**Example Task:**
```
Task 2: System Stability Studies

- Perform small-signal stability analysis in accordance with NESO LT2029 Stability Service Technical Specification V3, Section 4.2
- Develop PSCAD models of the proposed RS4 rotating stabilizer configuration
- Execute fault ride-through simulations as specified in Grid Code CC.6.3.15
- Validate dynamic response against NESO acceptance criteria
```

## Section 4: SCHEDULE

Define timeline from Notice to Proceed (NTP).

**Include:**
- Total project duration in weeks
- Key milestones with week numbers
- Dependencies on client data provision

**Standard Format:**
```
The project will be completed within [X] weeks from Notice to Proceed (NTP), subject to timely provision of required input data by the Client.

Key Milestones:
- Week 1: Kick-off meeting and data receipt confirmation
- Week 3: Draft Basis of Design for Client review
- Week 6: Draft Technical Report
- Week 8: Final Report submission
```

**Placeholder if Timeline Not in Tender:**
> "[TBD: Project timeline to be confirmed based on Client requirements]"

## Section 5: COMPENSATION

### 5.1 General

State pricing basis:
- Lump sum or Time and Materials
- Currency (EUR, GBP, USD)
- Exclusions (VAT, local taxes)

### 5.2 Lump Sums

Table format:

| Task | Description | Amount |
|------|-------------|--------|
| Task 1 | Project Initiation | [Amount] EUR |
| Task 2 | Stability Studies | [Amount] EUR |
| **Total** | | **[Total] EUR** |

If pricing not yet determined, use placeholders.

### 5.3 Rates and Expenses

Standard text about travel cost recovery. Example:
> "Travel and accommodation will be charged at cost. Mileage at EUR 0.35/km."

### 5.4 Budget

"Not applicable" for fixed lump sum projects.

### 5.5 Adjustment of Lump Sums

Standard validity statement:
> "Prices are valid for 3 months from the date of this proposal. After this period, standard DNV annual rate adjustments may apply."

### 5.6 Invoicing and Payment

Milestone payment schedule. Example:
```
- 30% on acceptance of this proposal
- 60% on delivery of draft report
- 10% on final acceptance
Payment terms: 30 days net from invoice date.
```

## Section 6: PROJECT ORGANISATION

### 6.1 Organigram

Placeholder for diagram:
> "[Insert DNV Project Organisation Chart]"

### 6.2 Key Personnel

Table format:

| Name | Role | Key Qualification |
|------|------|-------------------|
| [TBD] | Project Sponsor/QA | Senior Engineer, 15+ years experience |
| [TBD] | Project Manager | Grid integration specialist |
| [TBD] | Technical Lead | Power systems modelling expert |

If names not yet assigned, use "[TBD]" with role descriptions.

### 6.3 Resource Pool

Standard statement:
> "DNV will draw upon its global pool of qualified engineers to provide flexibility and additional expertise as required."

### 6.4 Contact Information

Project Manager contact details table. Use placeholder if not assigned.

## Section 7: CONTRACTUAL

### 7.1 Contract Basis

Standard reference:
> "This proposal is governed by the DNV General Terms and Conditions for Advisory Services, Energy Systems, a copy of which is available upon request."

### 7.2 Assumptions, Conditions and Limitations

**CRITICAL SECTION** - List 4-6 specific assumptions:

- What data the client must provide
- What is explicitly excluded from scope
- What third-party dependencies exist
- Physical or technical boundaries

Example:
```
- Client will provide OEM datasheets for the RS4 rotating stabilizers
- Dynamic models provided by third parties are assumed to be validated
- Site access is not included; all work is desktop-based
- NESO submission process itself is the Client's responsibility
- This proposal covers [X] sites only; additional sites quoted separately
```

### 7.3 Mandatory Health and Safety Terms

Three standard sub-sections (usually pre-filled in template):
- 7.3.1 Customer Responsibility
- 7.3.2 Main Principle (Right to refuse unsafe work)
- 7.3.3 Substance Abuse Screening

## Section 8: ACCEPTANCE

**Closing Statement:**
> "We look forward to the opportunity to support [Client Name] with this important project and remain available to discuss any aspects of this proposal."

**Instructions:**
> "To proceed, please sign and return this proposal to Salesdesk@dnv.com."

**Signature Block:**
```
Customer Acceptance:

Name: _______________________
Title: _______________________
Date: _______________________
Signature: ___________________
```
