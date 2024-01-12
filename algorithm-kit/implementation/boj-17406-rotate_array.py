# https://www.acmicpc.net/problem/17406
from sys import stdin, maxsize
from itertools import permutations

input = stdin.readline

N, M, K = map(int, input().split())
table_original = [list(map(int, input().split())) for _ in range(N)]
op_list = [list(map(int, input().split())) for _ in range(K)]
perm_list = permutations(op_list, len(op_list))
res = maxsize

for perm in perm_list:
    table = [[table_original[i][j] for j in range(M)] for i in range(N)]
    for op in perm:
        left_top = (op[0] - op[2] - 1, op[1] - op[2] - 1)
        right_bottom = (op[0] + op[2] - 1, op[1] + op[2] - 1)
        width = right_bottom[1] - left_top[1]
        height = right_bottom[0] - left_top[0]

        for i in range(op[2]):
            p = (left_top[0] + i, left_top[1] + i)
            temp = table[p[0]][p[1]]

            for j in range(0, width - i * 2):
                p = (p[0], p[1] + 1)
                temp2 = table[p[0]][p[1]]
                table[p[0]][p[1]] = temp
                temp = temp2

            for j in range(0, height - i * 2):
                p = (p[0] + 1, p[1])
                temp2 = table[p[0]][p[1]]
                table[p[0]][p[1]] = temp
                temp = temp2

            for j in range(0, width - i * 2):
                p = (p[0], p[1] - 1)
                temp2 = table[p[0]][p[1]]
                table[p[0]][p[1]] = temp
                temp = temp2

            for j in range(0, height - i * 2):
                p = (p[0] - 1, p[1])
                temp2 = table[p[0]][p[1]]
                table[p[0]][p[1]] = temp
                temp = temp2

    for i in range(N):
        res = min(sum(table[i]), res)

print(res)
