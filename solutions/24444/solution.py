from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for k in graph:
    graph[k].sort()

visited = [0] * (n + 1)


def bfs(node):
    order = 1
    visited[node] = order
    queue = deque([node])

    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v] == 0:
                order += 1
                visited[v] = order
                queue.append(v)


bfs(r)
sys.stdout.write("\n".join(map(str, visited[1:])))
