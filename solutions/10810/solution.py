import sys

n, _ = map(int, next(sys.stdin).split())
l = [0 for _ in range(n)]
for i, j, k in map(lambda x: map(int, x.split()), sys.stdin):
    for m in range(i - 1, j):
        l[m] = k
print(*l)
