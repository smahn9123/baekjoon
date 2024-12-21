# Solution 1
# import sys
#
# l = map(int, sys.stdin.readlines())
# for i, v in enumerate(l, start=1):
#     if i == 1:
#         max_v = v
#         max_i = i
#     else:
#         max_v = max(max_v, v)
#         max_i = i if max_v == v else max_i
# sys.stdout.write(f"{max_v}\n{max_i}")

# Solution 2
import sys

l = list(map(int, sys.stdin.readlines()))
sys.stdout.write(f"{max(l)} {l.index(max(l)) + 1}")

# Solution 3
# import sys
#
# (*l,) = map(int, sys.stdin.readlines())
# sys.stdout.write(f"{max(l)} {l.index(max(l)) + 1}")
