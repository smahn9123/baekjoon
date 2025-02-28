from collections import deque

n = int(input())
line = deque(map(int, input().split()))
stack = []
order = 1

while line:
    if line[0] == order:
        line.popleft()
        order += 1
    else:
        stack.append(line.popleft())
    while stack and stack[-1] == order:
        stack.pop()
        order += 1

print("Nice" if not stack else "Sad")
