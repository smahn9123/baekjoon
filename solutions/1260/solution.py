import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
for g in graph:
    g.sort()


def dfs(node, result, visited):
    result.append(node)
    visited[node] = 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor, result, visited)


def bfs(node, result):
    visited = [0 for _ in range(n + 1)]
    visited[node] = 1
    q = deque([node])
    while q:
        next_node = q.popleft()
        result.append(next_node)
        for neighbor in graph[next_node]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                q.append(neighbor)


dfs_result = []
dfs(v, dfs_result, [0 for _ in range(n + 1)])
bfs_result = []
bfs(v, bfs_result)
sys.stdout.write(" ".join(map(str, dfs_result)) + "\n" + " ".join(map(str, bfs_result)))
