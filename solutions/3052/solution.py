import sys

l = map(int, sys.stdin.readlines())
s = {i % 42 for i in l}
print(len(s))
