# DNV Proposal Writing Style Guide

This guide ensures proposals are professional, precise, and free of LLM artifacts or marketing language.

## Core Principles

1. **Technical precision over impressiveness** - State facts, not opinions
2. **Clarity over elegance** - Short sentences, simple words
3. **Evidence over claims** - Quote source documents, not assumptions
4. **Humility over confidence** - Use placeholders for unknowns

## Forbidden Elements

### Em-dashes

Never use em-dashes (--) or their Unicode equivalent. They are a common LLM artifact.

**Wrong:**
> The project -- which includes four sites -- will be completed in 8 weeks.

**Correct:**
> The project, which includes four sites, will be completed in 8 weeks.

Or break into two sentences:
> The project includes four sites. It will be completed in 8 weeks.

### Marketing Jargon

Never use these words or phrases:

| Forbidden | Use Instead |
|-----------|-------------|
| cutting-edge | current / modern |
| best-in-class | compliant with [standard] |
| world-class | experienced |
| leverage | use |
| synergy | coordination |
| holistic | comprehensive |
| ecosystem | system |
| seamless | integrated |
| robust | reliable |
| solution | approach / method |
| ensure | verify / confirm |
| optimize | improve |
| utilize | use |
| facilitate | support |
| streamline | simplify |
| state-of-the-art | modern / advanced |
| unparalleled | extensive |
| endeavour | work |
| strategize | plan |
| deep dive | detailed review |
| stakeholder alignment | coordination |

### Soft Qualifiers

Avoid vague qualifiers that do not add information:

| Avoid | Better |
|-------|--------|
| highly experienced | 15+ years of experience in |
| significant | [state the quantity] |
| substantial | [state the quantity] |
| comprehensive | covering [list what] |
| extensive | [state the scope] |
| various | [list them] |
| multiple | [state how many] |
| numerous | [state how many] |

### Empty Phrases

Remove phrases that add no content:

- "It should be noted that..."
- "It is important to mention..."
- "In order to..."
- "At this point in time..." (use "currently" or remove)
- "Going forward..." (remove)
- "As mentioned previously..."
- "Taking into account..."
- "With regard to..." (use "for" or "about")
- "In terms of..." (rephrase directly)

## Required Style Elements

### Action Verbs for Scope Items

Begin scope bullets with strong, specific verbs:

**Technical Analysis:**
- Assess
- Evaluate
- Analyse (British spelling for DNV Europe)
- Calculate
- Determine
- Verify
- Validate
- Model
- Simulate

**Document Production:**
- Prepare
- Develop
- Compile
- Draft
- Document
- Report

**Review Activities:**
- Review
- Examine
- Inspect
- Check
- Audit

**Design Activities:**
- Specify
- Define
- Size
- Configure
- Design
- Select

### Commitment Language

Use "will" for DNV commitments, not "shall" (which implies contractual obligation on the reader):

**Wrong:**
> DNV shall perform load flow studies.

**Correct:**
> DNV will perform load flow studies.

Reserve "shall" for requirements that the client must fulfil:
> The Client shall provide access to the OEM datasheets.

### Reference Specific Sources

Always cite where information comes from:

**Wrong:**
> The system capacity is approximately 40 MW.

**Correct:**
> The system capacity is 40.5 MW (per NESO Technical Specification V3, Section 2.1).

**If uncertain:**
> The system capacity is approximately 40 MW [TBD: confirm value from client documentation].

### Technical Derivations Must Include Sources

For calculations or scope derivations (e.g., number of simulations), always include a source reference table:

**Example - Simulation Count Derivation:**
```
| Test | Steps | Count | Source |
|------|-------|-------|--------|
| Test 1 (Short-Circuit) | 5, 6, 7, 8 | 4 | NESO V5, Page 8, 11 |
| Test 2 (Frequency) | 5-12, 14 | 9 | NESO V5, Page 13, 19 |
| Test 3 (Voltage Angle) | 5,6,11,12,17,18,23,24 | 8 | NESO V5, Page 20-21 |
| **Total per variant** | | **21** | |
```

This allows human reviewers to verify the scope against source documents.

### Technical Methodology Must Be Validated

**Never assume technical methodology.** Common decisions requiring source validation:

| Decision | Validate Against |
|----------|------------------|
| EMT vs RMS simulation | Tender spec (e.g., "For GBGF-S solutions RMS models are required" - NESO V5 Page 7) |
| Number of test cases | Tender spec test requirements |
| Compliance thresholds | Technical specification |
| Software requirements | Client/tender requirements |

If the tender documents don't specify, flag as [TBD] and ask the client.

### Quantities and Units

- Always include units
- Use SI units unless client documentation uses different convention
- Be specific rather than approximate where possible

**Wrong:**
> The cable run is quite long.

**Correct:**
> The cable route is 15 km.

### British vs American English

DNV Europe uses British English:
- analyse (not analyze)
- colour (not color)
- programme (not program, for projects)
- metre (not meter)
- centre (not center)
- organise (not organize)
- licence (noun) / license (verb)

## Handling Uncertainty

### When Information is Missing

Use bracketed placeholders with clear labels:

```
[TBD: transformer LV voltage - not specified in tender documents]
[TBD: project duration - awaiting client confirmation]
[PLACEHOLDER: Project Manager name to be assigned]
```

### When Information is Ambiguous

Use comments (in the Word document) to flag ambiguity:

Comment text example:
> "The tender documents reference 'approximately 90 MW' but also mention 'up to 100 MW'. Please clarify the design capacity with the client."

### When Making Reasonable Assumptions

If an assumption is reasonable and based on standard practice, state it explicitly in Section 7.2 (Assumptions):

```
- Cable sizing will be performed in accordance with IEC 60287
- Ambient temperature assumed to be 25C unless otherwise specified by Client
- Standard DNV modelling assumptions apply per [internal reference]
```

## Document Structure Conventions

### Headings

Match the template exactly. Do not add, remove, or renumber sections.

### Lists

Use bullets for unordered items, numbers for sequential steps:

**Bullets for deliverables:**
```
- Technical Report
- PSCAD Model Files
- Completed NESO Proforma
```

**Numbers for process:**
```
1. Review input data
2. Develop base case model
3. Execute stability studies
4. Compile results into report
```

### Tables

Use tables for:
- Pricing breakdowns
- Personnel qualifications
- Milestone schedules
- Comparative information

Keep tables simple. Avoid merged cells where possible.

## Final Checklist

Before completing a proposal, verify:

- [ ] No em-dashes anywhere
- [ ] No marketing jargon
- [ ] All quantities have units
- [ ] All uncertain values have placeholders
- [ ] Scope items begin with action verbs
- [ ] Sources cited for technical values
- [ ] **Technical derivations include source page references**
- [ ] **Methodology (EMT/RMS/etc.) validated against tender spec**
- [ ] British English used consistently
- [ ] Section numbers match template
- [ ] All insertions use tracked changes
- [ ] **Final output is DOCX with tracked changes (not just markdown)**
