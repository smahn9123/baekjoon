s = input()
non_rotate = ("I", "O", "S", "H", "Z", "X", "N")
result = "YES"
for c in s:
    if c not in non_rotate:
        result = "NO"
        break
print(result)
