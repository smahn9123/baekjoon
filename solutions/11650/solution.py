import sys

lines = (tuple(map(int, line.rstrip().split())) for line in sys.stdin.readlines()[1:])
print("\n".join(f"{x} {y}" for x, y in sorted(lines, key=lambda i: (i[0], i[1]))))
