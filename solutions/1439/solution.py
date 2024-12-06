s = input()

i = 0
zeros, ones = 0, 0

while i < len(s):
    if s[i] == "0":
        zeros += 1
    else:
        ones += 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        i += 1
    i += 1


print(min(zeros, ones))
