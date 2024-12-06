s = input()
a = ""
for i, c in enumerate(s):
    a += c
    if i % 10 == 9:
        a += "\n"
print(a)
