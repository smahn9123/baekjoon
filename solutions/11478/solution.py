s = input()
s_len = len(s)
unique_strings = set()

for length in range(1, s_len + 1):
    for i in range(s_len):
        if i + length > s_len:
            break
        unique_strings.add(s[i : i + length])

print(len(unique_strings))
