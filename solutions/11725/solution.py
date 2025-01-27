import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
tree = defaultdict(list)

n = int(next(sys.stdin))
for line in sys.stdin:
    a, b = map(int, line.split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1)


def dfs(node):
    for child in tree[node]:
        if parent[child] == 0:
            parent[child] = node
            dfs(child)


dfs(1)
sys.stdout.write("\n".join(map(str, parent[2:])))
