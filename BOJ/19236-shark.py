from sys import stdin
from copy import deepcopy

input = stdin.readline
SHARK = -1
EMPTY = 0
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
maps = [list(map(int, input().split())) for _ in range(4)]
res = maps[0][0]

for i in range(4):
    for j in range(1, 8, 2):
        maps[i][j] -= 1

maps[0][0] = SHARK


def move_fish(cur_maps):
    pos = [(-1, -1) for _ in range(17)]
    # calculate positions
    for i in range(4):
        for j in range(4):
            if cur_maps[i][j * 2] != SHARK and cur_maps[i][j * 2] != EMPTY:
                pos[cur_maps[i][j * 2]] = (i, j * 2)

    for i in range(1, 17):
        row, col = pos[i]
        dir = cur_maps[row][col + 1]

        if row == -1 and col == -1:
            continue

        for dir_increase in range(8):
            next_dir = (dir + dir_increase) % 8
            next_row = row + dr[next_dir]
            next_col = col + dc[next_dir] * 2

            if not (0 <= next_row < 4 and 0 <= next_col < 8):
                continue

            if cur_maps[next_row][next_col] == SHARK:
                continue

            cur_maps[row][col], cur_maps[next_row][next_col] = (
                cur_maps[next_row][next_col],
                cur_maps[row][col],
            )
            cur_maps[row][col + 1], cur_maps[next_row][next_col + 1] = (
                cur_maps[next_row][next_col + 1],
                next_dir,
            )

            pos[cur_maps[row][col]] = (row, col)
            pos[cur_maps[next_row][next_col]] = (next_row, next_col)
            break

    return cur_maps


def dfs(cur_maps, score):
    global res

    res = max(res, score)
    new_map = move_fish(deepcopy(cur_maps))
    shark_pos = (-1, -1)

    for i in range(4):
        for j in range(4):
            if new_map[i][j * 2] == SHARK:
                shark_pos = (i, j * 2)

    row, col = shark_pos

    dir = new_map[row][col + 1]

    for i in range(1, 5):
        next_row = row + dr[dir] * i
        next_col = col + dc[dir] * 2 * i

        if not (0 <= next_row < 4 and 0 <= next_col < 8):
            break

        if new_map[next_row][next_col] == EMPTY:
            continue

        newer_map = deepcopy(new_map)

        fish_socre = newer_map[next_row][next_col]
        newer_map[row][col] = EMPTY
        newer_map[row][col + 1] = 0
        newer_map[next_row][next_col] = SHARK

        dfs(newer_map, score + fish_socre)


dfs(maps, res)

print(res)
