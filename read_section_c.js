const XLSX = require('xlsx');
const workbook = XLSX.readFile('projects/PROP-004-PeakGen/rfp/2. LT2029 Stability Technical Proforma V4.xlsx');

console.log('=== SECTION C: DRC DATA ===\n');
const sheetC = workbook.Sheets['C. DRC Data'];
const dataC = XLSX.utils.sheet_to_json(sheetC, {header: 1, defval: ''});
dataC.forEach((row, i) => {
  const filtered = row.map(c => String(c || '').trim()).filter(c => c !== '');
  if (filtered.length > 0) {
    console.log('Row ' + (i+1) + ': ' + filtered.join(' | '));
  }
});
