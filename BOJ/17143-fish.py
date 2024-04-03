from sys import stdin
from copy import deepcopy

input = stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R, C, M = map(int, input().split())
maps = [[(0, 0, 0) for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1

    maps[r][c] = max(maps[r][c], (z, s, d))

res = 0

for col in range(C):
    # 잡아먹기
    for row in range(R):
        if maps[row][col] != (0, 0, 0):
            size, speed, dir = maps[row][col]
            maps[row][col] = (0, 0, 0)
            res += size
            break

    # 상어 이동
    new_maps = [[(0, 0, 0) for _ in range(C)] for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if maps[row][col] == (0, 0, 0):
                continue

            size, speed, dir = maps[row][col]

            row_dir_changed_cnt = 0
            col_dir_changed_cnt = 0

            if row + dr[dir] * speed < 0:
                row_dir_changed_cnt += 1
            if col + dc[dir] * speed < 0:
                col_dir_changed_cnt += 1

            next_row = abs(row + dr[dir] * speed)
            next_col = abs(col + dc[dir] * speed)
            # 0인 경우는 위, 1인 경우는 아래, 2인 경우는 오른쪽, 3인 경우는 왼쪽

            prev_row_add = next_row // R
            prev_col_add = next_col // C

            while (next_row + prev_row_add) // R != prev_row_add:
                prev_row_add = (next_row + prev_row_add) // R

            while (next_col + prev_col_add) // C != prev_col_add:
                prev_col_add = (next_col + prev_col_add) // C

            next_row += prev_row_add
            next_col += prev_col_add

            next_row = next_row % (2 * R)
            next_col = next_col % (2 * C)

            if next_row >= R:
                next_row = 2 * R - next_row - 1
                row_dir_changed_cnt += 1
            if next_col >= C:
                next_col = 2 * C - next_col - 1
                col_dir_changed_cnt += 1

            if row_dir_changed_cnt % 2:
                dir = (dir + 1) % 2
            if col_dir_changed_cnt % 2:
                dir = 2 + ((dir - 1) % 2)

            new_maps[next_row][next_col] = max(
                new_maps[next_row][next_col], (size, speed, dir)
            )

    maps = new_maps

print(res)
