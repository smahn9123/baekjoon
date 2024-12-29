import sys

numbers = list(map(int, sys.stdin.read().split()))
m = max(numbers)
i = numbers.index(m)
sys.stdout.write(f"{m}\n{i // 9 + 1} {i % 9 + 1}")
