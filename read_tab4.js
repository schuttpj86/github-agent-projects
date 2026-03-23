const XLSX = require('xlsx');

const filepath = 'c:/AI-projects/Projects/github-agent-projects/projects/PROP-004-PeakGen/rfp/2. LT2029 Stability Technical Proforma V4.xlsx';
const workbook = XLSX.readFile(filepath);

// Read Tab 4 - "B. Feasibility Simulation"
const sheet = workbook.Sheets['B. Feasibility Simulation'];
const data = XLSX.utils.sheet_to_json(sheet, { header: 1, defval: '' });

console.log('=== TAB 4: B. Feasibility Simulation - FULL CONTENTS ===');
console.log(`Total rows: ${data.length}`);
console.log('');

// Print all rows with their content
data.forEach((row, index) => {
    // Filter out empty cells for cleaner output
    const nonEmpty = row.filter(cell => cell !== '');
    if (nonEmpty.length > 0) {
        console.log(`Row ${index + 1}: ${JSON.stringify(row.slice(0, 17))}`);
    }
});
