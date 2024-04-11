from sys import stdin

input = stdin.readline

fish_dr = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dc = [-1, -1, 0, 1, 1, 1, 0, -1]
shark_dr = [-1, 0, 1, 0]
shark_dc = [0, -1, 0, 1]

M, S = map(int, input().split())
maps = [[[] for _ in range(4)] for _ in range(4)]
smell_maps = [[0] * 4 for _ in range(4)]

for _ in range(M):
    row, col, dir = map(int, input().split())
    col -= 1
    row -= 1
    dir -= 1
    maps[row][col].append(dir)

shark_row, shark_col = list(map(lambda k: k - 1, map(int, input().split())))

for time in range(1, S + 1):
    new_maps = [[[] for _ in range(4)] for _ in range(4)]

    # 물고기 한 칸 이동
    for row in range(4):
        for col in range(4):
            for dir in maps[row][col]:
                moved = False
                for turn in range(8):
                    next_dir = dir - turn
                    if next_dir < 0:
                        next_dir = 8 + next_dir
                    next_row = row + fish_dr[next_dir]
                    next_col = col + fish_dc[next_dir]

                    # 격자 밖을 넘어감
                    if not (0 <= next_row < 4 and 0 <= next_col < 4):
                        continue

                    # 물고기의 냄새가 있는 칸
                    if smell_maps[next_row][next_col] >= time:
                        continue

                    # 상어가 있는 칸
                    if (shark_row, shark_col) == (next_row, next_col):
                        continue

                    new_maps[next_row][next_col].append(next_dir)
                    moved = True
                    break
                if not moved:
                    new_maps[row][col].append(dir)

    max_cnt_pos = (-1, (10, 10, 10))

    # 상어가 연속해서 3칸 이동
    for first in range(4):
        for second in range(4):
            for third in range(4):
                dirs = [first, second, third]
                now_shark_row = shark_row
                now_shark_col = shark_col
                available = True
                local_cnt = 0
                visited = {}

                for dir in dirs:
                    now_shark_row += shark_dr[dir]
                    now_shark_col += shark_dc[dir]

                    # 격자 밖을 넘어감
                    if not (0 <= now_shark_row < 4 and 0 <= now_shark_col < 4):
                        available = False
                        break

                    if (now_shark_row, now_shark_col) not in visited:
                        local_cnt += len(new_maps[now_shark_row][now_shark_col])
                        visited[(now_shark_row, now_shark_col)] = True

                if not available:
                    continue
                max_cnt_pos = max(
                    max_cnt_pos, (local_cnt, tuple(map(lambda k: -k, dirs)))
                )

    _, paths = max_cnt_pos
    paths = tuple(map(lambda k: -k, paths))

    for path in paths:
        shark_row += shark_dr[path]
        shark_col += shark_dc[path]

        if len(new_maps[shark_row][shark_col]) > 0:
            new_maps[shark_row][shark_col] = []
            smell_maps[shark_row][shark_col] = time + 2

    # 복제 마법 완료
    for row in range(4):
        for col in range(4):
            new_maps[row][col] += maps[row][col]

    maps = new_maps

res = 0
for row in range(4):
    for col in range(4):
        res += len(maps[row][col])

print(res)
