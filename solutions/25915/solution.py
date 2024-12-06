def get_distance(x, y):
    return abs(ord(x) - ord(y))


s = input("").upper()
d = get_distance(s, "I")
p = "ILOVEYONSEI"
for i, c in enumerate(p[:-1]):
    d += get_distance(p[i], p[i + 1])
print(d)
