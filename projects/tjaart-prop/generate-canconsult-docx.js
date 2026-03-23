const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, PageBreak,
  Tab, TabStopPosition, TabStopType
} = require("docx");

// ── Brand Colors ──
const TEAL_DK = "1D5C5C";
const TEAL = "2A7A7A";
const TEAL_LT = "E4F4F4";
const INK = "1E1E1E";
const INK_MID = "555555";
const INK_LIGHT = "999999";
const WHITE = "FFFFFF";
const RULE = "E8E8E8";

// ── Reusable helpers ──
const noBorder = { style: BorderStyle.NONE, size: 0, color: WHITE };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: RULE };
const thinBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };

const PAGE_WIDTH = 12240; // US Letter
const PAGE_HEIGHT = 15840;
const MARGIN = 1440; // 1 inch
const CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN; // 9360

function spacer(pts = 200) {
  return new Paragraph({ spacing: { before: pts, after: 0 }, children: [] });
}

function sectionHeading(text) {
  return new Paragraph({
    spacing: { before: 360, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: TEAL, space: 6 } },
    children: [new TextRun({ text: text.toUpperCase(), bold: true, font: "Montserrat", size: 28, color: TEAL_DK })]
  });
}

function bodyText(text) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    children: [new TextRun({ text, font: "Inter", size: 23, color: INK_MID })]
  });
}

function termRow(key, value) {
  return new TableRow({
    children: [
      new TableCell({
        borders: { top: noBorder, bottom: thinBorder, left: noBorder, right: noBorder },
        width: { size: 2800, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 0, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: key, bold: true, font: "Inter", size: 21, color: TEAL_DK })] })]
      }),
      new TableCell({
        borders: { top: noBorder, bottom: thinBorder, left: noBorder, right: noBorder },
        width: { size: 6560, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 120, right: 0 },
        children: [new Paragraph({ children: [new TextRun({ text: value, font: "Inter", size: 21, color: INK_MID })] })]
      })
    ]
  });
}

function termsTable(items) {
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: [2800, 6560],
    rows: items.map(([k, v]) => termRow(k, v))
  });
}

// ── Phase card as a mini table ──
function phaseCard(num, headerText, title, items) {
  const headerRow = new TableRow({
    children: [new TableCell({
      borders: { top: { style: BorderStyle.SINGLE, size: 8, color: TEAL }, bottom: noBorder, left: thinBorder, right: thinBorder },
      shading: { fill: TEAL_LT, type: ShadingType.CLEAR },
      width: { size: 4500, type: WidthType.DXA },
      margins: { top: 80, bottom: 80, left: 120, right: 120 },
      children: [new Paragraph({ children: [
        new TextRun({ text: `PHASE ${num}  `, bold: true, font: "Inter", size: 18, color: TEAL }),
        new TextRun({ text: headerText, bold: true, font: "Inter", size: 18, color: TEAL_DK })
      ] })]
    })]
  });

  const titleRow = new TableRow({
    children: [new TableCell({
      borders: { top: noBorder, bottom: noBorder, left: thinBorder, right: thinBorder },
      width: { size: 4500, type: WidthType.DXA },
      margins: { top: 80, bottom: 40, left: 120, right: 120 },
      children: [new Paragraph({ children: [new TextRun({ text: title, bold: true, font: "Inter", size: 22, color: INK })] })]
    })]
  });

  const itemRows = items.map(item => new TableRow({
    children: [new TableCell({
      borders: { top: noBorder, bottom: noBorder, left: thinBorder, right: thinBorder },
      width: { size: 4500, type: WidthType.DXA },
      margins: { top: 20, bottom: 20, left: 120, right: 120 },
      children: [new Paragraph({ children: [
        new TextRun({ text: "\u25B8 ", font: "Inter", size: 20, color: TEAL }),
        new TextRun({ text: item, font: "Inter", size: 20, color: INK_MID })
      ] })]
    })]
  }));

  const bottomRow = new TableRow({
    children: [new TableCell({
      borders: { top: noBorder, bottom: thinBorder, left: thinBorder, right: thinBorder },
      width: { size: 4500, type: WidthType.DXA },
      margins: { top: 0, bottom: 60, left: 120, right: 120 },
      children: [new Paragraph({ children: [] })]
    })]
  });

  return new Table({
    width: { size: 4500, type: WidthType.DXA },
    columnWidths: [4500],
    rows: [headerRow, titleRow, ...itemRows, bottomRow]
  });
}

