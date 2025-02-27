from collections import deque

n = int(input())
line = deque(map(int, input().split()))
stack = deque()
order = 1
is_nice = True

while line or stack:
    if line and line[0] == order:
        line.popleft()
        order += 1
    elif stack and stack[-1] == order:
        stack.pop()
        order += 1
    elif line:
        stack.append(line.popleft())
    else:
        is_nice = False
        break

print("Nice" if is_nice else "Sad")
