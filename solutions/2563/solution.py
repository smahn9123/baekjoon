import sys

l = [[0 for _ in range(100)] for _ in range(100)]

next(sys.stdin)
for line in sys.stdin:
    x, y = map(int, line.split())
    for j in range(x, x + 10):
        for i in range(y, y + 10):
            l[i][j] = 1

sys.stdout.write(f"{(sum(sum(l, [])))}")
