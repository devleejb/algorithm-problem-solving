from sys import stdin
from collections import deque

input = stdin.readline

NOT_VISITED = 0
VISITED = 1
WAIT_KEY = 2

T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
res_list = []

for _ in range(T):
    h, w = map(int, input().split())
    maps = [list(input().rstrip()) for _ in range(h)]
    keys = list(input().rstrip())
    has_keys = [False] * 26
    visited = [[NOT_VISITED] * w for _ in range(h)]
    waiting_keys = [[] for _ in range(26)]

    if keys[0] != "0":
        for key in keys:
            has_keys[ord(key) - 97] = True

    q = deque([])

    for i in range(h):
        for j in range(w):
            if i != 0 and i != h - 1 and j != 0 and j != w - 1:
                continue

            if maps[i][j] != "*":
                q.append((i, j))

    res = 0

    while q:
        row, col = q.popleft()

        if visited[row][col] == VISITED:
            continue

        if maps[row][col] == "$":
            res += 1

        if "A" <= maps[row][col] <= "Z" and not has_keys[ord(maps[row][col]) - 65]:
            visited[row][col] = WAIT_KEY
            waiting_keys[ord(maps[row][col]) - 65].append((row, col))
            continue

        visited[row][col] = VISITED

        if "a" <= maps[row][col] <= "z":
            target = ord(maps[row][col]) - 97
            has_keys[target] = True

            for pos in waiting_keys[target]:
                q.append(pos)

            waiting_keys[target] = []

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if (
                0 <= next_row < h
                and 0 <= next_col < w
                and visited[next_row][next_col] == NOT_VISITED
                and maps[next_row][next_col] != "*"
            ):
                q.append((next_row, next_col))

    res_list.append(res)

for res in res_list:
    print(res)
