from sys import stdin

input = stdin.readline

SHARK = 1
SMELL = 2
EMPTY = 3

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, k = map(int, input().split())
initial_maps = [list(map(int, input().split())) for _ in range(N)]
maps = [[(EMPTY,) for _ in range(N)] for _ in range(N)]
dirs = list(map(int, input().split()))
dirs = [dir - 1 for dir in dirs]
priorities = [
    [list(map(lambda k: k - 1, map(int, input().split()))) for _ in range(4)]
    for _ in range(M)
]

for row in range(N):
    for col in range(N):
        if initial_maps[row][col] > 0:
            maps[row][col] = (
                SHARK,
                initial_maps[row][col] - 1,
                dirs[initial_maps[row][col] - 1],
            )

res = -1

for time in range(1, 1001):
    new_maps = [[(EMPTY,) for _ in range(N)] for _ in range(N)]

    # 냄새 감소
    for row in range(N):
        for col in range(N):
            if maps[row][col][0] == SMELL:
                _, shark_num, remain_time = maps[row][col]
                remain_time -= 1

                if remain_time == 0:
                    continue

                new_maps[row][col] = (SMELL, shark_num, remain_time)

    # 상어 이동
    for row in range(N):
        for col in range(N):
            if maps[row][col][0] != SHARK:
                continue
            _, shark_num, dir = maps[row][col]

            dir_priorites = priorities[shark_num][dir]

            next_dir = -1

            # 냄새가 없는 칸 찾기
            for target_dir in dir_priorites:
                next_row = row + dr[target_dir]
                next_col = col + dc[target_dir]

                if not (0 <= next_row < N and 0 <= next_col < N):
                    continue

                # 빈 칸인지 확인
                if maps[next_row][next_col][0] != EMPTY:
                    continue

                next_dir = target_dir
                break

            if next_dir == -1:
                # 냄새가 빈 칸이 없는 경우 -> 자신의 냄새가 있는 칸으로
                for target_dir in dir_priorites:
                    next_row = row + dr[target_dir]
                    next_col = col + dc[target_dir]

                    if not (0 <= next_row < N and 0 <= next_col < N):
                        continue

                    # 냄새 칸, 자신의 칸인지 확인
                    if (
                        maps[next_row][next_col][0] != SMELL
                        or maps[next_row][next_col][1] != shark_num
                    ):
                        continue

                    next_dir = target_dir
                    break

            next_row = row + dr[next_dir]
            next_col = col + dc[next_dir]

            # 상어 이동
            new_maps[next_row][next_col] = min(
                new_maps[next_row][next_col], (SHARK, shark_num, next_dir)
            )
            # 기존 자리에 냄새 남기기
            new_maps[row][col] = min(new_maps[row][col], (SMELL, shark_num, k - 1))

    maps = new_maps

    # 상어 수 카운트
    cnt = 0
    last_shark_num = -1
    for row in range(N):
        for col in range(N):
            if new_maps[row][col][0] == SHARK:
                cnt += 1
                last_shark_num = new_maps[row][col][1]

    if cnt == 1 and last_shark_num == 0:
        res = time
        break

print(res)
