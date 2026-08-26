const fs = require('fs');

const data = fs.readFileSync('access.log', 'utf8');

const lines = data.split('\n');

let count200 = 0;
let count500 = 0;

for (const line of lines) { 
    if (line.includes('200')) {
        count200++;
    }   
    else if (line.includes('500')) {
        count500++;
    }
}

const summary = {
    total_lines_processed: lines.length,
    status_200: count200,
    status_500: count500,
    generated_at: new Date().toISOString()
}

fs.writeFileSync('summary.json', JSON.stringify(summary,null,2));

console.log(`Number of 200 responses: ${count200}`);
console.log(`Number of 500 responses: ${count500}`);

