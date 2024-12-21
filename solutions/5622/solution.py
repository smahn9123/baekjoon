from functools import reduce


def lut(c):
    groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    for i, g in enumerate(groups):
        if c in g:
            return i + 3


print(reduce(lambda x, y: x + lut(y), input(), 0))
