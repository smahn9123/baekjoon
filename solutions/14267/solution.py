import sys

sys.setrecursionlimit(10**6)

n, m = map(int, next(sys.stdin).split())
graph = {i: [] for i in range(1, n + 1)}
for employee, boss in enumerate(map(int, next(sys.stdin).split()[1:]), start=2):
    graph[boss].append(employee)

compliments = [0] * (n + 1)

for _ in range(m):
    employee, compliment = map(int, next(sys.stdin).split())
    compliments[employee] += compliment


def dfs(boss):
    for employee in graph[boss]:
        compliments[employee] += compliments[boss]
        dfs(employee)


dfs(1)
print(*compliments[1:])
