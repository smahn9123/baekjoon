import sys

sys.stdout.write("\n".join(line.rstrip()[::-1] for line in sys.stdin.readlines()[1:]))
