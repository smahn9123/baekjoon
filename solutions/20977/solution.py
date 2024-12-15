import sys

_, s = sys.stdin.read().splitlines()


def f(x):
    if x == "J":
        return 2
    elif x == "O":
        return 1
    else:
        return 0


sys.stdout.write("".join(sorted(s, key=f, reverse=True)))
