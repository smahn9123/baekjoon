import sys

n = int(next(sys.stdin))
l = [0] * 10_001
for i in sys.stdin:
    l[int(i)] += 1

BUFFER_SIZE = 1_000
for i in range(1, 10_001):
    for _ in range(l[i] // BUFFER_SIZE):
        sys.stdout.write(f"{i}\n" * BUFFER_SIZE)
    for _ in range(l[i] % BUFFER_SIZE):
        sys.stdout.write(f"{i}\n")
