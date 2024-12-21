const input = require('fs').readFileSync("/dev/stdin").toString().trim().split('\n');
const n = Number(input[0]);
const scores = Array.from(input[1].split(' '), Number);
let max = 0;
for (const score of scores)
    if (score > max) max = score;
let newScores = scores.map(x => x / max * 100);
console.log(newScores.reduce((a, b) => a + b) / n);
