import sys

n, _m = map(int, sys.stdin.readline().split())
l = list(range(1, n + 1))
for s in sys.stdin:
    i, j = map(int, s.split())
    l[i - 1 : j] = l[i - 1 : j][::-1]
print(*l)
