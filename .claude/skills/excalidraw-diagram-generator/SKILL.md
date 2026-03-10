---
name: excalidraw-diagram-generator
description: 'Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process", "draw a system architecture", "create a mind map", or "generate an Excalidraw file". Supports flowcharts, relationship diagrams, mind maps, and system architecture diagrams. Outputs .excalidraw JSON files that can be opened directly in Excalidraw.'
---

# Excalidraw Diagram Generator

A skill for generating Excalidraw-format diagrams from natural language descriptions. This skill helps create visual representations of processes, systems, relationships, and ideas without manual drawing.

## When to Use This Skill

Use this skill when users request:

- "Create a diagram showing..."
- "Make a flowchart for..."
- "Visualize the process of..."
- "Draw the system architecture of..."
- "Generate a mind map about..."
- "Create an Excalidraw file for..."
- "Show the relationship between..."
- "Diagram the workflow of..."

**Supported diagram types:**
- 📊 **Flowcharts**: Sequential processes, workflows, decision trees
- 🔗 **Relationship Diagrams**: Entity relationships, system components, dependencies
- 🧠 **Mind Maps**: Concept hierarchies, brainstorming results, topic organization
- 🏗️ **Architecture Diagrams**: System design, module interactions, data flow
- 📈 **Data Flow Diagrams (DFD)**: Data flow visualization, data transformation processes
- 🏊 **Business Flow (Swimlane)**: Cross-functional workflows, actor-based process flows
- 📦 **Class Diagrams**: Object-oriented design, class structures and relationships
- 🔄 **Sequence Diagrams**: Object interactions over time, message flows
- 🗃️ **ER Diagrams**: Database entity relationships, data models

## Prerequisites

- Clear description of what should be visualized
- Identification of key entities, steps, or concepts
- Understanding of relationships or flow between elements

## Step-by-Step Workflow

### Step 1: Understand the Request

Analyze the user's description to determine:
1. **Diagram type** (flowchart, relationship, mind map, architecture)
2. **Key elements** (entities, steps, concepts)
3. **Relationships** (flow, connections, hierarchy)
4. **Complexity** (number of elements)

### Step 2: Choose the Appropriate Diagram Type

| User Intent | Diagram Type | Example Keywords |
|-------------|--------------|------------------|
| Process flow, steps, procedures | **Flowchart** | "workflow", "process", "steps", "procedure" |
| Connections, dependencies, associations | **Relationship Diagram** | "relationship", "connections", "dependencies", "structure" |
| Concept hierarchy, brainstorming | **Mind Map** | "mind map", "concepts", "ideas", "breakdown" |
| System design, components | **Architecture Diagram** | "architecture", "system", "components", "modules" |
| Data flow, transformation processes | **Data Flow Diagram (DFD)** | "data flow", "data processing", "data transformation" |
| Cross-functional processes, actor responsibilities | **Business Flow (Swimlane)** | "business process", "swimlane", "actors", "responsibilities" |
| Object-oriented design, class structures | **Class Diagram** | "class", "inheritance", "OOP", "object model" |
| Interaction sequences, message flows | **Sequence Diagram** | "sequence", "interaction", "messages", "timeline" |
| Database design, entity relationships | **ER Diagram** | "database", "entity", "relationship", "data model" |

### Step 3: Extract Structured Information

**For Flowcharts:**
- List of sequential steps
- Decision points (if any)
- Start and end points

**For Relationship Diagrams:**
- Entities/nodes (name + optional description)
- Relationships between entities (from → to, with label)

**For Mind Maps:**
- Central topic
- Main branches (3-6 recommended)
- Sub-topics for each branch (optional)

**For Data Flow Diagrams (DFD):**
- Data sources and destinations (external entities)
- Processes (data transformations)
- Data stores (databases, files)
- Data flows (arrows showing data movement from left-to-right or from top-left to bottom-right)
- **Important**: Do not represent process order, only data flow

**For Business Flow (Swimlane):**
- Actors/roles (departments, systems, people) - displayed as header columns
- Process lanes (vertical lanes under each actor)
- Process boxes (activities within each lane)
- Flow arrows (connecting process boxes, including cross-lane handoffs)

