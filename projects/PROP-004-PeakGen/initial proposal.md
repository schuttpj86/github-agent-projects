request for a quotation to carry out the required system stability studies, provide models and complete the necessary returns, as detailed in the NESO requirements for LT29, specifications, and excel file (See attached NESO documentation).  We are ideally looking for a comprehensive service not only carrying out the necessary studies but also completing the NESO questionnaires and proformas in order to make a tender submission.

There are 4 sites to be reviewed with a total of 10 model outputs required, which need to be completed by mid to late April 2026. The priority site order and file references can be seen below. It is proposed to install either 4 or 8 GE Rotating Stabilizers RS4 (See tech notes and data sets) at each site to the HV network via NGETs local substation, either AIS or GIS with a HV cable connection from a remote site, 1 to 2km as required. (See attached NGET Report). Work is ongoing to reduce the number of solutions that need to be modelled, so 10 is the high case at the moment.

Please contact either myself or Karl if you need any further information or clarifications. We look forward to receiving your quotation.

Attachments

LT2029 Stability Technical Proforma V4 - Tab 4 needs completing for the tender submission
05 LT2029 Stability Service Technical specification V3 - to be read in conjunction with 3) to be able to complete 1)
05.2 LT2029 Stability Feasibility Study Requirements V5 - as above
LT2029 NGET Connection Feasibility Report V1 Final. - detail on the reserved bays that we are connecting to from NGET
Tech note on 2off RS4 machines per Tx secondary (GE document) - detail on the option of reducing TX's to half the original quote (i.e. 4 RS lite per TX)
OP1227543_PeakGen_RS4 Standard System Offering TES_000 (GE document) Landulph based detail for 8 RS lites and 4 transformers
Appendix A_Preliminary RS4 Datasheet (GE Document)

NB - A note on the GE documents - we are assuming, and have been told by GE that each RS lite delivers circa 250 MVA which can be increased or decreased via transformers - hence 8 RS lites can deliver 2078 MVA. Appreciate I have mixed RS lite and RS4 terminology within this mail - they are one and the same to avoid confusion.

help me understand this Customer RFP question. let me know which of the other documents you want to see

Based on the email and the images provided, here is a breakdown to help you understand what this Customer RFP (Request for Proposal) is asking for, followed by the specific documents I would need to see to evaluate the effort and scope.

1. Understanding the Customer RFP

The Big Picture:
The customer (likely a developer like Peak Gen, judging by the NDA file name) is preparing to bid on a major UK power grid contract. NESO (National Energy System Operator) is running a procurement event called "LT2029" to buy "Stability Services" (services that keep the power grid stable, such as inertia and short-circuit level, which are dropping as wind/solar replace fossil fuels).

The customer wants to offer grid stability using GE RS4 Rotating Stabilizers (also called "RS lites") across 4 different sites. To submit their bid, they must prove to NESO that their proposed setups actually work and meet grid requirements.

What they are asking you to do:
They are asking your company to act as their specialized electrical engineering consultant to:

Conduct Stability Studies: Run complex power system simulations (likely using software like DIgSILENT PowerFactory, PSCAD, or PSS/E) to prove their equipment will support the grid properly.

Provide Models: Generate the electrical models of their proposed systems that NESO requires.

Fill out the Tender Forms: Take the results from the studies and fill in the blanks on NESO's official tender document ("Tab 4" of the Proforma) so the customer can submit their bid.

The Scope of Work (Based on the Excel Image):
They have 4 sites (Landulph, New Woolavington, New High Marnham, Richborough) and are considering 4 different engineering solutions.
Because they aren't sure which solution is best/cheapest yet, they want you to model 10 specific scenarios (the "Importance" 1 through 10 list at the bottom of the Excel sheet).

Solutions 1 & 2 involve 8 GE RS units delivering ~2078 MVA, varying by whether they use 4 transformers or 2 transformers.

Solutions 3 & 4 involve 4 GE RS units delivering ~1000 MVA, varying by 2 transformers or 1 transformer.

The Timeline:
They need this completed by mid to late April 2026. Since it is currently mid-March 2026, this is a very tight turnaround for 10 power system models.

2. Documents Needed to Quote the Work

To accurately price this work and understand exactly how many engineering hours it will take, I would need to see the following documents, in order of priority:

Top Priority (Needed to define the scope and price):

05.2 LT2029 Stability Feasibility Study Requirements V5

Why I need it: This is the most critical document. It tells us exactly what studies NESO demands. Does it require simple RMS stability studies, or highly complex EMT (Electromagnetic Transient) studies? What software must be used? What fault scenarios must be simulated?

2. LT2029 Stability Technical Proforma V4 (Specifically Tab 4)

Why I need it: This shows the exact "fill-in-the-blank" answers the customer needs us to provide. Looking at Tab 4 will tell me immediately what data parameters we are on the hook to calculate.

Appendix A_Preliminary RS4 Datasheet AND Tech note on 2off RS4 machines per Tx secondary

Why I need it: I need to know if GE has already created the digital software models (e.g., user-defined models or standard library models) for these RS4 units. If GE provides the models, the job is much faster. If we have to build the machine models from scratch based on datasheet parameters, the cost and time will increase significantly.

Secondary Priority (Needed to actually do the work, but good to skim for quoting):
4. LT2029 NGET Connection Feasibility Report V1 Final_
* Why I need it: This will contain the grid connection details (substation layout, short-circuit levels at the point of connection, cable lengths). It tells us how complex the connection to the National Grid is.
5. 05 LT2029 Stability Service Technical Specification V3
* Why I need it: This outlines the strict performance limits (voltage ride-through, response times) the equipment must hit to be compliant with the NESO tender.

