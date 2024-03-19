from sys import stdin
from bisect import bisect_left

input = stdin.readline

N, Q = map(int, input().split())
seqs = list(map(int, input().split()))
sight_positions = []

for i, seq in enumerate(seqs):
    if seq == 1:
        sight_positions.append(i)

res_list = []

current_postion = 0

for _ in range(Q):
    op = list(map(int, input().split()))

    if op[0] == 1:
        i = op[1]
        i -= 1
        idx = bisect_left(sight_positions, i)

        if idx != len(sight_positions) and sight_positions[idx] == i:
            sight_positions.pop(idx)
        else:
            sight_positions.insert(idx, i)
    elif op[0] == 2:
        x = op[1]
        current_postion = (current_postion + x) % N
    elif op[0] == 3:
        if len(sight_positions) == 0:
            res_list.append(-1)
            continue

        idx = bisect_left(sight_positions, current_postion)
        offset = 0

        if idx == len(sight_positions):
            offset = N - current_postion + sight_positions[0]
        else:
            offset = sight_positions[idx] - current_postion

        res_list.append(offset)

for res in res_list:
    print(res)
