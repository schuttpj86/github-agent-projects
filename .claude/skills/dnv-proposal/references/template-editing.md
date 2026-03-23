# Template Editing Technical Reference

This document contains the technical details for editing the DNV Word template. Only read this when you reach Stage 4 (Template Integration).

## Process Overview

1. Unpack the template
2. Edit the document XML
3. Repack with validation

## Platform Notes (Windows)

On Windows, Python may not be in PATH. Use the full path:
```bash
/c/Users/[USERNAME]/AppData/Local/Programs/Python/Python312/python.exe
```

Or find Python with:
```bash
which python || ls /c/Users/*/AppData/Local/Programs/Python/*/python.exe 2>/dev/null | head -1
```

## Step 1: Unpack

```bash
python .claude/skills/docx/scripts/office/unpack.py "DNV Proposal Template.docx" working/unpacked/
```

This extracts the template to an `unpacked/` directory with editable XML files.

## Step 2: Edit document.xml

The main content is in `unpacked/word/document.xml`.

### Tracked Changes Format

ALL new content must use tracked changes so the user can review insertions:

```xml
<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:t>New proposal text here</w:t></w:r>
</w:ins>
```

**Important:**
- Increment `w:id` for each insertion (1, 2, 3, ...)
- Use `w:author="Claude"` consistently
- Use current date in ISO format

### Preserving Formatting

When inserting into formatted sections, copy the existing `<w:rPr>` (run properties):

```xml
<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r>
    <w:rPr>
      <!-- Copy formatting from surrounding text -->
      <w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>
      <w:sz w:val="22"/>
    </w:rPr>
    <w:t>New text with matching formatting</w:t>
  </w:r>
</w:ins>
```

### Placeholders (Red Text)

For missing information, use red text:

```xml
<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r>
    <w:rPr>
      <w:color w:val="FF0000"/>
    </w:rPr>
    <w:t>[TBD: Description of missing item]</w:t>
  </w:r>
</w:ins>
```

### Placeholders with Comments

For placeholders that need explanation:

1. First, create the comment using the comment script:
```bash
python .claude/skills/docx/scripts/comment.py unpacked/ 0 "Explanation of why this is TBD"
```

2. Then add markers in document.xml:
```xml
<w:commentRangeStart w:id="0"/>
<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r>
    <w:rPr>
      <w:color w:val="FF0000"/>
    </w:rPr>
    <w:t>[TBD: Item description]</w:t>
  </w:r>
</w:ins>
<w:commentRangeEnd w:id="0"/>
<w:r>
  <w:rPr>
    <w:rStyle w:val="CommentReference"/>
  </w:rPr>
  <w:commentReference w:id="0"/>
</w:r>
```

### Smart Quotes

Use XML entities for professional typography:

| Character | Entity |
|-----------|--------|
| Left single quote (') | `&#x2018;` |
| Right single quote/apostrophe (') | `&#x2019;` |
| Left double quote (") | `&#x201C;` |
| Right double quote (") | `&#x201D;` |

Example:
```xml
<w:t>DNV&#x2019;s approach includes &#x201C;desktop analysis&#x201D;</w:t>
```

### Line Breaks and Paragraphs

- Never use `\n` in XML
- Each paragraph is a separate `<w:p>` element
- For a line break within a paragraph, use `<w:br/>`

### Bullet Points

Preserve the existing list formatting. If adding items to an existing list, match the `<w:numPr>` from surrounding items:

```xml
<w:p>
  <w:pPr>
    <w:numPr>
      <w:ilvl w:val="0"/>
      <w:numId w:val="1"/>  <!-- Match existing list -->
    </w:numPr>
  </w:pPr>
  <w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
    <w:r><w:t>New bullet point text</w:t></w:r>
  </w:ins>
</w:p>
```

## Step 3: Repack

```bash
python .claude/skills/docx/scripts/office/pack.py working/unpacked/ "output/DNV Proposal Output.docx" --original "DNV Proposal Template.docx" --validate false
```

The `--original` flag preserves relationships and metadata from the original template.
The `--validate false` flag skips validation if you encounter schema issues (use sparingly).

## Troubleshooting

### Python not found
On Windows, Python may not be in PATH. Use:
```bash
/c/Users/[USERNAME]/AppData/Local/Programs/Python/Python312/python.exe script.py
```

### Missing Python modules
Install required modules:
```bash
pip install defusedxml lxml
```

### Repack fails with relationship errors
Use the `--original` flag to preserve the original template's relationships:
```bash
python pack.py unpacked/ output.docx --original "DNV Proposal Template.docx"
```

### Document won't open in Word
- Check XML syntax errors (unclosed tags)
- Verify all `w:id` attributes are unique integers
- Ensure `<w:rPr>` comes before `<w:t>` in runs

## Common Mistakes to Avoid

| Mistake | Consequence | Correct Approach |
|---------|-------------|------------------|
| Forgetting `w:ins` wrapper | Changes not tracked | Always wrap new content |
| Using `\n` for newlines | Invalid XML | Use separate `<w:p>` elements |
| Missing `xml:space="preserve"` | Whitespace stripped | Add to `<w:t>` with spaces |
| Wrong ID sequence | Validation errors | Keep IDs sequential |
| Straight quotes in text | Unprofessional look | Use smart quote entities |

## Validation

The pack script automatically validates. If validation fails:

1. Check the error message for the problematic element
2. Common fixes:
   - Ensure all tags are properly closed
   - Check ID uniqueness
   - Verify `<w:rPr>` comes before `<w:t>` in runs

## Output Location

Save the output file to the same project folder as the input:
```
projects/PROP-XXX-ProjectName/DNV Proposal [Project Name].docx
```
