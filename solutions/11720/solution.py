import sys

next(sys.stdin)
s = list(next(sys.stdin))[:-1]
print(sum(int(i) for i in s))