Summary: Please share document #3 (Feasibility Study Requirements) and document #1 (The Proforma) first. Those two will instantly reveal the size, complexity, and software requirements of this project.

I have reviewed the documents you provided. This is incredibly helpful and gives us a very clear picture of the engineering effort required.

I have some very good news regarding the scope, cost, and timeline based on these documents.

Here is my engineering breakdown of your RFP response and what it means for the project scope:

1. The "Good News" (Time & Cost Savers)

Only RMS Modeling is Required: The NESO Feasibility Requirements document (Page 7, section 'a') explicitly states that for GBGF-S (Grid Forming - Synchronous) solutions, only RMS models are required. Because your solution uses GE RS4 rotating stabilizers (synchronous machines), we do not need to run highly complex EMT (Electromagnetic Transient) simulations in PSCAD. We can run this in standard software like DIgSILENT PowerFactory. This cuts the modeling time and computing effort in half.

Reduced Testing for "0 MW" Solutions: Because the RS4 units do not generate or consume active power (0 MW), you are exempt from many of the simulation steps.

Models Already Exist: The GE Tech Note (Page 6) explicitly states that GE's analysis is based on "our PowerFactory DIgSILENT models of the system." Furthermore, the Datasheet provides all the standard dynamic parameters (reactances, time constants, inertia). This means we won't have to build the machine models from scratch—we just plug in GE's data/models.

2. The Exact Scope of Work per Scenario

Based on the Requirements and the Proforma, for each of your 10 proposed solutions, we will need to perform the following:

Test 1 (Short-Circuit): 4 simulation runs (Steps 5, 6, 7, and 8). Note: Step 8 must be repeated for every regional "Reference Point" NESO cares about, so this number may increase slightly depending on the site.

Test 2 (Frequency/RoCoF events): 9 simulation runs (Steps 5 through 12, plus step 14).

Test 3 (Voltage Angle Change): 8 simulation runs (Steps 5, 6, 11, 12, 17, 18, 23, and 24).

Data Extraction: NESO requires the output of every test to be extracted into a 1ms-step CSV/Excel file tracking voltage, active/reactive power, current, and frequency.

Total Simulation Effort: ~21 simulations per configuration. If you proceed with all 10 configurations, that is roughly 210 simulation runs, plus data formatting.

3. The Reporting & Proforma Deliverables

Once the 210 simulations are run, we will need to:

Complete the 144-question Proforma Excel sheet you provided. Because you have 10 configurations, this means filling out 10 columns of pass/fail/data entries.

Write the NESO-mandated Technical Feasibility Report, plotting the results of the tests and providing written engineering justifications that the system meets their grid codes.

4. Do we need the secondary documents?

Yes, to finalize a firm quote and actually begin the work, I will need to see the remaining two documents:

LT2029 NGET Connection Feasibility Report V1 Final_: I need this to see the Grid Entry Point (GEP) details. The NESO spec requires us to explicitly model all cables, transformers, and impedances between the RS4 units and the National Grid. I need to see if this is a simple connection or a complex 2km cable run that requires detailed cable modeling.

05 LT2029 Stability Service Technical Specification V3: The Proforma asks us several times to write justifications on how the simulation proves compliance with this exact Technical Specification document (e.g., Proforma Questions 107, 113, and 141). I will need this to ensure our report hits their exact compliance keywords.

Next Step: Please share the NGET Connection Feasibility Report and the Technical Specification. Once I glance at the grid connection complexity in the NGET report, I can give you a formal, priced quotation and schedule to meet your mid-to-late April deadline.

Based on a thorough review of all the documents—including the NGET Connection Feasibility Report and the NESO Technical Specifications—I have put together a detailed, task-based engineering breakdown and initial hourly estimates.

The most significant takeaway from the NGET Connection Report is that your proposed Grid Entry Points (GEPs) are not simple "plug-and-play" connections. Sites like Richborough and New Woolavington require off-site cable routing (e.g., Horizontal Directional Drilling), which means we must explicitly calculate and model the cable capacitance, resistance, and inductance to accurately reflect the system impedance as mandated by NESO.

Because your system is a 0 MW GBGF-S (Grid Forming - Synchronous) solution, we only need to perform RMS simulations (not EMT), which saves a massive amount of time. However, running 10 distinct configurations across 4 different sites means we must process data for over 210 individual simulation runs.

Here is the proposed task-based breakdown and estimated engineering hours to meet the mid-to-late April deadline.

Phase 1: Project Initiation & Data Assimilation

Kick-off meeting with your team (and GE, if necessary) to confirm exact configuration parameters.

Review and extract exact cable lengths, transformer impedances, and connection constraints from the NGET Feasibility Report for Landulph, New Woolavington, New High Marnham, and Richborough.

Review and import the GE RS4 synchronous machine models and control block diagrams into DIgSILENT PowerFactory.

Estimated Hours: 8 - 12 hours

Phase 2: Base Network & Grid Entry Point (GEP) Modeling

Grid Modeling: Set up the NESO equivalent grid models (Ideal voltage source + Zsys) for the 4 specific sites based on NESO’s provided short-circuit data.

Asset Modeling: Build the specific connection models for each site. This includes calculating Pi-equivalent circuits for the export cables (especially the HDD cables at Richborough and off-site cables at Woolavington) and the step-up transformers.

