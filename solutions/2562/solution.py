import sys

l = map(int, sys.stdin.readlines())
for i, v in enumerate(l, start=1):
    if i == 1:
        max_v = v
        max_i = i
    else:
        max_v = max(max_v, v)
        max_i = i if max_v == v else max_i
sys.stdout.write(f"{max_v}\n{max_i}")
