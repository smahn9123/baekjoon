n = int(input())
for i in range(1, n + 1):
    print(f"Case #{i}: {' '.join(input().split()[::-1])}")
