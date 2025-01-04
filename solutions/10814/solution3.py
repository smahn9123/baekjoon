import sys

sys.stdout.write(
    "".join(sorted(sys.stdin.readlines()[1:], key=lambda x: (int(x.split()[0]))))
)
