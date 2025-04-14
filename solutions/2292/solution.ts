import * as fs from "fs";

const input: string = fs.readFileSync("/dev/stdin", "utf8").toString().trim();
const n: number = Number(input);

let sum: number = 1;
for (let i: number = 1; ; i++) {
  sum += 6 * (i - 1);
  if (sum >= n) {
    console.log(i);
    break;
  }
}