**For Class Diagrams:**
- Classes with names
- Attributes with visibility (+, -, #)
- Methods with visibility and parameters
- Relationships: inheritance (solid line + white triangle), implementation (dashed line + white triangle), association (solid line), dependency (dashed line), aggregation (solid line + white diamond), composition (solid line + filled diamond)
- Multiplicity notations (1, 0..1, 1..*, *)

**For Sequence Diagrams:**
- Objects/actors (arranged horizontally at top)
- Lifelines (vertical lines from each object)
- Messages (horizontal arrows between lifelines)
- Synchronous messages (solid arrow), asynchronous messages (dashed arrow)
- Return values (dashed arrows)
- Activation boxes (rectangles on lifelines during execution)
- Time flows from top to bottom

**For ER Diagrams:**
- Entities (rectangles with entity names)
- Attributes (listed inside entities)
- Primary keys (underlined or marked with PK)
- Foreign keys (marked with FK)
- Relationships (lines connecting entities)
- Cardinality: 1:1 (one-to-one), 1:N (one-to-many), N:M (many-to-many)
- Junction/associative entities for many-to-many relationships (dashed rectangles)

### Step 4: Generate the Excalidraw JSON

Create the `.excalidraw` file with appropriate elements:

**Available element types:**
- `rectangle`: Boxes for entities, steps, concepts
- `ellipse`: Alternative shapes for emphasis
- `diamond`: Decision points
- `arrow`: Directional connections
- `text`: Labels and annotations

**Key properties to set:**
- **Position**: `x`, `y` coordinates
- **Size**: `width`, `height`
- **Style**: `strokeColor`, `backgroundColor`, `fillStyle`
- **Font**: `fontFamily: 5` (Excalifont - **required for all text elements**)
- **Text**: Embedded text for labels
- **Connections**: `points` array for arrows

**Important**: All text elements must use `fontFamily: 5` (Excalifont) for consistent visual appearance.

### Step 5: Format the Output

Structure the complete Excalidraw file:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    // Array of diagram elements
  ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": 20
  },
  "files": {}
}
```

### Step 6: Save and Provide Instructions

1. Save as `<descriptive-name>.excalidraw`
2. Inform user how to open:
   - Visit https://excalidraw.com
   - Click "Open" or drag-and-drop the file
   - Or use Excalidraw VS Code extension

## Best Practices

### Element Count Guidelines

| Diagram Type | Recommended Count | Maximum |
|--------------|-------------------|---------|
| Flowchart steps | 3-10 | 15 |
| Relationship entities | 3-8 | 12 |
| Mind map branches | 4-6 | 8 |
| Mind map sub-topics per branch | 2-4 | 6 |

### Layout Tips

1. **Start positions**: Center important elements, use consistent spacing
2. **Spacing**: 
   - Horizontal gap: 200-300px between elements
   - Vertical gap: 100-150px between rows
3. **Colors**: Use consistent color scheme
   - Primary elements: Light blue (`#a5d8ff`)
   - Secondary elements: Light green (`#b2f2bb`)
   - Important/Central: Yellow (`#ffd43b`)
   - Alerts/Warnings: Light red (`#ffc9c9`)
4. **Text sizing**: 16-24px for readability
5. **Font**: Always use `fontFamily: 5` (Excalifont) for all text elements
6. **Arrow style**: Use straight arrows for simple flows, curved for complex relationships

### Complexity Management

**If user request has too many elements:**
- Suggest breaking into multiple diagrams
- Focus on main elements first
- Offer to create detailed sub-diagrams

**Example response:**
```
"Your request includes 15 components. For clarity, I recommend:
1. High-level architecture diagram (6 main components)
2. Detailed diagram for each subsystem

Would you like me to start with the high-level view?"
```

## Example Prompts and Responses

### Example 1: Simple Flowchart

**User:** "Create a flowchart for user registration"

**Agent generates:**
1. Extract steps: "Enter email" → "Verify email" → "Set password" → "Complete"
2. Create flowchart with 4 rectangles + 3 arrows
3. Save as `user-registration-flow.excalidraw`

### Example 2: Relationship Diagram

