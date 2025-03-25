import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    n = int(input())
    while stack and stack[-1] <= n:
        stack.pop()
    stack.append(n)

print(len(stack))
