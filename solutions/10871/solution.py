import sys

_, x = map(int, next(sys.stdin).split())
a = next(sys.stdin).split()
s = filter(lambda i: int(i) < x, a)
sys.stdout.write(" ".join(s))
