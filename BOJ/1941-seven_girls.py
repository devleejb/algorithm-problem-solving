from itertools import combinations
from collections import deque
from sys import stdin

input = stdin.readline

maps = [list(input()) for _ in range(5)]

combs = list(combinations(range(25), 7))

res = 0

NOT_VISITED = 1
VISITED = 2

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for comb in combs:
    prev_row, prev_col = comb[0] // 5, comb[0] % 5
    S_cnt = 0
    new_maps = [[0] * 5 for _ in range(5)]
    start_point = (0, 0)

    for i in range(7):
        row = comb[i] // 5
        col = comb[i] % 5
        start_point = (row, col)
        new_maps[row][col] = NOT_VISITED
        if maps[row][col] == "S":
            S_cnt += 1

    if S_cnt < 4:
        continue

    q = deque([start_point])
    adjacent_cnt = 0

    while q:
        row, col = q.popleft()

        if new_maps[row][col] == VISITED:
            continue

        new_maps[row][col] = VISITED
        adjacent_cnt += 1

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if not (0 <= next_row < 5 and 0 <= next_col < 5):
                continue

            if new_maps[next_row][next_col] != NOT_VISITED:
                continue

            q.append((next_row, next_col))

    if adjacent_cnt == 7:
        res += 1

print(res)
