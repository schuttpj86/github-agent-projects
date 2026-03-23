const XLSX = require('xlsx');
const workbook = XLSX.readFile('projects/PROP-004-PeakGen/rfp/2. LT2029 Stability Technical Proforma V4.xlsx');

// Helper function to clean and print rows
function printSheet(sheetName, maxRows) {
  console.log('\n' + '='.repeat(80));
  console.log('=== ' + sheetName + ' ===');
  console.log('='.repeat(80));

  const sheet = workbook.Sheets[sheetName];
  const data = XLSX.utils.sheet_to_json(sheet, {header: 1, defval: ''});

  const rows = maxRows ? data.slice(0, maxRows) : data;
  rows.forEach((row, i) => {
    const filtered = row.map(c => {
      if (c === null || c === undefined) return '';
      return String(c).trim();
    }).filter(c => c !== '');
    if (filtered.length > 0) {
      console.log('Row ' + (i+1) + ': ' + filtered.join(' | '));
    }
  });
}

// Print all sheets
printSheet('Introduction', 60);
printSheet('A Solution Outline', 60);
printSheet('B. Feasibility Simulation', 120);
printSheet('C. DRC Data', 25);
