import sys


def is_balanced(s):
    p = "([)]"
    stack = []
    for c in s:
        if c in p[0:2]:
            stack.append(c)
        elif c in p[2:]:
            if not stack or (stack[-1] != p[p.index(c) - 2]):
                return False
            stack.pop()
    return not stack


sys.stdout.write(
    "\n".join(
        ("yes" if is_balanced(s) else "no") for s in sys.stdin if s.rstrip() != "."
    )
)
