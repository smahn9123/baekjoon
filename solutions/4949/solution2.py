import sys


def is_balanced(s):
    stack = []
    pairs = {")": "(", "]": "["}
    for c in s:
        if c in "([":
            stack.append(c)
        elif c in ")]":
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return not stack


sys.stdout.write(
    "\n".join(
        ("yes" if is_balanced(s) else "no") for s in sys.stdin if s.rstrip() != "."
    )
)
