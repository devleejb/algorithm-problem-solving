from sys import stdin, maxsize
from collections import deque
from math import sqrt

input = stdin.readline

ALIVE = 0
REST = 1
END = maxsize

N, M, P, C, D = map(int, input().split())
Rr, Rc = map(int, input().split())
Rr -= 1
Rc -= 1
santas = [0] * P
santa_scores = [0] * P

R_dr = [-1, -1, 0, 1, 1, 1, 0, -1]
R_dc = [0, 1, 1, 1, 0, -1, -1, -1]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(P):
    num, row, col = map(int, input().split())
    num -= 1
    row -= 1
    col -= 1
    santas[num] = (row, col, ALIVE)

for turn in range(M):
    # 루돌프의 움직임
    min_dis_santa = (maxsize, maxsize, maxsize)

    for santa in santas:
        row, col, status = santa

        if status == END:
            continue

        dis = sqrt((Rr - row) ** 2 + (Rc - col) ** 2)
        min_dis_santa = min(min_dis_santa, (dis, -row, -col))

    min_pos = (maxsize, maxsize, maxsize, maxsize)

    for dir in range(8):
        next_row = Rr + R_dr[dir]
        next_col = Rc + R_dc[dir]

        if not (0 <= next_row < N and 0 <= next_col < N):
            continue

        dis, row, col = min_dis_santa
        row = -row
        col = -col
        next_dis = sqrt((next_row - row) ** 2 + (next_col - col) ** 2)
        if min_pos[0] > next_dis:
            min_pos = (next_dis, next_row, next_col, dir)

    if min_pos[0] < min_dis_santa[0]:
        Rr, Rc, dir = min_pos[1], min_pos[2], min_pos[3]

        # 루돌프가 움직여서 충돌
        for i, santa in enumerate(santas):
            if not ((Rr, Rc, ALIVE) == santa or (Rr, Rc, REST) == santa):
                continue

            santa_scores[i] += C
            next_row = santas[i][0] + R_dr[dir] * C
            next_col = santas[i][1] + R_dc[dir] * C
            next_status = REST + 1

            if not (0 <= next_row < N and 0 <= next_col < N):
                santas[i] = (next_row, next_col, END)
            else:
                target = i
                santas[target] = (next_row, next_col, next_status)

                while True:
                    moved = False
                    for j, santa in enumerate(santas):
                        santa_row, santa_col, santa_status = santa

                        if santa_status == END:
                            continue

                        if j == target:
                            continue

                        if santa_row == next_row and santa_col == next_col:
                            next_row += R_dr[dir]
                            next_col += R_dc[dir]
                            st = santas[j][2]
                            if not (0 <= next_row < N and 0 <= next_col < N):
                                st = END
                            santas[j] = (next_row, next_col, st)
                            target = j
                            moved = True

                    if not moved:
                        break
            break

    # 산타의 움직임
    for i, santa in enumerate(santas):
        row, col, status = santa
        min_dis = maxsize
        min_dis_list = []
        now_dis = sqrt((row - Rr) ** 2 + (col - Rc) ** 2)

        if status == END:
            continue
        if status >= REST:
            santas[i] = (row, col, status - 1)
            continue

        for dir in range(4):
            next_row = row + dr[dir]
            next_col = col + dc[dir]

            if not (0 <= next_row < N and 0 <= next_col < N):
                continue

            next_dis = sqrt((next_row - Rr) ** 2 + (next_col - Rc) ** 2)
            if now_dis >= next_dis:
                min_dis_list.append((next_dis, dir))

        if not min_dis_list:
            continue

        min_dis_list.sort()

        for _, dir in min_dis_list:
            next_row = row + dr[dir]
            next_col = col + dc[dir]

            if (
                (next_row, next_col, ALIVE) in santas
                or (
                    next_row,
                    next_col,
                    REST,
                )
                in santas
                or (
                    next_row,
                    next_col,
                    REST + 1,
                )
                in santas
            ):
                continue

            santas[i] = (next_row, next_col, ALIVE)

            if next_row == Rr and next_col == Rc:
                # 산타가 움직여서 충돌
                santa_scores[i] += D
                santas[i] = (next_row, next_col, REST)

                next_row = next_row - dr[dir] * D
                next_col = next_col - dc[dir] * D

                if not (0 <= next_row < N and 0 <= next_col < N):
                    santas[i] = (next_row, next_col, END)
                else:
                    target = i
                    santas[i] = (next_row, next_col, santas[i][2])

                    while True:
                        moved = False
                        for j, santa in enumerate(santas):
                            santa_row, santa_col, santa_status = santa

                            if santa_status == END:
                                continue

                            if j == target:
                                continue

                            if santa_row == next_row and santa_col == next_col:
                                next_row -= dr[dir]
                                next_col -= dc[dir]
                                st = santas[j][2]
                                if not (0 <= next_row < N and 0 <= next_col < N):
                                    st = END
                                santas[j] = (next_row, next_col, st)
                                target = j
                                moved = True

                        if not moved:
                            break
            break

    for i, santa in enumerate(santas):
        if santa[2] != END:
            santa_scores[i] += 1


print(*santa_scores)
