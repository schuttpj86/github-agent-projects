**Project Kick- Tilburg Substation EMC**

**Project:** Advisory services Tilburg Substation EMC
**Client:** SC&M II V.O.F. | **End Client:** TenneT
**DNV Reference:** 00431480-TDT 25-1641

### 1 PROJECT OBJECTIVE

To conduct a Conductive influence evaluation for the new Tilburg substation project, focusing on the impact of short circuits on nearby 3rd party metallic objects (pipelines, data cables, fences, etc.) based on NEN 3654:2023 and EN 50522.

A critical objective is to address the specific challenge regarding high soil resistivity (approx. 500 $\Omega\cdot m$) which currently results in a calculated station resistance ($R_a$) of 0.931 $\Omega$ and a potential Ground Potential Rise (GPR) of up to 27.1 kV. The study aims to verify these values and determine if mitigation is required for nearby assets.

### 2 SCOPE OF WORK & METHODOLOGY

DNV will execute the project in the following phases:

**Task 1: Analytical Modeling & Danger Zone Assessment**

* **Activity:** Perform initial analytical modeling to determine the Ground Potential Rise (GPR) and identify the immediate danger zones.
* **Output:** High-level identification of assets falling within critical influence areas.

**Task 2: Data Verification (KLIC vs. Reality)**

* **Activity:** Verification of input data. Specifically, clarifying the status of the pipeline indicated on current KLIC data (which is believed to be removed) versus the actual site conditions.
* **Requirement:** Client to provide updated "Click data" or as-built drawings to ensure the model does not calculate interference for non-existent assets.

**Task 3: Detailed Simulation (CDEGS/XGSLAB)**

* **Activity:** Preparation of a detailed electrode model based on substation design inputs.
* **Simulation:** Calculation of voltage rise in the soil using a fault current of 29.1 kA.
* **Analysis:** Plotting results on the terrain against updated asset locations to check compliance with limits.

**Task 4: Reporting**

* **Activity:** detailed EMC influence report including calculations and mitigation recommendations (if applicable within the 16-hour scope).

### 3 KEY DELIVERABLES

DNV will deliver the following:

1. **EMC Influence Report:** A comprehensive report in English including detailed calculations, methodology, and results plotted against terrain data.

### 4 SCHEDULE & TIMELINE

*The timeline is based on a 14-week duration as per the proposal.*

| Milestone    | Activity                           | Baseline Date        | Current Forecast     | Status            | Comments / Changes                               |
| :----------- | :--------------------------------- | :------------------- | :------------------- | :---------------- | :----------------------------------------------- |
| **T0** | **Project Start / Kick-off** | **05-12-2025** | **05-12-2025** | **PENDING** | Kick-off meeting scheduled.                      |
| **M1** | Data Collection / Verification     | 19-12-2025           | 19-12-2025           | PLANNED           | Critical: Confirmation of removed pipeline data. |
| **M2** | Draft Report Delivery              | 12-02-2026           | 12-02-2026           | PLANNED           | Based on 14-week schedule minus review time.     |
| **M3** | Client Review Period               | 26-02-2026           | 26-02-2026           | PLANNED           | 2 weeks allocated for stakeholder feedback.      |
| **M4** | **Final Delivery**           | **12-03-2026** | **12-03-2026** | **PLANNED** | Final version.                                   |

### 5 MINUTES OF MEETING & ACTION LOG

*Project: Tilburg Substation EMC*

| ID            | Category | Description                                                                                                                                                         | Owner         | Due Date   | Latest Status / Comments                                                               | Status         |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------ | :--------- | :------------------------------------------------------------------------------------- | :------------- |
| **A01** | Inputs   | **Asset Verification:** Confirm removal of the pipeline running through the substation terrace. Current KLIC data is outdated. Provide updated drawings/data. | Client (SC&M) | ASAP       | **[05-12]:** Discussed in Kick-off preparation. Essential for accurate modeling. | **OPEN** |
| **A02** | Inputs   | **Earthing Data:** Provide specific short circuit currents and earthing study data if different from TenneT standard assumptions.                             | Client        | TBD        |                                                                                        | **OPEN** |
| **A03** | Planning | **Kick-off Meeting:** Conduct formal project start meeting.                                                                                                   | DNV (Peet)    | 05-12-2025 | Scheduled for Dec 5th.                                                                 | **OPEN** |

### 6 DECISIONS & AGREEMENTS

| ID            | Category | Decision / Agreement                                                                                                                              | Date Agreed |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- |
| **D01** | Team     | **DNV Project Manager:** Peet Schutte.`<br>`**Engineers:** Ivan Grobelaar, Asim Al sofi.                                            | 05-12-2025  |
| **D02** | Method   | **Modeling Approach:** The team will first model analytically to check the GPR danger zone before proceeding to detailed CDEGS simulations. | 05-12-2025  |

### 7 RISK REGISTER (Watchlist)

| ID            | Risk Description                | Potential Impact                                                                                                                                                                                  | Mitigation Strategy                                                                                                              | Status           |
| :------------ | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| **R01** | **High Soil Resistivity** | Deep soil layer resistivity (~500$\Omega\cdot m$) may cause Station Resistance ($R_a$) to exceed the 0.1 $\Omega$ target (currently calc. 0.931 $\Omega$), leading to high GPR (27.1 kV). | DNV to perform detailed CDEGS modeling to verify conservatism of current assumptions. Highlight specific mitigation needs early. | **Active** |
| **R02** | **Input Data Accuracy**   | Modeling based on outdated KLIC data (e.g., phantom pipeline) will result in false positives for interference.                                                                                    | Client to verify "Click data" and confirm removal of assets before final simulation runs.                                        | **Active** |
| **R03** | **Resource Availability** | Personal challenges within the engineering team could impact the start date.                                                                                                                      | Work is kick-started in December to ensure momentum; timeline managed by PM.                                                     | **Active** |
