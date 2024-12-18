import sys

s = map(int, sys.stdin.readline().split())
r = iter((1, 1, 2, 2, 2, 8))
for _ in range(6):
    print(next(r) - next(s), end=" ")
