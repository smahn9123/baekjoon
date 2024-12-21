import sys

n, m = map(int, next(sys.stdin).split())
l = [i for i in range(1, n + 1)]
for s in sys.stdin:
    i, j = map(int, s.split())
    tmp = l[i - 1]
    l[i - 1] = l[j - 1]
    l[j - 1] = tmp

print(*l)
