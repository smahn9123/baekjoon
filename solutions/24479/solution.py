from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for k in graph:
    graph[k].sort()


def dfs(node, order):
    visited[node] = order
    order += 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            order = dfs(neighbor, order)
    return order


dfs(r, 1)
sys.stdout.write("\n".join(map(str, visited[1:])))
