s = input()
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
count = 0
while i < len(s):
    if s[i : i + 3] in croatian:
        i += 3
    elif s[i : i + 2] in croatian:
        i += 2
    else:
        i += 1
    count += 1
print(count)
