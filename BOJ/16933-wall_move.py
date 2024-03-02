from sys import stdin, maxsize
from collections import deque

input = stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M, K = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]


def bfs():
    q = deque([])
    visited = [[K + 1] * M for _ in range(N)]

    # (row, col, cost, time_type, broken_wall_cnt)
    q.append((0, 0, 0))

    time_type = 0
    cost = 1

    while q:
        for _ in range(len(q)):
            row, col, broken_wall_cnt = q.popleft()

            if row == N - 1 and col == M - 1:
                print(cost)
                return

            for i in range(4):
                next_row = row + dr[i]
                next_col = col + dc[i]

                if (
                    0 <= next_row < N
                    and 0 <= next_col < M
                    and visited[next_row][next_col] > broken_wall_cnt
                ):
                    if graph[next_row][next_col] == "1" and broken_wall_cnt < K:
                        if time_type == 1:
                            q.append((row, col, broken_wall_cnt))
                        else:
                            visited[next_row][next_col] = broken_wall_cnt + 1
                            q.append((next_row, next_col, broken_wall_cnt + 1))
                    elif graph[next_row][next_col] == "0":
                        visited[next_row][next_col] = broken_wall_cnt
                        q.append((next_row, next_col, broken_wall_cnt))
        cost += 1
        time_type = int(not time_type)

    print(-1)


bfs()
