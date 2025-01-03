a = {0: (1, 0), 1: (0, 1)}


def solve(n):
    if n in a:
        return a[n]
    v = (solve(n - 2)[0] + solve(n - 1)[0], solve(n - 2)[1] + solve(n - 1)[1])
    a[n] = v
    return v


t = int(input())
while t > 0:
    n = int(input())
    z, o = solve(n)
    print(z, o)
    t -= 1
