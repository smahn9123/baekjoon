import sys

commands = [s.rstrip("\n") for s in sys.stdin.readlines()][1:]
stack = []
result = []
for command in commands:
    if command[0] == "1":
        stack.append(command[2:])
    elif command[0] == "2":
        result.append(stack.pop() if stack else "-1")
    elif command[0] == "3":
        result.append(str(len(stack)))
    elif command[0] == "4":
        result.append("0" if stack else "1")
    elif command[0] == "5":
        result.append(stack[-1] if stack else "-1")

sys.stdout.write("\n".join(result))
