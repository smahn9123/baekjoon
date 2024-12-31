n, b = input().split()
b = int(b)


def get_value(c):
    if "A" <= c <= "Z":
        return ord(c) - ord("A") + 10
    return ord(c) - ord("0")


print(sum((b**i) * get_value(c) for i, c in enumerate(n[::-1])))