**User:** "Diagram the relationship between User, Post, and Comment entities"

**Agent generates:**
1. Entities: User, Post, Comment
2. Relationships: User → Post ("creates"), User → Comment ("writes"), Post → Comment ("contains")
3. Save as `user-content-relationships.excalidraw`

### Example 3: Mind Map

**User:** "Mind map about machine learning concepts"

**Agent generates:**
1. Center: "Machine Learning"
2. Branches: Supervised Learning, Unsupervised Learning, Reinforcement Learning, Deep Learning
3. Sub-topics under each branch
4. Save as `machine-learning-mindmap.excalidraw`

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Elements overlap | Increase spacing between coordinates |
| Text doesn't fit in boxes | Increase box width or reduce font size |
| Too many elements | Break into multiple diagrams |
| Unclear layout | Use grid layout (rows/columns) or radial layout (mind maps) |
| Colors inconsistent | Define color palette upfront based on element types |

## Advanced Techniques

### Grid Layout (for Relationship Diagrams)
```javascript
const columns = Math.ceil(Math.sqrt(entityCount));
const x = startX + (index % columns) * horizontalGap;
const y = startY + Math.floor(index / columns) * verticalGap;
```

### Radial Layout (for Mind Maps)
```javascript
const angle = (2 * Math.PI * index) / branchCount;
const x = centerX + radius * Math.cos(angle);
const y = centerY + radius * Math.sin(angle);
```

### Auto-generated IDs
Use timestamp + random string for unique IDs:
```javascript
const id = Date.now().toString(36) + Math.random().toString(36).substr(2);
```

## Output Format

Always provide:
1. ✅ Complete `.excalidraw` JSON file
2. 📊 Summary of what was created
3. 📝 Element count
4. 💡 Instructions for opening/editing

**Example summary:**
```
Created: user-workflow.excalidraw
Type: Flowchart
Elements: 7 rectangles, 6 arrows, 1 title text
Total: 14 elements

To view:
1. Visit https://excalidraw.com
2. Drag and drop user-workflow.excalidraw
3. Or use File → Open in Excalidraw VS Code extension
```

## Validation Checklist

Before delivering the diagram:
- [ ] All elements have unique IDs
- [ ] Coordinates prevent overlapping
- [ ] Text is readable (font size 16+)
- [ ] **All text elements use `fontFamily: 5` (Excalifont)**
- [ ] Arrows connect logically
- [ ] Colors follow consistent scheme
- [ ] File is valid JSON
- [ ] Element count is reasonable (<20 for clarity)

## Icon Libraries (Optional Enhancement)

For specialized diagrams (e.g., AWS/GCP/Azure architecture diagrams), you can use pre-made icon libraries from Excalidraw. This provides professional, standardized icons instead of basic shapes.

### When User Requests Icons

**If user asks for AWS/cloud architecture diagrams or mentions wanting to use specific icons:**

1. **Check if library exists**: Look for `libraries/<library-name>/reference.md`
2. **If library exists**: Proceed to use icons (see AI Assistant Workflow below)
3. **If library does NOT exist**: Respond with setup instructions:

   ```
   To use [AWS/GCP/Azure/etc.] architecture icons, please follow these steps:
   
   1. Visit https://libraries.excalidraw.com/
   2. Search for "[AWS Architecture Icons/etc.]" and download the .excalidrawlib file
   3. Create directory: skills/excalidraw-diagram-generator/libraries/[icon-set-name]/
   4. Place the downloaded file in that directory
   5. Run the splitter script:
      python skills/excalidraw-diagram-generator/scripts/split-excalidraw-library.py skills/excalidraw-diagram-generator/libraries/[icon-set-name]/
   
   This will split the library into individual icon files for efficient use.
   After setup is complete, I can create your diagram using the actual AWS/cloud icons.
   
   Alternatively, I can create the diagram now using simple shapes (rectangles, ellipses) 
   which you can later replace with icons manually in Excalidraw.
   ```

### User Setup Instructions (Detailed)

**Step 1: Create Library Directory**
```bash
mkdir -p skills/excalidraw-diagram-generator/libraries/aws-architecture-icons
```

