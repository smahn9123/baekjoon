const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const S: string = input[0];
const i: number = parseInt(input[1]);
console.log(S[i - 1]);
