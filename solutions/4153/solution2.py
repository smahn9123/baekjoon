import sys

for line in sys.stdin:
    sides = list(map(int, line.split()))
    if sum(sides) > 0:
        side_a, side_b, side_c = sorted(sides)
        if side_a**2 + side_b**2 == side_c**2:
            print("right")
        else:
            print("wrong")
