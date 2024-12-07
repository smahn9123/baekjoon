n = int(input())
i, j = 0, 1
while n > 0:
    s = i + j
    i = j
    j = s
    n -= 1
print(i)
