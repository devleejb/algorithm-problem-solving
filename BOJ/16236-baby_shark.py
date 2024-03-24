from sys import stdin
import heapq

input = stdin.readline

SHARK = 9
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
cur_pos = [0, 0]

for row in range(N):
    for col in range(N):
        if maps[row][col] == SHARK:
            cur_pos = [row, col]
            maps[row][col] = 0

size = 2
eat_cnt = 0
answer = 0

hq = [(0, cur_pos[0], cur_pos[1])]
visited = [[False] * N for _ in range(N)]

while hq:
    cost, row, col = heapq.heappop(hq)

    if visited[row][col]:
        continue

    if 0 < maps[row][col] < size:
        maps[row][col] = 0
        eat_cnt += 1
        visited = [[False] * N for _ in range(N)]

        if eat_cnt == size:
            size += 1
            eat_cnt = 0

        answer = cost

        hq = [(cost, row, col)]

        continue

    visited[row][col] = True
    next_cost = cost + 1

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if not (0 <= next_row < N and 0 <= next_col < N):
            continue

        if size < maps[next_row][next_col]:
            continue

        if not visited[next_row][next_col]:
            heapq.heappush(hq, (next_cost, next_row, next_col))

print(answer)