**Step 2: Download Library**
- Visit: https://libraries.excalidraw.com/
- Search for your desired icon set (e.g., "AWS Architecture Icons")
- Click download to get the `.excalidrawlib` file
- Example categories (availability varies; confirm on the site):
   - Cloud service icons
   - UI/Material icons
   - Flowchart symbols

**Step 3: Place Library File**
- Rename the downloaded file to match the directory name (e.g., `aws-architecture-icons.excalidrawlib`)
- Move it to the directory created in Step 1

**Step 4: Run Splitter Script**
```bash
python skills/excalidraw-diagram-generator/scripts/split-excalidraw-library.py skills/excalidraw-diagram-generator/libraries/aws-architecture-icons/
```

**Step 5: Verify Setup**
After running the script, verify the following structure exists:
```
skills/excalidraw-diagram-generator/libraries/aws-architecture-icons/
  aws-architecture-icons.excalidrawlib  (original)
  reference.md                          (generated - icon lookup table)
  icons/                                (generated - individual icon files)
    API-Gateway.json
    CloudFront.json
    EC2.json
    Lambda.json
    RDS.json
    S3.json
    ...
```

### AI Assistant Workflow

**When icon libraries are available in `libraries/`:**

**RECOMMENDED APPROACH: Use Python Scripts (Efficient & Reliable)**

The repository includes Python scripts that handle icon integration automatically:

1. **Create base diagram structure**:
   - Create `.excalidraw` file with basic layout (title, boxes, regions)
   - This establishes the canvas and overall structure

2. **Add icons using Python script**:
   ```bash
   python skills/excalidraw-diagram-generator/scripts/add-icon-to-diagram.py \
     <diagram-path> <icon-name> <x> <y> [--label "Text"] [--library-path PATH]
   ```
   - Edit via `.excalidraw.edit` is enabled by default to avoid overwrite issues; pass `--no-use-edit-suffix` to disable.
   
   **Examples**:
   ```bash
   # Add EC2 icon at position (400, 300) with label
   python scripts/add-icon-to-diagram.py diagram.excalidraw EC2 400 300 --label "Web Server"
   
   # Add VPC icon at position (200, 150)
   python scripts/add-icon-to-diagram.py diagram.excalidraw VPC 200 150
   
   # Add icon from different library
   python scripts/add-icon-to-diagram.py diagram.excalidraw Compute-Engine 500 200 \
     --library-path libraries/gcp-icons --label "API Server"
   ```

3. **Add connecting arrows**:
   ```bash
   python skills/excalidraw-diagram-generator/scripts/add-arrow.py \
     <diagram-path> <from-x> <from-y> <to-x> <to-y> [--label "Text"] [--style solid|dashed|dotted] [--color HEX]
   ```
   - Edit via `.excalidraw.edit` is enabled by default to avoid overwrite issues; pass `--no-use-edit-suffix` to disable.
   
   **Examples**:
   ```bash
   # Simple arrow from (300, 250) to (500, 300)
   python scripts/add-arrow.py diagram.excalidraw 300 250 500 300
   
   # Arrow with label
   python scripts/add-arrow.py diagram.excalidraw 300 250 500 300 --label "HTTPS"
   
   # Dashed arrow with custom color
   python scripts/add-arrow.py diagram.excalidraw 400 350 600 400 --style dashed --color "#7950f2"
   ```

4. **Workflow summary**:
   ```bash
   # Step 1: Create base diagram with title and structure
   # (Create .excalidraw file with initial elements)
   
   # Step 2: Add icons with labels
   python scripts/add-icon-to-diagram.py my-diagram.excalidraw "Internet-gateway" 200 150 --label "Internet Gateway"
   python scripts/add-icon-to-diagram.py my-diagram.excalidraw VPC 250 250
   python scripts/add-icon-to-diagram.py my-diagram.excalidraw ELB 350 300 --label "Load Balancer"
   python scripts/add-icon-to-diagram.py my-diagram.excalidraw EC2 450 350 --label "EC2 Instance"
   python scripts/add-icon-to-diagram.py my-diagram.excalidraw RDS 550 400 --label "Database"
   
   # Step 3: Add connecting arrows
   python scripts/add-arrow.py my-diagram.excalidraw 250 200 300 250  # Internet → VPC
   python scripts/add-arrow.py my-diagram.excalidraw 300 300 400 300  # VPC → ELB
   python scripts/add-arrow.py my-diagram.excalidraw 400 330 500 350  # ELB → EC2
   python scripts/add-arrow.py my-diagram.excalidraw 500 380 600 400  # EC2 → RDS
   ```

