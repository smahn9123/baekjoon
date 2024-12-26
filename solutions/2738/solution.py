import sys

n, m = map(int, next(sys.stdin).split())
a = [map(int, next(sys.stdin).split()) for _ in range(n)]
b = [map(int, next(sys.stdin).split()) for _ in range(n)]

final = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(f"{next(a[i]) + next(b[i])}")
    final.append(" ".join(row))
sys.stdout.write("\n".join(final))
