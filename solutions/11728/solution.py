import sys

next(sys.stdin)
print(*sorted(sys.stdin.read().split(), key=int))