**Benefits of Python Script Approach**:
- ✅ **No token consumption**: Icon JSON data (200-1000 lines each) never enters AI context
- ✅ **Accurate transformations**: Coordinate calculations handled deterministically
- ✅ **ID management**: Automatic UUID generation prevents conflicts
- ✅ **Reliable**: No risk of coordinate miscalculation or ID collision
- ✅ **Fast**: Direct file manipulation, no parsing overhead
- ✅ **Reusable**: Works with any Excalidraw library you provide

**ALTERNATIVE: Manual Icon Integration (Not Recommended)**

Only use this if Python scripts are unavailable:

1. **Check for libraries**: 
   ```
   List directory: skills/excalidraw-diagram-generator/libraries/
   Look for subdirectories containing reference.md files
   ```

2. **Read reference.md**:
   ```
   Open: libraries/<library-name>/reference.md
   This is lightweight (typically <300 lines) and lists all available icons
   ```

3. **Find relevant icons**:
   ```
   Search the reference.md table for icon names matching diagram needs
   Example: For AWS diagram with EC2, S3, Lambda → Find "EC2", "S3", "Lambda" in table
   ```

4. **Load specific icon data** (WARNING: Large files):
   ```
   Read ONLY the needed icon files:
   - libraries/aws-architecture-icons/icons/EC2.json (200-300 lines)
   - libraries/aws-architecture-icons/icons/S3.json (200-300 lines)
   - libraries/aws-architecture-icons/icons/Lambda.json (200-300 lines)
   Note: Each icon file is 200-1000 lines - this consumes significant tokens
   ```

5. **Extract and transform elements**:
   ```
   Each icon JSON contains an "elements" array
   Calculate bounding box (min_x, min_y, max_x, max_y)
   Apply offset to all x/y coordinates
   Generate new unique IDs for all elements
   Update groupIds references
   Copy transformed elements into your diagram
   ```

6. **Position icons and add connections**:
   ```
   Adjust x/y coordinates to position icons correctly in the diagram
   Update IDs to ensure uniqueness across diagram
   Add connecting arrows and labels as needed
   ```

**Manual Integration Challenges**:
- ⚠️ High token consumption (200-1000 lines per icon × number of icons)
- ⚠️ Complex coordinate transformation calculations
- ⚠️ Risk of ID collision if not handled carefully
- ⚠️ Time-consuming for diagrams with many icons

### Example: Creating AWS Diagram with Icons

**Request**: "Create an AWS architecture diagram with Internet Gateway, VPC, ELB, EC2, and RDS"

**Recommended Workflow (using Python scripts)**:
**Request**: "Create an AWS architecture diagram with Internet Gateway, VPC, ELB, EC2, and RDS"

**Recommended Workflow (using Python scripts)**:

```bash
# Step 1: Create base diagram file with title
# Create my-aws-diagram.excalidraw with basic structure (title, etc.)

# Step 2: Check icon availability
# Read: libraries/aws-architecture-icons/reference.md
# Confirm icons exist: Internet-gateway, VPC, ELB, EC2, RDS

# Step 3: Add icons with Python script
python scripts/add-icon-to-diagram.py my-aws-diagram.excalidraw "Internet-gateway" 150 100 --label "Internet Gateway"
python scripts/add-icon-to-diagram.py my-aws-diagram.excalidraw VPC 200 200
python scripts/add-icon-to-diagram.py my-aws-diagram.excalidraw ELB 350 250 --label "Load Balancer"
python scripts/add-icon-to-diagram.py my-aws-diagram.excalidraw EC2 500 300 --label "Web Server"
python scripts/add-icon-to-diagram.py my-aws-diagram.excalidraw RDS 650 350 --label "Database"

# Step 4: Add connecting arrows
python scripts/add-arrow.py my-aws-diagram.excalidraw 200 150 250 200  # Internet → VPC
python scripts/add-arrow.py my-aws-diagram.excalidraw 265 230 350 250  # VPC → ELB
python scripts/add-arrow.py my-aws-diagram.excalidraw 415 280 500 300  # ELB → EC2
python scripts/add-arrow.py my-aws-diagram.excalidraw 565 330 650 350 --label "SQL" --style dashed

# Result: Complete diagram with professional AWS icons, labels, and connections
```

