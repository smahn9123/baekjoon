n = int(input())

recursive_cnt = {1: 1, 2: 1}


def fr(n):
    if n in recursive_cnt:
        return recursive_cnt[n]
    cnt = fr(n - 1) + fr(n - 2)
    recursive_cnt[n] = cnt
    return cnt


def fd(n):
    if n <= 2:
        return 1
    return n - 2


print(fr(n), fd(n))
