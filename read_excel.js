const XLSX = require('xlsx');

const filepath = 'c:/AI-projects/Projects/github-agent-projects/projects/PROP-004-PeakGen/rfp/2. LT2029 Stability Technical Proforma V4.xlsx';
const workbook = XLSX.readFile(filepath);

console.log('=== WORKBOOK STRUCTURE ===');
console.log('Sheet names:', workbook.SheetNames);
console.log('');

// Show all sheets
workbook.SheetNames.forEach((sheetName, index) => {
    const sheet = workbook.Sheets[sheetName];
    const range = XLSX.utils.decode_range(sheet['!ref'] || 'A1');
    console.log(`Sheet ${index + 1}: "${sheetName}"`);
    console.log(`  Range: ${sheet['!ref']}`);
    console.log(`  Rows: ${range.e.r - range.s.r + 1}, Columns: ${range.e.c - range.s.c + 1}`);
    console.log('');
});

// Find Tab 4 - it could be named differently
const tab4Names = workbook.SheetNames.filter(name =>
    name.includes('4') || name.toLowerCase().includes('tab 4') || name.toLowerCase().includes('sheet4')
);
console.log('Sheets that might be Tab 4:', tab4Names);
console.log('');

// Let's show the content of each sheet to identify Tab 4
console.log('=== SHEET CONTENTS (First 5 rows each) ===');
workbook.SheetNames.forEach((sheetName, index) => {
    console.log(`\n--- Sheet ${index + 1}: "${sheetName}" ---`);
    const sheet = workbook.Sheets[sheetName];
    const data = XLSX.utils.sheet_to_json(sheet, { header: 1, defval: '' });
    data.slice(0, 5).forEach((row, rowIndex) => {
        console.log(`Row ${rowIndex + 1}:`, JSON.stringify(row.slice(0, 10)));
    });
});
