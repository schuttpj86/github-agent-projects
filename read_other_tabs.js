const XLSX = require('xlsx');

const filepath = 'c:/AI-projects/Projects/github-agent-projects/projects/PROP-004-PeakGen/rfp/2. LT2029 Stability Technical Proforma V4.xlsx';
const workbook = XLSX.readFile(filepath);

// Read Tab 3 - "A Solution Outline"
console.log('=== TAB 3: A Solution Outline - FULL CONTENTS ===');
const sheetA = workbook.Sheets['A Solution Outline'];
const dataA = XLSX.utils.sheet_to_json(sheetA, { header: 1, defval: '' });
console.log(`Total rows: ${dataA.length}`);
console.log('');

dataA.forEach((row, index) => {
    const nonEmpty = row.filter(cell => cell !== '');
    if (nonEmpty.length > 0) {
        console.log(`Row ${index + 1}: ${JSON.stringify(row.slice(0, 12))}`);
    }
});

console.log('\n\n');

// Read Tab 5 - "C. DRC Data"
console.log('=== TAB 5: C. DRC Data - FULL CONTENTS ===');
const sheetC = workbook.Sheets['C. DRC Data'];
const dataC = XLSX.utils.sheet_to_json(sheetC, { header: 1, defval: '' });
console.log(`Total rows: ${dataC.length}`);
console.log('');

dataC.forEach((row, index) => {
    const nonEmpty = row.filter(cell => cell !== '');
    if (nonEmpty.length > 0) {
        console.log(`Row ${index + 1}: ${JSON.stringify(row.slice(0, 21))}`);
    }
});
