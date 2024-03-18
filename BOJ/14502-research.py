from sys import stdin
from itertools import combinations

input = stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
empty_cells = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty_cells.append((i, j))


combs = combinations(empty_cells, 3)


def dfs(row, col, visited):
    visited[row][col] = True

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if (
            not (0 <= next_row < N and 0 <= next_col < M)
            or maps[next_row][next_col] != 0
            or visited[next_row][next_col]
        ):
            continue

        dfs(next_row, next_col, visited)


res = 0

for comb in combs:
    visited = [[False] * M for _ in range(N)]
    for row, col in comb:
        visited[row][col] = True

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2 and not visited[i][j]:
                dfs(i, j, visited)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0 and not visited[i][j]:
                cnt += 1

    res = max(res, cnt)

print(res)
