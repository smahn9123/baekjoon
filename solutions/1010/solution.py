from math import comb
from sys import stdin, stdout

stdout.write(
    "\n".join(str(comb(*map(int, l.split()[::-1]))) for l in stdin.readlines()[1:])
)
