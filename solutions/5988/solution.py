import sys

sys.stdout.write(
    "\n".join("even" if int(i) % 2 == 0 else "odd" for i in sys.stdin.readlines()[1:])
)
