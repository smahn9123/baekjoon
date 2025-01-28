from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    days = [[-1] * m for _ in range(n)]
    empty = 0
    init_ripe = 0
    days_max = 0

    q = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == -1:
                empty += 1
            elif box[i][j] == 1:
                init_ripe += 1
                days[i][j] = 0
                q.append((i, j))

    if empty + init_ripe == n * m:
        return 0

    ripe = 0
    while q:
        cur_i, cur_j = q.popleft()
        ripe += 1
        days_max = max(days_max, days[cur_i][cur_j])
        for move_i, move_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = cur_i + move_i, cur_j + move_j
            if 0 <= next_i < n and 0 <= next_j < m and box[next_i][next_j] == 0:
                days[next_i][next_j] = days[cur_i][cur_j] + 1
                box[next_i][next_j] = 1
                q.append((next_i, next_j))

    if empty + ripe < n * m:
        return -1

    return days_max


print(bfs())
