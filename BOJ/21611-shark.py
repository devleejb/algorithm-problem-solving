from sys import stdin
from collections import deque

input = stdin.readline

dx = [6, 2, 0, 4]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
now_pos = (N // 2, N // 2 - 1)
q.append(board[now_pos[0]][now_pos[1]])


for level in range(N // 2):
    # 아래
    for _ in range(level * 2 + 1):
        now_pos = (now_pos[0] + 1, now_pos[1])
        if board[now_pos[0]][now_pos[1]]:
            q.append(board[now_pos[0]][now_pos[1]])

    # 오른쪽
    for _ in range(level * 2 + 2):
        now_pos = (now_pos[0], now_pos[1] + 1)
        if board[now_pos[0]][now_pos[1]]:
            q.append(board[now_pos[0]][now_pos[1]])

    # 위
    for _ in range(level * 2 + 2):
        now_pos = (now_pos[0] - 1, now_pos[1])
        if board[now_pos[0]][now_pos[1]]:
            q.append(board[now_pos[0]][now_pos[1]])

    # 왼쪽
    for _ in range(level * 2 + (3 if level != N // 2 - 1 else 2)):
        now_pos = (now_pos[0], now_pos[1] - 1)
        if board[now_pos[0]][now_pos[1]]:
            q.append(board[now_pos[0]][now_pos[1]])

ops = [list(map(int, input().split())) for _ in range(M)]
res = 0

for dir, dis in ops:
    dir -= 1

    # 구슬 파괴
    if dx[dir] < len(q):
        q[dx[dir]] = 0
    prev_offset = dx[dir]

    for level in range(dis - 1):
        prev_offset = (
            (level * 2 + 3) * 2
            + (level * 2 + 3 - 2) * 2
            - (level * 2 + 3) // 2
            + ((level + 1) * 2 + 3) // 2
            + prev_offset
            + dx[dir]
        )
        if prev_offset < len(q):
            q[prev_offset] = 0

    # 구슬 폭발
    while True:
        explode = False
        new_q = deque([])
        prev_ball = -1
        prev_cnt = 0
        for ball in q:
            if ball == 0:
                continue
            if prev_ball == ball:
                prev_cnt += 1
            else:
                if prev_ball != -1:
                    if prev_cnt < 4:
                        for _ in range(prev_cnt):
                            new_q.append(prev_ball)
                    else:
                        explode = True
                        if prev_ball == 1:
                            res += prev_cnt
                        elif prev_ball == 2:
                            res += 2 * prev_cnt
                        elif prev_ball == 3:
                            res += 3 * prev_cnt

                prev_ball = ball
                prev_cnt = 1
        if prev_cnt < 4:
            if prev_ball != -1:
                for _ in range(prev_cnt):
                    new_q.append(prev_ball)
        else:
            if prev_ball == 1:
                res += prev_cnt
            elif prev_ball == 2:
                res += 2 * prev_cnt
            elif prev_ball == 3:
                res += 3 * prev_cnt
        q = new_q
        if not explode:
            break

    # 그룹 구슬 변환
    new_q = deque([])
    prev_ball = -1
    prev_cnt = 0
    for ball in q:
        if prev_ball == ball:
            prev_cnt += 1
        else:
            if prev_ball != -1:
                new_q.append(prev_cnt)
                new_q.append(prev_ball)
            prev_ball = ball
            prev_cnt = 1
    new_q.append(prev_cnt)
    new_q.append(prev_ball)

    while len(new_q) > N**2 - 1:
        new_q.pop()

    q = new_q


print(res)
