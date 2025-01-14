import sys

group_a, group_b = set(), set()
n, m = map(int, next(sys.stdin).split())
for _ in range(n):
    group_a.add(next(sys.stdin))
for _ in range(m):
    group_b.add(next(sys.stdin))
group_ab = sorted(group_a & group_b)
sys.stdout.write(f"{len(group_ab)}\n" + "".join(group_ab))
