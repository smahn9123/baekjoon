n = int(input())
for i in range(1, n + 1):
    print(f"{'*' * (2 * i - 1):^{2 * n - 1}}".rstrip())
for i in range(n - 1, 0, -1):
    print(f"{'*' * (2 * i - 1):^{2 * n - 1}}".rstrip())
