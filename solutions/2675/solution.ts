const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const T = parseInt(input[0]);

for (let i = 1; i <= T; i++) {
  const [R, S] = input[i].split(" ");
  let result = "";
  for (let char of S) {
    result += char.repeat(parseInt(R));
  }
  console.log(result);
}
