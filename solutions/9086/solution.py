import sys

next(sys.stdin)
for s in sys.stdin:
    sys.stdout.write(f"{s[0]}{s.rstrip('\n')[-1]}\n")
