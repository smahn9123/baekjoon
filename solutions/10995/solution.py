n = int(input())
s = ""
i = 0
for i in range(n):
    if i % 2 == 1:
        s += " "
    for j in range(n * 2 - 1):
        s += "*" if j % 2 == 0 else " "
    s += "\n"

print(s)
