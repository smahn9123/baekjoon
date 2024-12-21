s = input()
result = []
for c in "abcdefghijklmnopqrstuvwxyz":
    result.append(s.find(c))
print(*result)