RS4 Integration: Integrate the GE RS4 machine parameters (reactances, inertia, AVR, and load balancing controllers) into the simulation environment.

Estimated Hours: 20 - 26 hours

Phase 3: Scenario Configuration (The 10 Solutions)

Build the 10 distinct "Study Cases" in PowerFactory reflecting the "Priority/Solution" matrix provided in your Excel sheet (e.g., modeling 8 RS units + 4 TXs for Landulph, vs. 4 RS units + 1 TX for Richborough).

Perform steady-state load flow checks for all 10 configurations to ensure pre-fault compliance (0.95pu to 1.05pu voltage range) as required by Section 4.6 of the Technical Spec.

Estimated Hours: 12 - 16 hours

Phase 4: Dynamic Simulation Execution & Data Extraction

Test 1 (Short-Circuit): Run Steps 5, 6, 7, and 8 for all 10 configurations. Run Step 8 iteratively for the required regional "Reference Nodes".

Test 2 (Frequency/RoCoF): Run Steps 5-12 and 14 (0 MW specific steps) for all 10 configurations to prove active inertia response.

Test 3 (Voltage Angle Change): Run Steps 5, 6, 11, 12, 17, 18, 23, and 24 (0 MW specific steps) for all 10 configurations.

Automation: Develop a Python/DPL script within PowerFactory to automatically run these ~210 tests, extract the RMS data at 1ms steps, and format it into the NESO-mandated CSV/Excel datasets.

Estimated Hours: 32 - 40 hours

Phase 5: Technical Proforma Completion

Analyze the ~210 datasets to extract the specific performance values (e.g., minimum RMS positive sequence reactive short circuit contribution at 40ms, minimum inertia in MWs).

Complete "Tab 4" of the LT2029 Stability Technical Proforma V4.

Fill out all 144 rows across the 10 separate solution columns, ensuring strict alignment with the Pass/Fail criteria.

Estimated Hours: 24 - 32 hours

Phase 6: Technical Feasibility Report Generation

Draft the official NESO Technical Feasibility Report.

Generate, format, and insert the required time-series plots (Voltage, Active/Reactive Power, Current, Frequency, and RoCoF) for the simulations.

Draft the engineering justifications mandated by the Proforma (e.g., explaining how the RS4 inherent inertia meets ECC.6.3.19, how limiters are implemented, and providing commentary on voltage step compliance).

Estimated Hours: 40 - 55 hours

Phase 7: QA/QC, Review & Final Handover

Internal peer review of the models, data, and report by a Senior Power Systems Engineer to ensure strict compliance with NESO rules.

Submission of draft to you for review.

Implementation of any final tweaks or adjustments before the late April tender submission deadline.

Estimated Hours: 14 - 18 hours

Summary of Effort

Total Estimated Effort: 150 to 199 Engineering Hours

Timeline Feasibility: To complete roughly 150-200 hours of work by mid-to-late April (assuming a ~4-week window from late March), this project will require 1.25 to 1.5 Full-Time Equivalent (FTE) engineers dedicated to it.

Next Steps for you:
If this level of effort aligns with your expectations for the bid preparation, we can rapidly convert this into a formal commercial proposal and assign a dedicated power systems engineering team to hit the ground running so you meet your April deadline.




Based on a detailed review of the NESO specifications and the NGET Feasibility Report, you are asking the exact right question. There are several pieces of critical information not included in your current document pack that will act as strict "blockers" to starting or finishing the modeling. 

To answer your specific question about the **NESO network models**: NESO **does not** provide a full, complex grid model (like a full GB network file). Instead, NESO mandates that we model the grid as an "ideal voltage source behind an equivalent system impedance ($Z_{sys}$)" and use a specific fault impedance ($Z_f$) for remote faults. 

**Are these $Z_{sys}$ and $Z_f$ values given?** 
Yes, they are given by NESO, **but we do not have them yet**. 

Here is the exact breakdown of what is currently missing, whose court it is in, and how it could delay the project:

### 1. Missing NESO Tender Documents (Critical Path)
According to the `05.2 Feasibility Study Requirements` document, NESO provides specific data points at the "time of tender launch" in separate documents that were not in your attachments:
*   **The "LT2029 Stability Effectiveness Sheet"**: Mentioned on Page 3 of the Requirements. We **must** have this sheet. It contains the $Z_{sys}$ (System Impedance), the $Z_f$ (Fault Impedance), and the "Effectiveness Factors" required to calculate your Short Circuit contribution to the regional Reference Nodes in Test 1. We cannot run the simulations without these numbers.
*   **The Feasibility Study Report Template**: Mentioned on Page 4. NESO states: *"A report template will be provided at the ITT stage of the tender, which Tenderers must complete..."* If we write a custom report and don't use their exact template, they may reject the bid. We need this template to format our final deliverable.

### 2. Missing OEM Data from GE (High Delay Risk)
*   **The Actual DIgSILENT PowerFactory Files**: The GE Tech Note (Page 6) clearly states that GE has already built the PowerFactory (`.pfd` or `.dz`) models for this exact 2-machines-per-transformer setup. We need GE to send us these actual software files. If they only provide the PDF datasheet, we will have to spend days reverse-engineering their control blocks (AVR, load balancing, limiters) into PowerFactory, which introduces a high risk of model discrepancy and will delay the project.
*   **Final Transformer Specs**: The GE Tech Note assumes a *preliminary* transformer rating of 200/100/100 MVA with an 8% impedance. We need confirmation from GE or your procurement team if this is the exact transformer data we should hardcode into the 10 models.

