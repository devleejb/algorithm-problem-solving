from collections import deque

visited = []
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

# input
N = int(input())
r1, c1, r2, c2 = map(int, input().split())


def bfs():
    queue = deque()

    queue.append((r1, c1))
    visited[r1][c1] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]

            if (nr >= 0 and nc >= 0 and nr < N and nc < N and visited[nr][nc] == -1):
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))


for i in range(N):
    visited.append([-1] * N)

bfs()

print(visited[r2][c2])
