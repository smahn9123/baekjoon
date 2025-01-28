from collections import deque

n = int(input())
pic = [list(map(int, list(input()))) for _ in range(n)]
danji_pic = [[0] * n for _ in range(n)]
danji_size = {}

move_i = [0, 0, -1, 1]
move_j = [1, -1, 0, 0]


def bfs(start_i, start_j, num):
    danji_pic[start_i][start_j] = num
    q = deque([(start_i, start_j)])
    size = 0
    while q:
        cur_i, cur_j = q.popleft()
        size += 1
        for p in range(4):
            next_i, next_j = cur_i + move_i[p], cur_j + move_j[p]
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            if pic[next_i][next_j] == 0:
                continue
            if danji_pic[next_i][next_j] != 0:
                continue
            danji_pic[next_i][next_j] = num
            q.append((next_i, next_j))
    return size


num = 1
for i in range(n):
    for j in range(n):
        if pic[i][j] == 1 and danji_pic[i][j] == 0:
            size = bfs(i, j, num)
            danji_size[num] = size
            num += 1

print(num - 1)
print("\n".join(map(str, sorted(danji_size.values()))))
