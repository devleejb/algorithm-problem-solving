from sys import stdin
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]


def bfs(row, col, fill, visited):
    q = deque([(row, col)])
    visited[row][col] = True

    while q:
        row, col = q.popleft()

        maps[row][col] = fill

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if (
                0 <= next_row < N
                and 0 <= next_col < N
                and maps[next_row][next_col] == 1
                and not visited[next_row][next_col]
            ):
                visited[next_row][next_col] = True
                q.append((next_row, next_col))


input = stdin.readline

visited = [[False] * N for _ in range(N)]
fill = 1

for i in range(N):
    for j in range(N):
        if visited[i][j] or maps[i][j] == 0:
            continue

        bfs(i, j, fill, visited)

        fill = fill + 1

q = deque([])
visited = set()

for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            q.append((i, j, maps[i][j], 0))
            visited.add((maps[i][j], i, j))

end = False
res = -1

while not end and q:
    row, col, fill, cost = q.popleft()
    next_cost = cost + 1

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if not (0 <= next_row < N and 0 <= next_col < N):
            continue

        if (fill, next_row, next_col) in visited:
            continue

        if maps[next_row][next_col] == 0:
            visited.add((fill, next_row, next_col))
            q.append((next_row, next_col, fill, next_cost))
        elif maps[next_row][next_col] != fill:
            res = cost
            end = True
            break

print(res)
