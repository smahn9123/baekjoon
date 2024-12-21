import sys

l = [i for i in range(1, 31)]
[l.remove(int(next(sys.stdin))) for _ in range(28)]
print(min(l), max(l), sep="\n")
