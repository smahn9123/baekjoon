from collections import deque

n, k = map(int, input().split())
q = deque([str(i) for i in range(1, n + 1)])
sol = []
while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    sol.append(q.popleft())
print(f"<{', '.join(sol)}>")
