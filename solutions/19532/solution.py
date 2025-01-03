a, b, c, d, e, f = map(int, input().split())
x = (b * f - c * e) / (b * d - a * e)
y = (c * d - a * f) / (b * d - a * e)
print(int(x), int(y))
