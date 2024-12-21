import sys

next(sys.stdin)
for t in sys.stdin:
    r = int(t[0])
    s = t[2:-1]
    l = []
    for c in s:
        l.append(c * r)
    sys.stdout.write("".join(l) + "\n")
