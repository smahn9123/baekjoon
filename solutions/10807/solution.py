import sys

next(sys.stdin)
s = next(sys.stdin).split()
v = next(sys.stdin).rstrip("\n")
sys.stdout.write(f"{s.count(v)}")
