from sys import stdin, maxsize
from bisect import bisect_left, bisect_right

input = stdin.readline

N = int(input())
groups = {}
problems_ordered_group = []
problems_ordered_difficulty = []

for _ in range(N):
    P, L, G = map(int, input().split())
    problems_ordered_group.append((G, L, P))
    problems_ordered_difficulty.append((L, P, G))
    groups[P] = (L, G)

problems_ordered_group.sort()
problems_ordered_difficulty.sort()

M = int(input())
res_list = []

for _ in range(M):
    inputs = list(input().split())
    op = inputs[0]

    if op == "recommend":
        G, x = map(int, inputs[1:])
        idx = 0
        if x == 1:
            idx = bisect_right(problems_ordered_group, (G, maxsize, maxsize)) - 1
        elif x == -1:
            idx = bisect_left(problems_ordered_group, (G, 0, 0))
        res_list.append(problems_ordered_group[idx][2])
    elif op == "recommend2":
        x = int(inputs[1])
        if x == 1:
            res_list.append(problems_ordered_difficulty[-1][1])
        elif x == -1:
            res_list.append(problems_ordered_difficulty[0][1])
    elif op == "recommend3":
        x, L = map(int, inputs[1:])
        idx = 0
        if x == 1:
            idx = bisect_left(problems_ordered_difficulty, (L, 0, 0))
        elif x == -1:
            idx = bisect_right(problems_ordered_difficulty, (L, 0, 0)) - 1

        if idx == -1 or idx == len(problems_ordered_difficulty):
            res_list.append(-1)
        else:
            res_list.append(problems_ordered_difficulty[idx][1])
    elif op == "add":
        P, L, G = map(int, inputs[1:])
        if P in groups and groups[P] != 0:
            prev_L, prev_G = groups[P]
            idx = bisect_left(problems_ordered_group, (prev_G, prev_L, P))
            problems_ordered_group.pop(idx)
            idx = bisect_left(problems_ordered_difficulty, (prev_L, P, prev_G))
            problems_ordered_difficulty.pop(idx)
        groups[P] = (L, G)
        idx = bisect_left(problems_ordered_group, (G, L, P))
        problems_ordered_group.insert(idx, (G, L, P))
        idx = bisect_left(problems_ordered_difficulty, (L, P, G))
        problems_ordered_difficulty.insert(idx, (L, P, G))
    elif op == "solved":
        P = int(inputs[1])
        L, G = groups[P]
        groups[P] = 0
        idx = bisect_left(problems_ordered_group, (G, L, P))
        problems_ordered_group.pop(idx)
        idx = bisect_left(problems_ordered_difficulty, (L, P, G))
        problems_ordered_difficulty.pop(idx)

for res in res_list:
    print(res)