// ── Fee schedule table ──
function feeTable() {
  const hdrBorder = { style: BorderStyle.SINGLE, size: 1, color: TEAL_DK };
  const hdrBorders = { top: hdrBorder, bottom: hdrBorder, left: hdrBorder, right: hdrBorder };
  const colWidths = [2200, 1800, 2400, 2960];

  function hdrCell(text, width) {
    return new TableCell({
      borders: hdrBorders,
      shading: { fill: TEAL_DK, type: ShadingType.CLEAR },
      width: { size: width, type: WidthType.DXA },
      margins: { top: 80, bottom: 80, left: 120, right: 120 },
      children: [new Paragraph({ children: [new TextRun({ text: text.toUpperCase(), bold: true, font: "Inter", size: 19, color: WHITE })] })]
    });
  }

  function dataCell(text, width, opts = {}) {
    return new TableCell({
      borders: thinBorders,
      shading: opts.shaded ? { fill: TEAL_LT, type: ShadingType.CLEAR } : undefined,
      width: { size: width, type: WidthType.DXA },
      margins: { top: 80, bottom: 80, left: 120, right: 120 },
      children: [new Paragraph({ children: [new TextRun({
        text,
        bold: opts.bold || false,
        font: "Inter",
        size: 21,
        color: opts.rateColor ? TEAL_DK : (opts.first ? INK : INK_MID)
      })] })]
    });
  }

  const headerRow = new TableRow({ children: colWidths.map((w, i) => hdrCell(["Engagement", "Model", "Rate", "Notes"][i], w)) });

  const data = [
    ["Assessment Week", "Daily Rate", "$1,660+ / day", "Portal-to-portal + travel expenses"],
    ["Management Lectures", "Hourly", "$300\u2013$600 / hr", "Billed per session"],
    ["Technical Plant Report", "Fixed Milestone", "$50,000+", "Scales with plant size & complexity"],
    ["Training Dept. Support", "Monthly Retainer", "$5,000\u2013$15,000+ / mo", "Ongoing strategic advisory"]
  ];

  const dataRows = data.map((row, ri) => new TableRow({
    children: row.map((cell, ci) => dataCell(cell, colWidths[ci], {
      shaded: ri % 2 === 1,
      first: ci === 0,
      rateColor: ci === 2,
      bold: ci === 2
    }))
  }));

  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [headerRow, ...dataRows]
  });
}

