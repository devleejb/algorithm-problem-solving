# https://www.acmicpc.net/problem/7569
from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque([])

for i in range(N):
    for j in range(M):
        for k in range(H):
            if box[k][i][j] == 1:
                visited[k][i][j] = True
                q.append([(j, i, k), 0])

res = 0

while q:
    p, dis = q.popleft()

    x, y, z = p
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if (
            0 <= nx
            and nx < M
            and 0 <= ny
            and ny < N
            and 0 <= nz
            and nz < H
            and box[nz][ny][nx] == 0
            and not visited[nz][ny][nx]
        ):
            visited[nz][ny][nx] = True
            q.append([(nx, ny, nz), dis + 1])
            res = max(res, dis + 1)

is_finished = True

for i in range(N):
    for j in range(M):
        for k in range(H):
            if box[k][i][j] == 0 and not visited[k][i][j]:
                is_finished = False

if not is_finished:
    print(-1)
else:
    print(res)
