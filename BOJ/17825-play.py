from sys import stdin
from itertools import product

input = stdin.readline
dice_numbers = list(map(int, input().split()))
END = 31
points = [
    2,
    4,
    6,
    8,
    10,
    12,
    14,
    16,
    18,
    20,
    22,
    24,
    26,
    28,
    30,
    32,
    34,
    36,
    38,
    13,
    16,
    19,
    25,
    26,
    27,
    28,
    30,
    35,
    40,
    22,
    24,
]
graphs = {
    -1: [0],
    0: [1],
    1: [2],
    2: [3],
    3: [4],
    4: [5, 19],
    5: [6],
    6: [7],
    7: [8],
    8: [9],
    9: [10, 29],
    10: [11],
    11: [12],
    12: [13],
    13: [14],
    14: [15, 25],
    15: [16],
    16: [17],
    17: [18],
    18: [28],
    19: [20],
    20: [21],
    21: [22],
    22: [26],
    23: [22],
    24: [23],
    25: [24],
    26: [27],
    27: [28],
    28: [END],
    29: [30],
    30: [22],
}

perms = list(product(range(4), repeat=10))
res = 0
for perm in perms:
    score = 0
    pos = [-1, -1, -1, -1]
    for i in range(10):
        dice_idx = perm[i]
        cur_pos = pos[dice_idx]
        dice_num = dice_numbers[i]
        is_first = True
        moved = False
        while dice_num > 0 and cur_pos != END:
            moved = True
            if not is_first or len(graphs[cur_pos]) == 1:
                cur_pos = graphs[cur_pos][0]
            elif is_first and len(graphs[cur_pos]) == 2:
                cur_pos = graphs[cur_pos][1]

            is_first = False
            dice_num -= 1
            pos[dice_idx] = cur_pos

        if cur_pos != END and pos.count(cur_pos) > 1:
            break

        if moved:
            if cur_pos != END:
                score += points[cur_pos]
        else:
            break
    res = max(res, score)

print(res)
