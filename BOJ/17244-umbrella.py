from sys import stdin, maxsize, setrecursionlimit
from collections import deque

setrecursionlimit(10**5)


input = stdin.readline

N, M = map(int, input().split())
maps = [list(input()) for _ in range(M)]
stocks = {}
start = (0, 0)
visited = {}
res = maxsize

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(M):
    for j in range(N):
        if maps[i][j] == "X":
            stocks[(i, j)] = len(stocks)
        elif maps[i][j] == "S":
            start = (i, j)

ALL_VISITED = (2 ** len(stocks)) - 1

q = deque([])
q.append((start[0], start[1], 0, 0))

while q:
    row, col, cost, mask = q.popleft()

    if (row, col, mask) in visited:
        continue

    visited[(row, col, mask)] = cost

    if maps[row][col] == "E" and mask == ALL_VISITED:
        res = cost
        break

    next_cost = cost + 1
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if not (0 <= next_row < M and 0 <= next_col < N):
            continue

        if maps[next_row][next_col] == "#":
            continue

        next_mask = mask

        if maps[next_row][next_col] == "X":
            stock_num = stocks[(next_row, next_col)]
            next_mask = mask | (1 << stock_num)

        if (next_row, next_col, next_mask) not in visited or (
            visited[(next_row, next_col, next_mask)] > next_cost
        ):
            q.append((next_row, next_col, next_cost, next_mask))

print(res)
