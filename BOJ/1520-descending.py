from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1 for _ in range(N)] for _ in range(M)]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def visit(row, col):
    if row == M - 1 and col == N - 1:
        visited[row][col] = max(0, visited[row][col]) + 1
        return visited[row][col]

    cnt = 0

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < M and 0 <= nc < N and board[row][col] > board[nr][nc]:
            res = 0
            if visited[nr][nc] > 0:
                res = visited[nr][nc]
            elif visited[nr][nc] == 0:
                res = 0
            else:
                res = visit(nr, nc)

            cnt += res

    visited[row][col] = cnt

    return cnt


visit(0, 0)
print(visited[0][0])