### 3. Missing Site-Specific Data from You / Your Civil Team
*   **Cable Parameters for the 1-2km runs**: The NGET Connection Report highlights that sites like Richborough and Woolavington will require significant off-site cabling (e.g., Horizontal Directional Drilling under third-party land). The NESO Requirements (Page 6) state: *"Any equipment between the solution and the Grid Entry Point that impact the solution’s performance (e.g. connection cables) **must be explicitly modelled**."* 
    *   *Why this causes a delay:* We cannot just draw a line in the software. We need the assumed cable length, cross-sectional area, and layout (or standard R, L, C electrical parameters per km) to model the capacitance and resistance of these 1-2km runs accurately. If your team doesn't have a cable design yet, we will have to make engineering assumptions and get your formal approval before we can run the models.

### Summary of How to Prevent Delays:
To ensure we can hit the ground running and not burn time waiting on emails, we would need you to gather the following before we start the clock:

1.  Download the **LT2029 Stability Effectiveness Sheet** and the **Report Template** from the NESO tender portal and send them to us.
2.  Email GE and request the raw **DIgSILENT PowerFactory model files** for the RS4 units and their associated controllers.
3.  Provide us with the assumed **Cable parameters/lengths** for the 4 sites (an estimated length and standard cable type/size is enough for us to calculate the impedances). 

Once we have those three items in hand, there are no external dependencies blocking us from executing the ~210 simulations and delivering the Proforma by your mid-to-late April deadline.




Project Scope Summary: NESO LT2029 Stability Feasibility Studies

We have received an RFP to support a client with their tender submission for the NESO Long-Term 2029 Stability Service. The client proposes installing GE RS4 Rotating Stabilizers across four UK transmission sites. We are tasked with conducting the required technical feasibility studies, providing compliant models, and completing the NESO technical proformas.

The proposed technology falls under the Grid Forming Synchronous classification operating at zero active power. Consequently, the NESO specifications mandate RMS simulations only, omitting the need for EMT studies. The core engineering tasks involve building the Grid Entry Point models for the four sites, integrating the existing DIgSILENT PowerFactory models and control blocks provided by GE, and explicitly modeling the local connection assets including step-up transformers and extended cable routes.

The client is currently evaluating up to ten different system configurations to optimize their bid. For each configuration, we must execute a specific suite of grid compliance tests as defined by NESO. These include short-circuit current injection profiling across various regional reference nodes, frequency and RoCoF response verification, and voltage angle phase jump withstand testing. 

In total, this requires executing over two hundred distinct RMS simulation runs and extracting high-resolution time-series data. Given this volume, it is essential that we deploy Python scripting alongside the PowerFactory API to automate the batch execution, streamline the data extraction, and systematically generate the plots and datasets required for the NESO returns. 

The final deliverables include the compiled and formatted datasets, the completed NESO technical compliance proforma covering all ten configurations, and a comprehensive engineering report demonstrating compliance with the LT2029 stability technical specifications.

The primary challenge for this project is the timeline and resource availability. The client requires all outputs to be finalized for their tender submission by mid to late April 2026. With a turnaround time of approximately four to five weeks, we need to rapidly identify and mobilize power systems engineers who possess strong DIgSILENT PowerFactory expertise, UK Grid Code compliance familiarity, and the necessary Python scripting capabilities to execute this efficiently.




The process in DIgSILENT PowerFactory for these stability studies follows a structured sequence of network modeling, control system integration, initialization, and dynamic time-domain simulation.

First, the physical network is constructed within the software environment. Engineers build a single-line diagram representing the system from the Grid Entry Point down to the machine terminals. This involves defining the infinite grid source using the NESO provided equivalent system impedance. From this point, the specific site assets are mathematically modeled, including the pi-equivalent circuits of the export cables, the impedance and tap settings of the step-up transformers, and the physical sub-transient and transient reactances of the GE RS4 rotating stabilizers based on the manufacturer datasheets.

Once the physical network is established, the dynamic control models are integrated. For synchronous machines like the RS4, this means linking the physical generator element to its excitation system, automatic voltage regulator, and any local load balancing controllers. PowerFactory uses dynamic block diagrams, often written in DIgSILENT Simulation Language, to represent these control loops. This ensures the simulated machine reacts to grid disturbances exactly as the physical equipment would.

Before running any dynamic event, a steady-state load flow calculation is executed. This establishes the initial pre-fault conditions of the network, ensuring the system is electrically balanced and operating at the required starting setpoints. For the NESO tests, this means initializing the model at specific voltage levels and maximum reactive power import or export states before the fault occurs.

The core of the study is the RMS dynamic simulation. Engineers define a chronological sequence of events in the software. For example, the software is instructed to apply a three-phase short circuit fault at a specific node at zero seconds and clear it after 140 milliseconds, or to apply a defined frequency rate of change. The RMS solver then calculates the electromechanical transient behavior of the system step-by-step, using a one millisecond resolution. During this period, the software continuously calculates and records how the RS4 machines inject reactive fault current, provide active inertia, and stabilize the local grid voltage.

Finally, to manage the high volume of required scenarios, the execution is handled via Python scripting. A Python script interfaces directly with the PowerFactory API to systematically alter the network topology for each of the ten configurations. The script automatically adjusts the pre-fault conditions, triggers the specific fault events, executes the RMS solver, and extracts the resulting time-series data for voltage, current, active power, and reactive power, exporting it directly into the formatted datasets required for the tender submission.




