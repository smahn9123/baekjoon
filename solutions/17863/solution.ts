import { readFileSync } from "fs";

const input = readFileSync("/dev/stdin").toString();
console.log(input.startsWith("555") ? "YES" : "NO");
