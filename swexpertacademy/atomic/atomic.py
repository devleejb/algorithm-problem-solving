import sys
sys.stdin = open("sample_input.txt", "r")
from math import sqrt

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

EMPTY = 0

mem_combs = [[] for _ in range(1001)]
def comb(length):
    global mem_combs
    combs = []
    for i in range(length):
        for j in range(i + 1, length):
            combs.append((i, j))
    mem_combs[length] = combs
    return combs

for test_case in range(1, T + 1):
    N = int(input())
    res = 0
    points = [list(map(int, input().split())) for _ in range(N)]
    combs = mem_combs[N]
    if len(combs) == 0:
        combs = comb(N)
    removed_cnt = 0

    while True:
        if removed_cnt == N or removed_cnt == N - 1:
            break
        # 충돌 여지가 있는지 확인
        can_meet = False
        for i, j in combs:
            if points[i] == EMPTY or points[j] == EMPTY:
                continue
            # 이동한 곳에서의 거리가 더 가까운 경우 탐색
            i_point_x = points[i][0]
            i_point_y = points[i][1]
            j_point_x = points[j][0]
            j_point_y = points[j][1]
            i_next_point_x = i_point_x + dx[points[i][2]]
            i_next_point_y = i_point_y + dy[points[i][2]]
            j_next_point_x = j_point_x + dx[points[j][2]]
            j_next_point_y = j_point_y + dy[points[j][2]]
            prev_dis = sqrt((i_point_x - j_point_x) ** 2 + (i_point_y - j_point_y) ** 2)
            next_dis = sqrt((i_next_point_x - j_next_point_x) ** 2 + (i_next_point_y - j_next_point_y) ** 2)

            if points[i][2] != points[j][2] and  next_dis <= prev_dis:
                can_meet = True

            if can_meet:
                break
        if not can_meet:
            break

        hashed_pos = {}
        hashed_prev_pos = {}

        for point in points:
            if point == EMPTY:
                continue
            hashed_prev_pos[(point[0], point[1])] = point

        # 이동 후 위치를 Hashing, 서로 엇갈리는 경우도 확인 필요
        for i, point in enumerate(points):
            if point == EMPTY:
                continue
            x, y, dir, k = point
            next_x = x + dx[dir]
            next_y = y + dy[dir]

            conflict = False

            # 서로 엇갈리는 경우
            if (next_x, next_y) in hashed_prev_pos:
                conflict_point = hashed_prev_pos[(next_x, next_y)]
                next_conflict_x = conflict_point[0] + dx[conflict_point[2]]
                next_conflict_y = conflict_point[1] + dy[conflict_point[2]]
                if (x, y) == (next_conflict_x, next_conflict_y):
                    conflict = True

            if conflict:
                next_x = x + dx[dir] / 2
                next_y = y + dy[dir] / 2

            if (next_x, next_y) not in hashed_pos:
                hashed_pos[(next_x, next_y)] = []
            hashed_pos[(next_x, next_y)].append((i))

        # 길이가 2 이상인 Bucket을 Clean Up
        for key in hashed_pos:
            ids = hashed_pos[key]

            # 충돌
            if len(ids) > 1:
                for idx in ids:
                    res += points[idx][3]
                    points[idx] = EMPTY
                removed_cnt += len(ids)
            else:
                for idx in ids:
                    points[idx] = [key[0], key[1], points[idx][2], points[idx][3]]
    print("#" + str(test_case), res)