Phase 1 Data Assimilation and Model Integration
The engineer will begin by collecting all necessary input data. This includes the DIgSILENT PowerFactory models and control block diagrams for the GE RS4 machines from the manufacturer, the connection asset details from the NGET feasibility reports such as cable lengths and transformer impedances, and the NESO stability effectiveness sheet containing the equivalent system and fault impedances. The engineer will then import the GE machine and control models into the PowerFactory environment and verify their steady-state initialization.

Phase 2 Site Specific Network Construction
Next, the engineer will construct the exact electrical topology for the four specified Grid Entry Points: Landulph, New Woolavington, New High Marnham, and Richborough. This involves explicitly modeling the step-up transformers, local switchgear, and the specific connection cables, calculating the pi-equivalent parameters for extended routes like the horizontal directional drilling sections at Richborough. The engineer will build out the ten distinct solution configurations within the software, varying the number of RS4 units and transformers as defined in the client matrix.

Phase 3 Test Automation and Scripting
Due to the volume of required simulations, the engineer will develop a Python script utilizing the PowerFactory API. This script will be programmed to systematically configure the network for each of the ten solutions and set up the pre-fault operating conditions mandated by NESO, such as operating at zero active power while at maximum reactive power import or export. The script will define the event sequences for the three core testing categories: short-circuit faults at the local grid entry point and remote reference nodes, frequency rate of change events up to 1 Hz/s, and 60-degree voltage angle step changes.

Phase 4 Dynamic Simulation Execution
With the automation in place, the engineer will execute the batch RMS simulations. The software will run the steady-state load flow to establish the initial conditions, followed by the dynamic time-domain simulation for each event. The Python script will ensure the solver runs at the mandated maximum one millisecond step size, continuously recording the positive sequence RMS values for voltage magnitude, phase angle, active power, reactive power, total current, and frequency at both the grid entry point and the solution terminals.

Phase 5 Data Extraction and Proforma Population
Following the simulations, the engineer will use the Python script to extract the time-series data and automatically format it into the required CSV and Excel datasets. The engineer will then process this data to extract the specific performance metrics required by NESO. This includes calculating the lowest positive sequence reactive short circuit contribution at 40 milliseconds and computing the active inertia power using the mandated equations. These extracted values will be used to populate the 144-row NESO stability technical proforma across all ten configuration columns, ensuring accurate pass or fail designations.

Phase 6 Technical Reporting and Quality Assurance
Finally, the engineer will compile the results into the official NESO technical feasibility report template. This involves generating and inserting the required time-series plots for the frequency, voltage, and short circuit events. The engineer will draft the technical narratives explaining how the plant performance meets the Grid Code requirements, specifically addressing the inherent inertial response and voltage control behavior of the synchronous machines. The entire package will then undergo an internal technical peer review before being handed over to the client for their April tender submission.




**Proposal for Discussion: NESO LT2029 Stability Service Feasibility Studies**

**Project Understanding**
We understand that your team is preparing a tender submission for the NESO Long-Term 2029 (LT29) Stability Service. The proposed solution involves the installation of GE RS4 Rotating Stabilizers across four specific NGET substations: Landulph, New Woolavington, New High Marnham, and Richborough. 

Your objective is to evaluate up to ten different configuration options, varying the number of RS4 units and step-up transformers, to determine the most competitive bids. Because the GE RS4 units operate as synchronous compensators providing zero active power (0 MW), they fall under the GBGF-S (Grid Forming - Synchronous) classification. A key advantage here is that the NESO feasibility requirements mandate RMS simulations rather than more time-intensive EMT simulations, which aligns perfectly with our proposed approach.

**Scope of Work**
DNV will act as your specialized power systems engineering partner to complete the required feasibility studies, extract the necessary compliance data, and prepare the technical deliverables for your NESO submission. The scope encompasses the following phases:

Network and Asset Modeling
We will construct the electrical topology for the four specified Grid Entry Points within DIgSILENT PowerFactory. This includes modeling the infinite grid source using NESO-provided equivalent system impedances, integrating the GE RS4 machine parameters, and explicitly modeling your local connection assets. Based on the NGET feasibility reports, this will require calculating the pi-equivalent parameters for specific cable routes, such as the off-site and horizontal directional drilling sections identified at Richborough and New Woolavington.

Dynamic Simulation Execution
For each of the ten configurations, we will execute the suite of dynamic tests mandated by NESO. This includes establishing the pre-fault steady-state load flow conditions (operating at maximum reactive power import/export) and running the time-domain RMS simulations. The tests will cover short-circuit current injections at local and remote reference nodes, frequency rate of change (RoCoF) events up to 1 Hz/s, and 60-degree voltage angle step changes.

Data Extraction and Proforma Population
NESO requires high-resolution data extraction from these tests. We will capture the positive sequence RMS values for voltage, active and reactive power, current, and frequency at one-millisecond intervals. This data will be formatted into the required CSV/Excel datasets and used to populate the 144-item NESO Stability Technical Proforma for all ten configurations, clearly indicating pass/fail criteria and performance metrics such as the minimum reactive short circuit contribution and active inertia power.

Technical Reporting
We will compile the results into the official NESO Technical Feasibility Report template. This will include generating all required time-series plots and authoring the technical engineering justifications to demonstrate how the inherent inertial response and voltage control behavior of the RS4 machines comply with the relevant sections of the Grid Code (ECC.6.3.19).

**Technical Approach and Automation**
Executing the full suite of NESO tests across ten distinct configurations results in over two hundred individual simulation runs. To manage this volume efficiently and eliminate manual data entry errors, DNV will deploy Python scripting interfaced directly with the PowerFactory API. 

