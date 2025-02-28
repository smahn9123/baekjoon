import heapq
import sys

input = sys.stdin.readline

pq = []
result = []

for _ in range(int(input())):
    x = input().rstrip()
    if x == "0":
        result.append(heapq.heappop(pq)[1] if pq else x)
    else:
        heapq.heappush(pq, (int(x), x))

sys.stdout.write("\n".join(result))
