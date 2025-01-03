import sys

l = (int(i) for i in sys.stdin.readlines()[1:])
print("\n".join(map(str, sorted(l))))