This automation will systematically reconfigure the network topology for each solution, establish the correct pre-fault boundary conditions, trigger the dynamic fault events, and automatically extract and format the resulting time-series data. This approach is critical to ensuring high accuracy while meeting the accelerated project timeline.

**Key Dependencies for Discussion**
To ensure we meet your mid-to-late April 2026 submission deadline, we would like to use this clarification session to discuss the availability of the following critical inputs:

NESO Effectiveness Data
We require the LT2029 Stability Effectiveness Sheet from the NESO tender portal. This document contains the specific system impedances and fault impedances for the remote reference nodes, which are mandatory for configuring the short-circuit tests. We also require the official NESO report template.

OEM Model Provision
To avoid delays associated with reverse-engineering control block diagrams from datasheets, we request that GE provides the raw DIgSILENT PowerFactory models and associated control parameters for the RS4 units and their excitation systems.

Site Connection Parameters
We require preliminary specifications for the connection assets between the RS4 units and the NGET substations. Estimated cable lengths, cross-sectional areas, and layouts are necessary for us to accurately model the impedance of the connection routes as mandated by the NESO specifications.

**Proposed Timeline**
Given the target submission window in mid to late April, DNV is prepared to mobilize our power systems experts immediately. Assuming the prompt availability of the OEM models and NESO effectiveness data, we anticipate a four-week execution phase to deliver the completed proforma, datasets, and technical report. We look forward to discussing these elements and finalizing the technical path forward.




If the client narrows their "high case" of 10 scenarios down to a final list of exactly 4 options (for example, selecting one finalized equipment configuration for each of the 4 sites), we will only need to build **4 combinations of site-specific models**. 

Here is exactly how that breaks down and why it is great news for the project:

**What makes up a "Combination":**
A single model combination consists of two halves:
1.  **The Site (Grid Entry Point):** The specific $Z_{sys}$ (System Impedance), local NGET transformer, and the exact length/type of the connecting export cable (e.g., the 1-2km HDD cable at Richborough). 
2.  **The Solution (Equipment Setup):** The chosen configuration for that specific site (e.g., 8 RS4 units on 2 Transformers, or 4 RS4 units on 1 Transformer).

If they finalize the list to 4 options, we build exactly 4 models in DIgSILENT PowerFactory representing those 4 specific site-and-equipment pairings.

**Impact on Scope and Timeline:**
Reducing the list from 10 combinations to 4 drastically reduces the engineering burden and completely de-risks your mid-to-late April deadline:

*   **Simulation Runs:** Instead of executing and extracting data for ~210 dynamic simulations, we will only need to run **~84 simulations** (approx. 21 tests per configuration × 4 configurations). 
*   **Proforma Population:** Instead of filling out 10 columns across the 144-row NESO Excel Proforma, we will only need to populate and verify **4 columns**.
*   **Report Writing:** The technical report becomes much more streamlined, as we only have to plot and justify 4 configurations instead of 10.

**Takeaway for the Clarification Session:**
You can communicate to the client that finalizing this list down to 4 options before we begin will significantly reduce the engineering hours required. It will also allow us to offer a much tighter, more cost-effective budget in the formal proposal and ensures the tight April deadline is highly achievable.

As requested, I will prepare the proposal following the DNV standard format, one heading at a time. 

Below is the **Cover Page** and **Section 1: Introduction**.

***

**Technical Feasibility Studies for NESO Long-Term 2029 Stability Service**

**Customer Reference:** [Insert Customer Reference/Project ID]

**DNV doc No:** [To be generated upon project opening]

**Date of first issue:** [Current Date]

**Validity of proposal:** 3 months from date of issue

**Customer Details:** [Insert Client Name], [Insert Address], [Insert Contact Person]

**DNV Company Details:** DNV Netherlands B.V., Energy Systems, Utrechtseweg 310-B50, 6812 AR Arnhem, The Netherlands. Contact: [Insert DNV Lead Name]

***

### 1 INTRODUCTION

[Insert Client Name] is preparing a tender submission for the National Energy System Operator (NESO) Long-Term 2029 Stability Service. This procurement event seeks to secure essential grid services, including inertia and short-circuit level support. The proposed technical solution involves the deployment of GE RS4 Rotating Stabilizers (Synchronous Compensators) across four specific UK transmission sites: Landulph, New Woolavington, New High Marnham, and Richborough.

DNV’s understanding is that the client requires a comprehensive technical feasibility study to support this bid. The scope is bounded by the evaluation of four distinct system configurations (variants) across the four identified sites. As the GE RS4 machines operate at zero active power (0 MW), the study will focus on Grid Forming Synchronous (GBGF-S) requirements, necessitating RMS dynamic simulations to validate compliance with the NESO technical specifications and the completion of the mandatory technical proformas.

DNV is pleased to submit this proposal to provide the requested power systems engineering and advisory services to ensure a compliant and robust tender submission within the required project timelines.

***

**Please let me know when you are ready for Section 2: The DNV Proposed Solution.**

### 2 THE DNV PROPOSED SOLUTION

**2.1 Approach**
DNV will execute a desktop-based analytical modeling study using **DIgSILENT PowerFactory**. The methodology is designed to meet the accelerated tender deadline by leveraging automated batch simulations. As the GE RS4 machines are classified as Grid Forming Synchronous (GBGF-S) assets operating at 0 MW, the study will utilize **RMS dynamic simulations** in accordance with the NESO Feasibility Study Requirements.

