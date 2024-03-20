from sys import stdin
from collections import deque

input = stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

q = deque([])

for row in range(N):
    for col in range(M):
        if maps[row][col] > 0:
            q.append(
                (
                    row,
                    col,
                )
            )

time = 0
res = 0

while True:
    new_height_list = []
    time += 1

    for _ in range(len(q)):
        row, col = q.popleft()
        empty_cnt = 0

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if not (0 <= next_row < N and 0 <= next_col < M):
                continue

            if maps[next_row][next_col] == 0:
                empty_cnt += 1

        next_height = max(0, maps[row][col] - empty_cnt)
        new_height_list.append((row, col, next_height))

    for row, col, next_height in new_height_list:
        maps[row][col] = next_height

        if next_height > 0:
            q.append((row, col))

    if not q:
        break

    visited = [[False] * M for _ in range(N)]
    bfs_q = deque([(q[0][0], q[0][1])])

    while bfs_q:
        row, col = bfs_q.popleft()

        if visited[row][col]:
            continue

        visited[row][col] = True

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if not (0 <= next_row < N and 0 <= next_col < M):
                continue

            if maps[next_row][next_col] > 0 and not visited[next_row][next_col]:
                bfs_q.append((next_row, next_col))

    for row in range(N):
        for col in range(M):
            if maps[row][col] > 0 and not visited[row][col]:
                res = time
                break

    if res > 0:
        break

print(res)
