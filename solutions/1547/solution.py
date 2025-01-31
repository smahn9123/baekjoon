import sys

cups = ["0", "1", "2", "3"]
n = int(next(sys.stdin))
for _ in range(n):
    x, y = next(sys.stdin).split()
    x_pos, y_pos = cups.index(x), cups.index(y)
    cups[x_pos], cups[y_pos] = y, x
sys.stdout.write(cups[1])
