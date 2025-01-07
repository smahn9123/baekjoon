import sys

next(sys.stdin)
pool = set()
for log in sys.stdin:
    name, action = log.rstrip().split()
    if action == "enter":
        pool.add(name)
    else:
        pool.remove(name)
sys.stdout.write("\n".join(sorted(pool, reverse=True)))
