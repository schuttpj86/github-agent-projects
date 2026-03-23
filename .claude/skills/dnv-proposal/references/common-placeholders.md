# Common Placeholders Reference

Use these standardized placeholder formats when information is missing or needs confirmation.

## Placeholder Syntax

All placeholders use square brackets and a label:

```
[LABEL: description of what's needed]
```

## Standard Labels

| Label | Meaning | Use When |
|-------|---------|----------|
| TBD | To Be Determined | Information must be confirmed with client |
| PLACEHOLDER | Awaiting Assignment | Internal DNV assignment (e.g., personnel) |
| CLIENT INPUT | Requires Client Data | Specific data the client must provide |
| CONFIRM | Needs Verification | Value found but uncertain if correct |
| INSERT | Action Required | User must add something (diagram, table) |

## Common Placeholders by Section

### Cover Page

```
DNV doc No: [PLACEHOLDER: Document number to be assigned]
Customer Reference: [TBD: Client RFQ/RFP reference number]
Customer Contact: [TBD: Client contact person]
```

### Section 1: Introduction

```
[CLIENT INPUT: specific project background from RFQ]
[TBD: total installed capacity - values of X and Y noted in documents]
```

### Section 2: Deliverables

```
[TBD: number of reports - depends on final site count]
[TBD: model file formats - confirm PSCAD versus PSS/E requirement]
```

### Section 3: Scope of Work

```
[TBD: voltage level - LV voltage not specified in tender]
[TBD: number of scenarios - awaiting client confirmation]
[CONFIRM: cable length - stated as "approximately 15 km" in tender]
```

### Section 4: Schedule

```
[TBD: project duration - timeline not specified in tender documents]
[TBD: milestone dates - to be aligned with client programme]
[CLIENT INPUT: preferred start date]
```

### Section 5: Compensation

```
[TBD: pricing to be determined]
[PLACEHOLDER: lump sum amount]
[TBD: payment milestone percentages - to align with client procurement]
```

### Section 6: Project Organisation

```
[PLACEHOLDER: Project Sponsor name to be assigned]
[PLACEHOLDER: Project Manager name to be assigned]
[PLACEHOLDER: Technical Lead name to be assigned]
[INSERT: DNV Project Organisation Chart]
```

### Section 7: Assumptions

```
[TBD: specific exclusions - to be confirmed during proposal review]
[CLIENT INPUT: data provision timeline]
```

## Formatting Placeholders in Word XML

### Red Text Placeholder (visible in document)

```xml
<w:r>
  <w:rPr>
    <w:color w:val="FF0000"/>
  </w:rPr>
  <w:t>[TBD: description]</w:t>
</w:r>
```

### Red Text with Bold (for important placeholders)

```xml
<w:r>
  <w:rPr>
    <w:b/>
    <w:color w:val="FF0000"/>
  </w:rPr>
  <w:t>[CLIENT INPUT: required data]</w:t>
</w:r>
```

### Placeholder with Comment

For placeholders that need explanation, add a comment:

1. Add the placeholder text in red
2. Use `comment.py` to create the comment
3. Add comment markers around the placeholder

```xml
<w:commentRangeStart w:id="0"/>
<w:r>
  <w:rPr>
    <w:color w:val="FF0000"/>
  </w:rPr>
  <w:t>[TBD: transformer capacity]</w:t>
</w:r>
<w:commentRangeEnd w:id="0"/>
<w:r>
  <w:rPr>
    <w:rStyle w:val="CommentReference"/>
  </w:rPr>
  <w:commentReference w:id="0"/>
</w:r>
```

Comment content example:
> "The tender documents mention 'two transformers' but do not specify the MVA rating. Section 2.4 implies 90 MVA total capacity. Please confirm with the client whether this means 45 MVA each or 90 MVA each for N-1 redundancy."

## Tracking Placeholders

When using many placeholders, maintain a tracking list at the end of the document or in a separate file:

```
PLACEHOLDER TRACKING
====================
1. [TBD: transformer LV voltage] - Section 3, Task 4.1
   Source conflict: Tender says "to be confirmed by developer"

2. [PLACEHOLDER: Project Manager] - Section 6.2
   Status: Awaiting resource allocation

3. [CLIENT INPUT: site coordinates] - Section 3, Task 2
   Status: Request sent to client on [date]
```

## When NOT to Use Placeholders

Do not use placeholders for:
- Standard DNV terms that are always the same
- Information that can be reasonably derived from context
- Values that are clearly stated in the tender documents

If a value is stated in the tender, use it directly and cite the source:
```
The total installed capacity is 90 MW (per NESO Technical Specification V3, Section 1.2).
```

Only placeholder genuinely missing or ambiguous information.
