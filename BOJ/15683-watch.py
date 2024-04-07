from sys import stdin, maxsize
from copy import deepcopy

input = stdin.readline

EMPTY = 0
WALL = 6
WATCH = "#"
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

#   3
#  2 0
#   1
skips = [
    # Type 1
    [
        [1, 2, 3],
        [0, 2, 3],
        [0, 1, 3],
        [0, 1, 2],
    ],
    # Type 2
    [
        [0, 2],
        [1, 3],
    ],
    # Type 3
    [
        [1, 2],
        [2, 3],
        [0, 3],
        [0, 1],
    ],
    # Type 4
    [
        [0],
        [1],
        [2],
        [3],
    ],
    # Type 5
    [[]],
]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
cctv = []

for row in range(N):
    for col in range(M):
        if 0 < maps[row][col] < WALL:
            cctv.append((row, col, maps[row][col]))

res = maxsize


def search(cctv_idx, local_maps):
    global res
    if cctv_idx == len(cctv):
        cnt = 0
        for row in range(N):
            for col in range(M):
                if local_maps[row][col] == EMPTY:
                    cnt += 1
        res = min(res, cnt)
        return

    row, col, type = cctv[cctv_idx]

    for skip in skips[type - 1]:
        new_local_maps = deepcopy(local_maps)
        for dir in range(4):
            if dir in skip:
                continue
            i = 1
            while True:
                next_row = row + dr[dir] * i
                next_col = col + dc[dir] * i

                if not (0 <= next_row < N and 0 <= next_col < M):
                    break

                if new_local_maps[next_row][next_col] == WALL:
                    break

                if new_local_maps[next_row][next_col] == EMPTY:
                    new_local_maps[next_row][next_col] = WATCH

                i += 1
        search(cctv_idx + 1, new_local_maps)


search(0, maps)

print(res)
