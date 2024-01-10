# https://www.acmicpc.net/problem/21608
# 각 칸을 순회하며 좋아하는 학생이 인접한 수, 빈 칸의 수, 행의 번호, 열의 번호를 기록하고 이를 기준으로 정렬
from sys import stdin, maxsize

input = stdin.readline

N = int(input())
student_list = [list(map(int, input().split())) for _ in range(pow(N, 2))]
sit_list = [[0 for _ in range(N)] for _ in range(N)]
dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]


def calc_tuple(student, i, j):
    favorite_student_num_list = student[1:]
    favorite_cnt = 0
    empty_cnt = 0

    if sit_list[i][j] != 0:
        return (maxsize, maxsize, -maxsize, -maxsize)

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni and ni < N and 0 <= nj and nj < N:
            if sit_list[ni][nj] == 0:
                empty_cnt += 1
            elif sit_list[ni][nj] in favorite_student_num_list:
                favorite_cnt += 1

    return (-favorite_cnt, -empty_cnt, i, j)


def calc_satisfy(i, j):
    favorite_cnt = 0
    student_num = sit_list[i][j]
    favorite_student_num_list = student_list[student_num - 1][1:]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni and ni < N and 0 <= nj and nj < N:
            if sit_list[ni][nj] in favorite_student_num_list:
                favorite_cnt += 1

    if favorite_cnt == 0:
        return 0
    else:
        return pow(10, favorite_cnt - 1)


for student in student_list:
    min_tuple = (maxsize, maxsize, -maxsize, -maxsize)

    for i in range(N):
        for j in range(N):
            t = calc_tuple(student, i, j)
            min_tuple = min(min_tuple, t)

    sit_i = min_tuple[2]
    sit_j = min_tuple[3]

    sit_list[sit_i][sit_j] = student[0]

student_list.sort()

score = 0
for i in range(N):
    for j in range(N):
        score += calc_satisfy(i, j)


print(score)
