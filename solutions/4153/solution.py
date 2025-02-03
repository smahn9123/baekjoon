import sys


def print_if_right_triangle(sides):
    side_a, side_b, side_c = sorted(sides)
    if side_a**2 + side_b**2 == side_c**2:
        print("right")
    else:
        print("wrong")


for testcase in sys.stdin.readlines()[:-1]:
    print_if_right_triangle(map(int, testcase.split()))