// ── Build the document ──
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Inter", size: 24 } }
    }
  },
  sections: [
    // ── SECTION 1: Cover page ──
    {
      properties: {
        page: {
          size: { width: PAGE_WIDTH, height: PAGE_HEIGHT },
          margin: { top: 0, right: 0, bottom: 0, left: 0 }
        }
      },
      children: [
        // Teal cover block (simulated with a full-width table)
        new Table({
          width: { size: PAGE_WIDTH, type: WidthType.DXA },
          columnWidths: [PAGE_WIDTH],
          rows: [new TableRow({
            children: [new TableCell({
              borders: noBorders,
              shading: { fill: TEAL_DK, type: ShadingType.CLEAR },
              width: { size: PAGE_WIDTH, type: WidthType.DXA },
              margins: { top: 720, bottom: 600, left: 900, right: 900 },
              children: [
                new Paragraph({
                  spacing: { after: 160 },
                  children: [new TextRun({ text: "CANCONSULT \u00B7 ADVISORY SERVICES", font: "Inter", size: 18, color: "B3C9C9", bold: true, characterSpacing: 100 })]
                }),
                new Paragraph({
                  spacing: { after: 200 },
                  children: [new TextRun({ text: "BUSINESS\nPROPOSAL", font: "Montserrat", size: 64, bold: true, color: WHITE })]
                }),
                new Paragraph({
                  children: [new TextRun({ text: "Senior Canmaking Expert \u00B7 D&I Process \u00B7 Management Training \u00B7 Training Department Development", font: "Inter", size: 22, color: "A0BFBF" })]
                })
              ]
            })]
          })]
        }),
        // Prepared-for strip
        new Table({
          width: { size: PAGE_WIDTH, type: WidthType.DXA },
          columnWidths: [6000, 6240],
          rows: [new TableRow({
            children: [
              new TableCell({
                borders: { top: noBorder, bottom: noBorder, left: { style: BorderStyle.SINGLE, size: 10, color: TEAL }, right: noBorder },
                shading: { fill: TEAL_LT, type: ShadingType.CLEAR },
                width: { size: 6000, type: WidthType.DXA },
                margins: { top: 200, bottom: 200, left: 900, right: 120 },
                children: [
                  new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: "PREPARED FOR", font: "Inter", size: 16, bold: true, color: TEAL, characterSpacing: 60 })] }),
                  new Paragraph({ children: [new TextRun({ text: "US Canmaking Company", font: "Inter", size: 26, bold: true, color: INK })] })
                ]
              }),
              new TableCell({
                borders: noBorders,
                shading: { fill: TEAL_LT, type: ShadingType.CLEAR },
                width: { size: 6240, type: WidthType.DXA },
                margins: { top: 200, bottom: 200, left: 120, right: 900 },
                children: [
                  new Paragraph({ alignment: AlignmentType.RIGHT, children: [
                    new TextRun({ text: "Proposal Ref: ", font: "Inter", size: 19, color: INK_MID, bold: true }),
                    new TextRun({ text: "CC-2026-001", font: "Inter", size: 19, color: INK_LIGHT })
                  ] }),
                  new Paragraph({ alignment: AlignmentType.RIGHT, children: [
                    new TextRun({ text: "Date: ", font: "Inter", size: 19, color: INK_MID, bold: true }),
                    new TextRun({ text: "March 23, 2026", font: "Inter", size: 19, color: INK_LIGHT })
                  ] }),
                  new Paragraph({ alignment: AlignmentType.RIGHT, children: [
                    new TextRun({ text: "Status: ", font: "Inter", size: 19, color: INK_MID, bold: true }),
                    new TextRun({ text: "Confidential", font: "Inter", size: 19, color: INK_LIGHT })
                  ] })
                ]
              })
            ]
          })]
        }),
        spacer(600),
        // Nice centered tagline
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 400, after: 0 },
          children: [new TextRun({ text: "World-Recognized Expert  \u00B7  Drawn & Ironed Specialist  \u00B7  US Manufacturing \u00B7 2026", font: "Inter", size: 20, color: INK_LIGHT, italics: true })]
        })
      ]
    },

    // ── SECTION 2: Body content ──
    {
      properties: {
        page: {
          size: { width: PAGE_WIDTH, height: PAGE_HEIGHT },
          margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN }
        }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: "CanConsult  \u00B7  Proposal CC-2026-001  \u00B7  Confidential", font: "Inter", size: 16, color: INK_LIGHT })]
          })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            border: { top: { style: BorderStyle.SINGLE, size: 1, color: RULE, space: 6 } },
            children: [
              new TextRun({ text: "CanConsult  \u00B7  Page ", font: "Inter", size: 16, color: INK_LIGHT }),
              new TextRun({ children: [PageNumber.CURRENT], font: "Inter", size: 16, color: INK_LIGHT })
            ]
          })]
        })
      },
      children: [
        // ── Executive Summary ──
        sectionHeading("Executive Summary"),
        bodyText("CanConsult proposes a structured, phased advisory engagement to support your US canmaking facility \u2014 delivered by a retired, world-recognized senior expert with deep specialization in the Drawn and Ironed (D&I) process."),
        spacer(80),
        termsTable([
          ["Scope", "On-site technical assessment, management knowledge transfer, and long-term training department development"],
          ["Expert Profile", "World-recognized, retired senior specialist \u00B7 10+ years D&I process expertise \u00B7 operational and structural insight"],
          ["Talent Crisis", "56% of US manufacturers are struggling to retain skilled talent as the workforce ages"],
          ["Digital Imperative", "84.7% of US manufacturers are actively prioritizing upskilling and digital transformation in 2026"],
          ["Strategic Value", "A structured, expert-led training department is no longer optional \u2014 it is a competitive requirement"]
        ]),

        // ── Phased Engagement Model ──
        spacer(200),
        sectionHeading("Phased Engagement Model"),
        spacer(80),
        // Two phase cards side-by-side
        new Table({
          width: { size: CONTENT_WIDTH, type: WidthType.DXA },
          columnWidths: [4500, 360, 4500],
          rows: [new TableRow({
            children: [
              new TableCell({
                borders: noBorders,
                width: { size: 4500, type: WidthType.DXA },
                margins: { top: 0, bottom: 0, left: 0, right: 0 },
                children: [
                  phaseCard("I", "Discovery & Assessment \u2014 Week 1", "Paid Discovery Phase", [
                    "On-site plant floor observation",
                    "Full D&I process technical review",
                    "Management training lectures",
                    "Structural gap analysis vs. SA model",
                    "Formal written technical report"
                  ])
                ]
              }),
              // Spacer column
              new TableCell({
                borders: noBorders,
                width: { size: 360, type: WidthType.DXA },
                children: [new Paragraph({ children: [] })]
              }),
              new TableCell({
                borders: noBorders,
                width: { size: 4500, type: WidthType.DXA },
                margins: { top: 0, bottom: 0, left: 0, right: 0 },
                children: [
                  phaseCard("II", "Strategic Development \u2014 Ongoing", "Training Department Build-Out", [
                    "Protocol gap remediation plan",
                    "Industry 4.0 / Smart Factory alignment",
                    "Structured career track design",
                    "Formal training program development",
                    "Ongoing strategic retainer support"
                  ])
                ]
              })
            ]
          })]
        }),

        // ── Fee Schedule ──
        spacer(200),
        sectionHeading("Fee Schedule \u2014 2026 US Rates"),
        spacer(80),
        feeTable(),

        // ── Terms & Conditions ──
        spacer(200),
        sectionHeading("Terms & Conditions"),
        spacer(80),
        termsTable([
          ["Billing Start", "Portal-to-portal \u2014 from departure at home base through return"],
          ["Expenses", "Airfare, accommodation, and per diem billed at cost"],
          ["Overtime", "Daily rate covers up to 12 hrs; overtime billed at $152\u2013$412/hr"],
          ["Payment", "Phase I invoiced upon engagement commencement; Phase II monthly in advance"],
          ["Cancellation", "14 days written notice required; travel costs non-refundable once booked"],
          ["Confidentiality", "All plant data, processes, and findings treated as strictly confidential"],
          ["Validity", "This proposal is valid for 30 days from the date of issue"]
        ]),

        // ── Proposal Acceptance ──
        spacer(200),
        sectionHeading("Proposal Acceptance"),
        bodyText("By signing below, both parties agree to the scope and commercial terms outlined in this proposal. A detailed Statement of Work will be issued upon acceptance."),
        spacer(300),

        // Signature block
        new Table({
          width: { size: CONTENT_WIDTH, type: WidthType.DXA },
          columnWidths: [4400, 560, 4400],
          rows: [
            // Labels
            new TableRow({
              children: [
                new TableCell({
                  borders: { top: { style: BorderStyle.SINGLE, size: 4, color: TEAL }, bottom: noBorder, left: noBorder, right: noBorder },
                  width: { size: 4400, type: WidthType.DXA },
                  margins: { top: 80, bottom: 0, left: 0, right: 0 },
                  children: [new Paragraph({ children: [new TextRun({ text: "FOR CANCONSULT", font: "Inter", size: 17, bold: true, color: TEAL, characterSpacing: 40 })] })]
                }),
                new TableCell({ borders: noBorders, width: { size: 560, type: WidthType.DXA }, children: [new Paragraph({ children: [] })] }),
                new TableCell({
                  borders: { top: { style: BorderStyle.SINGLE, size: 4, color: TEAL }, bottom: noBorder, left: noBorder, right: noBorder },
                  width: { size: 4400, type: WidthType.DXA },
                  margins: { top: 80, bottom: 0, left: 0, right: 0 },
                  children: [new Paragraph({ children: [new TextRun({ text: "FOR CLIENT", font: "Inter", size: 17, bold: true, color: TEAL, characterSpacing: 40 })] })]
                })
              ]
            }),
            // Signature lines
            new TableRow({
              children: [
                new TableCell({
                  borders: noBorders,
                  width: { size: 4400, type: WidthType.DXA },
                  margins: { top: 400, bottom: 0, left: 0, right: 0 },
                  children: [
                    new Paragraph({ children: [new TextRun({ text: "________________________", font: "Inter", size: 22, color: INK })] }),
                    new Paragraph({ spacing: { before: 40 }, children: [new TextRun({ text: "Senior Advisor \u00B7 CanConsult", font: "Inter", size: 19, color: INK_MID })] }),
                    new Paragraph({ spacing: { before: 80 }, children: [new TextRun({ text: "Date: ___________________", font: "Inter", size: 19, color: INK_LIGHT })] })
                  ]
                }),
                new TableCell({ borders: noBorders, width: { size: 560, type: WidthType.DXA }, children: [new Paragraph({ children: [] })] }),
                new TableCell({
                  borders: noBorders,
                  width: { size: 4400, type: WidthType.DXA },
                  margins: { top: 400, bottom: 0, left: 0, right: 0 },
                  children: [
                    new Paragraph({ children: [new TextRun({ text: "________________________", font: "Inter", size: 22, color: INK })] }),
                    new Paragraph({ spacing: { before: 40 }, children: [new TextRun({ text: "Authorized Signatory", font: "Inter", size: 19, color: INK_MID })] }),
                    new Paragraph({ spacing: { before: 80 }, children: [new TextRun({ text: "Date: ___________________", font: "Inter", size: 19, color: INK_LIGHT })] })
                  ]
                })
              ]
            })
          ]
        }),

        // ── Footer band ──
        spacer(600),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          border: { top: { style: BorderStyle.SINGLE, size: 1, color: RULE, space: 10 } },
          spacing: { before: 200 },
          children: [new TextRun({ text: "Proposal Ref: CC-2026-001  \u00B7  Confidential  \u00B7  Valid 30 days from March 23, 2026", font: "Inter", size: 18, color: INK_LIGHT })]
        })
      ]
    }
  ]
});

// ── Generate ──
const outputPath = "c:\\AI-projects\\Projects\\github-agent-projects\\projects\\tjaart-prop\\canconsult-proposal.docx";
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log("DOCX created:", outputPath);
}).catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
