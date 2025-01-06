import sys

n, m = map(int, next(sys.stdin).split())
words = sys.stdin.readlines()
s = set(words[:n])
print(sum(1 for w in words[n : n + m] if w in s))
