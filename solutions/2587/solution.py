import sys

l = sorted(tuple(int(line) for line in sys.stdin.readlines()))
print(f"{sum(l) // len(l)}\n{l[2]}")
