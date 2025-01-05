import sys

x = tuple(map(int, sys.stdin.readlines()[1].rstrip().split()))
unique_ordered = sorted(set(x))
index_map = {v: i for i, v in enumerate(unique_ordered)}
sys.stdout.write(" ".join(str(index_map[i]) for i in x))
