import sys

lines = sys.stdin.read().splitlines()[:-1]

ans = []
for line in lines:
    sum = 0
    for i, c in enumerate(line, 1):
        if c != " ":
            sum += i * (ord(c) - ord("A") + 1)
    ans.append(str(sum))

sys.stdout.write("\n".join(ans))
