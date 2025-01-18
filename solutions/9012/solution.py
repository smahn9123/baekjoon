import sys


def is_vps(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                return "NO"
    if stack:
        return "NO"
    return "YES"


next(sys.stdin)
sys.stdout.write("\n".join(is_vps(s.rstrip()) for s in sys.stdin))
