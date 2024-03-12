from sys import stdin, maxsize
from bisect import bisect_left, bisect_right

input = stdin.readline

N = int(input())
problems_ordered_difficulty = []
problem_difficulties = {}

for _ in range(N):
    P, L = map(int, input().split())
    problems_ordered_difficulty.append((L, P))
    problem_difficulties[P] = L

problems_ordered_difficulty.sort()

M = int(input())
res_list = []

for _ in range(M):
    inputs = list(input().split())
    op = inputs[0]

    if op == "recommend":
        x = int(inputs[1])
        if x == 1:
            res_list.append(problems_ordered_difficulty[-1][1])
        elif x == -1:
            res_list.append(problems_ordered_difficulty[0][1])
    elif op == "add":
        P, L = map(int, inputs[1:])
        problem_difficulties[P] = L
        idx = bisect_left(problems_ordered_difficulty, (L, P))
        problems_ordered_difficulty.insert(idx, (L, P))
    elif op == "solved":
        P = int(inputs[1])
        L = problem_difficulties[P]
        problem_difficulties[P] = 0
        idx = bisect_left(problems_ordered_difficulty, (L, P))
        problems_ordered_difficulty.pop(idx)

for res in res_list:
    print(res)
