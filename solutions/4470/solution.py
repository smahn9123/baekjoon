import sys

sys.stdout.write(
    "".join(f"{i}. {l}" for i, l in enumerate(sys.stdin.readlines()[1:], 1))
)
