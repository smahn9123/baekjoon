from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, (input().rstrip()))) for _ in range(n)]


def bfs():
    maze_distance = [[n * m] * m for _ in range(n)]
    maze_distance[0][0] = 1
    q = deque([(0, 0)])
    while q:
        cur_i, cur_j = q.popleft()
        for move_i, move_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = cur_i + move_i, cur_j + move_j
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                continue
            if maze[next_i][next_j] == 0:
                continue
            if maze_distance[cur_i][cur_j] + 1 < maze_distance[next_i][next_j]:
                maze_distance[next_i][next_j] = maze_distance[cur_i][cur_j] + 1
                q.append((next_i, next_j))
    return maze_distance[n - 1][m - 1]


print(bfs())