**Benefits**:
- No manual coordinate calculation
- No token consumption for icon data
- Deterministic, reliable results
- Easy to iterate and adjust positions

**Alternative Workflow (manual, if scripts unavailable)**:
1. Check: `libraries/aws-architecture-icons/reference.md` exists → Yes
2. Read reference.md → Find entries for Internet-gateway, VPC, ELB, EC2, RDS
3. Load:
   - `icons/Internet-gateway.json` (298 lines)
   - `icons/VPC.json` (550 lines)
   - `icons/ELB.json` (363 lines)
   - `icons/EC2.json` (231 lines) 
   - `icons/RDS.json` (similar size)
   **Total: ~2000+ lines of JSON to process**
4. Extract elements from each JSON
5. Calculate bounding boxes and offsets for each icon
6. Transform all coordinates (x, y) for positioning
7. Generate unique IDs for all elements
8. Add arrows showing data flow
9. Add text labels
10. Generate final `.excalidraw` file

**Challenges with manual approach**:
- High token consumption (~2000-5000 lines)
- Complex coordinate math
- Risk of ID conflicts

### Supported Icon Libraries (Examples — verify availability)

- This workflow works with any valid `.excalidrawlib` file you provide.
- Examples of library categories you may find on https://libraries.excalidraw.com/:
   - Cloud service icons
   - Kubernetes / infrastructure icons
   - UI / Material icons
   - Flowchart / diagram symbols
   - Network diagram icons
- Availability and naming can change; verify exact library names on the site before use.

### Fallback: No Icons Available

**If no icon libraries are set up:**
- Create diagrams using basic shapes (rectangles, ellipses, arrows)
- Use color coding and text labels to distinguish components
- Inform user they can add icons later or set up libraries for future diagrams
- The diagram will still be functional and clear, just less visually polished

## PNG Export & Mermaid Conversion

The skill includes a powerful browser-based tool for exporting Excalidraw diagrams to PNG/SVG and converting Mermaid diagrams to Excalidraw format.

### Tool Location

**File**: `scripts/export-to-png.html`

**Usage**: Open the HTML file in any web browser (Chrome, Firefox, Safari, Edge)

```bash
# From Windows
start scripts/export-to-png.html

# From macOS
open scripts/export-to-png.html

# From Linux
xdg-open scripts/export-to-png.html
```

### Features

#### 📸 PNG Export Tab

Convert `.excalidraw` files to high-quality PNG or SVG images:

1. **Drag & Drop Interface**: Drop your `.excalidraw` file or click to browse
2. **Live Preview**: See the rendered diagram before exporting
3. **Export Options**:
   - **Scale**: 1x (original), 2x (high quality - recommended), 3x (print), 4x (extra high)
   - **Background Color**: Choose custom background (default: white)
   - **Format**: PNG or SVG
   - **Padding**: Add padding around the diagram (0-100px)
4. **Download**: Export to PNG or SVG with one click

