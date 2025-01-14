import sys
from math import lcm

next(sys.stdin)
sys.stdout.write("\n".join(str((lcm(*map(int, l.split())))) for l in sys.stdin))
