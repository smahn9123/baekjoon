import sys
from collections import deque

n, m = map(int, next(sys.stdin).split())
graph = {i: [] for i in range(1, n + 1)}
for employee, boss in enumerate(map(int, next(sys.stdin).split()[1:]), start=2):
    graph[boss].append(employee)

compliments = [0] * (n + 1)

for _ in range(m):
    employee, compliment = map(int, next(sys.stdin).split())
    compliments[employee] += compliment

stack = deque([1])
while stack:
    boss = stack.pop()  # popleft() 사용시 BFS
    for employee in graph[boss]:
        compliments[employee] += compliments[boss]
        stack.append(employee)

print(*compliments[1:])
