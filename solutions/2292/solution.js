const n = Number(require('fs').readFileSync("/dev/stdin").toString().trim());
let sum = 1;
for (let i = 1; ; i++) {
    sum += 6 * (i - 1);
    if (sum >= n) {
        console.log(i);
        break;
    }
}