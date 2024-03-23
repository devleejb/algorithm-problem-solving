from sys import stdin

input = stdin.readline

N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]


answer = 0

for i in range(N):
    j = 1
    prev_height = maps[i][0]
    success = True
    already = {}
    while j < N:
        if prev_height != maps[i][j] and abs(prev_height - maps[i][j]) > 1:
            success = False
            break

        if prev_height - maps[i][j] == 1:
            # 내려가는 경우
            same_height_cnt = 0
            for k in range(j, j + L):
                if k < N and maps[i][j] == maps[i][k] and k not in already:
                    already[k] = True
                    same_height_cnt += 1
            if same_height_cnt != L:
                success = False
                break

        if prev_height - maps[i][j] == -1:
            # 올라가는 경우
            same_height_cnt = 0
            for k in range(j - L, j):
                if 0 <= k and prev_height == maps[i][k] and k not in already:
                    already[k] = True
                    same_height_cnt += 1
            if same_height_cnt != L:
                success = False
                break
        prev_height = maps[i][j]
        j += 1
    if success:
        answer += 1

for i in range(N):
    j = 1
    prev_height = maps[0][i]
    success = True
    already = {}
    while j < N:
        if prev_height != maps[j][i] and abs(prev_height - maps[j][i]) > 1:
            success = False
            break

        if prev_height - maps[j][i] == 1:
            # 내려가는 경우
            same_height_cnt = 0
            for k in range(j, j + L):
                if k < N and maps[j][i] == maps[k][i] and k not in already:
                    already[k] = True
                    same_height_cnt += 1
            if same_height_cnt != L:
                success = False
                break

        if prev_height - maps[j][i] == -1:
            # 올라가는 경우
            same_height_cnt = 0
            for k in range(j - L, j):
                if 0 <= k and prev_height == maps[k][i] and k not in already:
                    already[k] = True
                    same_height_cnt += 1
            if same_height_cnt != L:
                success = False
                break
        prev_height = maps[j][i]
        j += 1
    if success:
        answer += 1

print(answer)