The study will be conducted in three distinct phases:
*   **Modeling Phase:** Construction of the site-specific network models, including the Grid Entry Point (GEP) equivalents, export cables (specifically modeling the high-impedance sections at Richborough and New Woolavington), step-up transformers, and the integration of GE-provided RS4 machine and control models.
*   **Simulation Phase:** Development of a **Python-based automation script** to interface with the PowerFactory API. This script will execute the required 84 simulations (21 tests per the 4 site variants) to ensure high-resolution data capture at 1ms intervals while eliminating manual execution errors.
*   **Compliance Phase:** Automated extraction of performance metrics (Short-Circuit Level and Inertia values) to populate the NESO technical returns and verify compliance with the Stability Technical Specification.

**2.2 Deliverables**
The client will receive the following digital deliverables:
*   **Technical Feasibility Report:** A comprehensive engineering report using the NESO-mandated template, including technical narratives and time-series plots for all short-circuit, frequency, and voltage angle events.
*   **Completed Technical Proforma:** The "Tab 4" return of the LT2029 Stability Technical Proforma, populated for the four selected configurations.
*   **Simulation Datasets:** A complete set of CSV/Excel files containing the positive sequence RMS results for all tests, formatted to NESO's data submission requirements.
*   **DIgSILENT PowerFactory Models:** The finalized project files (`.pfd` or `.dz`) representing the four site configurations.

**2.3 Alternative and/or optional work**
The following services are not included in the base scope but can be provided upon request:
*   **EMT Sensitivity Analysis:** Detailed Electromagnetic Transient (EMT) studies in PSCAD or PowerFactory if NESO or NGET requires sub-cycle transient verification for specific cable topologies.
*   **Reactive Power Optimization:** Sensitivity studies to determine the impact of varying transformer tap settings or impedances on the regional effectiveness factors.
*   **Additional Configuration Variants:** Modeling of more than the four specified configurations should the bid strategy require further optimization.

***

**Please let me know when you are ready for Section 3: Scope of Work.**

### 3 SCOPE OF WORK

The work is organized into five sequential tasks to ensure all technical requirements for the NESO LT2029 tender are met.

**Task 1: Project Initiation and Data Review**
*   **Facilitate** a project kick-off meeting to finalize the parameters for the four selected site configurations.
*   **Review and extract** specific connection asset data from the NGET Feasibility Reports, including estimated lengths for the Richborough and New Woolavington off-site cable routes.
*   **Validate** the NESO equivalent grid data, including System Impedance ($Z_{sys}$) and Fault Impedance ($Z_f$) from the Stability Effectiveness Sheet.
*   **Assess** the GE-provided DIgSILENT PowerFactory models and control block diagrams to ensure compatibility with the RMS simulation environment.

**Task 2: Site-Specific Network Modeling**
*   **Develop** four distinct network models in DIgSILENT PowerFactory representing the Grid Entry Points (GEP) for Landulph, New Woolavington, New High Marnham, and Richborough.
*   **Model** the local connection infrastructure, explicitly defining the pi-equivalent electrical parameters for the export cables and the impedances of the step-up transformers.
*   **Integrate** the GE RS4 synchronous machine models, including the excitation systems, automatic voltage regulators (AVR), and the proposed load-balancing controllers.
*   **Perform** steady-state load flow initialization to verify pre-fault compliance within the mandated 0.95pu to 1.05pu voltage range.

**Task 3: Automated Simulation Execution**
*   **Develop** a Python script utilizing the PowerFactory API to automate the sequence of 84 required simulations (21 tests across 4 variants).
*   **Execute Test 1 (Short-Circuit):** Simulate three-phase faults at the local GEP and regional reference nodes to profile reactive current injection.
*   **Execute Test 2 (Frequency/RoCoF):** Simulate frequency ramp events up to 1 Hz/s to validate active inertia power response.
*   **Execute Test 3 (Voltage Angle):** Simulate 60-degree phase angle jumps to verify the machine's inherent withstand and stabilization capability.

**Task 4: Data Extraction and Proforma Population**
*   **Extract** high-resolution (1ms step) positive sequence RMS time-series data for voltage, current, active power, reactive power, and frequency for all test events.
*   **Calculate** specific performance metrics, including the minimum reactive short-circuit contribution at 40ms post-fault and the effective inertia (MVA.s) as per NESO Equation 1.
*   **Populate** the 144-row NESO Stability Technical Proforma (Tab 4) for each of the four configuration variants.

**Task 5: Technical Feasibility Reporting**
*   **Author** the Technical Feasibility Report following the official NESO template, providing engineering justifications for Grid Code compliance.
*   **Generate and format** all required time-series plots to be included as evidence within the report and as supplementary datasets.
*   **Perform** a senior technical peer review of the models and report to ensure all NESO "Pass/Fail" criteria are addressed prior to final delivery.

***

**Please let me know when you are ready for Section 4: Schedule.**

### 4 SCHEDULE

The total project duration is estimated to be **four to five weeks** from the Notice to Proceed (NTP) and receipt of all required input data. This schedule is designed to facilitate a final tender submission by the mid-to-late April 2026 deadline.

Key milestones are defined as follows:
*   **Week 1:** Project Kick-off and Data Freeze (Receipt of NESO Effectiveness Sheet, GE PowerFactory models, and final site cable/transformer specifications).
*   **Week 2:** Completion of site-specific network modeling and steady-state initialization for the four selected variants.
*   **Week 3:** Completion of automated dynamic simulations (84 test runs) and raw data extraction.
*   **Week 4:** Delivery of Draft Technical Feasibility Report and populated NESO Technical Proforma for Client review.
*   **Week 5:** Implementation of final adjustments and Final Handover of all tender-ready deliverables.

