import sys

l = sorted(int(line) for line in sys.stdin.readlines()[1:])
print("\n".join(map(str, l)))
