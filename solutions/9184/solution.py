import sys


def w(a, b, c, dic={}):
    if (a, b, c) in dic:
        return dic[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        dic[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dic[(a, b, c)] = w(20, 20, 20, dic)
    elif a < b < c:
        dic[(a, b, c)] = (
            w(a, b, c - 1, dic) + w(a, b - 1, c - 1, dic) - w(a, b - 1, c, dic)
        )
    else:
        dic[(a, b, c)] = (
            w(a - 1, b, c, dic)
            + w(a - 1, b - 1, c, dic)
            + w(a - 1, b, c - 1, dic)
            - w(a - 1, b - 1, c - 1, dic)
        )
    return dic[(a, b, c)]


memo = {}
for l in sys.stdin:
    a, b, c = map(int, l.split())
    if a != -1 or b != -1 or c != -1:
        sys.stdout.write(f"w({a}, {b}, {c}) = {w(a, b, c, memo)}\n")