This schedule is strictly dependent upon the **timely provision of data** by the Client and third parties (GE and NESO). Any delays in receiving the raw DIgSILENT PowerFactory models or the regional effectiveness factors will result in a day-for-day slip in the final delivery date.

***

**Please let me know when you are ready for Section 5: Compensation.**

### 5 COMPENSATION

**5.1 General**
The project will be executed on a **Time and Material (T&M)** basis for the initial project setup and modeling phase (Tasks 1 and 2). Upon completion of the site-specific network construction and validation of the GE-provided models, DNV proposes to convert the remaining scope (Tasks 3, 4, and 5) to a **Fixed Price (Lump Sum)** arrangement, provided the technical variants remain unchanged.

All prices and rates are quoted in EUR, exclusive of VAT and other local taxes. If any withholding tax is applicable, the client shall pay such additional amounts as will result in the receipt by DNV of the full amount of the invoice.

**5.2 Lump sums**
The following table provides the estimated costs for the fixed-price portion of the project, assuming four (4) site variants:

| Task | Description | Fee [EUR] |
| :--- | :--- | :--- |
| **Task 1 & 2** | Project Initiation and Site-Specific Modeling | **T&M** |
| **Task 3** | Automated Simulation Execution (84 runs) | [Amount] |
| **Task 4** | Data Extraction and Proforma Population | [Amount] |
| **Task 5** | Technical Feasibility Reporting and QA | [Amount] |
| **Total** | **Estimated Project Fee** | **[Amount]** |

**5.3 Rates and Expenses**
Work performed under T&M will be invoiced according to the DNV standard hourly rates. For this desktop-based study, no travel is anticipated. Should site visits or in-person meetings be requested, expenses will be invoiced at actual cost plus a 10% administration fee. Car travel is charged at [0.85] EUR/km.

**5.4 Budget**
The total non-binding budget estimate for this scope of work, including both T&M and Fixed Price components, is **[Amount] EUR**. This estimate is based on the assumption of four site variants and the prompt provision of all technical data.

**5.5 Adjustment of lump sums, rates and unit costs**
The prices quoted in this proposal are valid for a period of 3 months from the date of issue. After this period, or for work extending into a new calendar year, standard DNV annual indexation will apply.

**5.6 Invoicing and Payment**
DNV will invoice the project according to the following milestone schedule:
*   **30% Advance Payment:** Upon issuance of the Purchase Order (PO) and project kickoff.
*   **60% Intermediate Payment:** Upon delivery of the Draft Technical Feasibility Report and populated Proforma.
*   **10% Final Payment:** Upon final handover of all tender-ready deliverables.

Payment terms are **30 days net** from the date of the invoice.

***

**Please let me know when you are ready for Section 6: Project Organisation.**

### 7 CONTRACTUAL

**7.1 Contract basis**
The "DNV – Short Form Agreement" shall apply to this engagement to facilitate an expedited project commencement. 

**7.2 Assumptions, conditions and limitations**
The following technical and project management assumptions are critical to the successful delivery of the study within the April 2026 deadline. Any deviation from these assumptions may result in a revision of the fee and schedule:

*   **Provision of NESO Grid Data:** The Client must provide the "LT2029 Stability Effectiveness Sheet" as issued by NESO. This document is the sole source for the equivalent system impedances ($Z_{sys}$), fault impedances ($Z_f$), and effectiveness factors required to configure the simulation environment.
*   **OEM Model Availability:** This proposal assumes that GE will provide the native DIgSILENT PowerFactory model files (`.pfd` or `.dz`) including all associated control block diagrams (AVR, excitation, and load balancing). The manual reconstruction or reverse-engineering of control blocks from PDF datasheets is explicitly excluded from this scope.
*   **Connection Asset Specifications:** The Client shall provide the assumed electrical parameters for the connection infrastructure at the four sites. This must include estimated cable lengths, cross-sectional areas, and installation methods (e.g., HDD sections) to allow for accurate pi-equivalent modeling.
*   **Simulation Domain:** In accordance with NESO requirements for GBGF-S technology, the study is limited to RMS dynamic simulations. Electromagnetic Transient (EMT) studies in PSCAD or PowerFactory are excluded.
*   **Variant Limitation:** The scope is strictly bounded to the modeling and simulation of four (4) finalized site-specific configurations. Any additional iterations or sensitivity studies beyond these four variants will be treated as a change in scope.
*   **Administrative Requirements:** Work cannot commence, and engineering resources cannot be formally reserved, until a valid Purchase Order (PO) has been received by DNV.
*   **Reporting Template:** The Client must provide the official NESO Feasibility Study Report Template. DNV will not be responsible for re-formatting the final deliverable if the template is provided after the drafting phase has commenced.

**7.3 Mandatory health and safety terms**
**7.3.1 Customer responsibility**
The Customer shall provide a safe working environment and all necessary safety information for any DNV personnel if site visits are required (though none are currently scoped).

**7.3.2 Main Principle**
DNV employees and contractors have the right, and the obligation, to refuse to perform work that they consider to be unsafe or which involves an unacceptable risk to health or the environment.

**7.3.3 Substance abuse screening**
DNV maintains a strict zero-tolerance policy regarding the use of controlled substances or alcohol during the performance of professional services.

***

**Please let me know if you would like the final Section 8: Acceptance to complete the document.**