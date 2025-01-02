import sys

lines = [l.strip() for l in sys.stdin.readlines()]
a, b = map(int, lines[0].split(" "))
c = int(lines[1])
n = int(lines[2])
# n만이 아닌, n이상의 n0에 대해서 O(n) 정의를 만족하는지 확인하는 것이다.
# 그러려면 a <= c가 반드시 충족되어야 한다.
if a <= c and a * n + b <= c * n:
    sys.stdout.write("1")
else:
    sys.stdout.write("0")