**Recommended Settings for Presentations**:
- Scale: 2x or 3x
- Format: PNG
- Background: White (#ffffff) or transparent
- Padding: 20-40px

**Recommended Settings for Print**:
- Scale: 3x or 4x
- Format: PNG or SVG
- Background: White
- Padding: 40px

#### 🔄 Mermaid Converter Tab

Convert Mermaid diagram syntax to Excalidraw format:

1. **Paste Mermaid Code**: Enter your Mermaid diagram text
2. **Quick Examples**: Load pre-made examples (flowchart, sequence, class, gantt, pie)
3. **Convert**: Generate Excalidraw JSON instantly
4. **Export Options**:
   - Download as `.excalidraw` file
   - Copy JSON to clipboard
   - **Convert & Export PNG**: One-click conversion + PNG export

**Supported Mermaid Types**:
- Flowcharts (`graph TD`, `graph LR`)
- Sequence diagrams (`sequenceDiagram`)
- Class diagrams (`classDiagram`)
- Gantt charts (`gantt`)
- Pie charts (`pie`)

### Workflow Integration

#### Creating New Diagrams from Mermaid

When users want to create diagrams using Mermaid syntax:

1. Direct them to use the Mermaid Converter tab
2. They can type or paste Mermaid code
3. Click "Convert & Export PNG" for instant PNG output
4. Or download `.excalidraw` for further editing

**Example workflow**:
```
User: "Create a flowchart showing the project lifecycle"

Agent: Creates Mermaid syntax or directs user to the tool

User opens: scripts/export-to-png.html
Pastes Mermaid code or uses example
Clicks: "Convert & Export PNG"
Result: Gets both .excalidraw file AND PNG image
```

#### Exporting Existing Diagrams

When users need PNG versions of existing `.excalidraw` files:

1. Open `scripts/export-to-png.html`
2. Switch to "PNG Export" tab
3. Drag and drop the `.excalidraw` file
4. Adjust settings (scale, background, padding)
5. Click "Download PNG"

**Use cases**:
- Adding diagrams to documentation (Markdown, Word, PowerPoint)
- Sharing diagrams via email or chat
- Including in reports or presentations
- Posting on websites or wikis

#### Batch Processing

For multiple diagrams:
1. Keep the browser tool open
2. Export each diagram sequentially
3. Adjust settings per diagram as needed

### Integration with Agent Workflow

When generating diagrams for users, provide complete instructions:

**Example response after creating diagram**:
```
Created: project-workflow.excalidraw

📊 Diagram Details:
- Type: Flowchart
- Elements: 12 boxes, 11 arrows
- File saved to: ai-promptengineering-visuals/project-workflow.excalidraw

🎨 To Export as PNG:
1. Open: .agents/skills/excalidraw-diagram-generator/scripts/export-to-png.html
2. Drag and drop project-workflow.excalidraw
3. Select scale: 2x (recommended for presentations)
4. Click "Download PNG"

The PNG will be ready for your slides, documentation, or reports!
```

### Advanced: Command-Line PNG Export

For users who prefer automation, you can document this future enhancement:

**Future Tool** (not yet implemented):
```bash
python scripts/excalidraw-to-png.py <input.excalidraw> [output.png] [--scale 2] [--bg white]
```

This would enable:
- Automated batch processing
- CI/CD integration
- Scripted documentation generation

Currently, the browser tool provides the most reliable and feature-rich export capability.

## References

See bundled references for:
- `references/excalidraw-schema.md` - Complete Excalidraw JSON schema
- `references/element-types.md` - Detailed element type specifications
- `templates/flowchart-template.json` - Basic flowchart starter
- `templates/relationship-template.json` - Relationship diagram starter
- `templates/mindmap-template.json` - Mind map starter
- `scripts/split-excalidraw-library.py` - Tool to split `.excalidrawlib` files
- `scripts/export-to-png.html` - PNG export and Mermaid converter tool
- `scripts/README.md` - Documentation for library tools
- `scripts/.gitignore` - Prevents local Python artifacts from being committed

## Limitations

- Complex curves are simplified to straight/basic curved lines
- Hand-drawn roughness is set to default (1)
- No embedded images support in auto-generation
- Maximum recommended elements: 20 per diagram
- No automatic collision detection (use spacing guidelines)

## Future Enhancements

Potential improvements:
- Auto-layout optimization algorithms
- ~~Import from Mermaid/PlantUML syntax~~ ✅ **Implemented**: See PNG Export & Mermaid Conversion section
- ~~PNG/SVG export capability~~ ✅ **Implemented**: See PNG Export & Mermaid Conversion section
- Template library expansion
- Interactive editing after generation
- Command-line PNG export tool (Python-based)
- Batch processing automation
