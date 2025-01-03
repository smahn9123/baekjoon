# Very Naive Code
# Solve https://www.acmicpc.net/problem/27441 for faster optimization!

n = int(input())
i = 666
order = 0
while True:
    if "666" in str(i):
        order += 1
        if order == n:
            break
    i += 1
print(i)
