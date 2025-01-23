from collections import deque
import sys

queue = deque()
results = []
commands = sys.stdin.readlines()[1:]

for command in commands:
    cmd_x = command.split()
    cmd = cmd_x[0]
    if cmd == "push":
        queue.append(cmd_x[1])
    elif cmd == "pop":
        results.append(queue.popleft() if queue else "-1")
    elif cmd == "size":
        results.append(str(len(queue)))
    elif cmd == "empty":
        results.append("0" if queue else "1")
    elif cmd == "front":
        results.append(queue[0] if queue else "-1")
    elif cmd == "back":
        results.append(queue[-1] if queue else "-1")

sys.stdout.write("\n".join(results))
