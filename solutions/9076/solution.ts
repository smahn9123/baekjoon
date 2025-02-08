import { readFileSync } from "fs";
const input = readFileSync("/dev/stdin").toString().split(/\r?\n/);
const t = Number(input[0]);
for (let i = 1; i <= t; i++) {
  const filteredScores = input[i]
    .split(" ")
    .map(Number)
    .sort((a: number, b: number) => a - b)
    .slice(1, 4);
  console.log(
    filteredScores[2] - filteredScores[0] >= 4
      ? "KIN"
      : filteredScores.reduce((a: number, b: number) => a + b, 0)
  );
}
