n = int(input())
b5 = n // 5
while b5 > 0 and (n - b5 * 5) % 3 > 0:
    b5 -= 1
n -= b5 * 5
b3 = n // 3
n -= b3 * 3
print(-1 if n > 0 else b5 + b3)
